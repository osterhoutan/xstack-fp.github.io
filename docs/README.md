  How To
==========
This documentation does not contain any information on how to setup the website system,
 just how to use it once it has been setup.
Please see the main [`/README.md`](../README.md) for those instructions.

## Table of Contents
- [How To](#how-to)
  - [Table of Contents](#table-of-contents)
  - [The Basics](#the-basics)

  - [ADMIN documentation](./ADMIN-ONLY.md)
  - [Directory Structure](./directory_structure.md)
  - [Jekyll + Liquid Basics](./jekyll-liquid.md)


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
In the [`directory_structure.md`](./directory_structure.md) file.



