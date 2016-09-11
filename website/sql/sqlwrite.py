from sql.DatabaseAccess import DatabaseAccess
from constants.SQLStatements import SQLStatements



class sqlwrite:
    
    def __init__(self):
        self.db = DatabaseAccess()
      
      
    def topicinsert (self,topicid,topicdata,userid):
        print("topic database access start")    
        sql=  SQLStatements.INSERT_INTO_TOPIC_SQL
        args =(topicid,topicdata,userid,)
        cursor = self.db.executeInsertSQLStatement(sql,args)
        print("sqlwrite database access end")    
        
    def userinsert(self,name,email,userid):
        print("topic database access start") 
        sql=  SQLStatements.INSERT_INTO_USER_SQL
        args =(name,email,userid,)
        cursor = self.db.executeInsertSQLStatement(sql,args)
        print("sqlwrite database access")    
        
        
    def commentinsert (self,commentid,commentdata,userid,topicid,foragainst):
        print("commentinsert enter")  
        sql= SQLStatements.INSERT_INTO_COMMENT_SQL
        args = (commentid, commentdata, userid,topicid,foragainst,)
        cursor = self.db.executeInsertSQLStatement(sql,args)
        
    def commentceptioninsert(self,commentceptionid,commentceptiondata,commentceptionuserid,commentceptioncommentid):    
        sql= SQLStatements.INSERT_INTO_COMMENTCEPTION_SQL
        args = (commentceptionid,commentceptiondata,commentceptionuserid,commentceptioncommentid,)
        cursor = self.db.executeInsertSQLStatement(sql,args)
    
    def commentlikeinsert(self,commentid,userid):
        sql =SQLStatements.INSERT_INTO_COMMENTLIKE_SQL
        args =(commentid,userid,)
        cursor = self.db.executeInsertSQLStatement(sql,args)
        
    def commentceptionlikeinsert(self,commentceptionid,userid):
        sql=SQLStatements.INSERT_INTO_COMMENTCEPTIONLIKE_SQL
        args=(commentceptionid,userid,) 
        cursor = self.db.executeInsertSQLStatement(sql,args)  