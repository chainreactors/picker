---
title: Apple’s Verified Photography System
url: https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html
source: Instapaper: Unread
date: 2026-10-07
fetch_date: 2026-10-08T08:08:22.581328
---

# Apple’s Verified Photography System

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Apple’s Verified Photography System

Apple just [released](https://security.apple.com/blog/apple-reference-image/) a system called “Reference Image.” It can verify the image is exactly as taken by an iPhone—new models only—without tying it to a specific iPhone or photographer. It can also verify that multiple images came from the same iPhone.

> Other industry solutions require a photographer or institution to vouch for an image using their own credentials. We are concerned this puts some photographers, such as those operating in conflict zones, in a difficult position; it should not be necessary to forgo anonymity in order to prove image authenticity. We built Apple Reference Image to avoid using an explicit, public credential for photographers, and to avoid even implicit public association between different photos taken by the same sensor. The final reference image is instead signed by Apple’s signing service, after validation by PCC. That signature is backed by Apple’s strongest technical guarantees.
>
> Our implementation also protects the confidentiality of the image itself, including from Apple. Merely capturing a reference image should never expose the actual pixels to Apple or anyone else. We achieve this through the exceptional privacy properties of PCC—the nodes themselves are architected so that not even Apple can access image data, just as Apple cannot see the information processed for Apple Intelligence in PCC. While the revocation service must maintain a private record of photo GUIDs and associated sensors to allow for revocation, it never has access to the image data, and does not allow for public access to this record. And as final revocation checks occur using on-device lists, a device never reveals to anyone which photo it’s looking at in order to find out whether it’s still valid.

The report makes for good reading; the details are interesting.

Tags: [Apple](https://www.schneier.com/tag/apple/), [authentication](https://www.schneier.com/tag/authentication/), [cameras](https://www.schneier.com/tag/cameras/), [reports](https://www.schneier.com/tag/reports/)

[Posted on October 7, 2026 at 7:07 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html) •
[18 Comments](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html#comments)

### Comments

alnm •
[October 7, 2026 8:24 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458774)

So instead of “photographer or institution to vouch[ing] for an image using their own credentials”, Apple will vouch for the image after you upload it to their servers. Ok then.

[Chris Boyle](https://chris.boyle.name) •
[October 7, 2026 9:00 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458776)

“It can also verify that multiple images came from the same iPhone.”

The report seems to state the opposite: “Privacy preservation: an outside observer cannot determine whether any pair of reference images were taken by the same device”. And later “If a device is later found to be compromised, its images can be revoked and flagged retroactively, without revealing which images came from the same sensor.”

(It also mentions checks that a sensor and an SEP are from the same device.)

Dave Sanford •
[October 7, 2026 9:31 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458777)

Unless I missed something, they could do all this with C2PA (<https://c2pa.org/>). Using an open standard would provide various benefits, including interoperability.

TimH •
[October 7, 2026 9:34 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458778)

There are two competing use cases:

1. Whistleblower wants to submit a photograph with no
   evidence linking them to the photograph. Also, hard evidence that the picture is exactly as taken by the camera without editing. Editing includes the photograph “improving” that cameras nowadays are wont to do. Just the sensor capture.
2. Copyright holder wants to submit a photograph with hard evidence that they own the rights. This is hard evidence that the picture is as taken and stored by a specific camera including merging multiple shots and other on-camera editing.

KC •
[October 7, 2026 11:09 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458780)

@ Dave Sanford

At early review, this feature appears to split image provenance into two strictly isolated phases.

1. Create a secure digital negative on device
2. Develop it inside Private Cloud Compute

Here’s a guide on how to opt-in as well as develop a reference image:

<https://support.apple.com/en-us/128064>

KC •
[October 7, 2026 11:10 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458781)

From Apple on sharing photos:

“If you share a Reference mode photo before reference image has been developed, it may include sensitive information about your device, such as the serial number, and the full image frame regardless of the zoom setting at capture.”

Also, does anyone know if you can develop the negative more than once?

Grumpy Old Coot •
[October 7, 2026 11:26 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458782)

“If a device is later found to be compromised, its images can be revoked and flagged retroactively, without revealing which images came from the same sensor.” And scarily, what prevents this being ‘hijacked’ to cause data to disappear? “This device was compromised” -> “This device belongs to a journalist. Let’s compromise it and invalidate all evidence.’

freedom •
[October 7, 2026 11:55 AM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458783)

What this means is that now the image sensors are backdoored as well.

This is another victory of the GCHQ-NSA-corporate mafia, a child-murdering mafia.

Rontea •
[October 7, 2026 12:20 PM](https://www.schneier.com/blog/archives/2026/10/apples-verified-photography-system.html/#comment-458785)

Fascinating move by Apple with their Reference Image system. This is a classic example of end-to-end thinking in both security and privacy. They’re not just slapping a signature on an image—they’re building a chain of trust from the sensor silicon, through cryptographic attestation, and into a privacy-preserving compute environment.

From a defensive standpoint, I like the layered approach: hardware-secured pixel capture, Secure Enclave attestation, cryptographic timestamps, and PCC for verifiable image development. The post-quantum signature step is forward-leaning, acknowledging that content authenticity needs to survive decades of adversarial advances.

The revocation ...