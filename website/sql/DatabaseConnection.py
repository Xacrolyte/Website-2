import MySQLdb
from Utility.FileUtility import FileUtility

class DatabaseConnection:
    fileData = FileUtility()
    dbsettingsDictionary = fileData.readDBSettings()
    dbServer = dbsettingsDictionary['Server'];
    dbName = dbsettingsDictionary['Name'];
    dbUserName = dbsettingsDictionary['UserName'];
    dbPassword = dbsettingsDictionary['Password'];
    db = MySQLdb.connect(dbServer,dbUserName,dbPassword,dbName)
    cursor = db.cursor()
    print("Database connection successful!!!")
    
    @staticmethod
    def getDBConnection():
        return DatabaseConnection.db
    
    @staticmethod
    def getDBCursor():
        return DatabaseConnection.cursor
    
    