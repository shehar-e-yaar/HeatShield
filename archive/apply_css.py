import re

css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
  --bg-deep: #07111F;
  --bg-sec: #0B1830;
  --accent-blue: #4DA3FF;
  --accent-cyan: #62D9FF;
  --accent-orange: #FF8A3D;
  --accent-red: #FF5A45;
  --accent-green: #32D583;
  --text-main: #F5F8FC;
  --text-sec: #A9B8CC;
  --text-muted: #718198;
  --glass-bg: rgba(255, 255, 255, 0.04);
  --glass-border: rgba(255, 255, 255, 0.08);
  --glass-hover: rgba(255, 255, 255, 0.08);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-deep);
  color: var(--text-main);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
}

/* Ambient Lighting Background */
body::before {
  content: '';
  position: fixed;
  top: -20%; left: -10%;
  width: 50vw; height: 50vw;
  background: radial-gradient(circle, rgba(77, 163, 255, 0.15) 0%, transparent 70%);
  filter: blur(100px);
  z-index: -1;
}
body::after {
  content: '';
  position: fixed;
  top: 20%; right: -10%;
  width: 40vw; height: 40vw;
  background: radial-gradient(circle, rgba(255, 138, 61, 0.1) 0%, transparent 70%);
  filter: blur(100px);
  z-index: -1;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  margin: 1rem 2rem;
  background: var(--glass-bg);
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

.header h1 {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-main);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.header-nav {
  display: flex;
  gap: 2rem;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-sec);
}
.header-nav span.active {
  color: var(--accent-blue);
  background: rgba(77, 163, 255, 0.1);
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
}

.location {
  font-size: 0.85rem;
  color: var(--text-sec);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.time-toggle {
  background: rgba(255, 255, 255, 0.05);
  color: var(--text-main);
  border: 1px solid var(--glass-border);
  padding: 0.35rem 1rem;
  border-radius: 20px;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.3s ease;
}
.time-toggle:hover {
  background: var(--glass-hover);
}

/* Glass Panels */
.glass-panel {
  background: var(--glass-bg);
  backdrop-filter: blur(25px);
  -webkit-backdrop-filter: blur(25px);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  padding: 1.5rem;
  box-shadow: 0 8px 32px rgba(0,0,0,0.15);
  transition: all 0.3s ease;
}
.glass-panel:hover {
  background: var(--glass-hover);
  border-color: rgba(255,255,255,0.15);
}

/* Sliders Bar */
.weight-sliders-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 2rem 2rem 2rem;
  padding: 1rem 2rem;
  background: var(--glass-bg);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  border: 1px solid var(--glass-border);
}

.weight-sliders {
  display: flex;
  gap: 2rem;
  flex: 1;
}

.slider-group {
  flex: 1;
}

.slider-group label {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-sec);
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}
.slider-group label span {
  color: var(--accent-blue);
  font-weight: 600;
}

input[type=range] {
  -webkit-appearance: none;
  width: 100%;
  background: rgba(255,255,255,0.1);
  height: 4px;
  border-radius: 2px;
  outline: none;
}
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 16px; height: 16px;
  border-radius: 50%;
  background: var(--accent-blue);
  cursor: pointer;
  box-shadow: 0 0 10px rgba(77, 163, 255, 0.5);
  transition: transform 0.2s;
}
input[type=range]::-webkit-slider-thumb:hover {
  transform: scale(1.2);
}

.reset-btn {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--glass-border);
  padding: 0.5rem 1.5rem;
  border-radius: 12px;
  font-size: 0.75rem;
  cursor: pointer;
  margin-left: 2rem;
}

/* Top Stats (Hero) */
.stats-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin: 0 2rem 2rem 2rem;
}
.stat-card {
  background: var(--glass-bg);
  backdrop-filter: blur(20px);
  border: 1px solid var(--glass-border);
  border-radius: 20px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.stat-card h3 {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-sec);
  margin-bottom: 0.5rem;
}
.stat-card .value {
  font-size: 2.5rem;
  font-weight: 300;
  color: var(--text-main);
}
.stat-card .sub-value {
  font-size: 0.9rem;
  color: var(--accent-blue);
  font-weight: 500;
  margin-left: 0.5rem;
}

/* Dash Layout */
.dashboard-top {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 1.5rem;
  margin: 0 2rem 2rem 2rem;
  height: 600px;
}

.map-container {
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid var(--glass-border);
}
#map {
  width: 100%; height: 100%;
  background: #0B1830 !important;
}

.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  overflow-y: auto;
  padding-right: 0.5rem;
}
.sidebar::-webkit-scrollbar { width: 4px; }
.sidebar::-webkit-scrollbar-track { background: transparent; }
.sidebar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }

/* Ranking Item */
.ranking-item {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease;
}
.ranking-item:hover {
  background: var(--glass-hover);
  transform: translateX(4px);
}
.ranking-item.selected {
  background: rgba(77, 163, 255, 0.08);
  border-color: rgba(77, 163, 255, 0.3);
}
.rank-number {
  font-size: 1.25rem;
  font-weight: 300;
  color: var(--text-sec);
  width: 2rem;
}
.rank-name {
  font-weight: 500;
  font-size: 0.95rem;
}
.rank-temp {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-top: 0.25rem;
}
.score-badge {
  margin-left: auto;
  font-size: 1.25rem;
  font-weight: 600;
}

/* Dashboard Bottom */
.dashboard-bottom {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin: 0 2rem 2rem 2rem;
}
.bottom-card {
  background: var(--glass-bg);
  backdrop-filter: blur(25px);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  padding: 2rem;
}

h3.section-title {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--text-sec);
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.section-title svg {
  width: 14px; height: 14px;
  stroke: var(--accent-blue);
}

/* Detail Card / Priority Area */
.detail-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}
.detail-header h2 {
  font-size: 1.5rem;
  font-weight: 400;
  margin-bottom: 0.25rem;
}
.priority-tag {
  font-size: 0.7rem;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  letter-spacing: 0.1em;
  font-weight: 600;
}
.priority-tag.critical { background: rgba(255, 90, 69, 0.15); color: var(--accent-red); }
.priority-tag.high { background: rgba(255, 138, 61, 0.15); color: var(--accent-orange); }
.priority-tag.moderate { background: rgba(98, 217, 255, 0.15); color: var(--accent-cyan); }
.priority-tag.low { background: rgba(50, 213, 131, 0.15); color: var(--accent-green); }

/* Progress Groups */
.progress-group { margin-bottom: 1rem; }
.progress-group label {
  display: flex;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--text-sec);
  margin-bottom: 0.4rem;
}
.progress-bar-bg {
  width: 100%; height: 4px;
  background: rgba(255,255,255,0.05);
  border-radius: 2px;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-cyan));
  border-radius: 2px;
}

/* Sensor Strip (Env Params) */
.env-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0.75rem;
  margin-top: 1.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--glass-border);
}
.env-item {
  background: rgba(0,0,0,0.2);
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  padding: 0.75rem;
  text-align: center;
}
.env-label {
  font-size: 0.6rem;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 0.25rem;
  letter-spacing: 0.05em;
}
.env-value {
  font-size: 1rem;
  font-weight: 500;
}
.wb-lethal { color: var(--accent-red); text-shadow: 0 0 10px rgba(255,90,69,0.5); }
.wb-dangerous { color: var(--accent-orange); text-shadow: 0 0 10px rgba(255,138,61,0.5); }
.wb-caution { color: var(--accent-cyan); }
.wb-safe { color: var(--accent-green); }

/* Surface Analysis */
.surface-bar-row {
  display: flex;
  align-items: center;
  margin-bottom: 0.75rem;
  gap: 1rem;
}
.surface-bar-label {
  width: 80px;
  font-size: 0.75rem;
  color: var(--text-sec);
  text-align: right;
}
.surface-bar-track {
  flex: 1;
  height: 8px;
  background: rgba(255,255,255,0.05);
  border-radius: 4px;
  overflow: hidden;
}
.surface-bar-fill {
  height: 100%;
  border-radius: 4px;
}
.surface-bar-value {
  width: 40px;
  font-size: 0.75rem;
  font-weight: 600;
}
.surface-insight {
  margin-top: 2rem;
  padding: 1rem;
  background: rgba(77, 163, 255, 0.05);
  border-left: 2px solid var(--accent-blue);
  font-size: 0.85rem;
  line-height: 1.5;
  color: var(--text-sec);
  border-radius: 0 8px 8px 0;
}

/* Budget Allocation */
.budget-amount {
  font-size: 3rem;
  font-weight: 300;
  color: var(--accent-green);
  margin: 1rem 0 2rem 0;
}
.budget-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.budget-item {
  display: flex;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  background: rgba(255,255,255,0.02);
  border: 1px solid var(--glass-border);
  border-radius: 12px;
  font-size: 0.85rem;
}
.budget-item.funded {
  border-color: rgba(50, 213, 131, 0.3);
}
.budget-item.funded .status {
  color: var(--accent-green);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
}
.budget-item.unfunded {
  opacity: 0.6;
}

/* What If */
.whatif-controls select {
  width: 100%;
  background: rgba(0,0,0,0.2);
  color: var(--text-main);
  border: 1px solid var(--glass-border);
  padding: 0.75rem;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  outline: none;
}
.whatif-result {
  margin-top: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255,255,255,0.02);
  padding: 1.5rem;
  border-radius: 16px;
  border: 1px solid var(--glass-border);
}
.whatif-state {
  text-align: center;
}
.whatif-state .label {
  font-size: 0.65rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
}
.whatif-state .val {
  font-size: 2rem;
  font-weight: 300;
}
.whatif-arrow {
  color: var(--text-muted);
}

/* Commercial Impact */
.commercial-stats {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}
.commercial-stat {
  text-align: center;
}
.commercial-value {
  font-size: 2.5rem;
  font-weight: 300;
  color: var(--accent-cyan);
}
.commercial-label {
  font-size: 0.75rem;
  color: var(--text-sec);
  margin-top: 0.5rem;
}
.commercial-pitch {
  margin-top: 3rem;
  font-size: 1.1rem;
  font-weight: 300;
  line-height: 1.6;
  color: var(--text-sec);
  text-align: center;
  max-width: 80%;
  margin-left: auto; margin-right: auto;
}

footer {
  text-align: center;
  padding: 2rem;
  color: var(--text-muted);
  font-size: 0.75rem;
}

.lucide {
  vertical-align: middle;
}
"""

with open(r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS updated successfully")
