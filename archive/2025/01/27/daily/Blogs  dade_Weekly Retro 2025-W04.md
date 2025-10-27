---
title: Weekly Retro 2025-W04
url: https://0xda.de/blog/2025/01/weekly-retro-2025-w04/
source: Blogs  dade
date: 2025-01-27
fetch_date: 2025-10-06T20:08:06.166060
---

# Weekly Retro 2025-W04

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/01/weekly-retro-2025-w04/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

4 minutes

# [Weekly Retro 2025-W04](https://0xda.de/blog/2025/01/weekly-retro-2025-w04/)

---

* [The Tailwindification of Natlas](#the-tailwindification-of-natlas)
* [The mysterious case of the unregistered nameserver](#the-mysterious-case-of-the-unregistered-nameserver)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

This past week has been a bit light, my mom has been visiting and I’ve been taking her to my favorite spots and doing some touristy things. I’m grateful to be in a position in life where I could fly her here and spend a few days eating good food and exploring San Francisco. When I have had time, I’ve been working on Natlas and doing DNS research.

## The Tailwindification of Natlas

Last week I mentioned that I was starting to move towards a Tailwind-based website styling, away from bootstrap. There’s a bunch of small components that need to be ported over, and some tweaks to a bunch of things to make it look better, a number of small details got pretty messed up while working on mimicing the bootstrap styles.

As part of this frontend overall, I’m learning a few things:

1. While I like tailwind for the consistency that it produces, I feel like the light/dark mode support is kinda meh. It’s just more classes with the `dark:` “selector.” I like the CSS variable strategy with media queries more than having to preface more classes on each component.
2. Bootstrap comes with javascript to make a bunch of it’s behaviors easy to use, and that’s great. But if I want to get rid of bootstrap, I have to replicate some of these behaviors. I tried using Alpine, and it’s a little painful. I’m likening some of the ways it works to react’s concept of lifting state up, but my markup isn’t really built/designed in a way where that’s very easy. E.g. my image modal, I don’t want to have a separate image modal for every image on a page, I want one modal that loads different data when you click on the image. But that was pretty difficult to achieve with Alpine. Maybe it’s not the right tool for the job.
3. I didn’t version my data, instead I just tied the markup for displaying data to the agent version. This ultimately means that I have a ton of duplicate markup. I think, since I’ve already gone full backwards-incompatible, I’m going to delete all the old agent-version markup folders and switch to a data-version approach. That way I can just change the markup for specific data version changes that require it. Maybe with a way that can do JIT data migrations when an old bit of data is rendered, if possible.

## The mysterious case of the unregistered nameserver

This week I also wrote about [unregistered nameservers in the .com zone](https://0xda.de/blog/2025/01/invalid-niger-nameservers-in-the-com-zone/), based on reporting from Brian Krebs about a researcher who found the same issue impacting some Mastercard properties.

If you want to learn more about the process and my thoughts on it, please visit the link above. But the TL;DR is that there are hundreds of domains out there with incorrect nameserver configurations that point to unregistered domains, leading to all sorts of potential problems. I think TLD operators *could* mitigate this by monitoring and validating the contents of their zone files, but I don’t know if this *should* be their responsibility.

## Interesting Links

* [The Mythical IO-Bound Rails App](https://byroot.github.io/ruby/performance/2025/01/23/the-mythical-io-bound-rails-app.html) - I don’t write ruby anymore, and I have no interest in writing ruby again, but I do like this sort of investigation into the idea that many web apps are IO bound by default due to waiting on the database.
* [Open Heart Protocol](https://openheart.fyi/) - This is a fun little idea that brings the idea of reaction emojis to web pages. I don’t think I’m going to implement it on this site (due to how much effort I put into keeping it static), but I do think it’s a fun idea.
* [Unpoly](https://unpoly.com/) - This library bills itself as progressive enhancement for HTML with graceful degradation. I haven’t looked too much at it, but I do want to investigate it further. Several things feel pretty similar to htmx, but it also looks like it might be able to address some of the things I was complaining about above in the natlas section.
* [rdap.org](https://about.rdap.org/) - I’ve been investigating RDAP recently as part of my efforts to build my own open source intelligence platform, and rdap.org seems like a super good resource. Thanks [Gavin Brown](https://gavinbrown.xyz/) for maintaining it.
* [Moving on from React, a Year Later](https://kellysutton.com/2025/01/18/moving-on-from-react-a-year-later.html) - A retrospective on a company’s decision to move on from React. I love reading people’s stories about how maybe React wasn’t the best tool for their particular job.
* [Incremental Writes in Hugo](https://www.thedroneely.com/posts/incremental-writes-in-hugo/) - A post about configuring Hugo to do incremental writes. The larger my site gets, the slower it feels like builds are, and I was curious about whether or not I could do incremental writes to improve this. Basically, most pages don’t change most times that I build. Could I *only* write the new & changed pages? It looks like there’s some promising opportunity.

## Upcoming Projects

* Protocol - I’ve recorded the first few episodes and am going to work on editing them in the coming week. I am hoping to have the first video launch during the first week of February.

---

Share this page

`https://0xda.de/blog/2025/01/weekly-retro-2025-w04/`

[weekly retro](https://0xda.de/tags/weekly-retro)[natlas](https://0xda.de/tags/natlas)

844 Words

Date Published

2025-01-26 20:50 +0000

d298235 @ 2025-02-23

---

[â
Lessons in Everything](https://0xda.de/blog/2025/01/lessons-in-everything/)

[Invalid Niger Nameservers in the com zone
â](https://0xda.de/blog/2025/01/invalid-niger-nameservers-in-the-com-zone/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2025
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2025/01/weekly-retro-2025-w04/ "Tor")
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

[Rss](https://0xda.de/blog/index.xml "RSS")
[JSON Feed](https://0xda.de/blog/index.json "JSON Feed")