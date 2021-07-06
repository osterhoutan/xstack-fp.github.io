  Adding Content
==================

## Table of Contents
- [Adding Content](#adding-content)
  - [Table of Contents](#table-of-contents)
  - [Tags and IDs](#tags-and-ids)
    - [IDs](#ids)
    - [Tags](#tags)
- [Blog Content](#blog-content)
  - [Instructions](#instructions)
- [Data Content](#data-content)
  - [Info-Posts](#info-posts)
    - [Instructions](#instructions-1)
  - [ABOUT Pages](#about-pages)
  - [Data Content By Type](#data-content-by-type)
    - [education](#education)
    - [publications](#publications)
    - [people](#people)
    - [software](#software)
- [Extra Content](#extra-content)


 Tags and IDs
--------------
To keep harmony between the large amounts of data this system could end up handling,
 a system of id's that implement a way to refer to the various people, software, and resources 
 that you enter into the site via the data files.
 _(see the data content section for more info \[[link](#data-content)\])_
So that you can build connections between the various parts of the website,
 and that the build system can construct additional connections for you.
Making the website more interconnected & allowing you to provide more information than 
 would otherwise be possible.

### IDs

ID's are meant to identify a piece of software, a person, or a resource (displayed on the education/talks page).
You will use this ID to let the jekyll build system know what you are referring to.

The place that defines what an id refers to is the relevant `.yml` data file in `/_data/`.
However, id's must also be unique across all of these data files.
The id is the top level field name for the entry in the particular file.
> ```yml
> <id>:
>   # Entry fields indented below the id, 
>   #  as an entry has a structure/dict/mapping/hash/object type data value.
>   <field-name>: <field-data>
>   # ...
> ```
The id can be used to get the data in the entry using liquid.


### Tags
Tags are used to tell jekyll what other blog posts are related to the current post.
So that it can build the related pages and post section at the bottom of your post.

Tags are defined in teh front matter of page or post with the `tags` keyword.
The value of the field should always be an array/list
 _(see YAML collections/sequences/array/list_
  _syntax \[[link](https://lzone.de/cheat-sheet/YAML#yaml-sequences)\])_.
> ```jekyll
> ---
> # ...
> tags: [tag1, tag2, tag3]
> ---
> <!-- ... -->
> ```

If you want the most interconnected site, make sure to add a good number of relevant tags.

You should use the ID of a person, software, or resource to tag it for best effect.

You should order tags in order of relevance, 
 as tags earlier in the list will show up closer to the top of the related pages and post sections.


<br/><br/>




 Blog Content
==============
Adding blog content is easy.

## Instructions
 1. Create a new file with the name `yyyy-mm-dd-title.md` inside of the `/posts/` directory,
     based off of the template file for posts ([`/_posts/__template__.md`](../_posts/__template__.md)).
    - The date part of the file name should be the day you want it published.
    - The title portion can be anything so long as it is still a valid file name, 
       as jekyll does not care after the `*-dd-` until the file extension.
    - This naming scheme ensures unique file names in the final build.
    - Copying the [template](../_posts/__template__.md) is a very good idea.
 2. Fill out the front matter of the post. \
     &ensp; Make sure that the following fields are filled out:
    - `title`
    - `author`
    - `date` (this should be the date you want it to start showing up on the site at)
    - `published` (set this to `true` when you want the post to actually show up. 
       `false` forces the post to stay hidden)
    - `tags` (very important but not required _see the tags section \[[link](#tags)\]_)
    - `image` (URL to an image that will be used as a thumbnail for the post in lists)
 3. Do not modify any front matter fields bellow the `# DON'T MODIFY THESE:` comment.
 4. _(optional)_ Add any other fields to the front matter you want to use.
     _(see the section on front-matter for more info \[[link](./jekyll-liquid.md#front-matter)\])_ 
 6. Add the content to the main body of the file (Kramdown markdown syntax for `.md` files).
    - You can use liquid template syntax in the post files 
       _(see the Jekyll+Liquid Section \[[link](./jekyll-liquid.md)\])_.
 7. When ready to publish the post make sure to set the `published` field in the front matter to `true`.

<br/><br/>



 Data Content
==============
Adding data content is a bit more complicated than adding a blog post.

As of this time there are four catagories of data content:
 - education resources
 - people
 - publications
 - software

Each of these catagories has their own directory in the structure 
  _(see the directory structure section for more info \[[link](./directory_structure.md)\])_.
In these directories you can place files named `<id>.md` _(replace `<id>` with the [id](#ids))_.
Which will allow you to make an info-post,
 which work largely like [blog posts](#blog-content),
 about the item associated with the `<id>` of the type
 indicated by the directory
 _(base these files of of the `__template__.md` file in the directory)_.
_(see the info-post section for more info \[[link](#info-posts)\])_

Each of them has a data file where the information used to generate teh content can be located.
For all but publications these are located in the [`/_data/`](../_data) directory,
 in `.yml` files with corresponding names.
In these `.yml` files are also comments giving more specific documentation as to the supported fields 
 and their use than is provided in this document.

Publications is different all around, as they do not support [info-posts](#info-posts),
 their data entry is a `.bib` file located in the publications directory: 
 [`/publications/pubs.bib`](../publications/pubs.bib).
These data entries of course take the form of standard BibTeX entries.
The publications page also is not generated by Jekyll but instead by javascript on the 
 website viewers machine, when they load the page.


## Info-Posts
Info-Posts Work similarly to [blog posts](#blog-content), but they are not shown on the blog pages.
Instead their static link is inside the associated date entries rendered content on teh respected page.
In addition when other info-posts, or blog posts put the [id](#ids) for a specific data entry type,
 a link to the info post will be generated in the related pages section at the bottom of that page.

> ***NOTE:*** \
> _Info-posts do not work for publications, only education resources, people, & software._

There can only be one info-post per entry [id](#ids).
So they should be used as general information pages that allow more fredom than the 
 `abstract` felid from the data entry, allows for the generated content.
Other remarks about a data entry should either be a [blog post](#blog-content),
 or better yet be on a website dedicated to that particular thing, 
 and not the general project website.

### Instructions
Info-posts are a bit more strict in how they can be created than blog posts but the process is almos the same:  
 1. Create a new file with the name `<id>.md` inside of the associated data-type directory,
     based off of the template file for info-posts _(located in the same directory and named: `__template__.md`)_.
    - The date part of the file name should be the day you want it published.
    - The title portion can be anything so long as it is still a valid file name, 
       as jekyll does not care after the `*-dd-` until the file extension.
    - This naming scheme ensures unique file names in the final build.
    - Copying the template, then modifying it, is a very good idea.
 2. Fill out the front matter of the post. \
     &ensp; Make sure that the following fields are filled out:
    - `title`
    - `author`
    - `date` (this should be the date you want to display on the page)
    - `published` (set this to `true` when you want the info-post to actually show up. 
       `false` forces the info-post to stay hidden)
    - `tags` (very important but not required _see the tags section \[[link](#tags)\]_)
    - `image` (URL to an image that will be used as a thumbnail for the post in lists)
 3. Do not modify any front matter fields bellow the `# DON'T MODIFY THESE:` comment.
 4. _(optional)_ Add any other fields to the front matter you want to use.
     _(see the section on front-matter for more info \[[link](./jekyll-liquid.md#front-matter)\])_ 
 5. Add the content to the main body of the file (Kramdown markdown syntax for `.md` files).
    - You can use liquid template syntax in the post files 
       _(see the Jekyll+Liquid Section \[[link](./jekyll-liquid.md)\])_.
 6. When ready to publish the info-post make sure to set the `published` field in the front matter to `true`.


## ABOUT Pages
In each of these directories exists an `ABOUT.md` file.
This file lets you add markdown content below the title of the page, before the generated content list.
It works like normal Kramdown markdown.

DO NOT modify the [front-matter](./jekyll-liquid.md#front-matter) of these pages.
Especially never change or add the `id`, `info_type`, or `layout` felids, or you will cues undetermined errors to the resulting webpage, if it builds at all.
However, changing or adding the `title`, `bio` and/or `description` fields is usuals harmless to do.


## Data Content By Type

### education
**Directory:** [`/education/`](./directory_structure.md#education-dir) \
**Data File:** [`/_data/education.yml`](./directory_structure.md#educationyml-file) \
**Info-Post Template File:** [`/education/__template__.md`](./directory_structure.md#education__template__md-file) \
**`ABOUT` File:** [`/education/ABOUT.md`](./directory_structure.md#educationABOUTmd-file) \
**Site Output Page:** &ensp; education/talks

**Example data entry:**\
&emsp; _in: [`/_data/education.yml`](../_data/education.yml)_
```yml
peachy_assignments:
    title: '"Peachy Assignments," a Poster Session at EduPar 2018'
    author: Ganesh Gopalakrishnan
    url: https://www.overleaf.com/read/whmzmrbwrvrw
    date: 2018
    icon: https://cdn.jim-nielsen.com/ios/512/peach-share-vividly-2018-09-06.png
    cite_key: edupar_peachy_assignments
    abstract: 
            These were some assignments contributed to
            EduPar 2018 which is trying to collect assignment
            nuggets to be inserted into courses.
```


### publications
**Directory:** [`/publications/`](./directory_structure.md#education-dir) \
**Data File:** [`/publications/pubs.bib`](./directory_structure.md#pubsbib-file) \
**Info-Post Template File:** &ensp; _N/A_ \
**`ABOUT` File:** [`/publications/ABOUT.md`](./directory_structure.md#publicationsABOUTmd-file) \
**Site Output Page:** &ensp; publications

**Example data entry:** \
&emsp; _in: [`/publications/pubs.bib`](../publications/pubs.bib)_
```bib
@inproceedings{rbp-gtc-poster,
  title = {Effective Parallelization of Belief Propagation on the GPU},
  author = {Mark Van der Merwe and Vinu Joseph and Ganesh Gopalakrishnan},
  year = 2019,
  note = {Nvidia GTC poster},
  abstract = {This is what an abstract would look like !!
  let's see how it does with new lines & html... <br/>
  <b>simple bold text text</b> some text </pre> </div> bad tag test(s) </body> you should see this text. },
  url = {https://www.nvidia.com/en-us/gtc/poster-gallery/developer-tools}
}
```

### people
**Directory:** [`/people/`](./directory_structure.md#people-dir) \
**Data File:** [`/_data/people.yml`](./directory_structure.md#peopleyml-file) \
**Info-Post Template File:** [`/people/__template__.md`](./directory_structure.md#people__template__md-file) \
**`ABOUT` File:** [`/people/ABOUT.md`](./directory_structure.md#peopleABOUTmd-file) \
**Site Output Page:** &ensp; people

**Example data entry:**\
&emsp; _in: [`/_data/education.yml`](../_data/education.yml)_
```yml
bob101:
    name      : Bobert Bently
    email     : bob101@gmail.com
    links     :
        website     : https://bob101.github.io   # URL your personal webpage and/or portfolio
        github      : bob101   # bitbucket username
        gitlab      : bob101   # gitlab username
        gitlab_url  : false   # URL to self hosted gitlab user profile (this will supersede the normal gitlab)
        bitbucket   : bob101   # bitbucket username
        reddit      : u/bob101   # sub-reddit name (prepend "r/" for sub-reddit or "u/" for a user)
        forum       : false   # URL to user profile on the proj help forum
        youtube     : false   # youtube channel URL (harmless self promotion)
        vimeo       : false   # vimeo channel name (who even are you?)
        twitter     : bob101   # twitter handle (if you add this you're probably annoying)
        instagram   : false   # instagram profile name (if you add this you're a bad person)
        facebook    : false   # facebook page name (if you add this you're old)
    position  : ms student 
    title     : Coffee Grabber Extraordinaire
    pronouns  : they/them
    pfp       : http://static1.squarespace.com/static/54c85166e4b03a5492fe6e90/t/5fca828c5bd8fe559a71b0e0/1607107218301/Rob+Salmeron+Headshot.jpeg
    abstract  :
                  Resident expert at maze solving algorithms & fetching coffee.
                  _Feel free to tag me in any issues with the aMAZEsoft project in it's repo._
```



### software
**Directory:** [`/software/`](./directory_structure.md#people-dir) \
**Data File:** [`/_data/software.yml`](./directory_structure.md#softwareyml-file) \
**Info-Post Template File:** [`/people/__template__.md`](./directory_structure.md#software__template__md-file) \
**`ABOUT` File:** [`/people/ABOUT.md`](./directory_structure.md#softwareABOUTmd-file) \
**Site Output Page:** &ensp; software

**Example data entry:**\
&emsp; _in: [`/_data/software.yml`](../_data/software.yml)_
```yml
uintah:
  title: The Uintah Software
  author: Alan Humphrey and Martin Berzins
  url: http://uintah.cs.utah.edu/
  repo:             https://github.com/some-user/some-repo # URL to other repo for the software
  icon: https://cdn.vox-cdn.com/thumbor/6C5Yi14bAf7iRHvCEWK9xlL5TYM=/0x0:3000x3000/1200x800/filters:focal(1260x1260:1740x1740)/cdn.vox-cdn.com/uploads/chorus_image/image/64978846/3b17607095.0.jpeg
  image: https://www.autoitscript.com/autoit3/docs/images/SampleGuiScreenshot.png
  links: 
    docs:             https://uintah.cs.utah.edu/docs # URL to page containing documentation for one thing or another (this will also be added to the nav bar)
    email:            false # primary contact email address for entire proj
    reddit:           false # sub-reddit name (prepend "r/" for sub-reddit or "u/" for a user)
    forum:            https://uintah.cs.utah.edu/forum # URL to a help forum (i.e. repo issues page or an actual forum)
    youtube:          false # youtube channel URL
    vimeo:            false # vimeo channel name (who even are you?)
    twitter:          false # twitter handle (if you add this you're probably annoying)
    instagram:        false # instagram profile name (if you add this you're a bad person)
    facebook:         false # facebook page name (if you add this you're old
  licence: MIT
  licence_url: false # url to official licence page or file.
  abstract: Uintah problem solving environment
```

<br/><br/>



 Extra Content
===============
There exists a few files in the root of the directory that enable you to modify the content of the 
main pages of the website.

[`/404.md`](./directory_structure.md#404md-file) allows you to change/set the content of the error page returned for bad URL & HTTP requests. \
[`/about.md`](./directory_structure.md#aboutmd-file) allows you to change/set the content on the main landing page. \
[`/blog.md`](./directory_structure.md#blogmd-file) allows you to change/set at the top of the blog page, before the gallery of blog posts. \
[`/contact.md`](./directory_structure.md#contactmd-file) allows you to change/set of the contact page. 

It is not recommended to add to the [front-matter](./jekyll-liquid.md#front-matter) of these pages.
Execpt for the section that says it is fine, which usualy just contains the `title`, `bio` and `description` felids.
And never change or add the `id`, `info_type`, or `layout` felids, or you will cues undetermined errors to the resulting webpage, if it builds at all.



 