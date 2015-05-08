# This file has a few mistakes and some things I forgot to put in.
# When I run it I don't get anything... can you fix it so I
# get asked for my vacation spot, and get a recommendation?
# Hint:
# Start at the bottom and work upwards.

import site

vacation_spots = {
    'snow': 'Tahoe', 
    'wind': 'Hawaii', 
    'rain': 'New York',
    'sun': 'Mexico'
}

seasons = ['spring', 'summer', 'fall', 'winter']

weather_patterns = {
    'spring': 'rain',
    'summer': 'sun',
    'fall': 'wind',
    'winter': 'snow'
}

activities = {
    'rain': 'visiting museums',
    'wind': 'kiteboarding',
    'sun': 'sunbathing',
    'snow': 'skiing'
}


def best_vacation_spot(weather_type):
    return vacation_spots[weather_type]


def vacation_activity(weather_type):
    # Look up the vacation activity from activities
    # and return just the activity itself
    return activities[weather_type]


def get_my_vacation():

    season = raw_input("What season do you want to travel? ")

    # check if season is in the seasons list
    if season not in seasons:
        print "Sorry, that isn't a season. I can't help you."
        exit()

    # look up the weather type for that season
    weather = weather_patterns[season]

    # get the best vacation spot for that type
    vacation_spot = best_vacation_spot(weather)

    # get the best vacation activity for that type
    activity = vacation_activity(weather)

    print "You should travel to {}, where you can spend your time {}!".format(vacation_spot, activity)


def main():
    print "Welcome to the Vacation-o-Matic!"
    get_my_vacation()


if __name__=="__main__":
    main()