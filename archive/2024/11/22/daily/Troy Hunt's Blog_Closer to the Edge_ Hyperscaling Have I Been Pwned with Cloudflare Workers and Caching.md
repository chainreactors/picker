---
title: Closer to the Edge: Hyperscaling Have I Been Pwned with Cloudflare Workers and Caching
url: https://www.troyhunt.com/closer-to-the-edge-hyperscaling-have-i-been-pwned-with-cloudflare-workers-and-caching/
source: Troy Hunt's Blog
date: 2024-11-22
fetch_date: 2025-10-06T19:20:02.014266
---

# Closer to the Edge: Hyperscaling Have I Been Pwned with Cloudflare Workers and Caching

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Closer to the Edge: Hyperscaling Have I Been Pwned with Cloudflare Workers and Caching

21 November 2024

I've spent more than a decade now [writing about how to make Have I Been Pwned (HIBP) fast](https://www.troyhunt.com/working-with-154-million-records-on/). *Really* fast. Fast to the extent that sometimes, it was even *too* fast:

> The response from each search was coming back so quickly that the user wasn’t sure if it was legitimately checking subsequent addresses they entered or if there was a glitch.

Over the years, the service has evolved to use emerging new techniques to not just make things fast, but make them scale more under load, increase availability and sometimes, even drive down cost. For example, 8 years ago now [I started rolling the most important services to Azure Functions, "serverless" code](https://www.troyhunt.com/azure-functions-in-practice/) that was no longer bound by logical machines and would just scale out to whatever volume of requests was thrown at it. And just last year, [I turned on Cloudflare cache reserve to ensure that all cachable objects *remained* cached](https://www.troyhunt.com/to-infinity-and-beyond-with-cloudflare-cache-reserve/), even under conditions where they previously would have been evicted.

And now, the pièce de résistance, the coolest performance thing we've done to date (and it is now "we", [thank you Stefán](https://www.troyhunt.com/have-i-been-pwned-employee-1-0-stefan-jokull-sigurdarson/)): just caching the whole lot at Cloudflare. Everything. Every search you do... almost. Let me explain, firstly by way of some background:

When you hit any of the services on HIBP, the first place the traffic goes from your browser is to one of [Cloudflare's 330 "edge nodes"](https://www.cloudflare.com/en-au/lp/ppc/overview-x/?ref=troyhunt.com):

![](https://www.troyhunt.com/content/images/2024/11/Artboard-1.png)

As I sit here writing this on the Gold Coast on Australia's most eastern seaboard, any request I make to HIBP hits that edge node on the far right of the Aussie continent which is just up the road in Brisbane. The capital city of our great state of Queensland is just a short jet ski away, about 80km as the crow flies. Before now, every single time I searched HIBP from home, my request bytes would travel up the wire to Brisbane and then take a giant 12,000km trip to Seattle where the Azure Function in the West US Azure data would query the database before sending the response 12,000km back west to Cloudflare's edge node, then the final 80km down to my Surfers Paradise home. But what if it didn't have to be that way? What if that data was already sitting on the Cloudflare edge node in Brisbane? And the one in Paris, and the one in well, I'm not even sure where all those blue dots are, but what if it was *everywhere?* Several awesome things would happen:

1. You'd get your response much faster as we've just shaved off more than 99% of the distance the bytes need to travel.
2. The availability would massively improve as there are far fewer nodes for the traffic to traverse through, plus when a response is cached, we're no longer dependent on the Azure Function or underlying storage mechanism.
3. We'd save on Azure Function execution costs, storage account hits and especially egress bandwidth ([which is *very* expensive](https://www.troyhunt.com/how-i-got-pwned-by-my-cloud-costs/)).

In short, pushing data and processing "closer to the edge" benefits both our customers and ourselves. But how do you do that for 5 *billion* unique email addresses? (Note: As of today, HIBP reports over 14 billion breached accounts, the number of unique email addresses is lower as on average, each breached address has appeared in multiple breaches.) To answer this question, let's recap on how the data is queried:

1. [Via the front page of the website](https://haveibeenpwned.com/?ref=troyhunt.com). This hits a "unified search" API which accepts an email address and [uses Cloudflare's Turnstile to prohibit automated requests not originating from the browser](https://www.troyhunt.com/fighting-api-bots-with-cloudflares-invisible-turnstile/).
2. [Via the public API](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#BreachesForAccount). This endpoint also takes an email address as input and then returns all breaches it appears in.
3. [Via the k-anonyity enterprise API](https://www.troyhunt.com/were-baking-have-i-been-pwned-into-firefox-and-1password/). This endpoint is used by a handful of large subscribers such as Mozilla and 1Password. Instead of searching by email address, it implements k-anonymity and searches by hash prefix.

Let's delve into that last point further because it's the secret sauce to how this whole caching model works. In order to provide subscribers of this service with complete anonymity over the email addresses being searched for, the only data passed to the API is the first six characters of the SHA-1 hash of the full email address. If this sounds odd, read the blog post linked to in that last bullet point for full details. The important thing for now, though, is that it means there are a total of 16^6 different possible requests that can be made to the API, which is just over 16 million. Further, we can transform the first two use cases above into k-anonymity searches on the server side as it simply involved hashing the email address and taking those first six characters.

In summary, this means we can boil the entire searchable database of email addresses down to the following:

1. AAAAAA
2. AAAAAB
3. AAAAAC
4. ...about 16 million other values...
5. FFFFFD
6. FFFFFE
7. FFFFFF

That's a large albeit finite list, and that's what we're now caching. So, here's what a search via email address looks like:

1. Address to search: test@example.com
2. Full SHA-1 hash: 567159D622FFBB50B11B0EFD307BE358624A26EE
3. Six char prefix: 567159
4. API endpoint: https://[host]/[path]/567159
5. If hash prefix is cached, retrieve result from there
6. If hash prefix is *not* cached, query origin and save to cache
7. Return result to client

K-anonymity searches obviously go straight to step four, skipping the first few steps as we already know the hash prefix. All of this happens in a Cloudflare worker, so it's "code on the edge" creating hashes, checking cache then retrieving from the origin where necessary. That code also takes care of handling parameters that transform queries, for example, [filtering by domain or truncating the response](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#BreachesForAccount). It's a beautiful, simple model that's all self-contained within a worker and a very simple origin API. But there's a catch - what happens when the data changes?

There are two events that can change cached data, one is simple and one is major:

1. Someone [opts out of public searchability](https://haveibeenpwned.com/OptOut?ref=troyhunt.com) and their email address needs to be removed. That's easy, we just call an API at Cloudflare and flush a single hash prefix.
2. A new data breach is loaded and there are changes to a large number of hash prefixes. In this scenario, we flush the entire cache and start populating it again from scratch.

The second point is kind of frustrating as we've built up this beautiful collection of data all sitting close to the consumer where it's super fast to query, and then we nuke it all and go from scratch. The problem is it's either that or we selectively purge what could be many millions of individual hash prefixes, [which you can't do](https://developers.cloudflare.com/api-next/resources/cache/?ref=troyhunt.com):

> For Zones on Enterprise plan, yo...