---
title: Staying ahead of censors in 2025: What we've learned from fighting censorship in Iran and Russia
url: https://blog.torproject.org/staying-ahead-of-censors-2025/
source: Tor Project blog
date: 2025-12-03
fetch_date: 2025-12-04T03:19:47.450135
---

# Staying ahead of censors in 2025: What we've learned from fighting censorship in Iran and Russia

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Staying ahead of censors in 2025: What we've learned from fighting censorship in Iran and Russia

by [meskio](/author/meskio) and [shelikhoo](/author/shelikhoo)
| December 3, 2025

![](/staying-ahead-of-censors-2025/lead.png)

From internet blackouts in Iran to Russia's evolving censorship tactics, 2025 has tested Tor's anti-censorship tools like never before. These are the moments where the work of Tor's anti-censorship team is more important than ever, to fulfill our mission of preserving connectivity between users in affected regions and the rest of the world.

In this blog post, we want to talk about what we've learned, how we've adapted, and what other internet users can do to keep Tor users connected.

## Iran

In June, during the war between Iran and Israel, the censorship in [Iran intensified up to a point where internet was disconnected for few days](https://filter.watch/english/2025/10/02/irans-stealth-blackout-a-multi-stakeholder-analysis-of-the-june-2025-internet-shutdown/). Presumably to impede espionage-related communication while simultaneously consolidating political power.

### Monitoring the censorship landscape

During this period, we were constantly monitoring the situation using our in-region vantage-point system. This vantage-point system is a network of monitoring locations inside Iran that provides more recent and accurate information about censorship than is available from public data.

One clear example is domain-fronting data. Domain-fronting is a technique that makes Tor traffic look like other popular, harder-to-block websites (like major cloud services). To determine which domain-fronting configurations perform best across the most locations, we deployed an automated testing tool that detects and reports the accessibility of the Snowflake broker and the Moat service for each domain-fronting configuration at each of our vantage points. This information is then aggregated by the log collector and subsequently used to monitor the domain-fronting configurations currently in use and to select the configurations to use in the future.

### Strengthening Snowflake

[Snowflake](https://snowflake.torproject.org/) is the most used network traffic obfuscation tool in Iran. Over the past year we have been working on improving it to ensure that it remains strong and accessible to users.

We have upgraded the web extension to Manifest Version 3 (the latest browser extension standard), to be compatible with modern browsers. We improved the NAT checking logic which helps us figure out what kind of network setup each user has. This way, the proxies are more accurately assigned to the clients depending on their network capabilities. And we enhanced the metrics reported by the standalone proxy, providing better tooling for proxy operators to assist what is happening with their proxies.

Under the hood we have created a staging server for Snowflake, so we have a robust infrastructure to stress test new features making sure they're fit for real deployment. This will help us bring big changes in the coming year to improve the efficiency of the protocol where networks are severely disrupted and to create better mechanisms to prevent censors from blocking Snowflake.

### Deploying Conjure

Censorship agencies like those in Iran often attempt to block bridges by obtaining bridge information in bulk and then inputing the network address of these bridges to their censorship gateways to block them. That's why we developed Conjure.

Conjure is a pluggable transport designed to stay ahead of proxy-listing-based blocking by leveraging unused address space within cooperating ISP networks, thereby limiting the damage caused by blocking individual network addresses. Think of it like the act of generating temporary email addresses to avoid spam emails, by making sure the address is temporary and easy to regenerate, anything blocked at that address won't affect your ability to get new ones.

We are working on distributing Conjure in places with strong censorship. To make it hard for censors, we have improved Tor's implementation of Conjure by extending the protocols used both for bootstrapping the connection and transport the data. We added multiple registration methods (DNS and AMP-cache), making the bootstrap of the conjure connection more censorship-resistant and the connection will look as if the user is connecting to widely used service. We also integrated additional transports from upstream (DTLS and prefix) that makes the Tor traffic look like common protocolsâmeaning regular internet traffic.

## Russia

Another region that has experienced many changes this year is Russia. With continued conflict and attrition, internet censorship has intensified, including increased allowlist-based censorship and address-block-based censorship.

Last year, we introduced WebTunnel as a new pluggable transport. We have seen this year how WebTunnel has become a key tool for users in Russia, thanks to its ability to blend into regular web traffic. As the severity of censorship in Russia has increased, WebTunnel has also received several fixes, such as SNI imitation and safe non-WebPKI certificate support with certificate-chain pinning to ensure it can withstand more kinds of censorship, including SNI allowlisting and the rapid blocking of distributed bridges.

Many of these improvements come from volunteers or are shaped by user feedback. Our community of users and supporters makes all this work possible and helps us stay ahead at Tor. Thanks to our Tor community team, we have first-hand insights into what works and what doesn't. This gives us access to the best information in the region. Additionally, through the community team's work with people on the ground, we receive support in testing and identifying the best technology for each censorship scenario.

### Experimenting with bridge distribution

When we started distributing WebTunnel bridges in December they were a very useful tool to connect to Tor. They worked well for months, and Tor Browser users got them configured automatically over Connect Assist if they were located in Russia. However, in June, the Russian censors began listing most of our WebTunnel bridges, prompting us to shift strategies.

In recent history, our Telegram distributor has proven to be a useful tool in Russia, as the censor has a harder time extracting all the bridges from it. This is why we have now added support for WebTunnel in our Telegram distributor. We are always trying to meet our users where they are, and while Telegram might not be the safest place for your online communications, many users in Russia already uses it. And is not only useful for Russian users, but also for Iranian ones that are currently using webtunnel bridges distributed over Telegram.

All these fast changes of bridges distribution are possible thanks to [rdsys](https://blog.torproject.org/making-connections-from-bridgedb-to-rdsys/), Tor's new bridge distribution system that we introduced last year. This year we kept improving rdsys adding a staging server, so we can stress-test it in a similar environments to the ones used in production. For our censored users that means that by the time new and updated anticensorship features arrive, we have already been able to fix many stability issues.

## Where do we go from here?

Supporting our users to continue fighting censorship is what our work is all about. Making it possible to connect to the Tor network on censored networksâwhatever they are. Whether it is your university, your internet service provider, or your government trying to keep you from getting the information you are entitled to. Next year we'll start rolling out Conjur...