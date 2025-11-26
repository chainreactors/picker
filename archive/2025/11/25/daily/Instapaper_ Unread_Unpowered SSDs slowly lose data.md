---
title: Unpowered SSDs slowly lose data
url: https://www.xda-developers.com/your-unpowered-ssd-is-slowly-losing-your-data/
source: Instapaper: Unread
date: 2025-11-25
fetch_date: 2025-11-26T03:17:03.423413
---

# Unpowered SSDs slowly lose data

Menu

[![XDA logo](https://static0.xdaimages.com/assets/images/xda-logo-full-colored-light.svg?v=3.1 "XDA")](/)

Sign in now

[ ]

Close

* + [News](/news/)
  + [PC Hardware](/category/pc-hardware/)
    [ ]
    Submenu
    - [CPU](/processor/)
    - [GPU](/gpu/)
    - [Storage](/storage/)
    - [Monitors](/monitors/)
    - [Keyboards & Mice](/input-devices/)
  + [ ]

    Software
    Submenu
    - [Productivity](/productivity/)
    - [Self-Hosting](https://www.xda-developers.com/self-hosting/)
    - [Home Lab](https://www.xda-developers.com/home-lab/)
    - [Other Software](/software-and-services/)
  + [ ]

    Operating Systems
    Submenu
    - [Windows](/windows/)
    - [Linux](/linux-hub/)
    - [macOS](/macos/)
  + [Devices](/devices/)
    [ ]
    Submenu
    - [Single-Board Computers](/single-board-computers/)
    - [Laptops](/laptops/)
    - [Gaming Handheld](/gaming-handhelds/)
    - [Prebuilt PC](/prebuilt-pc/)
  + [ ]

    Home
    Submenu
    - [Networking](/networking/)
    - [Smart Home](/smart-home/)
  + [Gaming](/gaming/)
    [ ]
    Submenu
    - [Game Reviews](https://www.xda-developers.com/gaming-reviews/)

* Sign in
* [Newsletter](/page/newsletter/)

[ ]

Menu
[![XDA logo](https://static0.xdaimages.com/assets/images/xda-logo-icon-colored-light.svg?v=3.1 "XDA")](/)

Follow

Followed

Like

[Threads

22](#threads "Threads")

More Action

Summary

Generate a summary of this story

Sign in now

[ ]

[ESP32](https://www.xda-developers.com/esp32/)

[Windows 11](https://www.xda-developers.com/windows-11/)

[NotebookLM](https://www.xda-developers.com/notebooklm/)

[Gaming](https://www.xda-developers.com/gaming/)

[Forums](https://xdaforums.com/)

[ ]

Close

# The unpowered SSDs in your drawer are slowly losing your data

![a samsung and crucial ssd next to each other on a table](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2025/01/crucial-and-samsung-ssd.jpg?&fit=crop&w=1600&h=900)

[![4](https://static0.xdaimages.com/wordpress%2Fwp-content%2Fauthors%2F6698b6624a3fe-PXL_20240717_153949958.jpg?fit=crop&w=90&h=90)](/author/tanveer-singh/)

By
[Tanveer Singh](/author/tanveer-singh/)

Published 2 days ago

After a 7-year corporate stint, Tanveer found his love for writing and tech too much to resist. An MBA in Marketing and the owner of a PC building business, he writes on PC hardware, technology, and Windows. When not scouring the web for ideas, he can be found building PCs, watching anime, or playing Smash Karts on his RTX 3080 (sigh).

Sign in to your XDA account

Summary

Generate a summary of this story

follow

Follow

followed

Followed

Like

Like

[Thread
22](#threads "Threads")

Log in

Here is a fact-based summary of the story contents:

Try something different:

Show me the facts

Explain it like I’m 5

Give me a lighthearted recap

SSDs have all but replaced hard drives when it comes to primary storage. They're orders of magnitude faster, more convenient, and consume less power than mechanical hard drives. That said, if you're also using SSDs for cold storage, expecting the drives lying in your drawer to work perfectly after years, you might want to rethink your strategy. Your reliable SSD could suffer from corrupted or lost data if left unpowered for extended periods. This is why many users [don't consider SSDs a reliable long-term storage medium](https://www.xda-developers.com/why-i-never-trust-ssd-for-long-term-storage/), and prefer using hard drives, magnetic tape, or M-Disc instead.

## Your SSD data isn't as permanent as you think

### Non-volatile with an asterisk

Unlike hard drives that magnetize spinning discs to store data, SSDs modify the electrical charge in NAND flash cells to represent 0 and 1. NAND flash retains data in underlying transistors even when power is removed, similar to other forms of non-volatile memory. However, the duration for which your SSD can retain data without power is the key here. Even the cheapest SSDs, say those with QLC NAND, can safely store data for about a year of being completely unpowered. More expensive TLC NAND can retain data for up to 3 years, while MLC and SLC NAND are good for 5 years and 10 years of unpowered storage, respectively.

The problem is that most consumer SSDs use only TLC or QLC NAND, so users who leave their SSDs unpowered for over a year are risking the integrity of their data. The reliability of QLC NAND has improved over the years, so you should probably consider 2–3 years of unpowered usage as the guardrails. [Without power, the voltage stored in the NAND cells can be lost](https://www.xda-developers.com/will-ssd-lose-data-without-power/), either resulting in missing data or completely useless drives.

This data retention deficiency of consumer SSDs makes them an unreliable medium for long-term data storage, especially for creative professionals and researchers. HDDs can suffer from bit rot, too, due to wear and tear, but they're still more resistant to power loss. If you haven't checked your archives in a while, I'd recommend doing so at the earliest.

![A graphic showing a hand holding an SSD.](https://static0.xdaimages.com/wordpress/wp-content/uploads/2024/10/ssd-wear.jpg?q=49&fit=crop&w=220&h=182&dpr=2)
Related

##### [5 SSD myths that are simply untrue](/ssd-myths-that-are-simply-untrue/ "5 SSD myths that are simply untrue")

Don't fall for these common SSD misunderstandings.

Posts
[12](/ssd-myths-that-are-simply-untrue/#threads "Total Posts")

By
[Jacob Roach](/author/jacob-roach/ "Posts by Jacob Roach")

Mar 8, 2025

## But, most people don't need to worry about it

### Archival storage isn't that common

The scenario I described above isn't relevant to people outside enterprise, enthusiast, and solopreneur usage. The need to store tons of data for years on drives that aren't plugged in isn't a concern for most people, who use one or two SSDs on their PC that might be left without power for only a few months, at the maximum. You've probably lost data on your SSD due to a rare power surge or a [faulty drive](https://www.xda-developers.com/do-this-if-ssd-dying/) rather than voltage loss. Some factors, like temperature and the quality of the underlying NAND flash, can accelerate this voltage loss.

SSDs aren't eternal, even if you keep them powered on forever. The [limited write cycles of NAND flash](https://www.xda-developers.com/ways-check-how-much-life-your-ssd-has-left/) will eventually bring an SSD to the end of its lifecycle, but the majority of users will probably replace the drive before that ever happens. So, you don't need to worry about writing too much data to your SSD or leaving your PC turned off for days, weeks, or even months. Just don't trust an unpowered SSD that's gathering dust in the house for years, which brings me to my next point.

![The Aiffro NAS with four SSDs slotted in](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2024/07/aiffro-nas-four-ssds.jpg?q=49&fit=crop&w=220&h=182&dpr=2)
Related

##### [3 ways to extend your SSD's lifespan](/ways-to-extend-your-ssds-lifespan/ "3 ways to extend your SSD's lifespan")

Don't waste your new SSD with needless writes.

Posts
[6](/ways-to-extend-your-ssds-lifespan/#threads "Total Posts")

By
[Samuel Contreras](/author/samuel-contreras/ "Posts by Samuel Contreras")

Jul 29, 2024

## You should always have a backup anyway

### Prevention is better than cure

[Backing up your data](https://www.xda-developers.com/how-back-up-windows-11-pc/) is the simplest strategy to counteract the limitations of storage media. Having multiple copies of your data on different [types of storage](https://www.xda-developers.com/storage-types-officially-too-old/) ensures that any unexpected incidents protect your data from vanishing forever. This is exactly what the [3-2-1 backup rule](https://www.xda-developers.com/how-to-quickly-set-up-the-3-2-1-backup-rule/) talks about: 3 copies of data on at least 2 different storage media, with 1 copy stored off-site. For most people, this co...