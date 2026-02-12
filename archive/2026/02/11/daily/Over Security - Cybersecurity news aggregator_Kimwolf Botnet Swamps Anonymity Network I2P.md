---
title: Kimwolf Botnet Swamps Anonymity Network I2P
url: https://krebsonsecurity.com/2026/02/kimwolf-botnet-swamps-anonymity-network-i2p/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-11
fetch_date: 2026-02-12T04:22:50.518634
---

# Kimwolf Botnet Swamps Anonymity Network I2P

Advertisement

[![](/b-knowbe4/44.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

Advertisement

[![](/b-doppel/6.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=outpace)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Kimwolf Botnet Swamps Anonymity Network I2P

February 11, 2026

[1 Comment](https://krebsonsecurity.com/2026/02/kimwolf-botnet-swamps-anonymity-network-i2p/#comments)

For the past week, the massive “Internet of Things” (IoT) botnet known as **Kimwolf** has been disrupting **The Invisible Internet Project** (I2P), a decentralized, encrypted communications network designed to anonymize and secure online communications. I2P users started reporting disruptions in the network around the same time the Kimwolf botmasters began relying on it to evade takedown attempts against the botnet’s control servers.

Kimwolf is a botnet that surfaced in late 2025 and quickly infected millions of systems, turning poorly secured IoT devices like TV streaming boxes, digital picture frames and routers into relays for malicious traffic and [abnormally large](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/) distributed denial-of-service (DDoS) attacks.

I2P is a decentralized, privacy-focused network that allows people to communicate and share information anonymously.

“It works by routing data through multiple encrypted layers across volunteer-operated nodes, hiding both the sender’s and receiver’s locations,” the [I2P website explains](https://i2p.net/). “The result is a secure, censorship-resistant network designed for private websites, messaging, and data sharing.”

On February 3, I2P users began [complaining on the organization’s GitHub page](https://github.com/PurpleI2P/i2pd/issues/2312#issuecomment-3875275177) about tens of thousands of routers suddenly overwhelming the network, preventing existing users from communicating with legitimate nodes. Users reported a rapidly increasing number of new routers joining the network that were unable to transmit data, and that the mass influx of new systems had overwhelmed the network to the point where users could no longer connect.

![](https://krebsonsecurity.com/wp-content/uploads/2026/02/i2p-github.png)

When one I2P user asked whether the network was under attack, another user replied, “Looks like it. My physical router freezes when the number of connections exceeds 60,000.”

![](https://krebsonsecurity.com/wp-content/uploads/2026/02/i2pconnections.png)

The same day that I2P users began noticing the outages, [the individuals in control of Kimwolf](https://krebsonsecurity.com/2026/01/who-benefited-from-the-aisuru-and-kimwolf-botnets/) posted to their Discord channel that they had accidentally disrupted I2P after attempting to join 700,000 Kimwolf-infected bots as nodes on the network.

![](https://krebsonsecurity.com/wp-content/uploads/2026/02/dort-killedi2p.png)

The Kimwolf botmaster openly discusses what they are doing with the botnet in a Discord channel with my name on it.

Although Kimwolf is known as a potent weapon for launching DDoS attacks, the outages caused this week by some portion of the botnet attempting to join I2P are what’s known as a “[Sybil attack](https://en.wikipedia.org/wiki/Sybil_attack),” a threat in peer-to-peer networks where a single entity can disrupt the system by creating, controlling, and operating a large number of fake, pseudonymous identities.

Indeed, the number of Kimwolf-infected routers that tried to join I2P this past week was many times the network’s normal size. I2P’s [Wikipedia page](https://en.wikipedia.org/wiki/I2P) says the network consists of roughly 55,000 computers distributed throughout the world, with each participant acting as both a router (to relay traffic) and a client.

However, **Lance James**, founder of the New York City based cybersecurity consultancy [Unit 221B](https://unit221b.com) and the original founder of I2P, told KrebsOnSecurity the entire I2P network now consists of between 15,000 and 20,000 devices on any given day.

![](https://krebsonsecurity.com/wp-content/uploads/2026/02/i2p-gh-graph.png)

An I2P user posted this graph on Feb. 10, showing tens of thousands of routers — mostly from the United States — suddenly attempting to join the network.

**Benjamin Brundage** is founder of [Synthient](https://synthient.com), a startup that tracks proxy services and was the first to [document Kimwolf’s unique spreading techniques](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/). Brundage said the Kimwolf operator(s) have been trying to build a command and control network that can’t easily be taken down by security companies and network operators that are working together to combat the spread of the botnet.

Brundage said the people in control of Kimwolf have been experimenting with using I2P and a similar anonymity network — [Tor](https://www.torproject.org/) — as a backup command and control network, although there have been no reports of widespread disruptions in the Tor network recently.

“I don’t think their goal is to take I2P down,” he said. “It’s more they’re looking for an alternative to keep the botnet stable in the face of takedown attempts.”

The Kimwolf botnet created challenges for Cloudflare late last year when it began instructing millions of infected devices to use Cloudflare’s domain name system (DNS) settings, causing control domains associated with Kimwolf to [repeatedly usurp](https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/) **Amazon**, **Apple**, **Google** and **Microsoft** in Cloudflare’s public ranking of the most frequently requested websites.

James said the I2P network is still operating at about half of its normal capacity, and that a new release is rolling out which should bring some stability improvements over the next week for users.

Meanwhile, Brundage said the good news is Kimwolf’s overlords appear to have quite recently alienated some of their more competent developers and operators, leading to a rookie mistake this past week that caused the botnet’s overall numbers to drop by more than 600,000 infected systems.

“It seems like they’re just testing stuff, like running experiments in production,” he said. “But the botnet’s numbers are dropping significantly now, and they don’t seem to know what they’re doing.”

*This entry was posted on Wednesday 11th of February 2026 11:08 AM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [DDoS-for-Hire](https://krebsonsecurity.com/category/ddos-for-hire/)

[Benjamin Brundage](https://krebsonsecurity.com/tag/benjamin-brundage/) [DDoS](https://krebsonsecurity.com/tag/ddos/) [I2P](https://krebsonsecurity.com/tag/i2p/) [Kimwolf botnet](https://krebsonsecurity.com/tag/kimwolf-botnet/) [Lance James](https://krebsonsecurity.com/tag/lance-james/) [Sybil attack](https://krebsonsecurity.com/tag/sybil-attack/) [Synthient](https://krebsonsecurity.com/tag/synthient/) [Tor](https://krebsonsecurity.com/tag/tor/) [Unit 221B](https://krebsonsecurity.com/tag/unit-221b/)

Post navigation

[← Patch Tuesday, February 2026 Edition](https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition/)

## One thought on “Kimwolf Botnet Swamps Anonymity Network I2P”

1. [DORT](http://maskify.su) [February 11, 2026](https://krebsonsecurity.com/2026/02/kimwolf-botnet-swamps-anonymity-network-i2p/#comment-650652)

   KIMWOLF INCOMING!!!

   [Reply](https://krebsonsecurity.com/2026/02/kimwolf-botnet-swamps-a...