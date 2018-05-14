import datetime, glob, json, re
from collections import defaultdict, Counter
import threads

################################################################################
# this is the main implementation of the FaceBot API, consisting of many
# functions for the user to use in their analysis of the data
# NOTE: we don't have user data any more, so I removed all that stuff
################################################################################

path = '../../data/'

with open(path + 'THREADS.json', 'r') as f:
    COMMENTS_BY_THREAD = json.load(f)

def badInput():
    """prints out bad input for wrong inputs"""
    print "bad input, try again"

def getThread(threadID):
    """returns a Thread object for the thread with ID _threadID_"""
    thread = None
    THREAD = COMMENTS_BY_THREAD.get(threadID, None)
    if THREAD:
        thread = threads.Thread(threadID, THREAD)
    #is this too confusing? with all the versions of "thread"
    return thread

def threadResponse(threadID, choice = "All"):
    """returns a list of response times for the thread with ID
    _threadID. allows for the usual choice of structure with
    _choice"""
    thread = getThread(threadID)
    if choice not in ["All", "Top", "Reply"]:
        badInput()
    else:
        return thread.responseTimes(choice)

def threadText(threadID, choice = "All"):
    """returns the a list of the text of thread with _threadID_.
    allows the user to choose top-level or replies only, using
    _choice_ = "All" or "Reply"""
    thread = getThread(threadID)
    if choice == "All":
        return thread.all_text
    elif choice == "Top":
        return thread.top_text
    elif choice == "Reply":
        return thread.reply_text
    else:
        badInput()

def threadTimes(threadID, choice = "All"):
    """returns a list of times of the comments on the thread,
    allows for choice of top-level or replies only as before"""
    thread = getThread(threadID)
    if choice == "All":
        return thread.all_times
    elif choice == "Top":
        return thread.top_times
    elif choice == "Reply":
        return thread.reply_times
    else:
        badInput()

def threadCommentTime(threadID, choice = "All"):
    """returns list of tuples of _threadID_ thread of
    messages with their times. allows for _choice_ of top
    and reply"""
    thread = getThread(threadID)
    if choice == "All":
        return thread.all_text_time
    elif choice == "Top":
        return thread.top_text_time
    elif choice == "Reply":
        return thread.reply_text_time
    else:
        badInput()

def cutThread(threadID, date_time):
    """allows the user to look at the contents of a thread from the
    start until the given _date_time_. this will be a datetime object,
    datetime(year, month, day, hour, minute, second, microsecond, timezone).
    just returns the slice of the thread as a new Thread object,
    which the user can then apply functions to"""
    THREAD = COMMENTS_BY_THREAD[threadID]
    CUT_THREAD = [] #only want comments before date_time
    for comment in THREAD:
        formatted = threads.Thread.getTime(comment['time'])
        if formatted <= date_time:
            CUT_THREAD.append(comment)
    #now we have the top level comments from t=0 to _datetime_,
    #but we still need to chop off the replies that were made after _datetime_
    for com in CUT_THREAD:
        new_replies = []    #only want the replies up till _datetime_
        if com['replies']:
            for reply in com['replies']:
                form_reply = threads.Thread.getTime(reply['time'])
                if form_reply <= date_time:
                    new_replies.append(reply)
            com['replies'] = new_replies
    thread = threads.Thread(threadID, CUT_THREAD)
    return thread





