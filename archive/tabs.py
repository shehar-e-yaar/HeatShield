import re

html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

tab_html = """
    <aside class="sidebar">
      <div class="sidebar-tabs">
        <button class="tab-btn active" onclick="switchTab('tab-rank')">Ranking & Info</button>
        <button class="tab-btn" onclick="switchTab('tab-analysis')">Analysis & Impact</button>
        <button class="tab-btn" onclick="switchTab('tab-action')">Simulators</button>
      </div>

      <div id="tab-rank" class="tab-content active">
        <div class="detail-card" id="detail-card"></div>
        <div class="ranking-panel" id="ranking-list"></div>
      </div>

      <div id="tab-analysis" class="tab-content">
        <div class="surface-section" id="surface-section">
          <h3>🛰️ Surface Analysis — Why Is It Hot?</h3>
          <div class="surface-subtitle" id="surface-area-name">Select an area</div>
          <div class="surface-bars" id="surface-bars"></div>
          <div class="surface-insight" id="surface-insight"></div>
        </div>
        <div class="discovery-section">
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

      <div id="tab-action" class="tab-content">
        <div class="budget-section">
          <h3>💰 Cooling Budget Allocation</h3>
          <div class="budget-header">
            <input type="range" id="budget-slider" min="0" max="1000000" step="50000" value="500000" style="width: 100%;">
          </div>
          <div class="budget-amount" id="budget-display">$500,000</div>
          <div class="budget-list" id="budget-list"></div>
        </div>
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
    </aside>
"""

pattern = re.compile(r'<aside class="sidebar">.*?</aside>', re.DOTALL)
new_content = pattern.sub(tab_html.strip(), content)

js_code = """
    function switchTab(tabId) {
      document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      event.currentTarget.classList.add('active');
    }
"""
if "function switchTab" not in new_content:
    new_content = new_content.replace('</script>', js_code + '\n  </script>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)
