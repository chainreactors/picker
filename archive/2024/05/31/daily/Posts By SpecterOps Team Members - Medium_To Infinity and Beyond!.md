---
title: To Infinity and Beyond!
url: https://posts.specterops.io/to-infinity-and-beyond-feab2d8ff93c?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-05-31
fetch_date: 2025-10-06T16:52:34.412624
---

# To Infinity and Beyond!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffeab2d8ff93c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fto-infinity-and-beyond-feab2d8ff93c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fto-infinity-and-beyond-feab2d8ff93c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-feab2d8ff93c---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-feab2d8ff93c---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# To Infinity and Beyond!

[![Luke Paine](https://miro.medium.com/v2/resize:fill:64:64/0*mDdi7Cpda086t25h.jpg)](https://medium.com/%40v3r5ace?source=post_page---byline--feab2d8ff93c---------------------------------------)

[Luke Paine](https://medium.com/%40v3r5ace?source=post_page---byline--feab2d8ff93c---------------------------------------)

11 min read

·

May 30, 2024

--

1

Listen

Share

Increasing our understanding of EDR capabilities in the face of impossible odds.

Press enter or click to view image in full size

![]()

## Introduction

I recently had a discussion with our chief strategist,

[Jared Atkinson](https://medium.com/u/b206c297df42?source=post_page---user_mention--feab2d8ff93c---------------------------------------)

, about purple teaming. We believe that large quantities of procedures per technique affect the overall success of the assessment and I began to theorize how I could prove this concept. In this post, I will discuss the validation of my theory.

## You know what assumptions do…

When you take a technique and make a broad statement of detection, you are often ignoring orders of magnitude more detail; forcing those who view it to make a broad assumption about what is and is not detected. Take this hypothetical EDR marketing:

Press enter or click to view image in full size

![]()

While some portions of this example are purely satirical, this still seems great! We have four different techniques that are detected! But is this the full story? If you have been following Jared Atkinson’s posts, you may realize that each of these techniques look something like this:

Press enter or click to view image in full size

![]()

This is a set of operation chains for different procedures of process injection. If you are unfamiliar with what operation chains are, I recommend reading Jared’s blog series on [Tactical to Functional](/on-detection-from-tactical-to-functional-1349e51e1a03). Using this information, I asked myself, “How could I build a representation of my understanding of the EDR’s capabilities with respect to process injection?”

EDR capabilities can, and should, be measured as a set of data. Our industry has different methods of measuring capabilities and representing the resulting data. Common examples that are used for measurement include MITRE [ATT&CK Evaluations](https://attackevals.mitre-engenuity.org/), or generically mapping the MITRE ATT&CK framework to testing performed via something like [Atomic Red Team](https://atomicredteam.io/). The problem with evaluations of this type are that they typically focus on one variation of a technique, which can only represent one procedure. While usually not explicitly stated, those using those projects often mistake the results for full “coverage” of that technique. The reality is that none of these approaches are designed to be used or interpreted in this fashion.

The argument I am going to make throughout this post is that these tests are not particularly sufficient to guarantee coverage. In fact, *no amount of testing will ever guarantee 100% coverage of any given technique*. This does not mean all hope is lost of detecting the use of process injection, but it does mean that we need to better understand what our testing results actually mean — so at least we have knowledge of the potential gaps prior to accepting the risk.

## EXCELerating Capability Testing

To start proving my argument, let’s start in Excel. We will build a table that represents a set of process injection procedures that an EDR may detect. The columns will represent the individual procedures while the rows will represent each possible combination of procedures an EDR may detect. We will treat a 0 as “not detected” and a 1 as “detected”.

For this first example, I will limit the procedures to “Standard” (e.g., shellcode injection) and “Thread Hijacking.” I am going to say, for the sake of argument, that these are the only two known forms of process injection. This means that there are four possibilities for an EDR’s capability to detect process injection. At this point, without running any tests, an end user of an EDR will have no idea which of the four outcomes is true for their EDR.

Press enter or click to view image in full size

![]()

We can safely rule out some of these outcomes because we assume that an EDR is detecting *at least* one of these procedures to make the claim that it detects process injection. Let’s say that the most likely candidate for detection is standard shellcode injection since that is the canonical form that comes to mind when process injection is mentioned.

If we know that standard injection is detected with our theoretical EDR, then we now have two potential cases, albeit in our hypothetical world where there are only two known forms of process injection. We can show this on the chart by graying out the rows that are not relevant to our EDR.

Press enter or click to view image in full size

![]()

The chart shows that by either testing or seeing real-world examples of an EDR detecting a given procedure, we removed 50% of the *possible combinations* of process injection procedures the EDR can potentially detect.

I want to be clear here — this is not a *probability* that an EDR will detect a given technique, or a full *coverage* of the EDR capabilities. This is merely filling in 50% of our *understanding* of an EDR’s capability regarding a specific technique using known procedures for that technique. I am going to continue stressing this throughout this post. All of these statistics are applicable to better understanding an EDR, but none of the table entries are weighted to convey the prevalence or any other attribute of a procedure.

Let’s add a third procedure and see what happens to our potential capability.

Press enter or click to view image in full size

![]()

We are dealing with exponential math here. There are two states that our data can be in (0 or 1), so the number of potential combinations of procedures from the table that an EDR can detect is n^x , where “n” is the number of potential results and “x” is the number of procedures. So the table above can be represented as 2³ or 8....