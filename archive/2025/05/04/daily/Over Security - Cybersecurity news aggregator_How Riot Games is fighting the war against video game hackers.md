---
title: How Riot Games is fighting the war against video game hackers
url: https://techcrunch.com/2025/05/03/how-riot-games-is-fighting-the-war-against-video-game-hackers/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-04
fetch_date: 2025-10-06T22:27:54.224654
---

# How Riot Games is fighting the war against video game hackers

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-lockup.svg) TechCrunch Desktop Logo](https://techcrunch.com)

[![](https://techcrunch.com/wp-content/uploads/2024/09/tc-logo-mobile.svg) TechCrunch Mobile Logo](https://techcrunch.com)

* [Latest](/latest/)
* [Startups](/category/startups/)
* [Venture](/category/venture/)
* [Apple](/tag/apple/)
* [Security](/category/security/)
* [AI](/category/artificial-intelligence/)
* [Apps](/category/apps/)
* [Disrupt 2025](https://techcrunch.com/events/tc-disrupt-2025/)

* [Events](/events/)
* [Podcasts](/podcasts/)
* [Newsletters](/newsletters/)

Search

Submit

Site Search Toggle

Mega Menu Toggle

### Topics

[Latest](/latest/)

[AI](/category/artificial-intelligence/)

[Amazon](/tag/amazon/)

[Apps](/category/apps/)

[Biotech & Health](/category/biotech-health/)

[Climate](/category/climate/)

[Cloud Computing](/tag/cloud-computing/)

[Commerce](/category/commerce/)

[Crypto](/category/cryptocurrency/)

[Enterprise](/category/enterprise/)

[EVs](/tag/evs/)

[Fintech](/category/fintech/)

[Fundraising](/category/fundraising/)

[Gadgets](/category/gadgets/)

[Gaming](/category/gaming/)

[Google](/tag/google/)

[Government & Policy](/category/government-policy/)

[Hardware](/category/hardware/)

[Instagram](/tag/instagram/)

[Layoffs](/tag/layoffs/)

[Media & Entertainment](/category/media-entertainment/)

[Meta](/tag/meta/)

[Microsoft](/tag/microsoft/)

[Privacy](/category/privacy/)

[Robotics](/category/robotics/)

[Security](/category/security/)

[Social](/category/social/)

[Space](/category/space/)

[Startups](/category/startups/)

[TikTok](/tag/tiktok/)

[Transportation](/category/transportation/)

[Venture](/category/venture/)

### More from TechCrunch

[Staff](/about-techcrunch/)

[Events](/events/)

[Startup Battlefield](/startup-battlefield/)

[StrictlyVC](https://strictlyvc.com/)

[Newsletters](/newsletters/)

[Podcasts](/podcasts/)

[Videos](/video/)

[Partner Content](/sponsored/)

[TechCrunch Brand Studio](/brand-studio/)

[Crunchboard](https://www.crunchboard.com/)

[Contact Us](/contact-us/)

![A screenshot from a game of Valorant, Riot Games' competitive online first-person shooter.](https://techcrunch.com/wp-content/uploads/2025/05/valorant-gameplay.png?w=1024)

**Image Credits:**Riot Games/YouTube

[Security](https://techcrunch.com/category/security/)

# How Riot Games is fighting the war against video game hackers

[Lorenzo Franceschi-Bicchierai](https://techcrunch.com/author/lorenzo-franceschi-bicchierai/)

5:00 AM PDT · May 3, 2025

For as long as there have been video games, there have been people willing to find ways to cheat. Hobbyists have long dedicated themselves to finding vulnerabilities in games, often with the goal of developing cheats that they could share or sell. But ever since online competitive gaming became a legitimate profession, that hobby-hacking has morphed into an entire industry that aims to sell an unfair advantage to those willing to pay.

Developing and selling video game cheats [can be a lucrative business](https://www.vice.com/en/article/inside-the-worlds-largest-video-game-cheating-empire/), and video game developers have in recent years had to beef up their anti-cheat teams, whose mission is to ban cheaters, neutralize the software they use, as well as go after cheat developers. [More companies](https://levvvel.com/games-with-kernel-level-anti-cheat-software/) are taking the [somewhat](https://www.wired.com/story/kernel-anti-cheat-online-gaming-vulnerabilities/) [controversial](https://arstechnica.com/gaming/2022/09/eas-new-anti-cheat-tools-dip-into-the-dreaded-kernel-mode/) step of deploying anti-cheat systems that run at the [kernel level](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#kernel), meaning they have the highest privileges in the operating system and can potentially monitor everything that happens on the machine the game is run on.

One of the most prominent kernel-level anti-cheat systems is [Vanguard](https://support-valorant.riotgames.com/hc/en-us/articles/360046160933-What-is-Vanguard), developed by Riot Games, which makes [popular](https://tracker.gg/valorant/population) [titles](http://activeplayer.io/league-of-legends/) such as multiplayer online battle arena game *League of Legends and* online first-person shooter *Valorant*.

Essentially, Vanguard “forces cheats to be visible,” said Phillip Koskinas, the director and head of anti-cheat at Riot who [describes](https://www.leagueoflegends.com/en-au/news/dev/dev-vanguard-x-lol/#:~:text=an%20anti%2Dcheat%20artisan) [himself](https://www.linkedin.com/in/mirageofpenguins/) as “an anti-cheat artisan” who was “put on this earth for the one singular purpose of banning cheaters from online video games.”.

Thanks to Vanguard and the anti-cheat team led by Koskinas,  Riot bans thousands of cheaters on *Valorant* every day, according to a chart shared with TechCrunch.

![a graph showing the number of cheaters banned by day and the type of bans,](https://techcrunch.com/wp-content/uploads/2025/05/Vanguard-Bans-Per-Day-April-2025.png)

A chart showing the number of cheaters banned per day, and the type of bans, on riot games’ first-person shooter valorant.

Riot’s efforts seem to be working. As of early 2025, the percentage of *Valorant* “ranked” games — meaning competitive matches — that have cheaters is now less than 1% globally, [the company says](https://playvalorant.com/en-us/news/dev/vanguard-hits-new-bans-per-second-record/).

In an interview with TechCrunch, Koskinas detailed the various strategies that the anti-cheat team at Riot uses to fight cheaters and cheat developers: leveraging the security features in the Windows operating system, fingerprinting cheaters’ hardware to stop them from reoffending, infiltrating cheat communities, and playing psychological games in an effort to discredit cheaters.

## **‘We can just make them look like fools’**

Much of Koskinas and his team’s efforts stem from Vanguard having the deepest level of access to a gamer’s computer. To weed out cheaters, Vanguard takes advantage of some of the security features already built into Windows.

First, Koskinas explained, the anti-cheat software “almost universally” enforces some of Windows’ most important security features, such as [Trusted Platform Module](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview), a hardware-based security component, and [Secure Boot](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-secure-boot). These two technologies check if a computer has been modified or tampered with, such as by malware or a cheat, and prevents it from booting if so. Then, Vanguard checks that all of the computer’s hardware drivers, which allow the operating system to communicate with the hardware, are up to date to identify additional hardware that can enable cheating. Finally, Vanguard prevents cheats from loading and executing code in the kernel’s memory.

“Basically, all the security features that Microsoft and hardware manufacturers have leveraged to protect the operating system, we use or enforce,” Koskinas told TechCrunch. “We have to have a playground where we can play. We have to enforce a certain level of security.”

But fighting cheaters is not just about technology; it’s also about understanding the cheaters themselves and how they operate.

Koskinas’s team has a “reconnaissance arm,” he said, whose primary responsibility is to obtain and catalog threats, which sometimes involves acquiring cheats. The team obtains cheats in part by using sock puppet identities that have infiltrated cheater and cheat developer communities for years, akin to undercover operations.

“We’ve even gone as far as giving anti-cheat information to establish credibility. We’ll masquerade as though it was something we [reverse engineered], and explain how an anti-cheat technique works to demonstrate...