---
title: Validating Tools
url: http://windowsir.blogspot.com/2023/02/validating-tools.html
source: Instapaper: Unread
date: 2023-02-07
fetch_date: 2025-10-04T05:54:28.103822
---

# Validating Tools

# [Windows Incident Response](http://windowsir.blogspot.com/)

The Windows Incident Response Blog is dedicated to the myriad information surrounding and inherent to the topics of IR and digital analysis of Windows systems. This blog provides information in support of my books; "Windows Forensic Analysis" (1st thru 4th editions), "Windows Registry Forensics",
as well as the book I co-authored with Cory Altheide, "Digital Forensics with Open Source Tools".

## Sunday, February 05, 2023

### Validating Tools

Many times, in the course of our work as analysts (SOC, DFIR, etc.), we run tools...and that's it. But do we often stop to think about *why* we're running *that* tool, as opposed to some other tool? Is it because that's the tool everyone we know uses, and we just never thought to ask about another? Not so much the *how*, but do we really think about the *why*?

The big question, however, is...do we validate our tools? Do we verify that the tools are doing what they are supposed to, what they should be doing, or do we simply accept the output of the tool without question or critical thought? Do we validate our tools against our investigative goals?

Back when [Chris Pogue](https://www.linkedin.com/in/christopher-pogue-6148441/) and I were working PCI cases as part of the IBM ISS X-Force ERS team, we ran across an instance where we really had to dig in and verify our toolset. Because we were a larger team, with varying skill levels, we developed a process for all of the required searches, scans and checks (search for credit card numbers, scans for file names, paths, hashes, etc.) based on Guidance Software's EnCase product, which was in common usage across the team. As part of the searches for credit card numbers (CCNs), we were using the built-in function *isValidCreditCard()*. Not long after establishing this process, we had a case where JCB and Discover credit cards had been used, but these weren't popping up in our searches.

Chris and I decided to take a look at this issue, and we went to the brands and got test card numbers...card numbers that would pass the necessary checks (BIN, length, Luhn check), but were not actual cards used by consumers. We ran test after test, and none using the *isValidCreditCard()* returned the card numbers. We tried reaching out via the user portal, and didn't get much in the way of a response that was useful. Eventually, we determined that those two card brands were simply not considered "valid" by the built-in function, so we overrode that function with one of our one, one that included 7 regexes in order to find *all* valid credit card numbers, which we verified with some help from [a friend](https://www.linkedin.com/in/lamueller/).

We learned a hard lesson from this exercise, one that really cemented the adage, "verify your tools". If you're seeing (or not, as the case may be) something that you don't expect to see in the output of your tools, verify the tool. Do not assume that the tool is correct, that the tool author knew everything about the data they were dealing with and had accounted for edge cases. This is not to say that tool authors aren't smart and don't know what they're doing...not at all. In fact, it's quite the opposite, because what can often happen is that the data changes over time (we see this a LOT with Windows...), or there are edge cases that the tool simply doesn't handle well.

So we're not just asking about the general "verify your tools" adage; what we're really asking about is, "do you verify your tools against your investigative goals?". The flip side of this is that if you can't articulate your investigative goals, why are you running any tools in the first place?

Not long ago, I was working with someone who was using a toolset built out of open source and free tools. This toolset included a data collection component, middleware (parsed the data), and a backend component for engaging with and displaying the parsed data. The data collection component included retrieving a copy of the WMI repository, and I asked the analyst if they saw any use of WMI persistence, to which they said, "no". In this particular case, open reporting indicated that these threat actors had been observed using WMI for persistence. While the data collection component retrieved the WMI repository, the middleware component did not include the necessary code to parse that repository, and as such, one could not expect to see artifacts related to WMI persistence in the backend, even if they did exist in the repository.

The issue was that we often expect the tools or toolset to be complete in serving our needs, without really understanding those "needs", nor the full scope of the toolset itself. Investigative needs or goals may not be determined or articulated, and the toolset was not validated against investigative goals, so assumptions were made, including ones that would lead to incomplete or incorrect reporting to customers.

*Going Beyond Tool Validation to Process Validation*

Not long ago, I [included a question](https://twitter.com/keydet89/status/1619310309520580608) in one of my tweet responses: "how would you use RegRipper to check to see if Run key values were disabled?" The point of me asking that question was to determine who was just running RegRipper because it was cool, and who was doing so because they were trying to answer investigative questions. After several days of not getting any responses to the question (I'd asked the same question on LinkedIn), I posed the question directly to Dr. Ali Hadi, who responded by [posting a YouTube video](https://twitter.com/binaryz0ne/status/1621032430135304192) demonstrating how to use RegRipper. Dr. Hadi then [posted a second YouTube video](https://twitter.com/binaryz0ne/status/1621384708452925440), asking, "did the program truly run or not?", addressing the issue of the [StartupApproved\Run](https://windowsir.blogspot.com/2022/07/startupapprovedrun-pt-ii.html) key.

The point is, if you're running RegRipper (or any other tool for that matter), *why* are you running it? Not *how*...that comes later. If you're running RegRipper thinking that it's going to address all of your investigative needs, then how do you know? What are your "investigative needs"? Are you trying to determine program execution? If so, [the plugin Dr. Hadi illustrated](https://github.com/keydet89/RegRipper3.0/blob/master/plugins/run.pl) in both videos is a great place to start, but it's nowhere near complete.

You see, the plugin will extract values from the keys listed in the plugin (which Dr. Hadi illustrated in one of the videos). That version includes the *StartupApproved\Run* key in the plugin, as well, as it was added before I had a really good chance to conduct some more comprehensive testing with respect to that key and it's values. I've since removed the key (and the other associated keys) from the *run.pl* plugin and moved them to a separate plugin, with associated MITRE ATT&CK mapping and analysis tips.

As you can see from Dr. Hadi's YouTube video, it would be pretty elementary for a threat actor to drop a malware executable in a folder, and create a Run key value that points to it. Then, create a *StartupApproved\Run* key value that disables the Run key entry so that it doesn't run. What would be the point of doing this? Well, for one, to create a distraction so that the responder's attention is focused elsewhere, similar to what [happened with this engagement](https://www.secureworks.com/blog/ransomware-as-a-distraction).

If you *are* looking to determine program execution and you're examining the contents of the Run keys, then you'd also want to include the *Microsoft-Windows-Shell-Core%4Operational* Event Log, as well, as the event records indicate when the key contents are processed, as well as when execution of individual programs (pointed to by the values) began and completed. This is a great way to determine program execution (not just "maybe it ran"), as well as t...