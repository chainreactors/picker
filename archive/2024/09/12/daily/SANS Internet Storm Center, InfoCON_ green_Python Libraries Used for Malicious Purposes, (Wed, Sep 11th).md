---
title: Python Libraries Used for Malicious Purposes, (Wed, Sep 11th)
url: https://isc.sans.edu/diary/rss/31248
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-12
fetch_date: 2025-10-06T18:31:29.939993
---

# Python Libraries Used for Malicious Purposes, (Wed, Sep 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31242)
* [next](/diary/31250)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python Libraries Used for Malicious Purposes](/forums/diary/Python%2BLibraries%2BUsed%2Bfor%2BMalicious%2BPurposes/31248/)

**Published**: 2024-09-11. **Last Updated**: 2024-09-11 06:36:28 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Python%2BLibraries%2BUsed%2Bfor%2BMalicious%2BPurposes/31248/#comments)

Since I’m interested in malicious Python scripts, I found multiple samples that rely on existing libraries. The most-known repository is probably pypi.org[[1](https://pypi.org/)] that reports, as of today, 567,478 projects! Malware developers are like regular developers: They don’t want to reinvent the wheel and make their shopping across existing libraries to expand their scripts capabilities.

I compiled a list of libraries that are often used by malicious scripts. Warning! These libraries are NOT malicious, they are also used for totally legit purposes. Like many Windows API calls, they are just (ab)used by developers. Here is my top list:

| Module | Description |
| --- | --- |
| pyWinhook | Python wrapper for out-of-context input hooks in Windows. The pyWinhook package provides callbacks for global mouse and keyboard events in Windows. Python applications register event handlers for user input events such as left mouse down, left mouse up, key down, etc. and set the keyboard and/or mouse hook. |
| pyperclip | Pyperclip is a cross-platform Python module for copy and paste clipboard functions. |
| psutil | psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. |
| win32gui | Python extensions for Microsoft Windows’ Provides access to much of the Win32 API, the ability to create and use COM objects, and the Pythonwin environment |
| win32process | An interface to the win32 Process and Thread API's |
| pythoncom | This module supports the Microsoft Component Object Model (COM). COM is a technology that allows you to use “objects” from your favorite language, even if the object isn’t implemented in your language. Many applications for Windows (including Microsoft Office) can be controlled using COM, making it particularly suitable for scripting-related tasks. |
| tkinter | This module provides the standard Python interface to the Tcl/Tk GUI toolkit. It is used to design and display GUI elements in some malicious scripts to simulate a player or a small game. |
| ctypes | This module is a "foreign function library". It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to interact with any Windows API calls. Often used for code injection. |
| winreg | This module integrates with the Windows registry and can read/write keys. |
| ftplib | Easy implementation of the FTP protocol to exfiltrate data or download next stages. |
| discord | This module helps to integrate with a Discord servers. Often used as a C2 protocol. |
| pyautogui | scripts control the mouse and keyboard to automate interactions with other applications. |
| PIL | The Python Imaging Library adds image processing capabilities to your Python interpreter. |
| getpass | Portable password input but provides getpass.getuser() to retrieve information about the current user. |
| faker | *Faker* is a Python package that generates fake data for you. Whether you need to bootstrap your database, create good-looking XML documents, fill-in your persistence to stress test it, or anonymize data taken from a production service, Faker is for you. |
| cloudscraper | A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM), implemented with Requests. Cloudflare changes their techniques periodically, so I will update this repo frequently. |
| fernet | Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. |
| qrcode | This modules manages (generates) QR codes. |
| secrets | The secrets module is used for generating random numbers for managing important data such as passwords, account authentication, security tokens, and related secrets, that are cryptographically strong. |
| smtplib | Easy implementation of the SMTP protocol to exfiltrate data. |
| pytesseract | Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images. |
| telebot | Helps to create a Telegram bot |
| telethon | Talks to Telegram |
| pyinput | This library allows you to control and monitor input devices.  Currently, mouse and keyboard input and monitoring are supported. |
| win32api | Helps to call Win32 API |
| wmi | Provides an interface to the Windows Management Instrumentation framework |
| win32crypt | Provides an interface to the win32 Cryptography API |
| wave | Provides an interface to the Waveform Audio “WAVE” (or “WAV”) file format. |
| sounddevice | Provides bindings for the PortAudio library and a few convenience functions to play and record NumPy arrays containing audio signals. Combined with the wave module (see above) it helps to use the microphone and exfiltrate conversations. |
| pythonnet | Embeds .Net into Python. |
| dropbox | Used to exfiltrate data via Dropbox. |
| win32pdh | Used to encapsulate the Windows Performance Data Helpers API[[2](https://learn.microsoft.com/en-us/windows/win32/perfctrs/using-the-pdh-functions-to-consume-counter-data)] and perform a footprint of the targeted computer (ex: user's activity) |
| py7zr | Used to manipulate 7Z archives and exfiltrate collected data. |
| pyzipper | Used to manipulate ZIP archives and exfiltrate collected data. |
| browser\_cookie3 | This module loads cookies used by your web browser into a cookie jar object. Often used by infostealers. |
| browser\_history | Simple python package used o retrieve (almost) any browser's history on (almost) any platform. Like the previous module, used by infostealers. |
| marshal | This modules ontains functions that can read and write Python values in a binary format. Used for obfuscation purposes. |
| py\_compile | This module generates a byte-code file from a source file. This is used as obfuscation technique. Once compiled, the initial script is deleted. |
| firebase\_admin | Used to integrate Firebase into scripts. This is often used for easy exfiltration of data. |

If not available on the victim's computer, these modules can be easily installed using a few lines of code:

```

import time
from sys import executable

required_modules = [ "module1", "module2", "moduleN" ]
for m in required_modules:
    try:
        import m
    except:
        subprocess.Popen(f"\"{executable}\" -m pip install {m} --quiet", shell=True)
        time.sleep(3)
```

If you discover more Python libraries sometimes used for malicious reasons, please share! I'd like to keep this list up-to-date!

[1] <https://pypi.org/>
[2] <https://learn.microsoft.com/en-us/windows/win32/perfctrs/using-the-pdh-functions-to-consume-counter-data>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Python](/tag.html?tag...