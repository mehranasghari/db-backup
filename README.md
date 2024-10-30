# DB Backup




DB-Backup is a simple and efficient tool for backing up and restoring three popular databases: MySQL, PostgreSQL, and MongoDB.

## Requirements
Python 3.x
Required libraries (listed in requirements.txt)

## Installation
Clone the repository:

``` bash
git clone https://github.com/mehranasghari/db-backup.git
cd db-backup
```
Install dependencies:

``` bash
pip install -r requirements.txt
```

## Usage
### Backup
``` bash
python db_backup.py --action backup --db-type <mysql/postgres/mongodb> --host <host> --user <user> --password <password>
```
### Restore
``` bash
python db_backup.py --action restore --db-type <mysql/postgres/mongodb> --host <host> --user <user> --password <password> --file <backup-file>
```
Notes:
Ensure you have the required permissions and correct configuration for each database.

you must have `postgresql-client` pcakage present on your system. If you don't have just run `sudo apt install postgresql-client`

you must have `mysql-client` package present on your system. If you don't have just run `sudo apt install mysql-client`

For backing up mongodb you must have `mongodump` tool installed on your system.

## Contributing
Feel free to submit issues, fork the repository, and make pull requests!

## License
This project is licensed under the MIT License.