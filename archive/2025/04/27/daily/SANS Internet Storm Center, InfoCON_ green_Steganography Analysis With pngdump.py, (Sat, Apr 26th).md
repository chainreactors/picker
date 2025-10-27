---
title: Steganography Analysis With pngdump.py, (Sat, Apr 26th)
url: https://isc.sans.edu/diary/rss/31894
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-27
fetch_date: 2025-10-06T22:05:33.702054
---

# Steganography Analysis With pngdump.py, (Sat, Apr 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31892)
* [next](/diary/31896)

# [Steganography Analysis With pngdump.py](/forums/diary/Steganography%2BAnalysis%2BWith%2Bpngdumppy/31894/)

**Published**: 2025-04-26. **Last Updated**: 2025-04-26 06:45:13 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Steganography%2BAnalysis%2BWith%2Bpngdumppy/31894/#comments)

I like it when a diary entry like "[Example of a Payload Delivered Through Steganography](https://isc.sans.edu/diary/Example%20of%20a%20Payload%20Delivered%20Through%20Steganography/31892)" is published: it gives me an opportunity to test my tools, in particular [pngdump.py](https://github.com/DidierStevens/Beta/blob/master/pngdump.py), a tool to analyze PNG files.

A PNG file consists of a header followed by chunks. pngdump.py shows this (sample [c2219ddbd3456e3df0a8b10c7bbdf018da031d8ba5e9b71ede45618f50f2f4b6](https://www.virustotal.com/gui/file/c2219ddbd3456e3df0a8b10c7bbdf018da031d8ba5e9b71ede45618f50f2f4b6)):

![](https://isc.sans.edu/diaryimages/images/20250426-081248.png)

The IHDR chunk gives us information about the image: it's 31744 pixels wide and 1 pixel high. That's already unusual!

There are 8 bits and the colortype is 6. That's RGBA (Red, Green, Blue and Alpha/Transparency). So there are 4 channels in total with a resolution of 8 bits, thus 4 bytes per pixel.

The IDAT chunk contains the compressed (zlib) image: there's only one IDAT chunk in this image. And the line filter is None: this means that the pixel data is not encoded.

So let's take a look at the decompressed raw pixel data:

![](https://isc.sans.edu/diaryimages/images/20250426-081952.png)

We see the letters M and Z: these letters are characteristic for the header of a PE file.

And a bit further we see the letters "This program ...".

So it's clear that a PE file is embedded in the pixel data.

Every fourth byte is a byte of the PE file, and the first byte of the PE file is the second byte of the pixel data: so the PE file is embedded in the second channel of the pixel data.

We can select these bytes with a tool like [translate.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/translate.py), that takes a Python function to manipulate the bytes it receives.

data[1::4] is a Python slice that starts with the second byte (position 1), ends when there is no more data, and selects every fourth byte (a step of 4). This allows us to extract the second channel:

![](https://isc.sans.edu/diaryimages/images/20250426-082715(1).png)

pngdump.py's option -d performs a binary dump, piping the raw pixel data into translate.py. translate.py's option -f reads all the data in one go (by default, translate.py operates byte per byte). lambda data: data[11:4] is a Python function that takes the raw pixel data as input (data) and returns the bytes of the second channel via a Python slice that selects every fourth byte starting with the second byte of the raw pixel data.

Finally, the extracted PE file is piped into [file-magic.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/file-magic.py) to identify the file type: it is a .NET file, as Xavier explained.

We can also check that it is a PE file with a tool like [pecheck.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pecheck.py):

![](https://isc.sans.edu/diaryimages/images/20250426-083352.png)

And we can calculate the hashes with [hash.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/hash.py)![](https://github.com/DidierStevens/DidierStevensSuite/blob/master/hash.py) to look up the file on VirusTotal:

![](https://isc.sans.edu/diaryimages/images/20250426-083726.png)

This is the SHA256 of the extracted PE file: [8f4cea5d602eaa4e705ef62e2cf00f93ad4b03fb222c35ab39f64c24cdb98462](https://www.virustotal.com/gui/file/8f4cea5d602eaa4e705ef62e2cf00f93ad4b03fb222c35ab39f64c24cdb98462).

It's clear that the steganography works in this example: 0 detections for the PNG file on VirusTotal, and 49 detections for the embedded PE file.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Steganography%2BAnalysis%2BWith%2Bpngdumppy/31894/#comments)

* [previous](/diary/31892)
* [next](/diary/31896)

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