---
title: Evil MSI Background: BASE64 Statistical Analysis, (Mon, Jun 15th)
url: https://isc.sans.edu/diary/rss/33072
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-15
fetch_date: 2026-06-16T07:16:52.729732
---

# Evil MSI Background: BASE64 Statistical Analysis, (Mon, Jun 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33068)
* [next](/diary/33080)

Click HERE to learn more about classes Didier is teaching for SANS

# [Evil MSI Background: BASE64 Statistical Analysis](/forums/diary/Evil%2BMSI%2BBackground%2BBASE64%2BStatistical%2BAnalysis/33072/)

**Published**: 2026-06-15. **Last Updated**: 2026-06-15 07:16:00 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Evil%2BMSI%2BBackground%2BBASE64%2BStatistical%2BAnalysis/33072/#comments)

I like it when a fellow handler posts a diary entry about images with malicious content. Last one is Xavier: "[The Evil MSI Background is Back!](https://isc.sans.edu/diary/The%20Evil%20MSI%20Background%20is%20Back%21/33054)".

I like to have a go at the sample with my tools, and see if there are any improvements I can make to my tools.

Let's take a look at the bytes present in this suspicious JPEG file, using my tool [byte-stats.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/byte-stats.py):

![](https://isc.sans.edu/diaryimages/images/20260611-192621.png)

The results: almost half of the content (45.65%) is BASE64 characters, and the longest BASE64 string is 1000 characters.

And the longest string is almost 1 million characters long.

Let's take a look with [base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py):

![](https://isc.sans.edu/diaryimages/images/20260611-192927.png)

The longest BASE64 string is indeed 1000 characters long but doesn't seem to decode to something recognizable.

A special encoding must have been used, and this is something you typically figure out by looking at the script or program that extracts and decodes the payload from this JPEG file.

But what if you don't have that script, what if you just have the JPEG file?

Then you need a bit of skills and luck to figure out what encoding was used.

You can try out all the encodings supported by [base64dump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py):

![](https://isc.sans.edu/diaryimages/images/20260612-054205.png)

![](https://isc.sans.edu/diaryimages/images/20260612-054245.png)

We see long BASE85 encoded strings, but still no string close to 1 million character. So this must be a custom encoding.

To try to figure out what custom encoding is used, I've added a --stats option to [base64dump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py):

![](https://isc.sans.edu/diaryimages/images/20260611-193034.png)

![](https://isc.sans.edu/diaryimages/images/20260611-193107.png)

We see that all BASE64 characters appear in the detected BASE64 strings, but that the letter A appears significantly less than other letters.

If we use a minimum length for the detected BASE64 strings, the letter A is even missing:

![](https://isc.sans.edu/diaryimages/images/20260611-193129.png)

![](https://isc.sans.edu/diaryimages/images/20260611-193200.png)

Notice that the = character is also missing, but the = character is a padding character in BASE64, not a normal character: it can only appear once or twice at the end of a BASE64 string.

So this statistics feature of [base64dump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py) helps us to detect that we might be dealing with a custom encoding, based on BASE64, where the letter A has been replaced with another character. Which character would that be? Let's take another look at out first analysis:

![](https://isc.sans.edu/diaryimages/images/20260611-192621.png)

Character # is the most frequent. So probably A has been replaced with #.

Let's try that out:

![](https://isc.sans.edu/diaryimages/images/20260611-193505.png)

Still no succes.

Let's run [byte-stats.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/byte-stats.py):

![](https://isc.sans.edu/diaryimages/images/20260611-193613.png)

This time we have a very long BASE64 string, almost 1 million characters long. But why isn't [base64dump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py) detecting it?

[byte-stats.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/byte-stats.py) looks for longest strings, for example the longest string of consecutive BASE64 characters. But it doesn't check if that string length is a multiple of 4 (that's a requirement for BASE64). While [base64dump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py) does check this.

So there must still be some kind of encoding we haven't figured out. Let's take a look at the string:

![](https://isc.sans.edu/diaryimages/images/20260611-193710.png)

![](https://isc.sans.edu/diaryimages/images/20260611-193942.png)

If you are a bit familiar with BASE64 encoding, you will notice that the string has been reversed: == appears at the beginning, and not at the end. And the end is ...qVT, which is TVq reversed, and that's a marker for MZ, e.g., a Windows executable.

So let's reverse the encoded payload with [translate.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/translate.py):

![](https://isc.sans.edu/diaryimages/images/20260611-194011(1).png)

That's indeed a PE file. And it has the same hash as the file Xavier extracted:

![](https://isc.sans.edu/diaryimages/images/20260611-194137.png)

This new feature of [base64dump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py), --stats, can help with the reversing of custom encodings by providing statistics of the encoding characters.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Evil%2BMSI%2BBackground%2BBASE64%2BStatistical%2BAnalysis/33072/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33068)
* [next](/diary/33080)

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