
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9934731
#    Student name: Kevin Duong
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import normpath, exists
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################

#====================================================================#
                            #TKINTER SETUP
#====================================================================#

#Please note that Windows os works fine, however I'm unsure if it's
#Compatible with mac os

# Create a window
window = Tk()
# Set the window's size
window.geometry('800x600')
# Make window background colour white
window['bg'] = 'white'
# Give the window a title
window.title('RT News Archive')
# Disables maximum mode
window.resizable(0,0)

# Radiobutton Frame
dates_frame = Frame(window, borderwidth=2, relief='solid')
dates_frame.place(relx=0.025, rely=0.42, width=376)

# HTML template, with blanks marked by asterisks
html_template = """<!DOCTYPE html>
<html>

    <head>
	
		<!-- Title for browser window/tab -->
		<title>RT News Archive</title>
		
		<!-- Overall document style -->
		<style>
		body {background-color: black}
		p	{width: 80%; margin-left: auto; margin-right: auto; text-align:justify; font-family: "Arial"}
		h1 	{width: 80%; margin-left: auto; margin-right: auto; text-align:center; font-family: "Arial"; font-size: 3em}
		h2 	{width: 80%; margin-left: auto; margin-right: auto; text-align:center; font-family: "Arial"; font-size: 2em}
		h3 	{width: 80%; margin-left: auto; margin-right: auto; text-align:center; font-family: "Arial"; font-size: 1.5em}
		div {width: 80%; margin-left: auto; margin-right: auto; background-color: white; height: 100%;}
		hr	{margin-top; margin-bottom: lem; background-color: black}
		</style>
	
	</head>
	
	<body>
	
		<div>
		<!-- Masterhead -->
		<h1>RT News Archive</h1>
		<!-- Day, Month, Year -->
		<h2>***SUBTITLE***</h2>
		
		<!-- RT News Logo from https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Russia-today-logo.svg/1200px-Russia-today-logo.svg.png -->
		<p style = "text-align:center"><img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Russia-today-logo.svg/1200px-Russia-today-logo.svg.png" 
										alt = "RT News Logo!" height="100%" width="100%" style="border: black 1px solid">
		<p style = "text-align:left"><strong>News source: </strong><a href="https://www.rt.com/rss/news/">https://www.rt.com/rss/news/</a>
		<br><strong>Archivist:</strong> Kevin Duong </br></p>
		
		<hr width = "80%" size = 5px>
		
		<!-- News article 1 -->
	
		<!-- Headline -->
		<h3>1. ***HEADLINE_1***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_1***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_1***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_1***">***SOURCE_1***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_1*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 2 -->
	
		<!-- Headline -->
		<h3>2. ***HEADLINE_2***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_2***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_2***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_2***">***SOURCE_2***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_2*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 3 -->
	
		<!-- Headline -->
		<h3>3. ***HEADLINE_3***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_3***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_3***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_3***">***SOURCE_3***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_3*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 4 -->
	
		<!-- Headline -->
		<h3>4. ***HEADLINE_4***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_4***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_4***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_4***">***SOURCE_4***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_4*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 5 -->
	
		<!-- Headline -->
		<h3>5. ***HEADLINE_5***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_5***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_5***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_5***">***SOURCE_5***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_5*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 6 -->
	
		<!-- Headline -->
		<h3>6. ***HEADLINE_6***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_6***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_6***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_6***">***SOURCE_6***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_6*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 7 -->
	
		<!-- Headline -->
		<h3>7. ***HEADLINE_7***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_7***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_7***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_7***">***SOURCE_7***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_7*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 8 -->
	
		<!-- Headline -->
		<h3>8. ***HEADLINE_8***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_8***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_8***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_8***">***SOURCE_8***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_8*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 9 -->
	
		<!-- Headline -->
		<h3>9. ***HEADLINE_9***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_9***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_9***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_9***">***SOURCE_9***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_9*** </br></p>
		
		<hr width = "80%" size = 5px>
		
		
		<!-- News article 10 -->
	
		<!-- Headline -->
		<h3>10. ***HEADLINE_10***</h3>
		<!-- Article Image -->
		<p style = "text-align:center"><img src = "***IMAGE_10***" alt = "Sorry, image not found!" height="100%" width="100%" style="border: black 1px solid;" />
		<!-- Story -->
		<p>***SYPNOSIS_10***</p>
		<!-- Source link -->
		<p style = "text-align:left"><strong>Full story:</strong> <a href="***SOURCE_10***">***SOURCE_10***</a>
		<!-- Date of publication -->
		<br><strong>Dateline:</strong> ***DATE_10*** </br></p>
		
		</div>
	
	</body>

</html>
"""

# Select date radiobutton indicatoron
MODES = [
        ("Thu, 12th Oct 2017", "InternetArchive/RTNews_12October_2017"),
        ("Fri, 13th Oct 2017", "InternetArchive/RTNews_13October_2017"),
        ("Sat, 14th Oct 2017", "InternetArchive/RTNews_14October_2017"),
        ("Sun, 15th Oct 2017", "InternetArchive/RTNews_15October_2017"),
        ("Mon, 16th Oct 2017", "InternetArchive/RTNews_16October_2017"),
        ("Tue, 17th Oct 2017", "InternetArchive/RTNews_17October_2017"),
        ("Wed, 18th Oct 2017", "InternetArchive/RTNews_18October_2017"),
        ("Latest", "InternetArchive/RTNews_Latest"),
    ]

# Create variables for each date
v = StringVar()
v.set("InternetArchive/RTNews_Latest") # Intial selection

#====================================================================#
                            #FUNCTIONS
#====================================================================#

# If radiobutton equals the date's value
# Date selection function
def selected_date():
    try:
        if MODES[0][1] == v.get():
            archive = open('InternetArchive/RTNews_12October_2017.xhtml',
                           'r', encoding = 'UTF-8')
            messenger.config(text = MODES[0][0])
        if MODES[1][1] == v.get():
            archive = open('InternetArchive/RTNews_13October_2017.xhtml',
                           'r',encoding = 'UTF-8')
            messenger.config(text = MODES[1][0])
        if MODES[2][1] == v.get():
             archive = open('InternetArchive/RTNews_14October_2017.xhtml',
                            'r',encoding = 'UTF-8')
             messenger.config(text = MODES[2][0])
        if MODES[3][1] == v.get():
             archive = open('InternetArchive/RTNews_15October_2017.xhtml',
                            'r',encoding = 'UTF-8')
             messenger.config(text = MODES[3][0])
        if MODES[4][1] == v.get():
             archive = open('InternetArchive/RTNews_16October_2017.xhtml',
                            'r',encoding = 'UTF-8')
             messenger.config(text = MODES[4][0])
        if MODES[5][1] == v.get():
             archive = open('InternetArchive/RTNews_17October_2017.xhtml',
                            'r',encoding = 'UTF-8')
             messenger.config(text = MODES[5][0])
        if MODES[6][1] == v.get():
             archive = open('InternetArchive/RTNews_18October_2017.xhtml',
                            'r',encoding = 'UTF-8')
             messenger.config(text = MODES[6][0])
        if MODES[7][1] == v.get():
             archive = open('InternetArchive/RTNews_Latest.xhtml',
                            'r',encoding = 'UTF-8')
             messenger.config(text = MODES[7][0])
    except FileNotFoundError:
        messenger.config(text = 'Error: News file not found in archive!')

for text, mode in MODES:
    b = Radiobutton(dates_frame, text=text, variable=v, value=mode,
                    indicatoron=0, width=26,anchor=W, selectcolor='#77BE17',
                    bg='white',fg='black', font = ('Arial', 18, 'bold'),
                    borderwidth=0, command = selected_date).pack()


# Log events on SQLite

# Create variable for checkbutton
check = IntVar()
check.set("-1") # initialize

log_description = ['News extracted from archive',
                   'Extracted news displayed in web browser',
                   'Latest news downloaded and stored in archive',
                   'Event logging switched on',
                   'Event logging switched off']

# When the db file is tampererd
sqlite_error = 'Error: event_log.db missing / modified!'

# Connect to the event_log.db file
connection = connect(database = 'event_log.db')
event_db = connection.cursor()

template = "INSERT INTO Event_Log VALUES (NULL, 'DESCRIPTION')"

# Checkbutton function
def log_events():
    try:
        # If the event log button is turned on
        if check.get() == 1:
            connection = connect(database = 'event_log.db')
            event_db = connection.cursor()
            event_description = log_description[3]
            sql_statement = template.replace('DESCRIPTION', event_description)
            event_db.execute(sql_statement)
            connection.commit()

        # If the event log button is turned off
        if check.get() == 0:
            connection = connect(database = 'event_log.db')
            event_db = connection.cursor()
            event_description = log_description[4]
            sql_statement = template.replace('DESCRIPTION', event_description)
            event_db.execute(sql_statement)
            connection.commit()
            
            event_db.close()
            connection.close()
    except:
        messenger.config(text = sqlite_error)

# Raw XML file from the internet archive is converted into
# a HTML with first 10 stories of that day

# Extract news function
def generate_html():
    try:
        # Initial conditions
        archive = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        if v.get() == "InternetArchive/RTNews_12October_2017":
            subtitle = "Thursday, 12th October 2017"
        if v.get() == "InternetArchive/RTNews_13October_2017":
            subtitle = "Friday, 13th October 2017"
        if v.get() == "InternetArchive/RTNews_14October_2017":
            subtitle = "Saturday, 14th October 2017"
        if v.get() == "InternetArchive/RTNews_15October_2017":
            subtitle = "Sunday, 15th October 2017"
        if v.get() == "InternetArchive/RTNews_16October_2017":
            subtitle = "Monday, 16th October 2017"
        if v.get() == "InternetArchive/RTNews_17October_2017":
            subtitle = "Tuesday, 17th October 2017"
        if v.get() == "InternetArchive/RTNews_18October_2017":
            subtitle = "Wednesday, 18th October 2017"
        if v.get() == "InternetArchive/RTNews_Latest":
            subtitle = "Latest Update"

        # Regex to find tags off xhtml files based on chosen archive
        headline_tag = '<title>(.*)</title>'
        image_tag = 'src="(.*?)"'
        item_tag = '<item>([\s\S]+?)</item>'
        story_tag = ['" /> (.*)<br/><a href',       # Single-line code
                     '" /> ([\s\S]+?)<br/><a href'] # Multi-line code
        news_tag = '<guid>(.*)</guid>'
        date_tag = '<pubDate>(.*)</pubDate>'

#====================================================================#
                                # STORY 1
#====================================================================#
        # Finds headline
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_1 = findall(headline_tag, xhtml_file.read())[2]

        # Finds image
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_1 = findall(image_tag, xhtml_file.read())[0]

        # Finds story
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[0]
        if sypnosis == '" /> <a href':
            sypnosis_1 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_1 = findall(story_tag[1], str(sypnosis))
            sypnosis_1 = ' '.join(sypnosis_1)

        # Finds news source
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_1 = findall(news_tag, xhtml_file.read())[0]

        # Finds date of publication
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        date_1 = findall(date_tag, xhtml_file.read())[0]
#====================================================================#
                                # STORY 2
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_2 = findall(headline_tag, xhtml_file.read())[3]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')   
        image_2 = findall(image_tag, xhtml_file.read())[1]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[1]
        if sypnosis == '" /> <a href':
            sypnosis_2 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_2 = findall(story_tag[1], str(sypnosis))
            sypnosis_2 = ' '.join(sypnosis_2)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        source_2 = findall(news_tag, xhtml_file.read())[1]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_2 = findall(date_tag, xhtml_file.read())[1]
#====================================================================#
                                # STORY 3
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_3 = findall(headline_tag, xhtml_file.read())[4]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_3 = findall(image_tag, xhtml_file.read())[2]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[2]
        if sypnosis == '" /> <a href':
            sypnosis_3 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_3 = findall(story_tag[1], str(sypnosis))
            sypnosis_3 = ' '.join(sypnosis_3)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_3 = findall(news_tag, xhtml_file.read())[2]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_3 = findall(date_tag, xhtml_file.read())[2]
#====================================================================#
                                # STORY 4
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_4 = findall(headline_tag, xhtml_file.read())[5]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_4 = findall(image_tag, xhtml_file.read())[3]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[3]
        if sypnosis == '" /> <a href':
            sypnosis_4 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_4 = findall(story_tag[1], str(sypnosis))
            sypnosis_4 = ' '.join(sypnosis_4)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_4 = findall(news_tag, xhtml_file.read())[3]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_4 = findall(date_tag, xhtml_file.read())[3]
#====================================================================#
                                # STORY 5
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_5 = findall(headline_tag, xhtml_file.read())[6]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')   
        image_5 = findall(image_tag, xhtml_file.read())[4]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[4]
        if sypnosis == '" /> <a href':
            sypnosis_5 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_5 = findall(story_tag[1], str(sypnosis))
            sypnosis_5 = ' '.join(sypnosis_5)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_5 = findall(news_tag, xhtml_file.read())[4]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_5 = findall(date_tag, xhtml_file.read())[4]
#====================================================================#
                                # STORY 6
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_6 = findall(headline_tag, xhtml_file.read())[7]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        image_6 = findall(image_tag, xhtml_file.read())[5]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[5]
        if sypnosis == '" /> <a href':
            sypnosis_6 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_6 = findall(story_tag[1], str(sypnosis))
            sypnosis_6 = ' '.join(sypnosis_6)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_6 = findall(news_tag, xhtml_file.read())[5]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_6 = findall(date_tag, xhtml_file.read())[5]
#====================================================================#
                                # STORY 7
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_7 = findall(headline_tag, xhtml_file.read())[8]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_7 = findall(image_tag, xhtml_file.read())[6]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[6]
        if sypnosis == '" /> <a href':
            sypnosis_7 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_7 = findall(story_tag[1], str(sypnosis))
            sypnosis_7 = ' '.join(sypnosis_7)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_7 = findall(news_tag, xhtml_file.read())[6]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_7 = findall(date_tag, xhtml_file.read())[6]
#====================================================================#
                                # STORY 8
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_8 = findall(headline_tag, xhtml_file.read())[9]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        image_8 = findall(image_tag, xhtml_file.read())[7]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[7]
        if sypnosis == '" /> <a href':
            sypnosis_8 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_8 = findall(story_tag[1], str(sypnosis))
            sypnosis_8 = ' '.join(sypnosis_8)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')   
        source_8 = findall(news_tag, xhtml_file.read())[7]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8') 
        date_8 = findall(date_tag, xhtml_file.read())[7]
#====================================================================#
                                # STORY 9
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_9  = findall(headline_tag, xhtml_file.read())[10]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')   
        image_9  = findall(image_tag, xhtml_file.read())[8]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[8]
        if sypnosis == '" /> <a href':
            sypnosis_9 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_9 = findall(story_tag[1], str(sypnosis))
            sypnosis_9 = ' '.join(sypnosis_9)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')  
        source_9  = findall(news_tag, xhtml_file.read())[8]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_9  = findall(date_tag, xhtml_file.read())[8]
#====================================================================#
                                # STORY 10
#====================================================================#
        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        headline_10 = findall(headline_tag, xhtml_file.read())[11]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8') 
        image_10 = findall(image_tag, xhtml_file.read())[9]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        sypnosis = findall(item_tag, xhtml_file.read())[9]
        if sypnosis == '" /> <a href':
            sypnosis_10 = findall(story_tag[0], str(sypnosis))
        else:
            sypnosis_10 = findall(story_tag[1], str(sypnosis))
            sypnosis_10 = ' '.join(sypnosis_10)

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        source_10 = findall(news_tag, xhtml_file.read())[9]

        xhtml_file = open(v.get() + '.xhtml','r',encoding = 'UTF-8')
        date_10 = findall(date_tag, xhtml_file.read())[9]
#====================================================================#
        
        # Adds the date of the news
        html_code = html_template.replace('***SUBTITLE***', subtitle)
        
        # Replace the blanks for story 1
        html_code = html_code.replace('***HEADLINE_1***', headline_1)
        html_code = html_code.replace('***IMAGE_1***', image_1)
        html_code = html_code.replace('***SYPNOSIS_1***', sypnosis_1)
        html_code = html_code.replace('***SOURCE_1***', source_1)
        html_code = html_code.replace('***DATE_1***', date_1)
        # Replace the blanks for story 2
        html_code = html_code.replace('***HEADLINE_2***', headline_2)
        html_code = html_code.replace('***IMAGE_2***', image_2)
        html_code = html_code.replace('***SYPNOSIS_2***', sypnosis_2)
        html_code = html_code.replace('***SOURCE_2***', source_2)
        html_code = html_code.replace('***DATE_2***', date_2)
        # Replace the blanks for story 3
        html_code = html_code.replace('***HEADLINE_3***', headline_3)
        html_code = html_code.replace('***IMAGE_3***', image_3)
        html_code = html_code.replace('***SYPNOSIS_3***', sypnosis_3)
        html_code = html_code.replace('***SOURCE_3***', source_3)
        html_code = html_code.replace('***DATE_3***', date_3)
        # Replace the blanks for story 4
        html_code = html_code.replace('***HEADLINE_4***', headline_4)
        html_code = html_code.replace('***IMAGE_4***', image_4)
        html_code = html_code.replace('***SYPNOSIS_4***', sypnosis_4)
        html_code = html_code.replace('***SOURCE_4***', source_4)
        html_code = html_code.replace('***DATE_4***', date_4)
        # Replace the blanks for story 5
        html_code = html_code.replace('***HEADLINE_5***', headline_5)
        html_code = html_code.replace('***IMAGE_5***', image_5)
        html_code = html_code.replace('***SYPNOSIS_5***', sypnosis_5)
        html_code = html_code.replace('***SOURCE_5***', source_5)
        html_code = html_code.replace('***DATE_5***', date_5)
        # Replace the blanks for story 6
        html_code = html_code.replace('***HEADLINE_6***', headline_6)
        html_code = html_code.replace('***IMAGE_6***', image_6)
        html_code = html_code.replace('***SYPNOSIS_6***', sypnosis_6)
        html_code = html_code.replace('***SOURCE_6***', source_6)
        html_code = html_code.replace('***DATE_6***', date_6)
        # Replace the blanks for story 7
        html_code = html_code.replace('***HEADLINE_7***', headline_7)
        html_code = html_code.replace('***IMAGE_7***', image_7)
        html_code = html_code.replace('***SYPNOSIS_7***', sypnosis_7)
        html_code = html_code.replace('***SOURCE_7***', source_7)
        html_code = html_code.replace('***DATE_7***', date_7)
        # Replace the blanks for story 8
        html_code = html_code.replace('***HEADLINE_8***', headline_8)
        html_code = html_code.replace('***IMAGE_8***', image_8)
        html_code = html_code.replace('***SYPNOSIS_8***', sypnosis_8)
        html_code = html_code.replace('***SOURCE_8***', source_8)
        html_code = html_code.replace('***DATE_8***', date_8)
        # Replace the blanks for story 9
        html_code = html_code.replace('***HEADLINE_9***', headline_9)
        html_code = html_code.replace('***IMAGE_9***', image_9)
        html_code = html_code.replace('***SYPNOSIS_9***', sypnosis_9)
        html_code = html_code.replace('***SOURCE_9***', source_9)
        html_code = html_code.replace('***DATE_9***', date_9)
        # Replace the blanks for story 10
        html_code = html_code.replace('***HEADLINE_10***', headline_10)
        html_code = html_code.replace('***IMAGE_10***', image_10)
        html_code = html_code.replace('***SYPNOSIS_10***', sypnosis_10)
        html_code = html_code.replace('***SOURCE_10***', source_10)
        html_code = html_code.replace('***DATE_10***', date_10)

#====================================================================#

        # Write the HTML code to a file
        html_file = open('RTNews.html', 'w')
        html_file.write(html_code)
        html_file.close()
        # Display message
        messenger.config(text = 'News Extraction Complete!')
        
    except FileNotFoundError:
        messenger.config(text = 'Extraction failed!')

    # If the event log button is turned on and
    # Extract news button is pressed
    try:
        if check.get() == 1:
            event_description = log_description[0]
            sql_statement = template.replace('DESCRIPTION', event_description)
            event_db.execute(sql_statement)
            connection.commit()
    except:
        messenger.config(text = sqlite_error)

#====================================================================#

# Displays extracted news function
def display():
    location = normpath('/RTNews.html')
    path = getcwd()
    fullpath = path + location
    # Imported 'exists' function from os.path
    if exists(fullpath):
        webopen('file://' + fullpath)
        messenger.config(text = 'Extracted News Displayed!')
    else:
        messenger.config(text = 'Cannot find Extracted News!')

    # If the event log button is turned on
    # Display extracted news button is pressed
    try:
        if check.get() == 1:
            event_description = log_description[1]
            sql_statement = template.replace('DESCRIPTION', event_description)
            event_db.execute(sql_statement)
            connection.commit()
    except:
        messenger.config(text = sqlite_error)

# Archives the latest news function
def archive():
    try:
        url = 'https://www.rt.com/rss/news/'
        web_page = urlopen(url)
        web_page_contents = web_page.read().decode('UTF-8')
        html_file = open('InternetArchive/RTNews_Latest.xhtml',
                         'w', encoding = 'UTF-8')
        html_file.write(web_page_contents)
        html_file.close()
        messenger.config(text = 'Latest News Archived!')
    except:
        messenger.config(text = 'Check Internet Connection / Internet Archive')

    # If the event log button is turned on
    # Archive latest news button is pressed
    try:
        if check.get() == 1:
            event_description = log_description[2]
            sql_statement = template.replace('DESCRIPTION', event_description)
            event_db.execute(sql_statement)
            connection.commit()
    except:
        messenger.config(text = sqlite_error)

#====================================================================#
                                #GUI
#====================================================================#

# Messenger label
messenger = Label(window, text = 'Select a date...', bg='white', fg='black',
            font = ('Arial', 22))
messenger.place(relx=0.75, rely=0.65, anchor='center')
messenger.configure(wraplength='260')

# Extract button
extract_button = Button(window, text = 'Extract news from archive',
                        font = ('Arial', 14), fg='black', bg='white',
                        relief = 'solid', command = generate_html)

extract_button.place(relx=0.515, rely=0.78, height=60, width=120)
extract_button.configure(wraplength='120')

# Display button
display_button = Button(window, text = 'Display news extracted',
                        font = ('Arial', 14), fg='black', bg='white',
                        relief = 'solid', command = display)

display_button.place(relx=0.675, rely=0.78, height=60, width=120)
display_button.configure(wraplength='120')

# Archive button
archive_button = Button(window, text = 'Archive the latest news',
                        font = ('Arial', 14), fg='black', bg='white',
                        relief = 'solid', command = archive)

archive_button.place(relx=0.835, rely=0.78, height=60, width=120)
archive_button.configure(wraplength='120')

# Log event checkbox
log_button = Checkbutton(window, text="Log events", font = ('Arial', 14),
                         fg='black', bg='white', variable = check,
                         command = log_events)
log_button.place(relx=0.675, rely=0.9)

# Logo image
try:
    Label(window, bg = 'black', height = 12).pack(fill=X, pady=23)
    img = PhotoImage(file="RT_Image.gif")
    img = img.zoom(16)
    img = img.subsample(32)
    logo = Label(window, image=img, borderwidth=0)
    logo.place(relx=0.025, rely=0.04)
except:
    messenger.config(text = 'Error: RT_Image.gif not found!')
    extract_button.config(state = DISABLED)
    display_button.config(state = DISABLED)
    archive_button.config(state = DISABLED)
    log_button.config(state = DISABLED)

# Logo subtitle
logo_subtitle = Label(window, text = 'Russia Today News Archive',
                bg='white', fg='black', font = ('Arial', 22, 'bold'))
logo_subtitle.place(relx=0.625, rely=0.4)
logo_subtitle.configure(wraplength='260')


# -------------------------------------------------------------------#

# Start the event loop
window.mainloop()

