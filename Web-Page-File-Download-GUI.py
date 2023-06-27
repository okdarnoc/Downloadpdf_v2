import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring
from urllib.parse import urlsplit

def download_files(url, ext, path):
    # Get the HTML
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all the links on the webpage
    links = soup.find_all("a")

    # Filter the links to get only the specified files
    file_links = [urljoin(url, link.get('href')) for link in links if link.get('href') and link.get('href').endswith(ext)]

    # Download the files
    for link in file_links:
        # Get the file name
        file_name = os.path.join(path, os.path.basename(urlsplit(link).path))
        
        # Download the file
        response = requests.get(link, stream=True)

        # Save the file
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                # Writing one chunk at a time to file
                if chunk:
                    file.write(chunk)


# Create a Tk root widget
root = Tk()

# Hide the main window 
root.withdraw()

# Prompt the user for the url of the webpage to scrape
url = askstring("URL", "Enter the URL of the webpage to scrape:")

# Prompt the user for the type of files to download
ext = askstring("File Extension", "Enter the file extension to download:")

# Prompt the user for the location to save the files
path = askdirectory(title="Select Folder")

# Use the function to download the files
download_files(url, ext, path)

# Close the Tk root widget
root.destroy()
