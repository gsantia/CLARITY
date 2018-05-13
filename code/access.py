
#!/usr/bin/python

import urllib2
import json, time
import os, re, csv


def createPostUrl(POST_ID, ACCESS_TOKEN = ACCESS_TOKEN):
    """create the URL needed to access the JSON describing a single Posts' metadata"""
    post_args = "?access_token=" + ACCESS_TOKEN + \
                    "&fields=link,message,created_time,name,story,caption,description,picture,place,shares,source,updated_time"
    post_url = "https://graph.facebook.com/" + POST_ID + post_args
    return post_url

def createPageUrl(PAGE_ID, ACCESS_TOKEN = ACCESS_TOKEN):
    """create the URL needed to obtain a JSON describing the most recent Posts made on a 
    Page"""
    page_url = "https://graph.facebook.com/" + PAGE_ID + "/posts?limit=100&access_token=" + ACCESS_TOKEN
    return page_url

def createPostCommentsUrl(POST_ID, ACCESS_TOKEN = ACCESS_TOKEN):
    """create the URL needed to access the JSON detailing the comments of a single Post"""
    comments_args = "/comments?access_token=" + ACCESS_TOKEN + \
                    "&order=chronological&limit=1000"
    comments_url = "https://graph.facebook.com/" + POST_ID + comments_args
    return comments_url

def getPage(PAGE_ID, ACCESS_TOKEN = ACCESS_TOKEN):
    """return the JSON of the list of recent posts made by the page in question"""
    page_url = createPageUrl(PAGE_ID, ACCESS_TOKEN)
    web_response = urllib2.urlopen(page_url)
    readable_page = web_response.read()
    return json.loads(readable_page)

def getPost(POST_ID, ACCESS_TOKEN = ACCESS_TOKEN):
    """return the JSON of a specific post"""
    post_url = createPostUrl(POST_ID, ACCESS_TOKEN)
    web_response = urllib2.urlopen(post_url)
    readable_page = web_response.read()
    return json.loads(readable_page)

def getPostComments(POST_ID):
    """returns a JSON of a post's comments"""
    data = []
    post_url = createPostCommentsUrl(POST_ID)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib2.install_opener(opener)
    batchnum = 1

    try:
        web_response = urllib2.urlopen(post_url)
        readable_page = web_response.read()
        thisdata = json.loads(readable_page)
        data.extend(thisdata['data'])
    except:
        print "comments didn't work at all!"
        #in this case, just return an empty dict
        return {}
    
    time.sleep(1)

    if 'paging' in thisdata.keys():
        while thisdata['paging'].get('next', False):
            batchnum += 1
            print "comments batch: ", batchnum
            try:
                web_response = urllib2.urlopen(thisdata['paging']['next'])
                thisdata = json.loads(web_response.read())
                if thisdata['data']:
                    data.extend(thisdata['data'])
            except:
                print "problem getting extra batches"
            time.sleep(1)

    return {'data' : data}

def collectPage(PAGE_ID):
    """given PAGE_ID, first gets the most recent Posts made by the Page. then
    loops through these Posts and creates posts.json and comments.json files for
    each, in appropriate directories"""
    posts = getPage(PAGE_ID)['data']    #this is a list of the posts
    time.sleep(1)
    # Now go through each post and scrape the comments
    for post in posts:
        try:
            yolo = getPostComments(post['id'])
        except:
            print time.time()

def mock_scrape():
    """
    I want to see how long scraping all 100 outlets might take. This function
    will perform it, without storing anything. At the end it'll dump a file
    which just says how many seconds it took.
    """

    with open('FB_PAGES.json', 'r') as f:
        PAGES = json.load(f)

    start = time.time()
    for page in PAGES:
        collectPage(page)

    end = time.time()
    elapsed = end - start

    with open('TIME.json', 'w') as f:
        json.dump({'time' : elapsed}, f)






