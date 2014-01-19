import sys
import re

ENTRY_START = 297
RATING_RANGE = (20, 24)
TITLE_START = 26

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    entries = [line.strip() for line in f]

start = RATING_RANGE[0]
end = RATING_RANGE[1]
capturing = False
prev_rating = None
prev_show = None
episode = r'{.*}'

for entry in entries[ENTRY_START:ENTRY_START+100]:
    try:
        rating = float(entry[start:end])
        show = re.search(r'(.*?)\s+{', entry[TITLE_START:])
        if show:
            show = show.group(1)
        episode_name = re.search(r'{(.*)}', entry[TITLE_START:])
        if episode_name:
            episode_name = episode_name.group(1)
            episode_comp = re.search(r'\(#(\d+)\.(\d+)\)', episode_name)
            season, episode = episode_comp.group(1), episode_comp.group(2)
        else:
            episode_name = season = episode = None
        print "rating:", rating
        print "show:", show
        print "episode name:", episode_name
        print "season:", season
        print "episode:", episode
        print "\n"
    except ValueError:
        print "reached terminator"
        break
    if capturing and episode:
        pass
        # we're capturing and there's another episode to add to the current show
        # print "NEW EPISODE:", rating, show
    elif capturing:
        # we're capturing and there's no match
        capturing = False
    elif episode:
        # we're not capturing and we just hit a match
        #print "NEW TV SHOW:", prev_rating, prev_show
        # print "NEW EPISODE:", rating, show
        capturing = True
    prev_rating = rating
    prev_show = show
