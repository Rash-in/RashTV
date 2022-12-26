# Initialization module for RashTV Django Frontend
import os, sys, argparse
from dotenv import load_dotenv

THIS_SCRIPT = os.path.realpath(__file__)
BIN_LOCATION = os.path.dirname(THIS_SCRIPT)
BASE_LOCATION = os.path.dirname(BIN_LOCATION)

RUNTIME_LOCATION = BASE_LOCATION + "/.env/runtime"
APP_LOCATION = BASE_LOCATION + "/src/web"
UVICORN_CONFIG = APP_LOCATION + "/config/uvicorn-config.py"

DOTENV_LOCATION = RUNTIME_LOCATION + "/local.env"
CERTS_PATH = RUNTIME_LOCATION + "/certs"
LOGS_PATH = RUNTIME_LOCATION + "/logs"
PIDS_PATH = RUNTIME_LOCATION + "/pids"

parser = argparse.ArgumentParser(
    prog='rashtv-web.py',
    description='Django Frontend Application Wrapper',
    epilog='''---'''
)
parser.add_argument('-e', '--environment', type=str, help='Environment being executed. Either "local" or "remote".')
args = parser.parse_args()
environment = args.environment

def main(environment):
    allowed_environments = ['local', 'remote']
    if environment in allowed_environments and environment == "local":
        load_dotenv(DOTENV_LOCATION)
        #os.system(f"cd {APP_LOCATION} && python -B manage.py collectstatic")
        os.system(f"cd {APP_LOCATION} && python -B -m gunicorn rashtv.asgi:application -k uvicorn.workers.UvicornWorker")
    elif environment in allowed_environments and environment == "remote":
        os.system(f"cd {APP_LOCATION} && python manage.py runserver")
    else:
        sys.exit(f"Invalid Arguments: {environment} is not in: {allowed_environments}")

if __name__ == "__main__":
    main(environment=environment)

# EOF