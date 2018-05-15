import datetime, glob, json, re
from collections import defaultdict, Counter
import threads

################################################################################
# this is the main implementation of the FaceBot API, consisting of many
# functions for the user to use in their analysis of the data
#
# NOTE: we don't have user data any more, so I removed all that stuff,
# along with the various levels of data (top/reply)
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

def threadResponse(threadID):
    """returns a list of response times for the thread with ID
    _threadID. allows for the usual choice of structure with
    _choice"""
    thread = getThread(threadID)
    return thread.responseTimes()

def threadText(threadID):
    """returns the a list of the text of thread with _threadID_."""
    thread = getThread(threadID)
    return thread.all_text

def threadTimes(threadID):
    """returns a list of times of the comments on the thread"""
    thread = getThread(threadID)
    return thread.all_times

def threadCommentTime(threadID):
    """returns list of tuples of _threadID_ thread of
    messages with their times."""
    thread = getThread(threadID)
    return thread.all_text_time

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
    thread = threads.Thread(threadID, CUT_THREAD)
    return thread





