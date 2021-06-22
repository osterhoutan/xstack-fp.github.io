  WebSite Content Instructions:
=================================

### Table of Contents
- [BibTeX Files](#bibtex-files)
  - [File Requirements](#file-requirements)
  - [Publication Entries](#publication-entries)
  - [Other Entries](#otehr-entries)
    - [Education Entries](#education-entries)
    - [People Entries](#people-entries)
    - [Software Entries](#software-entries)
- [Blog Posts](#blog-posts)

<!-- This repo https://gitlab.com/ganeshutah/cpu-website.git is the one
into which CPU faculty members (or their designees) can enter
their latest pubs so that it is automatically populated into the CPU
website.

* You (or your designee) may please ask for permissions to push into
  this repo by sending ganesh AT cs.utah.edu an email.

* How to update the CPU website: just create a bibtex entry in your
  directory, and push! Details below.

* Directories have been created for everyone:

* The contents of ganesh/ may be taken as an example of how to go about things. 
  Why don't you look at its *.bib files as examples? Below, under "BIBTEX FILE DESCRIPTIONS",
  I describe these bib file formats.

* The file name you choose does not matter; however, you must have a ".bib" extension

  - So foo.bib MyPubs.bib etc. are allowed
  - Feel free to split your bib entries across multiple files -->


 BibTeX Files    
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

### File Requirements
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


## Publication Entries
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

## Other Entries
Each of these is other types of entries will go in separate "tabs"/pages on the website.
Following similar methodologies, with only slight variations.
This methodology takes advantage of the BibTeX format to enforce regularity on these entries.

#### Requirements
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

|      Kind | Destination "Tab"/Page |        Recommended File       |  Type Field | Allowed Fields                                              | Description                                                                                                                      |
|----------:|:----------------------:|:-----------------------------:|:-----------:|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Education |     Education/Talks    | `/site-content/education.bib` | `education` | `title`, `url`, `author`, `year`, `month`, `notes`, `type`  | Entries about: events, resources, that are related to this project, that could provide supplementary information about the topic. |
|    People |         People         |   `/site-content/people.bib`  |   `people`/`person`  | `title`, `url`, `notes`, `type`                             | Entries about: people who have contributed to the project, in a meaningful way.                                                  |
|  Software |        Software        |  `/site-content/software.bib` |  `software` | `title`, `url`, `notes`, `year`, `type`                             |  Entries about: the software produced by this project.                 |

&emsp;&emsp; \* \- descriptions about what the _Allowed Felids_ are provided in the section about each kind.

### Education Entries:
_Entries about: events, resources, that are related to this project, that could provide supplementary information about the topic._

**Belongs in:** `/site-content/education.bib`.

|        Field | Description                                                                              |   Required?  |
|-------------:|------------------------------------------------------------------------------------------|:------------:|
| **`author`** | The primary person credited with the work                                                |      YES     |
|  **`month`** | The month the event is happening in, or the work was published _(can be abbreviation, name, or numeric)_ |      NO      |
|  **`notes`** | Brief but important details about the work or event (keep ~2 sentences)                  | _recommended_ |
|  **`title`** | The name of the work                                                                     |      YES     |
|   **`type`** | This field tells the build script where your entry needs to go (should be `{education}`) |      YES     |
|    **`url`** | Link to the resource or event, or at least to a place with more info.                    | _recommended_ |
|   **`year`** | The year of publication/release/occurrence else this year (required for sorting entries).           |      YES     |


> #### Example:
> In `/site-content/people.bib`
> ```bib
> @COMMENT{education-aMAZEing   % <-- this must be unique across all .bib files in the site-content dir.
>   title = {aMAZEing maze solving algorithm tutorial},
>   type = {education},
>   url = {https://geeksforgeeks.com/maze-solving-algorithms/fakeURL},
>   notes = {a quick tutorial to get you started on learning how to solve maze and other path finding problems.},
>   year = 2016,
>   month = feb
> }
> ```


### People Entries:
_Entries about: people who have contributed to the project, in a meaningful way._

**Belongs in:** `/site-content/people.bib`.

|       Field | Description                                                                                                                                                                                                       |   Required?  |
|------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------:|
| **`notes`** | The person's position, role, and/or responsibilities (must include somewhere in it one of the following _(case insensitive)_: `research staff`, `phd student`, `ms student`, `alumni`, `professor`, or `assistant professor`) _(NOTE: supports limited markdown)_  |      YES     |
| **`title`** | The name of the person.                                                                                                                                                                                           |      YES     |
|  **`type`** | This field tells the build script where your entry needs to go (should be `{people}` or `{person}`)                                                                                                               |      YES     |
|   **`url`** | Link to some site that the person wants associated with themselves (_i.e._ a personal website, GitHub, _etc._)                                                                                                    | _recommended_ |

> #### Example:
> In `/site-content/people.bib`
> ```bib
> @COMMENT{person-bob   % <-- this must be unique across all .bib files in the site-content dir.
>   title = {Bobert Bently},
>   type = {person},
>   url = {https://bob101.github.io},
>   notes = {ms student + _coffee grabber **Extraordinaire**_ \[[insta](https://instgram.com/profiles/bob101)\]}
> }
> ```


### Software Entries:
_Entries about: the software produced by this project._

**Belongs in:** `/site-content/software.bib`.
|       Field | Description                                                                                                |   Required?   |
|------------:|------------------------------------------------------------------------------------------------------------|:-------------:|
| **`notes`** | Brief description of what the software does. _(NOTE: supports limited markdown)_                         | _recommended_ |
| **`title`** | The name of the Software.                                                                                  |      YES      |
|  **`type`** | This field tells the build script where your entry needs to go (should be `{software}`)                    |      YES      |
|   **`url`** | Link to some site that provides more info and access to the software (like a GitHub, or dedicated website) | _recommended_ |
|  **`year`** | The year of publication/release of the software else this year (required for sorting entries).             |      YES      |

> #### Example:
> In `/site-content/software.bib`
> ```bib
> @COMMENT{software-amazeSoft   % <-- this must be unique across all .bib files in the site-content dir.
>   title = {aMazeSoft},
>   type = {software},
>   url = {https://goodSoft.github.io/aMazeSoft},
>   notes = {maze generating & solving software that **_WILL BLOW YOUR MIND !!_**},
>   year = {2020}
> }
> ```




  Blog Posts
==============

## Setup
Blog posts are in files with the name format `YYY-MM-DD-Your-Title.md`.
We request to avoid confusion and merge conflicts, that you only modify files in your own sub-directory of `/site-content/`.

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
