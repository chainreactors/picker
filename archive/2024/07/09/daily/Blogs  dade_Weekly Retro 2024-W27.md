---
title: Weekly Retro 2024-W27
url: https://0xda.de/blog/2024/07/weekly-retro-2024-w27/
source: Blogs  dade
date: 2024-07-09
fetch_date: 2025-10-06T17:43:15.725343
---

# Weekly Retro 2024-W27

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/weekly-retro-2024-w27/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Weekly Retro 2024-W27](https://0xda.de/blog/2024/07/weekly-retro-2024-w27/)

---

* [Bittensor Security Incident](#bittensor-security-incident)
* [Framework - Now With Sops-Nix](#framework---now-with-sops-nix)
* [Website Improvements](#website-improvements)
* [What I’m Reading](#what-im-reading)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

It was a short week, I had Thursday off for Independence Day, and don’t tell my boss but I mostly took Friday off, too. I mean, besides the few hours of work I did. I made pretty good progress on my Laptop setup, accidentally investigated a Bittensor security incident, and fixed my opengraph meta tags on my site.

## Bittensor Security Incident

Apparently a project called [Bittensor had a security incident](https://0xda.de/blog/2024/07/bittensor-security-incident-an-independent-analysis/) that resulted in some millions of dollars being transferred to an attacker’s wallet. This was about all I knew about the project, but someone was wrong about the cause on the internet, so I accidentally spent an hour or so digging into it.

The gist of it is that some malicious code was uploaded to PyPI under the official `bittensor` package. This happened a few hours before the Github and Dockerhub versions went live, and only the PyPI release was infected. The nature of the compromise suggests a compromised PyPI API key, either through accidental exposure or through a compromised PyPI package maintainer.

## Framework - Now With Sops-Nix

[Part 5 in my Framework & NixOS laptop setup journey](https://0xda.de/blog/2024/07/framework-and-nixos-sops-nix-secrets-management/), I got Sops-nix working with a private repository and use that to declaratively manage my user password to begin with. This process wasn’t so bad, but as I’m looking into the other secret values I’d like to declaratively manage, I’m definitely having a bit of a hard time. I’m learning a lot about the NixOS lifecycle in the process, though.

One of the reasons that proper secret management is important with Nix is that otherwise, your secret values will get copied into the Nix store, which is readable by all users and processes on your machine. Sops-nix ensures that the secrets are made available at runtime, which avoids them being copied into the Nix store.

## Website Improvements

For as long as I’ve been writing these posts and sharing them on social media, I realized that my opengraph tags weren’t displaying correctly, and I couldn’t figure out why.

It turns out, the theme that I’ve based this site off of didn’t use the `opengraph` internal Hugo template, it was only using the `twitter` template, which included twitter-specific opengraph tags. What’s particularly funny is that I think even those tags haven’t really worked reliably well since Elon took over.

```
{{- template "_internal/opengraph.html" . }}
```

Anyways, I fixed that and now my opengraph tags look good (or at least, how I expect them to look) everywhere, according to [opengraph.dev](https://opengraph.dev/panel?url=https%3A%2F%2F0xda.de).

I also updated my header menu to include a page about my music, and moved the colophon to the footer. I’d like to also think about where I’d add a digital garden concept to my site, as well as improve a few style things – namely:

* Key combination shortcode – I’d like to add a shortcode I can easily reference that will render key combinations in a way that makes it clear what they are. If you have recommendations for this, I’d love to hear about it!
* Language header for code blocks – I’d like to automatically create language headers or indicators in my code blocks. I’m not sure if this will be easy or not – the language is declared in `data-lang`, as well as a class `language-<language>` on both the `code` element and the parent `pre` element. I don’t want to rely on javascript, but also don’t know if I can easily change the way markdown is rendered in Hugo.

## What I’m Reading

![Book cover for Tor, by Ben Collier. Subtitle 'From the Dark Web to the Future of Privacy'](https://0xda.de/img/books/Tor-BenCollier.707217e2e555c61ae61bfda7e1186776.jpg)

### Tor: From the Dark Web to the Future of Privacy

#### By Ben Collier

**ISBN: 9780262548182**
[Learn More](https://mitpress.mit.edu/9780262548182/tor/ "Learn More About The Book")

---

Finally, I made progress! Not as much as I’d have liked, but so it goes. In the second chapter, it covers the different worlds of the early online communities, and in retrospect, it’s incredible how things like Tor evolved out of some radically different communities, with radically different end goals. It reminds me of how funny I think it is when people are like “It was made by the military, bro, of course it’s backdoored” – as if the military doesn’t have direct operational benefits of something like Tor.

## Interesting Links

* [Unraveling Factorio’s Lua Security Flaws](https://memorycorruption.net/posts/rce-lua-factorio/) - I’ll be honest. I’m not smart enough to understand this. But it’s pretty cool to hack a game so that a server can execute arbitrary code on clients. Maybe you’ll understand it better than me.
* [Cyber Is Full](https://cyberisfull.com/) - I saw some folks share this, I read it, I think there’s some truth to it, but I also think there’s several parts of it that are just personal whining/ranting about how people didn’t follow the same path as the author and/or that there are other paths that didn’t previously exist.
* [Should this be a map or 500 maps?](https://escapethealgorithm.substack.com/p/should-this-be-a-map-or-500-maps) - I’d be willing to bet if this guy just accepted that the work would be hard and long, he would have gotten it done correctly before he died. Instead, he delegated to people who had no idea what they were doing, and ended up with 500 maps that did not paint an accurate picture of the lay of the land.
* [The intelligence coup of the century](https://www.washingtonpost.com/graphics/2020/world/national-security/cia-crypto-encryption-machines-espionage/) - I really enjoyed this post about the history of Crypto AG, how it was run by spooks and sold intenionally weakened cryptography devices to hostile nations. It is an amusing foreshadowing of the same type of operation that led to the Anom phone network.
* [The ultimate guide to Full Disk Encryption with TPM and Secure Boot](https://blastrock.github.io/fde-tpm-sb.html) - I didn’t really end up needing this or using this, but it was another example of using hardware to back your encryption keys.
* [Cyberpunk Rhapsody](https://noveliss.bandcamp.com/album/cyberpunk-rhapsody) - I stumbled on 5 A.M. in Kyoto, the first song from this album, and immediately went to listen to the whole album. I really enjoyed it, and I hope you do as well.

## Upcoming Projects

* [BSides Las Vegas Talk](https://bsideslv.org/cfp) - **Accepted!** - I will be presenting “Free Your Mind: Battling Our Biases” at BSides Las Vegas 2024. This will be my first return to a public stage in like 6 years, and my first time speaking in Vegas. Stay tuned.
* [Defcon 32 Call For Soundtrack](https://twitter.com/defcon_music/status/1775625331258626434) - I’ve **submitted** my new song “Oh Dade”, produced by [Mikal kHill](https://mikalkhill.bandcamp.com/). If it’s accepted, it will debut on the Defcon soundtrack. If it’s not ...