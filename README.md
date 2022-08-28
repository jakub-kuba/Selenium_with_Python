# Selenium_with_Python
Examples of automation in Selenium.


- <b>Check the Box</b> - this is an example program that works like a website control robot.<br>
  - Imagine you have a web application and you need to activate a lot of codes in the table. The codes to be checked have to be in a text file.
  - Open the program, press 'Upload file' and select the code file (e.g 'upload_me.txt'). The program will display the number of codes to be checked.
  - The program will open a browser, go to the [address](https://data.jakub-kuba.com/table) indicated and check the code by code. If the box next to a given code is ticked, it will not be clicked again, but the program will go to the next code. If code is in the file but not in the table, the program will not be interrupted, only the next code will be checked. If for some reason the program operation is interrupted (e.g. due to lack of Internet connection or server error), restart the program and select the file 'codes left.txt'. This file will only contain the codes that have not been added yet.
  
    Additional information:
    - The program works properly in Windows, while in Linux there are problems with proper GUI display created in the Tkinter binding. The program has not been tested on Mac OS.
    - The program works with the Google Chrome browser and requires the Chromedriver to work. The driver file should be located in the same folder as the program.

    Main components: Selenium, Tkinter

