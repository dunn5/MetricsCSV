MetricsCSV
==========
Better readme will be added soon

For the time being here is something to start with :)

_____

This program will pull your minute by minute data from the MyBasis website and place it into a CSV file.

____

First you will need to find your unique identifier code for the MyBasis API
In Chrome Click View> Developer> Developer Tools

Click Network

Locate api/v1/chart

Open that in a new tab
In the URL there will be a code after "https://app.mybasis.com/api/v1/chart/" and before ".json"
This a unique identifier for your data. 
Be aware that as of the writing of this readme, this code is all it will take for someone to access 
your data there are no other security measures in place.


---
Download the .py file from this github

Create a plain text file called hexkey.txt and place in the same folder as the .py file.
In hexkey.txt place your unique identifier code and save the file

Now you chould be able to run your python file.
When you run the script the command line will prompt you to enter the number of days you want to download starting with today.
Enter the number and hit enter.
The file will download.

---------
Please note that it may take some time to download and more days = more time. 

[Process completed] will display when the download is complete. You can then view your data :)


If you run the program again it will overwrite your previous csv file so be sure to resave your file with a new name or in a new location to avoid accidental overwrites.

Enjoy!
