---
title: HIBP Mega Update: Passkeys, k-Anonymity Searches, Massive Speed Enhancements and a Bulk Domain Verification API
url: https://www.troyhunt.com/passkeys-k-anonymity-searches-massive-speed-enhancements-bulk-domain-verification-api/
source: Troy Hunt's Blog
date: 2026-03-30
fetch_date: 2026-03-31T04:37:34.448110
---

# HIBP Mega Update: Passkeys, k-Anonymity Searches, Massive Speed Enhancements and a Bulk Domain Verification API

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# HIBP Mega Update: Passkeys, k-Anonymity Searches, Massive Speed Enhancements and a Bulk Domain Verification API

31 March 2026

For a hobby project built in my spare time to provide a simple community service, Have I Been Pwned sure has, well, "escalated". Today, we support hundreds of thousands of website visitors each day, tens of millions of API queries, and *hundreds of millions* of password searches. We're processing billions of compromised records each year provided by breached companies, white hat researchers, hackers and law enforcement agencies. And it's used by every conceivable demographic: infosec pros, "mums and dads", customer support services, and, according to the data, more than half the Fortune 500 who are actively monitoring the exposure of their domains. So yeah, "escalated" seems fair!

Amidst all the time spent processing data, we've been trying to figure out where to invest energy in building new stuff. In essence, data breaches are pretty simple: you've got a bunch of exposed email addresses attributed to a source, sitting next to a whole bunch of fields we describe with metadata. Our goal has always been to help people use this data to do good after bad things happen, and today we're launching a bunch of new features to do just that. So, here goes:

## New Features, New Plans

In the beginning (ok, in "recent years"), there was one plan we referred to as "Pwned", and within that, there were various levels. For example, the entry-level plan has been "Pwned 1," and to this day, more than half our subscriptions are on it. That's "a coffee a month" for a simple service that, by the raw numbers, does precisely what most of our subscribers are looking for. These are typically small businesses that make a handful of API queries or monitor a domain or two with a few email addresses. It's simple, effective and... insufficient for larger organisations. So, we added Pwned 2, 3 and 4, and they all added more RPMs for email searches and more capacity for searching larger domains. Then we added Pwned 5, which added stealer log support, and somewhere along the way also added Pwned Ultra tiers for making large numbers of API requests. As a result, that one "plan" added more and more stuff at different levels and ultimately became a bit kludgy.

Today, we're launching a bunch of new features to better support the volume and privacy needs of our subscribers, and we're shuffling our existing plans to help do this. Here's what they now look like:

1. **Core:** The fundamentals, largely being what we already had and designed for entry-level use cases
2. **Pro:** Contains a bunch of the new features designed for larger orgs and those searching domains on behalf of customers
3. **High RPM:** The old "Ultra" plan levels, designed solely for making large volumes of requests to the email search API
4. **Enterprise:** We've had this for many years now, and it's a more tailored offering

So, that's the high-level overview. Let's now look at all the new stuff and everything that changes:

## Supporting MSPs Monitoring on Behalf of Third Parties

For most people, this won't sound particularly exciting, but I'm putting it up front because I'll refer to it when describing the more important stuff shortly. In the past, we've had the following carve-out in our terms of use, namely, what you're *not* permitted to use the service for:

> the benefit of a third party (including for use by a related entity or for the purpose of reselling or otherwise making the Services available to any third party for commercial benefit)

This excluded managed service providers from, for example, monitoring their customers' domains as part of their services. That clause has now been revised with the preceding text:

> unless you have purchased a Paid Service which expressly allows you to do so

Which means we can now welcome MSPs to the Pro and High RPM tiers. They can't just take HIBP and use it to create a competing product (for obvious reasons, that's a pretty standard clause within many online services), but they can absolutely add it to the offerings they provide to their own customers. *And* we're adding new features to make it easier to do just that, for example:

## Automating Domain Verification

Preserving privacy whilst still providing a practical, effective service has always been a balancing act, one I think we've gotten pretty spot on. But the hoops people have had to jump through for domain verification, in particular, have been cumbersome. An organisation wanting to add a bunch of its domains has had to go through the process one by one via the web interface, then verify control over them one by one. They'd spend *a lot* of time doing kludgy, repetitive work. Today, we're launching two new ways of adding domains in a much more automated fashion, and the first is the **verifying via DNS API**:

Successfully adding a pre-defined TXT record to DNS is solid proof that whoever is attempting to search that domain genuinely controls it. As well as the old kludgy way of doing it in the browser, waiting for DNS to propagate, then coming back to the browser to complete the verification, we can now fully automate the process via API. Here's how it works:

1. Call the HIBP API to generate the TXT record token
2. Call the API on your DNS provider to add the token to the TXT record
3. Call another HIBP API to validate that the token exists

This is easily scripted in your language of choice, and you can enumerate it over as many domains as you like. You can also keep retrying step 3 above as often as needed when DNS takes a little while to do its thing. [It's all now fully documented in the latest version of the API](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#VerifyDomainViaDns), and ready to roll. But what if you don't control the DNS? Perhaps it's a cumbersome process in your org, or you're an MSP monitoring your customers' domains, but you don't have control of DNS. That's where the **verifying by email API comes in:**

We've long had a verification process that involves choosing one of several standard aliases on a domain to email a verification token to. You do this via the dashboard, grab the token sent to the email, paste it back into the dashboard and the domain is now verified. The new API makes that much easier, especially when multiple domains are being verified. Here's how it works:

1. Call the HIBP API and specify one of the pre-defined aliases to send a verification email to
2. Click the link in the email and approve the domain to be added to the requester's account

And that's it. We see this being particularly useful for MSPs who can now send a heap of emails on their customers' domains, and so long as someone receives it and clicks the link, that's the verification process done. [That API is also now fully documented and ready to roll](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#VerifyDomainViaEmail) and is accessible to all Pro plan subscribers.

## Auto-verifying Subdomains

This one was just unnecessarily frustrating for larger customers who spread email addresses over multiple subdomains. Let's say a company owns example.com and they successfully verify control of it, but then they distribute their email addresses by region. They end up with addresses @apac.example.com and @emea.example.com and so on, and in the past, needed to verify each subdomain separately.

Turns out [we have 154 votes for this feature in User Voice](https://haveibeenpwned.uservoice.com/forums/275398-general/suggestions/9421500-allow-root-domain-to-verify-subdomains?ref=troyhunt.com), which is substantially more than I expected. So...