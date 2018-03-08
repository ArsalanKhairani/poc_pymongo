# the following 2 lines activate the virtual environment.
activate_this = '/home/madmin/venv/poc-pymongo/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
# because we store the app in a custom directory, this adds that directory to path.
import sys
sys.path.insert(0, '/home/madmin/poc_pymongo')
# import the application.
from app import app as application
