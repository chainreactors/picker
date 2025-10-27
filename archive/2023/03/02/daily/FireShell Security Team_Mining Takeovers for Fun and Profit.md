---
title: Mining Takeovers for Fun and Profit
url: https://fireshellsecurity.team/mining-takeovers-for-fun-and-profit/
source: FireShell Security Team
date: 2023-03-02
fetch_date: 2025-10-04T08:26:50.803816
---

# Mining Takeovers for Fun and Profit

[![](/assets/images/title.gif)](/)

* [Home](/)
* [Team](/team/)
* [Articles](/articles/)
* [Portfolio](/portfolio/)
* [Sponsors](/sponsors/)
* [About](/about/)
* Toggle theme
  + Light
  + Dark
  + Auto

Wednesday, March 1, 2023

# Mining Takeovers for Fun and Profit

by [Marzano "Macmod"](/macmod/)

Mining Takeovers for Fun and Profit

![Diamonds.png](https://i.imgur.com/3gtnDYk.png)

## Introduction

This article describes an experiment aimed at finding domains likely vulnerable to *DNS takeover*, a well-known technique that can be used to steal decomissioned, but active domains. In this experiment I will show how I was able to find with little effort more than 200 domains that could be theoretically taken over across different providers and parent domains by using data from a public search tool ([SecurityTrails](securitytrails.com)) and an open-source repository ([can-i-take-over-dns](https://github.com/indianajson/can-i-take-over-dns)).

*Please note that I did not find any new vulnerabilities nor develop any sort of attack tools or techniques during this research*. I just analyzed what was already there, not being responsible in any way for whatever damages could be caused by the usage of the methods described below.

## Background

A *Subdomain takeover* is a vulnerability that happens when there is a CNAME record pointing a domain `app.site.com` to a domain `name.b.com`, in which domain `b.com` belongs to a third-party platform that allows their customers to choose subdomains of their `b.com` zone for usage with their services.

For example, let’s imagine we are the current owners of `site.com` working with a provider named `host.net`. We decide to use a managed application service from `host.net` named `service` to host our app `myapp`. After configuring the service in `host.net`, it gives us a subdomain in their `service.host.net` zone hosting our app - let’s say `myapp.service.host.net`. We’d like to access our app through our domain, not theirs, so we create a CNAME in the `site.com` zone pointing `app.site.com` to `myapp.service.host.net`.

Later on we decide to remove our app from `host.net`, releasing the domain name in their zone. If we don’t remember to remove the CNAME (we won’t), another customer of `host.net` can come in and set up their own app named `myapp` in the managed app service. They would be able to host any content they wanted under our `app.site.com` subdomain, effectively taking over it.

![SubdomainTakeover.gif](https://i.imgur.com/Pw7OE5u.gif)

A *DNS takeover* is a similar vulnerability, but instead of allowing an attacker to hijack the contents that users see when they access one of your subdomains, it allows attackers to gain control over an entire zone, being able to create any records they want to. It happens when an entity registers a domain in their registrar, delegates administration of the domain to another more convenient provider, and in the future deletes the domain in that provider. Since the delegation is still in the registrar, an attacker can create an account in the provider and recreate the domain.

For example, suppose we are a loyal customer of the `cloud.net` provider. We just bought `bigcorp.com` for the next year from GoDaddy (our preferred registrar), but we actually want to manage the `bigcorp.com` zone using our `cloud.net` provider and not GoDaddy. Next we would have to create a zone for `site.com` in our `cloud.net` provider, and then access GoDaddy and create an `NS` record delegating the `bigcorp.com` site to the nameservers of `cloud.net`, which could be `ns1.cloud.net` and `ns2.cloud.net`.

Suppose we get tired of `bigcorp.com` and decide to use `bigcorp.io` instead. We would keep paying for `bigcorp.com` for the following years, since we don’t want to lose the name. Then at some point someone would remove the `bigcorp.com` zone from the `cloud.net` portal, thinking it has no business being there if it’s not in use, thus creating what is called a **lame delegation** - when a domain points to nameservers that don’t actually respond authoritatively to queries for that domain. If an attacker realizes that `bigcorp.com` has a lame delegation to `cloud.net` nameservers, this person could create an account in our provider and recreate `bigcorp.com`, being able to create all sorts of records there. For instance, they would be able to create subdomains of `bigcorp.com` for phishing purposes, or create an `MX` record to intercept all emails directed to `bigcorp.com`.

![DNSTakeover.gif](https://i.imgur.com/3zitvvi.gif)

In case you want to learn more before going further, [Patrik Hudak’s blog](https://0xpatrik.com/) has some pretty good educational articles describing these attacks, including other ways to find candidates for takeover with subdomain enumeration techniques, and how to develop other attacks after a subdomain takeover is exploited.

## The Problem & The Plan

I wanted to know what could be done to better understand, and possibly help mitigate risks of DNS takeovers in the internet. Of course it’s an unreasonable goal, but one can dream, right? The first question that I wanted to answer was whether we could come up with a simple and effective way to find domains that were likely vulnerable to DNS takeover.

The problem is that no one really knows which records exist in a registrar apart from the registrar itself, since it owns the zonefiles. One could find a huge list of random domains somewhere and scan them for possible DNS takeover scenarios, but this is too time-consuming and in most cases unlikely to yield good results. To find possible scenarios we need a way to dump a list of domains that delegate their zones to nameservers of vulnerable providers.

At this point I was just thinking, but then I was casually talking to my friend Kali Nathalie about pentesting the other day, and she mentioned that *SecurityTrails* had a subdomain search tool with a pretty good database, so I browsed to it and found that, not only does it have a great database, but it also provides *reverse NS* and *reverse CNAME* lookups, our missing piece of the puzzle. That’s something you don’t find very often, since the DNS protocol does not specify these sorts of lookups - there’s no reason why it should, really.

Now the plan was:

![Plan.png](https://i.imgur.com/vHpro0k.png)

First I extracted all nameservers of the vulnerable providers from indianajson’s [can-i-take-over-dns](https://github.com/indianajson/can-i-take-over-dns) repository. His repository currently documents the state of 28 providers regarding DNS takeover, 19 of which are currently listed as “Vulnerable” or “Edge Case”. Besides the “Not Vulnerable” nameservers, all CloudFlare nameservers were ignored for this step, since a successful attack is unlikely due to their high number of nameservers.

I had a list of 379 nameservers from 18 providers to search:

| **Provider** | **# of nameservers evaluated** |
| --- | --- |
| Azure | 228 |
| NS1 | 72 |
| Google Cloud | 28 |
| DNSMadeEasy | 7 |
| Hurricane Electric | 5 |
| DNSimple | 4 |
| Dotster | 4 |
| EasyDNS | 4 |
| 000Domains | 4 |
| Bizland | 4 |
| Name.com | 4 |
| Digital Ocean | 3 |
| Domain.com | 2 |
| TierraNet | 2 |
| Reg.ru | 2 |
| Yahoo Small Business | 2 |
| Linode | 2 |
| MyDomain | 2 |

For the top 3 providers in the table I just guessed their nameservers by trial and error since they weren’t explicited in indianajson’s repository, so the real number could be more or less than what I found.

Also note that, in most cases, many nameservers in the same provider will serve records from the same zonefiles, some acting as backups in case others fail. That should not stop us from analyzing them though, since some domains might not appear in the database as being associated with all nameservers of their provider. As long as we have the time to do so, the chances are we will be getting more domains this way.

I decided to try one of the Azure nameservers manually, going through the p...