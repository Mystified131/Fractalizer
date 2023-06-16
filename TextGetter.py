
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

    #sites = ["https://www.theafricareport.com//202535//africa-can-studying-chinas-first-sez-give-insight-into-the-continents-economic-recovery//"]
    #ln = len(sites)

    #uch = random_number(ln)

    #url = sites[uch]

   # ylist = []

    infile = open("C:\\Users\\mysti\\Desktop\\Sage.txt", "r")

    xstr = ""

    plist = infile.readline()
    while plist:
        qlist = plist.strip()
        ystr = " " + qlist + " "
        y1str = ystr.replace('.', '')
        y2str = y1str.replace(',', '')
        y3str = y2str.replace("'", '')
        xstr += y3str
        plist = infile.readline()

    #infile.close()

    #xstr = requests.get(url).text

    #xstr = "Inspired by Band Aids Do They Know Its Christmas? project in the UK, American entertainer and social activist Harry Belafonte had the idea to organize the recording of a song including all the generations best-known music artists. He planned to have the proceeds donated to a new organization called United Support of Artists for Africa (USA for Africa). The non-profit foundation would then provide food and relief aid to starving people in Africa, specifically Ethiopia, where a 1983–1985 famine raged. The famine ultimately killed about one million people. Belafontes idea for an American version of Band Aids Do They Know Its Christmas? project in the UK Belafonte also planned to set aside money to help eliminate hunger in the United States of America. He contacted entertainment manager and fellow fundraiser Ken Kragen, who asked his clients Lionel Richie and Kenny Rogers to participate. Kragen and the two musicians agreed to help Belafonte, and in turn, enlisted the cooperation of Stevie Wonder, to add more name value to their project. Quincy Jones was drafted to co-produce the song, taking time out from his work on the film The Color Purple. Jones also telephoned Michael Jackson, who had released the commercially successful Thriller album in 1982, and just concluded a tour with his brothers.Jackson told Richie that he not only wanted to sing the song, but to help write it as well. The songwriting team originally included Wonder, but his time was constrained by his song-writing for the film The Woman in Red. So Jackson and Richie wrote We Are the World themselves at Hayvenhurst, the Jackson family home in Encino, California. They sought to write a song that would be easy to sing and memorable, yet still an anthem. For a week, the two spent every night working on lyrics and melodies in Jacksons bedroom. Jacksons older sister La Toya recounted the process in an interview with the U.S. celebrity news magazine People: Id go into the room while they were writing and it would be very quiet, which is odd, since Michaels usually very cheery when he works. It was very emotional for them. She also later said that Jackson wrote most of the lyrics but hes never felt it necessary to say that. Richie had recorded two melodies for We Are the World, which Jackson took, adding music and words to the song on the same day. Jackson said, I love working quickly. I went ahead without even Lionel knowing. I couldnt wait. I went in and came out the same night with the song completed: drums, piano, strings, and words to the chorus. Jackson then presented his demo to Richie and Jones, who were both shocked; they did not expect the pop star to see the structure of the song so quickly. The next meetings between Jackson and Richie were unfruitful; the pair produced no additional vocals and got no work done. It was not until the night of January 21, 1985, that Richie and Jackson completed the lyrics and melody of We Are the World within two and a half hours, one night before the songs first recording session."
   
    #xstr = "Club drugs are a group of drugs commonly used by older adolescents and young adults to enhance dance parties like raves or going clubbing Club drug intoxication and side effects can be harmful or dangerous particularly when using different drugs together leading to injury or overdose and may even lead to long term consequences What club drugs are  Effects of club drugs Different types of club drugs. Risks associated with club and rave party drugs. How addictive club drugs are.Addiction treatment for club drugs. What Are Club Drugs? Club drugs are a group of drugs that are most often used by adolescents and young adults at dance parties, raves, bars, and clubs to help maintain energy levels for dancing, alter how they sense the environment around them, and reduce inhibitions. Stimulants. Depressants. Inhalants. Hallucinogens. Some of these drugs are relatively easy to access and inexpensive. Although they may be viewed as less harmful than other drugs, particularly those that are injected like heroin, cocaine, or methamphetamine, they can still be very dangerous. Club drugs often come in the form of pills, powders, or liquid found in small vials, which are taken orally.  common for these substances to be mixed or cut with other substances, or even be a completely different drug than what the user thinks which can increase the risks of using club drugs People often take club drugs together or combine them with alcohol, which can enhance their effects and raise the likelihood of overdose or experiencing other harmful unanticipated effects What Are the Effects of Club Drugs Club drugs can be unpredictable and may contain different ingredients than what a person thinks Their pharmacological psychological and physiological effects can vary widely Common effects of club drugs can include Altered sensory perception including seeing and hearing things that real or are distortions of reality. Impaired judgment Nausea and vomiting. Loss of muscle control Euphoria Dizziness Changes in energy level drowsiness or alertness Changes in blood pressure heart rate or body temperature  Aggressive behavior Loss of consciousness including coma However, everyone reacts differently and the specific effects that you feel depend on the person the substance taken substances they are combined with or ingredients that were added and the dose"

    #xstr = "Compositions that could be considered a precedent for aleatory composition date back to at least the late 15th century, with the genre of the catholicon, exemplified by the Missa cuiusvis toni of Johannes Ockeghem. A later genre was the Musikalisches Würfelspiel or musical dice game, popular in the late 18th and early 19th century. (One such dice game is attributed to Wolfgang Amadeus Mozart.) These games consisted of a sequence of musical measures, for which each measure had several possible versions and a procedure for selecting the precise sequence based on the throwing of a number of dice. The French artist Marcel Duchamp composed two pieces between 1913 and 1915 based on chance operations. One of these, Erratum Musical written with Duchamps sisters Yvonne and Magdeleine for three voices, was first performed at the Manifestation of Dada on marche 27th 1920 and was eventually published in 1934. Two of his contemporaries, Francis Picabia and Georges Ribemont-Dessaignes, also experimented with chance composition,[clarification needed] these works being performed at a Festival Dada staged at the Salle Gaveau concert hall, Paris, on 26 May 1920. American composer John Cages Music of Changes (1951) was the first composition to be largely determined by random procedures, though his indeterminacy is of a different order from Meyer-Epplers concept. Cage later asked Duchamp: How is it that you used chance operations when I was just being born?.The earliest significant use of aleatory features is found in many of the compositions of American Charles Ives in the early 20th century. Henry Cowell adopted Ivess ideas during the 1930s, in such works as the Mosaic Quartet (String Quartet No. 3, 1934), which allows the players to arrange the fragments of music in a number of different possible sequences. Cowell also used specially devised notations to introduce variability into the performance of a work, sometimes instructing the performers to improvise a short passage or play ad libitum. Later American composers, such as Alan Hovhaness (beginning with his Lousadzak of 1944) used procedures superficially similar to Cowells, in which different short patterns with specified pitches and rhythm are assigned to several parts, with instructions that they be performed repeatedly at their own speed without coordination with the rest of the ensemble. Some scholars regard the resultant blur as hardly aleatory, since exact pitches are carefully controlled and any two performances will be substantially the same although, according to another writer, this technique is essentially the same as that later used by Witold Lutosławski.Depending on the vehemence of the technique, Hovhanesss published scores annotate these sections variously, for example as Free tempo / humming effectand Repeat and repeat ad lib, but not together. In Europe, following the introduction of the expression aleatory music by Meyer-Eppler, the French composer Pierre Boulez was largely responsible for popularizing the term. Other early European examples of aleatory music include Klavierstück XI (1956) by Karlheinz Stockhausen, which features 19 elements to be performed in a sequence to be determined in each case by the performer.A form of limited aleatory was used by Witold Lutosławski (beginning with Jeux Vénitiens in 1960–61), where extensive passages of pitches and rhythms are fully specified, but the rhythmic coordination of parts within the ensemble is subject to an element of chance. There has been much confusion of the terms aleatory and indeterminate/chance music. One of Cages pieces, HPSCHD, itself composed using chance procedures, uses music from Mozarts Musikalisches Würfelspiel, referred to above, as well as original music."
 
    #xstr ="Early pop remixes were fairly simple; in the 1980s, extended mixes of songs were released to clubs and commercial outlets on vinyl 12-inch singles. These typically had a duration of six to seven minutes, and often consisted of the original song with 8 or 16 bars of instruments inserted, often after the second chorus; some were as simplistic as two copies of the song stitched end to end. As the cost and availability of new technologies allowed, many of the bands who were involved in their own production (such as Yellow Magic Orchestra, Depeche Mode, New Order, Erasure, and Duran Duran) experimented with more intricate versions of the extended mix. Madonna began her career writing music for dance clubs and used remixes extensively to propel her career; one of her early boyfriends was noted DJ John Jellybean Benitez, who created several mixes of her work. Art of Noise took the remix styles to an extreme—creating music entirely of samples. They were among the first popular groups to truly harness the potential that had been unleashed by the synthesizer-based compositions of electronic musicians such as Kraftwerk, Yellow Magic Orchestra, Giorgio Moroder, and Jean Michel Jarre. Contemporaneous to Art of Noise was the seminal body of work by Yello (composed, arranged and mixed by Boris Blank). Primarily because they featured sampled and synthesized sounds, Yello and Art of Noise would produce a great deal of influential work for the next phase. Others such as Cabaret Voltaire and the aforementioned Jarre (whose Zoolook was an epic usage of sampling and sequencing) were equally influential in this era. After the rise of dance music in the late 1980s, a new form of remix was popularised, where the vocals would be kept and the instruments would be replaced, often with matching backing in the house music idiom. Jesse Saunders, known as The Originator of House Music, was the first producer to change the art of remixing by creating his own original music, entirely replacing the earlier track, then mixing back in the artists original lyrics to make his remix. He introduced this technique for the first time with the Club Nouveau song Its a Cold, Cold World, in May 1988. Another clear example of this approach is Roberta Flacks 1989 ballad Uh-Uh Ooh-Ooh Look Out (Here It Comes), which Chicago House great Steve Silk Hurley dramatically reworked into a boisterous floor-filler by stripping away all the instrumental tracks and substituting a minimalist, sequenced track to underpin her vocal delivery, remixed for the UK release which reached No1 pop by Simon Harris. The art of the remix gradually evolved, and soon more avant-garde artists such as Aphex Twin were creating more experimental remixes of songs (relying on the groundwork of Cabaret Voltaire and the others), which varied radically from their original sound and were not guided by pragmatic considerations such as sales or danceability, but were created for arts sake. In the 1990s, with the rise of powerful home computers with audio capabilities came the mash-up, an unsolicited, unofficial (and often legally dubious) remix created by underground remixers who edit two or more recordings (often of wildly different songs) together. Girl Talk is perhaps the most famous of this movement, creating albums using sounds entirely from other music and cutting it into his own. Underground mixing is more difficult than the typical official remix because clean copies of separated tracks such as vocals or individual instruments are usually not available to the public. Some artists (such as Björk, Nine Inch Nails, and Public Enemy) embraced this trend and outspokenly sanctioned fan remixing of their work; there was once a web site which hosted hundreds of unofficial remixes of Björks songs, all made using only various officially sanctioned mixes. Other artists, such as Erasure, have included remix software in their officially released singles, enabling almost infinite permutations of remixes by users. The band has also presided over remix competitions for their releases, selecting their favourite fan-created remix to appear on later official releases. Remixing has become prevalent in heavily synthesized electronic and experimental music circles. Many of the people who create cutting-edge music in such genres as synthpop and aggrotech are solo artists or pairs. They will often use remixers to help them with skills or equipment that they do not have. Artists such as Chicago-based Delobbo, Dallas-based LehtMoJoe, and Russian DJ Ram, who has worked with tAtu, are sought out for their remixing skill and have impressive lists of contributions. It is not uncommon for industrial bands to release albums that have remixes as half of the songs. Indeed, there have been popular singles that have been expanded to an entire album of remixes by other well-known artists.Some industrial groups allow, and often encourage, their fans to remix their music, notably Nine Inch Nails, whose website contains a list of downloadable songs that can be remixed using Apples GarageBand software. Some artists have started releasing their songs in the U-MYX format, which allows buyers to mix songs and share them on the U-MYX website. Some radio stations, such as the UKs Frisk Radio. make extensive use of Remixes in their formats to create a hotter, more up-beat sound than their market rivals."

    #xstr = "Occupancy can also refer to the number of units in use, such as hotel rooms, apartment flats, or offices. When a motel is at full occupancy, it is common practice to turn on a NO VACANCY neon sign. Completely vacant buildings can also attract crime. A 2017 study found that demolishing vacant buildings reduce crime by about 8 percent on the block group in question and 5 percent on nearby block groups. Occupancy can also refer to the number of persons using an undivided space, such as a meeting room, ballroom, auditorium, or stadium. As with building codes, fire protection authorities often set a limit on the number of people that can occupy a space at one time. These limits are established primarily to allow all occupants safe passage through exits, but can also be employed to preserve the integrity of a structure. An occupancy sensor is a device that can tell if someone is in a room, and is often used in home automation and security systems. These are typically more advanced than motion sensors, which can only detect motion."

    #xstr = 'To determine the prevalence and correlates of DSM5 intermittent explosive disorder and related aggressive disorders in the United States.Community survey data from the National Comorbidity SurveyReplication and Adolescent Supplementinvolving 10,148 adolescents and 9,282 adults, respectively, were reanalyzed with recurrent aggressive behavior defined as 3 serious aggressive outbursts in any given year. In addition to prevalence, assessments of aggression severity, property damage, injury to others, intimate partner assault, utilization of guns and weapons to threaten, and treatment utilization for recurrent aggressive behavior were also assessed. About 17% of adolescents and 8% of adults report a pattern of recurrent aggressive outbursts within at least 1 year. Such individuals are much more aggressive and impulsive than nonaggressive controls and are more likely to engage in intimate partner assault, carry and use guns and other weapons to threaten others, and be arrested by law enforcement. Few aggressive individuals speak with health care providers about this behavior, and fewer receive treatment for aggression. Recurrent aggressive behavior is common in both adolescents and adults, with clinically significant consequences to those with this pattern and to others in their environment ie, using guns and other weapons to threaten others. While this type of behavior can be reduced though pharmacologic psychosocial treatment intervention, the vast majority of aggressive individuals do not engage in treatment for their aggressive behavior. Screening individuals for such behavior in ones practice may do much toward identifying this problem and bringing such individuals into treatment.'

    #xstr = 'I like electronic music because it can be very creative in compostion, or very simple, and contains interesting sounds. I listen to trance a lot, but electronic trance is too complex to understand. When I am in a trance state, I can not tell how the song is composed. If I were to listen I would not know. In electronic dance music, the composition is almost always laid out, so it is not as clear as a melody. The electronic sounds are often very interesting, sometimes beautiful. (I prefer trance because I have to do a little dance in order to get into trance.) That is why I like trance. It is easy to compose, it is so fun to make, most trance songs are quite simple and catchy. Trance is fun when you can control the feeling, you feel the music move, not the other way around. For example, if you are in trance you might want to feel all the cool sounds coming out of your ears, then the next song you hear might be a really fast paced song that is like a quick song in your head. Or you could be in the trance and the bass line sounds cool. Another example would be if I was in Trance and I heard a fast beat, like that same beat you listen too in dancefloors.'

    #xstr = 'LibriVox recording of Manchester Poetry by James Wheeler Read in English by Phil Benson Manchesters first published anthology of locally-written poetry was compiled by editor James Wheeler to show that Manchester the most mechanical of boroughs had more to offer than spinning jennies and power looms The collection includes selections from ten Manchester-born poets among whom Charles Swain was the best known Summary by Phil Benson'

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