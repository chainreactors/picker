---
title: Steganography Analysis With pngdump.py: Bitstreams, (Thu, May 1st)
url: https://isc.sans.edu/diary/rss/31904
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-02
fetch_date: 2025-10-06T22:31:17.298193
---

# Steganography Analysis With pngdump.py: Bitstreams, (Thu, May 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31902)
* [next](/diary/31906)

# [Steganography Analysis With pngdump.py: Bitstreams](/forums/diary/Steganography%2BAnalysis%2BWith%2Bpngdumppy%2BBitstreams/31904/)

**Published**: 2025-05-01. **Last Updated**: 2025-05-01 07:00:05 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Steganography%2BAnalysis%2BWith%2Bpngdumppy%2BBitstreams/31904/#comments)

A friend asked me if my [pngdump.py](https://github.com/DidierStevens/Beta/blob/master/pngdump.py) tool can extract individual bits from an image (cfr. diary entry "[Steganography Analysis With pngdump.py](https://isc.sans.edu/diary/Steganography%20Analysis%20With%20pngdump.py/31894)").

It can not. But another tool can: [format-bytes.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/format-bytes.py).

In the diary entry I mentioned, a PE file is embedded inside a PNG file according to a steganographic method: all the bytes of a channel are replaced by the bytes that make up the PE file. If one would visualize this image, it would be clear that it represents nothing. That it just looks like noise.

Often with steganography, the purpose is to hide a message in some medium, without distorting that medium too much. If it's a picture for example, then one would not notice a difference between the original picture and the altered picture upon visual inspection.

This is often achieved by making small changes to the colors that define individual pixels. Take an 8-bit RGB encoding: each pixel is represented by 3 bytes, one for the intensity of the color red, one for green and one for blue. By changing just the least significant bit (LSB) of each byte that represents the RGB color of the pixel, one can encode 3 bits, without noticable change in the final color (it's a change smaller than 0.5% (1/256)).

Take these pictures for example:

![](https://isc.sans.edu/diaryimages/images/20250430-171729.png)

The one on the left is the original picture, the one on the right has an embedded PE file (via LSB steganography). I can't see a difference.

To extract the PE file from the picture on the right, one has to extract the LSB of each color byte, and assemble them into bytes. This can be done with format-bytes.py.

format-bytes.py takes binary data as input and parses it per the instructions of the analyst. I typically use it to parse bytes, like in this example:

```

format-bytes.py -f "<IBB"
```

This means the input data should be parsed as a unsigned 32-bit integer (I), little-endian (<), followed by two unsigned bytes (BB).

But format-bytes.py can also extract individual bits: this is done with bitstream processing. Let me show you an example.

The steganographic lake image I created contains an embedded PE file. The bits that make up the bytes of the PE file, are stored in the least significant bit of each color byte of the pixels in the image.

First I encoded the length of the PE file as an unsigned, little-endian 32-bit integer. Using the LSBs of the pixels. And then followed by the PE file itself, also encoded in the LSBs of the pixels.

The following command decodes the length:

```

pngdump.py -R -d lake-exe.png   | cut-bytes.py 0:32l   | format-bytes.py -d -f "bitstream=f:B,b:0,j:>"   | format-bytes.py
```

[pngdump.py](https://github.com/DidierStevens/Beta/blob/master/pngdump.py)'s option -R extracts the raw bitmap of the image, option -d does a binary dump.

This bitmap data is piped into [cut-bytes.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/cut-bytes.py) to select the first 32 bytes (0:32l). We want the first 32 bytes to extract the 32 LSBs that make up the length of the embedded PE file.

[format-bytes.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/format-bytes.py)'s option -f "bitstream=f:B,b:0,j:>" instructs the tool to operate on the bit level (bitstream) and to treat the incoming data as individual unsigned bytes (f:B, e.g., format B), to select the least significant bit (b:0, e.g., the bit at position 0 in the byte) and to assemble the extracted bits into bytes in big-endian order (j:>, e.g., join in big-endian order).

That produces 4 bytes, that can then be piped again into another instance of format-bytes, this time to parse the integer.

![](https://isc.sans.edu/diaryimages/images/20250430-174520.png)

This output produced by the second instance of format-bytes.py, represents the incoming data in different formats. The line that starts with 4I shows the formatting of 4-byte long integers. ul stand for unsigned & little-endian. Thus the length of the PE file is 58120, this is stored in the LSBs of the first 32 bytes of the raw image.

Now that we know the length of the PE files, we know how many bits to extract: 58120 \* 8 = 464960. So from the 32nd byte in the raw image, we take 464960 bytes and process them with the same bitstream method (but this time, I do an HEX/ASCII dump (-a) to view the extracted PE file):

```

pngdump.py -R -d lake-exe.png   | cut-bytes.py 32:464960l   | format-bytes.py -a -f "bitstream=f:B,b:0,j:>" | headtail.py
```

![](https://isc.sans.edu/diaryimages/images/20250430-175900.png)

This looks indeed as a PE file. Let's do a binary dump and pipe it into tools [file-magic.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/file-magic.py) and [pecheck.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pecheck.py) to verify that it is indeed a valid PE file:

```

pngdump.py -R -d lake-exe.png   | cut-bytes.py 32:464960l   | format-bytes.py -d -f "bitstream=f:B,b:0,j:>" | file-magic.py
```

![](https://isc.sans.edu/diaryimages/images/20250430-180502.png)

```

pngdump.py -R -d lake-exe.png   | cut-bytes.py 32:464960l   | format-bytes.py -d -f "bitstream=f:B,b:0,j:>" | pecheck.py | headtail.py
```

![](https://isc.sans.edu/diaryimages/images/20250430-180539.png)

We did extract a valid PE file.

And as a final check, since I know the hash of the original file, let's validate it with [hash.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/hash.py):

```

pngdump.py -R -d lake-exe.png | cut-bytes.py 32:464960l | format-bytes.py -d -f "bitstream=f:B,b:0,j:>" | hash.py -v 0a391054e50a4808553466263c9c3b63e895be02c957dbb957da3ba96670cf34
```

![](https://isc.sans.edu/diaryimages/images/20250430-181016.png)

As Johannes explained in his [Stormcast](https://isc.sans.edu/podcastdetail/9426) episode, there are many ways to encode data using steganography, and it's often hard to detect/extract unless you know the exact algorithm. I was able to decode it with my tools, because I knew exactly how the PE file was encoded (as I did it myself :-) ).

You can find many (online) steganography tools, but they don't always explain how they encode a payload.

If you are interested, tune in this Saturday, I will present you with a challenge diary entry. :-)

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Steganography%2BAnalysis%2BWith%2Bpngdumppy%2BBitstreams/31904/#comments)

* [previous](/diary/31902)
* [next](/diary/31906)

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
  + [Threat Feeds Map...