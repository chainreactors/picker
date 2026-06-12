---
title: What’s Really Slowing Your Extractions (Hint Not Your Tools)
url: https://www.forensicfocus.com/news/whats-really-slowing-your-extractions-hint-not-your-tools/
source: Instapaper: Unread
date: 2026-06-11
fetch_date: 2026-06-12T06:28:08.738966
---

# What’s Really Slowing Your Extractions (Hint Not Your Tools)

[Skip to content](#content "Skip to content")

* [Login/Register](https://www.forensicfocus.com/sign-in/?redirect_to=https%3A%2F%2Fwww.forensicfocus.com%2Fnews%2Fwhats-really-slowing-your-extractions-hint-not-your-tools%2F)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/themes/generatepress_child/assets/images/logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

[Login](/sign-in/)
[Register](/sign-up/)

[![Forensic Focus](https://www.forensicfocus.com/stable/wp-content/uploads/2020/05/forensic-focus_logo.png)](https://www.forensicfocus.com/ "Forensic Focus")

Menu

* [News](https://www.forensicfocus.com/news/)
* Community
  + [Forums](https://www.forensicfocus.com/forums/)
  + [Discord (Invite)](https://discord.gg/97zKvTXHeS)
* Resources
  + [Newsletter](https://www.forensicfocus.com/newsletter/)
  + [Articles](https://www.forensicfocus.com/articles/)
  + [Reviews](https://www.forensicfocus.com/reviews/)
  + [Webinars](https://www.forensicfocus.com/webinars/)
  + [Podcast](https://www.forensicfocus.com/podcast/)
  + [Interviews](https://www.forensicfocus.com/interviews/)
  + [Videos](https://www.forensicfocus.com/videos/)
  + [Case Studies](https://www.forensicfocus.com/case-studies/)
  + [Well-Being](https://www.forensicfocus.com/well-being/)
  + [Guides](https://www.forensicfocus.com/guides/)
  + [Useful Links](https://www.forensicfocus.com/useful-links/)
  + [Digital Forensics Timeline](https://www.forensicfocus.com/digital-forensics-timeline/)
* Jobs & Careers
  + [View jobs](https://www.forensicfocus.com/jobs/)
  + [How To Start A Career In Digital Forensics](https://www.forensicfocus.com/articles/how-to-start-a-career-in-digital-forensics/)
* Education
  + [Course Listings](https://www.forensicfocus.com/education/)
  + [Education & Training Guide](https://www.forensicfocus.com/articles/digital-forensics-education-certification-and-training-guide/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](https://www.forensicfocus.com/event-info/)

Menu

* [News](https://www.forensicfocus.com/news/)
* Community
  + [Forums](https://www.forensicfocus.com/forums/)
  + [Discord (Invite)](https://discord.gg/97zKvTXHeS)
* Resources
  + [Newsletter](https://www.forensicfocus.com/newsletter/)
  + [Articles](https://www.forensicfocus.com/articles/)
  + [Reviews](https://www.forensicfocus.com/reviews/)
  + [Webinars](https://www.forensicfocus.com/webinars/)
  + [Podcast](https://www.forensicfocus.com/podcast/)
  + [Interviews](https://www.forensicfocus.com/interviews/)
  + [Videos](https://www.forensicfocus.com/videos/)
  + [Case Studies](https://www.forensicfocus.com/case-studies/)
  + [Well-Being](https://www.forensicfocus.com/well-being/)
  + [Guides](https://www.forensicfocus.com/guides/)
  + [Useful Links](https://www.forensicfocus.com/useful-links/)
  + [Digital Forensics Timeline](https://www.forensicfocus.com/digital-forensics-timeline/)
* Jobs & Careers
  + [View jobs](https://www.forensicfocus.com/jobs/)
  + [How To Start A Career In Digital Forensics](https://www.forensicfocus.com/articles/how-to-start-a-career-in-digital-forensics/)
* Education
  + [Course Listings](https://www.forensicfocus.com/education/)
  + [Education & Training Guide](https://www.forensicfocus.com/articles/digital-forensics-education-certification-and-training-guide/)
* Events
  + [Event Calendar](/events/)
  + [Event Info & Recaps](https://www.forensicfocus.com/event-info/)

[Home](https://www.forensicfocus.com/) » [News](https://www.forensicfocus.com/news/) » What’s Really Slowing Your Extractions? (Hint: Not Your Tools)

# What’s Really Slowing Your Extractions? (Hint: Not Your Tools)

11th June 2026 by [MSAB](https://www.forensicfocus.com/author/msab/ "View all posts by MSAB")

![](https://www.forensicfocus.com/stable/wp-content/uploads/2026/06/Copy-of-blogposts-1.png)

In digital forensics, we invest in high-end tools… then connect everything with whatever cable is closest.

Bad idea.

In testing, **the difference between cables on the same device was the difference between finishing in minutes … or losing hours**. It’s about what’s actually inside the cable. If your extractions feel slow, inconsistent, or painfully long … this might be why.

In a digital forensics lab, we agonise over CPU choice, write blocker brands, and software licences that cost more than a small car (or house in some cases). Then we plug all of it into a £3 cable from a drawer and wonder why the extraction is taking long enough to finish a novel.

The cable matters more than it has any right to. Not because of the headline bandwidth printed on the sleeve, but because of the engineering inside, most of which is doing a worse job than you think.

## The Numbers

A 128GB modern Android handset. Identical workstation and software. Four cables.

Worst to best, that’s **over 70 minutes saved on physical and potentially more than two hours on full file system**. Across an evidence queue, that’s not a coffee break or lunch. That’s half a day wasted on a single device!

## Get The Latest DFIR News

### Join the Forensic Focus newsletter for the best DFIR articles in your inbox every month.

Unsubscribe any time. We respect your privacy - read our [privacy policy](/privacy-policy).

Leave this field empty if you're human:

If you’re wondering why FFS hurts more than physical despite extracting less data, it’s because FFS isn’t one long sequential read. It’s hundreds of thousands of small file operations, each carrying its own protocol overhead and, on a marginal cable, its own opportunity for a silent retry. Bad cables don’t average out across a long stream; they get multiplied across every file boundary, every database, every cached thumbnail, every chat attachment.

## Bandwidth Isn’t the Answer

The obvious reading is that the faster cables were using their higher rated bandwidth. If only. Most current smartphones cap at USB 3.2 Gen 1 (5 Gbps) or USB 3.2 Gen 2 (10 Gbps), and none negotiate Thunderbolt or USB4 v2.0. Your phone has no idea what PAM-3 ternary signalling is, and frankly, it doesn’t care.

The top two cables in this test were running at the same negotiated link speed. Their gap happened *within* a single 5 Gbps link. The bandwidth headroom on the sleeve was, in both cases, decorative.

**Read the full blog by Technical Sales Engineer Alex Coley here:**[**Your Cable Is Stealing Your Lunch Break (and Possibly the Rest of Your Day) – MSAB**](https://www.msab.com/blog/your-cable-is-stealing-your-lunch-break-and-possibly-the-rest-of-your-day/)

Categories [News](https://www.forensicfocus.com/news/) Tags [extraction](https://www.forensicfocus.com/tag/extraction/), [msab](https://www.forensicfocus.com/tag/msab/)

[Present At Magnet User Summit & Magnet Virtual Summit 2027!](https://www.forensicfocus.com/news/present-at-magnet-user-summit-magnet-virtual-summit-2027/)

[Amped Podcast Episode 1 – CCTV Nightmares: Chain Of Custody Secrets From Scene To Courtroom](https://www.forensicfocus.com/videos/amped-podcast-episode-1-cctv-nightmares-chain-of-custody-secrets-from-scene-to-courtroom/)

### Leave a Comment [Cancel reply](/news/whats-really-slowing-your-extractions-hint-not-your-tools/#respond)

You must be [logged in](https://www.forensicfocus.com/sign-in/?redirect_to=https%3A%2F%2Fwww.forensicfocus.com%2Fnews%2Fwhats-really-slowing-your-extractions-hint-not-your-tools%2F) to post a comment.

### Latest Articles

[![Amped Podcast Episode 1 – CCTV Nightmares: Chain Of Custody Secrets From Scene To Courtroom](https://www.forensicfocus.com/stable/wp-content/uploads/2026/06/ep1-final-870x570.png)](https://www.forensicfocus.com/videos/amped-podcast-episode-1-cctv-nightmares-chain-of-custody-secrets-from-scene-to-courtroom/)

[Videos](https://www.forensicfocus.com/videos/)

### [Amped Podcast Episode 1 – CCTV Nightmares: Chain Of Custody Secrets From Scene To Courtroom](https://www.forensicfocus.com/videos/amped-podcast-episode-1-cctv-nightmares-chain-of-custody-s...