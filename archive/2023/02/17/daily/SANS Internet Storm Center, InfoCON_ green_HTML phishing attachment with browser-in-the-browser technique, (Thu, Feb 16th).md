---
title: HTML phishing attachment with browser-in-the-browser technique, (Thu, Feb 16th)
url: https://isc.sans.edu/diary/rss/29556
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-17
fetch_date: 2025-10-04T06:54:44.241727
---

# HTML phishing attachment with browser-in-the-browser technique, (Thu, Feb 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29552)
* [next](/diary/29560)

# [HTML phishing attachment with browser-in-the-browser technique](/forums/diary/HTML%2Bphishing%2Battachment%2Bwith%2Bbrowserinthebrowser%2Btechnique/29556/)

**Published**: 2023-02-16. **Last Updated**: 2023-02-16 11:25:31 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/HTML%2Bphishing%2Battachment%2Bwith%2Bbrowserinthebrowser%2Btechnique/29556/#comments)

Although the browser-in-the-browser (BitB) technique has been with us for a while now[[1](https://mrd0x.com/browser-in-the-browser-phishing-attack/)], it is far from what one might call ubiquitous. Simply put, the technique is based on displaying a simulated browser pop-up window (usually a login prompt) within the confines of an HTML page opened in a browser. The simulated pop-up may look almost indistinguishable from a real browser window and since it may contain an arbitrary URL in the simulated address bar, the use of the BitB technique for phishing can be quite effective, as most people have been repeatedly taught that they should “check the URL, and if it is the right one, the page should be genuine” during security awareness courses.

![](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-2.png)

Checking the URL is undoubtedly still a good advice, however, when it comes to BitB, one should probably preface it by saying, that one first has to make sure that a browser window is actually a real browser window and that its address bar is actually a real address bar… Unlike in the example shown in the following image.

[![](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-1.png)](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-1.png)

Even though the BitB technique has been repeatedly used by threat actors in the wild in targeted attacks[[2](https://blog.google/threat-analysis-group/tracking-cyber-activity-eastern-europe/),[3](https://www.darkreading.com/attacks-breaches/steam-gaming-phish-showcases-browser-in-browser-threat)], it hasn’t so far become the “default go to” for authors of phishing websites... Which is why I was a little surprised to find a generic phishing e-mail with an HTML attachment using this technique in my spam trap last week.

The e-mail itself had an empty body and – besides the fact that it originated from a SendGrid server, which seems to be used by the legitimate owner of the domain, and thus passed both SPF and DKIM checks – was completely uninteresting.

[![](https://isc.sans.edu/diaryimages/images/23-02-16-mail.png)](https://isc.sans.edu/diaryimages/images/23-02-16-mail.png)

At a first glance, the attachment looked just as uninteresting and run-of-the-mill as the e-mail itself.

[![](https://isc.sans.edu/diaryimages/images/23-02-16-html.png)](https://isc.sans.edu/diaryimages/images/23-02-16-html.png)

However, on a closer look, it proved to use the BitB technique to display fake pop-up login prompts if one of 5 of the 6 login options were selected. The displayed pop-ups looked somewhat convincing and behaved to a limited extent (it was possible to move them around on the screen, but not to resize/minimize/maximize them in any way) similarly to how real pop-ups would.

[![](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-2.png)](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-2.png)

The code behind the HTML attachment turned out to be notable in two ways – first, it wasn’t obfuscated, which is quite unusual these days for HTML phishing attachments, and second, the sections of code used to display and control the pop-ups weren’t the same for all windows and, in a strange turn of events, didn’t contain the same functionality.

As a result, only the login pop-up for O365/Outlook (which, as you may see, tried to load images from external site that were no longer available at the time of writing) performed any animation when one hovered a mouse cursor over the minimize, maximize and close buttons on its top bar. All other simulated pop-up windows were completely unresponsive to such interaction.

[![](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-3.png)](https://isc.sans.edu/diaryimages/images/23-02-16-bitb-3.png)

As we already mentioned, the use of BitB in phishing is currently not yet as common as are some other techniques. And though this is quite fortunate, one can reasonably expect the situation to change, as there is no reason why threat actors wouldn’t use the technique more, given its potential effectiveness… Or, rather, as the example described above shows, the situation is slowly changing already.

Therefore, one recommendation that can be made to any security professionals out there, who are responsible for building security awareness within their organizations, would be to include a mention of the browser-in-the-browser technique in any educational/awareness materials their organizations might use for employee/end-user training, along with some pointers on how to spot the use of BitB. The most straightforward method for identifying BitB windows would probably be to try to move the pop-up outside of the parent browser window, but the lack of an icon for the pop-up window on a taskbar or possible issues with interactivity of the pop-up window might be good points to mention as well…

[1] <https://mrd0x.com/browser-in-the-browser-phishing-attack/>
[2] <https://blog.google/threat-analysis-group/tracking-cyber-activity-eastern-europe/>
[3] <https://www.darkreading.com/attacks-breaches/steam-gaming-phish-showcases-browser-in-browser-threat>

-----------
Jan Kopriva
[@jk0pr](https://twitter.com/jk0pr)
[Nettles Consulting](https://www.nettles.cz/)

Keywords: [Phishing](/tag.html?tag=Phishing) [HTML](/tag.html?tag=HTML) [Browser in the browser](/tag.html?tag=Browser in the browser)

[0 comment(s)](/diary/HTML%2Bphishing%2Battachment%2Bwith%2Bbrowserinthebrowser%2Btechnique/29556/#comments)

* [previous](/diary/29552)
* [next](/diary/29560)

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