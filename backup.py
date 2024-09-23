import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

def backup_db(type, database, host=None, port=None, user=None, password=None, email=None):
    
    load_dotenv(dotenv_path='.env')
    env = os.environ.copy()

    email_address = os.getenv('SEND_EMAIL_TO') if email is None else email
    db_backup_host = os.getenv('DB_BACKUP_HOST') if host is None else host
    db_backup_port = os.getenv('DB_BACKUP_PORT') if port is None else port
    db_backup_user = os.getenv('DB_BACKUP_USER') if user is None else user
    db_backup_password = os.getenv('DB_BACKUP_PASSWORD') if password is None else password
    db_backup_database = os.getenv('DB_BACKUP_DATABASE') if database is None else database

    email_success_command = ['python', 'pytide_courier.py', 'send-email', email_address, '"backup succeeded"', '"backup completed successfully"']
    email_failure_command = ['python', 'pytide_courier.py', 'send-email', email_address, '"backup failed"', '"backup failed"']


    if database == 'all':
        file_name = 'backup_all_databases_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'

        if type == 'mongodb':
            file_name = 'mongodb_' + file_name
            backup_command = ['mongodump', '--host=' + db_backup_host, '--port=' + db_backup_port, '--username=' +\
                db_backup_user, '--password=' + db_backup_password, '--authenticationDatabase=admin', '--archive']
        
        elif type == 'postgres':
            file_name = 'postgres_' + file_name
            env['PGPASSWORD'] = db_backup_password
            backup_command = ['pg_dumpall', '-h', db_backup_host, '-p', db_backup_port, '-U', db_backup_user, '-w']

        elif type == 'mysql':
            file_name = 'mysql_' + file_name
            backup_command = ['mysqldump', '-h', db_backup_host, '-P', db_backup_port, '-u' + db_backup_user, '-p' + db_backup_password, '--all-databases']
        
        print(' '.join(backup_command))
        print(backup_command)
        with open(file_name, 'w') as file:
            try:
                subprocess.run(backup_command, stdout=file, text=True, check=True, env=env)
                print('===========================================================\n')
                print('\033[92mDatabase backup completed\033[0m\n')
                print(f'Backup file saved in {file_name}\n')
                subprocess.run(email_success_command, text=True, check=True)

            except subprocess.CalledProcessError as e:
                print('===========================================================\n')
                print(f'\033[91mError during backup database: {e.stderr}\033[0m')
                subprocess.run(email_failure_command, text=True, check=True)
            except Exception as e:
                print('===========================================================\n')
                print(f'\033[91mError during backup database: {e}\033[0m')
    
    else:
        file_name = 'backup_' + db_backup_database + '_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'
        if type == 'mongodb':
            file_name = 'mongodb_' + file_name
            backup_command = ['mongodump', '--host=' + db_backup_host, '--port=' + db_backup_port, '--username=' +\
                db_backup_user, '--password=' + db_backup_password, '--db=' + db_backup_database, '--authenticationDatabase=admin', '--archive']
        
        elif type == 'postgres':
            file_name = 'postgres_' + file_name
            env['PGPASSWORD'] = db_backup_password
            backup_command = ['pg_dump', '--dbname=' + db_backup_database, '-h', db_backup_host, '-p', db_backup_port, '-U', db_backup_user, '-w']

        elif type == 'mysql':
            file_name = 'mysql_' + file_name
            backup_command = ['mysqldump', '-h', db_backup_host, '-P', db_backup_port, '-u' + db_backup_user, '-p' + db_backup_password, db_backup_database]
        
        print(' '.join(backup_command))
        print(backup_command)
        with open(file_name, 'w') as file:
            try:
                subprocess.run(backup_command, stdout=file, text=True, check=True, env=env)
                print('===========================================================\n')
                print('\033[92mDatabase backup completed\033[0m\n')
                print(f'Backup file saved in {file_name}\n')
                subprocess.run(email_success_command, text=True, check=True)

            except subprocess.CalledProcessError as e:
                print('===========================================================\n')
                print(f'\033[91mError during backup database: {e.stderr}\033[0m')
                subprocess.run(email_failure_command, text=True, check=True)
            except Exception as e:
                print('===========================================================\n')
                print(f'\033[91mError during backup database: {e}\033[0m')
