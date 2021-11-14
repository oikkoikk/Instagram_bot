@echo off

cd C:\Users\ljjun\Instagram_bot

IF NOT EXIST mission_clear.txt (
  python ./src/main.py
  pause
) ELSE (
  shutdown -s -t 60
  EXIT
)