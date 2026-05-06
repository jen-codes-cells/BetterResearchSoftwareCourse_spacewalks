#required packages
import json
import csv
import datetime as dt
import matplotlib.pyplot as plt

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding="ascii")
output_file = open('./eva-data.csv','w', encoding="utf-8")
graph_file = './cumulative_eva_graph.png'

data=[]


for i in range(375):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet

csv_writer=csv.writer(output_file)



time = []
date =[]

j=0
for i in data:
    print(data[j])
    # and this bit
    csv_writer.writerow(data[j].values())
    if 'duration' in data[j].keys():
        time_dt=data[j]['duration']
        if time_dt == '':
            pass
        else:
            time=dt.datetime.strptime(time_dt,'%H:%M')
            time_float = dt.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second).total_seconds()/(60*60)
            print(time,time_float)
            time.append(time_float)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

time=[0]
for i in time:
    time.append(time[-1]+i)

date,time = zip(*sorted(zip(date, time)))


plt.plot(date,time[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig("cumulative_eva_graph.png")
plt.show()
