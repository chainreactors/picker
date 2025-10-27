---
title: Extracting Practical Observations from Impractical Datasets, (Thu, Jan 16th)
url: https://isc.sans.edu/diary/rss/31582
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-17
fetch_date: 2025-10-06T20:13:36.214146
---

# Extracting Practical Observations from Impractical Datasets, (Thu, Jan 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31580)
* [next](/diary/31586)

# [Extracting Practical Observations from Impractical Datasets](/forums/diary/Extracting%2BPractical%2BObservations%2Bfrom%2BImpractical%2BDatasets/31582/)

**Published**: 2025-01-16. **Last Updated**: 2025-01-16 02:43:03 UTC
**by** [Curtis Dibble, SANS.edu BACS Student](/handler_list.html#curtis-dibble,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Extracting%2BPractical%2BObservations%2Bfrom%2BImpractical%2BDatasets/31582/#comments)

[This is a Guest Diary by Curtis Dibble, an ISC intern as part of the SANS.edu BACS [1] program]

**![](https://isc.sans.edu/diaryimages/images/2025-01-16_figure1_v2.png)
Figure 1: A heatmap showing the date and frequency a given set of commands input to the honeypot**

Spoiler alert, sugar costs money, and syntactic sugar is the most expensive type. Fortunately, we live in an era where a developer’s laptop tends to come with resources unheard of in the server realm a decade ago [2] and a vibrant open-source community to make use of all that shiny new silicon. All that sweet, sweet, free and open source software living under the umbrella of the MIT and GNU Affero General Public License (commonly known as the AGPL) license agreements is a godsend to both the amateur and professional cyber practitioner - until it isn’t. Which brings us to the crux of the issue and why this article exists in the first place. Smarter and more experienced people than myself have been writing and discussing this for the last twenty five years or more, but the simplest explanation is that cybersecurity as an industry suffers from a relationship with Not-Invented-Here Syndrome [3][4] that’s dysfunctional enough to warrant its own definition in the DSM-V (Diagnostic and Statistical Manual of Mental Disorders v5). A significant portion of that stems from the wildly different origin stories of practitioners. From administrative professionals to software engineers, network admins to high school dropouts, the value of their contributions lies in the varied life experience and broad spectrum of perspectives. The conflict, however, is the age old problem of buy-vs-build.

To lay out the problem with examples, I’ll start with my own experience. Folks without extensive programming history tend to reach for the ‘buy’ or ‘off the shelf’ button to solve a problem, while anyone that’s written enough scripts (myself included…) will have a text editor with some boilerplate ready faster than Shodan can advertise unprotected RDP (Remote Desktop Protocol) access. Using off the shelf open source is usually the right answer - if for no other reason than to see whether an idea has merit. At some point though, the internals need customization and optimization to handle the problem, or open up options to integrate with other tools for deeper insights and fresh opportunities. To make that a little more concrete, I have nothing but praise for David Fitzmaurice and the work he’s done to weld together Zeek, Snort, and Grafana [5] with a little help from ChatGPT to dial it in. This is the right answer. Use best in breed tooling where you can, and tailor the important parts to the mission. Scott Jensen did exactly this with the DShield-SIEM project [6][7] and leaned hard on Elastic’s ELK (Elasticsearch, Logstash, Kibana) stack [8] as the implementation toolkit. Getting a working version of an idea off the ground is one of the hardest things around, but once it’s gained traction, the problem shifts to one of maintaining scope. Again, as a concrete example Joel Spolsky [2] made the point that Excel had a bespoke C compiler. Which, while that limits the scope, flexibility, and accessibility, it means that at one point, the internals of the bane of modern work were incredibly impressive before becoming just another fancy XML parser.

## Thoughts and Background

Expanding on that, we have plenty of tools, one-offs, and live with the near axiomatic fact that there are no one-size-fits-all solutions in this arena. ELK stack is mentioned often enough as the standard for security or general purpose analytics work. The problem with this - and the state of SIEM (Security Information and Event Management) or SOAR (Security Orchestration Automation and Response) solutions in general - is that storage, compute, and memory have become cheap enough to leave data in the native format which it was collected, and then reparse on update or cache results in temporary storage. I’ve dealt with this personally using the IBM QRadar [9] platform, waiting patiently for it to skim and then collate results from dozens of terabytes of flat files using regular expressions. That wouldn’t be an issue if it was at least fast for the end user, and scaling didn’t imply a choice between massive capital expenditures for more licenses and hardware vs paying for additional cloud services. At the end of the day, this is one  root cause of issues in the Information Age. In other words, there are professional tools that exist and scale, they are prohibitively expensive for all but the largest players, the only solution anyone is willing to try at scale involves throwing more servers at the problem, and nobody is interesting in solving these combined issues. I built the parts included in this article and published the repository at the end to act as a foundation for practitioners to at least try something different.

## Moving on

Admittedly, I have a few hesitations when using Docker-based products after dealing with them in production, which is one of the reasons for steering clear of the existing DShield-SIEM solution. I also wanted to get more out of the internship than simply observing and reporting. So, using the tools that I knew, I set off to see if it was worth reinventing the wheel, or at least to figure out if there was a better way forward. In the process, I had to apply several years of experiments across different fields to an old problem, and something novel seems to have come out the other end. Fair warning, I am by no stretch a master of SQL. At best, I am a semi-literate student of the language with access to a deep library. To get to this point required extensive study of Joe Celko’s work [10][11], a lot of experimentation, too much time reading SQL Server documentation [12], more Google-fu than I’m willing to admit. Standing up a prototype also meant having *significant* personal infrastructure to fail relentlessly forward. Fortunately, the slimmed down version is laptop friendly.

**![](https://isc.sans.edu/diaryimages/images/2025-01-16_figure2.png)
Figure 2: 60% of the time it happens every time. SQL Server and proper database management systems are memory hogs not meant for consumer hardware. Unless you set the proper constraints and configurations, of course.**

This project never would have forced me to face certain scaling issues without a little help from Jesse La Grew and a massive data dump of logs he provided. After that contribution, I ended up with an additional 11GB of Cowrie, Firewall, and Web/Honeypot logs to work with. There are over 300GB+ of compressed PCAP capture files included, but I have not had the time to create a decent model for them. Onto the meat and potatoes.

The first problem I solved wound up being the key to the entire structure – data deduplication and type-casting. In the end, an IP Address as we recognize it is nothing more than a formatted decimal representation of a binary string with a predefined length. This applies to IPv4 just as much as it does to IPv6 - or even an MD5 hash defining a session identifier. As it turns out, both open source and commercial implementations of SQL are highly optimized to process binary data, and come with extensive libraries of purpose built functions to...