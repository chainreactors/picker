---
title: De-Google Project Update
url: https://www.tbray.org/ongoing/When/202x/2025/07/29/DeGoogling
source: ongoing by Tim Bray
date: 2025-07-30
fetch_date: 2025-10-06T23:27:25.285891
---

# De-Google Project Update

# De-Google Project Update

Search

I
[introduced this family project](/ongoing/When/202x/2024/03/09/DeGoogling) in the spring of 2024.
I won’t reproduce those arguments for why we’re working on this, but in the current climate I feel like I hardly need to.
Since that post, our aversion to Google dependency has only grown stronger. Progress has been non-zero but not fast.

Here’s the table, with progress notes below.

| Need | Supplier | Alternatives |
| --- | --- | --- |
| [Office](/ongoing/When/202x/2024/03/09/DeGoogling#p-3) | Google Workspace | Proton? |
| [Data sharing](/ongoing/When/202x/2024/03/09/DeGoogling#p-17) | Dropbox |  |
| [Photos](/ongoing/When/202x/2024/03/09/DeGoogling#p-17) | Google Photos | Dropbox? |
| [Video meetings](/ongoing/When/202x/2024/03/09/DeGoogling#p-16) | Google Meet | Jitsi, Signal? |
| [Maps](/ongoing/When/202x/2024/03/09/DeGoogling#p-10) | Google Maps | Magic Earth, Here, something OSM-based? |
| [Browser](/ongoing/When/202x/2024/03/09/DeGoogling#p-4) | Safari, Firefox, Vivaldi, LibreWolf |  |
| [Search](/ongoing/When/202x/2024/03/09/DeGoogling#p-12) | Google | Bing-based options, Kagi? |
| [Chat](/ongoing/When/202x/2024/03/09/DeGoogling#p-5) | Signal |  |
| [Photo editing](/ongoing/When/202x/2024/03/09/DeGoogling#p-6) | Adobe Lightroom & Nik | Capture One, Darktable, ? |
| [In-car interface](/ongoing/When/202x/2024/03/09/DeGoogling#p-7) | Google Android Auto | Automaker software |
| [Play my music](/ongoing/When/202x/2024/03/09/DeGoogling#p-8) | Plex, USB |  |
| [Discover music](/ongoing/When/202x/2024/03/09/DeGoogling#p-9) | Qobuz |  |
| [TV](/ongoing/When/202x/2024/03/09/DeGoogling#p-13) | Roku, Apple, migration |  |

Pink indicates a strong desire to get off the incumbent service, green means we’re happy-ish with what we’re using, and blue
means that, happy or not, it’s not near the top of the priority list.

I’ll reproduce the metrics we care about when looking to replace Google products, some combination of:

1. Not ad-supported
2. Not VC-funded
3. Not Google, Microsoft, or Amazon

The list used to include “Open Source” but I decided that while that’s good, it’s less important than the other three criteria.

Now let’s walk down the chart.

Office ·
This is going to be a wrenching transition; we’ve been running the family on Google stuff forever, and I anticipate
muscle-memory pain. But increasingly, using Google apps feels like being in enemy territory. And, as I said last time, I
will not be sorry to shake the dust of Google Drive and Docs from my heels, I find them clumsy and am
always having trouble finding something that I know is in there.

While I haven’t dug in seriously yet, I keep hearing reasonably-positive things about Proton, and nothing substantive to
scare me away. Wish us luck.

Data sharing (progress!) ·
Dropbox is, eh, OK. It doesn’t seem actively evil, there’s no advertising, and the price is low.

Photos ·
We’re a four-Android family including a couple of prolific photographers, and everything just gets pumped into Google and
then it fills up and then they want more money. If we could configure the phones to skip Google and go straight to Dropbox,
that would be a step forward.

Video meetings ·
Google meet isn’t painful but I totally suspect it of data-mining what should be private conversations. I’m getting the
feeling that the technical difficulty of videoconferencing is going steadily down, so I’m reasonably optimistic that
something a little less evil will come along with a fair price.

Maps ·
The fear and loathing that
[I started feeling in 2017](/ongoing/When/201x/2017/06/29/Fear-Google-Reviews) grows only stronger. But replacements
aren’t obvious.
It’s a pity, maps
and directions and reviews feel like a natural monopoly that should be a public utility or something, rather than a corporate moat.

Browser (progress!) ·
Chrome has seriously started making my flesh crawl; once again, enemy territory. Fortunately, there are lots of good options.
Even people like us who have multiple lives we need to keep separate can find enough better browsers out there.

Maybe I’ll have a look at one of the new genAI-company browsers ha ha just kidding.

Search ·
The reports on Kagi keep being positive and giving it a try is definitely on the To-Do list.

Chat ·
Signal is the only sane choice at this point in history for personal use.

Photo editing ·
Adobe’s products are good, and I’m proficient and happy with Lightroom, but they are definitely suffering from bad genAI
craziness. Also the price is becoming unreasonable.

I’ve had a few Lightroom software failures in recent months and if that
becomes a trend, looking seriously at the alternatives will move to the top of the priority list.

In-car interface ·
It’s tough, Android Auto is a truly great product. I think I’m stuck here for now, particularly given that I plan to be
driving a [2019-model-year car](/ongoing/What/The%20World/Jaguar%20Diary/) for the foreseeable future. Also, it
supports my music apps.

Discover music and play mine (progress!) ·
Progress here. I’ve almost completely stopped using YouTube Music in favor of Plex and Qobuz. Really no downside; YTM has
more or less completely lost the ability to suggest good new stuff.

TV ·
Video continues morphing itself into Cable TV redux. We have an old Roku box that works fine and I think I’ve managed to find
its don’t-spy-on-us settings. We’ll keep subscribing to Apple+ as long as they keep shipping great shows. I have zero regrets
about having
[left Prime behind](/ongoing/When/202x/2025/03/06/Canceled-Prime).

As for the rest, we’ve become migrants,
exclusively month-at-a-time subscriptions for the purpose of watching some serial or sports league, unsubscribe after the season
finale or championship game. The good news is that I
haven’t encountered much friction in unsubscribing, just a certain amount of earnest pleading.

Looking forward ·
I have yet to confront any of the really hard parts of this project, but the sense of urgency is increasing. Let’s see.

---

**Updated: 2025/07/31**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: Niall Kennedy (Jul 29 2025, at 13:23)

Proton Drive recently improved its photo backup viewer and published a roadmap. Could have some good crossover with your "Office" need.

<https://proton.me/drive/photo-storage>

<https://proton.me/blog/drive-roadmap-summer-2025>

*[[link](#c1753820582.887789)]*

From: [Scott Laird](https://scottstuff.net) (Jul 29 2025, at 13:26)

I've heard good things about <https://immich.app/> for photos, but haven't tried it myself yet. Open Source, self-hosted (or paid hosting), with optional AI search, which is pretty much the only useful way to do content search on images.

*[[link](#c1753820799.371765)]*

From: [Nelson](https://www.somebits.com/) (Jul 29 2025, at 13:59)

I came here also to recommend Immich as an alternative to Google Photos. it's very good, a solid full product that is quite usable. You can host it yourself or for a few bucks a month at a hoster like PikaPods.

The UI is mostly a direct clone of Google Photos, and that's a good thing IMHO. It still has a bit of a beta feel, there's dire warnings not to trust it with your only copy of your photos. And I think the path to getting photos into it from your phone camera won't be as low friction as Google Photos. But people are using it that way.

*[[link](#c1753822775.50777)]*

From: [RawBob](http://) (Jul 29 2025, at 14:01)

I self-host immich on a beelink mini-pc, with nightly cron backups to USB drives.

It's got lots of great features:

<https://github.com/immich-app/immich?tab=readme-ov-file#features>

Has a nice Android client, too.

*[[link](#c1753822895.746734)]*

From: [Nathan](http://) (Jul 29 2025, at 14:46)

The Brave browser, while based on open-source Chromium bits, is its own thing. It's actually pretty good, and also has its own search which can be used independently (search.brave.com...