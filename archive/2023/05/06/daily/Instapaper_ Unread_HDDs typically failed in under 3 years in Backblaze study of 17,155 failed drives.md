---
title: HDDs typically failed in under 3 years in Backblaze study of 17,155 failed drives
url: https://arstechnica.com/gadgets/2023/05/hdds-typically-fail-in-under-3-years-backblaze-study-of-17155-drives-finds/
source: Instapaper: Unread
date: 2023-05-06
fetch_date: 2025-10-04T11:43:01.304478
---

# HDDs typically failed in under 3 years in Backblaze study of 17,155 failed drives

[Skip to content](#main)
[Ars Technica home](https://arstechnica.com/)

Sections

[Forum](/civis/)[Subscribe](/subscribe/)[Search](/search/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

* [Feature](/features/)
* [Reviews](/reviews/)

* [AI](https://arstechnica.com/ai/)
* [Biz & IT](https://arstechnica.com/information-technology/)
* [Cars](https://arstechnica.com/cars/)
* [Culture](https://arstechnica.com/culture/)
* [Gaming](https://arstechnica.com/gaming/)
* [Health](https://arstechnica.com/health/)
* [Policy](https://arstechnica.com/tech-policy/)
* [Science](https://arstechnica.com/science/)
* [Security](https://arstechnica.com/security/)
* [Space](https://arstechnica.com/space/)
* [Tech](https://arstechnica.com/gadgets/)

[Forum](/civis/)[Subscribe](/subscribe/)

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Pin to story

Theme

* HyperLight
* Day & Night
* Dark
* System

Search dialog...

Sign In

Sign in dialog...

Sign in

Hard drive reliability

# HDDs typically failed in under 3 years in Backblaze study of 17,155 failed drives

Seagate still stands out.

[Scharon Harding](https://arstechnica.com/author/scharonharding/)
–

May 4, 2023 9:00 am
| [250](https://arstechnica.com/gadgets/2023/05/hdds-typically-fail-in-under-3-years-backblaze-study-of-17155-drives-finds/#comments "250 comments")

[![A technician repairing a hard disk drive with a tester](https://cdn.arstechnica.net/wp-content/uploads/2023/05/GettyImages-1205651800.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2023/05/GettyImages-1205651800.jpg)

Credit:
[Getty](https://www.gettyimages.com/detail/photo/technician-repairing-an-hard-disk-with-a-tester-royalty-free-image/1205651800)

Credit:
[Getty](https://www.gettyimages.com/detail/photo/technician-repairing-an-hard-disk-with-a-tester-royalty-free-image/1205651800)

Text
settings

Story text

Size

Small
Standard
Large
Width
\*

Standard
Wide
Links

Standard
Orange

\* Subscribers only
  [Learn more](/store/product/subscriptions/)

Minimize to nav

We recently covered a study by Secure Data Recovery, an HDD, SSD, and RAID data recovery company, of [2,007 defective hard disk drives](https://arstechnica.com/gadgets/2023/03/hdds-arent-as-durable-as-they-used-to-be-study-of-2007-damaged-drives-suggests/) it received. It found the average time before failure among those drives to be 2 years and 10 months. That seemed like a short life span, but considering the limited sample size and analysis in Secure Data Recovery's report, there was room for skepticism. Today, Backblaze, a backup and cloud storage company with a reputation for detailed HDD and SSD failure analysis, followed up Secure Data Recovery's report with its [own research](https://www.backblaze.com/blog/backblaze-drive-stats-for-q1-2023/) using a much larger data set. Among the 17,155 failed HDDs Backblaze examined, the average age at which the drives failed was 2 years and 6 months.

## 2 years, 6 months

Backblaze arrived at this age by examining all of its failed drives and their respective power-on hours. The company recorded each drive's failure date, model, serial number, capacity, failure, and SMART raw value. The 17,155 drives examined include 72 different models and does not include failed boot drives, drives that had no SMART raw attribute data, or drives with out-of-bounds data.

If Backblaze only looked at drives that it didn't use in its data centers anymore, there would be 3,379 drives across 35 models, and the average age of failure would be a bit longer at 2 years and 7 months.

Backblaze said its results thus far "are consistent" with Secure Data Recovery's March findings. This is despite Backblaze currently using HDDs that are older than 2 years and 7 months.

"When we first saw the Secure Data Recovery average failed age, we thought that 2 years and 10 months was too low. We were surprised by what our data told us, but a little math never hurt anyone," Backblaze's blog says.

"Given we are always adding additional failed drives to our dataset, and retiring drive models along the way, we will continue to track the average failed age of our drive models and report back if we find anything interesting."

When looking at the average age of drive failure by model, Backblaze reduced the model count to 30, eliminating drives with fewer than 50 failures.

[![Average Age of Drive Failure by Model table](https://cdn.arstechnica.net/wp-content/uploads/2023/05/1.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2023/05/1.jpg)

Credit:
Backblaze

Credit:
Backblaze

One standout in the table above is the 12TB Seagate ST12000NM0007, which saw 2,023 failures, occuring when each drive was, on average, 1 year and 6 months old. The only model with more failures was the 4TB Seagate ST400DM000. Backblaze saw 5,249 failures, and the drives were each an average of 3 years and 3 months old upon failure.

When breaking things down by drive capacity, at first glance, it seems lower-capacity drives may last longer before failing. However, Backblaze's blog points out that Backblaze doesn't have any 1TB, 1.5TB, 2TB, 3TB, or 5TB HDDs in operation in its sample group, making the data set for the smaller capacity drives complete. In contrast, most of the larger-capacity HDDs are still being used.

"In other words, as these larger drives continue to fail over the coming months and years, they could increase or decrease the average failure age of that drive model," Klein explained.

![Average Age of Drive Failure by Drive Size ](https://cdn.arstechnica.net/wp-content/uploads/2023/05/2-1.jpg)

Credit:
Backblaze

## Failure rates since April 2013

As usual, Backblaze provided a quarterly update of the HDDs in its active arsenal. Today, it added data from Q1 2023.

The following table shows annualized failure rates (AFRs) for 236,893 HDDs across 30 models and through nearly 10 years. The chart doesn't include drives "only used for testing purposes" or of which Backblaze had fewer than 60 units.

[![Backblaze Hard Drives Lifetime Annualized Failure Rate (4/20/2023-1/31/2023 for drive models active as of 3/31/2023)](https://cdn.arstechnica.net/wp-content/uploads/2023/05/3-1.jpg)](https://cdn.arstechnica.net/wp-content/uploads/2023/05/3-1.jpg)

Credit:
Backblaze

Credit:
Backblaze

Overall, the average AFR was 1.4 percent. The drive with the lowest AFR (0.28 percent) and at least 2.2 million drive days is Western Digital Corporation (WDC)'s 16TB WUH721816ALE6L4 (Backblaze has 14,098 units).

The model with the highest AFR (2.57 percent) and at least 2.2 million drive days is Seagate's 4TB ST4000DM000 (Backblaze had 18,070 units). It's worth noting, though, that the model has the largest number of drive days out of any model on Backblaze's table. In February, Backblaze [said](https://arstechnica.com/gadgets/2023/02/new-data-illustrates-times-effect-on-hard-drive-failure-rates/) Seagate HDDs generally show higher failure rates in Backblaze's environment and are also "less expensive," so "their failure rates are typically not high enough to make them less cost-effective over their lifetime. You could make a good case that for us, many Seagate drive models are just as cost-effective as more expensive drives."

Backblaze's full data set is on its [Hard Drive Test Data](https://www.backblaze.com/b2/hard-drive-test-data.html) page.

Listing image:
[Getty](https://www.gettyimages.com/detail/photo/technician-repairing-an-hard-disk-with-a-tester...