---
title: Rightsholders Can’t Use OpenAI and Anthropic to Dismantle Meta’s Seeding Defense
url: https://torrentfreak.com/rightsholders-cant-use-openai-and-anthropic-to-dismantle-metas-seeding-defense/
source: TorrentFreak
date: 2026-09-14
fetch_date: 2026-09-15T07:03:14.647952
---

# Rightsholders Can’t Use OpenAI and Anthropic to Dismantle Meta’s Seeding Defense

[![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/search.svg)

* News
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/torrentfreak/build/assets/img/x.svg)

# Rightsholders Can’t Use OpenAI and Anthropic to Dismantle Meta’s Seeding Defense

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [AI](https://torrentfreak.com/category/ai/ "Go to the AI category archives.") >

Meta previously argued that uploading pirated books to other BitTorrent users was an unavoidable side effect of downloading them, and therefore fair use. Rightsholders suing Meta in three related cases tried to dismantle this theory by asking OpenAI and Anthropic to reveal how they torrented shadow library data. A magistrate judge denied the request, but that's not the end of the torrenting dispute.

![AI logos](https://torrentfreak.com/images/ailogos-600x357.png)Over the past two years, rightsholders of all kinds have filed lawsuits against companies that develop AI models.

Meta is among a long list of companies now being sued for this allegedly infringing activity. This includes a [class action](https://torrentfreak.com/meta-admits-use-of-pirated-book-dataset-to-train-ai-240111/) lawsuit filed by authors including Richard Kadrey and Sarah Silverman, which accused Meta of training its Llama models on pirated books, and of sharing those books with other BitTorrent users in the process.

Last summer, Judge Vince Chhabria ruled that the AI training itself [was fair use](https://torrentfreak.com/meta-secures-bittersweet-fair-use-victory-in-ai-piracy-case-250626/), leaving the BitTorrent distribution claims as the last live part of the case. Earlier this year, Meta added a new line of defense to those claims. In a supplemental interrogatory response, the company argued that any uploading of pirated books during its torrent downloads was “part-and-parcel” of a fair use purpose.

Meta stated that BitTorrent was “a more efficient and reliable means of obtaining the datasets,” and in the case of Anna’s Archive the only way to get them in bulk. Since torrent users upload to each other by design, any sharing was simply “an inherent characteristic of the BitTorrent protocol.”

Both of Meta’s torrenting claims are now being tested in three [related lawsuits](https://www.courtlistener.com/docket/73294395/cognella-inc-v-meta-platforms-inc/), filed by Chicken Soup for the Soul, academic publisher Cognella, and John Carreyrou’s Cambronne Inc. These three cases are all assigned to Judge Chhabria and target the same shadow library torrenting activity.

*The coordinated cases*
![disco 3](https://torrentfreak.com/images/disco3.png)

## Ask Torrenting AI Rivals

Instead of waiting for Meta to document the technical details of its torrent client setup, the publishers went to the two AI rivals that could potentially disprove the seeding requirement.

In August, they subpoenaed OpenAI and Anthropic for the identity, versions and configurations of every torrent client the companies have used since 2019. This specifically includes any records of efforts to prevent seeding.

In similar lawsuits, both companies have admitted that they used books from shadow libraries. If they configured a torrent client not to upload, Meta’s “necessity” argument would be in trouble.

“If OpenAI torrented but configured its clients to suppress uploading, then the redistribution Meta calls an ‘inherent characteristic’ of the protocol was a setting Meta declined to change,” the publishers told the court.

*“Inherent characteristic”*
![inherent](https://torrentfreak.com/images/inherent.png)

That argument builds on an earlier finding in the legal battle, which revealed that a Meta engineer wrote a script to prevent seeding, but apparently not leeching.

## OpenAI and Anthropic Won’t Talk

Instead of insisting on all requested documents, the publishers also offered an alternative. If OpenAI or Anthropic would simply explain how they acquired the shadow-library data and whether they tried to prevent uploading, the torrent document demands would be dropped.

The AI companies didn’t take the offer, however, and they pushed back instead. Both companies informed the court that examining the technical features of the relevant torrent client directly would be better, adding that their own practices say nothing about Meta’s.

“Clients are not interchangeable, they differ in their default upload settings, in whether those defaults can be reconfigured, and in their capacity to suppress uploading during and after a download,” Anthropic’s lawyers wrote.

“What Anthropic’s client allowed shows nothing about what Meta’s did.”

*It says nothing*
![disco 3](https://torrentfreak.com/images/disco3.png)

OpenAI made the same point, noting that there is no evidence that it used the same torrent clients or “built ‘comparable corpora’ to Meta.”

## Judge Sides With AI Rivals

In a new order released last week, Magistrate Judge Thomas Hixson sided with the two AI companies. Without deciding on Meta’s seeding arguments, the court concluded that the torrent logs of AI rivals are not the best place to gather evidence.

“To the extent Meta’s fair use defense hinges on the assertion that its use of BitTorrent was the only way BitTorrent can be used, that assertion can be tested by examining the BitTorrent client itself,” Judge Hixson writes.

Asking OpenAI or Anthropic for their logs says little about Meta’s technical setup or the technical capabilities of torrent clients.

“Any user of a torrent client would be relevant in that sense. Why can’t Plaintiffs’ expert use the torrent clients to show how torrent clients can be used?” the order adds.

Similarly, the claim that shadow library data could only be downloaded in bulk through torrents, would be something the publishers can check with the libraries directly, instead of trying to get that information through other AI companies.

## Meta’s Own Server Data

In these three cases, the court decided that getting data from AI rivals is off limits. However, the same doesn’t apply to data from Meta’s own servers.

On September 11, Judge Hixson granted a motion in the related class action case filed by Kadrey and other authors. This order covers the command history files for every server Meta used to torrent, including its virtual machines and AWS instances.

Command histories are the logs a server keeps of every command an operator types. For a torrenting machine, that presumably includes how the torrent client was installed and any changes made to its upload settings.

The order goes back to early 2025, when Meta admitted that it had held back relevant documents until after the discovery deadline had passed. To make up for that, Judge Chhabria gave the authors extra discovery, including records showing how Meta’s torrent clients were set up and used.

Meta argued that the log files it had already handed over were enough. Judge Hixson disagreed, however, ordering Meta to hand over the command histories as well.

The authors hope these command histories will also reveal exactly which copyrighted works Meta torrented. Whether the data will show any of that has yet to be seen.

For now, whether Meta could have downloaded the books without seeding is a question for the plaintiffs’ experts, who will have Meta’s own server records to work with. T...