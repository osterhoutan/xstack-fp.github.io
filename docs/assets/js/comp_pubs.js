/**
 * A script to build the publications page on the clients side.
 * Getting rid of the need for jekyll-scholar.
 * 
 * Make sure to include the citation.min.js in the header as well
 * as define `Cite` as teh module there as well.
 */


entry_html = `
<!-- This is a generated entry for a publication citation -->
<div class="collapsible-bib-entry">
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
</div>
`



