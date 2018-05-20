#############################################################################
# This script will take the data we have from the FaceBot project and create
# the basic data we need for training the algorithms behind CLARITY.
#############################################################################

import json
from random import shuffle

def create():
    """
    Make the new data.
    """
    TRAIN = []

    with open('annotation.json', 'r') as f:
        ANNOT = json.load(f)

    with open('USERS.json', 'r') as f2:
        USERS = json.load(f2)

    # Extract comments of the annotated users, then add bot category to each
    for bucket in ANNOT:
        for user in ANNOT[bucket]:
            is_bot = False if ANNOT[bucket][user] == "1" else True
            comments = USERS[user]
            for comment in comments:
                comment['bot'] = is_bot
            TRAIN.extend(comments)

    # Shuffle the list to make sure nothing weird happens in training
    shuffle(TRAIN)

    with open('TRAIN.json', 'w') as f3:
        json.dump(TRAIN, f3, indent = 4, sort_keys = True)

def strip_extra():
    """
    Get rid of the keys we don't need, stuff having to do with
    thread structure.
    """
    with open('TRAIN.json', 'r') as f:
        TRAIN = json.load(f)

    for comment in TRAIN:
        del comment['rep_index']
        del comment['top_index']

    with open('TRAIN.json', 'w') as f2:
        json.dump(TRAIN, f2, indent = 4, sort_keys = True)


