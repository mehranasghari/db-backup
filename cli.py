import os
import click
from dotenv import load_dotenv
from backup import *
import stat

load_dotenv(dotenv_path='./db_secrets.env')

@click.command()
@click.option('-t', '--type', help='Database type', required=True, type=click.Choice(['postgres', 'mysql', 'mongodb'], case_sensitive=False))
@click.option('-d', '--database', help='Database name to backup', default='all')
@click.option('-h', '--host', default=None, help='Host of database', required=True)
@click.option('-p', '--port', default=None, help='Database port for connecting', required=True)
@click.option('-u', '--user', default=None, help='With what user connect to the database', required=True)
@click.option('--password', default=None, help='Password of the user to connect the database', required=True)
@click.option('-e', '--email', default=None, help='Email address to send the status of backup')

def backup(type, database, host, port, user, password, email):
    backup_db(type, database, host, port, user, password, email)
    # if type == 'postgres':
    #     home_directory = os.path.expanduser("~")
    #     pgpass_file_path = os.path.join(home_directory, ".pgpass")

    #     with open(pgpass_file_path, 'w') as pgpass_file:
    #         pgpass_file.write(f"{host}:{port}:*:{user}:{password}")
    #     os.chmod(pgpass_file_path, 0o600)

    #     if database == 'all':
    #         backup_postgres_all_databases(host, port, user)
    #     else:
    #         backup_postgres(host, port, user, database)
    # elif type == 'mysql':
    #     if database == 'all':
    #         backup_mysql_all_databases(host, port, user)
    #     else:
    #         backup_mysql(host, port, user, database)
    # elif type == 'mongodb':
    #     if database == 'all':
    #         backup_mongodb_all_databases(host, port, user)
    #     else:
    #         backup_mongodb(host, port, user, database)
    
if __name__ == '__main__':
    backup()