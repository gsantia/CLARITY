import json

POLITICAL = {'346937065399354' : 'Occupy Democrats',
             '153080620724' : 'Donald J. Trump',
             '354522044588660' : 'Upworthy',
             '146422995398181' : 'Addicting Info',
             '177486166274' : 'Being Liberal',
             '889307941125736' : 'Hillary Clinton',
             '6815841748' : 'Barack Obama',
             '21392801120' : 'Mitt Romney',
             '219367258105115' : 'CNN Politics',
             '62317591679' : 'Politico',
             '114517875225866' : 'The Other 98%',
             '135665053303678' : 'Eagle Rising',
             '423006854503882' : 'Milo Yiannopoulos',
             '242174545810040' : 'Paul Joseph Watson',
             '9124187907' : 'Bernie Sanders',
             '24718773587' : 'Sarah Palin',
             '210277954204' : 'The Young Turks',
             '56845382910' : 'Huffington Post Politics',
             '9269711759' : 'ARNOLD',
             '155244824599302' : 'Paul Ryan',
             '114546728587728' : 'George W. Bush',
             '108734602494994' : 'WikiLeaks',
             '65646572251' : 'Bill Clinton',
             '1617668278499178' : 'The British Monarchy',
             '105479482835768' : 'Goodluck Jonathan',
             '6934857868' : 'Mike Huckabee',
             '6233046685' : 'Ron Paul',
             '7746841478' : 'World Economic Forum',
             '20446254070' : 'Business Insider',
             '10643211755' : 'NPR',
             '8304333127' : 'The Wall Street Journal',
             '120745732681' : 'Ivanka Trump',
             '1209300825752745' : "America's Update",
             '532734866892797' : 'We Support Donald Trump',
             '1220332944702810' : 'President Donald J. Trump',
             '1191441824276882' : 'The White House',
             '44473416732' : 'Positively Republican',
             '123624513983' : 'The Western Journal',
             '519305544814653' : 'Conservative Tribune',
             '235203259169' : 'Herman Cain',
             '475549362567960' : 'Conservative Review',
             '713780065339341' : 'Karl Marx',

             





             }




NEWS = {'228735667216' : 'BBC News',
        '5550296508' : 'CNN News',
        '15704546335' : 'Fox News',
        '184096565021911' : 'ABC News Politics',
        '389658314427637' : 'Right Wing News',
        '80256732576' : 'InfoWars',
        '6499393458' : 'Alex Jones',
        '95475020353' : 'Breitbart',
        '5281959998' : 'New York Times',
        '18793419640' : 'CNN International',
        '10606591490' : 'TIME',
        '155869377766434' : 'NBC News',
        '6013004059' : 'The Economist',
        '10513336322' : 'The Guardian',
        '18468761129' : 'The Huffington Post',
        '326683984410' : 'RT',
        '131459315949' : 'CBS News',
        '114050161948682' : 'Reuters',
        '97212224368' : 'CNBC',
        '18343191100' : 'Newsweek',
        '206630642689393' : 'LGBT News',
        '184599864915751' : "Women's Rights News",
        '357990416180' : 'Sputnik',
        '188625661189259' : "People's Daily",
        '338109312883186' : 'China Xinhua News',
        '191347651290' : 'China Daily',
        '23230437118' : 'India Today',
        '151955124848859' : 'BBC India',
        '26781952138' : 'The Times of India',
        '101402598109' : 'Euronews English',
        '6622931938' : 'Channel 4 News',
        '114019975312443' : 'Global News',
        '13652355666' : 'USA Today',






        
        
        }

SCIENCE = {'23497828950' : 'National Geographic',
           '54971236771' : 'NASA',
           '6002238585' : 'Discovery',
           '118071565920' : 'The Weather Channel',
           '153278754738777' : 'Climate Reality',
           '46126453526' : 'Big Think',
           '96191425588' : 'Science',
           '48947135361' : 'Bill Nye the Science Guy',
           '7720276612' : 'Neil deGrasse Tyson',
           '265383883540505' : 'The Flat Earth Society',


            }

OTHER = {'19013582168' : 'PBS',
         '5644748986' : 'National Wildlife Federation',
         '216311481960' : 'Bill Gates',
         '22561081832' : 'NRA',
         '665345483483486' : 'NRA 2',
         '8934429638' : 'Planned Parenthood',
         '383306620200' : 'I Love Jesus Christ',
         '142821199170363' : 'Jesus Christ',
         '309798029121030' : 'Everytown for Gun Safety',
         '145170355529600' : 'National Pro-Life Alliance',
         '294468630182' : 'Noam Chomsky',
         '23237898444' : 'The High Times',
         '119530294738528' : 'Legalize Marijuana',
         '13204463437' : 'UNHCR, the UN Refugee Agency',
         '207918945891587' : 'United Nations Human Rights'
         }

if __name__ == '__main__':
    outlets = {}
    for item in POLITICAL:
        outlets[item] = POLITICAL[item]

    for outlet in NEWS:
        outlets[outlet] = NEWS[outlet]

    for science in SCIENCE:
        outlets[science] = SCIENCE[science]

    for other in OTHER:
        outlets[other] = OTHER[other]

    with open('../data/FB_PAGES.json', 'w') as f:
        json.dump(outlets, f, indent = 4, sort_keys = True)








