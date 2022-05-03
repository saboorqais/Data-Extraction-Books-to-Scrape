import requests
from bs4 import BeautifulSoup
def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def in_stock(title, topic):
  
    URL = "http://books.toscrape.com/"
    r = requests.get(URL)
    catalgoue=[]
    soup = BeautifulSoup(r.content) # If this line causes an error, run 'pip install html5lib' or install 
    topicListing=soup.findAll('ul',
                         attrs = {'class':''})

    topicListing=topicListing[0].findAll("li")
   
    for each in topicListing:
        url =each.a['href']
        name = each.a.text
        dictionary={
        }
        dictionary['url']="http://books.toscrape.com/"+url
        dictionary['name']=name.replace('\n','')
        catalgoue.append(dictionary)
    url=""
    
    for each in catalgoue:
   
      if str(topic).replace(" ","").lower() == (str(each['name']).strip("\n").replace(" ","").lower()):
        url=each['url']
     
    if len(url)==0:
        return False
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    found=[]
    
    try:
        current=soup.find('li',
                         attrs = {'class':'current'}).text
        check1=current.replace(" ","").strip("\n")[-2]
        total=0
        if (isinteger(check1)):
            check1=current.replace(" ","").strip("\n")[-1]
            check2=current.replace(" ","").strip("\n")[-2]
            s=check2+check1
            total(int(s))
        
        else:
            total=int(current.replace(" ","").strip("\n")[-1])
        y=0
        x=1
       
        while(y<=total):     
            url1=url.split("/")
            url1.pop()
            url1.append( "page-"+str(x)+".html")
        
            url1="/".join(url1)
            r = requests.get(url1)
            soup = BeautifulSoup(r.content)
            books=soup.find('ol',
                            attrs = {'class':'row'})
           
            for each in books.findAll("li"):    
                if(title.lower() in each.article.h3.a["title"].lower()):
                    found.append(True)
                    break
            y=y+1
            x=x+1
   
        
    except :
            r = requests.get(url)
            soup = BeautifulSoup(r.content)
            books=soup.find('ol',
                            attrs = {'class':'row'})
            
            for each in books.findAll("li"):  
                
                if(title.lower() == each.article.h3.a["title"].lower()):
                    found.append(True)
                    break
                
    
    
        
      
      
    if(len(found)==0):
        return False
    else:
        return True
print(in_stock("awkward","sequential art"))