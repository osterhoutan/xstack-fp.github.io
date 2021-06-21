#!/usr/bin/env python3


import re
import sys
import glob
import os

from os import path
from pprint import pprint


def error(text):
    print(text, file=sys.stderr)
    sys.exit(-1)



field_names = [
    "author",
    "title",
    "booktitle",
    "month",
    "year",
    "url",
    "crossref",
    "type",
    "notes",
    "category",
]

def enter(entry, field, value):
    field = field.strip().lower() # normalize keys
    # replace html links with markdown links
    value = re.sub("<a\s+href\s*=([^>]+)>([^<]+)</a>", r"[\2](\1)", value)
    value = re.sub("and\s+and", "and", value)
    value = value.replace("``", '"')
    value = value.replace("''", '"')
    value = value.strip()         # remove extra whitespace from value
    if value[0] == "{":           # if enclosed in {} remove them
        value = value[1:]
    if value[-1] == ",":          # if in the middle of a list remove the ,
        value = value[:-1]
    if value[-1] == "}":          # if enclosed in {} remove them
        value = value[:-1]
    value = value.strip()         # remove extra whitespace
    entry[field] = value


def string_to_entry(text, origin):
    entry = {"raw" : text,     # keep unmodified for debugging
             "origin": origin} # also remember the user who added the file
    lines = text.split("\n")

    # look for the entry's @<at>{<entry_name>
    at_name_match = re.match("@([\w_\-]+)\s*{\s*([\w:_\-]+)", lines[0])
    if at_name_match == None:
        error("unable to extract entry @ type and name from: '{}'".format(text))
    entry["at"] = at_name_match.group(1).strip().lower()
    entry["entry_name"] = at_name_match.group(2).strip()

    curly_braces = 1
    state = 0
    field = ""
    value = ""
    for line in lines[1:]:
        line = line.strip()

        # skip blank lines
        if line == "":
            continue

        # looking for a new {} = {}, field
        if state == 0:
            # there should be no partial field, value pairs floating around
            assert field == "", field
            assert value == "", value

            # look for "="
            try:
                eqi = line.index("=")
            except ValueError:
                # None was found, something might be wrong
                if line == "}":
                    # the closing '}' was on its own line with the prior line
                    #  ending in a ','
                    state = 1
                    continue
                # Something is wrong
                print("Warning: Abrubt end on raw entry:\n{}".format(text))
                print("Stopped parsing on line:\n{}".format(line))
                print("Data scraped:\n{}".format(entry_to_string(entry)))
                break

            # grab out field and value, note value may be incomplete
            field = line[0:eqi]
            value = line[eqi+1:].strip()
            if "=" in value and "http" not in value:
                print("Warning: Two '=' found on one line: '{}'".format(line))

            # single line values that start with '{' must end with '},'
            if value[0] == "{" and line[-2:] == "},":
                enter(entry, field, value)
                field = ""
                value = ""
                continue

            # we assume that a single line ending in a ',' contains
            #  a complete field = value, if the value does not start with '{'
            if value[0] != "{" and line[-1] == ",":
                enter(entry, field, value)
                field = ""
                value = ""
                continue

            # we assume that a single line ending in a } contains
            #  a complete "field = value" and is the last field in the entry
            if line[-1] == "}":
                state = 2
                continue

            # we got a field and a partial value, look for the rest of the value
            value = value +  " "
            state = 3
            continue


        # there should be nothing left to read in this state
        if state == 1:
            if line != "}":
                print("Extra: '{}'".format(line))
                print("Warning: Extra data at end of entry: \n{}".format(text))


        # remember field, value and assume this was the last one
        if state == 2:
            enter(entry, field, value)
            field = ""
            value = ""
            state = 1
            continue


        # have partial value looking for more
        if state == 3:
            # concat on the rest of the value
            value = value + line

            # we assuma a multi-line value that has '},' on the end of a line
            #  also ends that value
            if line[-2:] == "},":
                enter(entry, field, value)
                field = ""
                value = ""
                state = 0
                continue

            # we assuma a multi-line value that has '}' on the end of a line
            #  also ends that value and is the last field in the entry
            if line[-1] == "}":
                state = 2
                continue

            # there is more to this multiline value
            value = value.strip() +  " "
            state = 3
            continue

    # there might be a hanging field, value pair
    if field != "":
        enter(entry, field, value)

    if entry.get("year", "") == "":
        entry["year"] = "unknown"

    return entry




def entry_to_string(entry):
    string = "@{}{{{}".format(entry["at"], entry["entry_name"])

    # add the fields we know in the order we decided
    for category in field_names:
        data = entry.get(category, None)
        if data != None:
            string += ",\n  {} = {{{}}}".format(category, data)

    # add all other fields in sorted order
    for field in sorted(entry):
        if field not in field_names and field not in {"at", "entry_name"}:
            string += ",\n  {} = {{{}}}".format(field, entry[field])

    string += "\n}\n"

    return string




def read_entries(filename, origins):
    # find the origin directory
    rest, origin = path.split(path.dirname(filename))
    while origin not in origins:
        rest, origin = path.split(path.dirname(rest))

    # grab all data
    with open(filename, "r") as f:
        lines = f.readlines()

    # strip comments
    lines = [line for line in lines if not line.strip().startswith("%")]

    # push together into one string
    text = "\n" + "".join(lines)

    # split on "<newline>@" (this may be brittle)
    raw_entries = ["@"+e for e in text.split("\n@") if e.strip() != ""]

    # convert to entry dicts
    entries = [string_to_entry(e, origin) for e in raw_entries]

    return entries




def read_all_entries(filenames, origins):
    entries:list = list()
    for filename in filenames:
        # grab all entries in each file
        print("Reading: {}".format(filename))
        new_entries = read_entries(filename, origins)

        # check that these entries do not have the same name as existing entries
        removable_entries = list()
        for ne in new_entries:
            overlap = [e for e in entries if e["entry_name"] == ne["entry_name"]]
            if len(overlap) != 0:
                print("Duplicate entries named '{}'".format(ne["entry_name"]))
                removable_entries.append(ne)

        for r in removable_entries:
            new_entries.remove(r)

        # add the new entries to the list of all entries
        entries.extend(new_entries)

    return entries



def write_out_people(entries, filename):
    # filter to only comment entries
    comment_type = [e for e in entries if e["at"] == "comment"]
    # filter those to only things marked as people or person
    people = [e for e in comment_type if
              ("person" in e.get("type", "").lower()
               or "people" in e.get("type", "").lower())]

    # grab Ganesh
    ganesh = [e for e in people if e.get("title", "") == "Ganesh Gopalakrishnan"]
    # grab professors
    professors = [e for e in people if
                  (e.get("title", "") != "Ganesh Gopalakrishnan"
                   and e.get("notes", "").lower().count("professor") >= 1
                   and e.get("notes", "").lower().count("assistant") == 0)]
    # grab assistant_professors
    assistant_professors = [e for e in people if
                            (e.get("title", "") != "Ganesh Gopalakrishnan"
                             and e.get("notes", "").lower().count("professor") >= 1
                             and e.get("notes", "").lower().count("assistant") >= 1)]
    # grab researchers
    ras = [e for e in people if
            e.get("notes", "").lower().count("research staff") >= 1]
    # grab PhDs
    phds = [e for e in people if
            e.get("notes", "").lower().count("phd student") >= 1]
    # grab masters
    mss = [e for e in people if
            e.get("notes", "").lower().count("ms student") >= 1]
    # grab alumns
    alumns = [e for e in people if
            e.get("notes", "").lower().count("alumni") >= 1]

    # sort by name (may need to sort by last name)
    professors.sort(key=lambda e:e["title"].split()[-1])
    ras.sort(key=lambda e:e["title"].split()[-1])
    phds.sort(key=lambda e:e["title"].split()[-1])
    mss.sort(key=lambda e:e["title"].split()[-1])
    alumns.sort(key=lambda e:e["title"].split()[-1])

    # join in order
    faculty = ganesh + professors + assistant_professors
    students =  ras + phds + mss + alumns
    with open(filename, "w") as f:
        # include the frontmatter
        f.write("---\n")
        f.write("layout: page\n")
        f.write("title: People\n")
        f.write("---\n\n")

        f.write("# Faculty\n")
        for s in faculty:
            entries.remove(s) # this entry has been consumed

            # use hyperlink if present
            if s.get("url", "") == "":
                f.write("* {}, {}\n\n\n".format(s["title"], s["notes"]))
            else:
                f.write("* [{}]({}), {}\n\n\n".format(
                    s["title"], s["url"], s["notes"]))

        f.write("# Students\n")
        for s in students:
            entries.remove(s) # this entry has been consumed

            # use hyperlink if present
            if s.get("url", "") == "":
                f.write("* {}, {}\n\n\n".format(s["title"], s["notes"]))
            else:
                f.write("* [{}]({}), {}\n\n\n".format(
                    s["title"], s["url"], s["notes"]))




month_to_ord = {
    "unknown"   : 0,
    "january"   : 1,
    "jan"       : 1,
    "february"  : 2,
    "feb"       : 2,
    "march"     : 3,
    "mar"       : 3,
    "april"     : 4,
    "may"       : 5,
    "jun"       : 6,
    "june"      : 6,
    "jul"       : 7,
    "july"      : 7,
    "august"    : 8,
    "aug"       : 8,
    "september" : 9,
    "sept"      : 9,
    "october"   : 10,
    "oct"       : 10,
    "november"  : 11,
    "nov"       : 11,
    "december"  : 12,
    "dec"       : 12,
}
ord_to_month = {
    1  : "January",
    2  : "February",
    3  : "March",
    4  : "April",
    5  : "May",
    6  : "June",
    7  : "July",
    8  : "August",
    9  : "September",
    10 : "October",
    11 : "November",
    12 : "December",
}

def write_out_publications(entries, filename):
    # filter to only entries of not of types COMMENT or PREAMBLE
    publications = [e for e in entries if
                    e["at"].lower() not in {"comment","preamble"}]

    with open(filename, "w") as f:
        for p in publications:
            raw = p["raw"]
            raw = re.sub("url *= *{([^}]*)}", r'url = {<a href="\1">link</a>}', raw)
            raw = raw.replace('.pdf">link', '.pdf">pdf')
            f.write(raw)
            entries.remove(p)


def write_out_education(entries, filename):
    # filter to only comment entries
    comment_type = [e for e in entries if e["at"] == "comment"]
    # filter those to only education entries
    education = [e for e in comment_type if
                 "education" in e.get("type", "").lower()]

    # get unique years sorted from most recent to oldest
    years = [e["year"] for e in education]
    years = set(years)
    years = list(years)
    years.sort(reverse=True)

    with open(filename, "w") as f:
        # include the frontmatter
        f.write("---\n")
        f.write("layout: page\n")
        f.write("title: Education/Talks\n")
        f.write("---\n\n")

        for y in years:
            # add header for year
            f.write("## {}\n\n".format(y))

            # grab this year's entries, sort by month from most recent to oldest
            #  entries with no month are considered the most recent
            this_year = [e for e in education if e["year"] == y]
            this_year.sort(key=lambda e: month_to_ord[e.get("month", "unknown").lower()],
                           reverse=True)
            for p in this_year:
                entries.remove(p)  # this entry has been consumed
                education.remove(p)  # this entry has been consumed

                month_num = month_to_ord[p.get("month", "unknown").lower()]

                # use hyperlink if present
                if p.get("url", "") == "":
                    f.write("* {}  \n".format(p["title"]))
                else:
                    f.write("* {} [\[LINK\]]({})  \n".format(p["title"], p["url"]))

                # output author
                f.write("   {}  \n".format(p["notes"]))
                f.write("   {}  \n".format(p["author"]))

                # output date using month if present
                if month_num == 0:
                    f.write("    {}\n\n".format(p["year"]))
                else:
                    f.write("    {}, {}\n\n".format(ord_to_month[month_num], p["year"]))




def write_out_software(entries, filename):
    # filter to only comment entries
    comment_type = [e for e in entries if e["at"] == "comment"]
    # filter those to only software entries
    software = [e for e in comment_type if
                "software" in e.get("type", "").lower()]

    # sort by name
    software.sort(key=lambda e: e["title"])

    with open(filename, "w") as f:
        # include the frontmatter
        f.write("---\n")
        f.write("layout: page\n")
        f.write("title: Software\n")
        f.write("---\n\n")

        for s in software:
            entries.remove(s) # this entry has been consumed

            # use hyperlink if present
            if s.get("url", "") == "":
                f.write("* {}  \n".format(s["title"]))
            else:
                f.write("* [{}]({})  \n".format(s["title"], s["url"]))

            # output description
            if s.get("notes", None) != None:
                f.write("  {}\n\n".format(s["notes"]))








def main(argv):
    if not (len(argv) == 3 or (len(argv) == 4 and argv[3] == "-cpu")):
        print("Usage: {} backend_git content_git [-cpu]".format(argv[0]))
        print("  backend_git: root directory of the git with the jekyll system setup")
        print("  content_git: root directory of the git with bib and md files to populate into the backend_git")
        print("  -cpu: flag to filter content for the cpu website")
        return -1
    
    backend_git = argv[1]
    content_git = argv[2]

    origins = {o for o in os.listdir(content_git) if path.isdir(path.join(content_git,o))}
    origins.add('')
    filenames = glob.iglob(path.join(content_git, "**/*.bib"), recursive=True)
    entries = read_all_entries(filenames, origins)

    software_md = path.join(backend_git, "software.md")
    publications_md = path.join(backend_git, "_bibliography/references.bib")# "publications.md")
    education_md = path.join(backend_git, "education.md")
    people_md = path.join(backend_git, "people.md")

    write_out_people(entries, people_md)
    write_out_publications(entries, publications_md)
    write_out_education(entries, education_md)
    write_out_software(entries, software_md)

    if len(entries) != 0:
        print("Entries with no home:")
        for e in entries:
            print(entry_to_string(e))


if __name__ == "__main__":
    main(sys.argv)
