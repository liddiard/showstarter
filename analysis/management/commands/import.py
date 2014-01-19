import sys
import re

from analysis.models import Show, Episode

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
        show_name = re.search(r'(.*?)\s+{', entry[TITLE_START:])
        if show_name:
            show_name = show_name.group(1)
        episode_name = re.search(r'{(.*)}', entry[TITLE_START:])
        if episode_name:
            episode_name = episode_name.group(1)
            episode_comp = re.search(r'\(#(\d+)\.(\d+)\)', episode_name)
            season, episode = episode_comp.group(1), episode_comp.group(2)
        else:
            episode_name = season = episode = None
        # print "rating:", rating
        # print "show:", show_name
        # print "episode name:", episode_name
        # print "season:", season
        # print "episode:", episode
        # print "\n"
    except ValueError:
        print "reached terminator"
        break
    if capturing and episode:
        pass
        # we're capturing and there's another episode to add to the current show
        e = Episode(name=episode_name, rating=rating, show=s, season=season, 
        e.save()
    elif capturing:
        # we're capturing and there's no match
        capturing = False
    elif episode:
        # we're not capturing and we just hit a match
        s = Show(name=prev_show, rating=prev_rating)
        s.save()
        e = Episode(name=episode_name, rating=rating, show=s, season=season, 
                    episode=episode)
        e.save()
        capturing = True
    prev_rating = rating
    prev_show = show_name
