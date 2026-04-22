---
title: A .WAV With A Payload, (Tue, Apr 21st)
url: https://isc.sans.edu/diary/rss/32910
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-21
fetch_date: 2026-04-22T04:45:04.915117
---

# A .WAV With A Payload, (Tue, Apr 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32904)
* [next](/diary/32914)

Click HERE to learn more about classes Didier is teaching for SANS

# [A .WAV With A Payload](/forums/diary/A%2BWAV%2BWith%2BA%2BPayload/32910/)

**Published**: 2026-04-21. **Last Updated**: 2026-04-21 07:14:56 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/A%2BWAV%2BWith%2BA%2BPayload/32910/#comments)

There have been reports of threat actors using a [.wav file as a vector for malware](https://www.bleepingcomputer.com/news/security/backdoored-telnyx-pypi-package-pushes-malware-hidden-in-wav-audio/).

It's a proper .wav file, but they didn't use staganography. The .wav file will play, but you'll just hear noise:

![](https://isc.sans.edu/diaryimages/images/20260419-100007.png)

That's because the TAs have just replaced the bytes that encode the sound with the BASE64 representation of their payload:

![](https://isc.sans.edu/diaryimages/images/20260419-100220.png)

Thus I don't need a .wav parser to extract the encoded payload, I can just use my [base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py) tool:

![](https://isc.sans.edu/diaryimages/images/20260419-100408.png)

The BASE64-decoded payload is an XOR-encoded PE file. So I don't need to make a custom decoder, I can just perform a known-plaintext attack looking for the DOS header with my [xor-kpa.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xor-kpa.py) tool:

![](https://isc.sans.edu/diaryimages/images/20260419-100857.png)

The XOR key was found. Thus we can easily dump the decoded PE file and see the MZ header at position 0x08 and a bit further down the DOS header we used in the known-plaintext-attack:

![](https://isc.sans.edu/diaryimages/images/20260419-102311.png)

And my tool [pecheck.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pecheck.py) can extract an analyse the [sample](https://www.virustotal.com/gui/file/a0a8857e8a65c05778cf6068ad4c05ec9b6808990ae1427e932d2989754c59a4/detection):

![](https://isc.sans.edu/diaryimages/images/20260419-101916.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/A%2BWAV%2BWith%2BA%2BPayload/32910/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/32904)
* [next](/diary/32914)

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