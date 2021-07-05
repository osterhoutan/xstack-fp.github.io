  Welcome to the ${ProjName} Website!!
==========================================
This is a website system system that utilizes jekyll 
 to build a static website from provided data.
As well as be compatible with GitHub Pages for easy hosting.

It utilizes a website template by [&copy;HTML5 UP&trade;](https://html5up.net/), 
  that was modified by [soundgrail](https://soundgrail.com/) to be compatible with jekyll.
Then I [@osterhoutan-UofU](https://github.com/osterhoutan-UofU) modified it further to make
 a website system that accompanied by the proper documentation (provided) 
 would allow anyone<sup>&dagger;</sup> to add content to the website, 
 as well as generate content based upon data provided.

This website system is primarily designed for scholarly work 
 in the many fields of computer science.
 specifically to be used as a landing page for a single research project, 
 or even a research center or department.
But overall it is not very flexible and would require modification to use for other applications.

<sup>&dagger;</sup> - As this website system has specific clientele in mind,
 who focus in computer science, 
 the instructions and other documentation is geared to them.
So while you do not need to know much about web technologies to use it,
 knowledge of TOML, markdown (enough to get by with github README files should suffice), 
 and some jekyll+liquid syntax if you want to get crazy.
Other than that though it is presumed that users have experience with git, 
 and basic computer skills should suffice.

## Table of Contents
- [Welcome to the ${ProjName} Website!!](#welcome-to-the-projname-website)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [GitHub Pages](#github-pages)
      - [system requirements<sup>&ddagger;</sup>](#system-requirementssupsup)
      - [Setup - Client](#setup---client)
      - [Setup - Repo](#setup---repo)
    - [Locally](#locally)
      - [system requirements](#system-requirements)
      - [instructions](#instructions)
    - [General Admin Setup](#general-admin-setup)

  - [How To Use](./docs/README.md)
    - [ADMIN Documentation](./docs/ADMIN-ONLY.md)
    - [Directory Structure](./docs/directory_structure.md)
    - [Jekyll + Liquid Basics](./docs/jekyll-liquid.md)

Most instructions to use this website system are contained in the [`/docs/`](docs) directory
 of the repo.
In the directory above are some basic links to the major sections of information,
 with their own directory sections to guide you from there.

I, one day, might bother to import and set up all the info in these documentation pages 
 in the wiki of the website systems repo, but that day is not today. 

## Setup
You can host this system yourself, 
  though this is more advanced, or just use GitHub Pages.
For most people using GitHub Pages will be the way to go,
 but even with this if you want to be able to do more advanced things,
 you might want to get set up to build and "host" locally. 
As this allows you to see the webpage in a local staging ground for testing, _etc._ 
In this case, however, you are likely an advanced user and should be able to figure that out.
But for most I recommend Building and hosting on GitHub Pages.


### GitHub Pages

#### system requirements<sup>&ddagger;</sup>
- git
- a text editor

<sub><sup>&ddagger;</sup>- you technically could just do everything from GitHub web client,
 as you can create and edit files to an sufficient extent to do most tasks from there.</sub>

#### Setup - Client

For clients just copy the repo for the GitHib Pages that your, website admin has setup.
Make sure they have granted you permission on GitHub to make commits/changes to the website repo.

Then to make changes to the website just do it on your own machine, commit & push the changes.
The changes should take effect on the website within 2 minutes of the push 
 (max I've sene is 5 min).
 
You can also just make changes via the GitHub Web Client for the repo.
Where you can create new files, and edit existing files. 
Which is all it takes to edit files on the website.


#### Setup - Repo
This section is primarily for the website administrator, and/or advanced users.

To Host on GitHub Pages you will need to either clone and/or for the systems repo.
You will only really need the master branch as other branches are wither dead 
 or used for active dev and therefore not stable.

I recommend,
 for the site administrators,
 making sure that you are able to merge with the master branch of the template repo down the line
 if you ever want to update your copy of the site, to fix bugs or get new features.<sup>&dagger;</sup>
But be ready and capable to deal with merge conflicts 
 or the occasional test data file slipping through.

<sub><sup>&dagger;</sup>- new features are not likely to come fast if at all.</sub>


**For this purpose when setting up a new site, I recommend either forking or cloning the repo from GitHub**
 **_(Specifically I recommend forking via GitHub)_.**
Unless you know how to use git to manage remotes and branches, then you would probably be fine,
 as the template repo should be safe from uncontrolled pushes.

Following setting up the template repo for your use, please follow the instructions in the 
 [`/_config.yml`](./_config.yml) and in the ADMIN documentation
 \[[link](./docs/ADMIN-ONLY.md/#_configyml-file)\]
 to do some basic configuring
 and customizing of the jekyll build system and this template. 

### Locally
#### system requirements
- a unix style terminal
  - for windows users it is recommended to use WSL (v1 or v2),
     as ruby and jekyll on windows is sometimes buggy especially when using crywigyn and the like.
- Ruby > v2.4.0
  - bundler
  - jekyll
- git
- a text editor

#### instructions
Use cases can vary to much between machines I recomend you look up the installation guide on 
 Jekyll's website \[[link](https://jekyllrb.com/docs/)\] for setup instructions,
 and how to use jekyll in a basic sense.

Then if you chose this option you probably know better than I do how to set up and host a website,
 from you own machine.

If you choose this option solely for the purpose of being able to see your changes
 without updating the official site, or debugging, 
 just follow jekyll's quick-start guide linked above, 
 and use the following command to launch a local test server.
```bash
bundle exec jekyll serve --trace
```  


### General Admin Setup
These instructions are for the website administrator.

After you have done whatever it is you need to do to set up and install this website system.
You will need to go and edit the top few fields in the [`/_config.yml`](./_config.yml)
 in order to set up some values for the website.
More information about the [`/_config.yml`](./_config.yml) file, 
 as it pertains to this website-system,
 can be found in comments inside of the [`/_config.yml`](./_config.yml) file itself,
 or in the ADMIN documentation \[[link](./docs/ADMIN-ONLY.md/#_configyml-file)\].
Most of the felids are either self explanatory or there are instructions in the file to guide you.

In addition it would be prudent to perform a find and replace all across the entire repo
 for the string (non-regex, and match case off for best results) `${ProjName}`,
 with whatever you want the title of the site to be. 

