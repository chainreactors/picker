---
title: Hunting for the warez & other dodgy stuff people install / download, part 1
url: https://www.hexacorn.com/blog/2025/03/01/hunting-for-the-warez-other-dodgy-stuff-people-install-download-part-1/
source: Hexacorn
date: 2025-03-02
fetch_date: 2025-10-06T21:57:04.746769
---

# Hunting for the warez & other dodgy stuff people install / download, part 1

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

[← Previous](https://www.hexacorn.com/blog/2025/02/24/dexray-v2-35/)
[Next →](https://www.hexacorn.com/blog/2025/03/08/hunting-for-the-warez-other-dodgy-stuff-people-install-download-part-2/)

# Hunting for the warez & other dodgy stuff people install / download, part 1

Posted on [2025-03-01](https://www.hexacorn.com/blog/2025/03/01/hunting-for-the-warez-other-dodgy-stuff-people-install-download-part-1/ "12:30 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

It is a sad IT fact, but employees install pirated/dodgy software on regular basis and download&execute whatever they want. There is no way to stop them… other than implementing a very strict software installation/program execution policy. Which obviously always ricochets and causes a negative user experience domino effect in any larger company, because employees simply need to install and/or use a lot of different random software, frequently, and often one that has to be installed quickly, ad hoc, to complete the task at hand, often with an aim to respond to client requests.

And support teams tasked with approving these ‘critical’ installs, even in these exemplary tightly controlled environments, are never able to keep up, let alone accurately (‘beyond any doubt’) confirm that this or that, ‘badly needed’ software is ‘safe’. And without such important and appropriate software assessment, all these installs must be treated as a risk…

The existing and more and more popular App Stores make it a bit easier for IT teams to manage this widespread issue, but the reality is that we still have to deal with a lot uncontrollable / unmanaged software installation events that are initiated when users freely download and install their ‘program du jour’ often sourced from questionable sources.

So…

How do we tackle this widespread Acceptable Use Policy (AUP) violation without being seen as a ‘nanny state’? And assuming the worst: an environment where installing a random software is a common event, how do we find the users who try to install pirated or otherwise unwanted software, specifically? And we want to find them not to punish them, but to reduce the attack surface?

The most basic, naive method will focus on telemetry searches for keywords like:

* keygen
* crack
* serial
* warez
* patch

Of course, if you ever searched for these keywords in any larger org telemetry you are intimately familiar with lots of these False Positives:

* red team and pentesting tools (AirCrack, L0phtcrack)
* audio files (Nutcracker by Tchaikovsky)
* documentation (InternetCrackUrl API)
* local repos (sometimes pirated, admittedly) with cyber security courses – with their PDFs and tools referencing many of these keywords (f.ex. CEH materials)
* forensic tools (password crackers)
* random cloned github repos (easily hitting any keyword really)
* e-books (crack <insert topic>, cracking <insert topic>, how to crack <insert topic>, etc.)
* product names (Patchlink)
* legitimate software patches (\*patch\*) including drivers, software updates, KBs, hot fixes, etc.
* legitimate key generating tools f.ex. ssh-keygen
* unexpected ‘false positives’ – matches on ‘wide’ keywords like ‘patch’ that catch things like ‘Dispatch’, ‘DispatcherNet’
* etc.

When you run these naive (yet wide in scope) searches across your org you quickly realize that this is a type of threat hunting exercise where we do not immediately focus on critical/high-fidelity detections, but it’s a more advanced game of tuning the queries, and eyeballing the resulting reports looking for anomalies in an iterative way….The good news is that in my experience, basic telemetry searches focused on these 5 keywords listed above yield a lot of very interesting results.

Still, one may wonder. How can we make such analysis even more productive?

Systematic analysis of existing pirated software is a bit risky. After all, even downloading any of it can be considered a dubious endeavor. Luckily, there are many resources out there that we can leverage for our analysis w/o (hopefully) breaking any law. If you look at Github, you can find copies of old PirateBay databases [out there](https://github.com/darksun-misc/piratebay-db-dump) that can be downloaded and analyzed.

Let’s clone this old repo and see where it takes us…

Running:

```
rg -i "(keygen|crack|serial|warez|patch)" piratebay_db_dump_2015_10_27T04_10_50_to_2019_09_14T22_09_31.csv | cut -f3 -d;> test
```

gives us a ‘test’ file including many interesting file names – all hits on our basic 5-words search. When we look at the resulting file we can immediately see an opportunity that is … cracking/release group names. They are ‘all over the place’, and are clearly defined (often using [group], {group} constructs incorporated into file names), and as such – easily extractable.

Running:

```
rg -i -o "([[a-z0-9]+]|{[a-z0-9]+})" test > groups.txt
```

gives us a list of many such cracking/release groups that incorporate their names into their ‘release’ torrent file names. A quick histogram of these can be found [here](https://hexacorn.com/d/groups_histogram.txt).

There are obvious FPs on this list f.ex. [3840×2160], but most of the items seem to be good ‘search’ targets. In fact, looking for these group names incorporated into file names that we see in our ‘file creation’ telemetry may yield pretty good, accurate results.

Another observation we can make is that a lot of torrent file names seem to be incorporating our keyword list (keygen|crack|serial|warez|patch) in a very peculiar way. We see a lot of occurrences of these infixes:

* With Crack
* With Keygen
* With Serial
* With Patch
* With Working
* With Activation
* With License
* With Cheats
* + crack
* + patch
* + keygen
* + serial
* + key
* + cracked
* + serials
* + activator
* + loader
* + walkthrough
* + license
* + keymaker
* + fix
* + patcher
* + working
* + repack
* + keyegn (yes, a typo!)
* + preactivated
* + multikeygen
* + lisence (yes, another typo!)
* + mod
* + hotfix
* + activated
* [Full Installer]

These are really good keywords! It would seem that with such a simple exercise we have immediately extended our original keyword list to cover a lot more cases!

When you analyze data sets of interest it’s really important to focus on the end goal. Starting with some 5, FP-prone common ‘pirate’ words we ended up generating a much longer and accurate list of some very unique, pirating-specific, and actionable keywords…

Happy hunting!

This entry was posted in [Threat Hunting](https://www.hexacorn.com/blog/category/threat-hunting/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/03/01/hunting-for-the-warez-other-dodgy-stuff-people-install-download-part-1/ "Permalink to Hunting for the warez & other dodgy stuff people install / download, part 1").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")