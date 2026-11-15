import os
from datetime import datetime

import pandas as pd


def generate_test_data(output_folder):

    # -------------------------
    # Create Source Dataset
    # -------------------------

    policy_types = ["Health", "Life", "Motor"]

    source_data = []

    for i in range(1001, 1051):

        source_data.append({
            "policy_id": i,
            "customer_name": f"Customer_{i}",
            "premium": 5000 + ((i % 10) * 500),
            "policy_type": policy_types[i % 3]
        })

    source_df = pd.DataFrame(source_data)

    # -------------------------
    # Create Target Dataset
    # -------------------------

    target_df = source_df.copy()

    # Missing Records
    target_df = target_df[
        ~target_df["policy_id"].isin(
            [1044, 1045]
        )
    ]

    # Updated Records
    target_df.loc[
        target_df["policy_id"] == 1041,
        "premium"
    ] = 4500

    target_df.loc[
        target_df["policy_id"] == 1042,
        "premium"
    ] = 6500

    target_df.loc[
        target_df["policy_id"] == 1043,
        "premium"
    ] = 8000

    # Additional Records
    additional_records = pd.DataFrame([
        {
            "policy_id": 2001,
            "customer_name": "John",
            "premium": 9000,
            "policy_type": "Health"
        },
        {
            "policy_id": 2002,
            "customer_name": "David",
            "premium": 8200,
            "policy_type": "Life"
        },
        {
            "policy_id": 2003,
            "customer_name": "Sam",
            "premium": 7800,
            "policy_type": "Motor"
        }
    ])

    target_df = pd.concat(
        [target_df, additional_records],
        ignore_index=True
    )

    # Duplicate Record
    duplicate_record = target_df[
        target_df["policy_id"] == 1046
    ]

    target_df = pd.concat(
        [target_df, duplicate_record],
        ignore_index=True
    )

    # -------------------------
    # Timestamp
    # -------------------------

    timestamp = datetime.now().strftime(
        "%d-%m-%Y-%H-%M"
    )

    source_file = os.path.join(
        output_folder,
        f"source_{timestamp}.xlsx"
    )

    target_file = os.path.join(
        output_folder,
        f"target_{timestamp}.xlsx"
    )

    # -------------------------
    # Save Files
    # -------------------------

    source_df.to_excel(
        source_file,
        index=False
    )

    target_df.to_excel(
        target_file,
        index=False
    )

    # -------------------------
    # Summary
    # -------------------------

    print("\nFiles Generated Successfully\n")

    print(f"Source File : {source_file}")
    print(f"Target File : {target_file}")

    print("\nExpected Results")
    print("----------------------")
    print("Source Records  : 50")
    print("Target Records  : 52")
    print("Matched         : 45")
    print("Mismatch        : 3")
    print("Missing         : 2")
    print("Additional      : 3")
    print("Duplicate       : 1")


# -------------------------
# Main
# -------------------------

output_path = input(
    "Enter Output Folder Path: "
).strip()

if not os.path.exists(output_path):
    print("Invalid Folder Path")
    exit()

generate_test_data(output_path)