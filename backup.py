import os
import subprocess
from datetime import datetime
from pytide_courier import pytide_courier
from dotenv import load_dotenv

def backup_db(type, database, host=None, port=None, user=None, password=None, email=None):
    
    load_dotenv(dotenv_path='./.env')
    env = os.environ.copy()
    
    email_address = os.getenv('SEND_EMAIL_TO') if email is None else email
    db_backup_host = os.getenv('DB_BACKUP_HOST') if host is None else host
    db_backup_port = os.getenv('DB_BACKUP_PORT') if port is None else port
    db_backup_user = os.getenv('DB_BACKUP_USER') if user is None else user
    db_backup_password = os.getenv('DB_BACKUP_PASSWORD') if password is None else password

    email_success_command = ['python', 'pytide_courier.py', 'send-email', email_address, '"backup succeeded"', '"backup completed successfully"']
    email_failure_command = ['python', 'pytide_courier.py', 'send-email', email_address, '"backup failed"', '"backup failed"']

    file_name = 'backup_all_databases_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'
    if database == 'all':
        
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




#     print(' '.join(backup_command))
#     try:
#         subprocess.run(backup_command, text=True, check=True)
#         print('Database backup completed')
#         print(f'Backup file saved in {file_name}')
#         subprocess.run(email_success_command, text=True, check=True)

#     except subprocess.CalledProcessError as e:
#         print(f'Error during mysqldump: {e.stderr}')
#         subprocess.run(email_failure_command, text=True, check=True)
#     except Exception as e:
#         print(f'Error during mysqldump: {e}')

# def backup_postgres_all_databases(host, port, user):
#     """Backup all databases in PostgreSQL database using pg_dumpall"""
    
#     load_dotenv()
#     EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')

#     file_name = 'postgres_backup_all_db_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') +'.db'
#     backup_command = ['pg_dumpall', '-h', host, '-p', port, '-U', user, '-w']
#     email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
#     email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
#     with open(file_name, 'w') as file:
#         try:
#             subprocess.run(backup_command, stdout=file, text=True, check=True)
#             print('Database backup completed')
#             print(f'Backup file saved in {file_name}')
#             subprocess.run(email_success_command, text=True, check=True)
        
#         except subprocess.CalledProcessError as e:
#             print(f'Error during pg_dumpall: {e.stderr}')
#             subprocess.run(email_failure_command, text=True, check=True)


# def backup_postgres(host, port, user, database):
#     """Backup specified databases in PostgreSQL database using pg_dump"""

#     load_dotenv()
#     EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')
    
#     file_name = 'postgres_backup_' + database + '_' + datetime.now().strftime('%Y-%m-%d_%H%-M%-S') +'.db'
#     backup_command = ['pg_dump', '-h', host, '-p', port, '-U', user, '-d', database, '-F', 'c', '-w']
#     email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
#     email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
#     with open(file_name, 'w') as file:
#         try:
#             subprocess.run(backup_command,stdout=file, text=True, check=True)
#             print('Database backup completed')
#             print(f'Backup file saved in {file_name}')
#             subprocess.run(email_success_command, text=True, check=True)

#         except subprocess.CalledProcessError as e:
#             print(f'Error during pg_dumpall: {e.stderr}')
#             subprocess.run(email_failure_command, text=True, check=True)

# def backup_mysql(host, port, user, database):
#     """Backup specified database MySQL database using mysqldump"""

#     load_dotenv(dotenv_path='./db_secrets.env')
#     EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')
#     MYSQL_BACKUP_PASSWORD = os.getenv('MYSQL_BACKUP_PASSWORD')
#     MYSQL_BACKUP_USER = os.getenv('MYSQL_BACKUP_USER')
#     file_name = 'mysql_backup_' + database + '_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'
    
#     backup_command = ['mysqldump', '-h', host, '-P', port, '-u' + MYSQL_BACKUP_USER, '-p' + MYSQL_BACKUP_PASSWORD, database]
#     email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
#     email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
#     print(' '.join(backup_command))
#     with open(file_name, 'w') as file:
#         try:
#             subprocess.run(backup_command, stdout=file, text=True, check=True)
#             print('Database backup completed')
#             print(f'Backup file saved in {file_name}')
#             subprocess.run(email_success_command, text=True, check=True)

#         except subprocess.CalledProcessError as e:
#             print(f'Error during mysqldump: {e.stderr}')
#             subprocess.run(email_failure_command, text=True, check=True)
#         except Exception as e:
#             print(f'Error during mysqldump: {e}')


# def backup_mysql_all_databases(host, port, user):
#     """Backup specified database MySQL database using mysqldump"""

#     load_dotenv(dotenv_path='./db_secrets.env')
#     EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')
#     MYSQL_BACKUP_PASSWORD = os.getenv('MYSQL_BACKUP_PASSWORD')
#     MYSQL_BACKUP_USER = os.getenv('MYSQL_BACKUP_USER')
#     file_name = 'mysql_backup_all_db_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'
    
#     backup_command = ['mysqldump', '-h', host, '-P', port, '-u' + MYSQL_BACKUP_USER, '-p' + MYSQL_BACKUP_PASSWORD, '--all-databases']
#     email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
#     email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
#     print(' '.join(backup_command))
#     with open(file_name, 'w') as file:
#         try:
#             subprocess.run(backup_command, stdout=file, text=True, check=True)
#             print('Database backup completed')
#             print(f'Backup file saved in {file_name}')
#             subprocess.run(email_success_command, text=True, check=True)

#         except subprocess.CalledProcessError as e:
#             print(f'Error during mysqldump: {e.stderr}')
#             subprocess.run(email_failure_command, text=True, check=True)
#         except Exception as e:
#             print(f'Error during mysqldump: {e}')


# def backup_mongodb(host, port, user, database):
#     """Backup specified database in Mongodb database using mongodump"""

#     load_dotenv(dotenv_path='./db_secrets.env')
#     EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')
#     MONGODB_BACKUP_PASSWORD = os.getenv('MONGODB_BACKUP_PASSWORD')
#     MONGODB_BACKUP_USER = os.getenv('MONGODB_BACKUP_USER')
#     file_name = 'mongodb_backup_' + database + '_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'
    
#     backup_command = ['mongodump', '--host=' + host, '--port=' + port, '--username=' + MONGODB_BACKUP_USER,\
#          '--password=' + MONGODB_BACKUP_PASSWORD, '--db=' + database, '--authenticationDatabase=admin', '--archive=' + file_name]
#     email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
#     email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
#     print(' '.join(backup_command))
#     try:
#         subprocess.run(backup_command, text=True, check=True)
#         print('Database backup completed')
#         print(f'Backup file saved in {file_name}')
#         subprocess.run(email_success_command, text=True, check=True)

#     except subprocess.CalledProcessError as e:
#         print(f'Error during mysqldump: {e.stderr}')
#         subprocess.run(email_failure_command, text=True, check=True)
#     except Exception as e:
#         print(f'Error during mysqldump: {e}')


# def backup_mongodb_all_databases(host, port, user):
#     """Backup specified database in Mongodb database using mongodump"""

#     load_dotenv(dotenv_path='./db_secrets.env')
#     EMAIL_SEND_TO = os.getenv('EMAIL_SEND_TO')
#     MONGODB_BACKUP_PASSWORD = os.getenv('MONGODB_BACKUP_PASSWORD')
#     MONGODB_BACKUP_USER = os.getenv('MONGODB_BACKUP_USER')
#     file_name = 'mongodb_backup_all_databases_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.db'
    
#     backup_command = ['mongodump', '--host=' + host, '--port=' + port, '--username=' + MONGODB_BACKUP_USER,\
#          '--password=' + MONGODB_BACKUP_PASSWORD, '--authenticationDatabase=admin', '--archive=' + file_name]
#     email_success_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup succeeded"', '"backup completed successfully"']
#     email_failure_command = ['python', 'pytide_courier.py', 'send-email', EMAIL_SEND_TO, '"backup failed"', '"backup failed"']
    
#     print(' '.join(backup_command))
#     try:
#         subprocess.run(backup_command, text=True, check=True)
#         print('Database backup completed')
#         print(f'Backup file saved in {file_name}')
#         subprocess.run(email_success_command, text=True, check=True)

#     except subprocess.CalledProcessError as e:
#         print(f'Error during mysqldump: {e.stderr}')
#         subprocess.run(email_failure_command, text=True, check=True)
#     except Exception as e:
#         print(f'Error during mysqldump: {e}')