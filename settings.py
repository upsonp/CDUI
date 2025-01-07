import os
import environ

BASE_DIR = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
env = environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SETTINGS = {
    'CONNECTION': None
}