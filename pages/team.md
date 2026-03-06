---
layout: page
permalink: /team/
---
## Team

<!-- Top Section: Leader & Join Us -->
<div id="team-grid">
    <!-- PI and Join Us Row -->
    <div class="team-section mb-3" id="pi-section">
        <h2 class="font-weight-bold mb-4 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
            <!-- <i class="fas fa-user-tie text-primary mr-2"></i> Principal Investigator -->
        </h2>
        <div class="row">
            <!-- PI Card -->
            <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card all" style="transition: all 0.3s ease;">
                <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(0,0,0,0.05) !important;">
                    <div class="card-body p-3 text-left">
                        <span class="badge badge-soft-primary mb-2" style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px;">Principal Investigator</span>
                        <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ site.data.pi.name }}</h5>
                        <p class="text-muted mb-3" style="font-size: 0.85rem; line-height: 1.4;">{{ site.data.pi.affiliation }}</p>
                        <div class="d-flex gap-2">
                            {% if site.data.pi.website %}<a href="{{ site.data.pi.website }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="fas fa-home"></i></a>{% endif %}
                            {% if site.data.pi.scholar %}<a href="https://scholar.google.com/citations?user={{ site.data.pi.scholar }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="ai ai-google-scholar"></i></a>{% endif %}
                            {% if site.data.pi.github %}<a href="https://github.com/{{ site.data.pi.github }}" target="_blank" class="text-dark" style="font-size: 0.9rem;"><i class="fab fa-github"></i></a>{% endif %}
                            {% if site.data.pi.orcid %}<a href="https://orcid.org/{{ site.data.pi.orcid }}" target="_blank" class="text-success" style="font-size: 0.9rem;"><i class="ai ai-orcid"></i></a>{% endif %}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Join Us Card -->
            <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card all ml-auto" style="transition: all 0.3s ease;">
                <div class="card border-0 shadow-lg h-100 text-white" style="border-radius: 16px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);">
                    <div class="card-body p-3 text-center d-flex flex-column justify-content-center align-items-center">
                        <div class="mb-2">
                            <i class="fas fa-user-plus fa-lg"></i>
                        </div>
                        <h5 class="card-title mb-2" style="font-weight: 700;">Join Our Lab</h5>
                        <p class="mb-3 opacity-90" style="font-size: 0.75rem;">We're looking for passionate students</p>
                        <a href="mailto:{{ site.data.pi.email }}" class="btn btn-sm btn-light px-4 py-2" style="border-radius: 8px; background: #3b82f6; color: white; border: none; font-size: 0.8rem; font-weight: 600;">Apply</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Filter Buttons -->
    <div class="d-inline-flex flex-wrap justify-content-center p-1 bg-light rounded-pill mb-3 shadow-sm border mx-auto" id="team-filter" style="display: flex !important;">
        <button class="btn btn-sm active px-4 rounded-pill border-0" data-filter="active">Current</button>
        <button class="btn btn-sm px-4 rounded-pill border-0" data-filter="past">Past</button>
    </div>
                <!-- PhD Students -->
                <div class="team-section phd-section mb-3">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-graduation-cap text-primary mr-2"></i> PhD Students
                    </h4>
                    <div class="row">
                        {% for member in site.data.team_members %}
                        {% if member.role contains "PhD" %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card phd" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(0,0,0,0.05) !important;">
                                <div class="card-body p-3 text-left">
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-3" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                    <div class="d-flex gap-2">
                                        {% if member.scholar %}<a href="https://scholar.google.com/citations?user={{ member.scholar }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="ai ai-google-scholar"></i></a>{% endif %}
                                        {% if member.github %}<a href="https://github.com/{{ member.github }}" target="_blank" class="text-dark" style="font-size: 0.9rem;"><i class="fab fa-github"></i></a>{% endif %}
                                        {% if member.linkedin %}<a href="https://linkedin.com/in/{{ member.linkedin }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="fab fa-linkedin"></i></a>{% endif %}
                                    </div>
                                </div>
                            </div>
                        </div>
                        {% endif %}
                        {% endfor %}
                    </div>
                </div>

                <!-- Master Students -->
                <div class="team-section master-section mb-3">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-user-graduate text-primary mr-2"></i> Master Students
                    </h4>
                    <div class="row">
                        {% for member in site.data.team_members %}
                        {% if member.role contains "Master" %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card master" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(0,0,0,0.05) !important;">
                                <div class="card-body p-3 text-left">
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-3" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                    <div class="d-flex gap-2">
                                        {% if member.scholar %}<a href="https://scholar.google.com/citations?user={{ member.scholar }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="ai ai-google-scholar"></i></a>{% endif %}
                                        {% if member.github %}<a href="https://github.com/{{ member.github }}" target="_blank" class="text-dark" style="font-size: 0.9rem;"><i class="fab fa-github"></i></a>{% endif %}
                                        {% if member.linkedin %}<a href="https://linkedin.com/in/{{ member.linkedin }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="fab fa-linkedin"></i></a>{% endif %}
                                    </div>
                                </div>
                            </div>
                        </div>
                        {% endif %}
                        {% endfor %}
                    </div>
                </div>

                <!-- Undergraduate Students -->
                <div class="team-section undergrad-section mb-3">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-user-tag text-primary mr-2"></i> Undergraduate Students
                    </h4>
                    <div class="row">
                        {% for member in site.data.team_members %}
                        {% if member.role contains "Undergraduate" %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card undergrad" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); border: 1px solid rgba(0,0,0,0.05) !important;">
                                <div class="card-body p-3 text-left">
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-3" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                    <div class="d-flex gap-2">
                                        {% if member.scholar %}<a href="https://scholar.google.com/citations?user={{ member.scholar }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="ai ai-google-scholar"></i></a>{% endif %}
                                        {% if member.github %}<a href="https://github.com/{{ member.github }}" target="_blank" class="text-dark" style="font-size: 0.9rem;"><i class="fab fa-github"></i></a>{% endif %}
                                        {% if member.linkedin %}<a href="https://linkedin.com/in/{{ member.linkedin }}" target="_blank" class="text-primary" style="font-size: 0.9rem;"><i class="fab fa-linkedin"></i></a>{% endif %}
                                    </div>
                                </div>
                            </div>
                        </div>
                        {% endif %}
                        {% endfor %}
                    </div>
                </div>

                <!-- Collaborating Students -->
                {% if site.data.collaborators.size > 0 %}
                <div class="team-section collab-section mb-3 past">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-handshake text-secondary mr-2"></i> Past Collaborators
                    </h4>
                    <div class="row">
                        {% for member in site.data.collaborators %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card past" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(248, 250, 252, 0.8); backdrop-filter: blur(5px); border: 1px solid rgba(0,0,0,0.03) !important;">
                                <div class="card-body p-3 text-left">
                                    <span class="badge badge-secondary mb-2" style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; background-color: #64748b;">{{ member.role }}</span>
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-0" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}

                <!-- Alumni Headers & Sections -->
                {% assign alumni_phd = site.data.alumni | where_exp: "m", "m.role contains 'PhD'" %}
                {% if alumni_phd.size > 0 %}
                <div class="team-section alumni-phd mb-3 past">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-history text-secondary mr-2"></i> Alumni - PhD
                    </h4>
                    <div class="row">
                        {% for member in alumni_phd %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card alumni" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(248, 250, 252, 0.8); backdrop-filter: blur(5px); border: 1px solid rgba(0,0,0,0.03) !important;">
                                <div class="card-body p-3 text-left">
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-0" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}

                {% assign alumni_master = site.data.alumni | where_exp: "m", "m.role contains 'Master'" %}
                {% if alumni_master.size > 0 %}
                <div class="team-section alumni-master mb-3 past">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-history text-secondary mr-2"></i> Alumni - Masters
                    </h4>
                    <div class="row">
                        {% for member in alumni_master %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card alumni" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(248, 250, 252, 0.8); backdrop-filter: blur(5px); border: 1px solid rgba(0,0,0,0.03) !important;">
                                <div class="card-body p-3 text-left">
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-0" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}

                {% assign alumni_undergrad = site.data.alumni | where_exp: "m", "m.role contains 'Undergraduate'" %}
                {% if alumni_undergrad.size > 0 %}
                <div class="team-section alumni-undergrad mb-3 past">
                    <h4 class="font-weight-bold mb-3 text-left border-bottom pb-2" style="color: rgb(33, 37, 41); text-transform: uppercase; letter-spacing: 1px;">
                        <i class="fas fa-history text-secondary mr-2"></i> Alumni - Undergrad
                    </h4>
                    <div class="row">
                        {% for member in alumni_undergrad %}
                        <div class="col-6 col-sm-6 col-md-4 col-lg-3 mb-4 team-card alumni" style="transition: all 0.3s ease;">
                            <div class="card border-0 shadow-sm h-100" style="border-radius: 16px; background: rgba(248, 250, 252, 0.8); backdrop-filter: blur(5px); border: 1px solid rgba(0,0,0,0.03) !important;">
                                <div class="card-body p-3 text-left">
                                    <h5 class="card-title mb-1" style="font-weight: 700; color: #0f172a;">{{ member.name }}</h5>
                                    <p class="text-muted mb-0" style="font-size: 0.85rem; line-height: 1.4;">{{ member.duration }}<br><span class="small opacity-75">{{ member.university }}</span></p>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}
    </div>

<!-- Lab Statistics Section -->
<!-- <div class="row mb-4 text-center">
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
</div> -->

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
    // Targeted filtering: exclude the PI section from being hidden
    const teamSections = document.querySelectorAll('.team-section:not(#pi-section)');
    const teamCards = document.querySelectorAll('.team-card:not(.all)'); // 'all' cards are PI and Join Us

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;

            // Handle section visibility directly by class
            teamSections.forEach(section => {
                if (filter === 'active') {
                    // Show sections that do NOT have the 'past' class
                    section.style.display = section.classList.contains('past') ? 'none' : 'block';
                } else {
                    // Show sections that DO have the 'past' class
                    section.style.display = section.classList.contains('past') ? 'block' : 'none';
                }
            });
        });
    });

    // Initialize the default view (Active)
    const activeBtn = document.querySelector('#team-filter button[data-filter="active"]');
    if (activeBtn) activeBtn.click();
});
</script>
