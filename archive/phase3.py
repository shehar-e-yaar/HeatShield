import re

css_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\style.css'
html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'

# --- PHASE 3 CSS ---
new_css = """
/* PHASE 3: COMPONENT STYLES */

/* Common Glass Card */
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: var(--glass-shadow);
  transition: all 0.3s ease;
}
.glass-card:hover {
  background: var(--glass-bg-hover);
  border-color: rgba(255,255,255,0.15);
}

/* Hero Area (Stats Bar Replacement) */
.hero-area {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 1.5rem;
}

.hero-main {
  display: flex;
  align-items: center;
  gap: 2rem;
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
}

.gauge-container {
  position: relative;
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: conic-gradient(var(--primary) 0%, var(--heat-accent) 50%, var(--critical) 75%, transparent 75%);
  display: flex;
  align-items: center;
  justify-content: center;
}
.gauge-container::before {
  content: '';
  position: absolute;
  width: 100px; height: 100px;
  background: var(--bg-base);
  border-radius: 50%;
}
.gauge-value {
  position: relative;
  font-size: 2.5rem;
  font-weight: 300;
  color: var(--text-primary);
}

.hero-info .title {
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}
.hero-info .name {
  font-size: 2rem;
  font-weight: 400;
  margin-bottom: 0.5rem;
}

.kpi-card {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.kpi-card.heat {
  box-shadow: 0 0 20px rgba(255, 138, 61, 0.1);
  border-color: rgba(255, 138, 61, 0.2);
}
.kpi-label {
  font-size: 0.65rem;
  letter-spacing: 0.1em;
  color: var(--text-secondary);
  text-transform: uppercase;
  margin-bottom: 0.5rem;
}
.kpi-val {
  font-size: 2rem;
  font-weight: 300;
  color: var(--text-primary);
}
.kpi-sub {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.5rem;
}

/* Priority Grid */
.priority-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 1.5rem;
}
.p-factor {
  background: rgba(0,0,0,0.2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
}
.p-factor .lbl { font-size: 0.65rem; color: var(--text-secondary); letter-spacing: 0.05em; text-transform: uppercase;}
.p-factor .val { font-size: 1.5rem; font-weight: 300; margin-top: 0.25rem; }

/* Sensor Strip */
.sensor-strip {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}
.sensor {
  flex: 1;
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 0.75rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.sensor .s-val { font-size: 1.25rem; font-weight: 400; }
.sensor .s-lbl { font-size: 0.6rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; margin-top: 0.25rem;}
.sensor-status { font-size: 0.5rem; color: var(--success); letter-spacing: 0.1em; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 4px; }
.sensor-status::before { content: ''; width: 6px; height: 6px; background: var(--success); border-radius: 50%; box-shadow: 0 0 5px var(--success); }

/* Surface Analysis */
.surface-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}
.surface-row .lbl { width: 80px; font-size: 0.75rem; color: var(--text-secondary); }
.surface-row .track { flex: 1; height: 6px; background: rgba(0,0,0,0.3); border-radius: 3px; overflow: hidden; }
.surface-row .fill { height: 100%; border-radius: 3px; }
.surface-row .val { width: 40px; font-size: 0.75rem; font-weight: 500; text-align: right; }
.surface-insight {
  margin-top: 1.5rem;
  padding: 1rem;
  background: rgba(77, 163, 255, 0.05);
  border-left: 2px solid var(--primary);
  font-size: 0.85rem;
  color: var(--text-secondary);
}
.surface-insight strong { color: var(--text-primary); display: block; margin-bottom: 0.25rem; }

/* Budget Rows */
.budget-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid var(--border);
  font-size: 0.85rem;
}
.budget-row:last-child { border-bottom: none; }
.budget-row .status { font-size: 0.7rem; letter-spacing: 0.1em; display: flex; align-items: center; gap: 0.5rem; }
.budget-row.funded .status { color: var(--success); }
.budget-row.unfunded .status { color: var(--text-muted); }

/* What-If Simulation */
.sim-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(0,0,0,0.2);
  border-radius: 16px;
  padding: 1.5rem;
  margin-top: 1.5rem;
}
.sim-block { text-align: center; }
.sim-block .lbl { font-size: 0.65rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; }
.sim-block .val { font-size: 2rem; font-weight: 300; margin-top: 0.25rem; }
.sim-arrow { color: var(--primary); opacity: 0.5; }
.sim-diff { color: var(--success); font-weight: 500; font-size: 0.85rem; margin-top: 0.5rem; }

/* Impact Section */
.impact-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1rem;
}
.impact-grid .val { font-size: 2.5rem; font-weight: 300; color: var(--text-primary); }
.impact-grid .lbl { font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.5rem; }
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css)


# --- PHASE 3 HTML/JS REPLACEMENT ---
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update stats-bar to hero-area
html = html.replace('<div class="stats-bar">', '<div class="hero-area" id="hero-area">')

# 2. Re-write updateStats()
new_updateStats = """
    function updateStats() {
      if (rankedAreas.length === 0) return;
      const top = rankedAreas[0];
      
      const tempFieldC = isNightMode ? 'night_temp_c' : 'avg_temp_c';
      let sumC = 0, count = 0;
      AREAS.forEach(a => { sumC += (a[tempFieldC] !== undefined ? a[tempFieldC] : (isNightMode ? a.avg_temp_c * 0.75 : a.avg_temp_c)); count++; });
      const avgC = (sumC / count).toFixed(1);
      const top5Pop = rankedAreas.slice(0, 5).reduce((sum, a) => sum + a.population, 0);

      const heroHTML = `
        <div class="glass-card hero-main">
          <div class="gauge-container" style="background: conic-gradient(${getColorForScore(top.priority_score)} ${top.priority_score}%, transparent ${top.priority_score}%)">
            <div class="gauge-value">${top.priority_score}</div>
          </div>
          <div class="hero-info">
            <div class="title">Heat Risk Analysis</div>
            <div class="name">${top.name}</div>
            <div class="priority-tag ${getPriorityTag(top.priority_score).class}">${getPriorityTag(top.priority_score).label} RISK</div>
          </div>
        </div>
        <div class="glass-card kpi-card heat">
          <div class="kpi-label">Heat Index</div>
          <div class="kpi-val">${avgC}°C</div>
          <div class="kpi-sub"><i data-lucide="thermometer"></i> High thermal stress</div>
        </div>
        <div class="glass-card kpi-card">
          <div class="kpi-label">Residents Exposed</div>
          <div class="kpi-val">${(top5Pop/1000).toFixed(1)}K</div>
          <div class="kpi-sub"><i data-lucide="users"></i> Top 5 areas</div>
        </div>
        <div class="glass-card kpi-card">
          <div class="kpi-label">Areas Scanned</div>
          <div class="kpi-val">${AREAS.length}</div>
          <div class="kpi-sub"><i data-lucide="scan"></i> Live telemetry</div>
        </div>
      `;
      document.getElementById('hero-area').innerHTML = heroHTML;
      lucide.createIcons();
    }
"""
html = re.sub(r'function updateStats\(\) \{.*?(?=function renderRankingList)', new_updateStats.strip() + '\n\n    ', html, flags=re.DOTALL)

# 3. Re-write renderDetailCard()
new_detailCard = """
    function renderDetailCard(area) {
      if (!area) return;
      const card = document.getElementById('detail-card');
      const tag = getPriorityTag(area.priority_score);

      card.innerHTML = `
        <div class="detail-header">
          <div>
            <div class="priority-tag ${tag.class}">${tag.label} RISK</div>
            <h2 style="font-size:2rem; font-weight:300; margin-top:0.5rem;">${area.name}</h2>
          </div>
          <div style="text-align:right;">
            <div style="font-size:3rem; font-weight:300; color:${getColorForScore(area.priority_score)}">${area.priority_score}<span style="font-size:1rem;color:var(--text-muted)">/100</span></div>
          </div>
        </div>
        
        <div class="priority-grid">
          <div class="p-factor"><div class="lbl">Heat Risk</div><div class="val">${Math.round(area.norm_scores?.heat || 0)}</div></div>
          <div class="p-factor"><div class="lbl">Vulnerable</div><div class="val">${Math.round(area.norm_scores?.pop || 0)}</div></div>
          <div class="p-factor"><div class="lbl">Trees</div><div class="val">${Math.round(area.norm_scores?.tree || 0)}</div></div>
          <div class="p-factor"><div class="lbl">Impervious</div><div class="val">${area.pavement_pct}</div></div>
        </div>

        <div class="sensor-strip">
          <div class="sensor">
            <div class="sensor-status">LIVE</div>
            <div class="s-val ${getWetBulbClass(area.wet_bulb_c)}">${area.wet_bulb_c || '--'}°</div>
            <div class="s-lbl">Wet Bulb</div>
          </div>
          <div class="sensor">
            <div class="sensor-status">LIVE</div>
            <div class="s-val">${area.humidity_pct || '--'}%</div>
            <div class="s-lbl">Humidity</div>
          </div>
          <div class="sensor">
            <div class="sensor-status">LIVE</div>
            <div class="s-val">${area.aqi || '--'}</div>
            <div class="s-lbl">AQI</div>
          </div>
          <div class="sensor">
            <div class="sensor-status">LIVE</div>
            <div class="s-val">${area.solar_ghi || '--'}</div>
            <div class="s-lbl">Solar W/m²</div>
          </div>
        </div>
      `;
    }
"""
html = re.sub(r'function renderDetailCard\(area\) \{.*?(?=function updateSurfaceAnalysis)', new_detailCard.strip() + '\n\n    ', html, flags=re.DOTALL)


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
