---
title: How the CNA thing is working out
url: https://daniel.haxx.se/blog/2025/04/24/how-the-cna-thing-is-working-out/
source: daniel.haxx.se
date: 2025-04-25
fetch_date: 2025-10-06T22:05:47.059357
---

# How the CNA thing is working out

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2024/09/cvemitrecvssnvdcnaoss-wtf-wide.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# How the CNA thing is working out

[April 24, 2025](https://daniel.haxx.se/blog/2025/04/24/how-the-cna-thing-is-working-out/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [3 Comments](https://daniel.haxx.se/blog/2025/04/24/how-the-cna-thing-is-working-out/#comments)

Do you remember how [curl became a CNA](https://daniel.haxx.se/blog/2024/01/16/curl-is-a-cna/) early last year?

I was reminded that I had not really gotten back to this topic and explained to you, my dear readers, how it is and how it has worked out. This curl-being-a-CNA thing I mean.

CNA stands for CVE Numbering Authority. Every CNA has the right and ability to allocate and publish their own CVE records. We manage a “vulnerability scope” that is ours and every CNA cares for all CVEs within our own respective scopes. Right now there are 450 CNAs, up from 350 when we joined.

## CVE instability

Recently the entire CVE system has been shaky. The funding was gone, came back and now while back still seems unreliable and the entire thing is like walking on thin ice. While a related issue, it is not really changing how we work with vulnerabilities and our role as CNA. If the CVE system breaks down and we change to something else tomorrow, we would still try to work exactly the same under that system.

It was never a good idea for CVE to be so tightly associated with or under the control of the US government (any government really). Maybe this can still push the development in the right direction?

## Becoming CNA

A primary reason for us to become CNA was to be able to block bogus CVEs from being registered against curl. This has worked fine, but we also have not yet had to reject a single CVE request…!

A secondary reason was to be able to set our own severity levels for the issues we publish. This has not worked out great – or at all really. Or rather, we *can* indeed set our own CVSS scores on issues and then that *would had been fine*, but since we object to the one-dimensional impossible mission of setting a single score for a problem with a product that can be used in virtually any product and in any context, it does not. When we don’t fill in the CVSS field, someone else does it for us and they do it more or less by rolling dice.

More on CVSS below.

The actual process of becoming a CNA is straight-forward. It does not cost any money (just some time and effort), there is not a lot of red tape or weirdo procedures to follow or forms to fill in. There are just a few basic and quite reasonable steps and confirmations made, and then you’re in.

## Being CNA

The actual being a CNA part is a low friction and low maintenance role. Allocating and publishing CVEs can of course be burdensome, but it’s not a lot more work to do it yourself than to fill in forms and have someone else press submit.

The bulk of the security work in curl is still the same as before we became a CNA, as that is the researching, understanding, debating and assessing part of it. In our case, we had meticulous control and check of every possible detail of our security related issues already before and we still do. We take pride in providing top notch security information.

## Working on the inside

Being a CNA of course allows us to discuss and work on things for and related to the CVE project on “the inside”. There are two things I primarily want like to see addressed:

### Flaw 1 – everyone must be a CNA

The fact that the CVE system works so bad for involved parties (like Open Source projects) that are not CNAs I believe is a primary weakness in the system. I believe this is the main reason for the current *avalanche* of new CNAs signing up. We all want control of CVEs assigned to us – or claiming to be about our products.

I would like to see a system where projects could add their products to the scope of an existing CNA so that small projects can avoid becoming a CNA but still “protect” and “own” their respective CVE spaces. This alone would drastically lessen the need and attraction of the whole world becoming CNAs. I don’t think there is anything inherent in the system that prevents this from working, but it would perhaps be good with a more formalized way of accepting this approach.

### Flaw 2 – CVSS is often more of a joke than useful

There is this *OSS CNA user group*, an informal formation of Open Source based CNAs that discuss CVE and vulnerability management within this system, and as a team we are currently drafting a proposal to allow Open Source projects to prevent ADPs (Authorized Data Publishers) like CISA to *amend* CVE records with CVSS scores.

This is far from being just a curl problem. The Linux kernel has it, perl has it, lots of projects who do foundational and ubiquitous software do. When we report a security problem, it is next to impossible for us to assess the CVSS score in a way that would work for everyone as our stuff can be used in some many different places in so many different ways.

For this reason we avoid setting CVSS scores, but for now we cannot stop official ADPs to then step in and do it for us. We cannot say stop. We cannot prevent them from doing this. We want to establish a formal mechanism and process where can say **STOP**. To tell them *hands off from our CVSS score field*. To let it remain unset if we decide so.

### Other flaws

Of course there are more issues in this system, but I consider the two ones mentioned above more important than others.

## Future

Remind me and I’ll follow up in a year or so and see how things are different if at all. I expect lots of new CNAs in the meantime. I expect the CVE system to go through at least some metamorphosis following in the footsteps of the US breakdown. I expect 2025 to have substantially more CVE entries published than during 2024 and I expect 2026 to have even more.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[CVE](https://daniel.haxx.se/blog/tag/cve/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous PostSumming up the curl distro 2025 meet](https://daniel.haxx.se/blog/2025/04/10/summing-up-the-curl-distro-2025-meet/)[Next Postcurl up 2025 is over](https://daniel.haxx.se/blog/2025/05/06/curl-up-2025-is-over/)

## 3 thoughts on “How the CNA thing is working out”

1. ![](https://secure.gravatar.com/avatar/9a1afd46ab2720cae3a32c37fa86d963f8e95b0e09e27530a58d2ffbf2e39dc1?s=34&d=monsterid&r=g) **Martin Prpi?** says:

   [April 24, 2025 at 20:42](https://daniel.haxx.se/blog/2025/04/24/how-the-cna-thing-is-working-out/#comment-27160)

   Re flaw #1: The current system does not assume that everyone should be a CNA. The role of a CNA should be reserved for organizations (both open source and commercial) that have the resources necessary to publish and maintain their own CVE records. This assumes the knowledge of how to create and publish the records with accurate data, and how to actively participate in the CVE program. Open source projects that don’t have the resources to do this can turn to other CNAs that will happily do this for them (allocate CVE IDs and publish the data in form of CVE records). If you’re an Apache project, you don’t have to be your own CNA, you can go to the Apache Software Foundation CNA. Same goes for Go packages within the Go language ecosystem (Go Project CNA) or official PostgreSQL components (PostgreSQL CNA). In absence of a more specific CNA, you can always turn to Red Hat, wh...