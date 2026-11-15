import os

from datetime import datetime

import pandas as pd


class ReportGenerator:

    def generate_report(
        self,
        results,
        output_folder
    ):

        timestamp = datetime.now().strftime(
            "%d-%m-%Y-%H-%M"
        )

        report_file = os.path.join(
            output_folder,
            f"reconciliation_report_{timestamp}.xlsx"
        )

        summary_df = pd.DataFrame({

            "Metric": [
                "Source Records",
                "Target Records",
                "Matched",
                "Mismatched",
                "Missing",
                "Additional",
                "Duplicates"
            ],

            "Count": [
                results["source_count"],
                results["target_count"],
                len(results["matched"]),
                len(
                        set(
                            row["policy_id"]
                            for row in results["mismatch_details"]
                        )
                    ),
                # len(results["mismatched"]),
                len(results["missing"]),
                len(results["additional"]),
                len(results["duplicates"])
            ]
        })

        matched_df = pd.DataFrame(
            {"policy_id": results["matched"]}
        )

        mismatch_df = pd.DataFrame(
        #     {"policy_id": results["mismatched"]}
              results["mismatch_details"]

        )

        missing_df = pd.DataFrame(
            {"policy_id": results["missing"]}
        )

        additional_df = pd.DataFrame(
            {"policy_id": results["additional"]}
        )

        duplicate_df = results["duplicates"]

        with pd.ExcelWriter(
            report_file,
            engine="openpyxl"
        ) as writer:

            summary_df.to_excel(
                writer,
                sheet_name="Summary",
                index=False
            )

            matched_df.to_excel(
                writer,
                sheet_name="Matched",
                index=False
            )

            mismatch_df.to_excel(
                writer,
                sheet_name="Mismatch",
                index=False
            )

            missing_df.to_excel(
                writer,
                sheet_name="Missing",
                index=False
            )

            additional_df.to_excel(
                writer,
                sheet_name="Additional",
                index=False
            )

            duplicate_df.to_excel(
                writer,
                sheet_name="Duplicates",
                index=False
            )

        return report_file