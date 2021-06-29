/**
 * A script to build the publications page on the clients side.
 * Getting rid of the need for jekyll-scholar.
 * 
 * Make sure to include the citation.min.js in the header as well
 * as define `Cite` as teh module there as well.
 */

// const Cite = require('citations-js');


function generate_publications(bib_url) {
    console.log(`URL of pubs.bib: ${bib_url}\n`);
    var out_div = document.getElementById("collapsible-bib-gen");
    out_div.innerHTML += `
    <div align="center">
        <img src="https://miro.medium.com/max/1158/1*9EBHIOzhE1XfMYoKz1JcsQ.gif" 
            class="loading-symbol" 
            alt="Loading..."/>
    </div>
    `;
    $.ajax({
        url: bib_url,
        success: function(data) {
            var bib_data = new String(data);
            out_div.innerHTML += `<textarea id="bibtex_entry" style="display: none;">${bib_data}</textarea>`;
            // console.log(`The contents of the BibTeX File: \n${bib_data}\n\n============\n`);
            // var pubs_bib = new Cite(bib_url);
            __generate_publications(bib_data, out_div);
        }
    });
}

function __generate_publications(bib_data, out_div) {
    let pubs_csl = new Cite();
    var pubs_split = bib_data.split(/\n@/);
    console.log(pubs_split);
    for (var entry of pubs_split) {
        if (entry == '')
            continue;
        entry = '@'+entry;
        pubs_csl.add(entry);
        // pubs_csl.add({data: entry, forceType: "@bibtex/text" });
    }
    // let pubs_csl = new Cite(bib_data);
    console.log(pubs_csl);
    
    var pubs_json = pubs_csl.data;
    console.log(pubs_json);
}



// * This is the basic template to use for making an bib entry in the drop down format.
// <!-- This is a generated entry for a publication citation -->
/* <div class="collapsible-bib-entry">
    <div class="collapsible-bib-btn" 
            id="collapsible-bib-btn-{{key}}" 
            onClick="collapsible_bib_btn_onClick('{{key}}')">
        <h3 class="collapsible-bib-title">
            <svg viewBox="-1 0 17 16" class="gs_or_svg"><path d="M1.5 3.5v5h2v.375L1.75 12.5h3L6.5 8.875V3.5zM9.5 3.5v5h2v.375L9.75 12.5h3L14.5 8.875V3.5z"></path></svg> 
            {{ entry.title | markdownify | strip_html | smartify }}
        </h3>
        <p class="collapsible-bib-authors"> {{ entry.author | strip_html }} </p> 
    </div>
    <div class="collapsible-bib-content" id="collapsible-bib-content-{{key}}">
        {% if entry.note %}
        <div class="collapsible-bib-note">
            <h4>note</h4>
            <p>{{- entry.note | markdownify | strip_html -}}</p>
        </div>
        {% endif %}
        {% if entry.abstract %}
        <div class="collapsible-bib-abstract">
            <h4><i>abstract</i></h4>
            <p>{{- entry.abstract | markdownify | strip_html | smartify -}}</p>
        </div>
        {% endif %}
        <div class="collapsible-bib-reference">
            <h4>Citation <span class="colapsible-bib-refrence-style">
                {%- if page.scholar.style -%}
                    {{- page.scholar.style  | replace "-", " " 
                                            | replace "_", " " -}}
                {%- else -%}
                    {{- site.scholar.style  | replace "-", " " 
                                            | replace "_", " " -}}
                {%- endif -%}
            </span></h4>
            {{ reference }}
        </div>
        <div class="collapsible-bib-bibtex">
            <h4>BibTeX</h4>
            <pre id="collapsible-bib-bibtex-pre-{{key}}">{{ entry.bibtex }}</pre>
        </div>
    </div>
</div> */




