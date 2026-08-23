"""HeatShield — Run the complete data pipeline.

Usage:
    python run_pipeline.py          # Run with sample data (no API key needed)
    python run_pipeline.py --live   # Run with live FortyGuard API data
"""
import sys
import os

def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    live_mode = '--live' in sys.argv
    
    print(' HeatShield — Data Pipeline')
    print('=' * 40)
    
    if live_mode:
        from config import API_KEY
        if not API_KEY:
            print(' No API key found! Set FORTYGUARD_API_KEY in .env file')
            print('   Copy .env.example to .env and add your key')
            sys.exit(1)
        
        print('\n Mode: LIVE (using FortyGuard API)\n')
        
        # Step 1: Fetch temperature data
        print('Step 1/4: Fetching temperature data...')
        from fetch_temperature import fetch_all_neighborhoods
        fetch_all_neighborhoods()
    else:
        print('\n Mode: SAMPLE DATA (no API key needed)\n')
    
    # Step 2: Fetch census data
    print('\nStep 2/4: Loading census data...')
    from fetch_census import fetch_census_data
    fetch_census_data()
    
    # Step 3: Fetch env params
    print('\nStep 3/5: Loading environmental parameters data...')
    from fetch_env_params import fetch_env_params_data
    fetch_env_params_data()
    
    # Step 4: Fetch tree cover data
    print('\nStep 4/6: Loading tree cover data...')
    from fetch_tree_cover import fetch_tree_cover_data
    fetch_tree_cover_data()
    
    # Step 5: Fetch satellite data
    print('\nStep 5/6: Loading satellite segmentation data...')
    from fetch_satellite import fetch_satellite_data
    fetch_satellite_data()
    
    # Step 6: Build master dataset
    print('\nStep 6/6: Building master dataset...')
    from build_master_dataset import build_master_dataset
    df = build_master_dataset(live_mode=live_mode)
    
    # Score and export
    print('\n Calculating priority scores...')
    from scoring import calculate_scores, generate_insights
    df = calculate_scores(df)
    
    print('\n PRIORITY RANKING')
    print('=' * 60)
    for _, row in df.iterrows():
        print(f"  #{int(row['rank']):2d}  {row['neighborhood']:<20s}  Score: {row['priority_score']:5.1f}  [{row['priority_level']}]")
    
    print('\n KEY INSIGHTS')
    for insight in generate_insights(df):
        print(f'  • {insight}')
    
    # Export to dashboard
    print('\n Exporting to dashboard...')
    from export_to_dashboard import export_to_js
    export_to_js(df)
    
    print('\n' + '=' * 40)
    print(' Pipeline complete!')
    print('   Open site/index.html in your browser to see the dashboard')
    if not live_mode:
        print('\n   To use real FortyGuard data, run: python run_pipeline.py --live')

if __name__ == '__main__':
    main()
