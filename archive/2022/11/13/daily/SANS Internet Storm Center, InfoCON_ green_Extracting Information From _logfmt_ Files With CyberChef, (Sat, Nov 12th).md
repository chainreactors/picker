---
title: Extracting Information From "logfmt" Files With CyberChef, (Sat, Nov 12th)
url: https://isc.sans.edu/diary/rss/29244
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-13
fetch_date: 2025-10-03T22:39:32.029790
---

# Extracting Information From "logfmt" Files With CyberChef, (Sat, Nov 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29242)
* [next](/diary/29246)

# [Extracting Information From "logfmt" Files With CyberChef](/forums/diary/Extracting%2BInformation%2BFrom%2Blogfmt%2BFiles%2BWith%2BCyberChef/29244/)

**Published**: 2022-11-12. **Last Updated**: 2022-11-12 13:15:59 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Extracting%2BInformation%2BFrom%2Blogfmt%2BFiles%2BWith%2BCyberChef/29244/#comments)

*I recorded a [video](https://youtu.be/ooSj_foAXbE) for this diary entry.*

I regularly have to look into log files that have a format that seems to be informally called "[logfmt](https://brandur.org/logfmt)" (I'm not sure of the name, if you know a better definition, on Wikipedia for example, please post a comment).

Every log line is a sequence of name1=value1 name2=value2 ... Thus each line contains the name of the field and the value of the field.

![](https://isc.sans.edu/diaryimages/images/20221112-121135.png)

For this diary entry, and other examples, I created this "[conn.ips.logfmt](https://gist.github.com/DidierStevens/66bc3a745bd1542ef5a04e3fb0247191)" file (it's based on conn.log.gz from this [repository](https://www.secrepo.com/)).

So, the problem: you have a log file with network events, and you want to know to which public IPv4 addresses a particular client connected to.

Here is a solution with [CyberChef](https://gchq.github.io/CyberChef/).

Log files can be very large, sometimes gigabytes of data. A browser running CyberChef can not process such files efficiently. My browser often crashes when I try that.

In that case, it's best to grep the file for the IPv4 address of the client you are interested in (192.168.202.106 in our example).

Like this: grep -F 192.168.202.106 logfile.log > logfile.grep.192\_168\_202\_106.log

You don't have to bother with boundaries, this is something we will deal with in CyberChef (say that you grep for 192.168.202.10, then you will also select 192.168.202.100, 192.168.202.101, 192.168.202.102, ...)

I start with a GZip compressed version of the file, conn.ips.logfmt.gz, and I load it into CyberChef:

![](https://isc.sans.edu/diaryimages/images/20221112-114152.png)

Next, I apply the Gunzip operation to obtain the decompressed log (if your log is not compressed, you can ignore this step):

![](https://isc.sans.edu/diaryimages/images/20221112-114221.png)

A filter operation with a regular expression allows me to select all log lines where 192.168.202.106 is the source of a connection. I use this regular expression (without double quotes): "srcip=192\.168\.202\.106 ".

![](https://isc.sans.edu/diaryimages/images/20221112-114304.png)

Since the dot (.) is a special character in regular expression syntax (it represents any character), I have to escape it: \.

Notice the space character at the end of the regular expression: this is how I handle boundaries in this example. If my source IPv4 address would have a LSB byte that is smaller than 100, for example 192.168.202.10, then a regular expression like "srcip=192\.168\.202\.10" would also select IPv4 source addresses like 192.168.202.100, 192.168.202.101, ...

The space character is a field separator in this log, so I add a space character at the end of the regular expression.
Notice that this would not work if the srcip field is the last one in the log, because then there would be no space character after that field.

Another solution would be to use the meta character for word boundaries: \b. Like this: "srcip=192\.168\.202\.106\b".

But some time ago, I found an issue with this word boundary character: I assumed that it meant: anything that is not a letter or digit is not part of word, and is thus a boundary. That's incomplete: it's actually: "anything that is not a letter or digit or underscore".

Next operation of the CyberChef recipe: apply a regular expression to select all the destination addresses:

![](https://isc.sans.edu/diaryimages/images/20221112-114353.png)

Regular expression "dstip=[^ ]+" selects all lines with a dstip field and its value. By defining a capture group ("dstip=([^ ]+)") and changing the output format to "list capture groups", I can select the individual IPv4 addresses.

Next, I want only public IPv4 addresses. This can be done with operation "Extract IP addresses" and selecting the option "Remove local IPv4 addresses":

![](https://isc.sans.edu/diaryimages/images/20221112-114428.png)

And finally, a unique operation with counters:

![](https://isc.sans.edu/diaryimages/images/20221112-114450.png)

This CyberChef recipe can be found [here](https://gist.github.com/DidierStevens/add4bdbd92b9c9cdfe7a55d955d74126).

Didier Stevens
Senior handler
Microsoft MVP
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Extracting%2BInformation%2BFrom%2Blogfmt%2BFiles%2BWith%2BCyberChef/29244/#comments)

* [previous](/diary/29242)
* [next](/diary/29246)

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