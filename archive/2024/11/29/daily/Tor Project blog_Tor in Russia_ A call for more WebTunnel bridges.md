---
title: Tor in Russia: A call for more WebTunnel bridges
url: https://blog.torproject.org/call-for-webtunnel-bridges/
source: Tor Project blog
date: 2024-11-29
fetch_date: 2025-10-06T19:19:50.571047
---

# Tor in Russia: A call for more WebTunnel bridges

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Tor in Russia: A call for more WebTunnel bridges

by [gus](/author/gus)
| November 28, 2024

![](/call-for-webtunnel-bridges/lead.png)

Recent reports from Tor users in Russia indicate an escalation in online censorship with the goal of blocking access to Tor and other circumvention tools. This new wave includes attempts to block Tor bridges and pluggable transports developed by the Tor Project, removal of circumvention apps from stores, and targeting popular hosting providers, shrinking the space for bypassing censorship. [Despite these ongoing actions](https://gitlab.torproject.org/tpo/anti-censorship/censorship-analysis/-/issues/40046), Tor remains effective.

One alarming trend is the targeted blocking of popular hosting providers by Roscomnadzor. As many circumvention tools are using them, this action made some Tor bridges inaccessible to many users in Russia. As Roscomnadzor and internet service providers in Russia are increasing their blocking efforts, the need for more [WebTunnel bridges](https://community.torproject.org/relay/setup/webtunnel/) has become urgent.

## Why Webtunnel bridges?

*Webtunnel* is a new type of bridge that is particularly effective at flying under a censors's radar. Its design blends itself into other web traffic, allowing a user to [hide in plain sight](https://blog.torproject.org/introducing-webtunnel-evading-censorship-by-hiding-in-plain-sight/). And since its launch earlier this year, we've made sure to prioritize small download sizes for more convenient distribution and simplified the support of uTLS intergration further mimicing the characteristics of more widespread browsers. This makes Webtunnel safe for general users because it helps conceal the fact that a tool like Tor is being used.

We are calling on the Tor community and the Internet freedom community to help us scale up WebTunnel bridges. If you've ever thought about running a Tor bridge, **now is the time**. Our goal is to deploy **200 new WebTunnel bridges** by the end of this December (2024) to open secure access for users in Russia.

## How to run a Tor WebTunnel bridge

On the International Day Against Online Censorship in March, we published a blog post introducing [WebTunnel: "Hiding in Plain Sight"](https://blog.torproject.org/introducing-webtunnel-evading-censorship-by-hiding-in-plain-sight/). Setting up a WebTunnel bridge requires some system administration skills, but we've streamlined the process to make it as straightforward as possible.

**1. Using Docker:** We offer a Docker image that simplifies deploying the Tor bridge and WebTunnel transport. Some additional configuration of your web server is required.

**2. Ansible automation:** A WebTunnel Ansible role, created by community member Jacobo NÃ¡jera, provides another way to set up a WebTunnel bridge quickly.

You can find the technical requirements in our [WebTunnel guide](https://community.torproject.org/relay/setup/webtunnel/). In short, you'll need:

* A static IPv4 address (preferred)
* A self-hosted website
* A valid SSL/TLS certificate (e.g., Let's Encrypt)
* Bandwidth usage: at least 1 TB/month, but more is recommendable.

**Important:** Avoid using free shared DNS services, as they are frequently blocked in Russia and other regions. Consult our community [Good/Bad ISPs](https://community.torproject.org/relay/community-resources/good-bad-isps/) page for finding a provider for your WebTunnel bridge and avoiding popular hosting companies.

## Bridge campaign rules for participation

**The campaign starts today, November 28, 2024, and will run until March 10, 2025.** As a token of our appreciation for your volunteer work, we're offering a Tor t-shirt to operators who run 5 or more WebTunnel bridges during this period. Please note: Only one t-shirt will be awarded per operator. See the technical requirements below to participate in the campaign.

### Technical requirements for campaign

1. Operators must run one WebTunnel bridge per IPv4. It is acceptable to use multiple subdomains or distinct domains.
2. Include a valid email address as your contact information. Or we won't be able to confirm and validate your participation in the campaign.
3. Maintain your bridges running for at least 1 year.
4. Ensure your bridges have a solid uptime, operating close to 24/7. Reboots for updates are fine.
5. Your bridge must remain functional during the campaign period.
6. Do not host your bridges with [Hetzner](https://ntc.party/t/12845).

### How to participate

After spinning up and verifying that your five WebTunnel bridges are working, confirm your participation by emailing frontdesk@torproject.org with the following template:

```
Subject: Participation in Bridge Campaign 2025
Body: Hi,
I'm signing up for the Tor Bridge Campaign. These are my bridges:
    <Add here your bridge lines>
My t-shirt is (pick your size: https://gitlab.torproject.org/tpo/community/team/-/wikis/tshirts/tshirt-size-charts).
```

To validate your participation, please contact us using the same email address listed in your contactinfo. You can expect your reward to be shipped in **Q2 2025**.

## Russian censors targeting pluggable transports

Tor-powered applications like Tor Browser include built-in censorship circumvention features, but censors in Russia are increasingly targeting these mechanisms. For example, user reports suggest that [obfs4 connections are being blocked on some 4G mobile networks in Russia](https://gitlab.torproject.org/tpo/anti-censorship/censorship-analysis/-/issues/40050). Despite this, obfs4 remains the most widely used pluggable transport for Tor users in the country. Snowflake has also experienced partial blocks at certain providers and Tor's [Anti-Censorship Team have been investigating](https://gitlab.torproject.org/tpo/anti-censorship/pluggable-transports/snowflake/-/issues/40407).

Analyzing censorship tactics, developing fixes, and implementing new mitigations takes time and resources. In the meantime, Tor WebTunnel bridges serve as an urgent and immediate way to bypass censorship in Russia.

Tor-powered applications are critical for combating online censorship in heavily restricted regions. In a country where ["the biggest banks were instructed to punish customers using credit cards to pay for VPN services"](https://cepa.org/article/russias-bankers-become-secret-policemen/), free and open source tools like Tor are some of the few remaining alternatives for keeping users connected.

## Background: Tor blocked in Russia (2021)

In late 2021, the Russian government attempted to block Tor, [as we detailed in our blog post.](https://blog.torproject.org/tor-censorship-in-russia/) Despite the censors' best efforts, Russian users were able to circumvent the block using Tor bridges.

Upon launch of WebTunnel in early 2024, we only had 60 WebTunnel bridges. Today, the number has more than doubled to 143. However, we must improve our efforts to meet the rising demand and counter the evolving censorship landscape.

If you've ever considered running a Tor bridge, now is an excellent time to get started. Please help us spread the word as your help is urgently needed.

## I want to help, but I am not tech-savvy

No problem, you can help us spread the word. Now, more so than ever, it is important to speak up. Share this in your social networksâonline AND offline. If enough people read this, we can reach those who can support with the technical aspects of this ask.

You can also make a [donation](https://donate.torproject.org) to the Tor Project. Right now, all donations are matched. That means when you donate $25, your donation will be matched by a generous donor, meaning Tor receives a total of $50. Every donation help...