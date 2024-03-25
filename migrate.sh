#!/bin/bash
CMD=$1
case $CMD in
    "init")
        alembic init -t async migrations
        ;;
    "run")
        alembic upgrade head
        ;;
    "add")
        if [ -z "$2" ]; then
            echo "Add a name/message for the migration."
            exit 1
        fi
        alembic revision --autogenerate -m "$2"
        ;;
    "revert")
        alembic downgrade -1
        echo "Make sure to delete the downgraded migration file in versions/ folder."
        ;;
    *)
        echo "$1 is not a command.\nCommands: init | run | add {MESSAGE/NAME} | revert"
        ;;
esac

