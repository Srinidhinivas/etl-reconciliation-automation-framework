import os
from reconciliation.compare_engine import ReconciliationEngine
from reconciliation.report_generator import ReportGenerator
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
from flask import flash

VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"

latest_report_path = None

app = Flask(__name__)

app.secret_key = "etl-framework"

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return render_template(
        "login.html"
    )
@app.route(
    "/login",
    methods=["POST"]
)
def login():

    username = request.form[
        "username"
    ]

    password = request.form[
        "password"
    ]

    if (
        username == VALID_USERNAME
        and
        password == VALID_PASSWORD
    ):

        return render_template(
            "index.html"
        )

    return render_template(
        "login.html",
        error_message=
        "Invalid Username or Password"
    )

    
@app.route(
    "/compare",
    methods=["POST"]
)
def compare():

    source_file = request.files[
        "source_file"
    ]

    target_file = request.files[
        "target_file"
    ]

    source_path = os.path.join(
        UPLOAD_FOLDER,
        source_file.filename
    )

    target_path = os.path.join(
        UPLOAD_FOLDER,
        target_file.filename
    )

    source_file.save(source_path)

    target_file.save(target_path)

    try:

        engine = ReconciliationEngine(
            source_path,
            target_path
        )

        results = engine.compare()

    except Exception as error:

        return render_template(
            "index.html",
            error_message=str(error)
        )

    report_generator = ReportGenerator()

    global latest_report_path

    latest_report_path = (
        report_generator.generate_report(
            results,
            "data/output"
        )
    )

    return render_template(
        "results.html",

        source_count=results["source_count"],

        target_count=results["target_count"],

        matched=len(results["matched"]),

        # mismatched=len(results["mismatched"]),
        mismatched=len(
            set(
                row["policy_id"]
                for row in results["mismatch_details"]
            )
        ),

        missing=len(results["missing"]),

        additional=len(results["additional"]),

        duplicates=len(results["duplicates"])
    )

@app.route("/download")
def download_report():

    global latest_report_path

    return send_file(
        latest_report_path,
        as_attachment=True
    )

if __name__ == "__main__":

    app.run(
        debug=True
    )