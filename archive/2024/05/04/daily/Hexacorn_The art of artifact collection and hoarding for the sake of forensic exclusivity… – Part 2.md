---
title: The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 2
url: https://www.hexacorn.com/blog/2024/05/03/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-2/
source: Hexacorn
date: 2024-05-04
fetch_date: 2025-10-06T17:15:51.383403
---

# The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 2

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

[← Previous](https://www.hexacorn.com/blog/2024/05/02/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity/)
[Next →](https://www.hexacorn.com/blog/2024/06/05/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-3/)

# The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 2

Posted on [2024-05-03](https://www.hexacorn.com/blog/2024/05/03/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-2/ "11:29 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In the [first part](https://www.hexacorn.com/blog/2024/05/02/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity/) I had promised that I would demonstrate that the piracy is good! (sometimes)

I kinda lied back there, but I am not going to lie today: I will tell you all about it in the part 3.

Forensic data hoarding has a lot of benefits. It helps to solve many very common yet often difficult problems (I will cover one of them later in this post), and it also has a nice side-effect to it – it makes us more aware of available forensic artifacts and the fact that there is, or at least should be a very basic need to collect data for everyone in this field.

For example, I keep reminding everyone who wants to listen that there are many [localized](https://www.hexacorn.com/blog/2023/03/10/threat-hunting-localization-issues/) versions of Windows, and there are lots of [architectural](https://www.hexacorn.com/blog/2023/05/04/threat-hunting-architecture-issues/) quirks around OS folders as well. Yes, it means that your *c:\Program Files* folder name, same as many others, can be localized and often is. This doesn’t stop people from continuing to write English-centric detections, but at least my conscience is clean…

I mentioned these common yet often difficult problems… Let’s focus on one of them for a moment.

When you analyze malware you often come across code that focuses on terminating processes and/or stopping and/or removing services (service processes). The easy ones do it by the book — they use direct string comparisons, Windows APIs. and the list of targets are often present inside the malware in a form of a string list. The more advanced ones use various hashing algorithms for comparison, and instead of actual strings they store hashes identifying the targets inside the malware samples.

As analysts looking at such hash lists we face an obvious challenge – given a list of hashes, how can we reconstruct a list of strings that these hashes were generated from?

This may sound easy, but it is not. We can brute-force all combinations, but it often can turn to be very costly, plus brute-force attack may end up with a list of random process names for which a calculated hash happens to be identical with the one on the target list, but may not be a correct one (so-called [hash collision](https://en.wikipedia.org/wiki/Hash_collision)). A more promising approach here relies on a dictionary attack where we compute hashes for all the possible known process names, and then compare against the targets, but it’s not easy either…

Why?

For the latter to be successful, one needs a large list of legitimate process names in a first place. Googling around and github searches may give you a head start, but it’s often not enough. Yes, many of these process names are often related to security software so an extensive list of process names used by antivirus, edr, firewall, etc. software may help, but it’s often not enough. Nowadays, the target lists are often far wider than that – f.ex. ransomware often kills many other programs as well: multiple variants of Office software, database software, various backup services, email clients, and so on and so forth.

It’s time for a recipe.

If you were about to collect the largest list of process names, how would you do it?

The below list is not extensive, but may help you out:

* Find your first list of interesting process names 🙂
* Use a set of the most unique process names from that list and Google it
* Search github repositories as well

Chances are, that a set of these will lead you to many interesting process lists.

And now you have your base. It is probably around 1% of all the process names that you want though…

So… we dig deeper.

* Web scrap data – there are a lot of websites out there that somehow managed to accumulate a lot of process names; they use it to generate tremendous number of landing pages that search engines will hit when people search for issues related to various software packages; these sites are trash of the internet, but in this particular case, they are great as we can leverage all these landing pages to collect more process names
* Download software and driver repositories and post-process them – many installers can be now unpacked and their metadata and installer scripts can be extracted and analyzed – they are a very juicy material for building database of process names
* Analyze large corpora of malware samples – for every advanced and complex malware family you will find 10 if not 100 dumb families that do it all in the open and include target process and/or service list in plain text – easy to extract and collect
* If you got access to any telemetry – from EDR, sysmon, 4688 – extract that process lists as well and best — do it on regular basis
* Web scrap forums for [HijackThisLog](https://www.google.com/search?q=HijackThis+Log) reports – old, but helpful
* Web scrap forums for [OTL logfile](https://www.google.com/search?q=OTL+logfile) reports – as above
* Post-process bundles of [CyberSecurity reports](https://github.com/aptnotes/data) – they often reference a lot of interesting process and service names
* Actively install software of interest and gather list of processes and services they create – nuh, just kidding, this takes too much time

My personal process list is 1.7M items long. I used it to crack quite a few malware families’ target lists. Yet it still fails me sometimes. Yes, the hoarding never stops.

This entry was posted in [Clustering](https://www.hexacorn.com/blog/category/clustering/), [Forensic Analysis](https://www.hexacorn.com/blog/category/forensic-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/05/03/the-art-of-artifact-collection-and-hoarding-for-the-sake-of-forensic-exclusivity-part-2/ "Permalink to The art of artifact collection and hoarding for the sake of forensic exclusivity… – Part 2").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")