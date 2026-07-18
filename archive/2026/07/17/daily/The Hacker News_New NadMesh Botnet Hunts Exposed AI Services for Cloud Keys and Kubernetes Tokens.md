---
title: New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens
url: https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html
source: The Hacker News
date: 2026-07-17
fetch_date: 2026-07-18T04:46:39.660602
---

# New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [New NadMesh Botnet Hunts Exposed AI Services for Cloud Keys and Kubernetes Tokens](https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html)

**Swati Khandelwal**Jul 17, 2026Botnet / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm0yasBDyeN2fn4q4y7Zs2Y6FvTDTIrI3xi4iN2ZBBUIBoCxLshnVvYc8OPDOrpSuHiyUNO0MLi-50Kf05SxJSo3m1n-PDfKnM3ztP48lWYBz_2IDzR2gNQ0D3-AzQcR6ZJC9qvBgM5wX3RCIaw6mAA7zDh3xAWFFoHScqZuqKSifh-FUr8Qum5dYGQPw/s1700-e365/botnet-malware.jpg)

A Go botnet called **NadMesh** turned up in early July hunting exposed AI services, and the operator's own dashboard claims 3,811 unique AWS keys.

A Shodan harvester keeps the scan queue stocked with ComfyUI, [Ollama](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html), [n8n](https://thehackernews.com/2026/03/cisa-flags-actively-exploited-n8n-rce.html), [Open WebUI](https://thehackernews.com/2025/06/cryptojacking-campaign-exploits-devops.html), [Langflow](https://thehackernews.com/2026/06/unpatched-langflow-flaw-cve-2026-5027.html), and Gradio: the image generators, local model runners, and workflow builders that teams stand up fast and firewall late.

The intel feed behind that counter shows 47 credential hauls and 41 model inventories in its last 100 records. Those inventories carry DeepSeek, GLM, and Kimi identifiers tagged :cloud, which suggests that what the bots catalogue reaches past the box itself.

QiAnXin's XLab [published](https://blog.xlab.qianxin.com/nadmesh-botnet-analysis-a-product-grade-threat-for-the-ai-service-era-en/) a report on Friday, named the malware after the "n4d mesh controller" string in its source, and screenshotted the panel. The figures on it are the operator's own, captured July 10, and they do not agree with each other.

A counter reading 17,700 total deploys sits above a funnel claiming 95,700 in the past 24 hours. One tile says 16 active bots; the next says 12. The credential number is at least the one it states twice. XLab's own sensors give an outside measure, and it is not a bot count either: distinct source IPs pushing NadMesh sat near zero through late June, then went vertical in the first week of July to around 139 a day.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

What a bot ships home is cloud keys pulled out of environment variables, k8s service account tokens, and the contents of ~/.aws/config, .env, and ~/.docker/config.json.

The researchers put it plainly: the operator is after "not the host itself, but the cloud credentials, Kubernetes cluster privileges" on it. Model access and callable MCP tools round out the list.

[MCP](https://thehackernews.com/2025/12/threatsday-bulletin-whatsapp-hijacks.html) heads the controller's priority order for exploitation, above [Kubernetes, Docker API, and Redis](https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html), and the vector XLab records beside it is a JSON-RPC tools/call to execute\_command. No CVE is attached to that line, and the report does not claim one.

MCP's [first specification](https://modelcontextprotocol.io/specification/2024-11-05/basic) put authentication outside the core protocol entirely, and the [authorization flow added in March 2025](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) is still optional in the spec's own words. Plenty of deployments skip it. [Censys](https://censys.com/blog/mcp-servers-on-the-internet/) counted 12,520 reachable MCP services across 8,758 IP addresses as of April 28, more than 21,000 by May 6, and roughly 90 advertising a tool that runs commands.

On 39 of those, the tool was named execute\_command, the exact call at the top of NadMesh's table. The botnet's own MCP counters do not reconcile: 12,100 MCP services listed as exploitable, 21 MCP vulnerabilities overall, and none at all among the 100 intel records on screen.

Then there is what XLab actually watched it throw. The firm charted the exploit traffic it observed, and docker\_containers\_api\_rce takes 30.31% of it, jenkins\_scripttext\_rce another 22.28%. Telnet weak passwords take 10.36%, Redis 8.29%.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzE6rH4pdCVUsca4Gi3PtJVnsnAB9mLh5W3hIVWZB6nFsH5H3BKKEowEZPaSyDzn3nbVG4hqur3NnzmoB515Q5ISMZJC-m0xQ1J2AAFDdshuqkbM3AlRW6D4d6dccXZ7iRjJJYszQoyClWmEXK4Wz96xTtES98OB6cJUqflP_ry_iyCoWxiYWLtdUbOwQ/s1700-e365/cve.png)

mcp\_cmd\_execute is on the chart, so the vector is in XLab's observed traffic, but it sits in the unlabeled tail below the smallest slice anyone bothered to label, at 0.78%. The chart's labels do not match the controller's own status strings, so it is XLab's sensor view of attempts, not the operator's success ledger.

So the AI targeting is real at the intake and in the loot, and most of the exploit traffic still goes to Docker sockets and Jenkins consoles.

The scanning feeds itself. Subnets that produce hits get resampled more densely every five minutes; IPs flagged dangerous in the last 24 hours come back every quarter hour as /32 rescans with the AI ports first; a full sweep drags everything marked dangerous in the last seven days back to the top.

Any target that absorbs ten deployment attempts without ever returning a result is auto-blacklisted as a suspected honeypot. XLab takes that as a sign the author knows researchers are watching. If the queue runs dry, bots generate a random /24 and keep going.

Five build versions run concurrently, eleven bots on 33.8-GO-TITAN, and the stragglers back on 30.0. A canary endpoint stages new builds to a slice of the fleet, 5,448 responses served, and 84,024 null. A funnel tracks tasks down through deploys to live hosts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSMkgSZ1G5EgYs0eLg_KHlUu6CGA4BCiBZCoGKWo2N1wcXWhNPuJjgblgKKPFiSmo9xv4tXcLp5QCZyavVrlTlb-1o9Eqaf2Zof6EY1nwBxLt3L71cFQ...