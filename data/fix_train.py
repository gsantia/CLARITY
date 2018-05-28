import json

def main():
    """
    This script will change TRAIN.json from a list of comments
    to a dict of comments with each key being the comment ID. Should
    be much faster!
    """

    with open("TRAIN.json", 'r') as f:
        TRAIN = json.load(f)

    COMMENT = {}
    for comment in TRAIN:
        commID = comment.pop('id')
        COMMENT[commID] = comment

    with open('COMMENTS.json', 'w') as f2:
        json.dump(COMMENT, f2, indent = 4, sort_keys = True)


        
