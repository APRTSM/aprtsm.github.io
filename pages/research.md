---
layout: page
title: Research
permalink: /research/
weight: 1
project_tags: [bug reports, bug localization, fault localization, bug characteristics, program analysis, program comprehension, mining software repositories, software metrics, fix patterns, patches, program repair, debugging, fix ingredients, code change actions, donor code, patch generation, code representations, patch assessment, bug classification, repository analysis, vulnerability repair, bug detection]

---
## Research Topics


<div class="container">
  <div class="row">
    <div class="col-md-4 mb-4">
      <div class="card h-100 shadow-sm hover-effect">
        <div class="card-body text-center">
          <div class="mb-3">
            <i class="fas fa-magic fa-3x text-primary"></i>
          </div>
          <h5 class="card-title">Automated Program Repair</h5>
          <p class="card-text text-muted">Developing techniques to automatically fix software bugs without human intervention.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100 shadow-sm hover-effect">
        <div class="card-body text-center">
          <div class="mb-3">
            <i class="fas fa-crosshairs fa-3x text-primary"></i>
          </div>
          <h5 class="card-title">Automated Fault Localization</h5>
          <p class="card-text text-muted">Pinpointing the root cause of failures to speed up the debugging process.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100 shadow-sm hover-effect">
        <div class="card-body text-center">
          <div class="mb-3">
            <i class="fas fa-project-diagram fa-3x text-primary"></i>
          </div>
          <h5 class="card-title">Fix Pattern Mining</h5>
          <p class="card-text text-muted">Learning from historical bug fixes to generate common repair patterns.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100 shadow-sm hover-effect">
        <div class="card-body text-center">
          <div class="mb-3">
            <i class="fas fa-database fa-3x text-primary"></i>
          </div>
          <h5 class="card-title">Mining Software Repositories</h5>
          <p class="card-text text-muted">Analyzing codebases and version history to understand software evolution.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100 shadow-sm hover-effect">
        <div class="card-body text-center">
          <div class="mb-3">
            <i class="fas fa-robot fa-3x text-primary"></i>
          </div>
          <h5 class="card-title">AI for SE</h5>
          <p class="card-text text-muted">Applying machine learning and natural language processing to solve SE problems.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4 mb-4">
      <div class="card h-100 shadow-sm hover-effect">
        <div class="card-body text-center">
          <div class="mb-3">
            <i class="fas fa-chart-line fa-3x text-primary"></i>
          </div>
          <h5 class="card-title">Empirical Software Engineering</h5>
          <p class="card-text text-muted">Conducting studies to evaluate tools and understand developer behavior.</p>
        </div>
      </div>
    </div>
  </div>
</div>

##### Prospective Students:

<div class="alert alert-primary">
 <strong>We are always looking for motivated new team members! </strong><br>
</div>
<div class="alert alert-info text-left">
	 <strong>Keywords: </strong><br>
	<p class="card-text">
		{%- for tag in page.project_tags -%}
		<span class="badge badge-pill text-primary border border-primary ml-1">{{ tag }}</span>
		{%- endfor -%}
	</p>
</div>
<div class="alert alert-success text-left">
 Students who wish to be involved in APR-TSM research can apply <a href="https://docs.google.com/forms/d/e/1FAIpQLSeb78YDUNAZC32LCr-WQjvN8iDj7D73c9Oipo_7MypcFLWnlw/viewform?usp=sharing" target="_blank" class="alert-link"> here! </a>
</div>

 
##### Research Projects:
{% include projects/pj-search.html %}
{% include projects/index.html %}



