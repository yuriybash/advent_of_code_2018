from collections import defaultdict
from dateutil import parser
from pprint import pprint
import operator

with open('day_4_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

sorted_data = sorted(data, key=lambda x: parser.parse(x[1:17]))

mapped_times = defaultdict(dict)

current_guard = None
fell_asleep_timestamp = None
for event in sorted_data:
    if 'Guard' in event:
        current_guard = event[26:event.index(' begins')]
        fell_asleep_timestamp = None
        woke_up_timestamp = None
    elif 'falls asleep' in event:
        fell_asleep_timestamp = parser.parse(event[1:17])
    elif 'wakes up' in event:
        woke_up_timestamp = parser.parse(event[1:17])
        for minute_asleep in xrange(fell_asleep_timestamp.minute, woke_up_timestamp.minute):
            if minute_asleep in mapped_times[current_guard]:
                mapped_times[current_guard][minute_asleep]+=1
            else:
                mapped_times[current_guard][minute_asleep]=1

total_times = {}
for guard, times in mapped_times.iteritems():
    total_times[guard] = sum(times.values())

guards_sorted_by_total_time = sorted(total_times.items(), key=operator.itemgetter(1), reverse=True)
print "guard id: ", guards_sorted_by_total_time[0][0]
print(guards_sorted_by_total_time[0][0])
