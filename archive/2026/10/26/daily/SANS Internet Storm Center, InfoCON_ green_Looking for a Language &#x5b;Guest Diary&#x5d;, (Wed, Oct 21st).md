---
title: Looking for a Language &#x5b;Guest Diary&#x5d;, (Wed, Oct 21st)
url: https://isc.sans.edu/diary/rss/33442
source: SANS Internet Storm Center, InfoCON: green
date: 2026-10-26
fetch_date: 2026-10-27T07:06:02.207658
---

# Looking for a Language &#x5b;Guest Diary&#x5d;, (Wed, Oct 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33440)
* [next](/diary/33450)

Click HERE to learn more about classes Guy is teaching for SANS

# [Looking for a Language [Guest Diary]](/forums/diary/Looking%2Bfor%2Ba%2BLanguage%2BGuest%2BDiary/33442/)

**Published**: 2026-10-21. **Last Updated**: 2026-10-26 09:38:03 UTC
**by** [Jeffray Spence, SANS.edu BACS Student](/handler_list.html#jeffray-spence,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Looking%2Bfor%2Ba%2BLanguage%2BGuest%2BDiary/33442/#comments)

[This is a Guest Diary by Jeffray Spence, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

Around Here, we start our day with coffee, but our day does not begin until we have our data...So much data.  Where to even begin?

When approaching a massive dataset, such as those from a DShield SIEM Honeypot, the first step is to actually find something to analyze.  As for myself, I usually go looking for something that makes me go; "*Huh.*"

Today we will be walking through a starting approach with Kibana Discover to search out embedded language preferences in webtraffic, then we will use this as a starting point for finding anomalous activity.

**Find A Problem to Get Some Data**

Inside of my DShield SIEM there are nearly a million records, so I approach by looking for a slightly smaller data carve with which to work which still represents the problem set:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic1.png)

Anyone with Elastic Kibana can perform this approach on their webtraffic data as long as the HTTP headers are provided.  Here, the logs are from my SANS Dshield Honeypot and the accompanying Dshield SIEM.  For those who desire to install this setup there are plenty of great resources out there with links at the end of this article [[1](https://github.com/dshield-isc/dshield)] [[2](https://github.com/bruneaug/DShield-SIEM)].

In slightly more than 3 weeks of observation the rasperry pi honeypot had transferred a Million Records into the Elastic SIEM.  These many records can prove very challenging when figuring out where to start, so it is helpful to know that even with no filtering applied on the ***Discover*** page the Field Statistics will give some fairly detailed metrics about what fields exist in the current Index.

On the ***Discover*** page in the upper right, I selected my index (here the ***index*** is “***cowrie***”) and without any filter applied I selected ***Field Statistics***:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic2.png)

Calculating statistics ourselves is possible using ESQL and Stats, however this feature of Elastic makes gaining visibility much more obtainable at the onset.  We are immediately presented with a screen displaying all of the ***Documents*** broken down by ***Top Values*** which potentially gives us some valuable insight:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic3.png)

The resultant statistics show that in these 3 weeks my honeypot had generated 960,000 logs, but all of those are only within 4 rules.  Four is less than a 960,000 so this gives a more manageable starting dataset:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic4.png)

“*Huh.*”  This little raspberry PI has been humming away quietly all day and all night and only 4 rules have popped up.  I found this interesting.  With no filtering applied only 15,271 records triggered any rule?

This setup is a honeypot, so literally every record is suspicious.  So, what about the other 944,866 records which triggered no rules?

Today, we want a problem not a project, so we are going to use one of these rules to narrow down our traffic for analysis.

We have rule triggers for the **Index page**.  Boring.  Great for generating a large dataset, but this is not a very targeted approach.

**Git Config** is something I had previously analyzed, and this led me to discover malicious traffic attempting to scrape Git Config from internet hosts.  Neat, but not for today.

**Fortinet Emulation**, for those who don't know, has fairly recently gotten a lot of attention [3].
Only one detection so far in my honeypot, so for me that's just an outlier.  Interesting, but not much of a corpus.

Through the process of elimination, we are left with the **Sonicwall Appliance Login Page** rule.
Good representation over the problem space with 41 individual hosts logging in activity.  This could potentially demonstrate how an attack is conducted or give a clue as to who was conducting one.  Perfect because we are looking for regular and repeating attack attempts.  I selected these criteria as a Kibana filter.

Now to start digging.

**Data Selection**

Now that we have a smaller dataset to work within, we need to decide what we want to find.  After that we need to figure out how to actually find that.

This first approach is what I would NOT recommend One do:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic5.png)

Noticing here that every field statistic for all 157 records has *One **Distinct Value*** and only1 category under Distribution tells us these fields are ALL common to ALL records.  A field common to every record will have a unique value for each record.

We don't want common, we want weird: the approach I will use is to flip it and look at ***Distribution*** 2 or higher.  This is Long tail analysis:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic6.png)

Here we see the ***Distinct values*** are now descending with the “sweet spot” between 2 and 6 so.  Not an exact criterion, but one that is practical for manual review.

Within these fields we have fields of interest:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic7.png)

When fields contain similar values, they may illustrate a relationship between the data represented.  Here the traffic triggering the Sonicwall Rule contains a relatively small subset of unique values.  The next step is to find something we cannot readily explain away; a simple exercise to conduct on the “*tags*”, “*host.ip*”, and “*host.mac*” fields.  The IP and MAC are going to be both interfaces of my Dshield Pi itself, while the Tags are going to be metadata about how the rules generate.  The “*source.geo.continent\_code*” is not very useful in a Virtual Private Server (VPS) enabled world but may prove useful later.  This leaves 2 fields:

![](https://isc.sans.edu/diaryimages/images/Jeffray_Spence_pic8.png)

http.request.connection

"**Close**" and "**close**".  Most traffic parsing tools are going to convert these all to lowercase string, and thus never see this small difference.
.  No longer interesting.

http.request.mime\_type

"utf-8" (the defacto choice) verses some interesting mime encoding...

Next was to break down what this mime encoding is saying: "GBK,utf-8;q=0.7,\*;q=0.3"

This string is sent to a webserver as the *Accept-Charset HTTP* header.  Values of *GBK,utf-8*, and wildcard (**\***) are present.  The preference weights are specified as "**q**" (for “quality value” by convention).  Since the implicit maximum weight value is q=1.0, the simplified character set preferences are:

(GBK;q=1.0),(utf-8;q=0.7),(\*;q=0.3)

I think of this as a preference for what character encoding to use:
(*Send me “GBK” 100% of the time, if not “utf-8” 70%, and if not Whatever 30%*)

UTF-8 makes sense as does wildcard (**\***).  However, ***GBK*** is explicitly the extension of the “GB 2312” character set for Simplified Chinese characters.
*"Huh.*"

Why do these requests explicitly state they greatly desire to transfer data to my Honeypot, which is not in China, using an exclusively Chinese character set?
I also apply this as a filter in Kibana to narrow our results to 8 Records:
...