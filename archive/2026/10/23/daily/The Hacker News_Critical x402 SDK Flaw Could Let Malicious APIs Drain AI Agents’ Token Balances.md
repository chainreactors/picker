---
title: Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents’ Token Balances
url: https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html
source: The Hacker News
date: 2026-10-23
fetch_date: 2026-10-24T06:48:22.655674
---

# Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents’ Token Balances

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Critical x402 SDK Flaw Could Let Malicious APIs Drain AI Agents’ Token Balances](https://thehackernews.com/2026/10/critical-x402-sdk-flaw-could-let.html)

**Swati Khandelwal**Oct 23, 2026Artificial Intelligence / Cryptocurrency

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1nl6HARmLzzb4BlklarhKxB1F2U6dwKebASj9-Ow-WI6otLzFoATEY-icF7OCAgwHqRzwNhs9jHY2S7e4ZGRHykrIzedvLxQlAyen6jQsOoY_L80gd0Lrjy3-3xzlHavaxahxsI1o13_r2MRRDwbQrtslkXfbITBGcp_736F1sPVq7dR8Rnq_JSVQP3A/s1700-nu-rw-lo-l85-e365/ai-wallet.jpg)

AI agents paying for API calls with the [x402 SDKs](https://github.com/x402-foundation/x402) could sign a payment for their full balance of a supported token if a malicious API asked for it, [security firm V12 said](https://v12.sh/blog/x402) on October 22.

The cause was the SDKs' default client, which set no spending limit until releases on August 18 added one. The risk was limited to agents who automatically signed payments and whose apps set no limits.

The missing limit is one of 25 flaws V12 found in the x402 code, and one of three it rated critical and described in detail. The x402 Foundation, which maintains the SDKs, had already fixed all three critical flaws in the August 18 releases.

One of the other two let a facilitator, the service that checks x402 payments, accept a Solana transaction that moved no tokens as a valid payment. Among the x402 SDKs, only the TypeScript one had this flaw. The other let a malicious server get an agent to sign a login message for a different website.

V12 found the flaws by reviewing the code and running local tests. Neither V12 nor the x402 Foundation has publicly reported any attacks using them.

The foundation has published no [security advisory](https://github.com/x402-foundation/x402/security/advisories) for the three flaws, and its changelogs list the fixes without calling them security fixes. As of October 23, npm audit returned no advisories for the last TypeScript releases before the fixes, and PyPI listed no vulnerabilities for the last Python release before them, The Hacker News found. A developer who relies on those checks gets no warning to upgrade.

Coinbase created x402 and handed it to the [x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications) this year, a Linux Foundation project whose members include Visa and Mastercard. Coinbase holds the most senior seat on the foundation's [technical steering committee](https://github.com/x402-foundation/x402/blob/main/TSC.md).

### No Spending Limit in the Default Client

x402 is an open standard that lets software, including AI agents, pay for an API call within the web request itself, without requiring a person to approve each payment.

A server that wants payment answers with the HTTP status code 402 Payment Required and lists its payment options, each with an amount, a token, and a recipient. The client picks one, signs a payment, and sends the request again.

The default client took the first option on the list, and before the fix, it set no limit on the amount.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

A hostile API could use that to turn a routine data request into a request for the wallet's full balance of a supported token, V12 said. An earlier small payment could reveal the wallet address, so the server could look up the balance first.

With an automatic signer and no payment policy set by the app, the client could sign a payment for that amount. For a token that supports signed transfers, the attacker could then submit the signed payment and collect the funds.

The August 18 releases added spend controls to the [TypeScript](https://github.com/x402-foundation/x402/pull/3124), [Python](https://github.com/x402-foundation/x402/pull/3154), and [Go](https://github.com/x402-foundation/x402/pull/3156) clients. By default, they now cap each payment at $1 and allow only US dollar stablecoins the SDK recognizes, such as USDC.

### Token Approvals Accepted as Solana Payments

In x402, a merchant's server relies on a facilitator to check each payment and submit it to the blockchain. On Solana, the facilitator also pays the transaction fee.

The TypeScript facilitator code for Solana checked that a payment called an allowed token program, then read it as a transfer without checking the instruction type. A token approval, which lets another account spend tokens later but moves none itself, differs from a transfer only in its first byte.

In V12's local test, the facilitator accepted such an approval as a valid payment. The test did not send a live transaction.

A merchant relying on the facilitator could therefore deliver a paid resource while receiving no tokens, V12 said, calling it "a complete payment bypass." The attacker needed a token account, but no balance, and the facilitator paid the transaction fee each time.

The Python and Go SDKs already checked the instruction type. The August 18 releases [added the same check](https://github.com/x402-foundation/x402/pull/3132) to the TypeScript code.

Every published @x402/svm release from 2.0.0 to 2.22.0 lacks the check, and every release from 2.23.0 on has it, The Hacker News found by searching the published packages.

### Logins Signed for Other Websites

x402 also has a sign-in extension called Sign-In-With-X (SIWx). It lets an agent log in by signing a short message with its wallet, for example to prove an earlier payment instead of paying again. On Ethereum, the message names the website, the wallet address, and a one-time code.

The automated client signed these messages without verifying that the website named in them was the one it had contacted.

A malicious server could get a fresh login message from another site, pass it to the agent, and use the signature to log in to that site as the agent's wallet, V12 said. T...