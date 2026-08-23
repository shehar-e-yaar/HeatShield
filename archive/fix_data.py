import re

path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Each neighbourhood clearly leads on a DIFFERENT metric so sliders change the ranking:
# Pacoima    -> heat leader (heat_score=95)
# South LA   -> population leader (pop=120k) but moderate heat
# Downtown   -> tree/pavement leader (worst green space)
# Van Nuys   -> high heat + high pop combo
overrides = {
    'South LA':      {'population': 120000, 'tree_cover_pct': 14, 'pavement_pct': 75, 'heat_score': 55.0},
    'Pacoima':       {'population': 65000,  'tree_cover_pct': 9,  'pavement_pct': 82, 'heat_score': 95.0},
    'Downtown LA':   {'population': 70000,  'tree_cover_pct': 5,  'pavement_pct': 93, 'heat_score': 52.0},
    'Van Nuys':      {'population': 115000, 'tree_cover_pct': 15, 'pavement_pct': 72, 'heat_score': 80.0},
    'Boyle Heights': {'population': 95000,  'tree_cover_pct': 12, 'pavement_pct': 80, 'heat_score': 68.0},
    'Compton':       {'population': 80000,  'tree_cover_pct': 11, 'pavement_pct': 78, 'heat_score': 62.0},
    'Hollywood':     {'population': 60000,  'tree_cover_pct': 20, 'pavement_pct': 65, 'heat_score': 55.0},
    'Echo Park':     {'population': 45000,  'tree_cover_pct': 25, 'pavement_pct': 60, 'heat_score': 42.0},
    'Santa Monica':  {'population': 55000,  'tree_cover_pct': 35, 'pavement_pct': 50, 'heat_score': 28.0},
    'Encino':        {'population': 40000,  'tree_cover_pct': 38, 'pavement_pct': 48, 'heat_score': 38.0},
}

# Find each area JSON block and replace field values
area_blocks = list(re.finditer(r'\{[^{}]+\}', content, re.DOTALL))
new_content = content

for m in reversed(area_blocks):
    block = m.group(0)
    name_match = re.search(r'"name":\s*"([^"]+)"', block)
    if not name_match:
        continue
    name = name_match.group(1)
    if name not in overrides:
        continue
    new_block = block
    for field, val in overrides[name].items():
        new_block = re.sub(
            r'("' + field + r'":\s*)[\d.]+',
            lambda mo, v=val: mo.group(1) + str(v),
            new_block
        )
    new_content = new_content[:m.start()] + new_block + new_content[m.end():]

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done. Verify:")
import json
blocks = re.findall(r'\{[^{}]+\}', new_content, re.DOTALL)
for b in blocks:
    nm = re.search(r'"name":\s*"([^"]+)"', b)
    hs = re.search(r'"heat_score":\s*([\d.]+)', b)
    pop = re.search(r'"population":\s*([\d.]+)', b)
    if nm and hs and pop:
        print(f"  {nm.group(1):20s} heat={hs.group(1):5s}  pop={pop.group(1)}")
