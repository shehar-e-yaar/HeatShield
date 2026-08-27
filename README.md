# 🛡️ HeatShield — Hyperlocal Heat Risk Intelligence

> *"We don't just show where it's hot. We show where to act first."*

## 🚨 Problem Statement
Every summer, Los Angeles burns. But not every neighborhood burns equally. The poorest areas—the ones with the fewest trees, the most concrete, and the highest population density—suffer the most. Extreme heat is not just a weather problem, it is an infrastructure and equity problem. City planners have temperature maps, but they lack a tool that combines hyper-local heat data with demographic vulnerability to tell them exactly *where* to spend their limited budgets first.

## 💡 Solution Overview
HeatShield is a real-time heat risk intelligence platform. We process live environmental data and combine it with census and satellite data to generate a **Priority Risk Score (0-100)** for every neighborhood. It generates actionable insights to direct interventions (like tree planting and cooling centers) where they are needed most.

## 📊 Key Features
1. **Vulnerability Scoring Engine:** Calculates a 0-100 risk score based on Heat Risk (40%), Demographic Vulnerability (35%), Tree Deficit (15%), and Pavement Density (10%).
2. **Scenario Lab:** An interactive tool allowing planners to simulate the impact of adding tree canopy to a specific neighborhood and watching the risk score dynamically recalculate based on empirical cooling math.
3. **Cooling Investment Budgeter:** Input a real dollar budget, and the system dynamically allocates the funds to the most vulnerable neighborhoods using the LA Bureau of Street Services standard cost model ($1,000 per tree).

## 🗄️ Architecture & Data Flow

```text
[FortyGuard API] --> (Live Surface Temp & Heat Index)
[Open-Meteo API] --> (AQI, Solar, Humidity)           } --> Python Pandas Pipeline --> data.js --> Vanilla JS UI
[Census Data]    --> (Population, Income, Age)
[Satellite Data] --> (Tree Canopy, Pavement %)
```

## 🔌 FortyGuard API Integration & Fallbacks
As requested by the hackathon guidelines, here is a trace of the exact FortyGuard API calls made by our pipeline (in `fetch_temperature.py` and `build_master_dataset.py`) when run with `--live`. 

Because the FortyGuard `/v1/env_params` endpoint was returning HTTP 500 Internal Server Errors during the hackathon (due to a Request/Response schema mismatch requiring input temperatures), we engineered a robust fallback. Our pipeline queries the **Heatmap** endpoint (`/v1/heatmap`), polls for the result, and extracts the mean surface temperature for the specific neighborhood polygon to drive our core engine.

**1. Request (Heatmap):**
```http
POST https://api.fortyguard.com/v1/heatmap
api-key: [HIDDEN]
Content-Type: application/json

{
    "area_type": "point",
    "lat": 33.975,
    "lng": -118.280,
    "date": "2024-10-23",
    "hour": 14
}
```

**2. Response (Status Poll):**
```json
{
    "status": "COMPLETED",
    "data": {
        "result": {
            "temperature_c": 38.2
        }
    }
}
```

### Limitations & Future Work
* **Limitations:** Due to the `env_params` 500 server error on the provider side, we had to rely on Open-Meteo to fill in the supplementary AQI, Humidity, and Solar Irradiance metrics. 
* **Future Work:** Once the FortyGuard `env_params` endpoint is patched by the developer team, we plan to swap out Open-Meteo entirely and feed FortyGuard's hyperlocal AQI and Solar data directly into our Vulnerability Index to provide even more precise neighborhood-level triage.

## 🚀 How to Run

### Setup
1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 1. Mode: Data Pipeline
Run the data pipeline to generate fresh `data.js` for the dashboard:
```bash
python run_pipeline.py
```
*(Use `python run_pipeline.py --live` if FortyGuard credentials are added to `.env`)*

### 2. Mode: Serve Dashboard
Start a local web server in the `site/` directory:
```bash
python -m http.server 8080 --directory site
```
Then open `http://localhost:8080` in your browser.

---
**Track:** Resilient Cities & Infrastructure  
**Event:** Built for FortyGuard Hackathon 2026  
**License:** MIT  
