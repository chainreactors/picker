---
title: 'A newspaper without borders': Mediapart now available as .onion
url: https://blog.torproject.org/mediapart-launches-onion-service/
source: Tor Project blog
date: 2024-09-06
fetch_date: 2025-10-06T18:31:56.924794
---

# 'A newspaper without borders': Mediapart now available as .onion

[![Tor Blog](/static/images/logo.png)](/)

* [About](https://www.torproject.org/about/history/)
* [Support](https://support.torproject.org/)
* [Community](https://community.torproject.org/)
* [Forum](https://forum.torproject.org/)
* [Donate](https://donate.torproject.org/)
* [ ]

# 'A newspaper without borders': Mediapart now available as .onion

by [pavel](/author/pavel)
| September 5, 2024

![](/mediapart-launches-onion-service/lead.png)

We are excited to officially welcome [Mediapart.fr](http://mediapart.fr), an independent French investigative online newspaper, to [the growing list of news outlets that have adopted a .onion site](https://community.torproject.org/onion-services/) on the Tor network. By leveraging Tor technology, Mediapart ensures that its reporting can reach everyone, everywhere, regardless of the political climate.

Readers can now access Mediapart's reporting via <https://www.mediapartrvj4bsgolbxixw57ru7fh4jqckparke4vs365guu6ho64yd.onion/>.Â

## Protecting readers, defending independent journalism

Freedom of expression, access to information, and freedom of the press are fundamental rights that Mediapart has upheld since its creation in 2008 through its extensive investigative reporting. In some countries however, authorities restrict access to the free press, as seen recently [with the blocking of European media outlets in Russia](https://www.mediapart.fr/journal/fil-dactualites/250624/la-russie-annonce-bloquer-l-acces-81-medias-europeens-dont-le-site-de-l-afp-sur-son-territoire). This ultimately prompted the launch of [Mediapart's onion](https://www.mediapartrvj4bsgolbxixw57ru7fh4jqckparke4vs365guu6ho64yd.onion/.): to counter such censorship and stand up to those "that hate checks and balances," says Carine Fouteau, the publication's president and publishing editor.

> *"Following Emmanuel Macron's dissolution of the French National Assembly in June 2024, the risk of the far right forming a government in France has prompted us to prepare for the worst," continues Carine. "By being available on the Tor network, we guarantee that our readers can access our information freely, regardless of the political circumstances. We are also thinking of our readers living abroad. Mediapart is a newspaper without borders: [our subscribers need to be able to read us securely wherever they live."](https://blogs.mediapart.fr/mediapart-journal-independant-et-participatif/blog/040924/mediapart-launches-tor)*

## Making the move to the Tor network

To dive deeper into the technical side of launching the .onion domain, we spoke with Yassine Zouggari, DevSecOps Engineer for the outlet, about setting up the [Onion Service](https://www.mediapartrvj4bsgolbxixw57ru7fh4jqckparke4vs365guu6ho64yd.onion/.) using [Onionspray](https://onionservices.torproject.org/apps/web/onionspray/). This tool simplifies the process by setting up HTTPS rewriting proxies between existing websites and Tor users. Onionspray provides an extra protocol layer for accessing public sites. By relying on the Onion Services technology, it protects the user location information and the website against censorship as long as both the website and users can access the Tor network.

### The Tor Project: Why did you decide to launch a .onion site now? Is it solving any problems you were experiencing?

**Yassine Zouggari:** One of our main objectives has been to provide a convenient way for our users to securely connect to our website. Launching the Onion Service also enables us to more easily allow legitimate Tor traffic to our site, as using our clearnet website with Tor is sometimes blocked by our website's own defenses.

What prompted us to launch this service at this particular moment in time were the recent European elections and the French Parliament's dissolution. We want to make sure that we have tools in place that make it as easy as possible for our readers to circumvent censorship of our clearnet website, should it occur in the future.

### TP: How was your experience using Onionspray? Did you find it easy to use?

**Yassine:** Onionspray made it straightforward for us to deploy the .onion domain without much effort. We had a basic version working pretty much out-of-the-box, with very minimal setup to make it work flawlessly. The software comes equipped with all the necessary tools and configurations, and the documentation is precise and helpful.

The bulk of the work has been 1) adapting our security measures to rate-limit requests per-user if coming through our Onionspray proxy, so that one brute-forcer does not impact the whole Onion Service; and 2) making Onionspray easier to deploy in our infrastructure as code (IaC) context. To make such a deployment easier for others, [we have open sourced our Ansible role](https://gitlab.torproject.org/zoug/onionspray-ansible-role), which handles the full setup.

### TP: Overall, how much time did you spend setting up your Onion Service? Would you say that it is a worthwhile investment for other websites and news outlets?

**Yassine:** All in all, the technical setup took about a week for one engineer. We also hope that our contributed Ansible role will significantly speed up this process for others--especially for other organizations with similar requirements to ours.

I believe this is a worthwhile investment: Ensuring that people around the world have access to trustworthy news sources is paramount, regardless of the political context and what might be allowedÂ  in their country. The more people use Tor, the more effective it becomes at anonymizing traffic. Setting up an Onion Service promotes the use of Tor and therefore will also contribute to the fight against mass surveillance.

---

If you are a news outlet or organization interested in enhancing access and security to your website, visit [Onionspray](https://onionservices.torproject.org/apps/web/onionspray/) to learn more about simplifying the setup of Onion Services for public websites.

* [announcements](/category/announcements)
* [onion services](/category/onion-services)
* [partners](/category/partners)

**Share this post:**
Copy link
[Facebook](http://www.facebook.com/share.php?u=https%3A//blog.torproject.org/mediapart-launches-onion-service/)
[Twitter/X](https://twitter.com/intent/tweet?url=https%3A//blog.torproject.org/mediapart-launches-onion-service/&text=Mediapart.fr%2C%20an%20independent%20French%20investigative%20online%20newspaper%2C%20is%20officially%20launching%20its%20.onion%20site%20to%20ensure%20that%20its%20reporting%20can%20reach%20everyone%2C%20everywhere.)
[Mastodon](https://mastodonshare.com/?url=https%3A//blog.torproject.org/mediapart-launches-onion-service/&text=Mediapart.fr%2C%20an%20independent%20French%20investigative%20online%20newspaper%2C%20is%20officially%20launching%20its%20.onion%20site%20to%20ensure%20that%20its%20reporting%20can%20reach%20everyone%2C%20everywhere.)
[Bluesky](https://bsky.app/intent/compose?text=Mediapart.fr%2C%20an%20independent%20French%20investigative%20online%20newspaper%2C%20is%20officially%20launching%20its%20.onion%20site%20to%20ensure%20that%20its%20reporting%20can%20reach%20everyone%2C%20everywhere.%0Ahttps%3A//blog.torproject.org/mediapart-launches-onion-service/)

## Comments

We encourage respectful, on-topic comments. Comments that violate our
[Code of Conduct](https://community.torproject.org/policies/code_of_conduct)
will be deleted. Off-topic comments may be deleted at the discretion of
the moderators. Please do not comment as a way to receive support or to
report bugs on a post unrelated to a release. If you are looking for
support, please see our [FAQ](https://support.torproject.org/),
[user support forum](https://forum.torproject.org/) or ways to
[get in touch with us](https://www.torproject.org/contact).

Join the discussion on the [Tor Project forum](https://forum.torproject.org/c/news/11)!

## Recent Updates

## [New Alpha Release: Tor Browser 15.0a3](/new-alpha-release-tor-browser-150a3/)

by [boklm](/a...