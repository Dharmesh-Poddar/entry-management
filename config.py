import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

# Twilio keys
account_sid = 'AC4791466c042afe63441f443b08ed04d1'
auth_token = 'bc142e43169be16f97b073107a75e67d'
from_phone = '+13343800679'

# sendgrid key
SENDGRID_API_KEY = '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'

#Office Address
address = '4560 1 Javier Street, Dallas, Texas'