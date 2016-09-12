from flask import Flask, render_template, request
from Index.datainput import datain
from oauth2client import client, crypt
import json
import urllib.request
import re
import uuid
from sql.sqlwrite import sqlwrite
from sql.sqlread import sqlread
 
result={}
sub = ""

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('login.html')



@app.route("/tokensignin",methods=['POST'])
def tokensignin():
    
    data = request.form
    #print(data)
    try:
        idinfo = client.verify_id_token(data["idtoken"], 'use your own web client id') 
    # If multiple clients access the backend server:
        if idinfo['aud'] not in ['use your own web client id']:
            return("Unrecognized client.")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return ("Wrong issuer.")
    except crypt.AppIdentityError as e :
        return("Verification failed")
    # look for reasons of above error and how to handle it
    # also look for crypt.AppIdentityerror
    # Invalid token
   # x=datain('a').index(idinfo)
    #print(idinfo)
    sqlwrite().userinsert(idinfo["name"],idinfo["email"],idinfo["sub"])
    return "hello"


@app.route("/loggedin",methods=['POST'])
def loggedin():
    data =request.form
    #print(data)
    idinfo = client.verify_id_token(data['datas'], 'use your own web client id')
    sub = idinfo["sub"]
    print (idinfo["sub"])
    
    return render_template('logged.html' ,id=idinfo["sub"])




@app.route("/topicslogin", methods=['POST'])
def topicslogin():          // still working on layout of webpage and thus using garbage data
    d=request.get_json(force=True)
    topic=({'topic':"my name is ali",'a':({'comment':"1st comment",'reply':{'b':"hahahaha", "likes":3,"id":1},"likes":4,'id':1},{'comment':"2st comment",'reply':{'b':"hahahaha", "likes":3,"id":2},"likes":4,'id':1245},{'comment':"3st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"4st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245})},{'topic':"my name is kali",'a':({'comment':"1st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"2st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"3st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"4st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245})},{'topic':"my name is rali",'a':({'comment':"1st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"2st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"3st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"4st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245})},{'topic':"my name is pali",'a':({'comment':"1st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"2st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"3st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245},{'comment':"4st comment",'reply':{'b':"hahahaha", "likes":3,"id":1234},"likes":4,'id':1245})})
    print ("hello")
    return (json.dumps(topic))


@app.route("/topicsloggedin", methods=['POST'])
def topicsloggedin():
    d=request.get_json(force=True)
    topic =sqlread().topicloggedin(d["userid"],0)
    print (tuple(topic))
    return (json.dumps(tuple(topic)))
    

@app.route("/liked",methods=['POST'])
def liked():
    data =request.get_json(force=True)
    print(data)
    sqlwrite().commentlikeinsert(data["commentid"], data["userid"])
    
    return True

@app.route("/forview",methods=['POST'])
def forview():
    data =request.get_json(force=True)
    print(data)
    sqlwrite().commentinsert(uuid.uuid4(),data["data"],data["userid"],data["topicid"],1)
   
    return "successfull for"



@app.route("/againstview",methods=['POST'])
def againstview():
    data =request.get_json(force=True)
    print(data)
    sqlwrite().commentinsert(uuid.uuid4(),data["data"],data["userid"],data["topicid"],0)
    
    return "successfull against"

@app.route("/topicasked",methods=['POST'])
def topicasked():
    data =request.get_json(force=True)
    sqlwrite().topicinsert(uuid.uuid4(),data["data"],data["userid"])
    print(data["userid"])
    return "successfull topic asked"


@app.route("/loadmoretopic",methods=['POST'])
def loadmoretopic():
    data =request.get_json(force=True)
    topic=sqlread().topicloggedin(data["userid"],data["offset"])
    print(data["offset"])
    return (json.dumps(tuple(topic)))

if __name__ == "__main__":
    app.run()
    
    
    
    
    
    
    
    
    
    
    
