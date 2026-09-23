---
title: One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor
url: https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:53.968761
---

# One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [One Hidden Meta Muse Setting Could Let Attackers Turn the AI Assistant Into a Backdoor](https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html)

**Swati Khandelwal**Sep 22, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjZLVTtI-AEbGRQqJ7aGa0tbXedD5L6P7VCEKIOGXOBZe7S3mhA-PnoHVEoZf3LBMzhcZSIX5sCTveGyZ-8qAqyAVaMXfEoxPL70OIESq-Iolqjkv8GuDjcVs1Jgh3k3SoOOGPDWFr6Lmk83avLqG1whcaiDclv5waXYhCuEqXk569wfwV8Ilrmvv3IKE/s1700-nu-rw-lo-l85-e365/muse.jpg)

Malware already running on a Mac can quietly take over Meta's Muse assistant and use the broad access its owner granted the app, security researcher Patrick Wardle has shown in a [proof-of-concept](https://github.com/pwardle/not-a-mused) released on September 21.

It works by changing a hidden setting so that when the user taps the microphone and dictates a prompt, the words go to the attacker instead of Meta.

The flaw is in the Mac version of Muse, and it only works if an attacker can already run code as the logged-in user. It cannot break into a Mac on its own. But Wardle told The Hacker News that a remote attacker could hijack Muse and steal its token through a ClickFix trick, which fools the user into running a single command with nothing to download or install.

Muse is the personal AI agent Meta [launched this month](https://www.pbs.org/newshour/nation/meta-launches-personal-ai-agent-muse-to-help-with-everyday-tasks) in the United States. Once a user turns it on, it can work across their files, email, messages, calendar, shopping and smart-home apps, using whatever access the person chooses to give it.

That access is the point, Wardle says. He urged people not to install Muse, calling it "trivial to turn Muse into the ultimate backdoor."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

macOS normally prevents one app from accessing another app's files, microphone, camera, or saved logins, so ordinary malware is limited in what it can access. An attacker who can quietly steer Muse instead gets everything the user allowed the app to do.

Wardle also warns that security software may not notice, because the commands come from Muse, a normal signed app, rather than from something that looks like malware.

The setting he found is undocumented and decides where Muse sends dictation. It is stored in the Mac app's preferences under the name *endo\_voyager\_dictation\_endpoint*, and any program running as the logged-in user can point it at an address the attacker controls, without needing extra permissions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOw30LVUstcu3e_dWWp9dyEepm3SJaqSLmwrDY-0xTlbuEcAwhwwprHZNC0kHloSzdCmulRsHbqncfULXcA6kYuOC0S3_v6j7oCh6aTdeheFsS6d5fv9OJTo4jmpZHbh386R7hSlplIj_FtPv0g5Vc3Jf6gaC5Sr9vNxnljVS2QL16iCFIpqKt5Bdv0GE/s1700-nu-rw-lo-l85-e365/options.jpg)

After that, the dictation no longer goes to Meta. When the user speaks a prompt, the audio and the text go to a small program the attacker is running on the same Mac.

From there, Wardle showed three things an attacker can do: read what the user dictated, add extra instructions that Muse trusts and acts on, and capture a token that signs in to the user's Muse account, then use it to read the account's chat history and control the assistant directly.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiI6G3JPnGD6rNboyAMOiNj4VqZ1PqYf8dkOeYNIExXAZ6fKa7pb4-cfq6WkGoi9bfH5BUDE1BIv7VsN3rIiF1iLvoxLLh_CCJ9AC73l36mDz-XmUczi3F7BmB01qpcPl6Yaj9RLrX1QoXyA_CzmamC5tV-pEQ8LFYPn90m1SS0pPdh1kyChTwI0fjIDBKj/s1700-nu-rw-lo-l85-e365/iphones.jpg)

Because a Muse account can be signed in on multiple devices, an attacker with the token can give orders to Muse on any of them, not just the Mac, Wardle said. He used it to direct the Muse app on his own iPhone to report its exact location, run a Bluetooth scan of nearby devices, and list the smart-home commands it could send. In his tests, the assistant only drafted messages rather than sending them on its own.

Wardle also pointed to what the attack does not do. It does not defeat the part of macOS that stops one app from reading another app's saved passwords and tokens. Muse sends its token along with the redirected dictation, and the attack works by getting Muse to act with access it already has. And it does not show that Meta's cloud system, which the company built to keep each user's agent walled off, was broken.

Wardle said he did not report the flaw to Meta before going public. He chose full disclosure so users would understand the risk, and because it is often the fastest way to get such bugs fixed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/event-security-need)

He said Meta has since pushed out what he called a "fix," pointing to a post on X. The Hacker News could not confirm what the change does and has reached out to Meta for comment. Meta has not published a security advisory.

### What Mac Users Can Do Now

Until Meta confirms a fix, a Mac user can limit the exposure:

* Quit Muse, or remove it.
* Review the apps and permissions Muse holds, and revoke any it does not need, so there is less for an attacker to access.
* If the Mac may already be compromised, treat the Muse account and the accounts connected to it as exposed, and change their passwords.
* Because the attack needs the user to dictate, avoid Muse's voice input, which closes the exact path shown.
* Do not run commands that a website or message tells you to paste into Terminal, which is how a ClickFix attack starts.

Meta has put a lot of weight on Muse's security. It built the agent to run in a separate cloud system that keeps each user's data apart from others, with a checking layer meant to approve the actions Muse takes. This flaw sits in the Mac app instead, not in that cloud design.

Wardle argues Meta cre...