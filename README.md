ETL Reconciliation Automation Framework

Overview:

This project automates ETL reconciliation by comparing source and target datasets, identifying data quality issues, generating reconciliation reports, and validating workflows using Playwright automation.

Features:

User Authentication
Source/Target File Upload
Data Reconciliation
Missing Record Detection
Additional Record Detection
Duplicate Record Detection
Mismatch Detection
Excel Report Generation
Report Download
Logging Framework
Playwright Automation

Technology Stack:

Python
Pandas
OpenPyXL
Flask
Playwright
TypeScript
Automation Coverage
Positive Scenarios
Valid Login
Reconciliation Validation
Report Download Validation
Negative Scenarios
Invalid Login
Missing Target File Validation
Empty Source File Validation
Framework Design
Page Object Model (POM)
Data Driven Testing
Screenshot On Failure
Trace Viewer
HTML Reporting


How To Run:
1.Flask Application - python app.py
2.Playwright Tests -  cd Playwright-Framework -->  npx playwright test