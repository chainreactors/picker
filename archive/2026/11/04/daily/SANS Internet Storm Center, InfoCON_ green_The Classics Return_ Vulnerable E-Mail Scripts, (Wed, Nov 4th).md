---
title: The Classics Return: Vulnerable E-Mail Scripts, (Wed, Nov 4th)
url: https://isc.sans.edu/diary/rss/33488
source: SANS Internet Storm Center, InfoCON: green
date: 2026-11-04
fetch_date: 2026-11-05T08:45:08.344445
---

# The Classics Return: Vulnerable E-Mail Scripts, (Wed, Nov 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33482)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [The Classics Return: Vulnerable E-Mail Scripts](/forums/diary/The%2BClassics%2BReturn%2BVulnerable%2BEMail%2BScripts/33488/)

**Published**: 2026-11-04. **Last Updated**: 2026-11-04 13:24:13 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[2 comment(s)](/diary/The%2BClassics%2BReturn%2BVulnerable%2BEMail%2BScripts/33488/#comments)

One of the early web application vulnerabilities I remember was CVE-2000-0411 [CVE]. This was a simple vulnerability in a CGI-bin script used to send e-mail. The vulnerability was pretty straightforward: Adding additional parameters to the URL leaked environment variables. Other vulnerabilities allowed setting the "To" address and were heavily abused by spammers. And if parameters were passed directly to the sendmail binary, similar vulnerabilities could allow arbitrary code execution.

Today, I noticed a slight resurgence in scans targeting e-mail scripts on our honeypots. Today, there are numerous scripts like the old "formail" scripts, and it is hard to link a specific vulnerability to any of these scans. But my main suspect is spammers looking for webforms that allow setting arbitrary "To" headers. The URLs I am seeing:

> `"/sendmail.php"
> "/test-mail.php"
> "/testemail.php"
> "/config/mail_config.php"
> "/mail_config.php"
> "/email-test.php"
> "/mailtest.php"`

In particular, the "Test" part of the filename suggests that the attacker is not looking for production scripts, but for test scripts left behind during development. This, along with the requests for credential/secret files that top our "Leaderboard," points to a more fundamental issue: Code hygiene. Do not leave behind development artifacts that should never have reached a live website.

For example, some excerpts from a random "mailtest.php" script that came back in a Google search [mailtest]:

> `<?php`
>
> `/*
>     DONT FORGET TO DELETE THIS SCRIPT WHEN FINISHED!
>     */`
>
> `$server = array(
>         'HTTP_HOST', 'SERVER_NAME', 'SERVER_ADDR', 'SERVER_PORT',
>          'SERVER_ADMIN', 'SERVER_SIGNATURE', 'SERVER_SOFTWARE',
>         'REMOTE_ADDR', 'DOCUMENT_ROOT', 'REQUEST_URI',
>         'SCRIPT_NAME', 'SCRIPT_FILENAME',
>     );
>
>     $to      = ( isset( $_GET['email'] ) ? $_GET['email'] : FALSE );
>     $subject = 'Mail Test Successful for ' . $_SERVER['HTTP_HOST'];
>     $message = '';`
>
> `![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-11-04%20at%208_22_06%E2%80%AFAM.png)???????    foreach ( $server as $s )
>     {
>         $message .= sprintf( '%s: %s', $s, $_SERVER[$s] ) . PHP_EOL;
>     };`
>
> `$success = mail( $to, $subject, $message, $headers );`

The comment at the top says it all: This is not meant for production use, and even on a development site, it should likely be deployed only briefly for debugging. The script takes any "To" address from the "email" GET parameter and exfiltrates/displays part of the server configuration. It can be useful to scan your own hosts for some of these URLs as an additional control, but you really want to catch these issues during application deployment.

[CVE] https://nvd.nist.gov/vuln/detail/cve-2000-0411
[mailtest] https://gist.github.com/Porrapat/60ed7411d933122fc481

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [test](/tag.html?tag=test) [mail](/tag.html?tag=mail)

[2 comment(s)](/diary/The%2BClassics%2BReturn%2BVulnerable%2BEMail%2BScripts/33488/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33482)

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