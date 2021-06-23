---
layout: page
title: Publications
---

<div id="collapsible-bib">
</div>

<div id="collapsible-bib-gen">

{% bibliography %}

</div>

<!-- !! THIS MUST BE INCLUDED IN ANY FILE THAT CALLS `{{ bibliography }}` !! -->
<script type="text/javascript">
    // - Add pertinent css ----
    var styles = `
    /* COLLAPSIBLE ITEM STUFF */

    .collapsible-bib-entry {
        margin-bottom: 8px;
    }

    /* Style the button that is used to open and close the collapsible content */
    .collapsible-bib-btn {
        background-color: #4B6C86;
        color: white;
        cursor: pointer;
        padding: 8px;
        width: 100%;
        border: none;
        text-align: left;
        outline: none;
    }

    .collapsible-bib-authors {
        font-style: italic;
        font-size: 10pt;
        text-transform: capitalize;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    .collapsible-bib-title {
        font-size: 12pt;
        overflow-wrap: break-word;
        text-transform: capitalize;
        color: white;
        margin-bottom: 0;
        padding-bottom: 0;
    }

    /* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
    .collapsible-bib-btn:hover {
        background-color: #204765aa;
    }

    .collapsible-bib-active {
        background-color: #204765;
    }

    /* Style the collapsible content. Note: hidden by default */
    .collapsible-bib-content {
        padding: 2px 8px;
        overflow: hidden;
        background-color: #5d7a9151;
        color: black;
        max-height: 0;
        transition: max-height 0.2s ease-out;
    }

    /* Add icon  */
    .collapsible-bib-btn:after {
        content: url({{ "/images/cite.svg" | absolute_url }});
        color: white;
        float: right;
        margin-left: 5px;
        fill: none;
        -webkit-transition: -webkit-transform 1s ease-in-out;
        -ms-transition: -ms-transform 1s ease-in-out;
        transition: transform 1s ease-in-out;
    }

    .collapsible-bib-active:after,
    .collapsible-bib-btn:hover:after {
        transform: rotate(180deg);
        -ms-transform: rotate(180deg);
        -webkit-transform: rotate(180deg);
    }

    .collapsible-bib-active:after {
        fill: white;
    }

    div.collapsible-bib-bibtex {
        padding: 6pt 2pt 2pt 2pt;
        margin: 0pt;
    }
    div.collapsible-bib-bibtex > pre {
        border: 1px #204765;
        padding: 2pt;
        margin: 2pt;
        background-color: #f7e99cb6;
        overflow-x: auto;
    }
    div.collapsible-bib-reference {
        padding-top: 6pt;
    }
    `
    var styleSheet = document.createElement("style")
    styleSheet.type = "text/css"
    styleSheet.innerText = styles
    document.head.appendChild(styleSheet)


    // // - Extract Bib entries from list ----
    // var genDiv = document.getElementById("collapsible-bib-gen");
    // var outDiv = document.getElementById("collapsible-bib");
    // var all_entries = document.getElementsByClassName("collapsible-bib");
    // var headerElements = genDiv.getElementsByTagName("h2");
    
    // var headers = [];
    // for (var elem of headerElements) {
    //     headers.push(elem.textContent);
    // }
    // years.sort();

    // for (var y of years) {
    //     var year_entries = all_entries.getElementsByClassName("collapsible-bib-entry-year-"+y);
    //     var secDiv = document.createElement("div");
    //     secDiv.id = "collapsible-bib-section-year-"+y;
    //     secDiv.classList.push("collapsible-bib-section");
    //     outDiv.children.appendChild(secDiv);
    //     var secHeader = document.createElement("h2");
    //     secHeader.textContent = y;
    //     outDiv.children.appendChild(secHeader);
    //     for (var e of year_entries) {
    //         outDiv.children.appendChild(e);
    //     }
    // }
    // genDiv.innerHTML = '';


    // - Modify all pertinent collapsible elements ----
    // var coll = document.getElementsByClassName("collapsible-bib-btn");
    // var i;
    //
    // for (i = 0; i < coll.length; i++) {
    //     coll[i].addEventListener("click", function () {
    //         this.classList.toggle("collapsible-bib-active");
    //         var content = this.nextElementSibling;
    //         if (content.style.maxHeight) {
    //             content.style.maxHeight = null;
    //         } else {
    //             content.style.maxHeight = content.scrollHeight + "px";
    //         }
    //     });
    // }

    function collapsible_bib_btn_onClick(key) {
        var btn = document.getElementById("collapsible-bib-btn-"+key);
        btn.classList.toggle("collapsible-bib-active");
        // var content = btn.nextElementSibling;
        var content = document.getElementById("collapsible-bib-content-"+key);
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            var bibtex = document.getElementById("collapsible-bib-bibtex-pre-" + key);
            var links = bibtex.getElementsByTagName('a');
            for (var e of links)
                e.textContent = e.getAttribute("href");
            content.style.maxHeight = content.scrollHeight + "px";
        }
    }
</script> 
