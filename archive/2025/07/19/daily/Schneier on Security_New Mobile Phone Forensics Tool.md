---
title: New Mobile Phone Forensics Tool
url: https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html
source: Schneier on Security
date: 2025-07-19
fetch_date: 2025-10-06T23:54:32.828749
---

# New Mobile Phone Forensics Tool

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

## New Mobile Phone Forensics Tool

The Chinese have a new tool called [Massistant](https://www.lookout.com/threat-intelligence/article/massistant-chinese-mobile-forensics).

> * Massistant is the presumed successor to Chinese forensics tool, “MFSocket”, reported in 2019 and attributed to publicly traded cybersecurity company, Meiya Pico.
> * The forensics tool works in tandem with a corresponding desktop software.
> * Massistant gains access to device GPS location data, SMS messages, images, audio, contacts and phone services.
> * Meiya Pico maintains partnerships with domestic and international law enforcement partners, both as a surveillance hardware and software provider, as well as through training programs for law enforcement personnel.

From a [news article](https://techcrunch.com/2025/07/16/chinese-authorities-are-using-a-new-tool-to-hack-seized-phones-and-extract-data/):

> The good news, per Balaam, is that Massistant leaves evidence of its compromise on the seized device, meaning users can potentially identify and delete the malware, either because the hacking tool appears as an app, or can be found and deleted using more sophisticated tools such as the [Android Debug Bridge](https://developer.android.com/tools/adb), a command line tool that lets a user connect to a device through their computer.
>
> The bad news is that at the time of installing Massistant, the damage is done, and authorities already have the person’s data.

Slashdot [thread](https://yro.slashdot.org/story/25/07/16/2042245/chinese-authorities-are-using-a-new-tool-to-hack-seized-phones-and-extract-data).

Tags: [China](https://www.schneier.com/tag/china/), [forensics](https://www.schneier.com/tag/forensics/), [hacking](https://www.schneier.com/tag/hacking/), [malware](https://www.schneier.com/tag/malware/), [privacy](https://www.schneier.com/tag/privacy/), [smartphones](https://www.schneier.com/tag/smartphones/)

[Posted on July 18, 2025 at 7:07 AM](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html) •
[5 Comments](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html#comments)

### Comments

Celos •
[July 18, 2025 7:33 AM](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html/#comment-446590)

Well, the usual advice is “do not trust your phone”. Used to be mainly for criminals, but now definitely applies to everybody. Dark times.

K Campbell •
[July 18, 2025 8:58 AM](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html/#comment-446591)

Android only, not iOS, correct?

Clive Robinson •
[July 18, 2025 9:10 AM](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html/#comment-446592)

@ Celos, ALL,

With regards,

> ‘Well, the usual advice is “do not trust your phone”’

Well it’s out of date by a long ways…

It should now be,

**“Do not trust your devices or cards”**

At the very least.

Even most modern microcontrollers contain the ability to communicate by EM Radiation…

So you just need a wire trace or coil on a PCB to act as an antenna.

Such devices can and do work from Long Wave Frequencies well below the “Medium Wave”(MW) band for “Near Field” communications. And likewise into the mid “High Frequencies”(HF) for “Radio Frequency ID”(RFID) devices similar to those used in passports. Then up through the Mobile Phone, WiFi and “Industrial Scientific and Medical”(ISM) bands into the low microwave bands.

Keeping track on what even your “portable radio” transmits as a Bluetooth signal supposedly just for speakers and ear buds can be more than a full time job.

Remember that all those “apps” can act as repeaters. Such that a BlueTooth channel can be received and then broadcast as a WiFi or Mobile signal is relatively trivial this century.

Worse is the idea of the “electronic rock” that the UK SiS developed to be used in Moscow. It acted as a repeater “but” it would “Store and Forward” sensitive data.

So you could eat a sandwich in the park mid day and upload data to the rock. But importantly have the rock save the data such that it would upload it to another device hours or days away.

Needless to say the Russian security forces realised what was going on thus could identify “Persons of Interest” for further attention upto and including FFF for “Find Fix and Finish” where the “Finish” could be upto and including “high velocity lead poisoning”…

But even modern “White Goods” in the Kitchen have such radio interfaces in them. And some TV’s and other entertainment devices.

As was noted a week or three back, pretty much any recent “consumer device” in your home or coat pocket can do all of this for less than 1USD increase in retail price…

lurker •
[July 18, 2025 1:52 PM](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html/#comment-446596)

@K Campbell

The article appears to discuss only Android, but given the popularity of iPhone in China I would expect an iOS version is lurking in the wild waiting to be discovered.

not important •
[July 19, 2025 6:42 PM](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html/#comment-446619)

<https://www.technologyreview.com/2025/06/23/1118401/privacy-book-reviews-surveillance-higher-education/>

=While most of us are at least vaguely aware that our phones and apps are a vector for data collection and tracking, both the way in which this is accomplished and the extent to which it happens often remain murky. Purposely so, argues Tau. In fact, one of the

[![Atom Feed](https://www.schneier.com/wp-content/themes/schneier/assets/images/rss.png)
Subscribe to comments on this entry](https://www.schneier.com/blog/archives/2025/07/new-mobile-phone-forensics-tool.html/feed/)

## Leave a comment [Cancel reply](/blog/archives/2025/07/new-mobile-phone-forensics-tool.html#respond)

[Blog moderation policy](https://www.schneier.com/blog/archives/2024/06/new-blog-moderation-policy.html)

[Login](https://www.schneier.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.schneier.com%2Fblog%2Farchives%2F2025%2F07%2Fnew-mobile-phone-forensics-tool.html "Login")

Name

Email

URL:

[ ]  Remember personal info?

Fill in the blank: the name of this blog is Schneier on \_\_\_\_\_\_\_\_\_\_\_ (required):

Comments:
![](https://www.schneier.com/wp-content/themes/schneier/assets/images/loader.gif)

**Allowed HTML**
<a href="URL"> • <em> <cite> <i> • <strong> <b> • <sub> <sup> • <ul> <ol> <li> • <blockquote> <pre>
**Markdown Extra** syntax via <https://michelf.ca/projects/php-markdown/extra/>

Δ

[← Security Vulnerabilities in ICEBlock](https://www.schneier.com/blog/archives/2025/07/security-vulnerabilities-in-iceblock.html) [Friday Squid Blogging: The Giant Squid Nebula →](https://www.schneier.com/blog/archives/2025/07/friday-squid-blogging-the-giant-squid-nebula.html)

Sidebar photo of Bruce Schneier...