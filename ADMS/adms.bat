@echo off
cd /d D:\MEET\ADMS
git add .
git commit -m "update"
git pull origin main --rebase
git push origin main
pause
