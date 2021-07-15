  ADMIN ONLY
==============
> This info page contains info only really relevant to the website admin.
> Feel free to skip it if you are not the website admin.
> Otherwise, please always consult the website admin,
>  before implementing any advice stated here.



## `_config.yml` file
[`/_config.yml`](../_config.yml)

This is Jekyll's config file, it defines all variables and configuration data used to build the website
 (data accessible via the `site` variable in liquid).
This file should only be touched by website admins.

The File is Split into three sections:

### Required Fields
If a felid is commented out you should only need to edit it if it is necessary for functionality.

- **`title` ::** The formal name of the webpage, recommended to make it the name of the project.
  - This is the display name that will appear at the top of the webpage, & on the landing page.
- **`bio` ::** this is a short sentiment/comment _(1-2 sentence(s))_ about the project. 
  - It will appear in the header of the landing page of the website and not really anywhere else.
  - It should be used as flavor text more than an actual description.
- **`description` ::** this is a short brief _(1-2 paragraph(s))_ about the project.
  - It will appear in the header of the landing page of the website and not really anywhere else.  
- **`locale` ::** this is the language encoding for the webpage, by default it is `en_us`.
- **`url` ::** this is the main portion of the url that the webpage is hosted at without the path.
  - Only used if there are url building issues when using jekyll.
     (only really a problem when you disable jekyll building on GitHub Pages to use static prebuilt sites instead)
- **`url` ::** this is the path portion of the url that the webpage is hosted at.
  - Used when the website is hosted at a particular path from the main website, like when doing a GitHub Pages
     project level webpage (though you won't need to use this so long as GitHub is building the wite for you).

### Optional Fields
Fields here are either set to false, commented out, or both.
To get the benefit of entering data into a feild make sure to both uncomment it 
 and change the value to your desired value given the contextual instructions given in the comments in the file.

### Expert Fields
These fields are crucial for jekyll to build the website correctly,
 do not modify them unless you have to, and know what you are doing!


## Fav-icons
_google fav-icon infrastructure_

To modify the fav-icons of the website 
 (the little thumbnail for the website shown on the tab in your browser).
 just go to the [`/assets/icon/`](../assets/icon/) directory 
 and replace the image files with your preferred icon files.
Do not change the file names or edit the `manifest.json` file.

Make sure they are of the same image type, size and resolution for best effect.

For more information on fav-icons see [this wikipedia entry](https://en.wikipedia.org/wiki/Favicon).



