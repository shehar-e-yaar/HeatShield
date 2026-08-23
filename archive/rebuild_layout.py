import re

html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace the whole <main class="dashboard">...</main> block
# Let's extract the pieces we need
map_match = re.search(r'<div class="map-container">.*?</div>', content, re.DOTALL)
if not map_match: print("Map not found"); exit(1)
map_html = map_match.group(0)

# The new HTML structure
new_main = """
  <main class="dashboard-top">
    """ + map_html + """
    <aside class="sidebar" style="height: 100%; overflow-y: auto;">
      <div class="detail-card" id="detail-card"></div>
      <div class="ranking-panel" id="ranking-list"></div>
    </aside>
  </main>

  <section class="dashboard-bottom">
    <div class="bottom-card">
      <div class="surface-section" id="surface-section">
        <h3>🛰️ Surface Analysis — Why Is It Hot?</h3>
        <div class="surface-subtitle" id="surface-area-name">Select an area</div>
        <div class="surface-bars" id="surface-bars"></div>
        <div class="surface-insight" id="surface-insight"></div>
      </div>
    </div>

    <div class="bottom-card">
      <div class="budget-section">
        <h3>💰 Cooling Budget Allocation</h3>
        <div class="budget-header">
          <input type="range" id="budget-slider" min="0" max="1000000" step="50000" value="500000" style="width: 100%;">
        </div>
        <div class="budget-amount" id="budget-display">$500,000</div>
        <div class="budget-list" id="budget-list"></div>
      </div>
    </div>

    <div class="bottom-card">
      <div class="whatif-section">
        <h3>🌳 What-If: Tree Planting Impact</h3>
        <div class="whatif-controls">
          <select id="whatif-area"></select>
          <label>Increase tree cover by: <span id="whatif-tree-val">10%</span></label>
          <input type="range" id="whatif-tree-slider" min="0" max="50" value="10">
        </div>
        <div class="whatif-result" id="whatif-result"></div>
      </div>
    </div>

    <div class="bottom-card">
      <div class="discovery-section" style="margin-bottom: 1rem;">
        <h3>💡 Key Insight</h3>
        <div class="discovery-text" id="discovery-text">Loading insights...</div>
      </div>
      <div class="commercial-section">
        <h3>💼 Value Proposition</h3>
        <div class="commercial-stats">
          <div class="commercial-stat"><div class="commercial-value" id="comm-lives">--</div><div class="commercial-label">Residents in Critical Zones</div></div>
          <div class="commercial-stat"><div class="commercial-value" id="comm-savings">--</div><div class="commercial-label">Est. Annual Savings</div></div>
          <div class="commercial-stat"><div class="commercial-value" id="comm-coverage">--</div><div class="commercial-label">Impervious Surface</div></div>
        </div>
        <div class="commercial-pitch">HeatShield transforms reactive emergency spending into proactive, data-driven cooling investments — saving lives and reducing costs.</div>
      </div>
    </div>
  </section>
"""

# Replace old <main>
content = re.sub(r'<main class="dashboard">.*?</main>', new_main.strip(), content, flags=re.DOTALL)

# Remove tabs JS if it exists
content = re.sub(r'function switchTab.*?}', '', content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
