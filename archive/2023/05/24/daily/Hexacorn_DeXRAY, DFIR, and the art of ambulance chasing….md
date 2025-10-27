---
title: DeXRAY, DFIR, and the art of ambulance chasing…
url: https://www.hexacorn.com/blog/2023/05/23/dexray-dfir-and-the-art-of-ambulance-chasing/
source: Hexacorn
date: 2023-05-24
fetch_date: 2025-10-04T11:38:53.278944
---

# DeXRAY, DFIR, and the art of ambulance chasing…

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

[← Previous](https://www.hexacorn.com/blog/2023/05/17/blue-teaming-its-data-complicated/)
[Next →](https://www.hexacorn.com/blog/2023/06/01/analysing-ps2exe-executables/)

# DeXRAY, DFIR, and the art of ambulance chasing…

Posted on [2023-05-23](https://www.hexacorn.com/blog/2023/05/23/dexray-dfir-and-the-art-of-ambulance-chasing/ "10:56 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Pretty much all of my [DeXRAY posts](https://www.hexacorn.com/blog/?s=dexray) ever published been focusing on new versions of this tool being released. Today I will talk about the ‘making of the sausages’ part of this process, aka how DeXRAY came to be.

If you have been working in a DFIR space for more than a decade you probably already know that any type of high-fidelity evidence found on an endpoint is gold, and Quarantine folders/files are one of the best in this category… These are locations where security software stores intercepted/blocked/quarantined files. Before the strong adoption of NextGen, EDR the AV products used to catch many malware files ‘just in time’, then encrypt their content, often move them to a ‘special safe location’, and delete them from their original location. And yes, these encrypted files (most of the time) can be decrypted by DeXRAY….

Despite this informative intro you may still ask… why do we even need talk about Quarantine files and folders today?

First of all, I believe not every DFIR analyst is aware of these file system locations. And as the time goes by, probably less and less of them, as well. It’s a knowledge of the past, after all. Moreso, in a world of ever-changing landscape that is affecting not only the actual threats, but also security solutions, it’s not uncommon for the following events to occur:

* multiple security solutions installed on the same host, plus
  + installation of one, doesn’t imply the older one was (fully) uninstalled! that is, there may be remnants of the old security solution still present on the system, not only the program binaries, configuration, but also quarantined files!
* different polices used by these security solutions may cause interesting interference (f.ex. exclusion policies for directories/files in one may suppress some detections, but still trigger other detections in another solution)
* some DFIR analysts can actually miss an opportunity to discover these existing quarantined files, because they simply don’t know about them!

So, if you want to improve your chances of detecting something interesting on the endpoint you investigate, this post is for you.

And yes, we are ambulance chasing, but for a good reason! Discovering that someone else (meaning: some other software) had discovered something before us is actually NOT A BAD THING. I would go as far as to say that while discovering and analysing quarantined files is being a bit of cheating, it may actually cut down a lot of analysis time in some cases. And in the DFIR world, time is really of essence.

The ambulance chasing rule #1 is that when you process your evidence, make sure you pay attention to these low-hanging fruits and nuggets…

Before I go into gore details, let me digress to deliver a personal rant: analysing paths where security software stores its quarantined files is not easy in 2010s/2020s. It requires a lot of patience, plus some more. The security solutions of ‘today’ migrated away from the golden era of 90s/2000s. Big time. Yup, while in the past you would download the software and just install it, today you can’t install anything w/o creating an online account at least, and/or (pre- or) paying for a subscription, even if just for a test period (credit card authorizations). So, if you want to try yourself – you have been warned: I went through hell of doing it for many security solutions and do not recommend. For realz, you are going to be exposed to a lot of b/s and ‘I really don’t wanna do it’ equilibristics. Plus, some solutions use consoles that are no longer present on the client side (endpoint) either, and have been moved to the server-side, so you will actually need these b/s online accounts — yes, the temp emails, phone numbers won’t cut it. Let me be blunt and say it’s actually quite an experience to install many of the security software packages of today w/o getting seriously pissed off… Now, imagine you are that damsel in distress, you know nothing about security, but you suspect you got hit by some malware/hacking attacks and want to purchase a security solution to help you with your problem. I am feeling very very sorry for you in 2023… Anyway… this is the end of the rant 🙂

The good news is that from a forensic investigators’ perspective, these solutions have already been (pre)installed on the systems you analyze. As such, we just need to find these quarantined folders/files!

Here are the rules:

* If part of the directory / folder refers to ‘/.\*?Quarantine/’ — check it!
* If part of the directory / folder refers to ‘/chest/’ — check it!
* If part of the directory / folder refers to ‘/QB/’ — check it!
* If part of the directory / folder refers to ‘/Infected/’ — check it!
* If part of the directory / folder refers to ‘/Backup/’ — check it!
* If part of the directory / folder refers to ‘/$360Section/’ — check it!
* If part of the directory / folder refers to ‘/fq/’ — check it!
* If part of the directory / folder refers to ‘/qv/’ — check it!
* If part of the directory / folder refers to ‘/Jail/’ — check it!
* If part of the directory / folder refers to ‘/Safestore/’ — check it!
* if the file extension is one of these
  + ‘.v3b’, ‘.eqf’, ‘.qua’, ‘.qv’, ‘.bdq’, ‘.q’, ‘.cmc’, ‘.vir’, ‘.ifc’, ‘.nqf’, ‘.tmp’ (with a header ‘KSS’), ‘.klq’, ‘.qnt’, ‘.bin’ (with a file name being a hash), ‘.lqf’, ‘.quar’, ‘.data’, ‘.bup’, ‘.mal’, ‘.exv’, ‘.dlv’, ‘.virus’, ‘.infected’, ‘.malware’, ‘.suspicious’, ‘.sdb’, ‘.qbd’, ‘.qbi’, ‘.idx’, ‘.qtn’, ‘.vbn’, ‘quarantine.db’ — check it !!!

I’d love to say – you see? it’s that simple. Yet, I know it is not. Still… happy ambulance chasing!

There you have it. It was that easy.

This entry was posted in [DeXRAY](https://www.hexacorn.com/blog/category/software-releases/dexray/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/05/23/dexray-dfir-and-the-art-of-ambulance-chasing/ "Permalink to DeXRAY, DFIR, and the art of ambulance chasing…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")