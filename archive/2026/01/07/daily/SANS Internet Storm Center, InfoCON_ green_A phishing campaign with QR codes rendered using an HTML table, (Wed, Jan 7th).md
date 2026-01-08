---
title: A phishing campaign with QR codes rendered using an HTML table, (Wed, Jan 7th)
url: https://isc.sans.edu/diary/rss/32606
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-07
fetch_date: 2026-01-08T03:31:00.903961
---

# A phishing campaign with QR codes rendered using an HTML table, (Wed, Jan 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32602)
* [next](/diary/32608)

# [A phishing campaign with QR codes rendered using an HTML table](/forums/diary/A%2Bphishing%2Bcampaign%2Bwith%2BQR%2Bcodes%2Brendered%2Busing%2Ban%2BHTML%2Btable/32606/)

**Published**: 2026-01-07. **Last Updated**: 2026-01-07 09:32:26 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/A%2Bphishing%2Bcampaign%2Bwith%2BQR%2Bcodes%2Brendered%2Busing%2Ban%2BHTML%2Btable/32606/#comments)

Malicious use of QR codes has long been ubiquitous, both in the real world as well as in electronic communication. This is hardly surprising given that a scan of a QR code can lead one to a phishing page as easily as clicking a link in an e-mail.

No more surprising is that vendors of security technologies have, over time, developed mechanisms for detecting and analyzing images containing QR codes that are included in e-mail messages[[1](https://www.proofpoint.com/us/blog/email-and-cloud-threats/malicious-qr-code-detection-takes-giant-leap-forward),[2](https://www.cloudflare.com/learning/security/what-is-quishing/)]. These security mechanisms make QR code-based phishing less viable. However, due to the “cat and mouse” nature of cybersecurity, threat actors continually search for ways of bypassing various security controls, and one technique that can be effective in bypassing QR code detection and analysis in e-mail messages was demonstrated quite well in a recent string of phishing messages which made it into our inbox.

The technique in question is based on the use of imageless QR codes rendered with the help of an HTML table. While it is not new by any stretch[[3](https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20villages/DEF%20CON%2032%20-%20Adversary%20Vilage%20-%20Melvin%20Langvik%20-%20Evading%20Modern%20Defenses%20When%20Phishing%20with%20Pixels.pdf)], it is not too well-known, and I therefore consider it worthy of at least this short post.

Samples of the aforementioned phishing messages I have access to have been sent out between December 22nd and December 26th, and all of them had the same basic layout consisting of only a few lines of text along with the QR code.

[![](https://isc.sans.edu/diaryimages/images/26-01-07-message.png)](https://isc.sans.edu/diaryimages/images/26-01-07-message.png)

Although it looks quite normal (except perhaps for being a little “squished”), the QR code itself was – as we have indicated above – displayed not using an image but rather with the help of an HTML table made up of cells with black and white background colors, as you can see from the following code.

```

<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="180" height="180" align="center">
	<tr height="4">
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#FFFFFF"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		<td width="4" height="4" bgcolor="#000000"></td>
		...
```

Links encoded in all QR codes pointed to subdomains of the domain lidoustoo[.]click, and except for the very first sample from December 22nd, which pointed to onedrive[.]lidoustoo[.]click, all the URLs had the following structure:

```

hxxps[:]//<domain from recipient e-mail><decimal or hexadecimal string>[.]lidoustoo[.]click/<alphanumeric string>/$<recipient e-mail>
```

While the underlying technique of rendering QR codes using HTML tables is – as we’ve mentioned – not new, its appearance in a real-world phishing campaign is a useful reminder that many defensive controls still implicitly rely on assumptions about how malicious content is represented… And these assumptions might not always be correct.

It is also a good reminder that purely technical security controls can never stop all potentially malicious content – especially content that has a socio-technical dimension – and that even in 2026, we will have to continue improving not just the technical side of security, but also user awareness of current threat landscape.

[1] <https://www.proofpoint.com/us/blog/email-and-cloud-threats/malicious-qr-code-detection-takes-giant-leap-forward>
[2] <https://www.cloudflare.com/learning/security/what-is-quishing/>
[3] <https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20villages/DEF%20CON%2032%20-%20Adversary%20Vilage%20-%20Melvin%20Langvik%20-%20Evading%20Modern%20Defenses%20When%20Phishing%20with%20Pixels.pdf>

-----------
Jan Kopriva
[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/A%2Bphishing%2Bcampaign%2Bwith%2BQR%2Bcodes%2Brendered%2Busing%2Ban%2BHTML%2Btable/32606/#comments)

* [previous](/diary/32602)
* [next](/diary/32608)

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