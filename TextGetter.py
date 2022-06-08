
import requests
from bs4 import BeautifulSoup
import re
import enchant
from RandFunct import random_number
from RandFunct2 import random_number2

d = enchant.Dict("en_US")

def GetWebText():

    print("")

    print("Processing page.")

    print("")

    sites = ["https://www.theafricareport.com//202535//africa-can-studying-chinas-first-sez-give-insight-into-the-continents-economic-recovery//"]
    ln = len(sites)

    uch = random_number(ln)

    url = sites[uch]

    #infile = open("Drugsb.txt", "r")

    #xstr = ""

    #plist = infile.readline()
    #while plist:
        #qlist = plist.strip()
        #ystr = " " + qlist + " "
        #xstr += ystr
    ##plist = infile.readline()

    #infile.close()

    #xstr = requests.get(url).text

    #xstr = "Inspired by Band Aids Do They Know Its Christmas? project in the UK, American entertainer and social activist Harry Belafonte had the idea to organize the recording of a song including all the generations best-known music artists. He planned to have the proceeds donated to a new organization called United Support of Artists for Africa (USA for Africa). The non-profit foundation would then provide food and relief aid to starving people in Africa, specifically Ethiopia, where a 1983–1985 famine raged. The famine ultimately killed about one million people. Belafontes idea for an American version of Band Aids Do They Know Its Christmas? project in the UK Belafonte also planned to set aside money to help eliminate hunger in the United States of America. He contacted entertainment manager and fellow fundraiser Ken Kragen, who asked his clients Lionel Richie and Kenny Rogers to participate. Kragen and the two musicians agreed to help Belafonte, and in turn, enlisted the cooperation of Stevie Wonder, to add more name value to their project. Quincy Jones was drafted to co-produce the song, taking time out from his work on the film The Color Purple. Jones also telephoned Michael Jackson, who had released the commercially successful Thriller album in 1982, and just concluded a tour with his brothers.Jackson told Richie that he not only wanted to sing the song, but to help write it as well. The songwriting team originally included Wonder, but his time was constrained by his song-writing for the film The Woman in Red. So Jackson and Richie wrote We Are the World themselves at Hayvenhurst, the Jackson family home in Encino, California. They sought to write a song that would be easy to sing and memorable, yet still an anthem. For a week, the two spent every night working on lyrics and melodies in Jacksons bedroom. Jacksons older sister La Toya recounted the process in an interview with the U.S. celebrity news magazine People: Id go into the room while they were writing and it would be very quiet, which is odd, since Michaels usually very cheery when he works. It was very emotional for them. She also later said that Jackson wrote most of the lyrics but hes never felt it necessary to say that. Richie had recorded two melodies for We Are the World, which Jackson took, adding music and words to the song on the same day. Jackson said, I love working quickly. I went ahead without even Lionel knowing. I couldnt wait. I went in and came out the same night with the song completed: drums, piano, strings, and words to the chorus. Jackson then presented his demo to Richie and Jones, who were both shocked; they did not expect the pop star to see the structure of the song so quickly. The next meetings between Jackson and Richie were unfruitful; the pair produced no additional vocals and got no work done. It was not until the night of January 21, 1985, that Richie and Jackson completed the lyrics and melody of We Are the World within two and a half hours, one night before the songs first recording session."
   
    xstr = "Club drugs are a group of drugs commonly used by older adolescents and young adults to enhance dance parties like raves or going clubbing Club drug intoxication and side effects can be harmful or dangerous particularly when using different drugs together leading to injury or overdose and may even lead to long term consequences What club drugs are  Effects of club drugs Different types of club drugs. Risks associated with club and rave party drugs. How addictive club drugs are.Addiction treatment for club drugs. What Are Club Drugs? Club drugs are a group of drugs that are most often used by adolescents and young adults at dance parties, raves, bars, and clubs to help maintain energy levels for dancing, alter how they sense the environment around them, and reduce inhibitions. Stimulants. Depressants. Inhalants. Hallucinogens. Some of these drugs are relatively easy to access and inexpensive. Although they may be viewed as less harmful than other drugs, particularly those that are injected like heroin, cocaine, or methamphetamine, they can still be very dangerous. Club drugs often come in the form of pills, powders, or liquid found in small vials, which are taken orally.  common for these substances to be mixed or cut with other substances, or even be a completely different drug than what the user thinks which can increase the risks of using club drugs People often take club drugs together or combine them with alcohol, which can enhance their effects and raise the likelihood of overdose or experiencing other harmful unanticipated effects What Are the Effects of Club Drugs Club drugs can be unpredictable and may contain different ingredients than what a person thinks Their pharmacological psychological and physiological effects can vary widely Common effects of club drugs can include Altered sensory perception including seeing and hearing things that real or are distortions of reality. Impaired judgment Nausea and vomiting. Loss of muscle control Euphoria Dizziness Changes in energy level drowsiness or alertness Changes in blood pressure heart rate or body temperature  Aggressive behavior Loss of consciousness including coma However, everyone reacts differently and the specific effects that you feel depend on the person the substance taken substances they are combined with or ingredients that were added and the dose"

    ylst = xstr.split(' ')

    xlst = []

    remword = ['asbox', 'parser', 'saved', 'idplogo', 'logged', 'inlili', 'alilia', 'page', 'hosted', 'a', 'pdf', 'cache', 'key', 'IP', 'main', 'portal', 'address', 'liliia', 'classnew', 'idpviews', 'content', 'titleHOW', 'article', 'articles', 'revision', 'Wikipedia', 'version', 'vector-menu', 'vector-menu-portal', 'Commons', 'registered', 'trademark', 'media', 'pages', 'Serialized', 'timestamp', 'vector-user-menu-legacy', 'non-profit', 'report', 'links', 'files', 'terms', 'edited']

    for elemi in ylst:
        elemj = elemi.lower()
        elem = elemj.strip()
        try:
            if (d.check(elem)) and (elem not in remword) and  (len(elem) > 4) : 
          
                xlst.append(elem)
        except:
            print("Bad Char")

    print(xlst)

    return(xlst)

    
def GetWebTextSF():

    print("")

    print("Processing page.")

    print("")

    #sites = ['https://en.wikipedia.org/wiki/Science_Fiction', 'https://en.wikipedia.org/wiki/Mass_Effect']

    sites = ['https://en.wikipedia.org/wiki/Human_spaceflight']

    ln = len(sites)

    uch = random_number(ln)

    url = sites[uch]

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