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

## directory
- [setup](#setup)
  - [host on GitHub Pages](#github-pages)
  - [host locally](#locally)
- [documentation](docs)
  - [Use](docs)
  - [Jekyll & Liquid](docs/jekyll)

## setup
You can host this system yourself, 
  though this is more advanced, or just use GitHub Pages.
For most people using GitHub Pages will be the way to go,
 but even with this if you want to be able to do more advanced things 
 you might want to 
### GitHub Pages

#### system requirements<sup>&ddagger;</sup>
- git
- a text editor

<sub><sup>&ddagger;</sup>- you technically could just do everything from GitHub web client,
 as you can create and edit files to an sufficient extent to do most tasks from there.</sub>

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

## setup:

 1. Install Ruby (version 2.4.0 or higher) for your system.
    - you will need to figure this step out as it varies between operating systems.
 2. Run the following lines of code to install all of the necessary Ruby Gems
    ```bash
    cd site-src
    bundle install  # run this with sudo if you want to install globally
    bundle update
    ```
## using this website builder
For how to add and modify content 
 please read the [`/site-content/README.md`](./site-content/README.md)
 to learn how to add content and update the website.

But after you have added whatever content you want, just run the `update-site.sh` script 
 to build and push (it will push for you) the site to GitHub.
Where it will take a few minutes (usually no more than 2) to republish your changes.

## setup GitHub Pages

 1. Figure out what your GitHub Pages url is going to be.
 2. Go modify [`/site-scr/_config.yml`](./site-scr/_config.yml) to match this information.
     1. Set the value of `url` to whatever the domain and protocol will be. _i.e._
        ```
        If your GitHub Pages url is:
          https://<username>.github.io/<repo-name>
        the url field should be set to:
          https://<username>.github.io
        ```
     2. If you are using a project level site or using a url with a partial path 
         set the value of `baseurl` to whatever the path is. _i.e._
        ```
        If your GitHub Pages url is:
          https://<username>.github.io/<repo-name>
        the baseurl field should be set to:
          <repo-name>
        ```
 3. Go to the settings page of this repo on GitHub.
 4. Navigate to the "Pages" settings pain (from the nave pain on the left)
 5. Select the branch you want to have the website be on.
 6. Set the directory to `docs`, as this is where jekyll will build your site too.
