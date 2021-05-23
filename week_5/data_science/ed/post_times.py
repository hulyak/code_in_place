# for loading files with nested data
import json
# for turning strings into dates
from dateutil import parser
from pytz import timezone
# for making pretty graphs
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    ed_data = json.load(open('ed.json'))

    hour_counts = {}
    for hour in range(24):  # 24 hours
        hour_counts[hour] = 0
    print(hour_counts)

    for post in ed_data:
        timestamp = post['created_at']
        hour = get_hour(timestamp)
        hour_counts[hour] += 1.  # how many posts created at that hour
    print(hour_counts)

    print('day, n_posts')
    for hour in range(24):
        n_posts = hour_counts[hour]
        print(hour, n_posts)
    make_bar_plot(hour_counts)


def get_hour(time_string):
    """
    Given a time string, returns the day of the week (in pacific time).
    >>> get_hour('2021-05-21T01:20:39.296044+10:00')
    'Thu'
    """
    date_time = parser.parse(time_string)
    # change to my timezone
    date_time = date_time.astimezone(timezone('US/Pacific'))
    # get the hour out of the time object
    return date_time.hour


def make_bar_plot(count_map):
    """
    Turns a dictionary (where values are numbers) into a bar plot.
    Labels gives the order of the bars! Uses a package called seaborn
    for making graphs.
    """
    # turn the counts into a list
    counts = []
    # loop over the labels, in order
    for label in count_map:
        counts.append(count_map[label])
    # format the data in the way that seaborn wants
    data = {
        'x': list(count_map.keys()),
        'y': counts
    }
    sns.barplot(x='x', y='y', data=data)
    plt.savefig("plot.png")


if __name__ == '__main__':
    main()
