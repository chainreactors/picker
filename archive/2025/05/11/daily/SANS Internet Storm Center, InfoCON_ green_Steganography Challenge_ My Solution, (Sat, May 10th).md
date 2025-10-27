---
title: Steganography Challenge: My Solution, (Sat, May 10th)
url: https://isc.sans.edu/diary/rss/31912
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-11
fetch_date: 2025-10-06T22:25:43.279796
---

# Steganography Challenge: My Solution, (Sat, May 10th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31910)
* [next](/diary/31920)

# [Steganography Challenge: My Solution](/forums/diary/Steganography%2BChallenge%2BMy%2BSolution/31912/)

**Published**: 2025-05-10. **Last Updated**: 2025-05-10 10:33:58 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Steganography%2BChallenge%2BMy%2BSolution/31912/#comments)

When I tried to solve "[Steganography Challenge](https://isc.sans.edu/diary/Steganography%2BChallenge/31910/)" with the same method as I used in "[Steganography Analysis With pngdump.py: Bitstreams](https://isc.sans.edu/diary/Steganography%20Analysis%20With%20pngdump.py%3A%20Bitstreams/31904)", I couldn't recover the text message.

So I looked into the [source code](https://github.com/auyer/steganography/blob/main/steganography.go) of the encoding function EncodeNRGBA, and noticed this:

![](https://isc.sans.edu/diaryimages/images/20250510-115534.png)

To encode each of the pixels, there are 2 nested for loops: "for x" and "for y". This means that first the column is processed (y).

While a raw bitmap is one line after the other (and not one column after the other). Thus we need to transpose the raw bitmap (rows and columns need to be swapped):

![](https://isc.sans.edu/diaryimages/images/20250510-120012.png)

And as 8-bit RGB encoding is used for pixels, each pixel is encoded with 3 bytes, that need to be transposed correctly:

![](https://isc.sans.edu/diaryimages/images/20250510-120223.png)

This transposition can be done with my tool [translate.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/translate.py) and the necessary Python function. I wrote this one to do the transposition:

```

def Transpose(data, size, width, height):
    result = []
    for x in range(width):
        for y in range(height):
            i = y * width + x
            result.append(data[i*size:(i + 1)*size])
    return b''.join(result)
```

So let's decode this.

First we need the dimensions of the image:

![](https://isc.sans.edu/diaryimages/images/20250510-120850.png)

1195 pixels wide and 642 pixels high.

With this information, I can do the transposition with translate.py (3 is the number of bytes per pixel): Transpose(data, 3, 1195, 642)

Then I use the following command to decode the size of the message. It's the same command as I used in diary entry "[Steganography Analysis With pngdump.py: Bitstreams](https://isc.sans.edu/diary/Steganography%20Analysis%20With%20pngdump.py%3A%20Bitstreams/31904)", except that this time there's an extra step (translate) to do the transposition:

```

pngdump.py -R -d encoded_stegosaurus.png | translate.py -f -s transpose.py "lambda data: Transpose(data, 3, 1195, 642)" | cut-bytes.py 0:32l | format-bytes.py -d -f "bitstream=f:B,b:0,j:>" | format-bytes.py
```

![](https://isc.sans.edu/diaryimages/images/20250510-121315.png)

The message is 547 bytes long. Let's decode this:

```

pngdump.py -R -d encoded_stegosaurus.png | translate.py -f -s transpose.py "lambda data: Transpose(data, 3, 1195, 642)" | cut-bytes.py 32:4376l | format-bytes.py -d -f "bitstream=f:B,b:0,j:>"
```

![](https://isc.sans.edu/diaryimages/images/20250510-121446.png)

We were able to extract the text message (a partial copy from the Wikipedia article on Stegosaurus).

But what surprised me is the lack of space characters ... I though that this could hardly be due to an error in the decoding, so I took a look at the [test encoder source code](https://github.com/auyer/steganography/blob/main/steganography_test.go). Line 19 contains the message encoded as decimal bytes, and I noticed that there are no values equal to 32 (that's the space character). Decoding this line with [numbers-to-string.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/numbers-to-string.py) does indeed reveal that there are no space characters in the source code:

![](https://isc.sans.edu/diaryimages/images/20250510-121958.png)

The solution to this challenge is identical to the one described in diary entry "[Steganography Analysis With pngdump.py: Bitstreams](https://isc.sans.edu/diary/Steganography%20Analysis%20With%20pngdump.py%3A%20Bitstreams/31904)", with one important difference: we need to transpose lines and columns.

Finally, if you would want to write this command as a one-liner without a file containing the source code for the Transpose Python function, you can to this with nested list comprehensions, but it's less readable:

```

pngdump.py -R -d encoded_stegosaurus.png | translate.py -f "lambda data: b''.join([b''.join([data[(y*1195+x)*3:(y*1195+x+1)*3] for y in range(642)]) for x in range(1195)])" | cut-bytes.py 32:4376l | format-bytes.py -d -f "bitstream=f:B,b:0,j:>"
```

![](https://isc.sans.edu/diaryimages/images/20250510-122731.png)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Steganography%2BChallenge%2BMy%2BSolution/31912/#comments)

* [previous](/diary/31910)
* [next](/diary/31920)

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