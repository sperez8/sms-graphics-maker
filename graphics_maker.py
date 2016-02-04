import prettyplotlib_local as ppl
import matplotlib_local.pyplot as plt
import csv
import sys

#datafile = 'map_records.csv'
datafile = 'sgvb_fake_data_mapformatted.csv'
delimiter = ','

#HEADER = ['DATE','NARRATIVE','GENDER','HEALTH','AGE','ACT','PUBLISHED']
HEADER = ["Title","Narrative","Date","Map filter #1","Map filter #2","Map filter #3","Map filter #4","Published"]

# def check(row):
# 	for item in row:
# 		if item[0]!='"' and item[-1]!='"':
# 			print row
# 			print "There is a comma in one of the narrative that is causing problems in parsing the file. Please remove it and try again"
# 			sys.exit()
# 	return None

#import data
with open(datafile, 'r') as myfile:
	reader = csv.reader(myfile, delimiter=delimiter)
	header = []
	first = True
	data = []
	for row in reader:
		if first:
			header = row
			first = False
		else:
			data.append(row)

if header != HEADER:
	print "Header needs to be checked"
	sys.exit()

def plot(labels,sublabels,data,title):
	fig, ax = plt.subplots(1)
	#colors = {sl: ppl.colors.set1[i] for i, sl in enumerate(sublabels)}
	width = 0.3
	for i,sl in enumerate(sublabels):
		ppl.bar(ax, [x + width*i for x in range(len(labels))], [data[category][sl] for category in labels], width, grid='y')#, color = colors[sublabels[i]])
	ax.set_xticks([x + width for x in range(len(labels))])
	ax.set_xticklabels(labels)
	ax.legend(sublabels)
	fig.savefig(title+'.png')
	return None

def bar_gender_by_act(data, header):
	gender_column = header.index('GENDER')+1
	act_column = header.index('ACT')+1
	acts = zip(*data)[act_column]
	genders = zip(*data)[gender_column]
	organized_data = {k:{l:0 for l in set(genders)}for k in set(acts)}
	for act,gender in zip(acts,genders):
		organized_data[act][gender]+=1
	plot(list(set(acts)),list(set(genders)),organized_data,"bar_gender_by_act")
	return None

def make_bar_charts(data, header):
	X = ['Map filter #1','Map filter #2']
	Y = ['Map filter #4']
	for x in X:
		for y in Y:
			filter_column = header.index(x)
			act_column = header.index(y)
			acts = zip(*data)[act_column]
			filters = zip(*data)[filter_column]
			organized_data = {k:{l:0 for l in set(filters)}for k in set(acts)}
			for act,filter in zip(acts,filters):
				organized_data[act][filter]+=1
			plot(list(set(acts)),list(set(filters)),organized_data,"bar_"+x+"_by_"+y)
	return None

make_bar_charts(data,header)