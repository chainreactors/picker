---
title: Book Review Cloud Forensics Demystified
url: https://bakerstreetforensics.com/2024/10/04/book-review-cloud-forensics-demystified/
source: Instapaper: Unread
date: 2024-10-08
fetch_date: 2025-10-06T18:53:55.851681
---

# Book Review Cloud Forensics Demystified

[Skip to content](#content)

[Baker Street Forensics](https://bakerstreetforensics.com/)

Where Irregulars are part of the Game

Menu

* [Blog](https://bakerstreetforensics.com/blog/)
* [Links, Resources & Swag](https://bakerstreetforensics.com/resources/)

[![](https://bakerstreetforensics.com/wp-content/uploads/2022/05/output-onlinepngtools-4.png)](https://bakerstreetforensics.com/)

# Book Review: Cloud Forensics Demystified

[Forensic Imaging](https://bakerstreetforensics.com/category/forensic-imaging/), [Forensics](https://bakerstreetforensics.com/category/forensics/), [M365](https://bakerstreetforensics.com/category/m365/), [Malware](https://bakerstreetforensics.com/category/malware/), [Memory Analysis](https://bakerstreetforensics.com/category/memory-analysis/), [RAM](https://bakerstreetforensics.com/category/ram/), [Triage](https://bakerstreetforensics.com/category/triage/)

![](https://bakerstreetforensics.com/wp-content/uploads/2024/10/cloud.jpg?w=1024)

At this point, we’ve all heard the expression *‘There is no cloud; It’s just someone else’s computer.’* While there is some truth to that, there are some fundamental differences when it comes to digital forensics when cloud resources are part of the investigation.

![](https://bakerstreetforensics.com/wp-content/uploads/2024/10/cover_image_large.png?w=657)

Recently, I had the chance to read [Cloud Forensics Demystified: Decoding cloud investigation complexities for digital forensic professionals, by Ganesh Ramakrishnan and Mansoor Haqanee](https://a.co/d/8fVlWIX). I received a complimentary this book in exchange for an honest and unbiased review. All opinions expressed are my own.

I’ve been doing DFIR for about 15 years now. In the early days, almost all investigations involved having hands on access to the data or devices being investigated. As I moved into Enterprise Incident Response, it became more and more frequent that the devices I would be investigating would be in a remote location, be it another state – or even another country. As the scope of my investigations grew, so did my techniques need to evolve and adapt.

Cloud Forensics is the next phase of that evolution. While the systems under investigation may still be in another state or country, extra factors come into play like multi-tenancy and shared responsibility models. **Cloud Forensics Demystified** does a solid job of shedding light on those nuances.

The book is divided into three parts.

* Part 1: Cloud Fundamentals
* Part 2: Forensic Readiness: Tools, Techniques, and Preparation for Cloud Forensics
* Part 3: Cloud Forensic Analysis: Responding to an Incident in the Cloud

## Part 1: Cloud Fundamentals

This section provides a baseline knowledge of the three major cloud providers, Amazon Web Services (AWS), Google Cloud Platform (GCP) and Microsoft Azure. It breaks down the different architectural components of each, and how the platforms each handle the functions of virtual systems, networking and storage.

Part 1 also includes a broad yet thorough introduction to the different Cyber and Privacy legislation that come into play for cloud investigations. This section is not only valuable to investigators. Whether you’re a lawyer providing legal counsel for an organization, or responsible for an organizations overall security at a CISO level, this material is beneficial in understanding the challenges and responsibilities that come from hosting your data or systems in the cloud, and the different legislation and regulations that follow those choices.

## Part 2: Forensic Readiness: Tools, Techniques, and Preparation for Cloud Forensics

As with enterprise investigations, logging is often where the hunting for incident indicators begins with telemetry and the correlation of different log sources. This section focuses on the different log sources available in AWS, GCP, and Azure. It also provides a detailed list of log types that are enabled by default and those that require manual activation to ensure that you have access to the most relevant data for your investigations when an incident occurs. This section also covers the different providers offerings for log analysis in the cloud including AWS Cloud Watch, Microsoft Sentinel and Google’s Cloud Security Command Center (Cloud SCC) as examples.

## Part 3: Cloud Forensic Analysis: Responding to an Incident in the Cloud

As an Incident Responder, this was the section I enjoyed the most. While the first two sections are foundational for understanding the architectures of networking and storage, part three provides detailed information on how to acquire evidence for cloud investigations. The section covers both log analysis techniques as well as recommendations for host forensics and memory analysis tools. The book covers the use of commercial forensic suites, like [Magnet Axiom](https://www.magnetforensics.com/products/magnet-axiom-cyber/), as well as open-source tools like [CyLR](https://github.com/orlikoski/CyLR) and [HAWK](https://github.com/T0pCyber/hawk). Besides covering investigations of the three Cloud Service Providers (CSPs), there is also a section covering the cloud productivity services of Microsoft M365 and Google Workspace, as well as a brief section on Kubernetes.

## Summary

Whether you’re a gray-haired examiner like me, or a neophyte in the world of digital forensics, chances are high that if you’re not running investigations in the cloud yet – you will be soon enough.  Preparation is the first step in the Incident Response lifecycle. To properly prepare for incidents you need to know both what sources will be most informative to your investigations, as well as the methodology to capture and process that evidence efficiently.

**Cloud Forensics Demystified** is a comprehensive guide that covers cloud fundamentals, forensic readiness, and incident response. It provides valuable insights into cloud investigation techniques, log analysis, and evidence acquisition for major cloud providers and productivity services. The book is valuable for both experienced and novice digital forensics professionals to prepare for cloud investigations.

### Share this:

* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://bakerstreetforensics.com/2024/10/04/book-review-cloud-forensics-demystified/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://bakerstreetforensics.com/2024/10/04/book-review-cloud-forensics-demystified/?share=reddit)
* [Click to share on Bluesky (Opens in new window)
  Bluesky](https://bakerstreetforensics.com/2024/10/04/book-review-cloud-forensics-demystified/?share=bluesky)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://bakerstreetforensics.com/2024/10/04/book-review-cloud-forensics-demystified/?share=mastodon)

Like Loading...

### *Related*

[October 4, 2024](https://bakerstreetforensics.com/2024/10/04/book-review-cloud-forensics-demystified/) [Doug Metz](https://bakerstreetforensics.com/author/dwmetz/)[AWS](https://bakerstreetforensics.com/tag/aws/), [Azure](https://bakerstreetforensics.com/tag/azure/), [Cloud](https://bakerstreetforensics.com/tag/cloud/), [cloud-computing](https://bakerstreetforensics.com/tag/cloud-computing/), [DFIR](https://bakerstreetforensics.com/tag/dfir/), [GCP](https://bakerstreetforensics.com/tag/gcp/), [Imaging](https://bakerstreetforensics.com/tag/imaging/), [Magnet](https://bakerstreetforensics.com/tag/magnet/), [Malware](https://bakerstreetforensics.com/tag/malware/), [Memory](https://bakerstreetforensics.com/tag/memory/)

## One thought on “Book Review: Cloud Forensics Demystified”

1. Pingback: [Week 40 – 2024 – This Week In 4n6](http://thisweekin4n6.com/2024/10/06/week-40-2024/)

## Leave a comment [Cancel reply](/2024/10/04/book-review-cloud-forensics-demystified/#respond)

Δ

## Post navigation

[Previous Previous post: Beyond Hashes: Simplifying Malware Identification with Python and MpCmdRun](https://bakerstreetforensics.com/2024/09/20/b...