---
title: TerminalFix: PNG Steganography, (Mon, Sep 21st)
url: https://isc.sans.edu/diary/rss/33318
source: SANS Internet Storm Center, InfoCON: green
date: 2026-09-21
fetch_date: 2026-09-22T07:05:05.181451
---

# TerminalFix: PNG Steganography, (Mon, Sep 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Didier Stevens](/handler_list.html#didier-stevens "Didier Stevens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33314)
* [next](/diary/33320)

Click HERE to learn more about classes Didier is teaching for SANS

# [TerminalFix: PNG Steganography](/forums/diary/TerminalFix%2BPNG%2BSteganography/33318/)

**Published**: 2026-09-21. **Last Updated**: 2026-09-21 10:33:53 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/TerminalFix%2BPNG%2BSteganography/33318/#comments)

Microsoft Security Research published an interesting blog post "[TerminalFix campaign deploys a reverse tunnel through multistage intrusion](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/)" about a malware campaign. The aspect that I want to take a closer look at, is the fact that the threat actors used PNG files with steganography. I reached out to the researchers and they kindly shared the IOCs for the PNG files with me.

The first image is a small PNG file ([f5f1eb6d43dd61d5b069c250e5c666384f7417d0c95014773bf9edf8ff13bebe](https://www.virustotal.com/gui/file/f5f1eb6d43dd61d5b069c250e5c666384f7417d0c95014773bf9edf8ff13bebe)).

Analysis with [pngdump.py](https://github.com/DidierStevens/Beta/blob/master/pngdump.py) reveals that this is a proper PNG file:

![](https://isc.sans.edu/diaryimages/images/2026-09-08_11-06-51.png)

There is no data appended to the end of the image. The image starts with the expected header, and has the 3 type of chunks one expects to find in a minimal PNG file: IHDR, IDAT and IEND. There is no metadata that can contain a payload. The IDAT chunk contains the pixels of the image: encoded and ZLIB compressed. The fact that pngdump was able to decompress the IDAT data, is another indication that this is a PNG image with valid IDAT data. It consists of 111 lines and 112 columns. All of the filters of the scanlines are known filters: yet another indication that this is valid data. Thus everything indicates that this is a valid image. If it contains a payload, then it hides in the pixels, and we can confirm that steganography is used.

Let's take a look at the decompressed IDAT data (the scanlines that make up the image):

![](https://isc.sans.edu/diaryimages/images/2026-09-08_18-22-41.png)

We can see strings like MZ, .text, .data, ... All strings often found inside a Windows executable (PE file). It's very likely that there is a PE file hiding in the pixel data, but what we see here is the encoded pixel data.

The picture consists of 111 scanlines. The first byte is the type of the filter. Value 01, seen at the start of the decompressed data, indicates that the first line is encoded with the SUB (subtract) filter. 8 bits are used to encode pixel data, and the colortype is 6, e.g., RGBA. This means that there are 4 bytes for each pixel: 1 for Red, 1 for Green, 1 for Blue and 1 for Alpha (transparency). 112 columns times 4 bytes gives 448 bytes per scanline.

A filter of type SUB means that the RGBA values of a pixel are substracted from the RGBA values of the previous pixel (except for the first pixel). Thus this is a transformation that needs to be applied to obtain the raw pixel data. And SUB is not the only filter, there are 5 different filter types.

But the easiest way to obtain the raw bitmat data is to use option -R (--raw):

![](https://isc.sans.edu/diaryimages/images/2026-09-08_11-13-00.png)

We can now see the familiar DOS stub "This program ...".

The first 8 bytes of this raw bitmap is actually the length of the embedded PE file.

It's stored little-endian:

![](https://isc.sans.edu/diaryimages/images/2026-09-08_11-14-17.png)

We can use this length (49720) to carve out the PE file and calculate its hashes:

![](https://isc.sans.edu/diaryimages/images/2026-09-08_11-15-07.png)

The embedded PE file is a [genuine Microsoft executable](https://www.virustotal.com/gui/file/de9d325af3156232c34916840210efb5706d6e6a5eba1827c8240e4f71c09fa2). That executable, LockScreenContentServer.exe, is used for sideloading.

So the payload is indeed stored inside the PNG file using steganography. Usually, when using steganography, only some of the available bits will be used to store the payload, and the others will be left untouched. If this is done with least significant bits, the medium can still be rendered, and is hard to visually distinguish from the original medium.

But in this campaign, the threat actors decided to use all of the available bits. The original medium is lost, and the PNG looks like this when rendered:

![](https://isc.sans.edu/diaryimages/images/2026-09-07_11-20-57.png)

The 2 other PNG files contain the malicious payload (a DLL), stored in 2 parts, also using all the bits.

This [image](https://www.virustotal.com/gui/file/20a0f60d7364766ce7317dd17c0287c72cb2a402872e15fbdeaf9303bcf0ceb7) contains the first [part](https://www.virustotal.com/gui/file/dbed9e4764c4d5ab9d316625a9301ccc099c3530b751dab097a3866b97f817b1):

![](https://isc.sans.edu/diaryimages/images/2026-09-21_12-14-20.png)

And this [image](https://www.virustotal.com/gui/file/57f84dd867e3a3857562f6dc08126608cf13a87f717602afb1a2526bddfc4ee7) contains the second [part](https://www.virustotal.com/gui/file/24ebde9b82e4a2825fcb5951ee735278372538917ed58c68fcd1215b4497405f):

![](https://isc.sans.edu/diaryimages/images/2026-09-21_12-17-31.png)

Concatenating both parts gives the [payload, a malicious DLL](https://www.virustotal.com/gui/file/906035b6092b2ce1290c566f590e88f1b960b25c6d987f46a3d99cca5b05ee9d).

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/TerminalFix%2BPNG%2BSteganography/33318/#comments)

Click HERE to learn more about classes Didier is teaching for SANS

* [previous](/diary/33314)
* [next](/diary/33320)

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