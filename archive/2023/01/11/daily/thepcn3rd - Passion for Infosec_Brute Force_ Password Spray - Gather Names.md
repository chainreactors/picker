---
title: Brute Force: Password Spray - Gather Names
url: https://thepcn3rd.blogspot.com/2023/01/brute-force-password-spray-gather-names.html
source: thepcn3rd - Passion for Infosec
date: 2023-01-11
fetch_date: 2025-10-04T03:35:00.308804
---

# Brute Force: Password Spray - Gather Names

# [thepcn3rd - Passion for Infosec](https://thepcn3rd.blogspot.com/)

Twitter: @lokut
This blog is for educational purposes only. The opinions expressed in this blog are my own and do not reflect the views of my employers.

## Monday, January 9, 2023

### Brute Force: Password Spray - Gather Names

For the Orange Attack Path in the IT420 course I challenged the students to gather the names from the home page of a provided website.  The below script was built to gather what resembles a first and last name like "Bob Smith" or "Bob. A. Smith".  The output of this script can be saved and then used to pull out the names that were found.

```
#!/usr/bin/python3

import requests
import re

# Use the below to supress the warnings due to not verifying the SSL/TLS certs
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def saveWebPage(urls, fileName):
    for url in urls:
        r = requests.get(url,verify=False)
        with open(fileName,'a') as f:
            #print(r.content)
            f.write(r.text)

def extractNames(fileName):
    nameList = []
    with open(fileName, 'r') as f:
        for line in f:
            firstLastName = re.findall(r"[A-Z][a-z]+\s[A-Z][a-z]+", line)
            firstMLastName = re.findall(r"[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+", line)
            if len(firstLastName) > 0:
                for i in firstLastName:
                    if i not in nameList:
                        nameList.append(i)
            if len(firstMLastName) > 0:
                for i in firstMLastName:
                    if i not in nameList:
                        nameList.append(i)
    for name in nameList:
        print(name)

def main():
    urls = ["https://www.website.web", "https://www.website.web/about"]
    fileName = "output.html"
    saveWebPage(urls, fileName)
    extractNames(fileName)
```

Then after you create a userlist from the above output you can use the following script to create a list that can be used in the password spray.  Only conduct this on the web application provided for testing.

```
#!/usr/bin/python3

import sys
import getopt

# Example execution
# ./buildList.py -i userlist.txt -d windomain.local

def main():
    inputfile = ''
    # Read the argument for the userlist file and the domain to append
    if len(sys.argv) < 2:
        print('./buildList.py -i --userlist-- -d --domain--')
        exit(1)
    else:
        argv = sys.argv[1:]
        opts, argv = getopt.getopt(argv,"i:d:")
        for opt, arg in opts:
            if opt in ['-i']:
                inputfile = arg
            if opt in ['-d']:
                domain = arg
        # Read in the file from the command line options...
        with open(inputfile) as f:
            for line in f:
                firstname, lastname = line.split(" ")
                firstname = firstname.lower()
                lastname = lastname.lower().strip()
                # first.last
                print(firstname + "." + lastname + "@" + domain)
                # first_last
                print(firstname + "_" + lastname + "@" + domain)
                # f.last
                print(firstname[0:1] + "." + lastname + "@" + domain)
                # first.l
                print(firstname + "." + lastname[0:1] + "@" + domain)

if __name__ == '__main__':
    main()
```

The below script is a method to develop a password list that can be used for the lab.

```
#!/usr/bin/python3

# Building a password list of common helpdesk passwords of 2022
# Not meant for password sprays due to account lockout thresholds if they are set

season = ["Fall", "Winter", "Spring", "Summer"]
year = ["2021", "2022", "2023"]
commonSpecialChars = ["!", "@", "#", "$"]
#for a in season:
#    for b in year:
#        for c in commonSpecialChars:
#            print(a + b + c)
[print(a+b+c) for a in season for b in year for c in commonSpecialChars]
```

at
[January 09, 2023](https://thepcn3rd.blogspot.com/2023/01/brute-force-password-spray-gather-names.html "permanent link")

[![](https://resources.blogblog.com/img/icon18_edit_allbkg.gif)](https://www.blogger.com/post-edit.g?blogID=450247628992736477&postID=1669563849413889031&from=pencil "Edit Post")

[Email This](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=1669563849413889031&target=email "Email This")[BlogThis!](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=1669563849413889031&target=blog "BlogThis!")[Share to X](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=1669563849413889031&target=twitter "Share to X")[Share to Facebook](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=1669563849413889031&target=facebook "Share to Facebook")[Share to Pinterest](https://www.blogger.com/share-post.g?blogID=450247628992736477&postID=1669563849413889031&target=pinterest "Share to Pinterest")

#### No comments:

#### Post a Comment

[Newer Post](https://thepcn3rd.blogspot.com/2023/01/setup-crontab-for-www-data.html "Newer Post")

[Older Post](https://thepcn3rd.blogspot.com/2021/11/simple-php-listener-on-udp-10000.html "Older Post")
[Home](https://thepcn3rd.blogspot.com/)

Subscribe to:
[Post Comments (Atom)](https://thepcn3rd.blogspot.com/feeds/1669563849413889031/comments/default)

### [Test Authentication from Linux Console using python3 pexpect](https://thepcn3rd.blogspot.com/2023/01/test-authentication-from-linux-console.html)

Working with the IT420 lab, you will discover that we need to discover a vulnerable user account.  The following python3 script uses the pex...

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYibk9C-SKPTd_Dxp0JFHv9abAT_RTwNOMLheOB5Bw0O5fRzu_kWE-JSDpDn4gnP49i74gKT6UiOyUHPjFdntq335wsNs8M9B_NFms1725AYh2k7B2I3-sTsMxtqh45Uq0hiz24m8W8wI/w72-h72-p-k-no-nu/Selection_016.png)](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-getboo-walkthrough.html)

  [OWASP Broken Web Apps - GetBoo Walkthrough](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-getboo-walkthrough.html)

  Here is a quick walk through of GetBoo.  The first item that I found was you can harvest the usernames of the existing users that are regist...
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgo8fg35w1-49ORqz0aLkEnSJvZZhEGpot4h552dq_D0KLtpKLs5AO_tthgUHnKoPV8G36Z840qPox06iz6jvFKum-Cvk4kcSiCJ9tdO9ZMSeHEmt5FcrV_sTK_wITnit5bm9aXKFkL4Aw/w72-h72-p-k-no-nu/Selection_025.png)](https://thepcn3rd.blogspot.com/2015/04/07-of-ip-addresses-continue-to-be.html)

  [0.7% or 311,026 IP Addresses found continue to be vulnerable to Heartbleed](https://thepcn3rd.blogspot.com/2015/04/07-of-ip-addresses-continue-to-be.html)

  As I was glancing through the logs of my honeypots I spent some time to look at the following logs.  In the past I have just overlooked them...
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhPqelQvMM6tetp3p0adCVe70liwYlI96lXKnVTJBicB9MawstZDwbvYBSAmURF3PBqgNG2Wa3BiGhiKnC0UGcHR1W93TzCdeaEBXqIWL1PvsQZu5noB-Q_NL-SQzoEM0xOAXZl4nPbgo/w72-h72-p-k-no-nu/Selection_006.png)](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-broken-wordpress.html)

  [OWASP Broken Web Apps - Broken Wordpress Walkthrough](https://thepcn3rd.blogspot.com/2015/04/owasp-broken-web-apps-broken-wordpress.html)

  I thought I would work through a few of these web applications provided by OWASP on their broken web applications VM. The first one I th...
* [What's in the honeypot? Frequency of SSH Login Attempts based on Country of Origin](https://thepcn3rd.blogspot.com/2015/04/whats-in-honeypot-frequency-of-ssh.html)

  Today looking at the logs of the honeypots, I became curious based on the whois of the IP Addresses attempting to login to SSH which country...
* [Using masscan with a configuration file](https://thepcn3rd.blogspot.com/2015/11/using-masscan-with-configuration-file.html)

  Recently ...