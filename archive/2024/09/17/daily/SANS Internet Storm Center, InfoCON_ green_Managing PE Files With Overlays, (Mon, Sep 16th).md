---
title: Managing PE Files With Overlays, (Mon, Sep 16th)
url: https://isc.sans.edu/diary/rss/31268
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-17
fetch_date: 2025-10-06T18:28:23.314891
---

# Managing PE Files With Overlays, (Mon, Sep 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31264)
* [next](/diary/31272)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Managing PE Files With Overlays](/forums/diary/Managing%2BPE%2BFiles%2BWith%2BOverlays/31268/)

**Published**: 2024-09-16. **Last Updated**: 2024-09-16 05:31:25 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Managing%2BPE%2BFiles%2BWith%2BOverlays/31268/#comments)

There is a common technique used by attackers: They append some data at the end of files (this is called an overlay). This can be used for two main reasons: To hide the appended data from the operating system (steganography). By example, you can append a text file at the end of a JPEG image. When your favourite image viewer will process the picture, it will just ignore the "rogue" data. Here is a PNG picture that has a text file (dir output) added at the end:

![](https://isc.sans.edu/diaryimages/images/isc-20240916-1.PNG)

The second reason is to defeat security controls and tools by creating a very big file. For performance reasons, many tools won't scan or inspect big files. So attackers will append data to increase the file size. Usually, data are just a suite of zeroes because the compression ration is excellent. Here is recent example of files that I discovered:

```

remnux@remnux:/MalwareZoo/20240910$ file 'Payment Confirmation.tgz'
Payment Confirmation.tgz: gzip compressed data, last modified: Tue Sep 10 06:05:16 2024, from FAT filesystem (MS-DOS, OS/2, NT), original size modulo 2^32 750001664 gzip compressed data, unknown method, ASCII, extra field, has comment, from FAT filesystem (MS-DOS, OS/2, NT), original size modulo 2^32 750001664
remnux@remnux:/MalwareZoo/20240910$ ls -l 'Payment Confirmation.tgz'
-rwx------ 1 remnux remnux 1167212 Sep 10 03:11 'Payment Confirmation.tgz'
```

The file is 1.1MB in size but it contains a pretty big executable (less common):

```

remnux@remnux:/MalwareZoo/20240910$ tar tzvf 'Payment Confirmation.tgz'
-rwxr-xr-x 0/0       750000000 2024-09-10 02:04 Payment Confirmation.exe
```

If you unpack and inspect the file manually, you'll see that it contains indeed a huge amount of NULL bytes:

```

remnux@remnux:/MalwareZoo/20240910$ xxd 'Payment Confirmation.exe'
...
00093fa0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00093fb0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00093fc0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00093fd0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00093fe0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00093ff0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094000: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094030: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094040: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094050: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094060: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094070: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000940a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000940b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000940c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000940d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000940e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000940f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094100: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094110: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094120: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094130: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094140: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094150: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094160: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094170: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094180: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094190: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000941a0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000941b0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000941c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000941d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000941e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
000941f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094200: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094210: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094220: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094230: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094240: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094250: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094260: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094270: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00094280: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```

From a Windows loader point of view, this is not an issue: it will just ignore all the bytes that are not interesting to execute the process. Thank you Microsoft!

How can you analyze the PE file without being annoyed by the overlay? Just remove it! If you can try to manipulate the file with your favourite text editor, there is an easy way to perform this task in a few lines of Python. A classic PE files looks like this (in a very simple way!):

![](https://isc.sans.edu/diaryimages/images/isc-20240916-2.png)

In the PE headers, you can find a list of all the sections present in the file with two parameters:

* The section offset (PointerToRawData)
* The section size (SizeOfRawData)

It's easy to get the overlay offset: PointerToRawData + SizeOfRawData. This value should be the end of the file. If the file size on disk is bigger, we have an overlay!

Python has a great module called pefile[[1](https://pypi.org/project/pefile/)] that helps to investigate executables. I wrote a small script to remove an overlay from a PE file:

```

#!/usr/bin/python3
#
# Detects if a PE file has an overlay.
# If yes, it creates a new PE file without the extra data.
#
import os
import sys
import pefile

def detect_overlay(pe_filename):
    '''
    Detects and removes overlay from a PE file
    '''
    try:
        pe = pefile.PE(pe_filename)
    except Exception as e:
        print(f"Can't open the PE file: {e}")
        return

    # Display sections
    print(f"{'Section Name':<15} {'Virtual Size':<15} {'Raw Size':<15} {'Raw Offset':<15}")
    print("="*58)
    for s in pe.sections:
        s_name = s.Name.decode('utf-8').rstrip('\x00')
        virtual_size = s.Misc_VirtualSize
        raw_size = s.SizeOfRawData
        raw_offset = s.PointerToRawData
        print(f"{s_name:<15} {virtual_size:<15} {raw_size:<15} {raw_offset:<15}")

    # The offset at which the PE sections end
    last_section = pe.sections[-1]
    end_of_pe = last_section.PointerToRawData + last_section.SizeOfRawData

    # The actual file size
    file_size = os.path.getsize(pe_filename)

    if file_size >...