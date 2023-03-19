from dotenv import load_dotenv
import os
load_dotenv()

DB_URI = os.environ.get('DB_URI')
PORT =  os.environ.get('PORT') or 3001
class Config(object):
    """
    This class is used to set the configuration for the application.
    """
    MONGODB_SETTINGS = {
        'host' : DB_URI,
    }
    PORT = PORT
    DEBUG = True
