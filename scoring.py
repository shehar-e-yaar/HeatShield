import pandas as pd
import os
from config import DEFAULT_WEIGHTS, PROCESSED_DATA_DIR

def normalize_to_100(series):
    """Normalize a pandas series to 0-100 scale."""
    min_val = series.min()
    max_val = series.max()
    if max_val == min_val:
        return pd.Series([50] * len(series), index=series.index)
    return ((series - min_val) / (max_val - min_val) * 100).round(1)

def calculate_scores(df, weights=None):
    """Calculate priority scores for all neighborhoods.
    
    Args:
        df: DataFrame with columns: avg_temp_c, population, tree_cover_pct, pavement_pct
        weights: dict with keys: heat, population, tree_cover, pavement (sum to 100)
    """
    if weights is None:
        weights = DEFAULT_WEIGHTS
    
    # Normalize weights to sum to 1
    total = sum(weights.values())
    w = {k: v / total for k, v in weights.items()}
    
    # Create score components (all 0-100, higher = more risk)
    if 'heat_index_c' in df.columns:
        df['heat_score'] = normalize_to_100(df['heat_index_c'])
    elif 'day_temp_c' in df.columns:
        df['heat_score'] = normalize_to_100(df['day_temp_c'])
    elif 'avg_temp_c' in df.columns:
        df['heat_score'] = normalize_to_100(df['avg_temp_c'])
    elif 'heat_score' not in df.columns:
        df['heat_score'] = 50  # fallback
    
    df['pop_score'] = normalize_to_100(df['population'])
    df['tree_score'] = normalize_to_100(100 - df['tree_cover_pct'])  # less trees = higher risk
    df['pavement_score'] = normalize_to_100(df['pavement_pct'])  # more pavement = higher risk
    
    # Weighted priority score
    df['priority_score'] = (
        df['heat_score'] * w['heat'] +
        df['pop_score'] * w['population'] +
        df['tree_score'] * w['tree_cover'] +
        df['pavement_score'] * w['pavement']
    ).round(1)
    
    # Rank
    df['rank'] = df['priority_score'].rank(ascending=False, method='min').astype(int)
    
    # Priority level
    df['priority_level'] = df['priority_score'].apply(lambda x: 
        'CRITICAL' if x >= 80 else
        'HIGH' if x >= 60 else
        'MODERATE' if x >= 40 else
        'LOW'
    )
    
    return df.sort_values('rank')

def generate_insights(df):
    """Generate discovery insights from the data."""
    insights = []
    
    # Top vs bottom comparison
    top5 = df.nsmallest(5, 'rank')
    bottom5 = df.nlargest(5, 'rank')  # lowest priority
    
    # Tree cover insight
    top_tree = top5['tree_cover_pct'].mean()
    avg_tree = df['tree_cover_pct'].mean()
    if avg_tree > 0:
        pct_less = round((1 - top_tree / avg_tree) * 100)
        insights.append(f'Top-priority areas have {pct_less}% less tree cover than the city average ({top_tree:.0f}% vs {avg_tree:.0f}%)')
    
    # Population insight
    top_pop = top5['population'].sum()
    total_pop = df['population'].sum()
    pct_pop = round(top_pop / total_pop * 100)
    insights.append(f'The 5 highest-risk areas contain {pct_pop}% of the total population ({top_pop:,} of {total_pop:,} residents)')
    
    # Pavement insight
    top_pave = top5['pavement_pct'].mean()
    avg_pave = df['pavement_pct'].mean()
    insights.append(f'High-risk neighborhoods average {top_pave:.0f}% pavement density vs {avg_pave:.0f}% citywide')
    
    return insights

if __name__ == '__main__':
    csv_path = os.path.join(PROCESSED_DATA_DIR, 'master_dataset.csv')
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df = calculate_scores(df)
        
        print('\n PRIORITY RANKING')
        print('=' * 60)
        for _, row in df.iterrows():
            print(f"  #{int(row['rank']):2d}  {row['neighborhood']:<20s}  Score: {row['priority_score']:5.1f}  [{row['priority_level']}]")
        
        print('\n KEY INSIGHTS')
        for insight in generate_insights(df):
            print(f'  • {insight}')
    else:
        print(f'No master dataset found at {csv_path}')
        print('Run: python fetch_census.py && python fetch_tree_cover.py && python build_master_dataset.py')
