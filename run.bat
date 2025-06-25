@echo off
echo =============================
echo Running Pytest Test Suite...
echo =============================

REM Activate virtual environment (if used)
call venv\Scripts\activate

REM Run Pytest with HTML report
pytest -m "smoke" --html=reports/report.html --self-contained-html --maxfail=2 --tb=short

echo =============================
echo Test execution completed.
echo Report generated at reports\report.html
echo =============================
pause
