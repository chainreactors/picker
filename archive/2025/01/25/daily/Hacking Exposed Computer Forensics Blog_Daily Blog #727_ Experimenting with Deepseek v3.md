---
title: Daily Blog #727: Experimenting with Deepseek v3
url: https://www.hecfblog.com/2025/01/daily-blog-727-experimenting-with.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-25
fetch_date: 2025-10-06T20:29:20.739793
---

# Daily Blog #727: Experimenting with Deepseek v3

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[deepseek](https://www.hecfblog.com/search/label/deepseek)

Daily Blog #727: Experimenting with Deepseek v3

# Daily Blog #727: Experimenting with Deepseek v3

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 23, 2025
•

[ai programming](https://www.hecfblog.com/search/label/ai%20programming?&max-results=8)
[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[deepseek](https://www.hecfblog.com/search/label/deepseek?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh28ZIwF5Gapvy8YQJCEHk0XRIBkxLjQT5ZOoYhH2euSVsQn8GIAH0gjr9k5HDXxZhcDHUnY26ULuKlDWYpeGRH7PlcJNuybaYlGog85MynQqRGvwEdawmyfnDAgDCT8bJKR4MWKT02SdAqcC74Sd5RmFSfIlICBsVmXNnWSLFS9csHPCHTkuLCueokkyM/w640-h640/deepseek.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh28ZIwF5Gapvy8YQJCEHk0XRIBkxLjQT5ZOoYhH2euSVsQn8GIAH0gjr9k5HDXxZhcDHUnY26ULuKlDWYpeGRH7PlcJNuybaYlGog85MynQqRGvwEdawmyfnDAgDCT8bJKR4MWKT02SdAqcC74Sd5RmFSfIlICBsVmXNnWSLFS9csHPCHTkuLCueokkyM/s1024/deepseek.webp)

Hello Reader,

    Deepseek v3 is an open source AI model that is challenging OpenAI's dominance.  I decided to give it a spin and provide it a one off prompt in Cursor (which now has Deepseek v3 as one of it's available models) to create a python script with a GUI to download onion links. According to the publicly available testing Deepseek v3 is matching in chain of thought functionality with o1 and is considerable cheaper to run.

I will say the code it wrote is good and its ability to correctly explain and define things works very well. I need to determine what the context window Cursor is making available for this so I can find out how much code I can provide.

Here is the code I got deepseek to write in just a few prompts:

import sys

import time

import requests

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,

QLabel, QLineEdit, QPushButton, QFileDialog, QProgressBar)

from PySide6.QtCore import QThread, Signal

from urllib3.util.retry import Retry

from requests.adapters import HTTPAdapter

from stem import Signal

from stem.control import Controller

import stem.process

# Tor proxy settings

TOR\_PROXY = {

'http': 'socks5h://127.0.0.1:9050',

'https': 'socks5h://127.0.0.1:9050'

}

class DownloadThread(QThread):

progress = Signal(int)

speed = Signal(str)

finished = Signal(bool)

error = Signal(str)

def \_\_init\_\_(self, url, save\_path):

super().\_\_init\_\_()

self.url = url

self.save\_path = save\_path

def run(self):

try:

# Test SOCKS support

try:

import socks

from socket import socket

# Test Tor connection

test\_socket = socket()

test\_socket.settimeout(10)

test\_socket.connect(('127.0.0.1', 9050))

test\_socket.close()

msg = "Tor connection verified"

print(msg)

self.error.emit(msg)

except ImportError:

msg = "SOCKS support not available. Please install PySocks."

print(msg)

self.error.emit(msg)

self.finished.emit(False)

return

except Exception as e:

msg = f"Failed to connect to Tor: {str(e)}"

print(msg)

self.error.emit(msg)

self.finished.emit(False)

return

# Create a session with retry logic

session = requests.Session()

retries = Retry(total=5, backoff\_factor=0.1, status\_forcelist=[500, 502, 503, 504])

session.mount('http://', HTTPAdapter(max\_retries=retries))

session.mount('https://', HTTPAdapter(max\_retries=retries))

msg = f"Attempting to connect to: {self.url}"

print(msg)

self.error.emit(msg)

with session.get(self.url, stream=True, proxies=TOR\_PROXY, timeout=30) as r:

msg = f"Connection established. Status code: {r.status\_code}"

print(msg)

self.error.emit(msg)

r.raise\_for\_status()

total\_length = int(r.headers.get('content-length', 0))

if total\_length == 0:

msg = "Warning: Content length is 0 or not provided"

print(msg)

self.error.emit(msg)

downloaded = 0

start\_time = time.time()

with open(self.save\_path, 'wb') as f:

for chunk in r.iter\_content(chunk\_size=8192):

if chunk:

f.write(chunk)

downloaded += len(chunk)

progress = int((downloaded / total\_length) \* 100) if total\_length > 0 else 0

elapsed\_time = time.time() - start\_time

speed = downloaded / (elapsed\_time \* 1024) if elapsed\_time > 0 else 0  # KB/s

self.progress.emit(progress)

self.speed.emit(f"{speed:.2f} KB/s")

msg = f"Download completed. Total bytes: {downloaded}"

print(msg)

self.error.emit(msg)

self.finished.emit(True)

except requests.exceptions.RequestException as e:

msg = f"Network error: {str(e)}\nResponse: {e.response.text if e.response else 'No response'}"

print(msg)

self.error.emit(msg)

self.finished.emit(False)

except Exception as e:

msg = f"Error: {str(e)}\nType: {type(e).\_\_name\_\_}"

print(msg)

self.error.emit(msg)

self.finished.emit(False)

class MainWindow(QMainWindow):

def \_\_init\_\_(self):

super().\_\_init\_\_()

self.setWindowTitle("Tor Downloader")

self.setGeometry(100, 100, 400, 200)

# Create main widget and layout

main\_widget = QWidget()

self.setCentralWidget(main\_widget)

layout = QVBoxLayout()

# URL input

self.url\_input = QLineEdit()

self.url\_input.setPlaceholderText("Enter .onion URL")

layout.addWidget(QLabel("Onion URL:"))

layout.addWidget(self.url\_input)

# Save location

self.save\_path\_input = QLineEdit()

self.save\_path\_input.setReadOnly(True)

browse\_button = QPushButton("Browse...")

browse\_button.clicked.connect(self.select\_save\_location)

layout.addWidget(QLabel("Save Location:"))

layout.addWidget(self.save\_path\_input)

layout.addWidget(browse\_button)

# Progress bar

self.progress\_bar = QProgressBar()

layout.addWidget(self.progress\_bar)

# Speed label

self.speed\_label = QLabel("Speed: 0.00 KB/s")

layout.addWidget(self.speed\_label)

# Download button

self.download\_button = QPushButton("Download")

self.download\_button.clicked.connect(self.start\_download)

layout.addWidget(self.download\_button)

main\_widget.setLayout(layout)

self.tor\_process = None

def select\_save\_location(self):

folder\_path = QFileDialog.getExistingDirectory(self, "Select Save Folder")

if folder\_path:

self.save\_path\_input.setText(folder\_path)

def start\_tor(self):

try:

# Check if Tor is already running

try:

with Controller.from\_port(port=9051) as controller:

controller.authenticate()

msg = "Connected to existing Tor process"

print(msg)

return True

except:

pass

# Start Tor process

self.tor\_process = stem.process.launch\_tor\_with\_config(

config={

'SocksPort': '9050',

'ControlPort': '9051',

},

take\_ownership=True,

timeout=300

)

msg = "Started new Tor process"

print(msg)

return True

except Exception as e:

msg = f"Failed to start Tor: {str(e)}"

print(msg)

self.handle\_error(msg)

return False

def stop\_tor(self):

if self.tor\_process:

self.tor\_process.terminate()

msg = "Stopped Tor process"

print(msg)

self...