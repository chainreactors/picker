---
title: Reflecting on How We Plant and Grow Onions
url: https://blog.torproject.org/how-we-plant-and-grow-new-onions/
source: Tor Project blog
date: 2023-03-10
fetch_date: 2025-10-04T09:11:19.520511
---

# Reflecting on How We Plant and Grow Onions

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# Reflecting on How We Plant and Grow Onions

by [raya](/author/raya)
| March 9, 2023

![](/how-we-plant-and-grow-new-onions/lead.png)

In February of 2022 we launched a small team within the Tor Project called the Onion Support group. It was initiated with the simple goal to increase onion service adoption among civil society groups, human rights organizations, and news media outlets.

What drove us to create the group was realizing that onion services were not being used to their fullest extent and their features were not well understood among those promoting human rights. More importantly, there's not enough support and guidance for groups around the world who want to set up their own onion site.

With support from the Open Technology Fund, we have been able to assist a number of organizations to learn about the world of onions and set up their own onion service. We supported organizations by deploying the onion service on their behalf and then handing it over to them, but for organizations with the technical capacity we provide high-level support for onion service deployment. We also trained team members on everything to do with Tor and co-created advocacy campaigns around the Tor network and onion services.

As a result, today, more and more organizations have a [".onion available" purple pill](https://support.torproject.org/onionservices/onionservices-5/) appear as you're visiting their site on Tor Browser.

## Tools to make Onion Services more widely available

In parallel to the above, we published open source tools to support onion services development more generally, including:

1. **Onionprobe**, which is an open source tool to monitor the status and uptime of an Onion Service and enables service operators to diagnose issues: <https://gitlab.torproject.org/tpo/onion-services/onionprobe>, [Debian package](https://tracker.debian.org/pkg/onionprobe), [Arch Linux package](https://aur.archlinux.org/packages/onionprobe-git)
2. **Onion Launchpad**, a customizable landing page that explains to a general audience how to download Tor Browser, connect to Tor, and access a specified Onion Service (content is being translated in over 61 languages): <https://gitlab.torproject.org/tpo/onion-services/onion-launchpad>
3. **Onionmine**, a handy wrapper to organize vanity addresses and TLS certificates generation for Onion Services: <https://gitlab.torproject.org/tpo/onion-services/onionmine>.

## Advocating for Onion Services

We've also been using this time to reflect on how we talk about onions and how we promote their use in a rational and responsible manner. One way we like to frame onion services is that they're currently the most censorship resistant technology out there. In one sense, it's technically untrue because as long as a user does not have access to the Tor network they won't be able to access any onion service. But what we mean by censorship resistance comes from the fact that the onion address itself is not censorable. No Internet provider or government can detect the connection to the service and block access to it, which in our view enforces the resistance against censorship.

Moreover, when connecting to an onion service, you can be sure that the communication is end-to-end encrypted with no metadata recorded on your activity. You are also contributing to the decentralized Web since, to launch an onion service, you don't need a static IP address or purchase a domain; in fact an onion address is basically a public key.

## A border-less country-agnostic space

One thought experiment we've been toying with is thinking of this onion space as a border-less country-agnostic space. When accessing a website over VPN, you're exiting from the VPN server which is located in a specific country, and the experience of navigating that website will differ based on which country you're visiting it from (i.e. where the VPN server is located). When accessing a website over Tor, this depends on where the exit node is located. When accessing an Onion Service on the other hand, you're not "exiting" from anywhere, rather you're meeting the website inside the Tor network.

**There are positives to thinking about Onion services this way:**

* A country-agnostic visit implies one that removes risks and pressures put forward by different jurisdictions (similar to risks VPN providers and Tor exit nodes face).
* A border-less Internet is akin to a quiet and peaceful room away from the noise bustling outside of the Tor network and on the "regular" Internet.

Finally, onion services offer maximum harm reduction when compared to visiting a regular site or visiting a site over Tor. There are multiple cases of people prosecuted over digital evidence - particularly metadata and IP information - that can only be avoided if people used onion counterparts to websites (obviously you would need to avoid logging in to an account which contains your real name or accounts you've logged in previously outside Tor exposing your IP and other information).

On a personal level, I find that sharing a .onion address with a friend or colleague is a way to gently influence them to open and browse a site using only the Tor Browser. This way I can guarantee that they're not going to visit it on a regular browser, risk being uncovered for visiting sensitive content, and expose themselves to a slew of threats as a result.

If you or your organization is interested in learning more about onions and onion support, please contact us through this form: <https://nc.torproject.net/apps/forms/s/bGswKTbTj8ikYb4oPen9W9ig>. You can also ask questions and start a discussion on [The Tor Project Forum.](https://forum.torproject.net/c/support/onion-services/)

## Additional resources:

* [Onion Support group on The Tor Project's GitLab](https://gitlab.torproject.org/tpo/onion-services/onion-support)
* [State of the Onion 2022 | Onions Everywhere talk](https://youtu.be/uSyBZ7GIzJY?t=1176)
* Threat models for Onion Services:
  + <https://gitweb.torproject.org/tor-design-2012.git/tree/tor-design-2012.tex>
  + <https://github.com/mikeperry-tor/vanguards/blob/master/README_SECURITY.md>
  + <https://code.briarproject.org/briar/briar/-/wikis/threat-model>
* [Why build an Onion Site / use Onion Services? By Alec Muffett](https://github.com/alecmuffett/guide-to-onion-services)

* [onion services](/category/onion-services)
* [circumvention](/category/circumvention)
* [community](/category/community)
* [human rights](/category/human-rights)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/how-we-plant-and-grow-new-onions/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/how-we-plant-and-grow-new-onions/&text=We%20realized%20Onion%20Services%20were%20not%20used%20to%20their%20fullest%20extent%2C%20so%20we%20launched%20support%20initiatives%20and%20resources%20to%20provide%20education%2C%20information%20and%20increase%20adoption.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/how-we-plant-and-grow-new-onions/&text=We%20realized%20Onion%20Services%20were%20not%20used%20to%20their%20fullest%20extent%2C%20so%20we%20launched%20support%20initiatives%20and%20resources%20to%20provide%20education%2C%20information%20and%20increase%20adoption.)
[Bluesky](https://bsky.app/intent/compose?text=We%20realized%20Onion%20Services%20were%20not%20used%20to%20their%20fullest%20extent%2C%20so%20we%20launched%20support%20initiatives%20and%20resources%20to%20provide%20education%2C%20information%20and%20increase%20adoption.%0Ahttps%3A//blog.torproject.org/how-we-plant-and-grow-new-onions/)

## Comments

We encourage respectful, on-topic comments. Co...