/**
 * This file contains an on action script to allow for the collapsible bib entries to function.
 * and therefore must be included in any file where you want them to work in.
 */
function collapsible_soft_btn_onClick(key) {
    var btn = document.getElementById("collapsible-soft-btn-"+key);
    btn.classList.toggle("collapsible-soft-active");
    // var content = btn.nextElementSibling;
    var content = document.getElementById("collapsible-soft-content-"+key);
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}
function collapsible_people_btn_onClick(key) {
    var btn = document.getElementById("collapsible-people-btn-"+key);
    btn.classList.toggle("collapsible-active");
    // var content = btn.nextElementSibling;
    var content = document.getElementById("collapsible-people-content-"+key);
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}
function collapsible_edu_btn_onClick(key) {
    var btn = document.getElementById("collapsible-edu-btn-"+key);
    btn.classList.toggle("collapsible-active");
    // var content = btn.nextElementSibling;
    var content = document.getElementById("collapsible-edu-content-"+key);
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}


/**
 * Perform the operations necessary to collapse and expand a drop down bibliography entry. 
 * @param {*} key The reference key generated for the entry 
 */
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