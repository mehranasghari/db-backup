import os
import subprocess
from dotenv import load_dotenv

def restore_db(type, file_path, database, host=None, port=None, user=None, password=None, email=None):
    
    load_dotenv(dotenv_path='.env')
    env = os.environ.copy()

    email_address = os.getenv('SEND_EMAIL_TO') if email is None else email
    db_restore_host = os.getenv('DB_RESTORE_HOST') if host is None else host
    db_restore_port = os.getenv('DB_RESTORE_PORT') if port is None else port
    db_restore_user = os.getenv('DB_RESTORE_USER') if user is None else user
    db_restore_password = os.getenv('DB_RESTORE_PASSWORD') if password is None else password
    db_restore_database = database
    db_restore_file_path = file_path

    email_success_command = ['python', 'pytide_courier.py', 'send-email', email_address, '"restore succeeded"', '"restore completed successfully"']
    email_failure_command = ['python', 'pytide_courier.py', 'send-email', email_address, '"restore failed"', '"restore failed"']


    if database == 'all':

        if type == 'mongodb':
            restore_command = ['mongodump', '--host=' + db_restore_host, '--port=' + db_restore_port, '--username=' +\
                db_restore_user, '--password=' + db_restore_password, '--authenticationDatabase=admin', '--archive']
        
        elif type == 'postgres':
            env['PGPASSWORD'] = db_restore_password
            restore_command = ['pg_dumpall', '-h', db_restore_host, '-p', db_restore_port, '-U', db_restore_user, '-w']

        elif type == 'mysql':
            restore_command = ['mysql', '-h', db_restore_host, '-P', db_restore_port, '-u' + db_restore_user, '-p' + db_restore_password]
        
        print(' '.join(restore_command))
        print(restore_command)
        with open(db_restore_file_path, 'r') as file:
            try:
                subprocess.run(restore_command, stdin=file, text=True, check=True, env=env)
                print('===========================================================\n')
                print('\033[92mDatabase restore completed\033[0m\n')
                print(f'restore file {db_restore_file_path} was successful\n')
                subprocess.run(email_success_command, text=True, check=True)

            except subprocess.CalledProcessError as e:
                print('===========================================================\n')
                print(f'\033[91mError during restore file: {db_restore_database}\033[0m\n{e.stderr}')
                subprocess.run(email_failure_command, text=True, check=True)
            except Exception as e:
                print('===========================================================\n')
                print(f'\033[91mError during restore file: {db_restore_file_path}\033[0m\n{e}')
    
    else:
        if type == 'mongodb':
            restore_command = ['mongodump', '--host=' + db_restore_host, '--port=' + db_restore_port, '--username=' +\
                db_restore_user, '--password=' + db_restore_password, '--db=' + db_restore_database, '--authenticationDatabase=admin', '--archive']
        
        elif type == 'postgres':
            env['PGPASSWORD'] = db_restore_password
            restore_command = ['pg_dump', '--dbname=' + db_restore_database, '-h', db_restore_host, '-p', db_restore_port, '-U', db_restore_user, '-w']

        elif type == 'mysql':
            restore_command = ['mysql', '-h', db_restore_host, '-P', db_restore_port, '-u' + db_restore_user, '-p' + db_restore_password, db_restore_database]
        
        print(' '.join(restore_command))
        print(restore_command)
        with open(db_restore_file_path, 'r') as file:
            try:
                subprocess.run(restore_command, stdin=file, text=True, check=True, env=env)
                print('===========================================================\n')
                print('\033[92mDatabase restore completed\033[0m\n')
                print(f'restore file {db_restore_file_path} was successful\n')
                subprocess.run(email_success_command, text=True, check=True)

            except subprocess.CalledProcessError as e:
                print('===========================================================\n')
                print(f'\033[91mError during restore file: {db_restore_database}\033[0m\n{e.stderr}')
                subprocess.run(email_failure_command, text=True, check=True)
            except Exception as e:
                print('===========================================================\n')
                print(f'\033[91mError during restore file: {db_restore_file_path}\033[0m\n{e}')