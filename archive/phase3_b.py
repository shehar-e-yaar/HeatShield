import re

html_path = r'C:\Users\SHEHARYAR HAMD\Desktop\Hackathon\site\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 4. Re-write updateSurfaceAnalysis()
new_surface = """
    function updateSurfaceAnalysis(area) {
      if (!area || area.buildings_pct === undefined) {
        document.getElementById('surface-area-name').textContent = 'Satellite data not available';
        document.getElementById('surface-bars').innerHTML = '';
        document.getElementById('surface-insight').innerHTML = '';
        return;
      }
      
      document.getElementById('surface-area-name').textContent = `Land cover composition for ${area.name}`;
      
      const bars = [
        { label: 'Buildings', val: area.buildings_pct, color: 'var(--primary)' },
        { label: 'Roads', val: area.roads_pct, color: 'var(--secondary)' },
        { label: 'Vegetation', val: area.vegetation_pct, color: 'var(--success)' },
        { label: 'Bare Soil', val: area.bare_soil_pct, color: 'var(--heat-accent)' },
        { label: 'Water', val: area.water_pct, color: 'var(--primary)' }
      ];
      
      let html = '';
      bars.forEach(b => {
        html += `
          <div class="surface-row">
            <div class="lbl">${b.label}</div>
            <div class="track"><div class="fill" style="width:${b.val}%; background:${b.color};"></div></div>
            <div class="val">${b.val}%</div>
          </div>
        `;
      });
      document.getElementById('surface-bars').innerHTML = html;
      
      document.getElementById('surface-insight').innerHTML = `
        <strong>${area.impervious_pct}% IMPERVIOUS SURFACE</strong>
        Buildings and roads dominate the landscape, severely limiting natural cooling.
      `;
    }
"""
html = re.sub(r'function updateSurfaceAnalysis\(area\) \{.*?(?=function updateBudget)', new_surface.strip() + '\n\n    ', html, flags=re.DOTALL)

# 5. Re-write updateBudget()
new_budget = """
    function updateBudget() {
      const budgetVal = parseInt(document.getElementById('budget-slider').value);
      document.getElementById('budget-display').textContent = '$' + (budgetVal / 1000).toFixed(0) + 'K';

      let remaining = budgetVal;
      let listHTML = '';

      rankedAreas.forEach(area => {
        const cost = 100000 + (area.population * 0.5);
        if (remaining >= cost) {
          remaining -= cost;
          listHTML += `
            <div class="budget-row funded">
              <div>${area.name}</div>
              <div class="status"><i data-lucide="check-circle" style="width:14px;color:var(--success)"></i> FUNDED ($${(cost/1000).toFixed(0)}K)</div>
            </div>`;
        } else {
          listHTML += `
            <div class="budget-row unfunded">
              <div>${area.name}</div>
              <div class="status">UNFUNDED</div>
            </div>`;
        }
      });
      document.getElementById('budget-list').innerHTML = listHTML;
      lucide.createIcons();
    }
"""
html = re.sub(r'function updateBudget\(\) \{.*?(?=function updateWhatIf)', new_budget.strip() + '\n\n    ', html, flags=re.DOTALL)

# 6. Re-write updateWhatIf()
new_whatif = """
    function updateWhatIf() {
      const selectedIndex = document.getElementById('whatif-area').value;
      const increasePct = parseInt(document.getElementById('whatif-tree-slider').value);
      document.getElementById('whatif-tree-val').textContent = increasePct + '%';

      if (selectedIndex === '') return;
      const area = AREAS[selectedIndex];
      
      const beforeScore = calculatePriorityScore(area, currentWeights);
      const simulatedTreeCover = Math.min(100, area.tree_cover_pct + increasePct);
      const afterScore = calculatePriorityScore(area, currentWeights, simulatedTreeCover);
      
      const diff = beforeScore - afterScore;

      document.getElementById('whatif-result').innerHTML = `
        <div class="sim-block">
          <div class="lbl">Before</div>
          <div class="val">${beforeScore}</div>
        </div>
        <i data-lucide="arrow-right" class="sim-arrow"></i>
        <div class="sim-block">
          <div class="lbl">After</div>
          <div class="val">${afterScore}</div>
          <div class="sim-diff">-${diff} POINTS</div>
        </div>
      `;
      lucide.createIcons();
    }
"""
html = re.sub(r'function updateWhatIf\(\) \{.*?(?=function updateDiscoveryInsight)', new_whatif.strip() + '\n\n    ', html, flags=re.DOTALL)


# 7. Redesign Discovery and Commercial sections statically
discovery_static = """
      <div class="glass-card" style="margin-bottom: 1.5rem;">
        <h3 class="section-title"><i data-lucide="lightbulb"></i> Key Insight</h3>
        <div class="discovery-text" id="discovery-text" style="font-size:1.1rem; font-weight:300; line-height:1.6;">
          Top priority areas have 6% less tree cover than the city average, exposing more than 335,000 residents to elevated thermal stress.
        </div>
      </div>
      <div class="glass-card">
        <h3 class="section-title"><i data-lucide="trending-up"></i> Impact Summary</h3>
        <div class="impact-grid">
          <div><div class="val" style="color:var(--accent-red)">780K</div><div class="lbl">Residents at Risk</div></div>
          <div><div class="val" style="color:var(--success)">$3.2M</div><div class="lbl">Est. Savings</div></div>
          <div><div class="val" style="color:var(--primary)">86%</div><div class="lbl">Impervious Surface</div></div>
        </div>
      </div>
"""
# Replace the bottom two sections inside .bottom-card
html = re.sub(r'<div class="discovery-section".*</div>\s*</div>\s*</section>', discovery_static.strip() + '\n    </div>\n  </section>', html, flags=re.DOTALL)


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
