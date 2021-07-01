  How To
==========
This documentation does not contain any information on how to setup the website system,
 just how to use it once it has been setup.
Please see the main [`/README.md`](../README.md) for those instructions.

## Directory
- [How To](#how-to)
  - [Directory](#directory)
  - [The Basics](#the-basics)
    - [The Directory Structure](#the-directory-structure)
      - [`_data/` dir](#_data-dir)
        - [`education.yml` file](#educationyml-file)
        - [`people.yml` file](#peopleyml-file)
        - [`software.yml` file](#softwareyml-file)
      - [`_posts/` dir](#_posts-dir)
        - [`_posts/__template__.md` file](#_posts__template__md-file)
      - [`education/` dir](#education-dir)
        - [`education/__template__.md` file](#education__template__md-file)


## The Basics
This is a website generation system, that utilizes [jekyll](https://jekyllrb.com)
 to allow for a static website to be generated from data and content files.
The system is pretty easy to use. 
Since it has been designed to hide,
 or at least remove the need to interact with, 
 the more complicated parts of the jekyll website build system.

All you need to know is what directories and files you can and should interact with. 
Sadly jekyll in order to ensure the safety of your files outside of this 
 project-directory/repo/website-root,
 does not allow you to configure it to use data files any directory above the `_config.yml` files.
This is for data safety but also means that you have to see all of the ugly behind the scenes files.

So I will give you a list of all of the directories you can touch, and what they do.

### The Directory Structure
- `/`
  - [`_data/`](#_data-dir)
    - [`education.yml`](#educationyml-file)
    - [`people.yml`](#peopleyml-file)
    - [`software.yml`](#softwareyml-file)
  - [`_posts/`](#_posts-dir)
    - [`__template__.md`](#_posts__template__md-file)
  <!-- - [`_site/`](#_site-dir) -->
  - [`education/`](#education-dir)
    - [`__template__.md`](#education__template__md-file)
    - [`ABOUT.md`](#educationaboutmd-file)
  - [`docs/`](#docs-dir)
  <!-- - [`downloads/`](#downloads-dir) -->
  - [`images/`](#images-dir)
  - [`people/`](#people-dir)
    - [`__template__.md`](#people__template__md-file)
    - [`ABOUT.md`](#peopleaboutmd-file)
  - [`publications/`](#publications-dir)
    - [`ABOUT.md`](#peopleaboutmd-file)
    - [`pubs.bib`](#pubsbib-file)
  - [`software/`](#software-dir)
    - [`__template__.md`](#software__template__md-file)
    - [`ABOUT.md`](#softwareaboutmd-file)
  - [`_config.yml`](#_configyml-file)
  - [`about.md`](#aboutmd-file)
  - [`contact.md`](#contactmd-file)

These directories and files are the only ones you should touch. 

> Unless you know what you are doing do not make any changes to files in the following directories:
> - `_includes/`
> - `_layouts/` 
> - `_site/` _(this is just the output directory)_
> - `.old/`
> - `assets/`
> Or any of the following files
> - `/Gemfile`
> - `/Gemfile.lock`
> - `/sitemap.xml`


#### `_data/` dir
This is the Jekyll data file directory. 
It is where you can put data files that you will use to dynamically build content for the website. 

You can add your own data files here to use in your posts and info pages.
If you would like to know more about jekyll data files I suggest you read the documentation for it
 on the jekyll website \[[link](https://jekyllrb.com/docs/datafiles/)\].

Overall though this is how you add people, software, and resources (education/talks) 
 to their respective pages.
See more about them in their respective sections.
But these 3 files do follow a pattern:
- The top level is a map/dict/obj
  - with a key that is the elements `id` 
    - see the respective section about `id`'s and `tags` for more info on this (TODO).
  - The value is another map/dict/obj

##### `education.yml` file
This file is where you put in data entries for the education/talks page.
It has a range of felids most information about this is in the header for that file.

##### `people.yml` file
This file is where you put in data entries describing the people working on the project 
 and goes on the people page.
It has a range of felids most information about this is in the header for that file.

##### `software.yml` file
This file is where you put in data entries describing the software made by the project 
 and goes on the software page.
It has a range of felids most information about this is in the header for that file.


#### `_posts/` dir
This directory is where you put your markdown (`.md`) files that are the blog posts for the website.
These files must be named `yyyy-mm-dd-title.md`.  
For more information see the section on posts (there is also a simple template in the file). (TODO)

##### `_posts/__template__.md` file
This is a simple template with junk contents, 
 the important thing contained in it is the jekyll front matter.
There are instructions on how to fill it out in the template.
Also check out the section on jekyll front matter. (TODO)


#### `education/` dir
This directory is where you can put supplementary info-post documents for the various 
 education, talks and other resources you wish to link.
There is another section to see with more info on info-post documents (TODO),
 that you should read for more info on these pages.

There is also an [`index.html`](../education/index.html) file in this directory,
 it contains delicate jekyll+liquid code for generating the 


##### `education/__template__.md` file
This is a simple template with junk contents, 
 the important thing contained in it is the jekyll front matter.
There are instructions on how to fill it out in the template.
Also check out the section on jekyll front matter. (TODO)