import os
from reconciliation.logger import ( FrameworkLogger )
from reconciliation.compare_engine import ( ReconciliationEngine )
from reconciliation.report_generator import (  ReportGenerator )


def get_file_path(message):

    while True:

        file_path = input(message).strip()

        file_path = file_path.replace(
            '"',
            ''
        )

        if os.path.isfile(file_path):

            return file_path

        print(
            "\nInvalid File Path. Try Again.\n"
        )


def get_folder_path(message):

    while True:

        folder_path = input(message).strip()

        folder_path = folder_path.replace(
            '"',
            ''
        )

        if os.path.isdir(folder_path):

            return folder_path

        print(
            "\nInvalid Folder Path. Try Again.\n"
        )


def main():

    logger = FrameworkLogger.setup_logger()

    logger.info(
        "Framework Started"
    )

    print("\n" + "=" * 50)

    print(
        " ETL RECONCILIATION FRAMEWORK "
    )

    print("=" * 50)

    source_file = get_file_path(

        "\nEnter Source File Path : "
    )

    logger.info(
        f"Source File Selected : {source_file}"
    )

    target_file = get_file_path(

        "\nEnter Target File Path : "
    )

    logger.info(
        f"Target File Selected : {target_file}"
    )

    output_folder = get_folder_path(

        "\nEnter Output Folder Path : "
    )

    logger.info(
        f"Output Folder Selected : {output_folder}"
    )

    engine = ReconciliationEngine(

        source_file,

        target_file
    )

    logger.info(
        "Comparison Started"
    )

    results = engine.compare()

    logger.info(
        "Comparison Completed"
    )

    report_generator = ReportGenerator()

    report_path = (

        report_generator.generate_report(

            results,

            output_folder
        )
    )

  
    print("\n" + "=" * 50)

    print(" RECONCILIATION SUMMARY ")

    print("=" * 50)

    print(
        f"Source Records : "
        f"{results['source_count']}"
    )

    print(
        f"Target Records : "
        f"{results['target_count']}"
    )

    print(
        f"Matched : "
        f"{len(results['matched'])}"
    )

    print(
        f"Mismatched : "
        # f"{len(results['mismatched'])}"
        f"{len(set(row['policy_id'] for row in results['mismatch_details']))}"

    )

    print(
        f"Missing : "
        f"{len(results['missing'])}"
    )

    print(
        f"Additional : "
        f"{len(results['additional'])}"
    )

    print(
        f"Duplicates : "
        f"{len(results['duplicates'])}"
    )


    print("\nReport Generated Successfully")

    print(
        f"\nReport Location:\n{report_path}"
    )

    logger.info(
         f"Report Generated : {report_path}"
    )

    logger.info(
        "Framework Completed"
    )


if __name__ == "__main__":

    main()