from sql.DatabaseAccess import DatabaseAccess
from constants.SQLStatements import SQLStatements



class sqlread:
    
    def __init__(self):
        self.db = DatabaseAccess()
      
      
    def topicloggedin(self,userid,limitoffset):
        topicfinal =[]
        forcommentfinal=[]
        againstcommentfinal=[]
        sqltopic=  SQLStatements.GET_TOPIC_SQL
        sqlcomment =SQLStatements.GET_COMMENT_SQL
        sqlcommentception = SQLStatements
        args =(limitoffset,)
        print("topicloggedin start")
        cursor = self.db.executeReadSQLWithArgsStatement(sqltopic,args)
        resulttopic =cursor.fetchall()
        print("topicloggedin end")
        print(resulttopic)        
        
        for i in range(0,(len(resulttopic))):
            args =(resulttopic[i][0],)
            cursorcomment = self.db.executeReadSQLWithArgsStatement(sqlcomment,args);
            resultcomment = cursorcomment.fetchall();
            print(len(resultcomment))
            print(resultcomment)
            if (len(resultcomment) >0):
                print("1")
                for j in range(0,(len(resultcomment))):
                    print("2")
                    if (resultcomment[j][4]==1):
                        print("3")  
                        comment= {"commentid":resultcomment[j][0],"commentdata":resultcomment[j][1].decode('ascii'),"commentuserid":resultcomment[j][2],"commenttopicid":resultcomment[j][3],"Likecount":resultcomment[j][5]}
                        forcommentfinal.append(comment)
                        comment={}
                    else:
                        print("4")
                        comment= {"commentid":resultcomment[j][0],"commentdata":resultcomment[j][1].decode('ascii'),"commentuserid":resultcomment[j][2],"commenttopicid":resultcomment[j][3],"Likecount":resultcomment[j][5]}
                        againstcommentfinal.append(comment)
                        comment={}  
                        
                                  
            else:
                print("7")
                comment= {"commentid":"null","commentdata":"nocomments","commenttopicid":"null","Likecount":"null","commentuserid":"null"}
                forcommentfinal.append(comment.copy())
                againstcommentfinal.append(comment.copy())
                comment={}
                
            if(len(forcommentfinal)==0):
                        print("5")
                        comment= {"commentid":"null","commentdata":"nocomments","commenttopicid":"null","Likecount":"null","commentuserid":"null"}
                        forcommentfinal.append(comment.copy())
                        comment={}
            if(len(againstcommentfinal)==0):
                        print("6")
                        comment= {"commentid":"null","commentdata":"nocomments","commenttopicid":"null","Likecount":"null","commentuserid":"null"}
                        againstcommentfinal.append(comment.copy())
                        comment={}    
                   
            topic={"topicid":resulttopic[i][0],"topicdata":resulttopic[i][1].decode('ascii'),"forcomment":tuple(forcommentfinal),"againstcomment":tuple(againstcommentfinal), "topicuserid":resulttopic[i][2]}
            
            topicfinal.append(topic.copy());
            forcommentfinal=[]
            againstcommentfinal=[]
            topic={} 
        return(topicfinal)   
                 
   
        
