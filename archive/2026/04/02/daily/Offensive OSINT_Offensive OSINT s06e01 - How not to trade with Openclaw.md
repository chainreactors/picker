---
title: Offensive OSINT s06e01 - How not to trade with Openclaw
url: https://www.offensiveosint.io/offensive-osint-s06e01-how-not-to-trade-with-openclaw/
source: Offensive OSINT
date: 2026-04-02
fetch_date: 2026-04-03T04:27:26.724527
---

# Offensive OSINT s06e01 - How not to trade with Openclaw

[![Offensive OSINT](https://www.offensiveosint.io/content/images/2020/07/OffensiveOsint-logo-RGB-2.png)](https://www.offensiveosint.io)

[About me](/about-me/)
[Sign in](/signin/)

##### Search Here

×

![Offensive OSINT s06e01 - How not to trade with Openclaw](/content/images/size/w2000/2026/03/roman-denisenko-XMtz9nIdljQ-unsplash.jpg)

Offensive OSINT
02.04.2026

# Offensive OSINT s06e01 - How not to trade with Openclaw

Coming up on the post we see what "alternative data" looks like when your budget is zero, an AI that spent 80k tokens explaining Middle East dynamics only to conclude "XLE remains a hold", and Raspberry Pi that trades better than I do.

**TL;DR**

*I gave an AI agent trading authority on a $10k Alpaca paper account and watched what happened. Behind it sits a real-time alternative & stock data platform I built, deployed on a Raspberry Pi 4 alongside OpenClaw. The agent has instruction files defining its personality, trading philosophy, and a step-by-step workflow it follows every 30 minutes during market hours. When a strong signal shows up, it trades without any confirmation needed.
The result so far is that it is still standing but hasn't made me rich. The infrastructure works, the failures have been learned, and the agent works as expected with couple minor issues. This post covers how it's built, what went wrong, and where is the place for improvement.*

Long time no post from me due to handover of [https://www.os-surveillance.io/](https://www.os-surveillance.io/?ref=offensiveosint.io) and preparation to workshop [https://q8asia.com.sg/event/offensive-osint-on-critical-infrastructure-with-ai-2/](https://q8asia.com.sg/event/offensive-osint-on-critical-infrastructure-with-ai-2/?ref=offensiveosint.io) in June, which I sincerely invite you, there are still seats left.

[OSINT Platform for Real-Time Intelligence | Surveillance

Discover an advanced Open Source Intelligence (OSINT) platform for real-time data analysis. Enhance your investigations with tools for monitoring, facial recognition, geolocation, and more. Start today!

![](https://www.offensiveosint.io/content/images/icon/66d505ba263255696d7c80d8_c1a7a189e3091f0fc2bda80dcdb57e8f-32bits-32-2.png)Surveillance

![](https://www.offensiveosint.io/content/images/thumbnail/66d1b3f24427e9c56d02ca71_logo-v2-2.png)](https://www.os-surveillance.io/?ref=offensiveosint.io)

## Predi

Almost every human action leaves a measurable trace that touches the market. You tweet about a product, you search for a company's name, you visit a store. All of it aggregates into signals that trained analysts pay a lot of money to see early.
The expensive version of this is companies like YipitData or other that include satellite imagery of parking lots, foot traffic data or credit card aggregates. What I built is the very very budget version.
I thought that if you can gather real-time public data and give it proper context, and you're curious about current events, then it's reasonable to think that AI can be finally useful.
PREDI started from one observation of fire hotspots detected by NASA's FIRMS satellite system, that was used in OS-Surveillance btw. A cluster of thermal anomalies near a steel mill or power plant tells you something about production levels. That same data becomes a signal when you cross-reference it with shipping routes, energy imports, or a company's recent SEC filings. The trick is doing that cross-referencing automatically and cheaply.

### Coverage

The platform covers 80+ sources which are broken down into four buckets.

![](https://www.offensiveosint.io/content/images/2026/03/Screenshot_83-3.png)

Tribute to Thomson Reuters Eikon

**Market-facing data** is the core: SEC filings (8-Ks, Form 4 insider transactions, 13D/G activist positions, the full EDGAR feed), unusual options flow, earnings calendars and surprises, analyst upgrades/downgrades, congress trades, prediction markets and more.

**Macro and economic signals** give the bigger picture: Fed releases, CFTC COT data, EIA petroleum and gasoline reports, FRED macro series, BLS data, short interest, FINRA data. Slower moving, updated daily at most, but important for context when something in the market-facing bucket pops up.

**Real-time noise detection** catches things as they're happening: trending search keywords, autocomplete across Google and e-commerce platforms, GDELT news articles, Twitter/Reddit trending, Wikimedia most-visited pages, financial press releases, GitHub trending repos, app store rankings. Most of this stuff is just noise by itself, but it gets interesting when their correlation engine starts seeing the same keywords popping up across different sources at the same time.

**The weird stuff** is what makes it interesting: NASA FIRMS fire hotspots near industrial facilities, vessel tracking through shipping chokepoints, flight tracking including military callsigns, NOTAMs, natural disasters, earthquake data, CISA vulnerability alerts, Shodan exposed infrastructure per company or popular phishing targets. Half of these sound irrelevant until they aren't. A cluster of thermal anomalies near a steel mill tells you something about production. A military callsign showing up over the Gulf tells you something about escalation risk.

In practice, the categories that have produced the most actionable signals so far are SEC filings (especially 8-K items 2.01 and 2.02), unusual options flow, and the correlation engine when it flags the same ticker across multiple sources at once. The rest is useful context.

I skipped job boards (high effort, marginal signal) and traditional alt data like satellite imagery or foot traffic due to costs.

### Workflow

PREDI was built mostly with help of OpenAI Codex (5.3 and 5.4 on high-reasoning mode). Good at integration work, not that great at writing scrapers from scratch. So the workflow became that I write the proof of concept scraper for each source and Codex integrates it into the broader platform. It was actually pretty fun, and efficient once you accept that AI assistants are better at fitting into existing infrastructure rather than creating something from the beginning.

Tasks to request data run periodically as cronjobs, for almost whole day, depending on the update time of the source. Realtime Google search and finance news run more often than Most Visited Communities in Reddit or NOTAM module.

Since the data comes from different sources, the first challenge is schema normalization. Everything needs to be in a consistent format before the agent sees it, because token costs add up fast.

The most interesting piece is the correlation engine. It's a dedicated endpoint that looks for the same keyword appearing across multiple sources at the same time. One source mentioning a ticker is noise. The same ticker showing up in unusual options flow *and* realtime search *and* an SEC 8-K filed that's potentially tradeable. The agent uses this as its first filter.

### API

The agent queries everything through an API. The design choices were driven by keeping token costs under control.

Every endpoint supports `?slim=1`, which strips the response to essential fields only, with no metadata. The `/api/digest/` endpoint aggregates all text-based sources (headlines, trending topics, events) into a single structured response the agent reads every cycle, instead of polling dozens of endpoints individually.

```
"correlations": [
    {
        "k": "iran israel war",
        "n": 6,
        "src": [
            "bing",
            "gdelt",
            "google",
            "massive_news",
            "polymarket",
            "yahoo_finance_news"
        ]
    },
    {
        "k": "FIRST HILL SECURITIES, LLC filed X-17A-5",
        "n": 5,
        "src": [
            "alphavantage_news",
            "businesswire",
            "prnewswire",
            "sec_8k",
            "sec_edgar"
        ]
    },
    {
        "k": "U.S. gasoline 3.961 $/GAL",
        "n": 5,
        "src": [
   ...