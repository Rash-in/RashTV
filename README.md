# RashTV
Django, FastAPI, Typer Command Line Tool, and SQLite application used to host media libraries privately to internal networks. A work in progress. Not ready for consumption.

## Local Installation
1) clone and cd into the repo directory
2) Create Virtual Environment: `python3 venv .env`
3) Activate Virtual Environment: `source .env/bin/activate` or `. .env/bin/activate`
4) Install dependencies: `pip install -r src/requirements.txt`
5) In RashTV/.env create the folder `runtime`
6) In the `runtime` folder create folders called `certs`, `logs`, `pids`
7) In the `runtime` folder create file called `local.env`.

8) In `local.env` create the following variables:
```python
WEB_APP_PATH='/path/to/RashTV/src/web'  #Change Path
API_APP_PATH='/path/to/RashTV/src/api'  #Change Path
CLI_APP_PATH='/path/to/RashTV/src/cli'  #Change Path
RUNTIME_PATH='/path/to/RashTV/.env/runtime' # Change Path
DJANGO_SETTINGS_MODULE='rashtv.config.settings'
DJANGO_STATIC_ROOT='/path/to/RashTV/src/web/rashtv/static'  # Change Path
DJANGO_DEBUG='True'
DJANGO_SECRET_KEY='SEE STEP 9'  #Change with input from step 9.
DJANGO_DB_ENGINE='django.db.backends.mysql'
DJANGO_DB_NAME='rashtv'
DJANGO_DB_USER='rashtvsvc'
DJANGO_DB_PASS=''   # Change to your password
DJANGO_DB_HOST=''   # Change to your db ip or hostname
DJANGO_DB_PORT='3306'
```

9) For the DJANGO_SECRET_KEY use python shell by just typing `python` in a command line and enter the following:
`from django.core.management.utils import get_random_secret_key`
`print(get_random_secret_key())`
copy/paste this into the value for DJANGO_SECRET_KEY

10) In mysql workbench, create a service user account and database with the following permission sets.
Database: `rashtv`
Characterset: `utf8`
Collation: `utf8_bin`

User Acct: `rashtvsvc`
Object Rights: `SELECT, INSERT, UPDATE, DELETE, EXECUTE, SHOW VIEW`
DDL Rights: `CREATE, ALTER, REFERENCES, INDEX`

