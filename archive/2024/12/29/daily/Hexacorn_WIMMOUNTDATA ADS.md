---
title: WIMMOUNTDATA ADS
url: https://www.hexacorn.com/blog/2024/12/28/wimmountdata-ads/
source: Hexacorn
date: 2024-12-29
fetch_date: 2025-10-06T19:37:06.987509
---

# WIMMOUNTDATA ADS

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/12/27/monotificationuxstub-exe-lolbin/)
[Next →](https://www.hexacorn.com/blog/2024/12/31/smuggling-payloads-and-tools-in-using-wim-images/)

# WIMMOUNTDATA ADS

Posted on [2024-12-28](https://www.hexacorn.com/blog/2024/12/28/wimmountdata-ads/ "11:32 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In [my old post](https://www.hexacorn.com/blog/2012/03/26/good-alternate-data-streams-ads/) I listed a number of ‘good Alternate Data Streams (ADS)’, and one of them was called $WIMMOUNTDATA.

I just came across the very same ADS again during one of my procmon tests, so I decided to bite. Googling around for this string doesn’t bring much other than some reports and complains related to suspected malware and issues with the *dism.exe* program.

After confirming the ADS is referenced by the *wimgapi.dll!WIMMountImage* API I created a quick & dirty test wim file, and then mounted it using *dism.exe*:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/WIMMOUNTDATA_1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/WIMMOUNTDATA_1.png)

The list of commands is listed below:

* md foo
* echo test > c:\foo\bar.txt
* Dism /Capture-Image /ImageFile:”foo.wim” /CaptureDir:C:\foo /Name:Foo
* md testmountwim
* Dism /Mount-Image /ImageFile:”foo.wim” /MountDir:C:\testmountwim
* dir /r testmountwim

The $WIMMOUNTDATA ADS created as a result of these commands looks like this:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/WIMMOUNTDATA_2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/12/WIMMOUNTDATA_2.png)

The first DWORD is obviously a size (0x00000128=296), then there are a few fields that i have not deciphered yet, including a potential hash at 0x10, and finally a few structures where first 3 are just Unicode (16-bit) strings and the rest are unknown data structures — all of them prefixed by their lengths (DWORD), and these prefixed by their record indexes(also DWORD), so we can interpret it as follows:

* @0x00 – 0x00000128 – length of the whole ADS
* @0x04 – ?
* @0x08 – ?
* @0x10 – hash (?) –> mount GUID=e242237c-66ed-4958-b9ec-c49b07eaeeb5 (see below)
* @0x20 – ?
* @0x28 – 0x00000001, 0x00000016 (rounded up to 8 bytes boundary) ***C:\foo.wim***
* @0x48 – 0x00000002, 0x00000020 (rounded up to 8 bytes boundary) ***C:\testmountwim***
* @0x70 – 0x00000003, 0x0000004C (rounded up to 8 bytes boundary) ***C:\Users\ADMINI~1\AppData\Local\Temp\***
* @0xC8 – 0x00000004, 0x00000008 ?
* @0xD8 – 0x00000005, 0x00000048 ? – the last part is the ***C:\WINDOWS\Logs\DISM\dism.log*** path (also aligned to 8 bytes boundary)

The last string referenced in the ADS is a log file name that is actively being used, and is a forensic gold mine as it includes a lot of very detailed logs coming directly from the *dism.exe* tool. An excerpt from the log helps us to make sense of the ‘hash’ we have observed at @0x10 — it’s actually a mount guid!

```
2024-12-28 14:25:40, Info                  DISM   DISM.EXE: Executing command line: Dism  /Mount-Image /ImageFile:"foo.wim" /MountDir:C:\testmountwim
2024-12-28 14:25:40, Info                  DISM   DISM Imaging Provider: PID=3908 TID=244 WIM image specified - CGenericImagingManager::GetImageInfoCollection
[3908.244] Mounting new image.
Wim:         [C:\foo.wim]
Image Index: [1]
Mount Guid:  [e242237c-66ed-4958-b9ec-c49b07eaeeb5]
Mount Path:  [C:\testmountwim]
[3908.244] Wimserv process started for mount guid e242237c-66ed-4958-b9ec-c49b07eaeeb5; PID is 2820
[2820.2864] Registered log file(s) for mount of wim at C:\foo.wim.
[2820.2864] Mount complete.
```

Analysis of this default dism log file may bring a lot of interesting information about the mounting and unmounting activities happening on the system, so it may be a valuable forensic artifact to collect, parse, and interpret.

This entry was posted in [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/12/28/wimmountdata-ads/ "Permalink to WIMMOUNTDATA ADS").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")