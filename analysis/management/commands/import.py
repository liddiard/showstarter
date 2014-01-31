import sys
import re

from analysis.models import Show, Episode

ENTRY_START = 297
RATING_RANGE = (20, 24)
TITLE_START = 26

input_file = sys.argv[2]

with open(input_file, 'r') as f:
    entries = [line.strip().decode('latin-1') for line in f]

start = RATING_RANGE[0]
end = RATING_RANGE[1]
capturing = False
prev_show = prev_rating = None
episode_re = r'{(?:(?P<episode_name>.*?)\s+)?\(#(?P<season>\d+)\.(?P<episode_number>\d+)\)}'
show_re = r'"(?P<name>.*?)"\s+\((?P<year>\d+)?(.*)?\)'

for entry in entries[ENTRY_START:]:
    try:
        rating = float(entry[start:end])
    except ValueError:
        print "reached terminator"
        sys.exit(0)
    else:
        episode = re.search(episode_re, entry[TITLE_START:])
        if episode:
            if episode.group('episode_name'):
                episode_name = episode.group('episode_name')[:127]
            else:
                episode_name = ''
            season = episode.group('season')
            episode_number = episode.group('episode_number')
        else:
            show = re.search(show_re, entry[TITLE_START:])
            episode_name = season = episode_number = None
        # print "rating:", rating
        # print "show:", show_name
        # print "episode name:", episode_name
        # print "season:", season
        # print "episode:", episode_number
        # print "\n"
    if capturing and episode:
        # we're capturing and there's another episode to add to the current show
        e = Episode(name=episode_name, rating=rating, show=s, season=season, 
                    episode=episode_number)
        e.save()
    elif capturing:
        # we're capturing and there's no match
        capturing = False
    elif episode:
        # we're not capturing and we just hit a match
        if prev_show.group('year'):
            year = prev_show.group('year')
        else:
            year = None
        s = Show(name=prev_show.group('name')[:127], 
                 year=year, rating=prev_rating)
        s.save()
        e = Episode(name=episode_name, rating=rating, show=s, season=season, 
                    episode=episode_number)
        e.save()
        capturing = True
    prev_show = show
    prev_rating = rating
