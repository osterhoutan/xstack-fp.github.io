  WebSite Content Instructions:
=================================

This repo https://gitlab.com/ganeshutah/cpu-website.git is the one
into which CPU faculty members (or their designees) can enter
their latest pubs so that it is automatically populated into the CPU
website.

* You (or your designee) may please ask for permissions to push into
  this repo by sending ganesh AT cs.utah.edu an email.

* How to update the CPU website: just create a bibtex entry in your
  directory, and push! Details below.

* Directories have been created for everyone:

  - ganesh/
  - hsundar/	
  - mb/
  - mhall/
  - zvonimir/

* The contents of ganesh/ may be taken as an example of how to go about things. 
  Why don't you look at its *.bib files as examples? Below, under "BIBTEX FILE DESCRIPTIONS",
  I describe these bib file formats.

* The file name you choose does not matter; however, you must have a ".bib" extension

  - So foo.bib MyPubs.bib etc. are allowed
  - Feel free to split your bib entries across multiple files


 BibTeX Files:    
=================

There are two uses for BibTeX files:
 1. Adding citations for this project's various publications.
 2. Adding entries for the various information tabs of the website:
    - The people involved in the project, 
       on the people tab of the website.
    - The software created by this project, 
       on the software tab of the website.
    - The supplementary Educational materials, events & recordings that this project produces,
       or thinks would be useful for people interested in the project to know about, 
       on the Education/Talks tab of the website.

### File requirements:
- Have the BibTeX File Extension (`.bib`)
  - Name of the file is irrelevant, 
     but we recommend using the existing files in `/site-content/` directory:
    - `pubs.bib` for BibTeX entries for publications.
    - `software.bib` for BibTeX entries meant for the software tab.
    - `education.bib` for BibTeX entries meant for the education/talks tab.
    - `people.bib` for the BibTeX entries meant for the people tab.
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
   request that you make any BibTeX files in your own sub-directory 
   of the `/site-content/` directory.
  This is to avoid any unessisary merge conflicts 
   that may arise from people trying to update the site at the same time. 


## Publication entries
Publication entries should go in `/site-content/pubs.bib`, 
 and they should follow the following conventions:
- Have an entry type **not** of `@COMMENT`, preamble `@PREAMBLE`, 
   or any unofficial entry type for the citation standard the cite is using.
   _(Default: chicago-annotated-bibliography)_
> #### Example
> In `/site-content/pubs.bib`:
> ```bib
>  ...
> @article{taco-failamp,
>   author = {Ian Briggs and Arnab Das and Vishal Sharma and Mark Baranowski and
>   Sriram Krishnamoorthy and
>   Zvonimir Rakamaric and Ganesh Gopalakrishnan},
>   title = {FailAmp: Relativization Transformation
>            for Soft Error Detection in Structured Address
>            Generation},
>   journal = {ACM TACO},
>   CATEGORY = {Parallel},
>   note = {Under revision},
>   year = 2019
> }
>  ...
> ```

## Other Entries:
Each of these is other types of entries will go in separate "tabs"/pages on the website.
Following similar methodologies, with only slight variations.
This methodology takes advantage of the BibTeX format to enforce regularity on these entries.

#### Requirements:
- All entries that will go on their own designated tabs on the website, 
   must be of the entry type `@COMMENT`, 
   as to not upset any BibTeX parser with custom field entries.
- They type of entry should be specified inside a comma separated list under the `TYPE` key.
  - Lists in BibTeX take the form `{1,2,3,4,...}`.
  - If the type value associated with a particular page type exists,
     in the list, it will end up that "tab"/page.
    - This means that an entry can go on multiple "tabs"/pages, 
       but likely this is unlikely to be what you want to happen.
- Other requirements and conventions are specific to the type of entry being entered.



### People Entries:

In the `@COMMENT` type entries, you may additionally have these fields with special
significance:

* `TYPE = {Education, ...}` : This entry ends up under the Education tab

* `TYPE = {Software, ...}` : This entry ends up under the Software tab

* `TYPE = {People, ...}` : This entry ends up under the People tab

Blog Posts
==========

## Setup
Blog posts are in files with the name fromat `YYY-MM-DD-Your-Title.md`.
We request to avoid confusion and merge conflicts, that you only modify files in your own sub-directory of `/site-content/`.

The file must start with a `yaml` header enclosed in `---`, of the following format.

```yml
---
layout: post
title: "Your Fancy Title"
author: "Who Wrote It"
---
```




The rest is standard markdown. One blog post per file.




  END
=======
