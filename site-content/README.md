  WebSite Content Instructions:
=================================

### Table of Contents
- [About](#about)
- [BibTeX Files](#bibtex-files)
  - [BibTeX File Requirements](#bibtex-file-requirements)
  - [Publication Entries](#publication-entries)
  - [Reference Entries](#reference-entries)
- [YAML Data Files](#yaml-data-files)
    - [YAML File Requirements](#yaml-file-requirements)
    - [Education Entries](#education-entries)
    - [People Entries](#people-entries)
    - [Software Entries](#software-entries)
- [Blog Posts](#blog-posts)

 About
========
This is the content management directory of the ${ProjName} project.
It is built on the Jekyll static website building system.
Please go and review the main [`README.md`](/README.md) 
 for information on how to configure your setup to use this system.

This system is configured to work for most hosting service including GitHub Pages, 
 with the cavitate that it must be built manually before pushing to the host service.
This is due to use of external scripts and uncommon Jekyll plugins.

This Site works by taking the information located in the `site-content` directory 
 and combining it with the nitty gritty details in the [`site-src`](../site-src) directory
 to build a semi-static website.

Information you need to put in to build the site goes in `pubs.bib` 
  and the files in the `data` directory.
Blog posts go in the posts directory, in either `_post` or `_draft` for their namesakes.
More information about these topics are below in their respective sections. 


 BibTeX Files    
================

 The primary use for the BibTeX files is for listing on the publication's "tab"/page information about this project's various publications.

There are two uses for BibTeX files:
 1. The primary use for the BibTeX files is for listing on the publication's "tab"/page
     information about this project's various publications.
    - These must be listed in the [`/site-content/pubs.bib`](./pubs.bib) file.
 2. The secondary use for BibTeX files, 
     is to be able to [add citations](https://github.com/inukshuk/jekyll-scholar#citations)
     with the `jekyll-scholar` plugin \[[doc](https://github.com/inukshuk/jekyll-scholar)\],
     in blog posts, 
     then [produce a Bibliography](https://github.com/inukshuk/jekyll-scholar#bibliographies) 
     at the end of said blog post.\
    _(see the [citations](#citations) sub-section 
     of the [Blog Post](#blog-post) section of this document for more info.)_
    - These can be any `.bib` file anywhere in the [`/site-content/`](./) directory,
       or any sub-directory of [`/site-content/`](./),
       but the main one will be [`/site-content/references.bib`](./refrences.bib).
    - In the end no matter where you put them all BibTeX entries will be combined 
       into one `.bib` file (even those in [`/site-content/pubs.bib`](./pubs.bib)),
       and therefore accessible anywhere on the site.
      - Therefore all BibTeX key's must be unique across all files.
 <!-- 2. Adding entries for the various information tabs of the website:
    - The people involved in the project, 
       on the people tab of the website.
    - The software created by this project, 
       on the software tab of the website.
    - The supplementary Educational materials, events & recordings that this project produces,
       or thinks would be useful for people interested in the project to know about, 
       on the Education/Talks tab of the website. -->

### BibTeX File Requirements
- Have the BibTeX File Extension (`.bib`)
  - Name of the file is irrelevant, 
     but we recommend using the existing files in [`/site-content/`](./) directory:
    - [`pubs.bib`](./pubs.bib) specifically and ONLY for BibTeX entries for publications
       made by this project.
    - [`references.bib`](./references.bib) for BibTeX entries that you might want to 
       [cite](#citations) in a "[blog post](#blog-post)" 
       or anywhere else on the site.
- Be syntactically valid BibTeX. \[[doc](http://www.bibtex.org/Format/)\]
  - All entries across all files must have unique "names"/IDs.
    - Entry names are always the first item in an entry, have no spaces, 
       are case insensitive, & do not have an associated key. \
       _i.e._
      ```bib
      @article{this-is-the-id, ...}
      ``` 
  - _**Note:** BibTeX is case insensitive for all key/field IDs,_
    _but will preserve letter case in their associated values._
- We, by convention, 
   request that you make any additional BibTeX files in your own sub-directory 
   of the [`/site-content/posts`](./posts) directory.
  This is to avoid any unessisary merge conflicts 
   that may arise from people trying to update the site at the same time. 


## Publication Entries
Publication entries **MUST** go in [`/site-content/pubs.bib`](./pubs.bib), 
 and they should follow the following conventions:
- Have an entry type **not** of `@COMMENT`, preamble `@PREAMBLE` (if you want it to work), 
   or any unofficial entry type for the citation standard the site is using. <br/>
   &emsp; _(Default: chicago-annotated-bibliography)_
- Have all of the required fields of the citation format the site is using. <br/>
   &emsp; _(Default: chicago-annotated-bibliography)_
  - Will ignore any fields that the citation format does not make use of.
  - The site has special purposes for the following fields that will be used 
     for rendering the info-box, even if the citation format does not support them:
    |      Field | Description   |  _¿Required?_ |
    |-----------:|---------------|:-------------:|
    | **`abstract`** | The publication's abstract or your own summary.<br/> This will be a single paragraph description that will be visible in the drop down info box.<br/> (_i.e._ the formatter surround it in `<p>` tags and strip the html out.) | _recommended_ |
    | **`note`** | A Note about the status of the publication, like if it is still under revision or if it has been retracted.<br/> This will be displayed at the top of the drop down info box, stylized to draw attention to it.      |       NO      |
    | **`year`** | Even if you have a `date` field, you will need this so that the webpage can sort the publication into a category on the website.     | YES |
> #### Example
> In [`/site-content/pubs.bib`](./pubs.bib):
> ```bib
> @article{taco-failamp,
>   author = {Ian Briggs and Arnab Das and Vishal Sharma and Mark Baranowski and
>   Sriram Krishnamoorthy and
>   Zvonimir Rakamaric and Ganesh Gopalakrishnan},
>   title = {FailAmp: Relativization Transformation
>            for Soft Error Detection in Structured Address
>            Generation},
>   journal = {ACM TACO},
>   note = {Under revision},
>   year = {2019},
>   abstract = {IDK I have not read it and the bib did not include a proper abstract, 
>               but the site does support abstracts <b>& even limited html !!</b> <br/>
>               &emps; <i>NOTE: supports any HTML tags that can go in a `p` tag (&lt;p&gt;)</i>
>              }
> }
> ```

## Reference Entries
These will be normal BibTeX entries found in any `.bib` file in the `/site-content` directory, 
 or any subdirectory therein.
This includes the [`/site-content/pubs.bib`](./pubs.bib) file.
You can use them to cite things & then generate bibliographies in blog posts 
 & other jekyll markdown pages, across the site
 _(see the [Citations](#citations) section for mote info)_.

There are no major requirements or special considerations for these beyond what is stated in 
 the [BibTeX File Requirements](#bibtex-file-requirements) section.


  YAML Data Files
===================
In order to maintain data structures to use for generating content we use (`.yml`) files.
That hold data formatted in the Yet Another Markup language (YMAL) 
 \[[syntax-spec](https://yaml.org/spec/1.2/spec.html)\] \[[tutorial](https://www.tutorialspoint.com/yaml/index.htm)\].
_Which is a proper superset of JSON, so if you get confused 
 you can just start typing JSON after any `<key>:` and it should work just fine._

These data files are use dto dynamically generate content for the site.
Currently there are three catagories of such info, and later in this file we will go over them in greater detail.
 1. [`/site-content/data/education.yml`](./data/education.yml): 
     this is for educational resources 
     that you would like to have show up on the education "tab"/page.
    Be they textbooks, seminars, activities, _etc._
    The main idea is that they help to educate visitors to the site about the topics
     this project works on.
    - please note this will not allow you to cite them, 
       for that you will also need to add an entry to a BibTeX file as described
       in the [BibTeX Files](#bibtex-files) section(s).
 2. [`/site-content/data/people.yml`](./data/people.yml): 
     this is for YOU.
    Meaning, this is where you should put in data about you for it to show up on the 
     people "tab"/page, which serves as the credits for the project.
    Here you will put in all of the requisite information to show up, as well as,
     extra information if you so choose, like GitHub and social links, _etc._
 3. [`/site-content/data/software.yml`](./data/software.yml):
      this is for any software that the project puts out.
    Will be rendered out on the Software "tab"/page.

In addition you can add any other 
 YAML (`.yml`/`.yaml`), JSON (`.json`), CSV (`.csv`), or TSV (`.tsv`) files
 you would like, to the [`/site-content/data/`](./data/) directory.
Then you can have access to the data in them with Jekyll's liquid comments,
 in any blog post or other page you create for the site
 _(see the [jekyll docs](https://jekyllrb.com/docs/) for more info on using 
 [data files](https://jekyllrb.com/docs/datafiles/), 
 & [liquid](https://jekyllrb.com/docs/liquid/))_.


### YAML File Requirements
- Be in the [`/site-content/data/`](./data/) directory.
- Be of a supported data file type:
  - Yet Another Markup Language (YAML `.yml`/`.yaml`)
  - JavaScript Object Language (JSON `.json`)
  - Comma-Separated Values (CSV `.csv`)
    - Must have a header row!
  - Tab-Separated Values (TSV `.tsv`)
    - Must have a header row!


## Education Entries:
_Entries about: events, resources, that are related to this project, that could provide supplementary information about the topic._

**Belongs in:** [`/site-content/data/education.yml`](./data/education.yml).

### Fields and Structure
_field names in **bold** are required to have._
- **`/`** (type: dict/obj) :: top level / root of the file.
  |  keys  |  values  |
  |:------:|:--------:|
  | the id to use when getting data in liquid  |  a dict/obj containing the information about the entry |
  - `abstract` (type: str/md) :: A brief explanation of the resource 
     ***(recommended not required)***
    - 1 paragraph max length.
    - Supports jekyll-liquid + markdown
      - You can use YAML Block scalar syntax (_i.e._ `|` & `>`) to allow multiline values.
        - Try to keep it short for better formatting.
  - **`author`** (type: str) :: The Authors name.
  - `cite_key` (type: str) :: The citation key for BibTeX entry.
    - If defined then a citation dropdown-info-box will be included
       _(similar to those used for the publications page)_.
  - **`date`** (type: str/date) :: The date of the resources publication 
     ***(requires at least the year to be present)***.
    - can be formatted as ruby timestamp or any other common date format. 
  - `icon` (type: str/url) :: a URL to an image that will be displayed 
     as an icon for the resource, try grabbing a logo associated with the resource.
  - `note` (type: str/md) :: A quick notice about the piece, like if it is a work in progress 
     or something like that.
    Will be formatted such that attention will be drawn to it.
    - Try to keep it real short for best formatting outcomes, like 2 sentences max.
    - supports jekyll-liquid + markdown, just like abstract _(don't go crazy with it)_.
  - **`title`** (type: str) :: The name of the Resource.
  - `url` (type: str/url) :: a link to the resource or reliant page about the resource.
     _(Highly recommended but not required)_
    


> #### Example:
> In [`/site-content/data/education.yml`](./people.bib)
> ```yml
> # ... content before ...
> aMAZEing:   # <-- this must be unique for the top level list of the file
>     title     : An aMAZEing Maze Solving Algorithm Tutorial
>     author    : Bobert Bently
>     url       : https://geeksforgeeks.com/maze-solving-algorithms/fakeURL
>     date      : 2020/07  # <-- must be a "well formatted" date 
>                          #      (aka: follow a common date formatting scheme)
>     abstract  : |
>                   A quick tutorial to get you started 
>                    on learning how to solve maze and other path finding problems.
>                   (Supports jekyll-liquid + markdown, but don't go too crazy with it.)
>     note      : "!! Work in Progress !!"  
>     cite_key  : education-aMAZEing  # <-- Requires there to be an entry in some .bib file with
>                                     #      a key that matches this value.
>                                     #     Will cause a citation dropdown entry to appear
>                                     #      like that in the publications page inside this
>                                     #      education item's info-box.   
> # ... content after ...
> ```


## People Entries:
_For: people who have contributed to the project, in a meaningful way._

**Belongs in:** [`/site-content/people.bib`](./people.bib).

### Fields and Structure
_field names in **bold** are required to have._
- **`/`** (type: dict/obj) :: top level / root of the file.
  |  keys  |  values  |
  |:------:|:--------:|
  | the id to use when getting data w/ liquid <br/> should be either a first name or something memorable and unique <br/> **!! no duplicate keys!!**  |  a dict/obj containing the information about the entry |
  - `abstract` (type: str/md) :: A short aside about the work the person 
     is responsible for in the project. 
     ***(recommended not required)***
    - 1 paragraph max length.
    - Supports jekyll-liquid + markdown
      - You can use YAML Block scalar syntax (_i.e._ `|` & `>`) to allow multiline values.
        - Try to keep it short for better formatting.
  - `degree` (type: str) :: The abbreviation for whatever the highest degree the person has.
    Will be appended after their name in some contexts.
    - Common options are: `Ph.D`, `MS`, or `BS` 
  - `links` (type: dict/obj) :: a collection of personal links.
    - `github` (type: str) :: the person's GitHub user name (just the username not a url).
    - `website` (type: str/url) :: a URL to the person's personal website.
    - `facebook` (type: str/url) :: a URL to a facebook profile, page, _etc._
    - `instagram` (type: str) :: the person's Instagram handle (just the handle not a url). 
    - `reddit` (type: str) :: the person's reddit username (just the username not a url). 
    - `twitter` (type: str) :: the person's Twitter handle (just the handle not a url). 
      - I recommend that you only use any of the social media links 
         if you act & post professionally on them.  
  - **`name`** (type: str | dict/obj) :: The persons name. (can either be a string or )
  - `pfp` (type: str/url) :: A URL to a picture to use as a profile picture.
    - I recommend using a professional photo you might see on a school faculty board,
       and staying away form avatars or recreational photos.
  - **`position`** (type: str/enum) :: The category that the person fits into 
     (used for organizing the people).
    - Must be one of the following: 
       `research staff`, `phd student`, `ms student`, `alumni`,
       `professor`, or `assistant professor`
  - `pronouns` (type: str) :: The persons preferred pronouns.
    - There are no restrictions here, but recommend you follow the format: 
       `he/him/his`, `she/her/hers`, or `they/them/theirs`.
       for consistency and formatting reasons.
    - This is scrubbed for HTML, _etc._
  - `title` (type: str) :: The persons official title for the project.
    

> #### Example:
> In [`/site-content/people.bib`](./people.bib)
> ```yml
> # ... content before ...
> bob101:  # <-- This must be unique for the top level list of the file
>                #     I recommend using a first name, if its unique for the project,
>                #       or screen name like your GitHub Username.  
>     name      : Bobert Bently
>     links     :
>         website   : https://bob101.github.io
>         github    : bob101
>     position  : ms student 
>     title     : Coffee Grabber Extraordinaire
>     pronouns  : they/them
>     pfp       : https://imgur.com/some-profesional-pic.png
>     abstract  : | 
>                   Resident expert at maze solving algorithms & fetching coffee.
>                   _Feel free to tag me in any issues with the aMAZEsoft project in it's repo._
> # ... content after ...
> ```


## Software Entries:
_Entries about: the software produced by this project._

**Belongs in:** [`/site-content/data/software.yml`](./data/software.yml).

### Fields and Structure
_field names in **bold** are required to have._
- **`/`** (type: dict/obj) :: top level / root of the file.
  |  keys  |  values  |
  |:------:|:--------:|
  | the id to use when getting data in liquid <br/> **!! Must be Unique !!**  |  a dict/obj containing the information about the entry |
  - `abstract` (type: str/md) :: A brief explanation of the software 
     ***(recommended not required)***
    - 1 paragraph max length.
    - Supports jekyll-liquid + markdown
      - You can use YAML Block scalar syntax (_i.e._ `|` & `>`) to allow multiline values.
        - Try to keep it short for better formatting.
  - **`author`** (type: str) :: The Author(s)' name.
  - `cite_key` (type: str) :: The citation key for BibTeX entry.
    - If defined then a citation dropdown-info-box will be included
       _(similar to those used for the publications page)_.
  - **`date`** (type: str/date) :: The date of the resources publication 
     ***(requires at least the year to be present)***.
    - can be formatted as ruby timestamp or any other common date format. 
  - `icon` (type: str/url) :: a URL to an image that will be displayed 
     as an icon for the resource, try grabbing a logo associated with the resource.
  - `image` (type: str/url) :: a URL to an image that will be displayed 
     in the info-box as a preview of the software.
  - `licence` (type: str) :: The licence the software has (is distributed under).
  - `licence_url` (type: str/URL) :: URL to the licence the software has (is distributed under).
  - `note` (type: str/md) :: A quick notice about the piece, like if it is a work in progress 
     or something like that.
    Will be formatted such that attention will be drawn to it.
    - Try to keep it real short for best formatting outcomes, like 2 sentences max.
    - supports jekyll-liquid + markdown, just like abstract _(don't go crazy with it)_.
  - **`title`** (type: str) :: The name of the Resource.
  - `url` (type: str/url) :: a link to the resource or relevant page about the resource.
     _(Highly recommended but not required)_
  - `repo` (type: str/url) :: a link to the software's repository 
      (use if separate different from `url`).
     _(Highly recommended but not required)_
  - `version` (type: str/num) :: the version identifier for the software.

<!-- |       Field | Description    |   Required?   |
|------------:|----------|:-------------:|
| **`notes`** | Brief description of what the software does. _(NOTE: supports [limited html](#limited-html))_    | _recommended_ |
| **`title`** | The name of the Software.  |      YES      |
|  **`type`** | This field tells the build script where your entry needs to go (should be `{software}`)    |      YES      |
|   **`url`** | Link to some site that provides more info and access to the software (like a GitHub, or dedicated website) | _recommended_ |
|  **`year`** | The year of publication/release of the software else this year (required for sorting entries).    |      YES      |
> #### Example:
> In [`/site-content/data/software.yml`](./data/software.yml)
> ```bib
> @COMMENT{software-amazeSoft   % <-- this must be unique across all .bib files in the site-content dir.
>   title = {aMazeSoft},
>   type = {software},
>   url = {https://goodSoft.github.io/aMazeSoft},
>   notes = {maze generating & solving software that **_WILL BLOW YOUR MIND !!_**},
>   year = {2020}
> }
> ``` -->

> #### Example:
> In [`/site-content/data/education.yml`](./people.bib)
> ```yml
> # ... content before ...
> aMAZEsoft:  # <-- this must be unique for the top level of the file
>     title     : An aMAZEing Maze Solving Algorithm Tutorial
>     author    : Bobert Bently
>     url       : https://github.com/bob101/aMAZEsoft
>     date      : 2020/07  # <-- must be a "well formatted" date 
>                          #      (aka: follow a common date formatting scheme)
>     abstract  : |
>                   An [aMAZEing](https://geeksforgeeks.com/maze-solving-algorithms/fakeURL)
>                    maze solving algorithm software project.
>                   (Supports jekyll-liquid + markdown, but don't go too crazy with it.)
>     note      : "!! Work in Progress (beta-release) !!"  
>     version   : Beta w172a  
>     licence   : MIT v2  
>     icon      : https://github.com/bob101/aMAZEsoft/images/logo.png
>     cite_key  : software-aMAZEsoft  # <-- Requires there to be an entry in some .bib file with
>                                     #      a key that matches this value.
>                                     #     Will cause a citation dropdown entry to appear
>                                     #      like that in the publications page inside this
>                                     #      education item's info-box.   
> # ... content after ...
> ```




  Blog Posts
==============

## Setup
Blog posts are in files with the name format `YYY-MM-DD-Your-Title.md`.
We request to avoid confusion and merge conflicts, that you only modify files in your own sub-directory of [`/site-content/`](./).

The file must start with a `yaml` header enclosed in `---`, of the following format.

```yml
---
layout: post
title: "Your Fancy Title"
author: "Who Wrote It"
---
```

The rest is mostly standard markdown. One blog post per file.

We recommend using uploading images and other multimedia to external sites like [imgur](https://imgur.com) then linking with static URL's from that hosting service.
If you know how to use Jekyll's liquid comments to build proper URLs to local resources, you can store images in the `/site-src/images` directory.
But as mentioned the external linking method would be best in most cases for simplicity, and ensuring efficient builds & data transfer and storage restrictions on GitHub.

> #### Advanced
> The site uses [jekyll](https://jekyllrb.com/) to build static websites from dynamic data.\
> Therefore, if you know how to use 
>  [jekyll's liquid template syntax](https://jekyllrb.com/docs/liquid/)
>  you can make more dynamic webpages.\
> This also means that despite this being markdown, unlike most places you can use markdown,
>  you can insert custom javascript, so long as it is client side only.\
> Finally this means that you can use jekyll plugins to improve your content, 
>  though unless you know how to use jekyll and have the permissions of the site maintainer,
>  you should only use the plugins currently installed on the site.
> Which if you know jekyll you should be able to figure out what ones are installed.





  END
=======
