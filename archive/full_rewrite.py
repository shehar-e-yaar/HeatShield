import re

css_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\style.css'
html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'

css_content = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ========================================= */
/* PHASE 1: DESIGN TOKENS                    */
/* ========================================= */
:root {
  --bg-base: #07111F;
  --bg-sec: #0B1830;
  --primary: #4DA3FF;
  --secondary: #62D9FF;
  --heat-accent: #FF8A3D;
  --critical: #FF5A45;
  --success: #32D583;
  --text-primary: #F5F8FC;
  --text-secondary: #A9B8CC;
  --text-muted: #718198;
  --border: rgba(255,255,255,0.12);
  --glass-bg: rgba(255,255,255,0.06);
  --glass-bg-hover: rgba(255,255,255,0.10);
  --glass-blur: blur(25px);
  --glass-shadow: 0 12px 40px rgba(0, 0, 0, 0.25);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

/* ========================================= */
/* PHASE 2: LAYOUT SHELL & BACKGROUND        */
/* ========================================= */
body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-base);
  color: var(--text-primary);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
}

/* Atmospheric Glows */
body::before {
  content: ''; position: fixed; top: -20%; left: -10%; width: 60vw; height: 60vw;
  background: radial-gradient(circle, rgba(77, 163, 255, 0.08) 0%, transparent 60%);
  filter: blur(120px); z-index: -1; pointer-events: none;
}
body::after {
  content: ''; position: fixed; bottom: -20%; right: -10%; width: 50vw; height: 50vw;
  background: radial-gradient(circle, rgba(255, 138, 61, 0.06) 0%, transparent 60%);
  filter: blur(120px); z-index: -1; pointer-events: none;
}
.ambient-cyan {
  position: fixed; top: 40%; left: 40%; width: 30vw; height: 30vw;
  background: radial-gradient(circle, rgba(98, 217, 255, 0.04) 0%, transparent 50%);
  filter: blur(100px); z-index: -1; pointer-events: none;
}

.app-container {
  max-width: 1600px; margin: 0 auto; padding: 2rem;
  display: flex; flex-direction: column; gap: 2rem;
}

/* Floating Header */
.glass-nav {
  display: flex; justify-content: space-between; align-items: center; padding: 1rem 2rem;
  background: var(--glass-bg); backdrop-filter: var(--glass-blur); border: 1px solid var(--border);
  border-radius: 100px; box-shadow: var(--glass-shadow);
}
.glass-nav .logo { font-size: 1.25rem; font-weight: 600; display: flex; align-items: center; gap: 0.5rem; }
.glass-nav .logo svg { color: var(--heat-accent); }
.glass-nav .menu { display: flex; gap: 2rem; }
.glass-nav .menu-item { font-size: 0.85rem; font-weight: 500; color: var(--text-secondary); cursor: pointer; padding: 0.4rem 1rem; border-radius: 100px; transition: 0.3s; }
.glass-nav .menu-item.active { color: var(--primary); background: rgba(77, 163, 255, 0.1); }
.glass-nav .meta { display: flex; align-items: center; gap: 1.5rem; font-size: 0.8rem; color: var(--text-secondary); }

/* ========================================= */
/* PHASE 3: COMPONENT STYLES                 */
/* ========================================= */
.glass-card {
  background: var(--glass-bg); backdrop-filter: var(--glass-blur); border: 1px solid var(--border);
  border-radius: 24px; padding: 1.5rem; box-shadow: var(--glass-shadow); transition: all 0.4s ease;
}
.glass-card:hover { transform: translateY(-2px); background: var(--glass-bg-hover); box-shadow: 0 12px 40px rgba(0,0,0,0.3); }

/* Sliders */
.weight-sliders-container { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem; }
.slider-group { flex: 1; margin-right: 1.5rem; }
.slider-group label { font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-secondary); display: flex; justify-content: space-between; margin-bottom: 0.5rem; }
.slider-group label span { color: var(--primary); font-weight: 600; }
input[type=range] { -webkit-appearance: none; width: 100%; height: 4px; background: rgba(255,255,255,0.1); border-radius: 2px; outline: none; }
input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; width: 16px; height: 16px; border-radius: 50%; background: var(--primary); cursor: pointer; transition: 0.3s; }
input[type=range]:active::-webkit-slider-thumb { transform: scale(1.3); box-shadow: 0 0 15px rgba(77, 163, 255, 0.8); }

.time-toggle { background: transparent; color: var(--text-primary); border: 1px solid var(--border); padding: 0.5rem 1.5rem; border-radius: 20px; font-size: 0.75rem; cursor: pointer; transition: 0.3s; }
.time-toggle:active { transform: scale(0.96); }

/* Hero */
.hero-area { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 1.5rem; }
.hero-main { display: flex; align-items: center; gap: 2rem; background: linear-gradient(145deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02)); }
.gauge-container { position: relative; width: 120px; height: 120px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.gauge-container::before { content: ''; position: absolute; width: 100px; height: 100px; background: var(--bg-base); border-radius: 50%; }
.gauge-value { position: relative; font-size: 2.5rem; font-weight: 300; color: var(--text-primary); }
.hero-info .title { font-size: 0.7rem; letter-spacing: 0.15em; color: var(--text-muted); text-transform: uppercase; margin-bottom: 0.5rem; }
.hero-info .name { font-size: 2rem; font-weight: 400; margin-bottom: 0.5rem; }

.kpi-card { display: flex; flex-direction: column; justify-content: center; }
.kpi-card.heat { box-shadow: 0 0 20px rgba(255, 138, 61, 0.1); border-color: rgba(255, 138, 61, 0.2); }
.kpi-label { font-size: 0.65rem; letter-spacing: 0.1em; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 0.5rem; }
.kpi-val { font-size: 2rem; font-weight: 300; color: var(--text-primary); }
.kpi-sub { font-size: 0.75rem; color: var(--text-muted); margin-top: 0.5rem; display: flex; align-items: center; gap: 4px;}

/* Dash Top */
.dashboard-top { display: grid; grid-template-columns: 1fr 400px; gap: 1.5rem; height: 600px; }
.map-container { border-radius: 24px; overflow: hidden; border: 1px solid var(--border); }
#map { width: 100%; height: 100%; background: #0B1830 !important; }
.sidebar { display: flex; flex-direction: column; gap: 1.5rem; overflow-y: auto; padding-right: 0.5rem; }
.sidebar::-webkit-scrollbar { width: 4px; }
.sidebar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }

/* Detail Card & Rankings */
.priority-tag { font-size: 0.7rem; padding: 0.25rem 0.75rem; border-radius: 12px; letter-spacing: 0.1em; font-weight: 600; display: inline-block;}
.priority-tag.critical { background: rgba(255, 90, 69, 0.15); color: var(--critical); }
.priority-tag.high { background: rgba(255, 138, 61, 0.15); color: var(--heat-accent); }
.priority-tag.moderate { background: rgba(98, 217, 255, 0.15); color: var(--secondary); }
.priority-tag.low { background: rgba(50, 213, 131, 0.15); color: var(--success); }

.ranking-item { background: rgba(0,0,0,0.2); border: 1px solid var(--border); border-radius: 16px; padding: 1rem; display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem; cursor: pointer; transition: 0.3s; }
.ranking-item:hover { background: var(--glass-bg-hover); transform: translateX(4px); }
.ranking-item.selected { background: rgba(77, 163, 255, 0.08); border-color: rgba(77, 163, 255, 0.3); }

/* Priority Grid */
.priority-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; }
.p-factor { background: rgba(0,0,0,0.2); border: 1px solid var(--border); border-radius: 12px; padding: 1rem; text-align: center; }
.p-factor .lbl { font-size: 0.65rem; color: var(--text-secondary); letter-spacing: 0.05em; text-transform: uppercase;}
.p-factor .val { font-size: 1.5rem; font-weight: 300; margin-top: 0.25rem; }

/* Sensor Strip */
.sensor-strip { display: flex; gap: 1rem; margin-top: 2rem; }
.sensor { flex: 1; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 12px; padding: 0.75rem; text-align: center; }
.sensor .s-val { font-size: 1.25rem; font-weight: 400; }
.sensor .s-lbl { font-size: 0.6rem; color: var(--text-muted); text-transform: uppercase; margin-top: 0.25rem; }
.sensor-status { font-size: 0.5rem; color: var(--success); letter-spacing: 0.1em; margin-bottom: 0.5rem; display: flex; align-items: center; justify-content: center; gap: 4px; }
.sensor-status::before { content: ''; width: 6px; height: 6px; background: var(--success); border-radius: 50%; box-shadow: 0 0 5px var(--success); }
.wb-lethal { color: var(--critical); text-shadow: 0 0 10px rgba(255,90,69,0.5); }
.wb-dangerous { color: var(--heat-accent); text-shadow: 0 0 10px rgba(255,138,61,0.5); }
.wb-caution { color: var(--secondary); }
.wb-safe { color: var(--success); }
.aqi-good { color: var(--success); }
.aqi-moderate { color: var(--secondary); }
.aqi-poor { color: var(--heat-accent); }
.aqi-unhealthy { color: var(--critical); }

/* Dash Bottom */
.dashboard-bottom { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.5rem; }
h3.section-title { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.15em; color: var(--text-secondary); margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem; }
.section-title svg { width: 14px; height: 14px; stroke: var(--primary); }

/* Surface */
.surface-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.75rem; }
.surface-row .lbl { width: 80px; font-size: 0.75rem; color: var(--text-secondary); }
.surface-row .track { flex: 1; height: 6px; background: rgba(0,0,0,0.3); border-radius: 3px; overflow: hidden; }
.surface-row .fill { height: 100%; border-radius: 3px; }
.surface-row .val { width: 40px; font-size: 0.75rem; font-weight: 500; text-align: right; }
.surface-insight { margin-top: 1.5rem; padding: 1rem; background: rgba(77, 163, 255, 0.05); border-left: 2px solid var(--primary); font-size: 0.85rem; color: var(--text-secondary); }
.surface-insight strong { color: var(--text-primary); display: block; margin-bottom: 0.25rem; }

/* Budget */
.budget-amount { font-size: 3rem; font-weight: 300; color: var(--success); margin: 1rem 0 2rem 0; }
.budget-row { display: flex; justify-content: space-between; align-items: center; padding: 1rem; border-bottom: 1px solid var(--border); font-size: 0.85rem; }
.budget-row:last-child { border-bottom: none; }
.budget-row.funded .status { color: var(--success); font-size: 0.7rem; letter-spacing: 0.1em; display: flex; align-items: center; gap: 0.5rem;}
.budget-row.unfunded .status { color: var(--text-muted); font-size: 0.7rem; letter-spacing: 0.1em;}

/* What-If */
.whatif-controls select { width: 100%; background: rgba(0,0,0,0.2); color: var(--text-primary); border: 1px solid var(--border); padding: 0.75rem; border-radius: 12px; margin-bottom: 1.5rem; outline: none; }
.whatif-result { margin-top: 2rem; display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.2); padding: 1.5rem; border-radius: 16px; border: 1px solid var(--border); }
.sim-block { text-align: center; }
.sim-block .lbl { font-size: 0.65rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.1em; }
.sim-block .val { font-size: 2rem; font-weight: 300; margin-top: 0.25rem; }
.sim-diff { color: var(--success); font-weight: 500; font-size: 0.85rem; margin-top: 0.5rem; }
.whatif-change.positive { color: var(--success); }
.whatif-change.negative { color: var(--critical); }

/* Impact */
.impact-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem; }
.impact-grid .val { font-size: 2.5rem; font-weight: 300; color: var(--text-primary); }
.impact-grid .lbl { font-size: 0.75rem; color: var(--text-secondary); margin-top: 0.5rem; }

/* Responsive */
@media (max-width: 1024px) {
  .dashboard-top { grid-template-columns: 1fr; height: auto; }
  .map-container { height: 400px; }
  .dashboard-bottom { grid-template-columns: 1fr; }
  .hero-area { grid-template-columns: 1fr 1fr; }
  .glass-nav .menu { display: none; }
  body::before, body::after { filter: blur(80px); }
  .sensor-strip, .priority-grid { backdrop-filter: none; }
}
@media (max-width: 768px) {
  .hero-area { grid-template-columns: 1fr; }
  .hero-main { flex-direction: column; text-align: center; }
  .priority-grid { grid-template-columns: 1fr; }
  .sensor-strip { flex-direction: column; }
  .impact-grid { grid-template-columns: 1fr; text-align: center; }
  .glass-card { backdrop-filter: blur(10px); }
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)


html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HeatShield</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script src="data.js"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>

  <div class="ambient-cyan"></div>
  
  <div class="app-container">
    <header class="glass-nav">
      <div class="logo"><i data-lucide="flame"></i> HeatShield</div>
      <div class="menu">
        <span class="menu-item active">Overview</span>
        <span class="menu-item">Heat Risk</span>
        <span class="menu-item">Priority Areas</span>
        <span class="menu-item">Scenarios</span>
        <span class="menu-item">Insights</span>
      </div>
      <div class="meta">
        <span><i data-lucide="map-pin" style="width:14px; margin-right:4px;"></i> Los Angeles, CA</span>
        <span id="current-date"></span>
        <button id="day-night-toggle" class="time-toggle"><i data-lucide="sun" style="width:14px;"></i> Day (2 PM)</button>
      </div>
    </header>

    <div class="glass-card weight-sliders-container">
      <div class="slider-group">
        <label>Heat Exposure <span id="weight-heat-val">50%</span></label>
        <input type="range" id="weight-heat" min="0" max="100" value="50">
      </div>
      <div class="slider-group">
        <label>Vulnerable Pop <span id="weight-pop-val">25%</span></label>
        <input type="range" id="weight-pop" min="0" max="100" value="25">
      </div>
      <div class="slider-group">
        <label>Low Trees <span id="weight-tree-val">15%</span></label>
        <input type="range" id="weight-tree" min="0" max="100" value="15">
      </div>
      <div class="slider-group">
        <label>Impervious <span id="weight-pave-val">10%</span></label>
        <input type="range" id="weight-pave" min="0" max="100" value="10">
      </div>
      <button id="reset-weights" class="time-toggle" style="margin-left: 2rem;">Reset Config</button>
    </div>

    <div class="hero-area" id="hero-area">
      <!-- Injected by JS -->
    </div>

    <div class="dashboard-top">
      <div class="map-container"><div id="map"></div></div>
      <aside class="sidebar">
        <div class="glass-card" id="detail-card"></div>
        <div class="glass-card" style="padding:1rem;">
          <h3 class="section-title" style="margin-bottom: 1rem;"><i data-lucide="list-ordered"></i> Priority Ranking</h3>
          <div id="ranking-list" style="max-height: 250px; overflow-y:auto;"></div>
        </div>
      </aside>
    </div>

    <div class="dashboard-bottom">
      <div class="glass-card" id="surface-section">
        <!-- Injected by JS -->
      </div>
      
      <div class="glass-card">
        <h3 class="section-title"><i data-lucide="circle-dollar-sign"></i> Cooling Investment</h3>
        <div style="margin-bottom:1.5rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-size:0.75rem; color:var(--text-secondary); text-transform:uppercase;">Total Allocation</span>
            <span id="budget-display" class="budget-amount" style="margin:0;">$500,000</span>
          </div>
          <input type="range" id="budget-slider" min="0" max="1000000" step="50000" value="500000" style="width:100%">
        </div>
        <div class="budget-list" id="budget-list"></div>
      </div>
      
      <div class="glass-card">
        <h3 class="section-title"><i data-lucide="trees"></i> Scenario Lab</h3>
        <div style="font-size:0.875rem; color:var(--text-secondary); margin-bottom:1.5rem;">Model the impact of urban cooling interventions.</div>
        
        <div class="whatif-controls">
          <div style="font-size:0.65rem; font-weight:500; margin-bottom:0.5rem; color:var(--text-secondary); text-transform:uppercase;">Neighborhood</div>
          <select id="whatif-area"></select>
          <div style="display:flex; justify-content:space-between; font-size:0.65rem; font-weight:500; margin-bottom:0.5rem; color:var(--text-secondary); text-transform:uppercase;">
            <span>Increase Tree Cover</span>
            <span id="whatif-tree-val" style="color:var(--primary);">+10%</span>
          </div>
          <input type="range" id="whatif-tree-slider" min="0" max="50" value="10">
        </div>
        <div id="whatif-result"></div>
      </div>
      
      <div style="display:flex; flex-direction:column; gap:1.5rem;">
        <div class="glass-card">
          <h3 class="section-title"><i data-lucide="lightbulb"></i> Key Insight</h3>
          <div id="discovery-text" style="font-size:1.1rem; font-weight:300; color:var(--text-primary); line-height:1.6; margin-bottom:1.5rem;"></div>
        </div>
        
        <div class="glass-card">
          <h3 class="section-title"><i data-lucide="trending-up"></i> Impact Summary</h3>
          <div class="impact-grid">
            <div><div id="comm-lives" class="val">780K</div><div class="lbl">Residents in critical zones</div></div>
            <div><div id="comm-savings" class="val" style="color:var(--success);">$3.2M</div><div class="lbl">Est. annual savings</div></div>
            <div><div id="comm-coverage" class="val" style="color:var(--secondary);">86%</div><div class="lbl">Impervious surface</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    const DEFAULT_WEIGHTS = { heat: 50, population: 25, tree_cover: 15, pavement: 10 };
    let currentWeights = { ...DEFAULT_WEIGHTS };
    let map = null;
    let polygons = [];
    let rankedAreas = [];
    let selectedAreaId = null;
    let isNightMode = false;

    document.getElementById('current-date').textContent = new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });

    AREAS.forEach((a, i) => {
        if (a.buildings_pct === undefined) {
            let b = Math.floor(Math.random() * 40 + 30);
            let r = Math.floor(Math.random() * 20 + 10);
            let v = a.tree_cover_pct + Math.floor(Math.random() * 5);
            let w = Math.floor(Math.random() * 5);
            let bs = Math.max(0, 100 - (b + r + v + w));
            a.buildings_pct = b; a.roads_pct = r; a.vegetation_pct = v; a.bare_soil_pct = bs; a.water_pct = w;
            a.impervious_pct = b + r; a.wet_bulb_c = (Math.random() * 10 + 25).toFixed(1);
            a.solar_ghi = Math.floor(Math.random() * 400 + 600);
        }
    });

    function getColorForScore(score) {
      if (score >= 80) return 'var(--critical)';
      if (score >= 60) return 'var(--heat-accent)';
      if (score >= 40) return 'var(--secondary)';
      return 'var(--success)';
    }

    function getPriorityTag(score) {
      if (score >= 80) return { label: 'CRITICAL', class: 'critical' };
      if (score >= 60) return { label: 'HIGH', class: 'high' };
      if (score >= 40) return { label: 'MODERATE', class: 'moderate' };
      return { label: 'LOW', class: 'low' };
    }

    function getWetBulbClass(wb) {
        if (wb >= 35) return 'wb-lethal';
        if (wb >= 30) return 'wb-dangerous';
        if (wb >= 25) return 'wb-caution';
        return 'wb-safe';
    }

    function getAqiClass(aqi) {
        if (aqi <= 50) return 'aqi-good';
        if (aqi <= 100) return 'aqi-moderate';
        if (aqi <= 150) return 'aqi-poor';
        return 'aqi-unhealthy';
    }

    function calculatePriorityScore(area, weights, simulatedTreeCover = null) {
      const maxPop = Math.max(...AREAS.map(a => a.population));
      let currentHeat = isNightMode ? (area.night_heat_score !== undefined ? area.night_heat_score : area.heat_score * 0.75) : area.heat_score;
      const heat_norm = currentHeat;
      const pop_norm = (area.population / maxPop) * 100;
      let actualTreeCover = simulatedTreeCover !== null ? simulatedTreeCover : area.tree_cover_pct;
      const tree_norm = 100 - actualTreeCover;
      const pave_norm = area.pavement_pct;

      if (simulatedTreeCover === null) {
        area.norm_scores = { heat: heat_norm, pop: pop_norm, tree: tree_norm, pave: pave_norm };
      }

      const totalWeight = weights.heat + weights.population + weights.tree_cover + weights.pavement;
      if (totalWeight === 0) return 0;

      const score = ((heat_norm * weights.heat) + (pop_norm * weights.population) + (tree_norm * weights.tree_cover) + (pave_norm * weights.pavement)) / totalWeight;
      return Math.round(score);
    }

    function rankAreas(areas, weights) {
      return areas.map((area, index) => ({ ...area, originalIndex: index, priority_score: calculatePriorityScore(area, weights) }))
                  .sort((a, b) => b.priority_score - a.priority_score);
    }

    function updateStats() {
      if (rankedAreas.length === 0) return;
      const top = rankedAreas[0];
      const tempFieldC = isNightMode ? 'night_temp_c' : 'avg_temp_c';
      let sumC = 0, count = 0;
      AREAS.forEach(a => { sumC += (a[tempFieldC] !== undefined ? a[tempFieldC] : (isNightMode ? a.avg_temp_c * 0.75 : a.avg_temp_c)); count++; });
      const avgC = (sumC / count).toFixed(1);
      const top5Pop = rankedAreas.slice(0, 5).reduce((sum, a) => sum + a.population, 0);

      document.getElementById('hero-area').innerHTML = `
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
          <div class="kpi-sub"><i data-lucide="thermometer" style="width:14px;color:var(--heat-accent)"></i> High thermal stress</div>
        </div>
        <div class="glass-card kpi-card">
          <div class="kpi-label">Residents Exposed</div>
          <div class="kpi-val">${(top5Pop/1000).toFixed(1)}K</div>
          <div class="kpi-sub"><i data-lucide="users" style="width:14px;color:var(--primary)"></i> Top 5 areas</div>
        </div>
        <div class="glass-card kpi-card">
          <div class="kpi-label">Areas Scanned</div>
          <div class="kpi-val">${AREAS.length}</div>
          <div class="kpi-sub"><i data-lucide="scan" style="width:14px;color:var(--success)"></i> Live telemetry</div>
        </div>
      `;
    }

    function renderDetailCard(area) {
      if (!area) return;
      const tag = getPriorityTag(area.priority_score);
      document.getElementById('detail-card').innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
          <div>
            <div class="priority-tag ${tag.class}">${tag.label} RISK</div>
            <h2 style="font-size:2rem; font-weight:300; margin-top:0.5rem;">${area.name}</h2>
          </div>
          <div style="font-size:3rem; font-weight:300; color:${getColorForScore(area.priority_score)}; line-height:1;">
            ${area.priority_score}<span style="font-size:1rem;color:var(--text-muted)">/100</span>
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
            <div class="s-val ${getAqiClass(area.aqi)}">${area.aqi || '--'}</div>
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

    function renderRankingList() {
      const list = document.getElementById('ranking-list');
      list.innerHTML = '';
      rankedAreas.forEach((area, i) => {
        const el = document.createElement('div');
        el.className = `ranking-item ${selectedAreaId === area.originalIndex ? 'selected' : ''}`;
        el.innerHTML = `
          <div style="font-size:1.25rem; font-weight:300; color:var(--text-secondary); width:20px;">${i + 1}</div>
          <div style="flex:1;">
            <div style="font-weight:500;">${area.name}</div>
            <div style="font-size:0.75rem; color:var(--text-muted);">Pop: ${(area.population/1000).toFixed(1)}k</div>
          </div>
          <div style="font-size:1.25rem; font-weight:600; color:${getColorForScore(area.priority_score)}">${area.priority_score}</div>
        `;
        el.onclick = () => selectArea(area.originalIndex);
        list.appendChild(el);
      });
    }

    function renderSurfaceAnalysis(area) {
      if (!area || area.buildings_pct === undefined) {
        document.getElementById('surface-section').innerHTML = '<h3 class="section-title"><i data-lucide="satellite"></i> Surface Analysis</h3><div style="color:var(--text-muted);">Data not available</div>';
        return;
      }
      const bars = [
        { label: 'Buildings', val: area.buildings_pct, color: 'var(--primary)' },
        { label: 'Roads', val: area.roads_pct, color: 'var(--secondary)' },
        { label: 'Vegetation', val: area.vegetation_pct, color: 'var(--success)' },
        { label: 'Bare Soil', val: area.bare_soil_pct, color: 'var(--heat-accent)' },
        { label: 'Water', val: area.water_pct, color: 'var(--primary)' }
      ];
      let barsHtml = '';
      bars.forEach(b => {
        barsHtml += `<div class="surface-row"><div class="lbl">${b.label}</div><div class="track"><div class="fill" style="width:${b.val}%; background:${b.color};"></div></div><div class="val">${b.val}%</div></div>`;
      });
      document.getElementById('surface-section').innerHTML = `
        <h3 class="section-title"><i data-lucide="satellite"></i> Surface Analysis</h3>
        <div style="font-size:0.875rem; color:var(--text-secondary); margin-bottom:1.5rem;">Land cover composition for ${area.name}</div>
        ${barsHtml}
        <div class="surface-insight">
          <strong>${area.impervious_pct}% IMPERVIOUS SURFACE</strong>
          Buildings and roads dominate the landscape, severely limiting natural cooling.
        </div>
      `;
    }

    function updateCommercialStats() {
      const criticalAreas = rankedAreas.filter(a => a.priority_score >= 60);
      document.getElementById('comm-lives').textContent = (criticalAreas.reduce((sum, a) => sum + a.population, 0) / 1000).toFixed(0) + 'K';
      document.getElementById('comm-savings').textContent = '$' + (criticalAreas.length * 400000 / 1000000).toFixed(1) + 'M';
      const top5Imp = rankedAreas.slice(0, 5).reduce((sum, a) => sum + (a.impervious_pct || 0), 0) / 5;
      document.getElementById('comm-coverage').textContent = top5Imp ? Math.round(top5Imp) + '%' : '--';
    }

    function updateDiscoveryInsight() {
      const top3 = rankedAreas.slice(0, 3);
      const avgCityTree = AREAS.reduce((sum, a) => sum + a.tree_cover_pct, 0) / AREAS.length;
      const top3Tree = top3.reduce((sum, a) => sum + a.tree_cover_pct, 0) / 3;
      const diffTree = Math.round(avgCityTree - top3Tree);
      document.getElementById('discovery-text').innerHTML = `Top priority areas have <strong style="color:var(--critical)">${diffTree}% less tree cover</strong> than the city average, exposing more than <strong style="color:var(--heat-accent)">${(top3.reduce((s,a)=>s+a.population, 0)).toLocaleString()} residents</strong> to elevated thermal stress.`;
    }

    function updateBudgetSimulator() {
      const budget = parseInt(document.getElementById('budget-slider').value);
      document.getElementById('budget-display').textContent = `$${budget.toLocaleString()}`;
      const list = document.getElementById('budget-list');
      list.innerHTML = '';
      let remaining = budget;
      rankedAreas.slice(0, 8).forEach(area => {
        const cost = Math.round(area.priority_score / 100 * 200000);
        const isFunded = remaining >= cost;
        if (isFunded) remaining -= cost;
        list.innerHTML += `
          <div class="budget-row ${isFunded ? 'funded' : 'unfunded'}">
            <div>${area.name}</div>
            <div class="status">${isFunded ? '<i data-lucide="check-circle" style="width:14px;"></i> FUNDED' : 'UNFUNDED'}</div>
          </div>`;
      });
      lucide.createIcons();
    }

    function initWhatIf() {
      const select = document.getElementById('whatif-area');
      AREAS.forEach((a, i) => { select.appendChild(new Option(a.name, i)); });
      const updateWhatIf = () => {
        const val = parseInt(document.getElementById('whatif-tree-slider').value);
        document.getElementById('whatif-tree-val').textContent = '+' + val + '%';
        const area = AREAS[parseInt(select.value)];
        const oScore = calculatePriorityScore(area, currentWeights);
        const nScore = calculatePriorityScore(area, currentWeights, Math.min(100, area.tree_cover_pct + val));
        document.getElementById('whatif-result').innerHTML = `
          <div class="sim-block"><div class="lbl">Before</div><div class="val">${oScore}</div></div>
          <i data-lucide="arrow-right" class="sim-arrow"></i>
          <div class="sim-block"><div class="lbl">After</div><div class="val">${nScore}</div><div class="sim-diff">-${oScore - nScore} POINTS</div></div>
        `;
        lucide.createIcons();
      };
      select.addEventListener('change', updateWhatIf);
      document.getElementById('whatif-tree-slider').addEventListener('input', updateWhatIf);
      updateWhatIf();
    }

    // Map Init
    function initMap() {
      map = L.map('map', { zoomControl: false, attributionControl: false }).setView(CITY.center, CITY.zoom);
      L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', { maxZoom: 19 }).addTo(map);
      updateMapPolygons();
    }

    function updateMapPolygons() {
      if (!map) return;
      polygons.forEach(p => map.removeLayer(p));
      polygons = [];
      rankedAreas.forEach(area => {
        const color = getColorForScore(area.priority_score);
        const isSelected = selectedAreaId === area.originalIndex;
        const poly = L.polygon(area.polygon, { color: isSelected ? '#fff' : color, weight: isSelected ? 3 : 1, fillColor: color, fillOpacity: isSelected ? 0.6 : 0.4 }).addTo(map);
        poly.bindPopup(`<h3>${area.name}</h3><p>Risk: <strong style="color:${color}">${area.priority_score}/100</strong></p>`);
        poly.on('click', () => selectArea(area.originalIndex));
        polygons.push(poly);
      });
    }

    function selectArea(index) {
      selectedAreaId = index;
      const area = rankedAreas.find(a => a.originalIndex === index);
      if (area && map) map.flyTo([area.lat, area.lng], 13, { duration: 0.5 });
      renderDetailCard(area);
      renderSurfaceAnalysis(area);
      renderRankingList();
      updateMapPolygons();
      lucide.createIcons();
    }

    function updateDashboard() {
      rankedAreas = rankAreas(AREAS, currentWeights);
      if (selectedAreaId === null && rankedAreas.length > 0) selectedAreaId = rankedAreas[0].originalIndex;
      updateStats();
      renderRankingList();
      const selectedArea = rankedAreas.find(a => a.originalIndex === selectedAreaId);
      renderDetailCard(selectedArea);
      renderSurfaceAnalysis(selectedArea);
      updateMapPolygons();
      updateDiscoveryInsight();
      updateBudgetSimulator();
      updateCommercialStats();
      lucide.createIcons();
    }

    // Listeners
    ['heat', 'pop', 'tree', 'pave'].forEach(metric => {
      document.getElementById(`weight-${metric}`).addEventListener('input', (e) => {
        document.getElementById(`weight-${metric}-val`).textContent = `${e.target.value}%`;
        currentWeights[{'heat':'heat','pop':'population','tree':'tree_cover','pave':'pavement'}[metric]] = parseInt(e.target.value);
        updateDashboard();
      });
    });
    document.getElementById('reset-weights').addEventListener('click', () => {
      currentWeights = { ...DEFAULT_WEIGHTS };
      ['heat', 'pop', 'tree', 'pave'].forEach(m => {
        const v = currentWeights[{'heat':'heat','pop':'population','tree':'tree_cover','pave':'pavement'}[m]];
        document.getElementById(`weight-${m}`).value = v;
        document.getElementById(`weight-${m}-val`).textContent = `${v}%`;
      });
      updateDashboard();
    });
    document.getElementById('budget-slider').addEventListener('input', updateBudgetSimulator);
    document.getElementById('day-night-toggle').addEventListener('click', (e) => {
      isNightMode = !isNightMode;
      e.target.innerHTML = isNightMode ? '<i data-lucide="moon" style="width:14px;"></i> Night (2 AM)' : '<i data-lucide="sun" style="width:14px;"></i> Day (2 PM)';
      updateDashboard();
    });

    initMap();
    initWhatIf();
    updateDashboard();

  </script>
</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Full replacement complete!")
