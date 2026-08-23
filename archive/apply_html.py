import re

html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Lucide to <head>
if "unpkg.com/lucide" not in html:
    html = html.replace('</head>', '  <script src="https://unpkg.com/lucide@latest"></script>\n</head>')

# Rewrite Header
new_header = """
  <header class="header">
    <h1><i data-lucide="flame" style="color:var(--accent-orange)"></i> HeatShield</h1>
    <div class="header-nav">
      <span class="active">Overview</span>
      <span>Heat Risk</span>
      <span>Priority Areas</span>
      <span>Scenarios</span>
      <span>Insights</span>
    </div>
    <div class="location">
      <i data-lucide="map-pin"></i> Los Angeles, CA 
      <span id="current-date" style="margin:0 1rem;"></span>
      <button id="day-night-toggle" class="time-toggle"><i data-lucide="sun"></i> Current Weather</button>
    </div>
  </header>
"""
html = re.sub(r'<header class="header">.*?</header>', new_header.strip(), html, flags=re.DOTALL)

# Replace section titles
html = html.replace('<h3>🛰️ Surface Analysis — Why Is It Hot?</h3>', '<h3 class="section-title"><i data-lucide="satellite"></i> Surface Analysis</h3>')
html = html.replace('<h3>💰 Cooling Budget Allocation</h3>', '<h3 class="section-title"><i data-lucide="circle-dollar-sign"></i> Cooling Investment</h3>')
html = html.replace('<h3>🌳 What-If: Tree Planting Impact</h3>', '<h3 class="section-title"><i data-lucide="trees"></i> Scenario Lab</h3>')
html = html.replace('<h3>💡 Key Insight</h3>', '<h3 class="section-title"><i data-lucide="lightbulb"></i> Key Insight</h3>')
html = html.replace('<h3>💼 Value Proposition</h3>', '<h3 class="section-title"><i data-lucide="trending-up"></i> Impact</h3>')

# Update class names for bottom cards
html = html.replace('<div class="bottom-card">', '<div class="glass-panel">')

# Modify JS rendering string replacements using Regex or standard replace
# 1. Detail Card HTML
html = html.replace(
    '<div class="detail-header">\n          <div>\n            <h2>${area.name}</h2>\n            <div class="priority-tag ${tag.class}">${tag.label} PRIORITY</div>\n          </div>\n          <div class="score-badge" style="color: ${getColorForScore(area.priority_score)}">${area.priority_score}</div>\n        </div>',
    '<div class="detail-header">\n          <div>\n            <div class="priority-tag ${tag.class}">${tag.label} RISK</div>\n            <h2 style="font-size:2rem; font-weight:300; margin-top:0.5rem;">${area.name}</h2>\n          </div>\n          <div style="text-align:right;">\n            <div style="font-size:3rem; font-weight:300; color:${getColorForScore(area.priority_score)}">${area.priority_score}<span style="font-size:1rem;color:var(--text-muted)">/100</span></div>\n          </div>\n        </div>'
)

# 2. Add lucide init at the end
if "lucide.createIcons();" not in html:
    html = html.replace('</script>', '\n    lucide.createIcons();\n  </script>')

# Update budget rendering JS (checkmarks instead of emojis)
html = html.replace('✓', '<i data-lucide="check" style="width:12px;height:12px;margin-right:4px;"></i>')
html = html.replace('❌', '<i data-lucide="x" style="width:12px;height:12px;margin-right:4px;"></i>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated successfully")
