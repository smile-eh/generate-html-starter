@echo off

if [%1]==[] goto usage

python .\generate-project-starter.py %1
goto :eof

:usage
@echo Usage: %0 Project_Path/Project_Name
exit /B 1