import pandas as pd


def get_feature_status_from_csv():
    try:
        # Ask user for CSV file path
        csv_file = input("Enter the path to the CSV file: ").strip()

        # Read CSV file
        df = pd.read_csv(csv_file)

        # Check if required columns exist
        required_columns = {"Bit Number", "Feature Name", "Feature Enable/Disable"}
        if not required_columns.issubset(df.columns):
            print("Error: CSV file must contain 'Bit Number', 'Feature Name', and 'Feature Enable/Disable' columns.")
            return

        # Sorting by Bit Number to ensure correct order
        df = df.sort_values(by="Bit Number")

        # Initializing binary representation
        binary_representation = 0

        for _, row in df.iterrows():
            feature_status = row["Feature Enable/Disable"].strip().lower()

            if feature_status in {'y', 'yes'}:
                binary_representation |= (1 << (row["Bit Number"] - 1))  # Adjusting bit position
            elif feature_status in {'n', 'no'}:
                continue  # Feature is disabled, do nothing
            else:
                print(
                    f"Warning: Invalid input '{row['Feature Enable/Disable']}' for feature '{row['Feature Name']}'. Expected 'y', 'yes', 'n', or 'no'.")

        decimal_representation = binary_representation

        print(f"Binary Representation: {bin(binary_representation)[2:].zfill(len(df))}")
        print(f"Decimal Representation: {decimal_representation}")

    except Exception as e:
        print(f"Error: {e}")


# Run the function
get_feature_status_from_csv()