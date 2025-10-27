---
title: BOFHound: AD CS Integration
url: https://posts.specterops.io/bofhound-ad-cs-integration-91b706bc7958?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-10-31
fetch_date: 2025-10-06T18:58:04.657524
---

# BOFHound: AD CS Integration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F91b706bc7958&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbofhound-ad-cs-integration-91b706bc7958&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fbofhound-ad-cs-integration-91b706bc7958&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-91b706bc7958---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-91b706bc7958---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# BOFHound: AD CS Integration

[![Matt Creel](https://miro.medium.com/v2/resize:fill:64:64/1*6EFikqGheJt57CGRXLXuVg.png)](https://medium.com/%40Tw1sm?source=post_page---byline--91b706bc7958---------------------------------------)

[Matt Creel](https://medium.com/%40Tw1sm?source=post_page---byline--91b706bc7958---------------------------------------)

11 min read

·

Oct 30, 2024

--

Listen

Share

> TL;DR: [BOFHound](https://github.com/coffeegist/bofhound) can now parse Active Directory Certificate Services (AD CS) objects, manually queried from LDAP, for review and attack path mapping within BloodHound Community Edition (BHCE).

## Background

My [last](/bofhound-session-integration-7b88b6f18423) BOFHound-related post covered the support and usage strategies for Beacon object files (BOFs) enabling the manual collection of data required for BloodHound’s AdminTo and HasSession edges, among others. This brief post will cover the addition of AD CS object parsing (shoutout to GitHub user [P-aLu](https://github.com/P-aLu) for collaborating on the update) and some queries to get you started.

But first, to clear up some misconceptions…

### BOFHound is not a BOF!

Surprised and/or confused? Somewhat angry? Yes, this is the most common misconception I hear about the tool. BOFHound is not a BOF implementation of SharpHound; rather, it is a *Python script* that runs completely offline from your target network. I repeat — it is neither a BOF, nor a tool that actively enumerates a target Active Directory (AD) network. If this is not news to you, enlightened reader, consider skipping ahead to [*The Good Stuff*](#cea8).

### So What Does BOFHound Do (and Why on Earth Did You Name It That)?

BOFHound was born from repeated red team engagements in a large AD network where the blue team would flag SharpHound and other “loud” methods of LDAP enumeration. (In this environment, “loud” meant an [expensive LDAP query](https://github.com/SpecterOps/presentations/blob/main/SO-CON%202024/Matt%20Creel%20%26%20Adam%20Brown%20-%20Manually%20Enumerating%20AD%20Attack%20Paths%20with%20BOFHound/Matt%20Creel%20and%20Adam%20Brown%20-%20Manually%20Enumerating%20AD%20Attack%20Paths%20With%20BOFHound%20-%20SO-CON%202024.pdf) — a query that returned a number of results over a threshold the client had determined to be indicative of attacker reconnaissance.) The team I worked with at the time adjusted by primarily relying on the ldapsearch BOF, part of TrustedSec’s [situational awareness](https://github.com/trustedsec/CS-Situational-Awareness-BOF) collection, for LDAP reconnaissance. This had two main benefits:

* It grants the operator full control over the LDAP query filter, meaning discretion can be used to avoid static query strings tied to common offensive tools and leveraged in detections [[1](https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/hunting-for-reconnaissance-activities-using-ldap-search-filters/ba-p/824726), [2](https://falconforce.nl/falconfriday-detecting-active-directory-data-collection-0xff21/)]
* The operator can specify a limit on the result count, so that the query returns no more than N entries; this is helpful when consciously avoiding expensive queries (result pools can also be narrowed with search scope, targeted query filters, or through a search base)

Here are some downsides to solely relying on this approach for LDAP enumeration:

* Queries only return text-based results (i.e., there is no visualization or BloodHound-like graph that many operators prefer)
* Identifying ACL abuses is essentially impossible with this approach alone
* Trying to keep track of and organize relationships between objects, like group memberships (let alone nested memberships), by hand in text/Excel files is difficult

The bigger the target environment is, the more these problems are amplified. These also all sound like problems that BloodHound was originally created to solve. Is there any way we could maintain the granular control the ldapsearch BOF offers us over enumeration and still be able to use BloodHound?

Enter BOFHound. It aims to serve this very niche need by reading LDAP objects from your ldapsearch results in C2 logs, processing them, and producing BloodHound JSON files.

> Thus the name BOFHound — read output from the ldapsearch BOF in log files and make it BloodHound-usable. LogHound just doesn’t have the same ring to it, does it?

This allows for ACL relationships to be parsed (from base64 encoded nTSecurityDescriptor attributes) and for your operators to continue visualizing nodes and relationships in the BloodHound UI where they are happy.

Now you might be wondering “BloodHound collects *all* data [that we frequently care for] in an AD environment, so how can this work with partial data obtained from manual queries?” Well, it’s simple; the BloodHound UI will only show you what you have enumerated via manual queries and parsed with BOFHound. In other words, it will be incomplete data and, if you’re using this approach, you’re likely fine with that. We can target specific information we want to populate the graph with, such as objects related to our objectives, objects that have privileges we want to compromise, or objects that often make easy targets (i.e., [AD CS](/certified-pre-owned-d95910965cd2), [SCCM](https://github.com/subat0mik/Misconfiguration-Manager)).

But BloodHound will actually show you *a little more* than only what you’ve queried. Object ACLs return references (SIDs) to other objects in the environment that are granted some permission over the object you queried. When you parse these ACLs without an object tied to the SID, they are represented in the graph by nodes with SIDs for names or question mark icons. For example, if I query **only** the domain object, run it through BOFHound, upload the result to BloodHound, and check the *Inbound Object Control* on the domain object, we’ll see this.

Press enter or click to view image in full size

![]()

Parsing Single Object Reveals the Presence of Many More

I’ve only queried the domain object, but I also now know that these six other objects exist. Knowing their SIDs provides a means to qu...