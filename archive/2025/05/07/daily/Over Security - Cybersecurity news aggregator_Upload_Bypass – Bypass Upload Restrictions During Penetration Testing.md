---
title: Upload_Bypass – Bypass Upload Restrictions During Penetration Testing
url: https://www.darknet.org.uk/2025/05/upload_bypass-bypass-upload-restrictions-during-penetration-testing/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-07
fetch_date: 2025-10-06T22:28:44.850302
---

# Upload_Bypass – Bypass Upload Restrictions During Penetration Testing

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Upload\_Bypass – Bypass Upload Restrictions During Penetration Testing

May 5, 2025

Views: 1,035

**Upload\_Bypass** is a command-line tool that automates discovering and exploiting weak file upload filters. If you’re tired of manually renaming extensions and tweaking payloads by hand, this tool does the dirty work.

![Upload_Bypass - Bypass Upload Restrictions During Penetration Testing](https://www.darknet.org.uk/wp-content/uploads/2025/05/Upload_Bypass-Bypass-Upload-Restrictions-During-Penetration-Testing-640x322.png)

File upload restrictions are one of the last lines of defence in many web apps and one of the most misunderstood.

Some developers rely on MIME type checks. Others try to validate file extensions. A few go the extra mile with content inspection. But as any decent pentester knows, **there’s almost always a way in.**

---

## What Is Upload\_Bypass?

Upload\_Bypass is a Python-based tool built by [sAjibuu](https://github.com/sAjibuu) that helps bypass file upload protections commonly seen in CTFs, bug bounty targets, and poorly configured web apps.

Instead of endlessly trying variations like `shell.php`, `shell.php5`, or `shell.jpg.php`, you can throw your file at Upload\_Bypass and let it rip through **automated filter evasion techniques**, including:

* Filename and extension variations
* MIME type spoofing
* Header manipulation
* Extension appending (.jpg;.php)
* Uploading polyglot files (e.g. image + PHP)

---

## Why This Matters

Improper file upload validation is one of the most **common paths to remote code execution (RCE)**.
Once you can smuggle a malicious file onto a server, you’ve got the ability to:

* Drop webshells
* Execute arbitrary code
* Establish persistence
* Escalate privilege (depending on misconfig)

It’s one of the highest-ROI vulnerabilities in both offensive security and bug bounty hunting.

---

## Features

* Automatically tests multiple **upload bypass payloads**
* Supports common web extensions (`.php`, `.asp`, `.jsp`, `.html`)
* Smart payload renaming and MIME spoofing
* Verbose output to show what worked and what didn’t
* Designed for **CTF players**, **bug bounty hunters**, and **red teamers**
* Clean and hackable Python source

---

## Installation

Simple setup on any system with Python 3:

git clone https://github.com/sAjibuu/Upload\_Bypass.git
cd Upload\_Bypass
pip install -r requirements.txt
python3 Upload\_Bypass.py

|  |  |
| --- | --- |
| 1  2  3  4 | git clone https://github.com/sAjibuu/Upload\_Bypass.git  cd Upload\_Bypass  pip install -r requirements.txt  python3 Upload\_Bypass.py |

## Example Usage

Upload\_Bypass is interactive. You’ll be prompted to:

* Select the file you want to upload
* Choose the output folder
* Pick target extension (e.g. `.php`)
* Specify the platform (`web`, `mobile`, `ctf`, etc.)

Usage options:

Usage: Upload Bypass &#91;OPTIONS]
Options:
-h, --help Print help (see more with '--help')
-U, --usage Print the how to save the request file instructions.
-v, --version Print version
Required Arguments:
-r, --request\_file &lt;REQUEST\_FILE> Provide a request file to be proccessed
-E, --extension &lt;EXTENSION> Forbidden extension to check (ex: php)
-A, --allowed &lt;EXTENSION> Allowed extension (ex: jpeg) - Optional - if not set the program will auto-detect the extension
Choose only one from the options below:
-s, --success &lt;MESSAGE> Provide a success message when a file is uploaded (ex: File was uploaded successfully)
-f, --failure &lt;MESSAGE> Provide a failure message when a file is uploaded (ex: File is not allowed!)
-S, --status\_code &lt;STATUS\_CODE> Provide a status code for a success upload (ex: 200)
Mode Settings:
-d, --detect Upload harmless sample files (Suitable for a real penetration test)
-e, --exploit Upload Web-Shells files when testing
-a, --anti\_malware Upload Anti-Malware Test file (Eicar) when testing
I. If set with -E flag the program will test with the Eicar string along with the choosen extension
II. If set without the -E flag the program will test with Eicar string and a com extension
Modules Settings:
-l, --list List all modules
-i, --include\_only &lt;MODULES> Include only modules to test from (ex: extension\_shuffle, double\_extension)
-x, --exclude &lt;MODULES> Exclude modules (ex: svg\_xxe, svg\_xss)
Request Settings:
--base64 Encode the file data with Base64 algorithm
--allow\_redirects Follow redirects
-P, --put Use the HTTP PUT method for the requests (Default is POST)
-Pa, --patch Use the HTTP Patch method for the requests (Default is POST)
-R, --response Print the response to the screen
-c, --continue Continue testing all files, even if a few uploads encountered success
-t, --time\_out &lt;NUM> Set the request timeout (Default is 8)
-rl, --rate\_limit &lt;NUMBER> Set a rate-limit with a delay in milliseconds between each request
Proxy Settings:
-p, --proxy &lt;PROXY> Proxy to use for requests (ex: http(s)://host:port, socks5(h)://host:port)
-k, --insecure Do not verify SSL certificates
--burp\_http Set --proxy to 127.0.0.1:8080 and set --insecure to true (For HTTP requests)
--burp\_https Set --proxy to 127.0.0.1:8080 and set --insecure to false (For HTTPs requests)
Optional Settings:
-D, --upload\_dir &lt;UPLOAD\_DIR> Provide a remote path where the Web-Shell should be uploaded (ex: /uploads)
-o, --output &lt;OUTPUT\_PATH> Output file to write the results into - Default current directory (ex: ~/Desktop/results.txt)
--debug &lt;NUM> Debug mode - Print the stack trace error to the screen and save it to a file (ex: --debug 1)
I. Level 1 - Saves only the stack trace error (default).
II. Level 2 - Saves the stack trace error and user's arguments along with the request file.
Resume settings:
--resume &lt;STATE\_FILE> State file from which to resume a partially complete scan
Update settings:
-u, --update Update the program to the latest version

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57 | Usage: Upload Bypass &#91;OPTIONS]    Options:  -h, --help     Print help (see more with '--help')  -U, --usage   Print the how to save the request file instructions.  -v, --version  Print version    Required Arguments:  -r, --request\_file &lt;REQUEST\_FILE>    Provide a request file to be proccessed  -E, --extension    &lt;EXTENSION>       Forbidden extension to check (ex: php)  -A, --allowed      &lt;EXTENSION>       Allowed extension (ex: jpeg) - Optional - if not set the program will auto-detect the extension    Choose only one from the options below:  -s, --success      &lt;MESSAGE>         Provide a success message when a file is uploaded (ex: File was uploaded successfully)  -f, --failure      &lt;MESSAGE>         Provide a failure message when a file is uploaded (ex: File is not allowed!)  -S, --status\_code  &lt;STATUS\_CODE>     Provide a status cod...