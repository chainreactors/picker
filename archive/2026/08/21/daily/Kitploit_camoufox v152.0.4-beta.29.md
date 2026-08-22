---
title: camoufox v152.0.4-beta.29
url: https://kitploit.com/en/posts/github-daijro-camoufox-v15204-beta29
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:50:59.468813
---

# camoufox v152.0.4-beta.29

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/41473/1ea2da371c4a9bc2e1ff5e6f2b1761cd44ca6ad0b503dc1e6e20606a48cd7454.png)

New releaseAug 21, 2026

# camoufox v152.0.4-beta.29

Open-source anti-detect Firefox fork for undetectable web scraping and AI agent automation. Injects realistic browser fingerprints, spoofs geolocation/WebRTC, and evades anti-bot systems at scale.

Share

![](https://camoufox.com/static/banner.svg)

# Camoufox

#### Camoufox is an open source anti-detect browser built for webscraping & AI agents. 🦊

[![daijro%2Fcamoufox | Trendshift](https://trendshift.io/api/badge/repositories/12224)](https://trendshift.io/repositories/12224)
[![Total Downloads](https://static.pepy.tech/personalized-badge/camoufox?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/camoufox)[![Monthly Downloads](https://static.pepy.tech/personalized-badge/camoufox?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads/month)](https://pepy.tech/projects/camoufox)
[![Weekly Downloads](https://static.pepy.tech/personalized-badge/camoufox?period=weekly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads/week)](https://pepy.tech/projects/camoufox)

#### ⚠️ This project is under development. It may not be suitable for stable production use. ⚠️

---

> [!NOTE]
> **All of the latest documentation is available at [camoufox.com](https://camoufox.com).**

> [!NOTE]
> Browser development is active at [github.com/CloverLabsAI/camoufox](https://github.com/CloverLabsAI/camoufox) and [github.com/VulpineOS/VulpineOS](https://github.com/VulpineOS/VulpineOS).
> This repo is being used to merge checkpoint releases and should be treated as the master copy.

---

# Sponsors

View/Collapse All

|  |  |
| --- | --- |
| [![Scrapfly.io](https://assets.kitploit.com/production/public/readmes/41473/45b2820aff381a9fb2cb01df09bfd2dbc7def136463454eacc4126e527bf23fe.png)](https://scrapfly.io/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox) | [Scrapfly](https://scrapfly.io/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox) is an enterprise-grade solution providing Web Scraping API that aims to simplify the scraping process by managing everything: real browser rendering, rotating proxies, and fingerprints (TLS, HTTP, browser) to bypass all major anti-bots. Scrapfly also unlocks the observability by providing an analytical dashboard and measuring the success rate/block rate in detail. |
| [![cloverlabs.ai](https://assets.kitploit.com/production/public/readmes/41473/07965d63c1bc08c25f1f074c192d0a2b49313c3a8d054816db1bbbc4e861a6e8.jpg)](https://cloverlabs.ai/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox) | [Clover Labs](https://cloverlabs.ai/?utm_source=github&utm_medium=sponsoring&utm_campaign=camoufox) is a Toronto based venture studio building AI agents for growth and distribution. |
| [![color horizontal](https://assets.kitploit.com/production/public/readmes/41473/a8af8b266340afc54d5300cf53ce73c5fb337bb47d659bc365a568b5ea9152ff.png)](https://serpapi.com/use-cases/web-search-api?utm_source=camoufox) | [SerpApi, a web search API](https://serpapi.com/use-cases/web-search-api?utm_source=camoufox) to scrape Google and other search engines with a simple API. |
| [![color horizontal](https://assets.kitploit.com/production/public/readmes/41473/b354514d262068a0c64895d64c0b39ca6621dd9d2773f69b29068f7ba5f3f878.jpg)](https://talordata.com/?campaignid=X01VSF4OOvlHfN6U&utm_source=github&utm_term=camoufox) | [Talordata](https://talordata.com/?campaignid=X01VSF4OOvlHfN6U&utm_source=github&utm_term=camoufox) is a simple web search API to scrape Google and other search engines at a fraction of the cost. Get 1,000 free requests upon registration, and pay just $0.25 per 1,000 successful responses—zero charges for failed scrapes.  Use coupon code **CAMOUFOX** for **10% OFF** Residential Proxies. [[Discord](https://discord.gg/dMZFyY39Fx)] |
| [![color horizontal](https://assets.kitploit.com/production/public/readmes/41473/020e7132e9b09a934bf14724693e4dc08c2ff874036a9834ae24375d350f6116.png)](https://crawlbase.com/?utm_source=github&utm_medium=sponsorship&utm_campaign=camoufox) | **Web data that survives the anti-bots.**  [Crawlbase](https://crawlbase.com/?utm_source=github&utm_medium=sponsorship&utm_campaign=camoufox) gives developers and AI teams reliable data at scale: a 99% success-rate Crawler, Crawling API, Smart AI Proxies, and Web MCP Server that get through, so your scrapers and agents don't break. You build, we handle the infrastructure. **Get 15% off your first 3 months with code CAMOUFOX** → [crawlbase.com](https://crawlbase.com/?utm_source=github&utm_medium=sponsorship&utm_campaign=camoufox) |
| [![scrappey](https://assets.kitploit.com/production/public/readmes/41473/8c99b2aa71f5ecc64080cfeb3148c82ab2bb8e48cb39fbedaf17f88bc9f81d28.png)](https://scrappey.com/?utm_source=camoufox&utm_medium=sponsorship&utm_campaign=camoufox_sponsorship) | [Scrappey](https://scrappey.com/?utm_source=camoufox&utm_medium=sponsorship&utm_campaign=camoufox_sponsorship) is a Web Scraping API that only charges successful scrapes with pay as you go - no subscriptions. Scrape complex sites. Residential proxies included, no hidden proxy fees, or expiring balances. One API for direct HTTP, full-browser rendering, JavaScript-heavy pages, screenshots, sessions, 30+ browser actions and 200+ concurrent sessions at a time - trusted by 1000+ developers and AI agents. Get 10% off with code CAMOUFOX. |

## Proxy providers

Camoufox is intended to be used with rotating proxies (preferably residential IPs). Check out these providers:

|  |  |
| --- | --- |
| [![proxyempire](https://assets.kitploit.com/production/public/readmes/41473/92b2725ccb0fcf098cecc9fcc0e7042971b4f772051861f723569460460d3664.png)](https://proxyempire.io/?ref=camoufox&utm_source=camoufox) | **🚀 Camoufox × ProxyEmpire**  Running Camoufox? Your proxy layer decides whether you scale — or get blocked.  [ProxyEmpire](https://proxyempire.io/?ref=camoufox&utm_source=camoufox) delivers:  • 🌍 30M+ Residential IPs (170+ countries)  • 📱 4G/5G Mobile Proxies  • 🔄 Rotating & Sticky Sessions  • ⚡ Unlimited Concurrent Sessions  • 🎯 Precise geo-targeting  • HTTP, HTTPS & SOCKS5 Support  Built for scraping, automation, and high-stealth workflows.  **🔥 Exclusive Offer** - Use code **Camoufox30**  Get **30% recurring discount** (not just first month). Upgrade your proxies. Reduce bans. Scale properly |
| [![birdproxies](https://assets.kitploit.com/production/public/readmes/41473/456ce202471adb0c98121d95c2bf1d76cb6a9def3cdf50921e5b78a2558494ec.png)](https://birdproxies.com/t/camoufox) | Hey, we built BirdProxies because proxies shouldn't be complicated or overpriced. Fast residential and ISP proxies in 195+ locations, fair pricing, and real support.  Try our FlappyBird game on the landing page for free data!  [Try Now](https://birdproxies.com/t/camoufox) | [Discord](https://discord.com/invite/birdproxies) |
| [![rapidproxy](https://assets.kitploit.com/production/public/readmes/41473/1f26966f5a352e9647f168957db44215336f362493ee6f3a93c63078998bcbe9.png)](https://www.rapidproxy.io/?ref=daijro) | [RapidProxy](https://www.rapidproxy.io/?ref=daijro) - Power Your Data with Premium Proxies.  🎁 Try proxies for free + Use code **RAPID10** for **10% OFF**   **Why Choose RapidProxy?**  • 🌍 90M+ IPs in 200+ countries & regions  • ♾️ No expiration on traffic — use anytime, no pressure  • 🔥 Unlimited concurrency for maximum performance  • 💰 Starting from just $0.65/GB ...