---
title: A phishing page interested in MX records, (Tue, Nov 17th)
url: https://isc.sans.edu/diary/rss/33526
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-17
fetch_date: 2026-11-18T09:22:37.897048
---

# A phishing page interested in MX records, (Tue, Nov 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33522)

Click HERE to learn more about classes Jan is teaching for SANS

# [A phishing page interested in MX records](/forums/diary/A%2Bphishing%2Bpage%2Binterested%2Bin%2BMX%2Brecords/33526/)

**Published**: 2026-11-17. **Last Updated**: 2026-11-17 10:56:38 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/A%2Bphishing%2Bpage%2Binterested%2Bin%2BMX%2Brecords/33526/#comments)

I’ve mentioned before in some of my diaries that it can be instructive to look at what appear to be “generic” phishing messages in detail from time to time, since some of them might prove not to be as generic as they initially appear. I came across a good example of this while going over phishing messages delivered to our handler inbox over the past few weeks, when a message that, at first glance, appeared to be a fairly ordinary attempt at stealing e-mail credentials turned out to lead to a page interested in collecting a little more information than just the victim's password.

As you can see, the original message was not especially noteworthy on its own, being a spin on the usual “your password will expire today” approach…

[![](https://isc.sans.edu/diaryimages/images/26-11-17-phish.png)](https://isc.sans.edu/diaryimages/images/26-11-17-phish.png)

The link pointed to an HTML page hosted on Google Cloud Storage, with the recipient's e-mail address included in the URL fragment:

hxxps[:]//storage[.]googleapis[.]com/alx2/03/1a/we.html#[recipient\_e-mail\_address]

After opening the link, the recipient would be presented with a generic login form, personalized using the domain part of their e-mail address. The page also attempted to use a screenshot of the legitimate website of the recipient's organization as its background, which it retrieved using the thum.io service. This didn't work quite as intended for isc.sans.edu, since the screenshot service returned an error message instead of the requested image. However, when I modified the URL to contain an e-mail address from another domain, the resulting page looked considerably more convincing.

[![](https://isc.sans.edu/diaryimages/images/26-11-17-site1.png)](https://isc.sans.edu/diaryimages/images/26-11-17-site1.png)

[![](https://isc.sans.edu/diaryimages/images/26-11-17-site2.png)](https://isc.sans.edu/diaryimages/images/26-11-17-site2.png)

Looking at the source code revealed a couple of layers of URL-encoding and additional JavaScript obfuscation. Once these were removed, the page turned out to contain a fairly typical credential-harvesting kit, which supported multiple languages and attempted to collect not just the submitted password, but also the visitor's public IP address, geographic location, browser information and language. This information, along with a timestamp, was supposed to be sent to the attacker using the Telegram Bot API.

Such extensive collection of information is not particularly unusual. In fact, another phishing page that I examined recently collected a similarly extensive set of information and also sent it to the attacker using Telegram. In the present case, however, one additional field included in the information sent to the attacker caught my attention – it was labeled "MX Record".

A closer look at the corresponding code revealed that the JavaScript actually performed a DNS-over-HTTPS query for MX records associated with the victim's e-mail domain, using Google's public DNS service. The relevant parts of the code (slightly simplified and reformatted for readability) looked as follows:

```

...
const response = await fetch(
    "https://dns.google/resolve?name=" + domain + "&type=MX"
);
const data = await response.json();
return data.Answer.map(answer => answer.data).join("\n");
...
```

The retrieved records were then included in the message containing the stolen credentials:

```

...
message += "MX Record : " + await getMXRecord(domain) + "\n";
...
```

The use of MX records in phishing is certainly not new. For example, Infoblox documented a phishing-as-a-service operation called Morphing Meerkat in March 2025, which used DNS-over-HTTPS queries for MX records to identify victims' e-mail service providers and dynamically select appropriate phishing templates[[1](https://www.infoblox.com/blog/threat-intelligence/a-phishing-tale-of-doh-and-dns-mx-abuse/)].

In the present case, however, the MX records weren't used to customize the phishing page. Instead, the lookup was performed as part of the credential collection process, and its results were included in the information sent to the attacker.

Of course, MX records are publicly available, and there is nothing preventing an attacker from looking them up independently. Nevertheless, including them with each set of stolen credentials would help the attacker automatically identify the e-mail infrastructure used by the targeted organization, which could be useful for further attacks or for prioritizing the collected credentials.

Whether the threat actor behind this particular phishing actually used the collected MX records in this (or any) way is impossible to say. Still, having the phishing page perform a little additional reconnaissance on the victim's organization, and including the results with the stolen credentials, seems like a noteworthy detail in an otherwise fairly ordinary phishing kit…

[1] <https://www.infoblox.com/blog/threat-intelligence/a-phishing-tale-of-doh-and-dns-mx-abuse/>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [DNS](/tag.html?tag=DNS) [Phishing](/tag.html?tag=Phishing)

[0 comment(s)](/diary/A%2Bphishing%2Bpage%2Binterested%2Bin%2BMX%2Brecords/33526/#comments)

Click HERE to learn more about classes Jan is teaching for SANS

* [previous](/diary/33522)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)