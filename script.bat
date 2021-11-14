@echo off

cd C:\Users\ljjun\project_oikk\WebProject\frontend\InstagramBot_2.0

IF NOT EXIST mission_clear.txt (
  python ./src/main.py
  pause
) ELSE (
  shutdown -s -t 60
  EXIT
)