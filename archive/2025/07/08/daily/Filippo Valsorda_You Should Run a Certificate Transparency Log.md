---
title: You Should Run a Certificate Transparency Log
url: https://words.filippo.io/run-sunlight/
source: Filippo Valsorda
date: 2025-07-08
fetch_date: 2025-10-06T23:17:48.588222
---

# You Should Run a Certificate Transparency Log

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

7 Jul 2025

# You Should Run a Certificate Transparency Log

Hear me out. If you are an organization with some spare storage and bandwidth, or an engineer looking to justify an [overprovisioned homelab](https://bsky.app/profile/filippo.abyssdomain.expert/post/3l7os3ds64c2d), you should consider running a Certificate Transparency log. It’s cheaper, easier, and more important than you might think.

[Certificate Transparency](https://certificate.transparency.dev/) (CT) is one of the technologies that underpin the security of the whole web. It keeps Certificate Authorities honest, and allows website owners to be notified of unauthorized certificate issuance. It’s a big part of how the WebPKI went from the punchline of “weakest link” jokes to the robust foundation of the security of most of digital life… in less than fifteen years!

CT is an intrinsically distributed system: CAs must submit each certificate to two CT logs operated by third parties and trusted by the browsers. This list is, and has been for a couple years, uncomfortably short. There just aren’t as many independent log operators as we’d like. Operating a log right now would be an immense contribution to the security of virtually every Internet user.

It also comes with the bragging rights to claim that your public key is on *billions* of devices.

Where’s the catch? Well, until recently running a log was a pain, and expensive. I am writing this because as of a few months ago, **this has changed**!

![The Sunlight logo, a bench under a tree in stylized black ink, cast against a large yellow sun, with the text Sunlight underneath](https://assets.buttondown.email/images/ac85a5bf-0a04-4d05-b006-7d1751d49de8.png)

Browsers now accept CT logs that implement the new [Static CT API](https://c2sp.org/static-ct-api), which I designed and productionized in collaboration with Let’s Encrypt and the rest of the WebPKI community over the past year and a half. The key difference is that it makes it possible to serve the read path of a CT log exclusively through static, S3 and CDN friendly files.

Moreover, the new [Sunlight](https://github.com/FiloSottile/sunlight) implementation, sponsored by Let’s Encrypt, implements the write path with minimal dependencies and requirements. It can upload the Static CT assets directly to object storage, or store them on any POSIX filesystem.

You can learn more if you are curious in [Let’s Encrypt’s retrospective](https://letsencrypt.org/2025/06/11/reflections-on-a-year-of-sunlight/), in the original [Sunlight design document](https://filippo.io/a-different-CT-log), or in the summarized [public announcement](https://groups.google.com/a/chromium.org/g/ct-policy/c/v9JzlbphYBs/m/kyQk4ZP6AAAJ).

[Geomys](https://geomys.org), my open source maintenance firm, [operates a pro-bono Sunlight-backed trusted Static CT log for $10k/year](https://groups.google.com/a/chromium.org/g/ct-policy/c/KCzYEIIZSxg/m/zD26fYw4AgAJ), including hardware amortization, colocation, and bandwidth. I’m sure it can be done for cheaper.

## The shopping list

Ok, so what does it take to run a CT log in 2025[6](#fn:grow)?

* Servers: one. No need to make the log a distributed system, CT itself is a distributed system.
  + If you want to offer redundancy you can run multiple logs.
  + The uptime target is 99%[5](#fn:five) over three months, which allows for nearly 22h of downtime. That’s more than three [motherboard failures](https://groups.google.com/a/chromium.org/g/ct-policy/c/P1rR_tVHR2Y/m/hqU59xExAwAJ) per month.
* CPU and memory: whatever, **as long as it’s [ECC](https://groups.google.com/a/chromium.org/g/ct-policy/c/S17_j-WJ6dI/m/Fi-FonxUAwAJ) [memory](https://groups.google.com/a/chromium.org/g/ct-policy/c/PCkKU357M2Q/m/xbxgEXWbAQAJ)**. Four cores and 2 GB will do.
* Bandwidth: 2 Gbps outbound peak capacity[2](#fn:bw) (which you can offload to a CDN).
* Storage: you have two options.

  1. 3 – 5 TB[1](#fn:range) of usable redundant filesystem space on SSDs[3](#fn:ssd).
  2. 3 – 5 TB[1](#fn:range) of S3-compatible object storage, and 200 GB of cache on SSD.

  Static CT logs are just flat static files, which you can serve with any HTTP server[4](#fn:skylight) from disk, or expose as a public object storage bucket.

* People: Google policy requires the email addresses of two representatives. The uptime target is forgiving enough that it can probably be met by a single person working during business hours.

That’s pretty much it!

Durability is the first priority: it’s really important that you never lose data once it’s fsync’ed to disk or PUT to object storage, since your log will have signed and returned SCTs, which are promises to serve the certificates it received. This means for example that backups are useless: they would rollback the log’s state.

In terms of ongoing effort, a log operator is expected to read the [Google](https://googlechrome.github.io/CertificateTransparency/log_policy.html) and [Apple](https://support.apple.com/en-us/103703) CT Log policies, monitor the ct-policy@chromium.org mailing list, update the log implementation from time to time, and rotate log temporal shards every year. (For example, we just stood up 2027 shards of our log.)

Given the logs lifecycle, you should plan to stick around for at least three years.

## Sign me up!

If you want to become a CT log operator, first of all… thank you!

The [Sunlight README](https://github.com/FiloSottile/sunlight?tab=readme-ov-file) was rewritten recently to get you up and running easily. Sunlight is highly specialized for Certificate Transparency and the WebPKI, and it’s designed to help you operate a healthy, useful CT log with minimal configuration.

The community is eager to welcome new log operators. You can post questions, reports, and updates on the [transparency.dev Slack](https://transparency.dev/slack/), [ct-policy mailing list](https://groups.google.com/a/chromium.org/g/ct-policy), or [Sunlight issue tracker](https://github.com/FiloSottile/sunlight/issues). I encourage you to reach out even just to share your plans, or to ask any questions you might have before committing to running a log.

You might also want to follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo).

## The picture

I *systematically* make the mistake of reaching a beautiful spot with my motorcycle, watching the sunset, and *then* realizing “oh, shoot, now it’s dark!” This time, the motorcycle didn’t start, too, and it was the first ride of the season in January. Got to read [A Tour of WebAuthn](https://www.imperialviolet.org/tourofwebauthn/tourofwebauthn.html) by Adam Langley, though, so who can say if it was good or bad.

![An e-ink tablet rests on a wooden table in the foreground, with a motorcycle parked on a roadside in the background along a mountain road against a beautiful sunset with haze and scattered clouds.](https://assets.buttondown.email/images/13d84ddb-41d1-484e-a4a6-cee51054c99e.jpeg?w=960&fit=max)

[Geomys](https://geomys.org), my Go open source maintenance organization, is funded by [Smallstep](https://smallstep.com/), [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [Tailscale](https://tailscale.com/), and [Sentry](https://sentry.io/). Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)

Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social e...