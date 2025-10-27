---
title: Computer Repair Technicians Are Stealing Your Data
url: https://www.schneier.com/blog/archives/2022/11/computer-repair-technicians-are-stealing-your-data.html
source: Schneier on Security
date: 2022-11-29
fetch_date: 2025-10-04T00:01:28.817833
---

# Computer Repair Technicians Are Stealing Your Data

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Computer Repair Technicians Are Stealing Your Data

Laptop technicians [routinely violate the privacy](https://arstechnica.com/information-technology/2022/11/half-of-computer-repairs-result-in-snooping-of-sensitive-data-study-finds/) of the people whose computers they repair:

> Researchers at University of Guelph in Ontario, Canada, recovered logs from laptops after receiving overnight repairs from 12 commercial shops. The logs showed that technicians from six of the locations had accessed personal data and that two of those shops also copied data onto a personal device. Devices belonging to females were more likely to be snooped on, and that snooping tended to seek more sensitive data, including both sexually revealing and non-sexual pictures, documents, and financial information.
>
> […]
>
> In three cases, Windows Quick Access or Recently Accessed Files had been deleted in what the researchers suspect was an attempt by the snooping technician to cover their tracks. As noted earlier, two of the visits resulted in the logs the researchers relied on being unrecoverable. In one, the researcher explained they had installed antivirus software and performed a disk cleanup to “remove multiple viruses on the device.” The researchers received no explanation in the other case.
>
> […]
>
> The laptops were freshly imaged Windows 10 laptops. All were free of malware and other defects and in perfect working condition with one exception: the audio driver was disabled. The researchers chose that glitch because it required only a simple and inexpensive repair, was easy to create, and didn’t require access to users’ personal files.
>
> Half of the laptops were configured to appear as if they belonged to a male and the other half to a female. All of the laptops were set up with email and gaming accounts and populated with browser history across several weeks. The researchers added documents, both sexually revealing and non-sexual pictures, and a cryptocurrency wallet with credentials.

A few notes. One: this is a very small study—only twelve laptop repairs. Two, some of the results were inconclusive, which indicated—but did not prove—log tampering by the technicians. Three, this study was done in Canada. There would probably be more snooping by American repair technicians.

The moral isn’t a good one: if you bring your laptop in to be repaired, you should expect the technician to snoop through your hard drive, taking what they want.

Research [paper](https://arxiv.org/pdf/2211.05824.pdf).

Tags: [computer security](https://www.schneier.com/tag/computer-security/), [privacy](https://www.schneier.com/tag/privacy/)

[Posted on November 28, 2022 at 10:44 AM](https://www.schneier.com/blog/archives/2022/11/computer-repair-technicians-are-stealing-your-data.html) •
[19 Comments](https://www.schneier.com/blog/archives/2022/11/computer-repair-technicians-are-stealing-your-data.html#comments)

### Comments

Doug •
[November 28, 2022 11:29 AM](https://www.schneier.com/blog/archives/2022/11/computer-repair-technicians-are-stealing-your-data.html/#comment-413048)

This is why I always remove disk drive before giving laptop to repair in case of hardware problems.

Clive Robinson •
[November 28, 2022 12:10 PM](https://www.schneier.com/blog/archives/2022/11/computer-repair-technicians-are-stealing-your-data.html/#comment-413051)

@ Bruce,

With regards,

> “Laptop technicians routinely violate the privacy of the people whose computers they repair”

All humans are “curious” those that can “fault find” tend to be way more curious than most, it’s what makes them able to do the job.

What is not mentioned is how old and the sex of the repair technicians.

I’m guessing male and not very old, maybe not even “out of college” age.

Lets just say I would not be overly surprised if their “morals” were not as advanced as say a father.

Which brings us to,

> “Three, this study was done in Canada. There would probably be more snooping by American repair technicians.”

Why would you think that?

Could it be connected to the fact that the US divorce rate for infidelity in the US is alleged to be the highest per capiter. Further that the data from “illicit date” web sites, indicate a very high level of marital infidelity / partner cheating in certain classes of US males?

Also “the boys and their toys” issue, suggesting that a higher number of US males do not develop socially much beyond adolescent behaviour?

Or could it be that there is something in the US life style and education that actively promotes those of the “Dark Tetrad” of mental deficiencies?

If I had to bet the price of a cup of tea, it would be towards the last one “life style and education”. The “every man as an island” giving rise to a “Me first” self entitlment is at best asocial if not antisocial and you would expect it to exhibit in a lack of morals towards others in society…

Finley •
[November 28, 2022 12:26 PM](https://www.schneier.com/blog/archives/2022/11/computer-repair-technicians-are-stealing-your-data.html/#comment-413052)

@ Doug,

> This is why I always remove disk drive before giving laptop to repair in case of hardware problems.

I thought that was obvious when I did it as a kid, 25 years ago, but non-removable and difficult-to-remove SSDs will make this less practical. One can’t always just press a tab or undo a screw to remove a laptop or phone’s storage device (or battery) anymore. And how easy is it to disable an automatic cloud login if the device won’t turn on? (Ideally, one could log in from another device to do it; I don’t use these services, so I don’t know.)

What’s happening is not “stealing” or “taking” of data, though, and it’s misleading to call it that. If data were stolen, it would be obvious: the owner would find things missing. This is an invasion of privacy and an unauthorized copying of data, and in Canada or Europe could be litigated as such (but not as larceny). The USA should really have a federal privacy law, beyond overly specific ones such as the Video Privacy Protection Act and Health Insurance Portability and Accountability Act that probably won’t apply.

As for clearing logs, recently accessed files, etc., I don’t think that implies anything nefarious. From my point of view, these are privacy-invading features that nobody wanted and most people don’t use, though they have vague worries about this data collection (“In case I die in this mess, clear my browser history” or “destroy my hard drive” has become a trope at this point—yet I’ve never seen anyone actually use browser history other than the “back” button). I have the habit of clearing these things when I find them. Maybe it’s the same for these technicians, or they just don’t want internal URLs or the history of their failed repair attempts recorded. Maybe people have brought devices back and complained about incomplete fixes when errors remained visible in the logs;...