import pandas as pd

# Load each country's dataset
us_df = pd.read_csv(r'C:\Users\Sayan Saha\OneDrive\Documents\my doc\intern\project work\dataset\USvideos.csv')
in_df = pd.read_csv(r'C:\Users\Sayan Saha\OneDrive\Documents\my doc\intern\project work\dataset\INvideos.csv')
uk_df = pd.read_csv(r'C:\Users\Sayan Saha\OneDrive\Documents\my doc\intern\project work\dataset\GBvideos.csv')  # UK dataset is labeled as GB on Kaggle

# Add 'country' column to each
us_df['country'] = 'US'
in_df['country'] = 'IN'
uk_df['country'] = 'UK'

# Combine all dataframes into one
combined_df = pd.concat([us_df, in_df, uk_df], ignore_index=True)

# Check basic info
print(combined_df.info())
print(combined_df['country'].value_counts())

# Save the combined dataset (optional)
combined_df.to_csv('merged_trending_videos.csv', index=False)
print("Merged dataset saved as 'merged_trending_videos.csv'!")
