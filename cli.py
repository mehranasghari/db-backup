import os
import click
from dotenv import load_dotenv
from backup import *
import stat

load_dotenv(dotenv_path='./db_secrets.env')

@click.command()
@click.option('-t', '--type', help='Database type', required=True, type=click.Choice(['postgres', 'mysql', 'mongodb'], case_sensitive=False))
@click.option('-d', '--database', help='Database name to backup', default='all')
@click.option('-h', '--host', default=None, help='Host of database')
@click.option('-p', '--port', default=None, help='Database port for connecting')
@click.option('-u', '--user', default=None, help='With what user connect to the database')
@click.option('--password', default=None, help='Password of the user to connect the database')
@click.option('-e', '--email', default=None, help='Email address to send the status of backup')

def backup(type, database, host, port, user, password, email):
    backup_db(type, database, host, port, user, password, email)

if __name__ == '__main__':
    backup()