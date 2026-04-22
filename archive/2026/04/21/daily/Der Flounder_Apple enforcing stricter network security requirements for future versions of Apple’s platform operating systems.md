---
title: Apple enforcing stricter network security requirements for future versions of Apple’s platform operating systems
url: https://derflounder.wordpress.com/2026/04/21/apple-enforcing-stricter-network-security-requirements-for-future-versions-of-apples-platform-operating-systems/
source: Der Flounder
date: 2026-04-21
fetch_date: 2026-04-22T04:39:10.560825
---

# Apple enforcing stricter network security requirements for future versions of Apple’s platform operating systems

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [iOS](https://derflounder.wordpress.com/category/ios/), [iPadOS](https://derflounder.wordpress.com/category/ipados/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [PKI](https://derflounder.wordpress.com/category/pki/), [tvOS](https://derflounder.wordpress.com/category/tvos/), [visionOS](https://derflounder.wordpress.com/category/visionos/), [watchOS](https://derflounder.wordpress.com/category/watchos/) > Apple enforcing stricter network security requirements for future versions of Apple’s platform operating systems

## Apple enforcing stricter network security requirements for future versions of Apple’s platform operating systems

April 21, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

Apple released a new KBase article on April 21st 2026, where the intended audience is IT admins and device management service developers. (For device management service developers, these are the vendors and other folks who [build MDM servers](https://www.jamf.com/blog/what-is-apple-mdm-server/).) The KBase article is available via the link below:

<https://support.apple.com/126655>

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-21-at-9.57.png?w=599&h=386 "Screenshot 2026-04-21 at 9.57.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2026/04/screenshot-2026-04-21-at-9.57-1.png?w=599&h=386 "Screenshot 2026-04-21 at 9.57.png")

For more details, please see below the jump.

The key parts of Apple’s guidance are the following:

**When is it happening?**

In a future version of Apple’s various OS platforms, which include iOS, iPadOS, macOS, watchOS, tvOS, and visionOS, Apple is going to be enforcing stricter controls on [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS) connections. (These connections may also be referred to as [Secure Sockets Layer](https://en.wikipedia.org/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0) (SSL) connections, as SSL is the now-deprecated technology that TLS was built on.)

This change could come as soon as the next major operating system release, which would mean the following operating systems:

* iOS 27
* iPadOS 27
* macOS 27
* watchOS 27
* tvOS 27
* visionOS 27

This does not necessarily mean that this change will be happening once those future operating systems have been released, but Apple is saying that it may happen at that time or at a later point in the future.

**What’s affected?**

* Mobile device management (MDM)
* Declarative Device Management (DDM)
* Automated Device Enrollment
* Configuration profile installation
* App installation, including enterprise app distribution
* Software updates

What’s that all mean? If I’m interpreting it correctly, it means that the tighter controls on TLS connections are going to be for communication between Apple devices and the following:

* MDM servers
* Apple’s Automated Device Enrollment service (part of Apple Business and Apple School Manager)
* Apple’s app deployment services
* Apple’s software update service

Apple is also explicitly saying there will be some exceptions to these tighter security controls. These exceptions are:

* Network connections to a [Simple Certificate Enrollment Protocol](https://en.wikipedia.org/wiki/Simple_Certificate_Enrollment_Protocol) (SCEP) server
* Network connections to an [Apple content caching server](https://support.apple.com/en-gb/guide/deployment/depde72e125f/web)

For those not familiar with SCEP, SCEP servers are intermediaries that sit between a certificate authority which issues digital certificates and the devices which use those digital certificates. In many enterprise environments which issue digital certificates to devices, an MDM server communicates with a SCEP server to get digital certificates for the devices the MDM server is managing, then provides those certificates to the devices which the MDM server is managing by putting the certificate in a [configuration profile](https://support.apple.com/en-au/guide/mac-help/mh35561/mac), then delivering that configuration profile using an [MDM command](https://support.apple.com/guide/deployment/dep789n2k1qp/web).

Meanwhile, content caching servers are Apple’s solution which allows one device on your network to download Apple updates once and then share them locally with other devices. If there is a content caching server active on your local network, it is effectively a local copy of Apple’s software update servers which is available on your local network and allows you to save bandwidth by having your devices get their updates from that local copy in place of each device individually downloading their updates over the Internet from Apple’s software update service.

I don’t know why these exceptions for SCEP and content caching servers have been made, but my assumption is that Apple examined what would be involved in making these two exceptions also have to comply with the new standards and concluded that it either wasn’t possible or operationally too difficult at this time.

**What’s changing?**

Affected servers and services must:

* Support TLS 1.2 or later
* Use ATS-compliant ciphersuites
* Present valid certificates that meet ATS standards

OK, what’s all that mean? First, let’s talk about the requirement to enforce TLS 1.2 and later. TLS and the earlier SSL have gone through various versions, with cryptographic strength increasing and bugs being fixed in each new version. To summarize why Apple is requiring TLS 1.2 and later, it’s because older versions of TLS and the older SSL supported communicating using weaker encryption methods which are not supported in TLS 1.2 and later and were subject to vulnerabilities that TLS 1.2 and later are not vulnerable to. By mandating TLS 1.2 and later, Apple is closing off those vulnerabilities and weaker encryption methods by rejecting connections which continue to use these prior versions of SSL and TLS. For those who want to dig deeper into this topic, please see the links below:

<https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/>
<https://www.ncsc.gov.uk/guidance/using-tls-to-protect-data>
<https://blog.gigamon.com/2021/07/14/what-is-tls-1-2-and-why-should-you-still-care/>
<https://www.statuscake.com/kb/knowledge-base/why-you-should-still-use-tls1-2-and-not-just-tls1-3/>

Next, what the heck is ATS? In this case, it’s [App Transport Security](https://developer.apple.com/documentation/Security/preventing-insecure-network-connections) (ATS). ATS is a network security feature developed by Apple for its platforms, which mandates that network connections meet certain standards or ATS blocks them. ATS has been used to secure network communication for apps and app extensions. Now with this advisory being published, it looks like Apple is now extending ATS to secure communication between devices and MDM servers along with Apple’s app deployment, Automated Device Enrollment and software update services. So what is ATS requiring?

First, ATS is checking the TLS certificate provided by an MDM server or Apple’s affected services. This certificate must meet the following requirements:

* Have an intact digital signature (this tells ATS that the certificate hasn’t been tampered with.)
* Be unexpired (this tells ATS that the certificate is still within the date range prior to the certificate expiring.)
* Certificate’s subject name matches the DNS name of the server in question
* Has a valid certificate chain (where ATS can verify that the certificate it’s examining was signed by another valid certificate, which may be ...