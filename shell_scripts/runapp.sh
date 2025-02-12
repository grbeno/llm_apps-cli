#!/bin/bash

# Change the working directory to the directory where the script is located
cd "."

# Initialize variables with default values

MODEL="gpt-4o-mini"
ROLE="short and concise"

menu() {
    echo "This is an AI based natural language tool written in Python."
    echo "Please select:"
    echo
    echo "1) Set Model"
    echo "2) Set Role"
    echo "3) Run Application"
    echo "4) Exit"
    echo
    echo "Current settings:"
    echo "Model: $MODEL"
    echo "Role: $ROLE"
    echo
    read -p "Enter your choice (1-4): " CHOICE

    case $CHOICE in
        1) set_model ;;
        2) set_role ;;
        3) run_app ;;
        4) safe_exit ;;
        *) echo "Invalid choice. Please try again."; sleep 2; menu ;;
    esac
}

set_model() {
    clear
    echo "Select Model:"
    echo "1) gpt-4o-mini"
    echo "2) gpt-4o"
    echo "3) llama3.1"
    echo
    read -p "Enter model (1-3): " MODEL_CHOICE

    case $MODEL_CHOICE in
        1) MODEL="gpt-4o-mini" ;;
        2) MODEL="gpt-4o" ;;
        3) MODEL="llama3.1" ;;
        *) echo "Invalid choice. Please try again."; sleep 2; set_model ;;
    esac
    menu
}

set_role() {
    echo "Select Role:"
    echo "1) Correct English"
    echo "2) Correct German"
    echo "3) Translate to English"
    echo "4) Translate to Hungarian"
    echo "5) Translate to German"
    echo "6) Upgrade English"
    echo "7) Remaster the conversation"
    echo
    read -p "Enter role (1-7): " ROLE_CHOICE

    case $ROLE_CHOICE in
        1) ROLE="correct english" ;;
        2) ROLE="correct german" ;;
        3) ROLE="translate to english" ;;
        4) ROLE="translate to hungarian" ;;
        5) ROLE="translate to german" ;;
        6) ROLE="upgrade english" ;;
        7) ROLE="remaster the conversation" ;;
        *) echo "Invalid choice. Please try again."; sleep 2; set_role ;;
    esac
    menu
}

run_app() {
    # Activate the virtual environment and run the application
    source venv/bin/activate
    VENV_ACTIVATED=1
    python3 chat.py --m "$MODEL" --r "$ROLE"
    menu
}

safe_exit() {
    if [ "$VENV_ACTIVATED" == 1 ]; then
        echo "Deactivating virtual environment..."
        deactivate
    fi
    echo "Exiting..."
    exit 0
}

menu
