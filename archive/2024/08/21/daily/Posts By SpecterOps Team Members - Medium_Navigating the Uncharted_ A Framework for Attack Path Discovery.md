---
title: Navigating the Uncharted: A Framework for Attack Path Discovery
url: https://posts.specterops.io/navigating-the-uncharted-a-framework-for-attack-path-discovery-c5a0a020a144?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-08-21
fetch_date: 2025-10-06T18:05:17.436511
---

# Navigating the Uncharted: A Framework for Attack Path Discovery

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc5a0a020a144&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fnavigating-the-uncharted-a-framework-for-attack-path-discovery-c5a0a020a144&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fnavigating-the-uncharted-a-framework-for-attack-path-discovery-c5a0a020a144&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-c5a0a020a144---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-c5a0a020a144---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Navigating the Uncharted: A Framework for Attack Path Discovery

[![Elad Shamir](https://miro.medium.com/v2/resize:fill:64:64/1*ocQXH46k-rk5MSdLEXKXfA.jpeg)](https://medium.com/%40elad.shamir?source=post_page---byline--c5a0a020a144---------------------------------------)

[Elad Shamir](https://medium.com/%40elad.shamir?source=post_page---byline--c5a0a020a144---------------------------------------)

8 min read

·

Aug 20, 2024

--

Listen

Share

This is the second post in a series on Identity-Driven Offensive Tradecraft, which is also the focus of the [new course](https://specterops.io/training/identity-driven-offensive-tradecraft/) we will [launch in October](https://events.humanitix.com/adversary-tactics-identity-driven-offensive-tradecraft-october-2024-hybrid-us-time). In the [previous post](/the-security-principle-every-attacker-needs-to-follow-905cc94ddfc6), I asked, “How does one discover and abuse new attack paths?” To start answering this question, I made two key arguments:

* Every Attack Path is identity-driven, meaning that it is motivated by, centered around, and strategically guided by the abuse of identity and access management (IAM)
* Every attack path must contain at least one attack vector that abuses a violation of the Clean Source Principle, which dictates that all security dependencies must be as trustworthy as the object being secured.
  To level set, an attack path can be defined as a chain of control relationships with at least one violation of the Clean Source Principle

In this post, I will share a framework I developed for discovering known and unknown attack paths.

## Does Clean Source Violation Necessarily Introduce an Attack Vector?

We’ve already established that attack paths are a chain of control relationships with at least one Clean Source Principle violation, but is the opposite also true? Does every Clean Source violation necessarily create an attack path? Logic suggests the answer is “no”, but let’s see why.

The reason lies in the “control” definition. In our context, we define “control” as a relationship that can contribute to compromising the target resource or impacting its operability. I previously explained that I chose the words “contribute to compromising or impacting” rather than “compromise or impact” because we sometimes need to abuse more than one security dependency to fully compromise or impact the target. For example, if multi-factor authentication (MFA) is enforced on an account, we must abuse both authentication factors to gain control.

Press enter or click to view image in full size

![]()

Therefore, the conclusion was that **a set of one or multiple security dependencies can control a resource that depends on it**. I’ll note that not every control prerequisite is necessarily a security dependency. For example, you need to establish a connection to a remote host/service to control it, but a network connection is not a security dependency and shouldn’t be a security dependency, at least not in $CurrentYear.

## Attack Path Criteria

Two criteria determine whether a set of security dependencies violating the Clean Source Principle introduce an attack path:

* We know how to weaponize the security dependency set to control the dependent resource (or, in other words, we have an attack primitive for abusing it)
* We know that the security dependency set is present in the environment, and the target resource depends on it. To clarify this point, we may learn how to abuse a piece of technology to gain control of resources; however, it does not introduce an attack path if the technology is not used in the environment or the target resources don’t depend on it directly or transitively

I’m not adding the Clean Source violation as a criterion because it is implied and I’ll address it later.

Both criteria are binary, so we can represent security dependencies in a 2x2 matrix:

Press enter or click to view image in full size

![]()

The top left quadrant is where we want to be: both criteria are met, so any Clean Source violation we identify is abusable. Paths BloodHound finds are in that quadrant — that’s the easy part. The challenge is bringing everything else into that quadrant. How do we achieve that?

## Attack Path Discovery Framework

Press enter or click to view image in full size

![]()

## Define Target

There are generally two approaches for discovering attack paths:

* **Analyzing outbound control** — This approach seeks to understand the attacker’s reach given an initial position. I would describe it as exploratory or opportunistic
* **Analyzing inbound control** — This approach seeks to understand the ways to reach a specific resource, backtracking from a given target. I would describe this approach as intentional or objective-oriented

The latter is more suitable for this framework but requires a well-defined target or targets. As attackers, we would derive that from our red team objectives. The former can also serve a purpose, especially earlier on, for gaining situational awareness.

## Map Security Dependencies

Performing reconnaissance, enumeration, and [discovery](https://attack.mitre.org/tactics/TA0007/) helps discover what is present in an environment and identify the target’s direct and transitive security dependencies. This activity represents an upward shift from the bottom quadrants to the top quadrants.

Press enter or click to view image in full size

![]()

The bottom left quadrant represents known tradecraft, which is typically easier to discover. For example, we can run SharpHound and AzureHound to collect and ingest data into BloodHound. BloodHound can’t provide complete coverage of all known offensive tradecraft, so other enumeration tools and discovery techniques must be utilized.

The bottom right quadrant represents unknown tradecraft. It could be commodity, off-the-shelf technologies that we, as operators or as a community, don’t know how to abuse. It could also be proprietary/bespoke technologies for the target organization. Discovering those can be more challenging, as it requires more manual research an...