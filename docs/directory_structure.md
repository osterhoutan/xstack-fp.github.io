  The Directory Structure
=============================

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
  - [`404.md`](#404md-file)
  - [`about.md`](#aboutmd-file)
  - [`blog.md`](#blogmd-file)
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


## `_data/` dir
[`/_data/`](../_data/)

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

### `education.yml` file
[`/_data/education.yml`](../_data/education.yml)
This file is where you put in data entries for the education/talks page.
It has a range of felids most information about this is in the header for that file.

### `people.yml` file
[`/_data/people.yml`](../_data/people.yml)

This file is where you put in data entries describing the people working on the project 
 and goes on the people page.
It has a range of felids most information about this is in the header for that file.

### `software.yml` file
[`/_data/software.yml`](../_data/software.yml)

This file is where you put in data entries describing the software made by the project 
 and goes on the software page.
It has a range of felids most information about this is in the header for that file.


## `_posts/` dir
[`/_posts/`](../_posts)

This directory is where you put your markdown (`.md`) files that are the blog posts for the website.
These files must be named `yyyy-mm-dd-title.md`.  
For more information see the section on posts (there is also a simple template in the file). (TODO)

### `_posts/__template__.md` file
[`/_posts/__template__.md`](../_posts/__template__.md)

This is a simple template with junk contents, 
 the important thing contained in it is the jekyll front matter.
There are instructions on how to fill it out in the template.
Also check out the section on jekyll front matter. (TODO)



## `/education/` dir
[`/education/`](../education/)

This directory is where you can put supplementary info-post documents for the various 
 education, talks and other resources you wish to link.
There is another section to see with more info on info-post documents (TODO),
 that you should read for more info on these pages.

There is also an [`index.html`](../education/index.html) file in this directory,
 it contains delicate jekyll+liquid code for generating the 

### `education/__template__.md` file
[`/education/__template__.md`](../education/__template__.md)

This is a simple template with junk contents, 
 the important thing contained in it is the jekyll front matter.
There are instructions on how to fill it out in the template.

Also check out the section on jekyll front matter (TODO),
 especially the section about the front matter in info-posts & posts in general (TODO).

### `education/ABOUT.md` file
[`/education/ABOUT.md`](../education/ABOUT.md)

This is a markdown file, 
 that allows you to add supplementary content to the top of the education/talks page.
Works similarly to the info-post & blog-post markdown files for the main content 
 _(see section on markdown file contents for more info (TODO))_.

DO NOT modify any felid in the front matter of this file, 
  below the comment instructing you to not modify the following values.
You can add whatever fields you may want otherwise, to the front matter,
 so long as they do not overwrite existing fields in the `page` variable. 

In the main body of the `ABOUT.md` file you can add whatever content you want,
 but remember it will go between the page title & the generated list of
 education/talks drop down info boxed generated from [`/_data/education.yml`](#educationyml-file).



## `docs` dir
[`/docs/`](./)

This directory contains the vast majority of the documentation for how to use this website system.
Use the repo's primary [`/README.md`](../README.md), 
 or the [`README.md`](./README.md) located in the [`/docs/`](./) dir 
 for easy descriptive links on how to get around.



## `images/` dir
[`/docs/`](../images)

This directory is where you can put images that you would like to link, 
 in any markdown file, or in the education, people, and/or software entries 
 in their respective `.yml` files.

You can learn what the url to these image files will be in the multimedia input section (TODO).
Though it is highly recommended ease of use, for those unfamiliar with jekyll+liquid, 
 to upload images to external hosts like [imgur.com](https://imgur.com) and use absolute links to link them.



## `/people/` dir
[`/people/`](../people/)

This directory is where you can put supplementary info-post documents for the various 
 people, who you have contributed to the project.
There is another section to see with more info on info-post documents (TODO),
 that you should read for more info on these pages.

There is also an [`index.html`](../people/index.html) file in this directory,
 it contains delicate jekyll+liquid code for generating the 

### `people/__template__.md` file
[`/people/__template__.md`](../people/__template__.md)

This is a simple template with junk contents, 
 the important thing contained in it is the jekyll front matter.
There are instructions on how to fill it out in the template.

Also check out the section on jekyll front matter (TODO),
 especially the section about the front matter in info-posts & posts in general (TODO).

### `people/ABOUT.md` file
[`/people/ABOUT.md`](../people/ABOUT.md)

This is a markdown file, 
 that allows you to add supplementary content to the top of the people page.
Works similarly to the info-post & blog-post markdown files for the main content 
 _(see section on markdown file contents for more info (TODO))_.

DO NOT modify any felid in the front matter of this file, 
  below the comment instructing you to not modify the following values.
You can add whatever fields you may want otherwise, to the front matter,
 so long as they do not overwrite existing fields in the `page` variable. 

In the main body of the `ABOUT.md` file you can add whatever content you want,
 but remember it will go between the page title & the generated list of
 people drop down info boxed generated from [`/_data/people.yml`](#peopleyml-file).



## `publications/` dir
[`/publications/`](../publications)

This is the directory that corresponds to the data/content of the publications page of the website.
There are only two files in this directory, 
 they both can and should be used to provide content to the website.

This means that the publications page is meant to hold information on anything published,
 or citable that this project produces.
It produces a list of drop down items that correspond the contents of the 
 [`pubs.bib`](#pubsbib-file) file.
That provides the requisite quick access information about the entries as well as 
 a copy-&-paste-able, BibTeX entry for site viewers to copy and use for referencing the 
 work produced by this project. 

However, there is never a purpose to add any other files or folders to this directory.
Unlike many of the other directories for the info pages, 
 the publications does not support info-posts.

This is because, the website uses javascript, 
 to build the site's content on the clients machine, 
 and not with jekyll, like the other pages.

### `publications/ABOUT.md` file
[`/publications/ABOUT.md`](../publications/ABOUT.md)

This is a markdown file, 
 that allows you to add supplementary content to the top of the publications page.
Works similarly to the info-post & blog-post markdown files for the main content 
 _(see section on markdown file contents for more info (TODO))_.

DO NOT modify any felid in the front matter of this file, 
  below the comment instructing you to not modify the following values.
You can add whatever fields you may want otherwise, to the front matter,
 so long as they do not overwrite existing fields in the `page` variable. 

In the main body of the `ABOUT.md` file you can add whatever content you want,
 but remember it will go between the page title & the generated list of
 publications drop down info boxed generated from [`/publications/pubs.bib`](#pubsbib-file).

### `pubs.bib` file
[`/publications/pubs.bib`](../publications/pubs.bib)

This is the data file used to generate the content for the publications page.

> Because of how jekyll works,
>  this content is generated by a javascript script on the page viewer's client,
>  and not by jekyll, like all of the other pages,
>  its data file is located in the [`/publications/`](../publications/) dir 
>  and not jekyll's [`/_data/`](../_data/) directory, like the other pages.

The info in this file is just normal BibTeX, 
 except that for single line comments are always started with `%` 
 and not just any content outside of a BibTeX entry like normal BibTeX
_(NOTE: never put comments inside of a BibTeX entry even if you use a `%`,_
 _as they will show up in the copy-able BibTeX area on the webpage._
_Also make sure to escape `%` symbols in the BibTeX entries, i.e. `\%` so that they show up)_.

This format also makes a strange modification to BibTeX, in that all entries
 regardless of type can have a `note` and an `abstract` field.
Instead of the normal one or the other.
Most citation tools like Zotero, the $\LaTeX$ default bib behavior & the bibliography package, 
 as well as most formats formats that use CSL,
 will prioritize looking at the `abstract` field over
 the `note` field to use for the abstract/summary fo the piece.
Therefore, I have provided a way to leave a oblivious note about a publication by putting it in the `note` field.
It will show up at the top of the items drop down info box, before anything else.


## `/software/` dir
[`/software/`](../software/)

This directory is where you can put supplementary info-post documents for the various 
 software, that this project produces.
There is another section to see with more info on info-post documents (TODO),
 that you should read for more info on these pages.

There is also an [`index.html`](../software/index.html) file in this directory,
 it contains delicate jekyll+liquid code for generating the 

### `software/__template__.md` file
[`/software/__template__.md`](../software/__template__.md)

This is a simple template with junk contents, 
 the important thing contained in it is the jekyll front matter.
There are instructions on how to fill it out in the template.

Also check out the section on jekyll front matter (TODO), 
 especially the section about the front matter in info-posts & posts in general (TODO).

### `software/ABOUT.md` file
[`/software/ABOUT.md`](../software/ABOUT.md)

This is a markdown file, 
 that allows you to add supplementary content to the top of the software page.
Works similarly to the info-post & blog-post markdown files for the main content 
 _(see section on markdown file contents for more info (TODO))_.

DO NOT modify any felid in the front matter of this file, 
  below the comment instructing you to not modify the following values.
You can add whatever fields you may want otherwise, to the front matter,
 so long as they do not overwrite existing fields in the `page` variable. 

In the main body of the `ABOUT.md` file you can add whatever content you want,
 but remember it will go between the page title & the generated list of
 software drop down info boxed generated from [`/_data/software.yml`](#softwareyml-file).




## `_config.yml` file
[`/_config.yml`](../_config.yml)

This is Jekyll's config file, it defines all variables and configuration data used to build the website
 (data accessible via the `site` variable in liquid).
This file should only be touched by website admins.
Therefore, most instructions on how to use it is located in the [`ADMIN-ONLY.md`](./ADMIN-ONLY.md) file.



## `404.md` file
[`/404.md`](../about.md)

This is the markdown file that provides the content for the 404 error page,
 that the web server returns anytime there is any HTTP request error
 (un-elegant I know, but jekyll can be limiting).

Website Admins should, feel free to add any content you want to the body of the markdown file.
But do not edit any felid in the front-matter below the comment indicating that all felids below
 should not be edited.
Otherwise feel free to modify and add additional felids as you see fit.

Also check out the section on jekyll front matter (TODO), 
 especially the section about the front matter in info-posts & posts in general (TODO).

Non-Website-Admins, should probably not tough this file unless they get permission first.



## `about.md` file
[`/about.md`](../about.md)

This is the markdown file that provides the content for the website's main "landing" page.

Website Admins should, feel free to add any content you want to the body of the markdown file.
But do not edit any felid in the front-matter below the comment indicating that all felids below
 should not be edited.
Otherwise feel free to modify and add additional felids as you see fit.

Also check out the section on jekyll front matter (TODO), 
 especially the section about the front matter in info-posts & posts in general (TODO).

Non-Website-Admins, should probably not tough this file unless they get permission first.



## `blog.md` file
[`/blog.md`](../blog.md)

This is the markdown file that provides the content for the top section of the blog page,
 before the list of blog entries, as sort of supplementary information.

Website Admins should, feel free to add any content you want to the body of the markdown file.
But do not edit any felid in the front-matter below the comment indicating that all felids below
 should not be edited.
Otherwise feel free to modify and add additional felids as you see fit.

Also check out the section on jekyll front matter (TODO), 
 especially the section about the front matter in info-posts & posts in general (TODO).

Non-Website-Admins, should probably not tough this file unless they get permission first.



## `contact.md` file
[`/contact.md`](../contact.md)

This is the markdown file that provides the content for the website's main contact page.
This is where information on how to formally contact the project should go.
The body is entirely manually generated from the contents of the [`/contact.md`](../contact.md) file,
 so you will have to manually input whatever content you want to show up there,
 it will not grab any data from any data file,
 but you can use jekyll+liquid to get such data to use. 

Website Admins should, feel free to add any content you want to the body of the markdown file.
But do not edit any felid in the front-matter below the comment indicating that all felids below
 should not be edited.
Otherwise feel free to modify and add additional felids as you see fit.

Also check out the section on jekyll front matter (TODO), 
 especially the section about the front matter in info-posts & posts in general (TODO).

Non-Website-Admins, should probably not tough this file unless they get permission first.

