---
title: YARA: Detect The Unexpected ..., (Thu, Mar 2nd)
url: https://isc.sans.edu/diary/rss/29598
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-03
fetch_date: 2025-10-04T08:33:24.490162
---

# YARA: Detect The Unexpected ..., (Thu, Mar 2nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29596)
* [next](/diary/29606)

# [YARA: Detect The Unexpected ...](/forums/diary/YARA%2BDetect%2BThe%2BUnexpected/29598/)

**Published**: 2023-03-02. **Last Updated**: 2023-03-02 05:51:43 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/YARA%2BDetect%2BThe%2BUnexpected/29598/#comments)

A friend and colleague of mine, [@DhaeyerWolf](https://twitter.com/dhaeyerwolf), asked me for a bit of help with the design of a YARA rule.

It’s to detect [OneNote files](https://blog.nviso.eu/2023/02/27/onenote-embedded-file-abuse/) with [embedded files](https://isc.sans.edu/diary/Detecting%2BMalicious%2BOneNote%2BFiles/29494), that are not images.
He has strings to detected any embedded file, and strings to detect embedded PNG files, JPEG files, ...

So, in YARA, how can you use this to detect OneNote files that contain embedded files, but are not images? The trick is to count and compare string occurrences.

Take this YARA string:

```

$FileDataStoreObjectGUID =  { E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC }
```

If we want to count the number of occurrences of string $FileDataStoreObjectGUID inside a file, we use this expression: #FileDataStoreObjectGUID ([# is the operator to count occurences of a string](https://yara.readthedocs.io/en/stable/writingrules.html#counting-strings)).

A condition might then be:

```

condition: #FileDataStoreObjectGUID > 2
```

A rule with this condition will trigger if there are more than 2 occurrences of string $FileDataStoreObjectGUID inside a file (and by extension, more than 2 embedded files inside that file).

This string detects embedded PNG files:

```

$FileDataStoreObjectGUIDPNG = { E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00 89 50 4E 47 0D 0A 1A 0A }
```

To write a rule that detects OneNote files with embedded files that are not PNG files, we can do the following:

```

rule onenote_suspicious {
    strings:
        $FileDataStoreObjectGUID =  { E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC }
        $FileDataStoreObjectGUIDPNG = { E7 16 E3 BD 65 26 11 45 A4 C4 8D 4D 0B 7A 9E AC ?? ?? ?? ?? ?? ?? ?? ?? 00 00 00 00 00 00 00 00 00 00 00 00 89 50 4E 47 0D 0A 1A 0A }
    condition: #FileDataStoreObjectGUID > #FileDataStoreObjectGUIDPNG
}

```

This rule triggers if we have more embedded files overall than embedded files that are PNG files. If that’s the case, then we have embedded files that are not PNG files. And these are suspicious to us.

Of course, other image types might be present, and these have been accounted for by my colleague in his [blog post](https://blog.nviso.eu/2023/02/27/onenote-embedded-file-abuse/).

This method works because all embedded files are prefixed by a data structure ([FileDataStoreObject](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-onestore/8806fd18-6735-4874-b111-227b83eaac26)) that starts with a unique GUID. Thus we just have to make strings to count all embedded files and strings for all embedded file types we consider to be benign. If there is a difference between these 2 counts, then we trigger an alert.
Best case: the rule triggers on malicious embedded files.
Worst case: the rule triggers on benign embedded files of a type we did not know about or did not expect.

This generic method works as long as it is easy to count generic objects (e.g., any embedded file) and specific objects (e.g., embedded images): then you just have to compare counters.

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords: [onenote](/tag.html?tag=onenote) [yara](/tag.html?tag=yara)

[0 comment(s)](/diary/YARA%2BDetect%2BThe%2BUnexpected/29598/#comments)

* [previous](/diary/29596)
* [next](/diary/29606)

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