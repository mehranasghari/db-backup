import os
import subprocess
from datetime import datetime
from pytide_courier import pytide_courier
from dotenv import load_dotenv



def backup_postgres_all_databases(host, port, user):
    """Backup all databases in PostgreSQL database using pg_dumpall"""
    
    load_dotenv()
    EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')

    file_name = 'postgres_backup_all_db_' + datetime.now().strftime('%Y-%m-%d_%H%M%S') +'.db'
    backup_command = ['pg_dumpall', '-h', host, '-p', port, '-U', user, '-w']
    email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
    email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
    with open(file_name, 'w') as file:
        try:
            subprocess.run(backup_command, stdout=file, text=True, check=True)
            print('Database backup completed')
            print(f'Backup file saved in {file_name}')
            subprocess.run(email_success_command, text=True, check=True)
        
        except subprocess.CalledProcessError as e:
            print(f'Error during pg_dumpall: {e.stderr}')
            subprocess.run(email_failure_command, text=True, check=True)


def backup_postgres(host, port, user, database):
    """Backup specified databases in PostgreSQL database using pg_dump"""

    load_dotenv()
    EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')
    
    file_name = 'postgres_backup_' + database + '_' + datetime.now().strftime('%Y-%m-%d_%H%M%S') +'.db'
    backup_command = ['pg_dump', '-h', host, '-p', port, '-U', user, '-d', database, '-F', 'c', '-w']
    email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
    email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
    with open(file_name, 'w') as file:
        try:
            subprocess.run(backup_command,stdout=file, text=True, check=True)
            print('Database backup completed')
            print(f'Backup file saved in {file_name}')
            subprocess.run(email_success_command, text=True, check=True)

        except subprocess.CalledProcessError as e:
            print(f'Error during pg_dumpall: {e.stderr}')
            subprocess.run(email_failure_command, text=True, check=True)