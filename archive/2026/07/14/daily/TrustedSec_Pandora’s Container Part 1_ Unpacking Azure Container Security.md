---
title: Pandora’s Container Part 1: Unpacking Azure Container Security
url: https://trustedsec.com/blog/pandoras-container-part-1-unpacking-azure-container-security
source: TrustedSec
date: 2026-07-14
fetch_date: 2026-07-15T04:49:30.692337
---

# Pandora’s Container Part 1: Unpacking Azure Container Security

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Pandora’s Container Part 1: Unpacking Azure Container Security](https://trustedsec.com/blog/pandoras-container-part-1-unpacking-azure-container-security)

July 14, 2026

# Pandora’s Container Part 1: Unpacking Azure Container Security

Written by
Justin Mahon

Cloud Penetration Testing
Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PandorasContainerP1_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1783689414&s=f59e523a8075b6cbd850b3663cf112f2)

Table of contents

* [Container Registries](#Registries)
* [Identifying Roles and Registries](#Identifying)
* [Checking if Admin User is Enabled](#checking)
* [Enabling Admin User & Retrieving Passwords](#Enabling)
* [Pushing, Pulling and Tagging](#PPT)
* [Dissecting Docker Images](#Dissecting)
* [Modifying a Task With a Managed Identity](#Modifying)
* [Creating a Malicious YAML File](#Creating)
* [Running the Task](#Running)
* [Token Keys and Scope Maps](#Maps)
* [Creating a Token](#Token)
* [Change Image](#Change)
* [“How it’s Supposed to Work”](#How)
* [My Method for Exfiltration](#Method)
* [Building a Custom Dockerfile](#Building)
* [Restart the Container With the Modified Image](#Restart)
* [Exfil to Listener With ngrok](#Exfil)
* [Reverse Shell With ngrok](#Reverse)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#c6f9b5b3a4aca3a5b2fb85aea3a5ade3f4f6a9b3b2e3f4f6b2aeafb5e3f4f6a7b4b2afa5aaa3e3f4f6a0b4a9abe3f4f692b4b3b5b2a3a295a3a5e3f4f7e0a7abb6fda4a9a2bffb96a7a8a2a9b4a7e383f4e3fef6e3ffffb5e3f4f685a9a8b2a7afa8a3b4e3f4f696a7b4b2e3f4f6f7e3f587e3f4f693a8b6a7a5adafa8a1e3f4f687bcb3b4a3e3f4f685a9a8b2a7afa8a3b4e3f4f695a3a5b3b4afb2bfe3f587e3f4f6aeb2b2b6b5e3f587e3f480e3f480b2b4b3b5b2a3a2b5a3a5e8a5a9abe3f480a4aaa9a1e3f480b6a7a8a2a9b4a7b5eba5a9a8b2a7afa8a3b4ebb6a7b4b2ebf7ebb3a8b6a7a5adafa8a1eba7bcb3b4a3eba5a9a8b2a7afa8a3b4ebb5a3a5b3b4afb2bf "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpandoras-container-part-1-unpacking-azure-container-security "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Pandora%E2%80%99s%20Container%20Part%201%3A%20Unpacking%20Azure%20Container%20Security%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpandoras-container-part-1-unpacking-azure-container-security "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpandoras-container-part-1-unpacking-azure-container-security&mini=true "Share on LinkedIn")

Containers have become a foundational component of modern Azure environments. However, the attack surface introduced by services such as container registries, container apps, container instances, and container jobs is often underexplored. This blog series examines common attack techniques targeting Azure container services, including registries, secrets, jobs, keys, container instances, and container apps.

During testing, I found that a standard reverse shell approach for container image replacement did not work reliably. I developed an alternative technique that embeds IMDS token theft and secret exfiltration directly into a Dockerfile's entrypoint, eliminating the need for a persistent reverse shell connection.

Again, another shoutout to the [AzRTE course by HackTricks](https://hacktricks-training.com/courses/azrte/) for their amazing content. The course covered a lot of material and helped me understand Azure container security, identity abuse, and more.

## Pre-Requisites

This blog assumes you at least have reader rights over the container assets.  I have included a link to my GitHub repo with scripts you can run from CloudShell to enumerate these permissions.

<https://github.com/OffsecPierogi/Azure>

The following permissions are used for this demo:

* Microsoft.ContainerRegistry/registries/read
* Microsoft.ContainerRegistry/registries/write
* Microsoft.ContainerRegistry/registries/listCredentials/action
* Microsoft.ContainerRegistry/registries/pull/read
* Microsoft.ContainerRegistry/registries/push/write
* Microsoft.ContainerRegistry/registries/tasks/read
* Microsoft.ContainerRegistry/registries/tasks/write
* Microsoft.ContainerRegistry/registries/runs/write
* Microsoft.ContainerRegistry/registries/tokens/read
* Microsoft.ContainerRegistry/registries/tokens/write
* Microsoft.ContainerRegistry/registries/scopeMaps/write
* Microsoft.ContainerInstance/containerGroups/restart/action
* Microsoft.ContainerInstance/containerGroups/write
* Microsoft.ContainerRegistry/registries/generateCredentials/action

The following built-in roles in Azure RBAC have all or some of these permissions assigned to them by default.

* Owner
* Contributor
* AcrPull
* AcrPush

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PandorasContainer_Mah...