import datetime, json
from collections import Counter, defaultdict

###########################################################################
# Allows for the API user to examine a single Thread in the data set and look
# at various features such as the comments, the users involved, the times of
# the comments, etc
###########################################################################

#NOTE: Had to remove all references to users and also top/reply structure, since
# we don't have any of that in CLARITY data.

class Thread(object):
    """this will hold the data we'd like for a single thread,
    such as the comments, the times they were made, the users etc.
    not sure about the methods yet."""

    def __init__(self, threadID, THREAD):
        """threadID is the Facebook ID of the thread, and THREAD is a
        list containing all comment JSONs for it."""

        self.THREAD = THREAD
        self.threadID = threadID
        #the time of the original FB post sparking the comment thread
        self.post_time = self.getPostTime()
        #list of the total text of the comments made
        self.all_text = []
        #list of the times of the comments, in datetime format
        self.all_times = []
        #list of comment/time tuples
        self.all_text_time = []

        #fill out the parameters with _getStructure_
        self._getStructure()

    def _getStructure(self):
        """setup the top-level and reply parameters"""
        for comment in self.THREAD:
            message = comment['message']
            time = Thread.getTime(comment['time'])
            #adjust all parameters
            self.all_text_time.append((message, time))

        if self.all_text_time:  #can't unpack null
            self.all_text, self.all_times = zip(*self.all_text_time)

    def getPostTime(self):
        """gets the post time of the thread and returns it in datetime form"""
        path = '../../data/POST_TIMES.json'
        with open(path, 'r') as f:
            POST_TIMES = json.load(f)
        post_time = POST_TIMES.get(self.threadID, None)
        if not post_time:
            return None
        return Thread.getTime(post_time)

    def responseTimes(self):
        """returns a list of time taken from the previous comment till the
        current comment."""
        response_times = [comment['response'] for comment in self.THREAD]
        return response_times

    @staticmethod
    def getTime(time):
        """produce a datetime object from a time string"""
        formatted = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S+0000")
        return formatted

