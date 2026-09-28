@echo off

cd /d "%~dp0"

git add .
git commit -m "Auto update"
git push

echo.
echo =========================
echo Successfully pushed to GitHub!
echo =========================
pause