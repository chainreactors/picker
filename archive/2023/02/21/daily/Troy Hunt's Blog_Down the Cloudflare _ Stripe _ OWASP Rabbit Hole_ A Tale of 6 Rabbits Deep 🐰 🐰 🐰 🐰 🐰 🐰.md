---
title: Down the Cloudflare / Stripe / OWASP Rabbit Hole: A Tale of 6 Rabbits Deep 🐰 🐰 🐰 🐰 🐰 🐰
url: https://www.troyhunt.com/down-the-cloudflare-stripe-owasp-rabbit-hole-a-tale-of-6-rabbits-deep/
source: Troy Hunt's Blog
date: 2023-02-21
fetch_date: 2025-10-04T07:39:19.085404
---

# Down the Cloudflare / Stripe / OWASP Rabbit Hole: A Tale of 6 Rabbits Deep 🐰 🐰 🐰 🐰 🐰 🐰

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Down the Cloudflare / Stripe / OWASP Rabbit Hole: A Tale of 6 Rabbits Deep 🐰 🐰 🐰 🐰 🐰 🐰

20 February 2023

I found myself going down a previously unexplored rabbit hole recently, or more specifically, what I thought was "a" rabbit hole but in actual fact was an ever-expanding series of them that led me to what I refer to in the title of this post as "6 rabbits deep". It's a tale of firewalls, APIs and sifting through layers and layers of different services to sniff out the root cause of something that seemed very benign, but actually turned out to be highly impactful. Let's go find the rabbits!

### The Back Story

When you [buy an API key on Have I Been Pwned](https://haveibeenpwned.com/API/Key?ref=troyhunt.com) (HIBP), Stripe handles all the payment magic. I *love* Stripe, it's such an awesome service that abstracts away so much pain and it's dead simple to integrate via their various APIs. It's also dead simple to [configure Stripe to send notices back to your own service via webhooks](https://stripe.com/docs/webhooks?ref=troyhunt.com). For example, when an invoice is paid or a customer is updated, Stripe sends information about that event to HIBP and then lists each call on the webhooks dashboard in their portal:

![](https://www.troyhunt.com/content/images/2023/01/image-7.png)

There are a whole range of different events that can be listened to and webhooks fired, here we're seeing just a couple of them that are self explanatory in name. When an invoice is paid, the callback looks something like this:

![](https://www.troyhunt.com/content/images/2023/01/image-9.png)

HIBP has received this call and updated it's own DB such that for a new customer, they can now retrieve an API key or for an existing customer whose subscription has renewed, the API key validity period has been extended. The same callback is also issued when someone upgrades an API key, for example when going from 10RPM (requests per minute) to 50RPM. It's super important that HIBP gets that callback so it can appropriately upgrade the customer's key and they can immediately begin making more requests. When that call doesn't happen, well, let's go down the first rabbit hole.

### The Failed API Key Upgrade 🐰

This should never happen:

![](https://www.troyhunt.com/content/images/2023/01/image-10.png)

This came in via [HIBP's API key support portal](https://support.haveibeenpwned.com/?ref=troyhunt.com) and is pretty self-explanatory. I checked the customer's account on Stripe and it did indeed show an active 50RPM subscription, but when drilling down into the associated payment, I found the following:

![](https://www.troyhunt.com/content/images/2023/02/image-11.png)

Ok, so at least I know where things have started to go wrong, but why? Over to the webhooks dashboard and into the failed payments and things look... suboptimal:

![](https://www.troyhunt.com/content/images/2023/01/image-12.png)

Dammit! Fortunately this is only a small single-digit percentage of all callbacks, but every time this fails it's either stopping someone like the guy above from making the requests they've paid for or potentially, causing someone's API key to expire even though they've paid for it. The latter in particular I was really worried about as it would nuke their key and whatever they'd built on top of it would cease to function. Fortunately, because that's such an impactful action I'd built in heaps of buffer for just such an occurrence and I'd gotten onto this issue quickly, but it was disconcerting all the same.

So, what's happening? Well, the response is HTTP 403 "Forbidden" and the body is clearly a Cloudflare challenge page so something at their end is being triggered. Looks like it's time to go down the next rabbit hole.

### Cloudflare's Firewall and Logs 🐰 🐰

Desperate just to quickly restore functionality, I dropped into Cloudflare's WAF and allowed [all Stripe's outbound IPs used for webhooks](https://stripe.com/docs/ips?ref=troyhunt.com#webhook-notifications) to bypass their security controls:

![](https://www.troyhunt.com/content/images/2023/01/image-13.png)

This wasn't ideal, but it only created risk for requests originating from Stripe and it got things up and running again quickly. With time up my sleeve I could now delve deeper and work out precisely what was going on, starting with the logs. Cloudflare has a really extensive set of APIs that can control a heap of features of the service, including [pulling back logs](https://developers.cloudflare.com/api/operations/logs-received-get-logs-received?ref=troyhunt.com) (note: this is a feature of their Enterprise plan). I queried out a slice of the logs corresponding to when some of the 403s from Stripe's dashboard occurred and found 2 entries similar to this one:

```
{"BotScore":1,"BotScoreSrc":"Verified Bot","CacheCacheStatus":"unknown","ClientASN":16509,"ClientCountry":"us","ClientIP":"54.187.205.235","ClientRequestHost":"haveibeenpwned.com","ClientRequestMethod":"POST","ClientRequestReferer":"","ClientRequestURI":"[redacted]","ClientRequestUserAgent":"Stripe/1.0 (+https://stripe.com/docs/webhooks)","EdgeRateLimitAction":"","EdgeResponseStatus":403,"EdgeStartTimestamp":1674073983931000000,"FirewallMatchesActions":["managedChallenge"],"FirewallMatchesRuleIDs":["6179ae15870a4bb7b2d480d4843b323c"],"FirewallMatchesSources":["firewallManaged"],"OriginResponseStatus":0,"WAFAction":"unknown","WorkerSubrequest":false}
```

That's one of Stripe's outbound IP's on 54.187.205.235 and the "FirewallMatchesRuleIDs" collection has a value in it. Ergo, something about this request triggered the firewall and caused it to be challenged. I'm sure many of us have gone through the following thought process before:

What did I change?

Did I change *anything?*

Did *they* change something?

Except "they" could have been either Cloudflare or Stripe; if it wasn't me (and I was fairly certain it wasn't), was it a Cloudflare change to the rules or a Stripe change to a webhook payload that was now triggering an existing rule? Time to dig deeper again so it's over to the Cloudflare dashboard and down into the WAF events for requests to the webhook callback path:

![](https://www.troyhunt.com/content/images/2023/01/image-28.png)

Yep, something proper broke! Let's drill deeper and look at recent events for that IP:

![](https://www.troyhunt.com/content/images/2023/01/image-16.png)

As you dig deeper through troubleshooting exercises like this, you gradually turn up more and more information that helps piece the entire puzzle together. In this case, it looks like the "Inbound Anomaly Score Exceeded" rule was being triggered. What's that? And why? Time to go down another rabbit hole.

### The Cloudflare OWASP Core Ruleset 🐰 🐰 🐰

So, deeper and deeper down the rabbit holes we go, this time into the depths of the requests that triggered the managed rule:

![](https://www.troyhunt.com/content/images/2023/01/image-18.png)

Well that's comprehensive 🙂

There's a lot to unpack here so let's begin with the ruleset that the previously identified "Inbound Anomaly Score Exceeded" rule belongs to, [the Cloudflare OWASP Core Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/?ref=troyhunt.com):

> The Cloudflare OWASP Core Ruleset is Cloudflare’s implementation of the OWASP ModSecurity Core Rule SetOpen external link (CRS). Cloudflare routinely monitors for updates from OWASP based on the latest version available from the official code repository.

That link is yet another rabbit hole altogether so let me summarise succinctly here: Cloudflare uses OWASP's rules to identify anomalous traffic based o...