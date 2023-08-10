@echo off
start cmd /k "cd chat && python manage.py runserver"
start cmd /k "cd noneBot && python bot.py"
start cmd /k "cd go-cqhttp && .\go-cqhttp_windows_amd64.exe"
