import os
import click
from dotenv import load_dotenv
from backup import *
import stat

load_dotenv(dotenv_path='./db_secrets.env')

@click.command()
@click.option('-t', '--type', help='Database type', required=True, type=click.Choice(['postgres', 'mysql', 'mongodb'], case_sensitive=False))
@click.option('-d', '--database', help='Database name to backup', default='all')
@click.option('-h', '--host', default=os.getenv('BACKUP_DB_HOST'),help='Database host', required=True, envvar='BACKUP_DB_HOST')
@click.option('-p', '--port', default=os.getenv('BACKUP_DB_PORT'), help='Database port for connecting', required=True, envvar='BACKUP_DB_PORT')
@click.option('-u', '--user', default=os.getenv('BACKUP_DB_USER'), help='With what user backup database', required=True, envvar='BACKUP_DB_USER')
@click.option('--password', default=os.getenv('BACKUP_DB_PASS'), help='Password of the user to connect the database', required=True, envvar='BACKUP_DB_PASS')
def backup(type, database, host, port, user, password):
    if type == 'postgres':
        home_directory = os.path.expanduser("~")
        pgpass_file_path = os.path.join(home_directory, ".pgpass")

        with open(pgpass_file_path, 'w') as pgpass_file:
            pgpass_file.write(f"{host}:{port}:*:{user}:{password}")
        os.chmod(pgpass_file_path, 0o600)

        if database == 'all':
            backup_postgres_all_databases(host, port, user)
        else:
            backup_postgres(host, port, user, database)
    elif type == 'mysql':
        if database == 'all':
            backup_mysql_all_databases(host, port, user)
        else:
            backup_mysql(host, port, user, database)
    
if __name__ == '__main__':
    backup()