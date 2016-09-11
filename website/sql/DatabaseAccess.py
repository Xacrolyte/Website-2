from sql.DatabaseConnection import DatabaseConnection

class DatabaseAccess:
    
    def __init__(self):
        self.dbConnection = DatabaseConnection.getDBConnection()
        self.dbCursor = DatabaseConnection.getDBCursor()
    
    def getVersion(self):
        self.dbCursor.execute("SELECT VERSION()")
        return self.dbCursor.fetchone()
    
    def executeInsertSQLStatement(self,sql,args):   
        try:
            self.dbCursor.execute(sql,args)
            self.dbConnection.commit()
        except Exception as e: 
            print (str(e))
            self.dbConnection.rollback()

    def executeReadSQLStatement(self,sql):
        try:
            self.dbCursor.execute(sql)
            self.dbConnection.commit()
            return  self.dbCursor
        except Exception as e: 
            print (str(e))
            self.dbConnection.rollback()
    
    def executeReadSQLWithArgsStatement(self,sql,args):
        try:
            self.dbCursor.execute(sql,args)
            self.dbConnection.commit()
            return self.dbCursor
        except Exception as e: 
            print (str(e))
            self.dbConnection.rollback()
            
    def executeUpdateSQLStatement(self,sql,args):    
        try:
            self.dbCursor.execute(sql,args)
            self.dbConnection.commit()
#             print ("Update Executed Successfully")
            return self.dbConnection.fetchAll()
        except Exception as e: 
            print (str(e))
            self.dbConnection.rollback()
        
            
        