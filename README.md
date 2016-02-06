# sms-graphics-maker

This repository contains everything you need to make visual graphs of the sms map record data.

So far two bar charts have been developped: one showing counts of victims by gender and act, and one by health status and act.

More coming soon!

## Setup

You will need a working version of Python on your machine, ideally version 2.7. You can download Python [here](https://www.python.org/downloads/).

### Getting SMS-graphics-maker

Getting the graphics maker on your computer is quite simple. First, go the the [github homepage](https://github.com/sperez8/sms-graphics-maker) and click **Download Zip** in the top right of the page. Unzip the file and store it somewhere convenient on your machine like your **Desktop** folder.

### Opening the sms-graphics-maker folder

Unzip the **sms-graphics-maker** folder. You should see something like this:

![default](http://i.imgur.com/sqso2xb.jpg)

There are really only 3 files you care about:
* **map_records.csv** - the file with all the data. Anytime you want to update the data, simply replace the file (keeping exactly the same name)
*  **runme** files - There are three of these depending on what kind of computer you are using Windows, Mac or Windows
*  **bar_gender_by_violent_act.png** and similar files - these are the visualizations in picture format. As you update the data and run the scripts, these files will be updated.

### Running the graphics maker, the easy way

Once you have updated the **map_records.csv** data file. Click on the **runme** files with the name that matches the kind of computer you have. I have a windows so I will double click on the **runme_windows.bat** file.

If all goes well a little black window will open momentarily, close, and the graphics should have been updated.

You are all done!



---

### Running the graphics maker using the command line (experienced users only!)

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
