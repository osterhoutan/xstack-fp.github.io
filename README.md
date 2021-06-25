# Welcome to the ${ProjName} Website!!

## system requirements

- a unix style terminal
  - windows users must use crywigin, or preferably WSL
- Ruby > v2.4.0
- git

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
