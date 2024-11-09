# --------------------------------------------------------------------------------------------------------------------------------------- #
# This version of the work is licensed under the Github Restrictive License v1.2                                                          #
# You can read the text of the license here: https://github.com/hikeri/Ripify/blob/main/LICENSE.md                                        #
# The license allows you to use the work only:                                                                                            #
# Download and use the Work only in its original form as it is, without modification or redistribution, for non-commercial purposes only. #
# Please, use codeberg version instead: https://codeberg.org/hikeri/Ripify                                                                #
# --------------------------------------------------------------------------------------------------------------------------------------- #
from flask import Flask ,request ,send_file ,render_template ,after_this_request #line:1
import os #line:2
import re #line:3
import subprocess #line:4
import threading #line:5
import hashlib #line:6
import datetime #line:7
app =Flask (__name__ )#line:9
DOWNLOAD_PATH ='downloads'#line:11
os .makedirs (DOWNLOAD_PATH ,exist_ok =True )#line:13
file_map ={}#line:15
file_lock =threading .Lock ()#line:16
@app .route ('/')#line:18
def index ():#line:19
    return render_template ('index.html')#line:20
def generate_hash (O00OO0O00O000OOOO ):#line:22
    O0OOO00000O00O00O =datetime .datetime .now ().strftime ("%Y-%m-%d")#line:23
    O0OO00OO0OO00000O =f"{O00OO0O00O000OOOO}{O0OOO00000O00O00O}".encode ('utf-8')#line:24
    return hashlib .sha256 (O0OO00OO0OO00000O ).hexdigest ()#line:25
@app .route ('/download',methods =['POST'])#line:27
def download ():#line:28
    OO00O00OO00O0O0O0 =request .form ['user_input']#line:29
    OO0000OO0O000O0OO =request .form ['hash']#line:30
    O0O0O0000OO00OO00 =generate_hash (OO00O00OO00O0O0O0 )#line:32
    if OO0000OO0O000O0OO !=O0O0O0000OO00OO00 :#line:34
        return "Invalid request.",403 #line:35
    if re .search (r'\b(?:curl|wget|python|bash|sh|node|php|ruby|perl|java|go)\b',OO00O00OO00O0O0O0 ,re .IGNORECASE ):#line:37
        return "Invalid input. Please enter a valid command.",400 #line:38
    OOOOO0O000OO00OO0 =os .path .join (DOWNLOAD_PATH ,'downloaded_music')#line:40
    try :#line:42
        subprocess .run (['python3','orpheus.py',OO00O00OO00O0O0O0 ,'-o',OOOOO0O000OO00OO0 ],check =True )#line:43
        OO00OOOOO000O0000 =os .listdir (OOOOO0O000OO00OO0 )#line:45
        O0000O00O00O0OOO0 =max ([os .path .join (OOOOO0O000OO00OO0 ,O0OO0OO00O00OO000 )for O0OO0OO00O00OO000 in OO00OOOOO000O0000 ],key =os .path .getctime )#line:46
        with file_lock :#line:48
            file_map [O0000O00O00O0OOO0 ]=threading .current_thread ().name #line:49
        O00OO00O0OOOOO0O0 =send_file (O0000O00O00O0OOO0 ,as_attachment =True )#line:51
        @after_this_request #line:53
        def O0O000000OOO00000 (OO0O0OOOOO000OOOO ):#line:54
            with file_lock :#line:55
                if O0000O00O00O0OOO0 in file_map :#line:56
                    del file_map [O0000O00O00O0OOO0 ]#line:57
                    try :#line:58
                        os .remove (O0000O00O00O0OOO0 )#line:59
                    except Exception as OO00OO0O0OOO0OOO0 :#line:60
                        print (f'Error removing file {O0000O00O00O0OOO0}: {OO00OO0O0OOO0OOO0}')#line:61
            return OO0O0OOOOO000OOOO #line:62
        return O00OO00O0OOOOO0O0 #line:64
    except Exception :#line:65
        return "An error occurred while processing your request.",500 #line:66
if __name__ =='__main__':#line:68
    app .run (host ="0.0.0.0")
# --------------------------------------------------------------------------------------------------------------------------------------- #
# This version of the work is licensed under the Github Restrictive License v1.2                                                          #
# You can read the text of the license here: https://github.com/hikeri/Ripify/blob/main/LICENSE.md                                        #
# The license allows you to use the work only:                                                                                            #
# Download and use the Work only in its original form as it is, without modification or redistribution, for non-commercial purposes only. #
# Please, use codeberg version instead: https://codeberg.org/hikeri/Ripify                                                                #
# --------------------------------------------------------------------------------------------------------------------------------------- #
