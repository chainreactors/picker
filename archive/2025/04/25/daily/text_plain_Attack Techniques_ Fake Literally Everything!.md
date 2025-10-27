---
title: Attack Techniques: Fake Literally Everything!
url: https://textslashplain.com/2025/04/24/attack-techniques-fake-literally-everything/
source: text/plain
date: 2025-04-25
fetch_date: 2025-10-06T22:05:48.124900
---

# Attack Techniques: Fake Literally Everything!

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: Fake Literally Everything! (Escrow Scam)

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-04-242025-09-12](https://textslashplain.com/2025/04/24/attack-techniques-fake-literally-everything/)Posted in[security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/), [web](https://textslashplain.com/category/tech/web/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [OSINT](https://textslashplain.com/tag/osint/), [scam](https://textslashplain.com/tag/scam/), [SmartScreen](https://textslashplain.com/tag/smartscreen/)

The team recently got a false-negative report on the SmartScreen phishing filter complaining that we fail to block `firstline-trucking.com`. I passed it along to [our graders](https://textslashplain.com/2023/01/19/defense-techniques-reporting-phish/#:~:text=sent%20to%20a%20human%20grader) but then took a closer look myself. I figured that maybe the legit site was probably at a very similar domain name, e.g. `firstlinetrucking.com` or something, but no such site exists.

*Curious.*

### Simple Investigation Techniques

I popped open the [Netcraft Extension](https://chromewebstore.google.com/detail/netcraft-extension/bmejphbfclcpmpohkggcjeibfilpamia) and immediately noticed a few things. First, the site is a **new site**. Suspicious, since they claim to have been around since 2002. Next, the site is apparently hosted in the UK, although they brag about being “*Strategically located at the U.S.-Canada border*.” *[Sus](https://www.urbandictionary.com/define.php?term=sus).*.. and just above that, they supply an address in Texas. *Sus*.

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-43.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/04/image-43.png)

Let’s take a look at that [address in Google Maps](https://www.google.com/maps/place/225%2BGarza%2BAve%2C%2BWeslaco%2C%2BTX%2B78596/%4026.1605978%2C-97.9888598%2C17z/data%3D%213m1%214b1%214m6%213m5%211s0x866577a36140f4fb%3A0x2de3df68f18cb126%218m2%213d26.160593%214d-97.9862795%2116s/g/11c0_r_hn9?entry=ttu&g_ep=EgoyMDI1MDQyMi4wIKXMDSoJLDEwMjExNDUzSAFQAw%3D%3D). Hmm. A non-descript warehouse with no signage. *Sus.*

Well, let’s see what else we have. Let’s go to the “About Us” page and see who claims to be employed here. Right-click the CEO’s picture and choose “Copy image link.”

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-44.png?w=531)](https://textslashplain.com/wp-content/uploads/2025/04/image-44.png)

Paste that URL into [TinEye to see where else that picture appears](https://tineye.com/search/ee0fa9f33a36be26c07646bb6ed72c60437bb27e?sort=score&order=desc&page=1) on the web. Ah, it’s from a stock photo site. *Very sus*.

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-45.png?w=905)](https://textslashplain.com/wp-content/uploads/2025/04/image-45.png)

Investigating the other employee photos and customer pictures from the “Customer testimonials” section reveals that most of them are also from stock photo sites. The unfortunately-named “Marry Hoe” has her picture on [several other “About us” pages](https://tineye.com/search/d9dd275d8cf8c05816e637374b88c9040016aff1?sort=score&order=desc&page=1) — it looks like she probably came with the template. Her profile page is all [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) placeholder text.

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-61.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/04/image-61.png)

I was surprised that one of the biggest photos on the site didn’t show up in TinEye at all. Then I looked at the Developer Tools and noticed that the secret is revealed by the image’s filename — `ai-generated-business-woman-portrait`. *Ah, that’ll do it.*

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-46.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/04/image-46.png)

I tried searching for the phone number atop the site (`(956) 253-7799`) but there were basically no hits on Google. This is both *very sus* and very surprising, because often Googling for a phone number will turn up many complaints about scams run from that number.

### Moar Scams!

Hmm…. what about all of those blog posts on the site. They’re not all lorem ipsum text. Hrm… but they do reference other companies. Maybe these scammers just lifted the text from some legit company? It seems plausible that “New England Auto Shipping” is probably a legit company they stole this from. Let’s copy this text and paste it into Google:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-47.png?w=942)](https://textslashplain.com/wp-content/uploads/2025/04/image-47.png)

I didn’t find the source (*likely `[neautoshipping.com](https://web.archive.org/web/%2A/https%3A//neautoshipping.com/%2A)`, an earlier version of the scam from October 2024*), but I *did* find another live copy of the attack, hosted on a similar domain:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-48.png?w=789)](https://textslashplain.com/wp-content/uploads/2025/04/image-48.png)

This version is hosted at `firstline-vehicle.com` with the phone number (`908-505-5378`) and an address in New Jersey. They’ve literally been copy/pasting their scam around!

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-49.png?w=385)](https://textslashplain.com/wp-content/uploads/2025/04/image-49.png)

Netcraft reports that it’s first seen next month 🙃. Good thing I’ve got my time machine up and running!

The page title of this scam site doesn’t match the scammers though. Hmm… What happens if I look for “Bergen Auto Logistics” then?

Another scam site, `bergen-autotrans.com`, this one registered this month and CEO’d by a Stock Photo woman:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-50.png?w=389)](https://textslashplain.com/wp-content/uploads/2025/04/image-50.png)

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-51.png?w=935)](https://textslashplain.com/wp-content/uploads/2025/04/image-51.png)

There are some more interesting photos here, including some that are less obviously faked:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-53.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/04/image-53.png)

It looks like there was an earlier version of this site in November 2024 at `bergenautotrans.com` that is now offline:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-52.png?w=760)](https://textslashplain.com/wp-content/uploads/2025/04/image-52.png)

Searching around, we see that there’s also currently a **legit business** in New York named “Bergen Auto” whose name and reputation these scammers may have been trying to coast off of. And now some of the pieces are starting to make more sense — Bergen New York *is* on the US/Canada border.

Searching for the string `"Your car does not need be running in order to be shipped"` turns up yet more copies of the scam, including `britt-trucking.net` with phone number `(602) 399-7327`:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-54.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/04/image-54.png)

Another random [Stock Photo CEO](https://tineye.com/search/563daa489c8257e1b52ec0ff05414a52efe84846?sort=score&order=desc&page=1) is here, and our same General Manager now has a new name:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-56.png?w=573)](https://textslashplain.com/wp-content/uploads/2025/04/image-56.png)

…and hey, look, it’s our old friends, now with a different logo on their shirts!

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-55.png?w=420)](https://textslashplain.com/wp-content/uploads/2025/04/image-55.png)

Interestin...