import re

css_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix body overflow
css = re.sub(r'body\s*\{[^}]*\}', '''body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-main);
  color: var(--text-primary);
  margin: 0;
  padding: 0;
  min-height: 100vh;
  overflow-x: hidden;
}''', css, count=1)

# Add new dashboard classes
new_classes = '''
/* New Dashboard Layout */
.dashboard-top {
  display: grid;
  grid-template-columns: 1fr 400px;
  height: 550px;
  background-color: var(--bg-main);
}
.dashboard-bottom {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  padding: 1.5rem;
  background-color: var(--bg-main);
  border-top: 1px solid var(--card-border);
}
.bottom-card {
  background: var(--bg-card);
  border-radius: 12px;
  height: 100%;
}
@media (max-width: 1024px) {
  .dashboard-top { grid-template-columns: 1fr; height: auto; }
  .dashboard-top .map-container { height: 400px; }
  .dashboard-bottom { grid-template-columns: 1fr; }
}
'''
css += new_classes

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
