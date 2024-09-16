import os
import subprocess
from datetime import datetime

def backup_postgres_all_databases(host, port, user):
    """Backup all databases in PostgreSQL database using pg_dumpall"""
    file_name = 'postgres_backup_all_db_' + datetime.now().strftime('%Y-%m-%d_%H%M%S') +'.sql'
    command = [
            'pg_dumpall',
            '-h', host,
            '-p', port,
            '-U', user,
            '-w'
        ]
    with open(file_name, 'w') as file:
        try:
            subprocess.run(command, stdout=file, text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Error during pg_dumpall: {e.stderr}')