---
title: Don’t Let API Leaks Sink Your Ship | API Security Newsletter
url: https://buaq.net/go-147718.html
source: unSafe.sh - 不安全
date: 2023-02-03
fetch_date: 2025-10-04T05:33:55.557318
---

# Don’t Let API Leaks Sink Your Ship | API Security Newsletter

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9b2584acfd06618cde8e17336224f900.jpg)

Don’t Let API Leaks Sink Your Ship | API Security Newsletter

Leaks of API keys and other secrets. The industry has been abuzz with news about attacks – an
*2023-2-2 22:24:48
Author: [lab.wallarm.com(查看原文)](/jump-147718.htm)
阅读量:41
收藏*

---

Leaks of API keys and other secrets. The industry has been abuzz with news about attacks – and the ongoing ripple effect – involving leaked API keys, credentials and other secrets. This adds another dimension to your API attack surface, which in turn complicates your defenses and adds to your workload. So, this month the focus of The APIary is on leaked API keys and other secrets – read on for this month’s bit o’ honey.

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Note-from-Ivan.png?resize=300%2C103&ssl=1)

2023 certainly started with a bang. News, which dribbled out (perhaps deliberately?) in the waning minutes of 2022 and into early 2023, regarding several development infrastructure breaches involving APIs gave us a lot to think about. For instance:

* **CircleCI** posted an [advisory](https://circleci.com/blog/january-4-2023-security-alert/) in early January regarding a presumed breach of their systems, potentially putting 1000s of organizations at risk.
* **Slack** [notified](https://slack.com/intl/en-gb/blog/news/slack-security-update) the development community on New Year’s Eve that some Slack employee tokens were stolen and misused to gain access to their GitHub repository.
* **LastPass** finally [admitted](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/) on Dec 22nd that an earlier breach back in August, in which credentials and keys were obtained, allowed an adversary nearly unfettered access to a cloud-based backup system, putting end users’ password vaults at risk.
* **Travis CI** continues to have issues, with the latest coming from researchers who [reported last summer](https://arstechnica.com/information-technology/2022/06/credentials-for-thousands-of-open-source-projects-free-for-the-taking-again/) that they had found over 73,000 tokens, secrets, and various credentials.

These incidents, all involving leaked API keys and other secrets at some point, are another example of the growing API attack surface that many may not be aware of. And while it’s absolutely necessary to mitigate this issue as early as possible (i.e., during the development process), it’s also true that it’s impossible to prevent the issue entirely.

Why? Because of increasing development velocity, tech stack complexity and of course SW supply chain risks. That’s why we’ve just dropped an “early release” version of our new [**API Leak Management**](https://lab.wallarm.com/introducing-proactive-api-leak-management/) capability. It provides actionable threat intelligence regarding leaked API keys and other secrets from your domain, covering your entire API portfolio. Read on to learn more!

Speaking of API-related breaches, by now you’ve undoubtedly heard about another T-Mobile breach, this one impacting 37M customers. If not, read [the coverage](https://www.infosecurity-magazine.com/news/api-attacker-steals-data-37/) by the always excellent Phil Muncaster in Infosecurity Magazine, or head over to [our blog post](https://lab.wallarm.com/learn-from-the-t-mobile-api-breach-to-improve-your-api-security-program-in-2023/). It’s just another proof point that API security needs to be at the forefront of everyone’s minds, and 2023 security plans!

 – Ivan, CEO & Co-Founder, Wallarm

PS – Stay up-to-the-minute on all the latest news about [#apisecurity](https://www.linkedin.com/feed/hashtag/?keywords=apisecurity&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A6999039478417825792) exploits and updates by following our new [**API ThreatStats LinkedIn page**](https://www.linkedin.com/company/threatstats/).

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Poll-header.png?fit=770%2C103&ssl=1)

Last month we asked whether you use any of the existing cybersecurity frameworks (such as CIS CSC, MITRE ATT&CK, NIST CSF, etc.) for managing your API Security? It looks like most of you are well down this path, although almost one-third say it’s not on your radar:

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/January-poll-results-1.png?resize=512%2C409&ssl=1)

And we’d love to have you weigh in on our next **LinkedIn poll** we’re conducting: ***[How confident are you that \_none\_ your API keys and other secrets have leaked into the wild?](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7026628486760910848)*** Please let us know where you stand on this – [connect with Ivan](https://www.linkedin.com/in/d0znpp/) or [follow us at Wallarm](https://www.linkedin.com/company/wallarm/) to register your vote.

![](https://i0.wp.com/lab.wallarm.com/wp-content/uploads/2023/02/Industry-News-header.png?fit=770%2C103&ssl=1)

[**Devs urged to rotate secrets after CircleCI suffers security breach**](https://portswigger.net/daily-swig/devs-urged-to-rotate-secrets-after-circleci-suffers-security-breach)

(***The Daily Swig***) Developers are being urged to rotate secrets and API tokens following the discovery of a breach at popular [DevOps](https://portswigger.net/daily-swig/devsecops) platform CircleCI.

[**3Commas API Leak Highlights Yet Another Way to Lose Your Money**](https://www.securities.io/3commas-api-leak-highlights-yet-another-way-to-lose-your-money/)

(***Securities.io***) In today’s digital age, it’s more important than ever to guard against the potential risks of API leaks, as it can lead to the loss of personal information and financial data.

[**Toyota, Mercedes, BMW API flaws exposed owners’ personal info**](https://www.bleepingcomputer.com/news/security/toyota-mercedes-bmw-api-flaws-exposed-owners-personal-info/)

(***BleepingComputer***) Almost 20 car manufacturers and services contained API security vulnerabilities that could have allowed hackers to unlock, start, and track cars, and/or expose customers’ personal information.

[**Employee Tokens Stolen Through Slack GitHub Account**](https://informationsecuritybuzz.com/employee-tokens-stolen-through-slack-github-account/)

(***Information Security Buzz***) Indications are that intruders used stolen employee tokens to download private code from the company’s GitHub repository.

[**Twitter data breach shows APIs are a goldmine for PII and social engineering**](https://venturebeat.com/security/twitter-social-engineering/)

(***VentureBeat***) Insecure APIs provide cybercriminals with direct access to user’s personally identifiable information ([PII](https://venturebeat.com/data-infrastructure/the-new-meaning-of-pii-can-you-ever-be-anonymous/)), usernames and passwords when a client connects to a third-party service’s API.

[**API Security Is the New Black**](https://www.darkreading.com/dr-tech/api-security-is-the-new-black)

(***DarkReading***) API attacks are back in the news. It turns out the likely ingress point for the [Optus breach](https://www.darkreading.com/attacks-breaches/fbi-helping-australian-authorities-investigate-massive-optus-data-breach-reports) was a lowly REST API. And someone has leaked all of the data stolen from the [Twitter breach](https://venturebeat.com/security/twitter-breach-api-attack/) — which also involved an API.

[**To Solve the API Security Crisis, Think Beyond OWASP**](https://securityboulevard.com/2023/01/to-solve-the-api-security-crisis-think-beyond-owasp/)

(***Security Boulevard***) APIs have now become the top attack vector for enterprises to worry about, [accordin...