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
```
WEB_APP_PATH='/path/to/RashTV/src/web'
API_APP_PATH='/path/to/RashTV/src/api'
CLI_APP_PATH='/path/to/RashTV/src/cli'
DB_APP_PATH='/path/to/RashTV/src/db'
RUNTIME_PATH='path/to/RashTV/.env/runtime'
```

9) In mysql workbench, create a service user account and database with the following permission sets.
Database: `rashtv`
Default Characterset: `utf8`
Default Collation: `utf8_bin`

User Acct: `rashtvsvc`
Object Rights: `SELECT, INSERT, UPDATE, DELETE, EXECUTE, SHOW VIEW`
DDL Rights: `CREATE, ALTER, REFERENCES, INDEX`