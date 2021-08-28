
import requests
from bs4 import BeautifulSoup
import re
import enchant

d = enchant.Dict("en_US")

def GetWebText():

    print("")

    print("Processing page.")

    print("")

    url = 'https://en.wikipedia.org/wiki/Portal:Technology'

    xstr = requests.get(url).text

    ylst = xstr.split(' ')

    xlst = []

    remword = ['asbox', 'parser', 'saved', 'idplogo', 'logged', 'inlili', 'alilia', 'page', 'hosted', 'a', 'pdf', 'cache', 'key', 'IP', 'main', 'portal', 'address', 'liliia', 'classnew', 'idpviews', 'content', 'titleHOW', 'article', 'articles', 'revision', 'Wikipedia', 'version', 'vector-menu', 'vector-menu-portal', 'Commons', 'registered', 'trademark', 'media', 'pages', 'Serialized', 'timestamp', 'vector-user-menu-legacy', 'non-profit', 'report', 'links', 'files', 'terms', 'edited']

    for elemi in ylst:
        elemj = elemi.lower()
        elem = elemj.strip()
        try:
            if (d.check(elem)) and (elem not in remword) and (not elem.isnumeric()) and (len(elem) > 4) and (elem not in xlst): 
                xlst.append(elem)
        except:
            print("Bad Char")

    print(xlst)

    return(xlst)