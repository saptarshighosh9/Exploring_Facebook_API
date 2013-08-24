import sys
import urllib
import urllib2
import time
import datetime
import json
import webbrowser


ACCESS_URL = "https://graph.facebook.com/"

def collect_data():	
    k=0
    kolkata=0;
    others=0
    nu=0
    ot=0
    print "\n\n"
    print " #############################################_________________Facebook API information access System____________________#############################################"
    print "***********************************************************************************************************************************************************************"
    print "                                                                        Developed by Gooblu"
    webbrowser.open("https://www.facebook.com/dialog/oauth?"
                    "response_type=token&client_id=145634995501895&"
                    "redirect_uri=http://developers.facebook.com/tools/"
                    "explorer/callback&scope=user_birthday,user_friends,publish_actions"
                    ",read_stream")
    
    webbrowser.open("http://developers.facebook.com/tools/explorer")
    ACCESS_TOKEN = raw_input("\nEnter the TOKEN string obtained from API "
                           "explorer page: \n")
   
    print "\n\n\n"
    print "                                                           Downloading Users Information"
    print "------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
 
    male=0
    female=0
    s=0
    r=0
    m=0
    c=0
    e=0
    sp=0
    mm=0
    d=0
    ng=0
    o=0
    bh=0
    bhh=0
    while(k<100):  
        datafile = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(hometown)&access_token='+ACCESS_TOKEN)
        df=urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)             
        rs = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(relationship_status)&access_token='+ACCESS_TOKEN)        
        gender= urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(gender)&access_token='+ACCESS_TOKEN)   
        br = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(birthday)&access_token='+ACCESS_TOKEN)  
        us=urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(username)&access_token='+ACCESS_TOKEN)
        pt=""
        ut=""
        if 'gender' in json.loads(gender.read())['friends']['data'][k]:
           gender.close()
           gender= urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(gender)&access_token='+ACCESS_TOKEN)
           g=json.loads(gender.read())['friends']['data'][k]['gender']
           if g== "male":
              male+=1   
           elif g=="female":
              female+=1
           else:
              g=="NA"	    
           gender.close()
        if  'username' in json.loads(us.read())['friends']['data'][k]:
            us.close()
            us=urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(username)&access_token='+ACCESS_TOKEN)
            usr=json.loads(us.read())['friends']['data'][k]['username']	
            us.close()
        else:
            usr="NA"	
            us.close()
            	
        ut+="  %8s  ||"%(g)
        
        if  'birthday' in json.loads(br.read())['friends']['data'][k]:
               br.close()
               br = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(birthday)&access_token='+ACCESS_TOKEN)
               dt=json.loads(br.read())['friends']['data'][k]['birthday']
               br.close()
               bh+=1
        else:
               dt="NA"
               br.close()
               bhh+=1
               
        ut+="  %10s  ||"%(dt)       
        if  'relationship_status' in json.loads(rs.read())['friends']['data'][k]: 
               rs.close()
               rs = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(relationship_status)&access_token='+ACCESS_TOKEN)
               rss=json.loads(rs.read())['friends']['data'][k]['relationship_status']
            
               if rss=="Single":
                  s+=1
               elif rss=="In a relationship":
                  r+=1
               elif rss=="Married":
                  m+=1
               elif rss=="Engaged":
                  e+=1
               elif rss=="It's complicated":
                  c+=1
               elif rss=="Separated":
                  sp+=1
               elif rss=="In a domestic partnership":
                  d+=1
               elif rss=="In an open relationship":
                  o+=1    
               else:
                  mm+=1	
               rs.close()   
        else:	
               ng+=1 
               rss="NA"
               rs.close() 
        
        ut+="  %20s  ||"%(rss)
            
        if 'hometown' in json.loads(datafile.read())['friends']['data'][k]:
            	
            datafile.close()
            ud=json.loads(df.read())['friends']['data'][k]['name']
            df.close()
            df=urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)
            udd=json.loads(df.read())['friends']['data'][k]['id']
            df.close()
            datafile = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(hometown)&access_token='+ACCESS_TOKEN)
            bb=json.loads(datafile.read())['friends']['data'][k]['hometown']['name']
            datafile.close()
            datafile = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(hometown)&access_token='+ACCESS_TOKEN)
            bbb=json.loads(datafile.read())['friends']['data'][k]['hometown']['id']  
            
   
 
            
           
            if bbb=='105803266126801' or bbb=='108553765841012':
               kolkata+=1;	    
            else:
                others+=1;	    
            
            pt+= '  %25s  ||'%(ud) 
            pt+= '  %40s  ||'%(bb)
           
          
        else:
	
            df=urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)
            udd=json.loads(df.read())['friends']['data'][k]['id']
            df.close()	
            df=urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)
            ud=json.loads(df.read())['friends']['data'][k]['name']
            df.close()
             
            bbb="NA"
            bb="NA"
            
            pt+= '  %25s  ||'%(ud) 
            pt+= '  %40s  ||'%(bb)	
             
            datafile.close()
            nu+=1
          
          
          
          
        
        pt+="  %20s  ||"%(usr)   
        ut+="  || %s"%(k+1) 
        pt+=ut
        print pt     
        k=k+1
        
    print "\n" 
    print "***********************************************************Analyzing Data###### Results*******************************************************************************"
    print  'Number of friends with hometown Calcutta              : %15s'%(kolkata)
    print  'Home town outside kolkata                             : %15s'%(others)
    print  'Not updated their hometown in facebook                : %15s'%(nu)
    print "######################################################################################################################################################################"
    print  'male friends                                          : %15s'%(male)
    print  'female friends                                        : %15s'%(female)
    print  '#####################################################################################################################################################################'
    print  'Likes to get birthday wish on facebook                : %15s'%(bh)
    print  'Hides their birthday in facebook                      : %15s'%(bhh)
    print  '#####################################################################################################################################################################'
    print  'single                                                : %15s'%(s)
    print  'married                                               : %15s'%(m)
    print  'separated                                             : %15s'%(sp)
    print  'inrelationship                                        : %15s'%(r)
    print  'engaged                                               : %15s'%(e)
    print  'complicated                                           : %15s'%(c)
    print  'open relationship                                     : %15s'%(o)
    print  'domestic parternship                                  : %15s'%(d)
    print  'other                                                 : %15s'%(mm)
    print  'not given                                             : %15s'%(ng)
    #if u wish u can store this detail info in your local disk
    raw_input("\n \n Processing Complete.Data saved in your local disk.Press enter to exit")  
   
    
    
    
    
    
if __name__ == "__main__":
   collect_data()
