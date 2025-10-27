---
title: Interfacing With A Cheap Geiger Counter
url: https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/
source: Didier Stevens
date: 2024-11-23
fetch_date: 2025-10-06T19:17:29.305321
---

# Interfacing With A Cheap Geiger Counter

# [Didier Stevens](https://blog.didierstevens.com/)

## Friday 22 November 2024

### Interfacing With A Cheap Geiger Counter

Filed under: [Hardware](https://blog.didierstevens.com/category/hardware/),[My Software](https://blog.didierstevens.com/category/my-software/) — Didier Stevens @ 0:00

I got a cheap [Geiger](https://en.wikipedia.org/wiki/Geiger_counter) counter from Aliexpress:

![](https://blog.didierstevens.com/wp-content/uploads/2024/11/20241120-212035.png)

This picture was taken on an airplane: you have more radiation (cosmic rays) at high altitude.

I figured out how to interface with this counter in Python to log real time data:

```
#!/usr/bin/env python

from __future__ import print_function

__description__ = "Program for geiger meter"
__author__ = 'Didier Stevens'
__version__ = '0.0.1'
__date__ = '2024/05/11'

"""

Source code put in the public domain by Didier Stevens, no Copyright
https://DidierStevens.com
Use at your own risk

History:
  2024/05/11: start

Todo:
"""

import optparse
import serial
import time

def FormatTime(epoch=None):
    if epoch == None:
        epoch = time.time()
    return '%04d%02d%02d-%02d%02d%02d' % time.localtime(epoch)[0:6]

def FindCOMPorts():
    ports = []
    for number in range(1, 10):
        try:
            comport = 'COM%d' % number
            with serial.Serial(comport) as oSerial:
                ports.append(comport)
        except serial.serialutil.SerialException as e:
            if 'PermissionError' in e.args[0]:
                ports.append(comport)
    return ports

def LogToCSV(comport):
    ser = serial.Serial(comport, 115200, timeout=0, write_timeout=0)
    ser.write(b'\xAA\x05\x0E\x01\xBE\x55\x00')
    alldata = b''
    fOut = open('geiger.csv', 'a')
    while True:
        data = ser.read(1000)
        if data != b'':
            alldata += data
            lines = alldata.split(b'\xaaU\x0e')
            alldata = lines[-1]
            lines = lines[:-1]
            for line in lines:
                if line != b'':
                    out = FormatTime() + ';' + line.decode('latin')
                    print(out)
                    fOut.write(out + '\n')
            if alldata.endswith(b'U') and not alldata.endswith(b'\xaaU'):
                out = FormatTime() + ';' + alldata.decode('latin')
                print(out)
                fOut.write(out + '\n')
                alldata = b''
            time.sleep(0.40)

def Main():
    oParser = optparse.OptionParser(usage='usage: %prog [options]\n' + __description__ , version='%prog ' + __version__)
    oParser.add_option('-l', '--listports', action='store_true', default=False, help='List ports')
    (options, args) = oParser.parse_args()

    comports = FindCOMPorts()
    if options.listports:
        print('Available ports:')
        for comport in comports:
            print(' %s' % comport)
        return

    if len(args) == 1:
        LogToCSV(args[0])
    elif len(comports) == 1:
        print('Using %s' % comports[0])
        LogToCSV(comports[0])
    else:
        print('Provide the COM port as argument')
        print('Available ports:')
        for comport in comports:
            print(' %s' % comport)

if __name__ == '__main__':
    Main()
```

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/11/22/interfacing-with-a-cheap-geiger-counter/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/programs/yara-rules/)
    - [ZIPEncryptFTP](https://blog.didierstevens.com/programs/zipencryptftp/)
  + [Public Drafts](https://blog.didierstevens.com/public-drafts/)
    - [Cisco Tricks](https://blog.didierstevens.com/public-drafts/cisco-tricks/)
  + [Screencasts & Videos](https://blog.didierstevens.com/screencasts-videos/)
* Search for:
* ## Top Posts

  + [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
  + [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
  + [Quickpost: No Escape From PDF](https://blog.didierstevens.com/2010/06/29/quickpost-no-escape-from-pdf/)
  + [Escape From PDF](https://blog.didierstevens.com/2010/03/29/escape-from-pdf/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
* ## Categories

  + [.NET](https://blog.didierstevens.com/category/net/)
  + [010 Editor](https://blog.didierstevens.com/category/010-editor/)
  + [Announcement](https://blog.didierstevens.com/category/announcement/)
  + [Arduino](https://blog.didierstevens.com/category/arduino/)
  + [Bash Bunny](https://blog.didierstevens.com/category/bash-bunny/)
  + [Beta](https://blog.didierstevens.com/category/beta/)
  + [bpmtk](https://blog.didierstevens.com/category/bpmtk/)
  + [Certification](https://blog.didierstevens.com/category/certification/)
  + [Didier Stevens Labs](https://blog.didierstevens.com/category/didier-stevens-labs/)
  + [Eee PC](https://blog.didierstevens.com/category/eee-p...