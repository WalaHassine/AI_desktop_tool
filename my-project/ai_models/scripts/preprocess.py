import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    try:
        # Load the dataset
        data = pd.read_csv(file_path)

        # Ensure 'target' column exists
        if 'target' not in data.columns:
            raise ValueError("The dataset must contain a 'target' column.")

        # Handle missing values
        data.fillna(data.mean(numeric_only=True), inplace=True)

        # Feature scaling
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(data.drop('target', axis=1))

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            scaled_features, data['target'], test_size=0.2, random_state=42
        )

        return X_train, X_test, y_train, y_test

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None, None, None, None
    except pd.errors.EmptyDataError:
        print("Error: The provided file is empty.")
        return None, None, None, None
    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")
        return None, None, None, None

if __name__ == "__main__":
    # Example usage
    X_train, X_test, y_train, y_test = preprocess_data('path/to/your/data.csv')