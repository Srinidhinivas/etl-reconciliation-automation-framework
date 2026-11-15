import pandas as pd


class ReconciliationEngine:

    def __init__(self, source_file, target_file):

        self.source_df = pd.read_excel(source_file)
        self.target_df = pd.read_excel(target_file)

        if self.source_df.empty:
            raise ValueError(
                "Source file contains no records."
            )

        if self.target_df.empty:
            raise ValueError(
                "Target file contains no records."
            )

    def compare(self):

        source_count = len(self.source_df)
        target_count = len(self.target_df)

        matched = []
        missing = []
        additional = []

        mismatch_details = []

        duplicates = self.target_df[
            self.target_df.duplicated(
                subset=["policy_id"],
                keep=False
            )
        ]

        source_ids = set(self.source_df["policy_id"])
        target_ids = set(self.target_df["policy_id"])

        compare_columns = [
            col
            for col in self.source_df.columns
            if col != "policy_id"
        ]

        for policy_id in source_ids:

            if policy_id not in target_ids:

                missing.append(policy_id)

            else:

                source_row = self.source_df[
                    self.source_df["policy_id"] == policy_id
                ].iloc[0]

                target_row = self.target_df[
                    self.target_df["policy_id"] == policy_id
                ].iloc[0]

                row_match = True

                for column in compare_columns:

                    source_value = source_row[column]
                    target_value = target_row[column]

                    if source_value != target_value:

                        row_match = False

                        mismatch_details.append({
                            "policy_id": policy_id,
                            "column_name": column,
                            "source_value": source_value,
                            "target_value": target_value
                        })

                if row_match:

                    matched.append(policy_id)

        for policy_id in target_ids:

            if policy_id not in source_ids:

                additional.append(policy_id)

        return {

            "source_count": source_count,

            "target_count": target_count,

            "matched": matched,

            "mismatch_details": mismatch_details,

            # "mismatched": mismatched

            "missing": missing,

            "additional": additional,

            "duplicates": duplicates
        }