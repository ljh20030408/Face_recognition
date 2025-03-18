a=1
HOSTNAME = '101.43.93.152'
PORT = '3306'
DATABASE = 'safe_record'
USERNAME = 'root'
PASSWORD = 'cLZ@2002'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOSTNAME,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True