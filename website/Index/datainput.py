from elasticsearch import Elasticsearch


class datain:
    
    es = Elasticsearch()
    def __init__(self,info):
        self.a =info

    def index(self,user_login_info ):
        
        res = self.es.search(index="index_user", body={"query": {"match": {"id":user_login_info['sub']}}})
        if(res['hits']['total']==0):
            doc={'name':user_login_info['name'],
                 'email':user_login_info['email'],
                 'id': user_login_info['sub'],
                 'list_of_likes':(0,1),
                 'list of answers':('topic+answer','t+a')
                }
            res_in = self.es.index(index="index_user", doc_type='law', body=doc)
            print ('indexed')
            print(res_in)
        else:
            print(res)
            
        return str("sucessfully signed in")
        
        
        
    
    