#  HeatShield — Hyperlocal Heat Risk Intelligence

> *"We don't just show where it's hot. We show where to act first."*

##  Problem Statement
Urban heat islands are increasingly dangerous, but heat alone doesn't tell the whole story. Vulnerable populations in areas with sparse tree cover and high pavement density face disproportionate risks. City planners and emergency services need actionable intelligence to allocate resources effectively, prioritizing the most at-risk neighborhoods.

##  Solution Overview
HeatShield is a data-driven pipeline and dashboard that combines high-resolution environmental data (temperature, tree cover, pavement density) with sociodemographic data to identify and score hyperlocal heat vulnerabilities in Los Angeles. It generates actionable insights to direct interventions where they are needed most.

##  Architecture & Data Flow

```ascii
+-------------------+      +-------------------+      +-------------------+
| Open-Meteo API    |      | Static/Fallback   |      | FortyGuard API    |
| (Current Weather) |      | (Pop / Trees)     |      | (Map & Sat Layer) |
+---------+---------+      +---------+---------+      +---------+---------+
          |                          |                          |
          v                          v                          v
+-------------------------------------------------------------------------+
|                          Data Ingestion Pipeline                        |
|   (fetch_env_params.py, fetch_census.py, fetch_tree_cover.py)           |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                           Scoring Engine                                |
|                        (scoring.py)                                     |
|  * Applies Min-Max Normalization to bounded 0-100 scores                |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                        Dashboard Exporter                               |
|                     (export_to_dashboard.py)                            |
|  * Outputs site/data.js (Snapshot of computed scores)                   |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                       Interactive Web Dashboard                         |
|                          (site/index.html)                              |
|  * Renders Priority Areas and Key Insights                              |
|  * Scenario Lab: Bounded Empirical Simulation of Canopy expansion       |
+-------------------------------------------------------------------------+
```

##  Data Provenance
- **Heat Index:** FortyGuard heatmap result when `--live` succeeds for that neighborhood; Open-Meteo apparent temperature otherwise. (Note: FortyGuard data is fetched with a 1-day offset to account for provider-side processing lag for satellite aggregations).
- **AQI / Solar / Humidity:** Open-Meteo API snapshot (unchanged).
- **Population / Tree Cover / Pavement / Land Cover:** Configured LA fallback estimate (unchanged).
- **Scores:** Locally calculated using min-max normalization (unchanged).

*Note: FortyGuard's `env_params` endpoint was evaluated and is currently unavailable (returns 500 error on provider's side) as of this submission. The heatmap endpoint is utilized instead to power the live heat metric when run with `--live`.*

##  How to Run

### Setup
1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

###  Mode: Data Pipeline
Run the data pipeline to generate fresh `data.js` for the dashboard:
```bash
python run_pipeline.py
```
*(Optionally use `--live` if FortyGuard credentials are added to `.env` for heatmap imagery)*

###  Mode: Serve Dashboard
Start a local web server in the `site/` directory:
```bash
python -m http.server 8080 --directory site
```
Then open `http://localhost:8080` in your browser.

##  Project Structure
- `config.py`: Core configurations and constants for LA neighborhoods.
- `fetch_*.py`: Data ingestion scripts for weather, census, satellite, and tree cover.
- `build_master_dataset.py`: Joins raw data into a structured CSV dataset.
- `scoring.py`: Computes vulnerability scores and generates insights.
- `export_to_dashboard.py`: Exports scored data into JavaScript format for the frontend.
- `run_pipeline.py`: Main execution script.
- `site/`: Contains the frontend dashboard (`index.html`, `style.css`, `data.js`).

---
**Track:** Resilient Cities & Infrastructure
**Event:** Built for FortyGuard Hackathon 2026
**License:** MIT
