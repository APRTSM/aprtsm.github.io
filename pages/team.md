---
layout: page
permalink: /team/
---
## Team

<!-- Top Section: Leader & Join Us -->
<div class="row mb-5">
    <!-- Leader Spotlight -->
    <div class="col-lg-8 mb-4 mb-lg-0">
        <div class="card border-0 shadow h-100" style="border-radius: 24px; overflow: hidden;">
            <div class="row no-gutters align-items-center h-100">
                <div class="col-md-4 p-0 h-100">
                    <div class="p-4 text-center h-100 d-flex align-items-center justify-content-center" style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);">
                        <img src="{{ site.url }}{{ site.baseurl }}/img/{{ site.data.pi.photo }}" alt="{{ site.data.pi.name }}" class="img-fluid rounded-circle shadow" style="width: 120px; height: 120px; object-fit: cover;  border: 4px solid #fff;">
                    </div>
                </div>
                <div class="col-md-8">
                    <div class="card-body glass-card p-4" style="background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(10px); border-left: 1px solid rgba(255, 255, 255, 0.5);">
                        <span class="badge badge-soft-primary mb-2 px-3 py-1">Principal Investigator</span>
                        <h3 class="card-title mb-2" style="color: #0f172a;">{{ site.data.pi.name }}</h3>
                        <p class="text-muted mb-2" style="font-size: 0.95rem;">{{ site.data.pi.affiliation }}</p>
                        <!-- Bio removed as requested -->
                        <div class="d-flex gap-3 justify-content-center justify-content-md-start mt-3">
                            {% if site.data.pi.website %}<a href="{{ site.data.pi.website }}" class="btn btn-outline-primary btn-sm rounded-circle p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-home"></i></a>{% endif %}
                            {% if site.data.pi.email %}<a href="mailto:{{ site.data.pi.email }}" class="btn btn-outline-primary btn-sm rounded-circle p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;"><i class="fas fa-envelope"></i></a>{% endif %}
                            {% if site.data.pi.scholar %}<a href="https://scholar.google.com/citations?user={{ site.data.pi.scholar }}" class="btn btn-outline-primary btn-sm rounded-circle p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;"><i class="ai ai-google-scholar"></i></a>{% endif %}
                            {% if site.data.pi.github %}<a href="https://github.com/{{ site.data.pi.github }}" class="btn btn-outline-primary btn-sm rounded-circle p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;"><i class="fab fa-github"></i></a>{% endif %}
                            {% if site.data.pi.orcid %}<a href="https://orcid.org/{{ site.data.pi.orcid }}" class="btn btn-outline-primary btn-sm rounded-circle p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;"><i class="ai ai-orcid"></i></a>{% endif %}
                            {% if site.data.pi.researchgate %}<a href="{{ site.data.pi.researchgate }}" class="btn btn-outline-primary btn-sm rounded-circle p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;"><i class="ai ai-researchgate"></i></a>{% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Join Us Card -->
    <div class="col-lg-4">
        <div class="card border-0 shadow-lg h-100 text-white" style="border-radius: 24px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);">
            <div class="card-body text-center p-4 d-flex flex-column justify-content-center align-items-center">
                <div class="mb-3">
                    <div class="d-inline-flex align-items-center justify-content-center rounded-circle p-3 icon-circle" style="background-color: rgba(255, 255, 255, 0.1);">
                        <i class="fas fa-user-plus fa-2x"></i>
                    </div>
                </div>
                <h4 class="card-title mb-2">Join Our Research Lab</h4>
                <p class="mb-3 opacity-90">We're looking for passionate students at all levels</p>
                <a href="mailto:{{ site.data.pi.email }}" class="btn btn-light px-4" style="border-radius: 12px; background: #3b82f6; color: white; border: none;">Apply Now</a>
            </div>
        </div>
    </div>
</div>

<!-- Filter Navigation Container / Research Projects -->
<div class="card border-0 shadow-sm mb-4">
    <div class="card-header bg-white border-0" id="projectsHeading" style="cursor: pointer;" data-toggle="collapse" data-target="#projectsCollapse" aria-expanded="true" aria-controls="projectsCollapse">
        <h5 class="mb-0 font-weight-bold d-flex align-items-center justify-content-between">
            <span style="color: #0f172a;">Research Projects</span>
            <i class="fas fa-chevron-down text-muted"></i>
        </h5>
    </div>
    <div id="projectsCollapse" class="collapse show" aria-labelledby="projectsHeading">
        <div class="card-body">
            {% include projects_filtered.html %}
        </div>
    </div>
</div>

<!-- Team Directory Section -->
<div class="card border-0 shadow-sm mb-5">
    <div class="card-header bg-white border-0" id="teamHeading" style="cursor: pointer;" data-toggle="collapse" data-target="#teamCollapse" aria-expanded="true" aria-controls="teamCollapse">
        <h5 class="mb-0 font-weight-bold d-flex align-items-center justify-content-between">
            <span style="color: #0f172a;">Team Directory</span>
            <i class="fas fa-chevron-down text-muted"></i>
        </h5>
    </div>

    <div id="teamCollapse" class="collapse show" aria-labelledby="teamHeading">
        <div class="card-body text-center">
             <div class="d-inline-flex flex-wrap justify-content-center p-1 bg-light rounded-pill mb-4 shadow-sm border" id="team-filter">
                <button class="btn btn-sm active px-4 rounded-pill border-0" data-filter="all">All</button>
                <button class="btn btn-sm px-4 rounded-pill border-0" data-filter="phd">PhD</button>
                <button class="btn btn-sm px-4 rounded-pill border-0" data-filter="master">Masters</button>
                <button class="btn btn-sm px-4 rounded-pill border-0" data-filter="undergrad">Undergrad</button>
                <button class="btn btn-sm px-4 rounded-pill border-0" data-filter="alumni">Alumni</button>
            </div>

            <!-- Compact Team Table -->
            <div class="table-responsive">
                <table class="table table-hover table-sm" id="team-table" style="table-layout: fixed; width: 100%;">
                    <thead class="bg-light text-left">
                        <tr>
                            <th class="text-left" style="width: 30%;">Name</th>
                            <th style="width: 25%;">Role</th>
                            <th style="width: 25%;">University</th>
                            <th style="width: 20%;">Duration</th>
                        </tr>
                    </thead>
                    <tbody class="small text-left">
                        <!-- Current Members -->
                        {% for member in site.data.team_members %}
                        {% assign filter_class = "" %}
                        {% if member.role contains "PhD" %}{% assign filter_class = "phd" %}{% endif %}
                        {% if member.role contains "Master" %}{% assign filter_class = "master" %}{% endif %}
                        {% if member.role contains "Undergraduate" %}{% assign filter_class = "undergrad" %}{% endif %}
                        
                        <tr class="team-row {{ filter_class }}" style="transition: all 0.3s ease;">
                            <td class="align-middle text-left">
                                <div class="d-flex align-items-center">
                                    <strong>{{ member.name }}</strong>
                                </div>
                            </td>
                            <td class="align-middle"><span class="badge badge-primary">{{ member.role }}</span></td>
                            <td class="align-middle text-muted small">{{ member.university }}</td>
                            <td class="align-middle text-muted small">{{ member.duration }}</td>
                        </tr>
                        {% endfor %}
                        
                        <!-- Alumni -->
                        {% for member in site.data.alumni %}
                        <tr class="team-row alumni" style="transition: all 0.3s ease; opacity: 0.75;">
                            <td class="align-middle text-left">
                                <div class="d-flex align-items-center">
                                    <strong>{{ member.name }}</strong>
                                </div>
                            </td>
                            <td class="align-middle"><span class="badge badge-secondary">{{ member.role }}</span></td>
                            <td class="align-middle text-muted small">{{ member.university }}</td>
                            <td class="align-middle text-muted small">{{ member.duration }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- Lab Statistics Section -->
<div class="row mb-4 text-center">
  <div class="col-md-3 col-sm-6 mb-3">
    <div class="stat-card p-3">
      <div class="stat-icon mb-2">
        <i class="fas fa-users fa-2x text-primary"></i>
      </div>
      <h3 class="stat-number mb-1">{{ site.data.team_members.size }}</h3>
      <p class="stat-label text-muted mb-0">Current Members</p>
    </div>
  </div>
  <div class="col-md-3 col-sm-6 mb-3">
    <div class="stat-card p-3">
      <div class="stat-icon mb-2">
        <i class="fas fa-graduation-cap fa-2x text-success"></i>
      </div>
      <h3 class="stat-number mb-1">{{ site.data.alumni.size }}</h3>
      <p class="stat-label text-muted mb-0">Alumni Supervised</p>
    </div>
  </div>
  <div class="col-md-3 col-sm-6 mb-3">
    <div class="stat-card p-3">
      <div class="stat-icon mb-2">
        <i class="fas fa-lightbulb fa-2x text-warning"></i>
      </div>
      <h3 class="stat-number mb-1">{{ site.data.active_projects.size }}</h3>
      <p class="stat-label text-muted mb-0">Active Projects</p>
    </div>
  </div>
  <div class="col-md-3 col-sm-6 mb-3">
    <div class="stat-card p-3">
      <div class="stat-icon mb-2">
        <i class="fas fa-flask fa-2x text-info"></i>
      </div>
      <h3 class="stat-number mb-1">{{ site.data.past_projects.size }}</h3>
      <p class="stat-label text-muted mb-0">Completed Projects</p>
    </div>
  </div>
</div>

<style>
  .stat-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 16px;
    transition: all 0.3s ease;
    border: 1px solid #e9ecef;
  }
  .stat-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  }
  .stat-number {
    font-size: 2rem;
    font-weight: 700;
    color: #1e293b;
  }
  .stat-label {
    font-size: 0.85rem;
    font-weight: 500;
  }
  .stat-icon {
    opacity: 0.8;
  }

  .gap-2 { gap: 0.6rem; }
  .gap-1 { gap: 0.3rem; }
  
  #team-filter .btn { font-size: 0.8rem; font-weight: 600; color: #64748b; background: transparent; }
  #team-filter .btn:hover { color: #334155; }
  #team-filter .btn.active { background-color: #ffffff !important; color: #0f172a !important; shadow: 0 2px 4px rgba(0,0,0,0.05); }
  
  .badge-soft-primary { background-color: #e0f2fe; color: #0369a1; }
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('#team-filter button');
    const rows = document.querySelectorAll('.team-row');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;

            rows.forEach(row => {
                if (filter === 'all' || row.classList.contains(filter)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    });
});
</script>
