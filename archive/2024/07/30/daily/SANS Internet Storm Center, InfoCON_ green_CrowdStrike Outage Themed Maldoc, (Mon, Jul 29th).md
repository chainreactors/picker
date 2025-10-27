---
title: CrowdStrike Outage Themed Maldoc, (Mon, Jul 29th)
url: https://isc.sans.edu/diary/rss/31116
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-30
fetch_date: 2025-10-06T17:46:54.137035
---

# CrowdStrike Outage Themed Maldoc, (Mon, Jul 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31112)
* [next](/diary/31118)

# [CrowdStrike Outage Themed Maldoc](/forums/diary/CrowdStrike%2BOutage%2BThemed%2BMaldoc/31116/)

**Published**: 2024-07-29. **Last Updated**: 2024-07-29 00:03:44 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/CrowdStrike%2BOutage%2BThemed%2BMaldoc/31116/#comments)

I found a [malicious Word document](https://www.virustotal.com/gui/file/457c0227a937215335b9c7793c83f3c9b5329ea839d8b2b44e20dda0e808379c) with VBA code using the CrowdStrike outage for social engineering purposes. It's an .ASD file (AutoRecover file). My tool [oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py) can analyze it:

![](https://isc.sans.edu/diaryimages/images/20240728-100404.png)

Before I dive into the VBA code, I want to highlight the metadata of this document:

![](https://isc.sans.edu/diaryimages/images/20240728-100645.png)

oledump.py's -M option displays the metadata of this document. This option uses olefile's method to parse metadata. That method does not parse custom properties.

To view custom properties, you need to use my plugin for metadata, [plugin\_medata.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/plugin_metadata.py):

![](https://isc.sans.edu/diaryimages/images/20240728-100716.png)

There is a GrammarlyDocumentId custom property. I was able to verify that this custom property is added when a Word document is checked by the Grammarly plugin.

So does that mean that threat actors are using Grammarly to create their phishing & maldoc documents in proper English? Let's take a look at the text, by dumping the strings (-S) in the WordDocument stream:

![](https://isc.sans.edu/diaryimages/images/20240728-101841.png)

This reminds me of the [maldoc CrowdStrike wrote about](https://www.crowdstrike.com/blog/fake-recovery-manual-used-to-deliver-unidentified-stealer/). Let's open this document in a VM to have a better look:

![](https://isc.sans.edu/diaryimages/images/20240728-102613.png)

That fails, I need to put the file in the proper folder (C:\Users\USERNAME\AppData\Roaming\Microsoft\Word):

![](https://isc.sans.edu/diaryimages/images/20240728-102713.png)

![](https://isc.sans.edu/diaryimages/images/20240728-102746.png)

This does indeed look like the maldoc CrowdStrike wrote about. It's using a copy of the [Microsoft CrowdStrike recovery guidance article](https://techcommunity.microsoft.com/t5/intune-customer-success/new-recovery-tool-to-help-with-crowdstrike-issue-impacting/ba-p/4196959) as bait.

Let's take a look at the [maldoc](https://www.virustotal.com/gui/file/803727ccdf441e49096f3fd48107a5fe55c56c080f46773cd649c9e55ec1be61) CrowdStrike wrote about:

![](https://isc.sans.edu/diaryimages/files/20240728-103550(1).png)

It's an OOXML file, so the text and the properties are stored in XML documents, not inside OLE streams. Let's take a look with [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py) and [xmldump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xmldump.py):

![](https://isc.sans.edu/diaryimages/images/20240728-104126.png)

Custom properties are stored inside file docProps/custom.xml (file 25):

![](https://isc.sans.edu/diaryimages/images/20240728-104225.png)

This one too contains a GrammarlyDocumentId custom property, and the value is the same. So these documents are related.

Let's take a look at the core properties:

![](https://isc.sans.edu/diaryimages/images/20240728-105425.png)

As the usernames and dates match exactly, it's very likely that these 2 documents are related.

I compared the text of the .docm Word document with the text of the Microsoft post ("[New Recovery Tool to help with CrowdStrike issue impacting Windows endpoints](https://techcommunity.microsoft.com/t5/intune-customer-success/new-recovery-tool-to-help-with-crowdstrike-issue-impacting/ba-p/4196959)"), and apart from some differences due to updates to the Microsoft post (like script versions), there is just one difference that was clearly made by the threat actors. The word "post", used in the original Microsoft post, has been replaced by the word "document" twice by the threat actors:

![](https://isc.sans.edu/diaryimages/images/20240728-113344.png)

So there are no changes in the document that could be attributed to Grammarly edits: I can't conclude that threat actors are actually using Grammarly for the texts they create.

It might even be that this GrammarlyDocumentId custom property is present because the threat actors just reused an older document, where this property was already present. If we look at the dates in the metadata, we see that the last print date is much older than the creation and modification dates:

![](https://isc.sans.edu/diaryimages/images/20240728-114209.png)

If the last print date is older than the creation date, it usually means that the document was created by opening an older document with Word and then performing a "Save As" operation.

Notice that the creation date is "2024-07-19T10:29:00Z", which means July 19th 2024, 10:29:00 UTC. According to CrowdStrike, the faulty update was released on July 19th 2024, 04:09 UTC. So it looks like the threat actors were reacting very fast.

So in conclusion, although a Grammarly custom property is present, there is no evidence that Grammarly is actually being used to correct texts of phishing/maldoc files.

To conclude, let's take a quick look at the VBA code.

Comparing the content of the streams of the document I found and the document CrowdStrike wrote about, we see that the SHA256 hashes are identical, thus that this exactly the same VBA code. More proof that the two documents are related:

![](https://isc.sans.edu/diaryimages/images/20240728-115231.png)

Let's dump the VBA code:

![](https://isc.sans.edu/diaryimages/images/20240728-115654.png)

It's easy to spot the URL (mentioned in the CrowdStrike blog post):

![](https://isc.sans.edu/diaryimages/images/20240728-115731.png)

The [file that is downloaded](https://www.virustotal.com/gui/file/5eaf0f1c1d23f4372e24eb15ee969552c416a38dbc45e4f2b4af283e3bfb8721) is a fake certificate:

![](https://isc.sans.edu/diaryimages/images/20240728-120116.png)

I know that it is a fake certificate, because the BASE64 code does not start with an M (I explain [here](https://blog.nviso.eu/2018/07/31/powershell-inside-a-certificate-part-1/) why the BASE64 code of certificates always have to start with the letter M).

It actually starts with TVq..., which decodes to MZ... so very likely a PE file.

Let's decode it with [base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py):

![](https://isc.sans.edu/diaryimages/images/20240728-120843.png)

And we obtain the [Daolpu stealer](https://www.virustotal.com/gui/file/4ad9845e691dd415420e0c253ba452772495c0b971f48294b54631e79a22644a) identified by CrowdStrike.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/CrowdStrike%2BOutage%2BThemed%2BMaldoc/31116/#comments)

* [previous](/diary/31112)
* [next](/diary/31118)

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
  + [...