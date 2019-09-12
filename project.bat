
@ECHO OFF 

REM If no input after "project" 
IF [%1]==[] GOTO error

REM Record original location of command prompt
SET filePath=%cd%

REM Goto location of script on system
CD %~dp0

REM Run githubUrl script to establish GitHub repository
"python" "%~dp0githubUrl.py" %1 > out

REM Grab username written to command prompt by python script
SET /p userName=<out
DEL out

CD %filePath%

REM Return to original command prompt location and clone GitHub repository
"git" "clone" "https://github.com/%userName%/%1.git"

REN %1 "%1 Project"

CD "%filePath%\%1 Project"

REM Error case: If there is no input after "project", the usage case will be shown
GOTO :eof

:error
ECHO Usage: %0 ^<RepositoryName^>