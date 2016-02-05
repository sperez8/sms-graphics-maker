# sms-graphics-maker

This repository contains everything you need to make visual graphs of the sms map record data.

## Setup

You will need a working version of Python on your machine, ideally version 2.7, as well as the [NumPy](http://www.numpy.org/) package package. You can download Python [here](https://www.python.org/downloads/) and Numpy [here](http://sourceforge.net/projects/numpy/files/).

## Getting SMS-graphics-maker

Getting the graphics maker on your computer is quite simple. First, go the the [github homepage](https://github.com/sperez8/sms-graphics-maker) and click **Download Zip** in the top right of the page. Unzip the file and store it somewhere convenient on your machine like your **Desktop** folder.

## Running the graphics maker

Let's test that everything works on some of the test data. Open a **terminal window** (here are instructions to open a terminal window for [Windows](http://windows.microsoft.com/en-ca/windows-vista/open-a-command-prompt-window) and for a [Mac](https://www.google.ca/webhp?sourceid=chrome-instant&ion=1&espv=2&es_th=1&ie=UTF-8#q=how+to+open+terminal+on+macbook)).

From the terminal window, change directories until you are in the **sms-graphics-maker** folder you just unzipped.

```
$ cd Desktop/sms-graphics-maker/
```

If you want to take a look at the test data, check out the **sgvb_fake_data_mapformatted.csv** file using a text editor or Excel.

The python script we want to run is called **graphics_maker.py**. We run it by using the following command:

```
$ python graphics_maker.py -file sgvb_fake_data_mapformatted.csv
```

You should see the following text printed in your terminal:

```
Reading .csv file: sgvb_fake_data_mapformatted.csv

Making graphs:
        bar_gender_by_violent_act.png
        bar_health_by_violent_act.png

```

It worked! Open the directory to see the new graph files in .png files.

To run the script with new data, you'll need to first move the data file in the sms-graphics-maker folder, then run the command:

```
$ python .\graphics_maker.py -file my_new_data_file.csv
```

where **my_new_data_file.csv** is the name of your file.

Good luck!
