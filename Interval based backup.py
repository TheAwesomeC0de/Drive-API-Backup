from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from apiclient.http import MediaFileUpload
import mimetypes
import time

def Repeat():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    parent= ['1ycfRqVRu7dzhJ31WQue9XEPqlO8GUTT-']
    folder=os.listdir(os.getcwd())
    
    obj1=service.files().list(q="'1ycfRqVRu7dzhJ31WQue9XEPqlO8GUTT-' in parents and trashed != True").execute().get('files',[])

    dest=[0,0]
    dest[0]=[i['name'] for i in obj1]
    dest[1]=[i['id'] for i in obj1]
    f_id=0
    for i in range(len(folder)):
        mime=mimetypes.guess_type(folder[i])
        if str(mime)=="(None, None)":
            print(folder[i],"not possible")
            continue
        #print(mime)
        if folder[i] in dest[0]:
            file_metadata = {
            'name': folder[i],          
            }
            file_Id=''
            for k in range(len(dest[0])):
                if dest[0][k]==folder[i]:
                    file_Id=dest[1][k]
            media = MediaFileUpload(folder[i], mimetype=mime[0],resumable=True)
            file = service.files().update(
                fileId=file_Id,body=file_metadata,
                media_body=media,fields='id').execute()
            print ('File ID:',file.get('id'))
        else:  
            file_metadata = {
            'name': folder[i],
            'parents': parent           
                        }
            media = MediaFileUpload(folder[i], mimetype=mime[0],resumable=True)
            file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
            print ('File ID:',file.get('id'))
    log = open('log.txt','a')
    tt=time.localtime(time.time())
    log.write(str(tt.tm_mday)+'/'+str(tt.tm_mon)+'/'+str(tt.tm_year)+" " +str(tt.tm_hour)
              + ':'+ str(tt.tm_min)+':'+str(tt.tm_sec)+" backup successful "+os.getcwd()+"\n")
    log.close()def Repeat():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    parent= ['1ycfRqVRu7dzhJ31WQue9XEPqlO8GUTT-']
    folder=os.listdir(os.getcwd())
    mimefol=[]
    for i in range(len(folder)):
        mimefol.append(mimetypes.guess_type(folder[i]))
    obj1=service.files().list(q="'1ycfRqVRu7dzhJ31WQue9XEPqlO8GUTT-' in parents and trashed != True").execute().get('files',[])

    dest=[0,0]
    dest[0]=[i['name'] for i in obj1]
    dest[1]=[i['id'] for i in obj1]
    f_id=0
    for i in range(len(folder)):
        mime=mimetypes.guess_type(folder[i])
        if str(mime)=="(None, None)":
            print(folder[i],"not possible")
            continue
        #print(mime)
        if folder[i] in dest[0]:
            file_metadata = {
            'name': folder[i],          
            }
            file_Id=''
            for k in range(len(dest[0])):
                if dest[0][k]==folder[i]:
                    file_Id=dest[1][k]
            media = MediaFileUpload(folder[i], mimetype=mime[0],resumable=True)
            file = service.files().update(
                fileId=file_Id,body=file_metadata,
                media_body=media,fields='id').execute()
            print ('File ID:',file.get('id'))
        else:  
            file_metadata = {
            'name': folder[i],
            'parents': parent           
                        }
            media = MediaFileUpload(folder[i], mimetype=mime[0],resumable=True)
            file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()
            print ('File ID:',file.get('id'))
    log = open('log.txt','a')
    tt=time.localtime(time.time())
    log.write(str(tt.tm_mday)+'/'+str(tt.tm_mon)+'/'+str(tt.tm_year)+" " +str(tt.tm_hour)
              + ':'+ str(tt.tm_min)+':'+str(tt.tm_sec)+" backup successful "+os.getcwd()+"\n")
    log.close()

if __name__ =="__main__":
    delay=float(input("delay in hrs (accepts float values)"))
    while(True):
        try:
            Repeat()
        except :
            log = open('log.txt','a')
            tt=time.localtime(time.time())
            log.write(str(tt.tm_mday)+'/'+str(tt.tm_mon)+'/'+str(tt.tm_year)+" "+ str(tt.tm_hour)
                      + ':'+ str(tt.tm_min)+':'+str(tt.tm_sec)+"  backup failed "+ sys.exc_info[0]+"/n")
            log.close()
        time.sleep(int(60*60*delay))
