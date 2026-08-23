import re

css_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\style.css'
html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'

# --- PHASE 1 & 2 CSS ---
new_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* PHASE 1: DESIGN TOKENS */
:root {
  --bg-base: #07111F;
  --bg-sec: #0B1830;
  --bg-tint: #102A4C;
  
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
  
  --gradient-blue: linear-gradient(135deg, #4DA3FF, #6C63FF);
  --gradient-heat: linear-gradient(135deg, #FFB15C, #FF6B35);
  --gradient-climate: linear-gradient(135deg, #42D6C5, #4DA3FF);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* PHASE 2: LAYOUT SHELL & BACKGROUND */
body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-base);
  color: var(--text-primary);
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
}

/* Deep Atmospheric Background Glows */
body::before {
  content: '';
  position: fixed;
  top: -20%; left: -10%;
  width: 60vw; height: 60vw;
  background: radial-gradient(circle, rgba(77, 163, 255, 0.08) 0%, transparent 60%);
  filter: blur(120px);
  z-index: -1;
  pointer-events: none;
}
body::after {
  content: '';
  position: fixed;
  bottom: -20%; right: -10%;
  width: 50vw; height: 50vw;
  background: radial-gradient(circle, rgba(255, 138, 61, 0.05) 0%, transparent 60%);
  filter: blur(120px);
  z-index: -1;
  pointer-events: none;
}

.ambient-cyan {
  position: fixed;
  top: 40%; left: 40%;
  width: 30vw; height: 30vw;
  background: radial-gradient(circle, rgba(98, 217, 255, 0.03) 0%, transparent 50%);
  filter: blur(100px);
  z-index: -1;
  pointer-events: none;
}

/* App Shell Container */
.app-container {
  max-width: 1600px;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Floating Glass Header */
.glass-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: var(--glass-bg);
  backdrop-filter: var(--glass-blur);
  -webkit-backdrop-filter: var(--glass-blur);
  border: 1px solid var(--border);
  border-radius: 100px; /* Pill shape */
  box-shadow: var(--glass-shadow);
}

.glass-nav .logo {
  font-size: 1.25rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.glass-nav .logo svg {
  color: var(--heat-accent);
}

.glass-nav .menu {
  display: flex;
  gap: 2rem;
}
.glass-nav .menu-item {
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0.4rem 1rem;
  border-radius: 100px;
}
.glass-nav .menu-item.active {
  color: var(--primary);
  background: rgba(77, 163, 255, 0.1);
}
.glass-nav .menu-item:hover:not(.active) {
  color: var(--text-primary);
}

.glass-nav .meta {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  font-size: 0.8rem;
  color: var(--text-secondary);
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    existing_css = f.read()

# We will PREPEND the new tokens and shell to the CSS so we don't break everything, 
# but we should remove the old :root and body rules.
existing_css = re.sub(r':root\s*\{[^}]*\}', '', existing_css)
existing_css = re.sub(r'body\s*\{[^}]*\}', '', existing_css)
existing_css = re.sub(r'body::before\s*\{[^}]*\}', '', existing_css)
existing_css = re.sub(r'body::after\s*\{[^}]*\}', '', existing_css)
existing_css = re.sub(r'\.header\s*\{[^}]*\}', '', existing_css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(new_css + "\n\n/* EXISTING COMPONENT CSS (To be restyled in Phase 3) */\n" + existing_css)


# --- PHASE 1 & 2 HTML ---
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_header = """
  <div class="ambient-cyan"></div>
  <div class="app-container">
    <header class="glass-nav">
      <div class="logo">
        <i data-lucide="flame"></i> HeatShield
      </div>
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
        <button id="day-night-toggle" class="time-toggle" style="background:transparent; border:1px solid var(--border); color:var(--text-primary); padding:0.3rem 0.8rem; border-radius:100px; cursor:pointer;"><i data-lucide="sun" style="width:14px;"></i> Day (2 PM)</button>
      </div>
    </header>
"""
# Replace <header> and wrap in app-container
html = re.sub(r'<header class="header">.*?</header>', new_header.strip(), html, flags=re.DOTALL)

# Add closing div for app-container right before script
html = html.replace('<script>', '  </div>\n  <script>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
