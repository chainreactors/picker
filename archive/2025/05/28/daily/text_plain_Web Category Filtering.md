---
title: Web Category Filtering
url: https://textslashplain.com/2025/05/27/web-category-filtering/
source: text/plain
date: 2025-05-28
fetch_date: 2025-10-06T22:28:38.948896
---

# Web Category Filtering

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Web Category Filtering

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-05-272025-09-17](https://textslashplain.com/2025/05/27/web-category-filtering/)Posted in[browsers](https://textslashplain.com/category/browsers/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [Defender](https://textslashplain.com/tag/defender/), [Edge](https://textslashplain.com/tag/edge/), [networking](https://textslashplain.com/tag/networking/)

Since the first days of the web, users and administrators have sought to control the flow of information from the Internet to the local device. There are many different ways to implement [internet filters](https://en.wikipedia.org/wiki/Internet_filter), and numerous goals that organizations may want to achieve:

* [blocking malicious sites](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/),
* [blocking ads](https://textslashplain.com/2015/06/10/collateral-damage/) or [trackers](https://web.archive.org/web/20101205015334/http%3A//blogs.msdn.com/b/ie/archive/2010/11/30/selectively-filtering-content-in-web-browsers.aspx#:~:text=Evaluation%20of%20Blocking%20Mechanisms),
* blocking responses based on the category of content a site serves.

Today’s post explores the last of these: **blocking content based on category**.

### The Customer Goal

The customer goal is generally a straightforward one: *Put the administrator in control of what sorts of content may be downloaded and viewed on a device*. This is often intended as an enforcement mechanism for an organization’s **Acceptable Use Policy (AUP)**.

An AUP often defines what sorts of content a user is permitted to interact with. For example, a school may forbid students from viewing pornography and any sites related to alcohol, tobacco, gambling, firearms, hacking, or other criminal activity. Similarly, a company may want to forbid their employees from spending time on data and social media sites, or from using legitimate-but-unsanctioned tools for sharing files, conducting meetings, or interacting with artificial intelligence.

### Mundane Impossibility

The simplicity of the goal belies the impossibility of achieving it. On today’s web, category filtering is inherently impossible to perfect for several reasons:

1. **New sites** arrive all day, every day.
2. The content served by any site can [**change** at any time](https://textslashplain.com/2023/10/13/beware-urls-are-pointers-to-mutable-entities/).
3. There are an **infinite number of categories** for content (and no true standard taxonomy).
4. Decisions of a site’s category are **inherently subjective**.
5. Many sites host content **across multiple categories,** and some sites host content from almost every category.
6. [**Self-labelling** schemes](https://en.wikipedia.org/wiki/Internet_filter#:~:text=%5B37%5D-,Content%20labeling,-%5Bedit%5D) like ICRA and [PICS](https://en.wikipedia.org/wiki/Platform_for_Internet_Content_Selection) (Platform for Internet Content Selection), whereby a site can declare its own category, have all failed to be adopted.

As an engineer, while it would be nice to work on only tractable problems, in life there are many intractable problems for which customers are willing to buy imperfect **best-effort** solutions.

Web content categorization is one of these, and because sites and categories change constantly, it’s typically the case that content filtering is sold on a **subscription basis** rather than as a one-time charge. Most of today’s companies *love* recurring revenue streams.

So, given that customers have a need, and software can help, how do we achieve that?

### Filtering Approaches

The first challenge is figuring out how and where to block content. There are [many approaches](https://en.wikipedia.org/wiki/Internet_filter#:~:text=Types%20of%20filtering%5Bedit%5D); Microsoft’s various Web Content Filtering products and features demonstrate three of them:

* **Browser Integration** – [Defender WCF](https://learn.microsoft.com/en-us/defender-endpoint/web-content-filtering)-atop-Edge or [Edge’s Native WCF](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-web-content-filtering#enable-wcf-for-a-configuration-policy:~:text=Your%20organization%20must%20have%20a%20M365) (available to only specific M365 licensees)
* **On-Device [Network Filtering](https://textslashplain.com/2025/03/31/defensive-technology-windows-filtering-platform/)** – [Defender WCF](https://learn.microsoft.com/en-us/defender-endpoint/web-content-filtering)-atop-[Network-Protection](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/)
* **Remote Proxy or VPN** – [Microsoft Entra Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-web-content-filtering-categories)

Each implementation approach has its plusses and minuses, from:

1. Supported browsers: does it work in any browser? Only a small list? Only a specific one?
2. Performance: Does it slow down browsing? Because the product may categorize *billions* of URLs, it’s usually not possible to store the map on the client device.
3. User-experience: What kind of block notice can be shown? Does it appear in context?
4. Capabilities: Does it block only on navigating a frame (e.g. HTML), or can it block any sub-resources (images, videos, downloads, etc)? Are blocks targeted to the current user, or to the entire device?

## Categorization

After choosing a filtering approach, the developer must then choose a source of categorization information. Companies that are already constantly crawling and monitoring the web (e.g. to build search engines like Bing or Google) might perform categorization themselves, but most vendors acquire data from a classification vendor like [NetStar](https://incompass.netstar-inc.com/urlsearch) or [Cyren](https://data443.com/cyren-url-category-check-gate/) that specializes in categorization.

Exposing the classification vendor’s entire taxonomy might be problematic though– if you bind your product offering too tightly to a 3rd-party classification, any taxonomy changes made by the classification vendor could become a breaking change for your product and its customers. So, it’s tempting to go the other way, and ask your customers what categories *they* expect, then map any of the classification vendor’s taxonomy onto the customer-visible categories.

This is the approach taken by Microsoft Defender WCF, for example, but it can lead to surprises. For example, Defender WCF classifies `archive.org` in the `Illegal Software` category, because that’s where our data vendor’s `Remote Proxies` category is mapped. But to the browser user, that opaque choice might be very confusing — while `archive.org` almost certainly contains illegal content (it’s effectively a time-delayed proxy for the entire web), that is not the category a normal person would first think of when asked about the site.

Ultimately, an enterprise that implements Web Content Filtering must expect that there will be categorizations with which they disagree, or sites whose categories they agree with but wish to allow anyway (e.g. because they run ads on a particular social networking site, for instance). Administrators should define a process by which users can request exemptions or reclassifications, and then the admins evaluate whether the request is reasonable. Within Defender, an [ALLOW Custom Network indicator](https://learn.microsoft.com/en-us/defender-endpoint/indicators-overview#ipurldomain-indicators) will override any WCF category blocks of a site.

### Aside: Performance

If your categorization approach requires making a web-service request to look up a content category, you typically want to do so in parallel with the request for the content to im...