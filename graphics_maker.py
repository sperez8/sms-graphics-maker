import prettyplotlib as ppl
import matplotlib.pyplot as plt
import argparse
import csv
import sys

DATAFILE = 'sgvb_fake_data_mapformatted.csv'
delimiter = ','
COLORSET = ["#a6d854","#e78ac3","#ffd92f"]
#HEADER = ['DATE','NARRATIVE','GENDER','HEALTH','AGE','ACT','PUBLISHED']
HEADER = ["Title","Narrative","Date","Map filter #1","Map filter #2","Map filter #3","Map filter #4","Published"]
mapfilternames = {"Map filter #1":"gender","Map filter #2":"health","Map filter #3":"age","Map filter #4":"violent_act"}

# def check(row):
# 	for item in row:
# 		if item[0]!='"' and item[-1]!='"':
# 			print row
# 			print "There is a comma in one of the narrative that is causing problems in parsing the file. Please remove it and try again"
# 			sys.exit()
# 	return None

def import_data(datafile):
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

	print "\nReading .csv file:", datafile, "\n"
	return data, header

def plot(labels,sublabels,data,x,y):
	fig, ax = plt.subplots(1)
	colors = {sl: COLORSET[i] for i, sl in enumerate(sublabels)}
	width = 0.3
	for i,sl in enumerate(sublabels):
		ppl.bar(ax, [w + width*i for w in range(len(labels))], [data[category][sl] for category in labels], width, grid='y', color = colors[sublabels[i]])
	ax.set_xticks([w + width for w in range(len(labels))])
	ax.set_xticklabels(labels)
	ax.set_title("Count of {1}s by {0} of victims".format(x.replace('_',' '),y.replace('_',' ')))
	ax.legend(sublabels)
	filename = "bar_{0}_by_{1}.png".format(x,y)
	fig.savefig(filename)
	print "\t", filename
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
	print "Making graphs:"
	for x in X:
		for y in Y:
			filter_column = header.index(x)
			act_column = header.index(y)
			acts = zip(*data)[act_column]
			filters = zip(*data)[filter_column]
			organized_data = {k:{l:0 for l in set(filters)}for k in set(acts)}
			for act,filter in zip(acts,filters):
				organized_data[act][filter]+=1
			plot(list(set(acts)),list(set(filters)),organized_data,mapfilternames[x],mapfilternames[y])
	print "\n"
	return None

def main(*argv):
	'''handles user input and creates a panel'''
	parser = argparse.ArgumentParser(description='This scripts takes a csv file of map records and created graphs to visualize the data.')
	parser.add_argument('-file', help='Gets the input file', default = DATAFILE)
	args = parser.parse_args()

	data,header =  import_data(args.file)
	make_bar_charts(data,header)

if __name__ == "__main__":
	main(*sys.argv[1:])