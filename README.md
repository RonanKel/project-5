Author = Ronan Kelly
Date Modified = 02/22/2023


	This application lets us run a web program using flask. This program helps us to calculate a race's (brevet's) control's start and open time without having to reload the page.
To start this program all you must do is enter the '/brevets' directory and type "python3 flask_brevets.py". This will read the Dockerfile start it and let you access the server through which ever port
you have described in your credentials.ini file. In your browser type 'localhost:<port>'.

	The way this works is that you select a start date, time, brevet length, and at what distance you would like there to be a control. Using JS and flask every time you enter in a control position,
the JS will get a getJSON request to the flask_brevets.py file. It will send the data of the start date and time, brevets distance, and control position. Then the script will pass it through
two functions, one to see what time the control opens and when it closes.

	This is handled through a file called "acp_times.py". For the open times this function will see the position and pass it through an if statement which will then parse the amount of hours
that will have passed since the start time, then truncates the number of minutes so it doesn't round and then returns an arrow object which now represents the time in which the control opens.
It is tested on whether distance is 0, less than 200, 300, 400, 600, and 1000, then calculates. Or it tests to see if the control is past the brevet length in which it will return the same time the
control at the control that is at the brevet length.


	For the close times function, it tests to see if the control is at 0, if its less than 60, 600, and 1000 then calculates the hours and returns an arrow object like the open times function. It also tests to see if a control is past the brevet length and then returns the same closing time a control at the brevet length would be. These function largely the same, however the closing time function uses
dictionary based data to check how long a brevet max closing time would be.

	For more information about how these times were calculated, visit: https://rusa.org/pages/acp-brevet-control-times-calculator

	Once returned they are turned into strings, put into a dictionary and are sent to the webpage with a JSONify response. The JS in the webpage parses this information, and chnges the values of the
open and close time on the web page corosponding to the row the distance was entered. This is all done without reloading the page.


	When the Submit button is pressed it clears the form and sends the entered values to flask. Then it gets processed in mypymongo.py where it is saved to the mongodb database in the collection
races. Then when the Display button is pressed the form is reset and then the latest submission is filled out into the form by sending a json request to the flask which then retrieves the data from the
database and then returns it, which is then processed in JS and is loaded into the form.
