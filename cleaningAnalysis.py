import pandas as pd
def clean_netflix_data(file_path):
    """"
    Performs data cleaning on the Netflix dataset.
    Args:
        file_path (str): The path to the Netflix CSV file.
    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    print(f"Loading data from: {file_path}")
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully. Initial shape:", df.shape)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None
    # --- 1. Data Integrity & Initial Inspection ---
    print("\n--- Initial Data Info ---")
    df.info()
    print("\n--- Missing Values Before Cleaning ---")
    print(df.isnull().sum())
    # --- 2. Missing Data Handling ---
    # Fill 'director' and 'country' with 'Not Given'
    df['director'] = df['director'].fillna('Not Given')
    df['country'] = df['country'].fillna('Not Given')
    # For 'date_added', we'll drop rows where it's missing, as it's hard to impute meaningfully.
    initial_rows = df.shape[0]
    df.dropna(subset=['date_added'], inplace=True)
    print(f"\nDropped {initial_rows - df.shape[0]} rows with missing 'date_added'.")
    # Fill 'rating' with the mode
    if 'rating' in df.columns:
        most_frequent_rating = df['rating'].mode()[0]
        df['rating'] = df['rating'].fillna(most_frequent_rating)
        print(f"Filled missing 'rating' with: {most_frequent_rating}")
    # For 'duration', if it's missing, it implies an issue, so we'll drop these rows.
    initial_rows_duration = df.shape[0]
    df.dropna(subset=['duration'], inplace=True)
    print(f"Dropped {initial_rows_duration - df.shape[0]} rows with missing 'duration'.")
    print("\n--- Missing Values After Handling ---")
    print(df.isnull().sum())
    # --- 3. Duplicate Removal ---
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    print(f"\nRemoved {initial_rows - df.shape[0]} duplicate rows.")
    # --- 4. Standardization ---
    # Convert 'date_added' to datetime objects
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    # Drop rows where date_added couldn't be parsed (if any)
    initial_rows_date_parse = df.shape[0]
    df.dropna(subset=['date_added'], inplace=True)
    print(f"Dropped {initial_rows_date_parse - df.shape[0]} rows with unparseable 'date_added'.")
    df['duration_minutes'] = df['duration'].apply(lambda x: int(x.split(' ')[0]) if 'min' in x else None)
    df['duration_seasons'] = df['duration'].apply(lambda x: int(x.split(' ')[0]) if 'Season' in x else None)
    # Convert 'release_year' to integer type if it's not already
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64') # Use Int64 for nullable integer
    df.dropna(subset=['release_year'], inplace=True) # Drop rows where release_year is not numeric
    # Standardize 'listed_in' (genres) by splitting and stripping whitespace
    df['listed_in'] = df['listed_in'].apply(lambda x: [g.strip() for g in x.split(',')])
    print("\n--- Data Info After Cleaning and Standardization ---")
    df.info()
    print("\n--- First 5 rows of Cleaned Data ---")
    print(df.head())
    print("\n--- Value Counts for 'type' ---")
    print(df['type'].value_counts())
    print("\n--- Value Counts for 'rating' ---")
    print(df['rating'].value_counts())
    # --- 5. Outlier Detection (Conceptual for this dataset) ---
    print(f"\nMin Release Year: {df['release_year'].min()}")
    print(f"Max Release Year: {df['release_year'].max()}")
    if df['duration_minutes'].notna().any():
        print(f"Max Movie Duration (minutes): {df['duration_minutes'].max()}")
    if df['duration_seasons'].notna().any():
        print(f"Max TV Show Duration (seasons): {df['duration_seasons'].max()}")
    print("\nData cleaning complete!")
    return df
# Specify the path to your uploaded Netflix CSV file
file_name = 'Data Cleaning third project/netflix1.csv' # Updated file path
cleaned_df = clean_netflix_data(file_name)

if cleaned_df is not None:
    print(f"\nCleaned DataFrame shape: {cleaned_df.shape}")
  