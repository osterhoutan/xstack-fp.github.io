   Jekyll + Liquid Basics
============================
This website-system utilizes the Jekyll ruby static webpage build system,
 which utilizes Liquid tempesting syntax inside of it's files to dynamically 
 build a static site from the provided data & content files.

## Table of Contents
- [Jekyll + Liquid Basics](#jekyll--liquid-basics)
  - [Table of Contents](#table-of-contents)
    - [Helpful External Resources](#helpful-external-resources)
  - [Jekyll](#jekyll)
    - [`_config.yml` file](#_configyml-file)
    - [Front Matter](#front-matter)
    - [Data Files](#data-files)
  - [Liquid](#liquid)
  - [Markdown](#markdown)
    - [$\LaTeX$ Math](#latex-math)



### Helpful External Resources
- Jekyll
  - [official docs](https://jekyllrb.com/docs)
  - [front matter docs](https://jekyllrb.com/docs/front-matter/)
  - [data file docs](https://jekyllrb.com/docs/datafiles/)
- Liquid
  - [official Liquid docs](https://shopify.github.io/liquid/)
  - [the basics](https://shopify.github.io/liquid/basics/introduction/)
  - [Jekyll additions](https://jekyllrb.com/docs/liquid/)
    - [filters](https://jekyllrb.com/docs/liquid/filters/)
    - [tags](https://jekyllrb.com/docs/liquid/tags/)
    - [variables](https://jekyllrb.com/docs/variables/)
- Markdown (Kramdown)
  - [general docs](https://kramdown.gettalong.org/documentation.html)
  - Kramdown's markdown syntax
    - [docs](https://kramdown.gettalong.org/syntax.html)
    - [cheat sheet](https://aoterodelaroza.github.io/devnotes/kramdown-cheatsheet/)
- YAML
  - [Official Doc](https://yaml.org/spec/1.2/spec.html)
  - [Quick Start Tutorial](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)
  - [In-Depth Tutorial](https://www.tutorialspoint.com/yaml/index.htm)
  - [Cheat Sheet](https://lzone.de/cheat-sheet/YAML)

<br/><br/>



 Jekyll
--------
### `_config.yml` file
[`/_config.yml`](../_config.yml) \
This is where jekyll looks for global config settings for the build process are set. \
I have laid out a series of fields already in this file.
Follow the instructions on what to do with them that are included in comments in the file. \
_!! **DO NOT** remove any field I have put in, as it could disrupt the functionality of the system !!_

You can however, add whatever fields you want to the file.
_(NOTE: All top level entries in the file must have unique names_
 _& not be names of jekyll configured variables,_ 
 _else risk overwriting or braking existing data or the entire build process !!)_ \
All data entered into this file will be available via the `site` variable in liquid.
As well as, any fields jekyll generates for the build.


### Front Matter
In jekyll `.html`, and `.md` files can contain a section called front matter.
This section is where you can encode data for jekyll and liquid to use when building the site.
The front matter section must start on teh first line of the file, and is delimited with `---` before and after.
Data in the front matter must be encoded in the YAML format.
> ##### Example
> ```jekyll
> ---
> title: "some title"
> description: "some more text"
> tags: [tag1, tag2, tag3]
> ---
> ```
> <!-- The content of your file -->
All fields you put in the front matter can be acessed as members of the `page` variable for liquid.
There are a number of fields that if they are not defined in the front matter 
 jekyll will assign default values to.
Such as `permalink`, `date`, `collection`, `id`, `exerpt`, _etc._
As well as, some felids that jekyll will overwrite if you define a value for them.
Such as `content`, `url`, `path`, `relative_path`, `previous`, `next`, _etc._

I have added some basic conventions to the front-matter of 
 [info-posts](./adding-content.md#data-content) and 
 [blog posts](./adding-content.md#blog-content)
 (see their sections respectively). 


### Data Files
With jekyll you can put any YAML (`.yml` or `.yaml`), JSON (`.json`), CSV (`.csv`), or TSV (`.tsv`) file
 in the `/_data/` directory and you can have access to it in liquid comments via the `site.data.<file-name>` variable.
This is really handy if you have some data that you want to reference frequently that is subject to change.
_(see the section on liquid for info on how to do so \[[link](#liquid)\])_

In this website-system I have predefined three such data files: `education.yml`, `people.yml`, & `software.yml`.
These are where you can input data to populate the site given the infrastructure already in place.
_(see the add content section for more info \[[link](./adding-content.md)\])_
I do not recommend adding random data points into these files, it should be safe to add new felids to entries in these files, but any item at the top level of the file must conform to the standards defined in teh file, else break the website.

You can also add any additional files you would like to the `/_data/` directory, and access them
 without breaking anything. 


<br/><br/>



 Liquid
--------
Liquid in a template syntax that jekyll uses to allow the individual files of the website to be built dynamically, into a static website.

The syntax has only a few parts, most of which are best described in the official liquid doc \[[link](https://shopify.github.io/liquid/basics/introduction/)\].

Jekyll does not remove any features from the base implementation of liquid.
However, it does add some custom [tags](https://jekyllrb.com/docs/liquid/tags/) 
 and [filters](https://jekyllrb.com/docs/liquid/filters/) to use,
 as well as, defining all of the [variables](https://jekyllrb.com/docs/variables/) 
 accessible by default.
Most of which, are defined either in the `/_config.yml`, 
 the [front matter](#front-matter) of a page,
 in some [data file](#data-files),
 or during the build process by jekyll.

The system is best learned from the official resources, 
 and I have not really made any changes,
 or instigated any conventions to the system that are not mentioned elsewhere in this documentation.
_(see the tags & id section \[[link](./adding-content.md#tags-and-ids)\]_ 
 _and the `info_type`s section \[[link](./adding-content.md#info_types)\])_


<br/><br/>


 Markdown
----------
In jekyll you can either use HTML or markdown.

The [`/_config.yml`](../_config.yml) defines what markdown engine & syntax is used.
I have configured it to use jekyll's preferred default 
 [Kramdown](https://kramdown.gettalong.org/documentation.html),
Which works mostly like the GitHub Flavored markdown you are used to,
 just without the 
 [emoji short-codes](https://www.markdownguide.org/extended-syntax/#using-emoji-shortcodes) 
 support, 
 but it does still let you use `@<github-username>` to
 tag/link to a profile (because of a jekyll plugin).


### $\LaTeX$ Math
Markdown with Kramdown, also supports limited $\LaTeX$ via MathJaX,
 thx to some infrastructure set up with the website-system.
This means that Kramdown outputs text in a way that MathJaX will recognize,
 then when a user loads the page, MathJaX will render the math.

However, unlike in normal GitHub Markdown you must always use double `$$...$$`,
 even for inline math.
To get a math block you must have a blank line between the `$$...$$`s and any other text.
> **_i.e._**
> ```markdown
> Inline math test $$\LaTeX$$ some normal text $$E=mc^2$$.
> 
> math block test
> 
> $$
> E=mc^2
> $$
> 
> Some more text
> ```
You can also use the new age $\LaTeX$ math mode delimiters:
- `\(...\)` :: for inline math
- `\[...\]` :: for a math block

However, this is a hacky trick done in part by MatJaX post jekyll build.
So you must escape you backslash in order for it to show up in Kramdown's output
 for mathJaX to render. \
Therefore the example above with this format would look like:
> **_i.e._**
> ```markdown
> Inline math test \\(\LaTeX\\) some normal text \\(E=mc^2\\).
> 
> math block test
> \\[
> E=mc^2
> \\]
> 
> Some more text
> ```

