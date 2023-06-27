# Webpage File Downloader GUI

This script is a simple Python application that allows you to download all files of a certain type from a webpage. It utilizes BeautifulSoup and requests libraries to scrape the webpage, and Tkinter to provide a simple graphical user interface.

## Dependencies
1. requests
2. BeautifulSoup4
3. Tkinter (comes pre-installed with Python)

## Mechanism

The script operates by sending a GET request to the specified URL, parsing the HTML response with BeautifulSoup to find all links, and filtering them based on the provided file extension. Then, it sends GET requests to download the selected files, saving them to the specified location.

## Use Case

This script can be used in a variety of situations where you need to download multiple files of a specific type from a webpage. For example, you could use it to download all PDF files from a webpage containing several research papers, or all JPEG images from a gallery webpage.

## Easiestway

Run the .exe file to use the program.

## Usage

A GUI will appear, asking you to enter the URL of the webpage from which you want to download files, the file extension of the files you want to download, and the directory where you want to save the downloaded files. Fill in these details and hit "OK" each time.
The script will start downloading the files. It may take some time depending on the number and size of the files.
Once all files are downloaded, you can find them in the directory you specified.

