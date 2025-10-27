---
title: Brute-Force ZIP Password Cracking with zipdump.py, (Sun, Jun 18th)
url: https://isc.sans.edu/diary/rss/29948
source: SANS Internet Storm Center, InfoCON: green
date: 2023-06-19
fetch_date: 2025-10-04T11:46:39.683816
---

# Brute-Force ZIP Password Cracking with zipdump.py, (Sun, Jun 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29946)
* [next](/diary/29952)

# [Brute-Force ZIP Password Cracking with zipdump.py](/forums/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy/29948/)

**Published**: 2023-06-18. **Last Updated**: 2023-06-18 10:39:07 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy/29948/#comments)

Gebhard's diary entry "[Brute Forcing Simple Archive Passwords](https://isc.sans.edu/diary/Brute%2BForcing%2BSimple%2BArchive%2BPasswords/29914/)" inspired me to make an update to my [zipdump.py](https://blog.didierstevens.com/2023/06/17/update-zipdump-py-version-0-0-26/) tool to add brute-force password cracking.

[Years ago, I added dictionary password cracking](https://blog.didierstevens.com/2017/05/11/crack-a-zip-password-and-fly-to-dubai/) to zipdump.py (a tool to analyze ZIP files).

Hence adding a brute-force attack mode would be simple.

One can start a zipdump dictionary attack with options -P (passwordfile) or --passwordfilestop. You give it a text file with passwords to try (like rockyou), or you use file name ".", and then it uses a small builtin list (that's [John-the-Ripper public domain password list](https://github.com/magnumripper/JohnTheRipper/blob/bleeding-jumbo/run/password.lst)).

Now, with the latest version, you can start brute-force attack mode with the following special filename: #b#.

This starts a brute-force attack, with password guesses from 1 to 3 characters long, and characters selected from these sets of characters: uppercase and lowercase ASCII letters, digits, all punctuation characters ([Python's definition](https://python.readthedocs.io/en/latest/library/string.html#string.punctuation)) and space character.

When I run this on Gebhard's sample, the password is not recovered:

![](https://isc.sans.edu/diaryimages/images/20230617-162426.png)

![](https://isc.sans.edu/diaryimages/images/20230617-162441.png)

The brute-force attack ran almost at 25.000 password guesses per second on the laptop I tested this on.

Now let's change some parameters. Gebhard found that the password is 4 characters long, and consisted of uppercase letters and digits.

I'm using these parameters: maximum=4,charsets=lud

This starts a brute-force attack of passwords consisting of uppercase and lowercase letters and digits, between 1 and 4 characters long.

![](https://isc.sans.edu/diaryimages/images/20230617-162630.png)

![](https://isc.sans.edu/diaryimages/images/20230617-163554.png)

With these parameters, it took 505 seconds to recover the password: X353.

ZIP files that are encrypted with AES (like the samples you get from Malware Bazaar) requier installation of the pyzipper module and are way slower to crack (less than 2.000 password guesses per second on the same laptop).

Remark that this solution only handles ZIP files, and not all archive types like Gebhard's shell script.

zipdump can also generated false positives. ZIP files that can be openened with a guessed password through the zipfile/pyzipper API, may still throw an error when the full content is actually read:

![](https://isc.sans.edu/diaryimages/images/20230618-095648.png)

![](https://isc.sans.edu/diaryimages/images/20230618-100647.png)

This is something I will fix in an upcoming version.

This dictionary and brute-force password cracking is just a convenience feature for me, to crack simple or popular passwords. For more complex passwords, I use hashcat.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/BruteForce%2BZIP%2BPassword%2BCracking%2Bwith%2Bzipdumppy/29948/#comments)

* [previous](/diary/29946)
* [next](/diary/29952)

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