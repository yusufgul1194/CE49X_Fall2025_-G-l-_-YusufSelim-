# CE 49X - Lab 2: Soil Test Data Analysis

# Student Name: _____Yusuf Selim GÜL___________  
# Student ID: _____2021403183___________  
# Date: ______16.10.2025__________

import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load the soil test dataset from a CSV file.
    
    Parameters:
        file_path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded DataFrame, or None if the file is not found.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from: {file_path}")
        expected_cols = {'sample_id', 'soil_ph', 'nitrogen', 'phosphorus', 'moisture'}
        if not expected_cols.issubset(set(df.columns)):
            missing = expected_cols.difference(set(df.columns))
            print(f"Warning: Missing expected columns: {missing}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found. Ensure the file exists at the specified path: {file_path}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def remove_outliers_std(df, column, n_std=3):
    """
    Remove rows where df[column] is more than n_std standard deviations from the mean.
    Returns the filtered DataFrame, (lower_bound, upper_bound), and rows_removed count.
    """
    if column not in df.columns:
        print(f"Column '{column}' not found; skipping outlier removal.")
        return df, (None, None), 0
    col_mean = df[column].mean()
    col_std = df[column].std()
    lower = col_mean - n_std * col_std
    upper = col_mean + n_std * col_std
    before = len(df)
    df_filtered = df[(df[column] >= lower) & (df[column] <= upper)]
    removed = before - len(df_filtered)
    return df_filtered, (lower, upper), removed


def clean_data(df, outlier_column='soil_ph', n_std=3):
    """
    Clean the dataset by handling missing values and removing outliers for a chosen column.

    - Missing values in ['soil_ph', 'nitrogen', 'phosphorus', 'moisture'] are filled with the column mean.
    - Outliers in `outlier_column` more than `n_std` standard deviations from the mean are removed.
    """
    df_cleaned = df.copy()
    
    # Fill missing values in each specified column with the rounded column mean
    for col in ['soil_ph', 'nitrogen', 'phosphorus', 'moisture']:
        if col in df_cleaned.columns:
            if df_cleaned[col].isnull().any():
                # Calculate the mean AND round it to the nearest whole number
                mean_val = round(df_cleaned[col].mean())
                df_cleaned[col] = df_cleaned[col].fillna(mean_val)
                print(f"Filled missing values in '{col}' with rounded mean value {mean_val:.2f}")
        else:
            print(f"Warning: Column '{col}' not found in data.")
    
    # Remove outliers for chosen column
    df_cleaned, (lower_bound, upper_bound), removed = remove_outliers_std(df_cleaned, outlier_column, n_std)
    if lower_bound is not None:
        print(f"After cleaning, '{outlier_column}' within [{lower_bound:.2f}, {upper_bound:.2f}] (removed {removed} rows).")
    
    print(df_cleaned.head())
    return df_cleaned

def compute_statistics(df, column):
    """
    Compute and print descriptive statistics for the specified column.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column for which to compute statistics.
    """
    if column not in df.columns:
        print(f"Column '{column}' not found in DataFrame.")
        return
    
    min_val = df[column].min()
    max_val = df[column].max()
    mean_val = df[column].mean()
    median_val = df[column].median()
    std_val = df[column].std()
    
    print(f"\nDescriptive statistics for '{column}':")
    print(f"  Minimum: {min_val}")
    print(f"  Maximum: {max_val}")
    print(f"  Mean: {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")
    print(f"  Standard Deviation: {std_val:.2f}")

def main():
    # Update the file path to point to your soil_test (1).csv file
    file_path = r'c:\Users\Erkun\Downloads\soil_test (2).csv'  # Update this path as needed
    
    # Load the dataset using the load_data function
    df = load_data(file_path)
    if df is None:
        return
    
        # Clean the dataset using the clean_data function
    df_clean = clean_data(df, outlier_column='soil_ph', n_std=3)

    # Verify no NaNs remain in numeric columns
    print("NaNs after cleaning:")
    for col in ['soil_ph', 'nitrogen', 'phosphorus', 'moisture']:
        print(col, df_clean[col].isna().sum())

    # Save cleaned data (new file or overwrite the original)
    output_path = r'c:\Users\Erkun\Downloads\soil_test.csv'
    df_clean.to_csv(output_path, index=False)
    print(f"Saved cleaned data to: {output_path}")
    
    # Compute and display statistics for the 'soil_ph' column
    compute_statistics(df_clean, 'soil_ph')
    compute_statistics(df_clean, 'nitrogen')
    compute_statistics(df_clean, 'phosphorus')
    compute_statistics(df_clean, 'moisture')
    # (Optional) Compute statistics for other columns
    # compute_statistics(df_clean, 'nitrogen')
    # compute_statistics(df_clean, 'phosphorus')
    # compute_statistics(df_clean, 'moisture')
    
if __name__ == '__main__':
    main()