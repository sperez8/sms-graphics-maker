#import prettyplotlib as ppl
import matplotlib.pyplot as plt
import argparse
import csv
import sys

DATAFILE = 'map_records.csv'
delimiter = ','
#COLORSETMORE = ["#fcd2a4","#fbaf5d","#f7941d","#f26c4f","#ed1c24","#9e0b0f"]

COLORSET2 = ["#BA2640","#1756ab"]
COLORSETMORE = ["#EC5E0C","#6D2243","#BA2640","#F78F1E","#85871A","#280904","#1756ab"]
COLORSETMOREORDER = ["#85871A","#F78F1E","#EC5E0C","#BA2640","#6D2243"]

HEADER = ["Title","Narrative","Date","Map filter #1","Map filter #2","Map filter #3","Map filter #4","Published"]
mapfilternames = {'Title':'organization_code',"Map filter #1":"gender","Map filter #2":"health","Map filter #3":"age_range","Map filter #4":"violent_act"}

def import_data(datafile):
	with open(datafile, 'r') as myfile:
		reader = csv.reader(myfile, delimiter=delimiter)
		header = []
		first = True
		data = []
		for row in reader:
			if first:
				header = [item.replace("Filter", "filter") for item in row]
				first = False
			else:

				data.append(clean_row(row))

	if header != HEADER:
		print "Header needs to be checked"
		sys.exit()

	print "\nReading .csv file:", datafile, "\n"
	data = remove_duplicates(data)
	return data, header

def remove_duplicates(data):
	new_data = []
	for row in data:
		if row not in new_data:
			new_data.append(row)
	return new_data



def clean_row(row):
	newrow = []
	title = row[0].split('-')[1:]
	newrow = row[1:]
	newrow.insert(0,'-'.join(title))
	newrow = ["NA" if x=='' or x==' ' else x for x in newrow]
	return newrow

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sortlabels(labels):
	numerical = True
	for l in labels:
	    if is_int(l.replace('+','').split('-')[0]) == False:
	    	numerical = False
	if numerical:
		parsed = [(l, int(l.replace('+','').split('-')[0])) for l in labels]
		newparsed = sorted(parsed, key = lambda x: x[1])
		newlabels = zip(*newparsed)[0]
	else:
		labels.sort()
		newlabels = labels
	return newlabels

def plot(labels,sublabels,data,x,y):
	fig, ax = plt.subplots(1)
	sublabels = sortlabels(sublabels)
	width = 0.8/float(len(sublabels))
	if len(sublabels)<=2:
		colors = {sl: COLORSET2[i] for i, sl in enumerate(sublabels)}
	elif len(sublabels) <= len(COLORSETMOREORDER):
		colors = {sl: COLORSETMOREORDER[i] for i, sl in enumerate(sublabels)}
	else:
		infinitepalette = COLORSETMORE
		while len(infinitepalette) < len(sublabels):
			infinitepalette.extend(COLORSETMORE)
		colors = {sl: infinitepalette[i] for i, sl in enumerate(sublabels)}
	max_y = 0
	for i,sl in enumerate(sublabels):
		#ppl.bar(ax, [w + width*i for w in range(len(labels))], [data[category][sl] for category in labels], width, grid='y', color = colors[sublabels[i]])
		ax.bar([w + width*i for w in range(len(labels))], [data[category][sl] for category in labels], width, color = colors[sublabels[i]], align='center')
		max_y = max(max_y,max([data[category][sl] for category in labels]))
	ax.set_xticks([w + width*2 for w in range(len(labels))])
	ax.set_xticklabels(labels)
	ax.set_title("Count of {1}s by {0}".format(x.replace('_',' '),y.replace('_',' ')),fontsize=16,y=1.03)
	ax.set_ylim([0,max_y*1.1])
	max_x = ax.get_xlim()[1]
	ax.set_xlim([-0.5,max_x])
	# Shrink current axis by 20%
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
	# Put a legend to the right of the current axis
	ax.legend(sublabels,loc='center left', bbox_to_anchor=(1, 0.5))
	filename = "bar_{0}_by_{1}.png".format(x,y)
	fig.savefig(filename)
	print "\t", filename
	return None

def make_bar_charts(data, header):
	X = ['Title','Map filter #1','Map filter #2','Map filter #3']
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
