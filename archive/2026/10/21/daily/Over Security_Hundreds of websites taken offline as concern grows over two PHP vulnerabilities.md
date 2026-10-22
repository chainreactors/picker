---
title: Hundreds of websites taken offline as concern grows over two PHP vulnerabilities
url: https://therecord.media/php-script-vulnerabilities-warnings
source: Over Security
date: 2026-10-21
fetch_date: 2026-10-22T06:46:25.573092
---

# Hundreds of websites taken offline as concern grows over two PHP vulnerabilities

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![PHP code](https://cms.therecord.media/uploads/large_pexels_pixabay_270557_b1a99bb16a.jpg)

PHP code. Image: Pixabay via Pexels

[Jonathan Greig](/author/jonathan-greig)October 21st, 2026

# Hundreds of websites taken offline as concern grows over two PHP vulnerabilities

*Editor's Note: Story updated 10:50 a.m. Eastern U.S. time with information about OpenAI's involvement.*

A set of vulnerabilities in one of the most popular scripting languages underpinning many websites set off alarm bells in the cybersecurity community on Tuesday evening, followed by a global scramble to apply patches on Wednesday.

The maintainers of PHP — used to build and run web applications and the vast majority of websites — [released](https://www.php.net/index.php#2026-10-20-1) an urgent notice warning of two new bugs. Hundreds of websites were down on Wednesday as administrators responded to the warning.

The vulnerabilities — CVE-2026-109618 and CVE-2026-109619 — carry severity scores of 9.2 out of 10 and are rated critical by PHP. The bugs can allow for remote code execution on unpatched websites.

“All PHP users are encouraged to prepare now so they can upgrade as soon as the release is available,” PHP’s security team said Tuesday evening. “PHP 8.1 and older no longer receive updates from the PHP project.”

PHP's maintainers started [releasing fixes](https://www.php.net/archive/2026.php#2026-10-21-5) after 10 a.m. Wednesday, Eastern U.S. time.

Dozens of government agencies had released urgent warnings throughout the evening and early on Wednesday morning telling website maintainers to stay alert and patch their systems immediately when the fixes were available.

Dane Knecht, the CTO of Cloudflare, [said](https://x.com/dok2001/status/2112811965735202970) the tech giant is already seeing attacks emerging, and it released stopgap mitigations to help protect some customers. At least [one video](https://media.infosec.exchange/infosec.exchange/cache/media_attachments/files/117/475/759/330/067/147/original/4e800fe72bfa6523.mp4) released on social media showed the vulnerabilities being used to cause damage.

Jake Knott, head of threat intelligence for watchTowr said the cybersecurity company is also observing in-the-wild exploitation of the vulnerabilities with a variety of proof-of-concept tools vibecoded with the help of AI.

“Whilst nobody has been successful to date, we don't expect that will last long,” he said.

## Websites down

The [European Union](https://cert.europa.eu/publications/security-advisories/2026-018/), [U.S.](https://x.com/NSACyber/status/2112903220209098897), [Germany](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-297981-1032.html), [Japan](https://x.com/mpd_cybersec/status/2112847929845416014), [Australia](https://x.com/asdgovau/status/2112754887113220213), [the U.K.](https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php) and [the Netherlands](https://www.ncsc.nl/index-en.html) all released warnings locally about the vulnerabilities. Several governments even [took some websites offline](https://x.com/cnil/status/2112853909077139835) in advance of the patch being released.

Large [companies](https://x.com/ohdearapp/status/2112877882200784956) and [organizations](https://x.com/chariteberlin/status/2112843864734351549) like [Nintendo](https://x.com/nintendo_cs/status/2112790118272802942) and [others](https://x.com/obsproject/status/2112782086956540044) also took services offline as they addressed the bugs, which are being called “PHP2Shell.”

Some estimates show that [more than 70%](http://wiz.io/blog/php2shell-php-rce) of all websites on the internet use PHP. Experts at watchTowr [noted](https://watchtowr.com/intelligence/php-cve-2026-109618-faq/?ref=metacurity.com) that enterprise networks commonly run PHP-based content management systems and internal tools, so servers running PHP often handle customer data and business logic reachable from the internet.

Sophos official Don Smith said the immediate challenge is not just installing a patch but finding and managing every instance where PHP is running.

“The use of PHP is pervasive, it can sit beneath public websites, content management systems, hosting platforms and third-party products, sometimes without even being obvious to the organization using it,” he said.

“Security teams should prioritise internet-facing systems, confirming which versions are affected as soon as the official advisory is published, and apply the updates without delay…any vulnerable system that cannot be patched should be isolated from the internet until it can be secured.”

## OpenAI and Calif

Shortly after the patches were released, OpenAI [came forward](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) to say researchers at a cybersecurity firm called [Calif](https://calif.io/) used its tools to discover the PHP bugs two months ago through its “Patch the Planet” program.

OpenAI said it worked with PHP and other companies to test the fixes, prepare guidance and “helped coordinate the response with infrastructure providers.”

The company defended its role in the situation, arguing that the “weaknesses already existed” and that AI helped the researchers find them. But they acknowledged that AI “can also help attackers exploit them” and said it is critical that organizations work together to deploy protections.

Experts [expressed deep concern](https://x.com/cyb3rops/status/2112663298088845676) that millions of PHP-backed websites are still running ancient versions of the language that [likely cannot be updated](https://cyberplace.social/%40GossiTheDog/117477828338038819).

Joviane Jardim, a senior security researcher at Swedish firm Detectify, said many organizations only learn about a forgotten PHP server when an attacker finds it.

“That’s the risk with this one: the flaws became public before the fix did, so both sides are starting at the same time. Attackers aren’t waiting for a working exploit. They’re building a list of every server on the internet that says it runs PHP, sorted by version, and the moment the fix is out, they will compare the old code with the new one to find the flaw,” he said.

With artificial intelligence, most attackers can create a working exploit in under an hour, meaning defenders can expect a wave of exploitation shortly after the patch is released.

Jardim added that roughly half of all PHP websites are running older versions of PHP but only PHP 8.2 and newer are getting patches.

“That’s the real exposure. Those sites haven’t been updated in years, which usually means nobody is watching them either,” he said.

“So the question this week is this: do you know where all your PHP is running? If yes, this is an afternoon of updates. If no, the risk is in the systems you’ve forgotten: an old marketing site, a hosting control panel, a device with PHP built in. And speed matters more than ever.”

* [Technology](/news/technology)
* [News](/ukraine-says-starshield-working-again-after-disruption)
* [Government](/news/government)
* [Industry](/)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm...