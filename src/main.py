import pandas as pd
import numpy as np

np.random.seed(42)

# A main dictionary, whose keys are the channels and its values consist of another dictionary with multiple key-value pairs for sources and dummy data
# (average, standard deviation)
channels_sources_info = {
    'Programmatic': {
        'sources': ['Amazon Ad Server', 'StackAdapt', 'Google Display & Video 360'],
        'imp': (40000, 8000), 'clicks': (500, 120), 'spend': (450, 100), 'conv': (18, 6), 'video': (8000, 2000)
    },
    'Paid Search': {
        'sources': ['Google Search Ads 360', 'Bing Ads (Microsoft Advertising)'],
        'imp': (18000, 4000), 'clicks': (1100, 250), 'spend': (1800, 400), 'conv': (65, 18), 'video': (0, 0)
    },
    'Paid Social': {
        'sources': ['LinkedIn Ads', 'Facebook'],
        'imp': (25000, 6000), 'clicks': (600, 150), 'spend': (700, 180), 'conv': (25, 8), 'video': (5000, 1500)
    },
    'Organic': {
        'sources': ['Organic Search', 'Direct Traffic'],
        'imp': (12000, 2500), 'clicks': (600, 120), 'spend': (0, 0), 'conv': (35, 10), 'video': (0, 0)
    }
}

campaigns = {
    'Business-focused zero tolerance arch': (pd.Timestamp('2023-01-01'), pd.Timestamp('2023-04-30')),
    'Persistent 24/7 attitude':             (pd.Timestamp('2023-01-01'), pd.Timestamp('2023-12-31')), # Always-on
    'Integrated dedicated contingency':     (pd.Timestamp('2023-03-01'), pd.Timestamp('2023-07-31')),
    'Profound intangible policy':           (pd.Timestamp('2023-05-01'), pd.Timestamp('2023-09-30')),
    'Centralized modular throughput':       (pd.Timestamp('2023-06-01'), pd.Timestamp('2023-10-31')),
    'Automated uniform software':           (pd.Timestamp('2023-08-01'), pd.Timestamp('2023-12-31')),
    'Cross-platform static hierarchy':      (pd.Timestamp('2023-10-01'), pd.Timestamp('2023-12-31')), # Q4
    'Networked value-added time-frame':     (pd.Timestamp('2023-11-01'), pd.Timestamp('2023-12-31')),
}

rows = []
for d in pd.date_range('2023-01-01', '2023-12-31', freq='D'):
    active_campaigns = [
        name for name, (start, end) in campaigns.items()
        if start <= d <= end
    ]

    for channel, info in channels_sources_info.items():
        # Organic Traffic is not paid
        current_campaigns = ['Organic (Not Set)'] if channel == 'Organic' else active_campaigns

        for source in info['sources']:
            for campaign in current_campaigns:
                impressions = max(100, int(np.random.normal(*info['imp'])))
                clicks = max(0, min(impressions, int(np.random.normal(*info['clicks']))))
                spend = round(max(0.0, np.random.normal(*info['spend'])), 2) if info['spend'][0] > 0 else 0.0
                conversions = max(0, min(clicks, int(np.random.normal(*info['conv']))))
                video_views = max(0, min(impressions, int(np.random.normal(*info['video'])))) if info['video'][0] > 0 else 0

                rows.append({
                    'Date': d,
                    'Channel': channel,
                    'Data Source': source,
                    'Campaign': campaign,
                    'Impressions': impressions,
                    'Clicks': clicks,
                    'Spend': spend,
                    'Conversions': conversions,
                    'Video Views': video_views
                })

df = pd.DataFrame(rows)
df.to_csv('marketing_data.csv', index=False, encoding='utf-8')
