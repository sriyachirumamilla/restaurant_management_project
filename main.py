#main.py
import os
import sys
from django/core.management import execute_from_command_line

def main():
    """Run Django server or any given command."""

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')

    if len(sys.argv) == 1:
        # If no arguments, default to running the development server
        sys.argv += ['runserver', '0.0.0.0:8000']
    execute_from_command_line(sys.argv)
if __name__ == '__main__':
    main()