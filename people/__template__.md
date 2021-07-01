---
#(don't forget to change file name to id of person in question)
# You MUST Modify these:
id: ${person id} # this should be the entry key in the _data/people.yml
title: ${Person's full name}
date: ${date}
published: false   # set to true to make it public
tags: [people, person] #, ${additional tags -optional-}]
# modify these if you want to:
categories: [people ] #, ${additional catagories}]
# Don't modify these:
layout: info-post
permalink: people/:basename
---

### Test Title

test content

this allows for limmited multimedia support, and you will need to either know how to use jekyll or link it with absolute URI from an external source to get it to work.
The later is recomended fo rmost people. 

gobldey gook

test image w/ jekyll liquid comments (image is in the `/site-src/images` directory already)

![test-image]({{ "/images/DecidabilityDiagram.png" | absolute_url }})


test image w/ external media:

![Test-Image-2](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXqq3j05ykEU69GBIwyuuuiFhePdmiIIk3zMJ6gfim7Sv3yaJ0v86GjGf4_W9P-BqgHjA&usqp=CAU)


that is all for now

