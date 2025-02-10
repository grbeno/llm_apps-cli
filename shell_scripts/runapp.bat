@echo off
setlocal enabledelayedexpansion

cd /d "<path>"

:: Initialize variables with default values
set ROLE="short and concise"
set MODEL="gpt-4o-mini"

:menu
cls
echo This is an AI based natural language tool written in Python.
echo Please select:
echo.
echo 1) Set Model
echo 2) Set Role
echo 3) Run Application
echo 4) Exit
echo.
echo Current settings:
echo Model: %MODEL%
echo Role: %ROLE%
echo.

set /p CHOICE="Enter your choice (1-4): "

if "%CHOICE%"=="1" goto set_model
if "%CHOICE%"=="2" goto set_role
if "%CHOICE%"=="3" goto run_app
if "%CHOICE%"=="4" goto safe_exit

echo Invalid choice. Please try again.
timeout /t 2 >nul
goto menu

:set_model
:: select model
cls
echo Select Model:
echo 1) gpt-4o-mini
echo 2) gpt-4o
echo 3) llama3.1
echo.

set /p MODEL_CHOICE="Enter role (1-3): "

if "%MODEL_CHOICE%"=="1" set MODEL="gpt-4o-mini"
if "%MODEL_CHOICE%"=="2" set MODEL="gpt-4o"
if "%MODEL_CHOICE%"=="3" set MODEL="llama3.1"

:set_role
:: select role
cls
echo Select Role:
echo 1) Correct English
echo 2) Correct German
echo 3) Translate to English
echo 4) Translate to Hungarian
echo 5) Translate to German
echo 6) Upgrade English
echo 7) Remaster the conversation
echo.

set /p ROLE_CHOICE="Enter role (1-7): "

if "%ROLE_CHOICE%"=="1" set ROLE="correct english"
if "%ROLE_CHOICE%"=="2" set ROLE="correct german"
if "%ROLE_CHOICE%"=="3" set ROLE="translate to english"
if "%ROLE_CHOICE%"=="4" set ROLE="translate to hungarian"
if "%ROLE_CHOICE%"=="5" set ROLE="translate to german"
if "%ROLE_CHOICE%"=="6" set ROLE="upgrade english"
if "%ROLE_CHOICE%"=="7" set ROLE="remaster the conversation"
goto menu

:run_app
call .venv/Scripts/activate
set VENV_ACTIVATED=1
python chat.py --m %MODEL% --r %ROLE%
goto menu

:safe_exit
:: Check if virtual environment is activated before deactivating
if "%VENV_ACTIVATED%"=="1" (
    echo Deactivating virtual environment...
    call deactivate
)
echo Exiting...
exit /b

