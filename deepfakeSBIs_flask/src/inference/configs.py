HOST="101.43.93.152"
PORT=3306
USERNAME="root"
PASSWORD="cLZ@2002"
DATABASE="safe_record" 
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True