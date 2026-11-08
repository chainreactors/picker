---
title: unlocking any car from X brand in most of the world
url: https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/
source: shubs
date: 2026-11-07
fetch_date: 2026-11-08T08:14:26.416288
---

# unlocking any car from X brand in most of the world

[![shubs](https://shubs.io/content/images/2026/05/cropped-headshot-1.jpg)](https://shubs.io)

# [shubs](https://shubs.io)

Co-founder of Assetnote, security researcher.

###### [Assetnote](https://assetnote.io/)

###### [Home](https://shubs.io/)

###### [Github](https://github.com/infosec-au)

###### [Twitter](https://twitter.com/infosec_au)

###### [LinkedIn](https://www.linkedin.com/in/shubhamshah/)

# unlocking any car from X brand in most of the world

November 7 2026

I've always had a soft spot for this particular car brand. Our family has owned a few of them over the years, and they've served us incredibly well. In 2023, I bought a new four wheel drive/SUV from them, and it was the first time I had access to their connected car platform.

Having looked at platforms like this before ([previous works](https://samcurry.net/hacking-subaru?ref=shubs.io)), I was sceptical about how secure they really were. I suspected there was something there, but life kept getting in the way of actually looking. This July, I collaborated with Sam Curry to take a look at the security of a major automaker's connected car systems. Throughout this post, I'll refer to them simply as "the automaker".

When you typically think of car hacking, it's often easy to jump into the hardware side of things, but my background sits pretty squarely in compromising internet-facing web applications and infrastructure. Regardless of all the hardware bits and bobs, it all connects back to some service that, by design, has to be reachable from the internet.

The journey started with a simple question: what infrastructure does the app talk to when I remotely unlock my car? To work this out, I downloaded the APK and decompiled it, eventually reconstructing the API requests that were being made.

Going through the code, the primary point of contact seemed to be assets under `*.redacted-telematics.com.au`:

```
dartExecutor.executeDartEntrypoint(createDefault, CollectionsKt.r(gson.toJson(new GlobalConfigParams(false, g11, com.redacted.app.xcapp.a.f69866f, "X", str)), new Gson().toJson(new ApiConfig("https://api.redacted-telematics.com.au", "https://api.redacted-telematics.com.au", "https://api.redacted-telematics.com.au" ...
```

Almost every part of the consumer application called back to `redacted-telematics.com.au`. What else existed under this domain?

## The admin tool

Running connected car infrastructure can be quite complex, and managing it requires a mix of admin tools, staging, dev, and QA environments, to make sure that customers get a clean experience. Whether all of that should be sitting on the public internet, available to anyone willing to do some basic reconnaissance, is a different story.

One asset caught my attention more than the others. `admintool.redacted-telematics.com.au` returned a page titled TEST HARNESS. Who can resist a subdomain with admintool in it?

Visiting this subdomain presented a very plain and grey login screen, which didn't exactly ooze quality, given it presented a logout button before we'd logged in.

I love that most single-page applications ship their entire JavaScript bundle even when all they need to render is a login page. Sure, some more modern frameworks split out JavaScript files so that they only serve what is necessary, but in this case, we could comb through the large JavaScript bundle to understand what this "admin tool" actually let you do.

![](https://shubs.io/content/images/2026/11/CleanShot-2026-07-24-at-09.35.19@2x.png)

Oozing quality

![](https://shubs.io/content/images/2026/11/CleanShot-2026-11-07-at-17.10.32.png)

Who even reads JavaScript bundles?

Turns out this admin tool let you do quite a lot. It had a rich API that let the automaker's employees interact with customer accounts and production vehicles with very few restrictions. Reconstructing the requests, we found that a lot of these APIs needed no authentication beyond the hardcoded API keys sitting in the JavaScript bundle.

For example, we could look up user accounts by email address:

![](https://shubs.io/content/images/2026/11/CleanShot-2026-11-07-at-17.12.40.png)

But that's just not good enough. If we want to unlock any of their cars from just knowing the number plate, we're going to need to do better than that.

In Australia, a number plate gets you the VIN (vehicle identification number) fairly easily through state-based registration lookup sites.

This isn't really a security flaw. There are plenty of legitimate reasons to want a VIN, like checking a car's true repair and insurance history before buying second-hand. If we could go from VIN to a subscriber or email, we'd complete the chain.

Fortunately, there was an API that let you do exactly that:

With the subscriber GUID, you could pull the full account details (including the user's email via the `/v1/account` endpoint) like so:

![](https://shubs.io/content/images/2026/11/CleanShot-2026-11-08-at-08.32.13.png)

Well, I guess we have the first part of our chain sorted. Plate -> VIN -> Subscriber GUID -> User Account PII (email) registered on the automaker's identity platform (ForgeRock OpenIDM).

Now, how do we send commands to any car we want? Surely this admin tool would let us do that? Unfortunately, no. It let us provision features to a car, add ourselves to a user's account as a secondary user, and even generate remote access codes. But for all that functionality, none of it actually got us remote control of a vehicle.

## The identity platform

Sam and I then spent two weeks digging into how the automaker manages their central identity system: the software they use, the way commands are issued, and how consumers authenticate.

When a user goes through the authentication flow for the automaker's mobile app, requests are made to `login.redacted-identity.com.au`, and after going through an MFA flow, a consumer auth token is finally issued. This auth token is then used for subsequent requests to `api.redacted-telematics.com.au` (both REST APIs and GraphQL). Once you have that auth token, it's pretty much game over. You can control a user's car (remote unlock/lock, horns, engine, etc).

So if we could mint a token for any user, we'd finally be able to control anyone's connected car. This is the angle we went for.

The automaker is a heavy user of ForgeRock's identity software (OpenAM/OpenIDM). This is the cornerstone of their authentication mechanisms. Pulling the subdomains for `*.redacted-identity.com.au`, we quickly found their OpenIDM instance at `openidm.redacted-identity.com.au`. This is the system that manages every identity registered on the automaker's connected car platform.

This all clicked together when we were combing through the JavaScript files under `*.redacted-telematics.com.au` and we came across an absolutely cursed vendor JavaScript bundle that embedded admin credentials for OpenIDM 😱:

![](https://shubs.io/content/images/2026/11/CleanShot-2026-11-07-at-17.15.20.png)

Even though these admin credentials were meant to be for their staging environment, given the hygiene we'd seen so far, we were pretty sure they'd work in production too.

## Fighting the WAF

Looking closer at OpenIDM, we couldn't tell whether the automaker knew how fragile it was. One thing was obvious though: they'd invested heavily in WAF rules to block access to the sensitive APIs that ForgeRock typically lets you call via `/openidm/*`.

![](https://shubs.io/content/images/2026/11/CleanShot-2026-11-07-at-19.32.01.png)

Even with the origin IP, any request to `/openidm/` came straight back as an Nginx WAF block. Someone had put real effort into hardening these assets (despite them being externally accessible).

Fair enough, and we respect the hardening. But that much WAF investment usually means bandaids over something known to be bad. They probably understood how bad it was to have this asset exposed at all, and some business case kept it there anyway.

I'm not sure a WAF rule has ever stopped us when we're motivated...