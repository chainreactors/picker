---
title: I accidentally logged hundreds of thousands of phone calls to military bases
url: https://lina.sh/blog/hijacking-e164-arpa
source: Over Security
date: 2026-08-22
fetch_date: 2026-08-23T02:57:54.773601
---

# I accidentally logged hundreds of thousands of phone calls to military bases

![](https://vg09.met.vgwort.de/na/2a0774cfd693439a98cb0dc98424be9b)

[![Home icon](/assets/home.svg)
back home](/)
[![Back icon](/assets/arrow_left.svg)
back to blogs](/blogs/en)

# I accidentally logged hundreds of thousands of phone calls to military bases

How an expired nameserver let me take over e164.arpa zones for multiple territories, and why I probably should have checked my logs sooner.

2026-07-30

short: <https://lina.sh/-e164>

![I accidentally logged hundreds of thousands of phone calls to military bases](/assets/blog/e164/cover.png)

DNS hijacking is silly. I already took over different `.gov` and `.edu` domains in the past, but I just immediately
reported that and moved on.
This one is a little different though, it's about how I took over phone-network infrastructure domains (`e164.arpa`) of
entire territories, and accidentally logged hundreds of thousands of phone calls to military bases. But let's start at
the beginning.

## What is e164.arpa anyway?

ENUM (`e164.arpa`) was an idea from the early 2000s[1](#fn:rfc): take a phone number, reverse the digits, put dots between
them, and add `.e164.arpa` at the end, so `+49 30 123456` becomes something like `6.5.4.3.2.1.0.3.9.4.e164.arpa`. You
can see that every German number will end up under `.9.4.e164.arpa`, which is the zone for all +49 numbers, and that
zone is controlled by DENIC (the same organization that runs `.de`). This means the DENIC decides which carrier or person
gets which number ranges under that zone, just like they hand out `.de` domains (which makes it decentralized, making every
country decide on delegation themselves).

The idea was that carriers could then look these domains up and get back a record saying "hey, this number can be
reached over SIP/VoIP under this address", skipping the expensive phone network and re-routing calls over the cheap
internet instead.

It never really took off though, and even back in its early days it saw barely any use. Over the years it just
deteriorated further, and today it's basically completely dead. I do actually own
[5.8.7.1.7.1.3.2.6.1.9.4.e164.arpa](https://5.8.7.1.7.1.3.2.6.1.9.4.e164.arpa) and
point it at this website, although technically I'm not supposed to do that (you can figure out my secondary number from
that!). Germany is actually one of the last countries that still technically allows registering an `e164.arpa` domain,
although I was the first person since 2019 to register one[2](#fn:denic-jahresbericht).

The RFC says you should only set NAPTR records on these domains, which are the records that tell carriers where to route a call.
It states that you *absolutely shouldn't* be using .arpa domains as normal "domains" and host stuff like websites on them,
they are meant to be "infrastructure" domains (you might know `in-addr.arpa` for reverse DNS lookups for example).
But there's nobody who can actually stop you from doing it, it's still just DNS at the end of the day,
and nothing prevents you from slapping an A record on there and hosting a website. Some people actually really dislike that,
and try to get Certificate Authorities to no longer issue certificates for `.arpa` domains[3](#fn:no-fun).

## Hijacking a territory's phone network

I was scanning `e164.arpa` to see if any of the delegated zones were hijackable, mostly out of curiosity about how
neglected this whole system really was.

I found three country-code zones, `0.9.2.e164.arpa`, `6.4.2.e164.arpa`, and `7.4.2.e164.arpa`, all delegated to the same
two nameservers: `ns6.icb.co.uk` and `ns.enum.org.uk`.

[![](/assets/blog/e164/dig-three-zones.png)](/assets/blog/e164/dig-three-zones.png)

Quick explainer for anyone who isn't a DNS person: when a domain is delegated to a nameserver, it basically means "for
any question about this domain, go ask this server, it has the answers", and if I control the nameserver a domain points
to, I control every DNS response for that domain.

`icb.co.uk` still exists as a domain, but the specific `ns6.icb.co.uk` subdomain no longer resolves to anything, meaning
any request falls back to the second listed nameserver instead: `ns.enum.org.uk`.

And that domain had expired, so I bought it for just 5€, and just like that I controlled the DNS for `0.9.2.e164.arpa`,
`6.4.2.e164.arpa`, and `7.4.2.e164.arpa`. Reversed, those are phone codes +290, +246, and +247: Saint Helena, the
British Indian Ocean Territory (Diego Garcia), and Ascension Island respectively (funnily enough, those
territories also have the popular ccTLDs `.sh`, `.io`, and `.ac`).

To be clear about what this meant: when a carrier does an ENUM lookup for one of these numbers, they're essentially
asking "where do I route this call?", and I could answer with whatever I wanted. I could point it at my own SIP server,
accept the incoming call, and then place an outgoing call to the real destination with a spoofed number.
The person being called would see the original number ringing, and after picking up would speak to the person on the
other end as if everything was normal, but I'd be sitting silently in the middle of the entire conversation.
I would theoretically be able to do this for every single request that I got if I could re-route a number, *if*
anyone was still actually using this system.

I reported it right away to everyone I could think of, through multiple channels into the British government, and got
nothing back. My best guess is that someone at the Internet Computer Bureau (who seemingly managed them in the past)
set these nameservers up over a decade ago. Then `e164.arpa` slowly died out, and whoever set it up either moved on or
just forgot about it, leaving nobody to renew a domain nobody remembered they depended on.

## Checking if anyone actually uses this

[Q Misell](https://magicalcodewit.ch/) (a researcher of the Max-Planck-Institute for Informatics) had heard about this and reported it to RIPE (who manages `e164.arpa`) on my behalf, but RIPE also declined to do anything, because
`e164.arpa` delegations are governed by an ITU-T committee at the UN level. And RIPE wasn't willing to go against a
decision made by a UN committee, which would probably be a bureaucratic nightmare.

Q also asked if I had any data on how much traffic these zones actually got, which I didn't know.
And because I was very curious about that myself, I set up logging on `0.9.2.e164.arpa` (Saint Helena) to find out, and waited a full day.

Not a single query came in. So after trying my best to get anyone to care and getting nowhere, I just kept the domains,
since nobody seemed to be relying on them anyway.

I hosted my [personal site](https://web.archive.org/web/20250925203323/https%3A//6.4.2.e164.arpa/) on it,
spun up [a Fediverse instance](https://archive.ph/o2dbx), a Matrix
homeserver, and handed out subdomains to friends, because why not, it's a dead system. It's not like it's gonna
hurt anyone, and no one cares. So it's time to be whimsical and have fun with it.

[![](/assets/blog/e164/fedi-instance.png)](/assets/blog/e164/fedi-instance.png)

## Six months later...

Just out of curiosity, I checked the logs again on all three zones,
since I enabled logging running on the other two as well when I set everything up.

Hundreds of thousands of ENUM queries, all logged[4](#fn:query-breakdown). Since the domain name is literally just the phone number reversed,
you can simply flip it back around to get the real number, so I had full phone numbers, timestamps, and the source IP
addresses of the DNS resolvers making the requests.

[![](/assets/blog/e164/log_screenshot.png)](/assets/blog/e164/log_screenshot.png)

Hundreds of thousands of lines in logs looking just like this (phone numbers are randomized)

Almost none of it was for Saint Helena (`0.9.2.e164.arpa`), it was basically almost entirely `6.4.2.e164.arpa` and
`7.4.2.e164.arpa`: Diego Garcia and Ascension Island. The source IPs were mostly American. That would at least explain
why I originally didn't see any traffic, as I was o...