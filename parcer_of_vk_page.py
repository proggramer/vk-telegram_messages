#We need only user_name from Vk_page
import httplib2 #for download of Vk_page
from bs4 import BeautifulSoup #parser

def get_user_name(user_id)

    user_link = 'https://vk.com/id' + str(user_id)

    h = httplib2.Http(".cache")
    response, content = h.request(user_link) #request page of our user_id


    soup = BeautifulSoup(content, "html5lib") #parser begins work

    return soup.find('title').string  #because <title>user_name</title>
