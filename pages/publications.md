---
layout: page
title: Publications
permalink: /publications/
weight: 3
---

<div class="row">
    <div class="col-md-12 mb-4">
        <label for="paperSearch" class="font-weight-bold text-muted">Filter Publications</label>
        <div class="input-group shadow-sm mb-3">
            <div class="input-group-prepend">
                <span class="input-group-text bg-white border-right-0"><i class="fas fa-search text-muted"></i></span>
            </div>
            <input type="text" class="form-control border-left-0" id="paperSearch" placeholder="Search by title, author, venue, or year...">
        </div>
        <div class="d-flex flex-wrap gap-2" id="typeFilters">
            <button class="btn btn-sm btn-primary active mr-2 mb-2 px-3 filter-btn" data-type="All">All</button>
            <button class="btn btn-sm btn-outline-success mr-2 mb-2 px-3 filter-btn" data-type="Journal">Journals</button>
            <button class="btn btn-sm btn-outline-info mr-2 mb-2 px-3 filter-btn" data-type="Conference">Conferences</button>
            <button class="btn btn-sm btn-outline-secondary mb-2 px-3 filter-btn" data-type="Other">Other</button>
        </div>
    </div>
</div>

<div id="publications-container" class="row">
    <div class="col-12 text-center">
        <div class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Inject local data directly via Liquid
    const papers = [
        {% for p in site.data.journal %}
        {
            "id": "J{{ site.data.journal.size | minus: forloop.index0 }}",
            "title": {{ p.title | jsonify }},
            "authors": {{ p.authors | jsonify }},
            "venue": {{ p.alias | jsonify }},
            "revenue": {{ p.revenue | jsonify }},
            "year": {{ p.revenue | split: "(" | last | split: ")" | first | strip | jsonify }},
            "doi": {{ p.doi | jsonify }},
            "link": {{ p.link | jsonify }},
            "code": {{ p.artifact | jsonify }},
            "slides": {{ p.slide | jsonify }},
            "type": "Journal"
        }{% unless forloop.last %},{% endunless %}
        {% endfor %}
        {% if site.data.journal.size > 0 and site.data.conference.size > 0 %},{% endif %}
        {% for p in site.data.conference %}
        {
            "id": "C{{ site.data.conference.size | minus: forloop.index0 }}",
            "title": {{ p.title | jsonify }},
            "authors": {{ p.authors | jsonify }},
            "venue": {{ p.alias | jsonify }},
            "revenue": {{ p.revenue | jsonify }},
            "year": {{ p.revenue | split: " " | last | strip | jsonify }},
            "doi": {{ p.doi | jsonify }},
            "link": {{ p.link | jsonify }},
            "code": {{ p.artifact | jsonify }},
            "slides": {{ p.slide | jsonify }},
            "acceptanceRate": {{ p.rate | jsonify }},
            "type": "Conference"
        }{% unless forloop.last %},{% endunless %}
        {% endfor %}
        {% if site.data.conference.size > 0 and site.data.paper.size > 0 %},{% endif %}
        {% for p in site.data.paper %}
        {
            "id": "O{{ site.data.paper.size | minus: forloop.index0 }}",
            "title": {{ p.title | jsonify }},
            "authors": {{ p.authors | jsonify }},
            "venue": {{ p.alias | jsonify }},
            "revenue": {{ p.revenue | jsonify }},
            "year": {{ p.revenue | split: " " | last | strip | jsonify }},
            "doi": {{ p.doi | jsonify }},
            "link": {{ p.link | jsonify }},
            "code": {{ p.artifact | jsonify }},
            "slides": {{ p.slide | jsonify }},
            "type": "Other"
        }{% unless forloop.last %},{% endunless %}
        {% endfor %}
    ];

    // Initial render
    let currentFiltered = papers;
    let selectedType = 'All';

    renderPapers(papers);
    setupSearch(papers);
    setupTypeFilters(papers);
    
    function renderPapers(papersList) {
        const container = document.getElementById('publications-container');
        container.innerHTML = '';
        
        if (papersList.length === 0) {
             container.innerHTML = '<div class="col-12 text-center text-muted p-5">No papers found matching your search.</div>';
             return;
        }

        papersList.forEach(p => {
            let badges = '';
            if (p.id) badges += `<span class="badge badge-primary mr-1">${p.id}</span>`;
            if (p.type) {
                const typeClass = p.type === 'Journal' ? 'badge-success' : (p.type === 'Conference' ? 'badge-info' : 'badge-secondary');
                badges += `<span class="badge ${typeClass} mr-1">${p.type}</span>`;
            }
            if (p.acceptanceRate) badges += `<span class="badge badge-warning mr-1">Acceptance: ${p.acceptanceRate}</span>`;
            if (p.venue) badges += `<span class="badge badge-light border mr-1">${p.venue}</span>`;
            
            let buttons = '';
            const pdfLink = p.link || (p.doi && p.doi.includes('.pdf') ? p.doi : null);
            if (pdfLink) buttons += `<a href="${pdfLink}" target="_blank" class="btn btn-outline-danger btn-sm mr-1 mt-1"><i class="fas fa-file-pdf"></i> PDF</a>`;
            if (p.doi && !p.doi.includes('.pdf')) buttons += `<a href="${p.doi}" target="_blank" class="btn btn-outline-secondary btn-sm mr-1 mt-1"><i class="fas fa-link"></i> DOI</a>`;
            if (p.code) buttons += `<a href="${p.code}" target="_blank" class="btn btn-outline-dark btn-sm mr-1 mt-1"><i class="fab fa-github"></i> Code</a>`;
            if (p.slides) buttons += `<a href="${p.slides}" target="_blank" class="btn btn-outline-info btn-sm mr-1 mt-1"><i class="fas fa-chalkboard-teacher"></i> Slides</a>`;
            
            // BibTeX button
            buttons += `<button onclick='copyBibTeX(${JSON.stringify(p).replace(/'/g, "&apos;")})' class="btn btn-outline-primary btn-sm mr-1 mt-1"><i class="fas fa-quote-right"></i> BibTeX</button>`;

            const card = `
            <div class="col-12 mb-3">
                <div class="card border-0 shadow-sm h-100 hover-effect">
                    <div class="card-body py-3">
                         <div class="d-flex justify-content-between align-items-start">
                            <h6 class="card-title mb-1 font-weight-bold" style="font-size: 1.1rem; line-height: 1.3;">${p.title}</h6>
                            <small class="text-muted font-weight-bold ml-2">${p.year || ''}</small>
                         </div>
                         <div class="mb-1">
                            <small class="text-muted">${p.authors || ''}</small>
                         </div>
                         <div class="mb-2">
                             <em><small class="text-secondary" style="font-size: 0.85rem;">${p.revenue || ''}</small></em>
                         </div>
                         <div class="mb-3">
                            ${badges}
                         </div>
                         <div class="d-flex flex-wrap">
                            ${buttons}
                         </div>
                    </div>
                </div>
            </div>`;
            container.innerHTML += card;
        });
    }

    function setupSearch(papersData) {
        const input = document.getElementById('paperSearch');
        if (!input) return;
        input.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            const filtered = papersData.filter(p => 
                (selectedType === 'All' || p.type === selectedType) &&
                ((p.title && p.title.toLowerCase().includes(term)) || 
                 (p.authors && p.authors.toLowerCase().includes(term)) ||
                 (p.venue && p.venue.toLowerCase().includes(term)) ||
                 (p.year && p.year.includes(term)) ||
                 (p.id && p.id.toLowerCase().includes(term)))
            );
            currentFiltered = filtered;
            renderPapers(filtered);
        });
    }

    function setupTypeFilters(papersData) {
        const btns = document.querySelectorAll('.filter-btn');
        btns.forEach(btn => {
            btn.addEventListener('click', () => {
                btns.forEach(b => {
                    b.classList.remove('active');
                    if (b.dataset.type === 'All') b.className = 'btn btn-sm btn-outline-primary mr-2 mb-2 px-3 filter-btn';
                    else if (b.dataset.type === 'Journal') b.className = 'btn btn-sm btn-outline-success mr-2 mb-2 px-3 filter-btn';
                    else if (b.dataset.type === 'Conference') b.className = 'btn btn-sm btn-outline-info mr-2 mb-2 px-3 filter-btn';
                    else b.className = 'btn btn-sm btn-outline-secondary mb-2 px-3 filter-btn';
                });
                
                selectedType = btn.dataset.type;
                btn.classList.add('active');
                // Set solid color for active
                if (selectedType === 'All') btn.className = 'btn btn-sm btn-primary active mr-2 mb-2 px-3 filter-btn';
                else if (selectedType === 'Journal') btn.className = 'btn btn-sm btn-success active mr-2 mb-2 px-3 filter-btn';
                else if (selectedType === 'Conference') btn.className = 'btn btn-sm btn-info active mr-2 mb-2 px-3 filter-btn';
                else btn.className = 'btn btn-sm btn-secondary active mb-2 px-3 filter-btn';

                const term = document.getElementById('paperSearch').value.toLowerCase();
                const filtered = papersData.filter(p => 
                    (selectedType === 'All' || p.type === selectedType) &&
                    ((p.title && p.title.toLowerCase().includes(term)) || 
                     (p.authors && p.authors.toLowerCase().includes(term)) ||
                     (p.venue && p.venue.toLowerCase().includes(term)) ||
                     (p.year && p.year.includes(term)))
                );
                currentFiltered = filtered;
                renderPapers(filtered);
            });
        });
    }
});

function copyBibTeX(p) {
    const firstAuthor = p.authors.split(',')[0].split(' ').pop();
    const key = `${firstAuthor}${p.year}${p.title.split(' ')[0].replace(/[^a-zA-Z]/g, '')}`;
    const bibType = p.type === 'Journal' ? 'article' : 'inproceedings';
    const venueField = p.type === 'Journal' ? 'journal' : 'booktitle';
    
    let bib = `@${bibType}{${key},\n`;
    bib += `  title = {${p.title}},\n`;
    bib += `  author = {${p.authors}},\n`;
    bib += `  ${venueField} = {${p.revenue}},\n`;
    bib += `  year = {${p.year}},\n`;
    if (p.doi) bib += `  doi = {${p.doi.replace('https://doi.org/', '')}},\n`;
    bib += `}`;

    navigator.clipboard.writeText(bib).then(() => {
        const btn = event.target.closest('button');
        const originalHtml = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
        btn.classList.add('btn-success');
        btn.classList.remove('btn-outline-primary');
        setTimeout(() => {
            btn.innerHTML = originalHtml;
            btn.classList.remove('btn-success');
            btn.classList.add('btn-outline-primary');
        }, 2000);
    });
}
</script>
