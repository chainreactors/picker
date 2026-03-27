---
title: Policy as Code: Stop Writing Policies and Start Compiling Them
url: https://trustedsec.com/blog/policy-as-code-stop-writing-policies-and-start-compiling-them
source: TrustedSec
date: 2026-03-26
fetch_date: 2026-03-27T04:33:05.088777
---

# Policy as Code: Stop Writing Policies and Start Compiling Them

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

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
* [Policy as Code: Stop Writing Policies and Start Compiling Them](https://trustedsec.com/blog/policy-as-code-stop-writing-policies-and-start-compiling-them)

March 26, 2026

# Policy as Code: Stop Writing Policies and Start Compiling Them

Written by
Martin Bos

Policy Development

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PolicyAsCode_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1774368780&s=2ca90ada7140f51420a8cd89704f4d37)

Table of contents

* [The Idea: If We Can Version-Control Code, Why Not Policy?](#Idea)
* [The Build System](#Build)
* [The Scale: 47 Policies, 3 Series, 1 Standard Format](#Scale)
* [Framework Alignment](#Framework)
* [The AI Angle: How This Was Actually Feasible](#AI)
* [The Audit Program](#Audit)
* [What Actually Changed](#Changed)
* [What's Next](#Next)
* [The Takeaway](#Takeaway)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#c7f8b4b2a5ada2a4b3fa84afa2a4ace2f5f7a8b2b3e2f5f7b3afaeb4e2f5f7a6b5b3aea4aba2e2f5f7a1b5a8aae2f5f793b5b2b4b3a2a394a2a4e2f5f6e1a6aab7fca5a8a3befa97a8abaea4bee2f5f7a6b4e2f5f784a8a3a2e2f486e2f5f794b3a8b7e2f5f790b5aeb3aea9a0e2f5f797a8abaea4aea2b4e2f5f7a6a9a3e2f5f794b3a6b5b3e2f5f784a8aab7aeabaea9a0e2f5f793afa2aae2f486e2f5f7afb3b3b7b4e2f486e2f581e2f581b3b5b2b4b3a2a3b4a2a4e9a4a8aae2f581a5aba8a0e2f581b7a8abaea4beeaa6b4eaa4a8a3a2eab4b3a8b7eab0b5aeb3aea9a0eab7a8abaea4aea2b4eaa6a9a3eab4b3a6b5b3eaa4a8aab7aeabaea9a0eab3afa2aa "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpolicy-as-code-stop-writing-policies-and-start-compiling-them "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Policy%20as%20Code%3A%20Stop%20Writing%20Policies%20and%20Start%20Compiling%20Them%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpolicy-as-code-stop-writing-policies-and-start-compiling-them "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpolicy-as-code-stop-writing-policies-and-start-compiling-them&mini=true "Share on LinkedIn")

## The Problem Nobody Wants to Talk About

Let me paint a picture most security leaders will recognize.

You have 30+ policies living as Word documents on SharePoint. Half of them have filenames like ***Acceptable\_Use\_Policy\_FINAL\_v3\_revised\_FINAL.docx***. Nobody is confident which version is current. The formatting is different in every document because six (6) different people authored them over four (4) years. Cross-references say things like "see the other policy" without specifying which one or which version.

Annual review time rolls around. Someone downloads all the docs, opens each one in Word, makes tracked changes, emails them to a reviewer, waits, gets them back, accepts changes, re-uploads. Repeat for every policy. The whole cycle eats weeks of billable time from people whose time is not cheap.

And then an auditor asks: "When was this policy last reviewed? Can you show me the change history?" And you're digging through SharePoint version history hoping the metadata is intact, knowing it probably isn't.

That was us. A company that does security for a living, and our own policy management was a mess. Not because anyone was lazy, but because Word docs on a shared drive is a fundamentally broken model for managing living documents. The tooling fights you at every step.

## The Idea: If We Can Version-Control Code, Why Not Policy?

The idea was simple and maybe obvious in hindsight: treat policies like source code:

* Markdown files in a Git repository
* YAML front matter for metadata (policy number, revision, date, reviewer, approver)
* A standard structure enforced across every document
* GitLab merge requests for review workflows
* CI/CD to generate output

Here's what that looks like in practice. Every policy starts with front matter like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PolicyAsCode_Martin/Fig01_Martin_PolicyAsCode.png?w=320&q=90&auto=format&fit=max&dm=1774298157&s=95b4938df4d5c44c1ed90f3d36903cb2)

Figure 1 - Example policy front matter defining metadata such as policy number, revision, ownership, and approval details.

Pandoc reads this metadata and injects it into the PDF template's header block. The body is plain Markdown—no proprietary format, no binary blobs, no lock files.

The contribution workflow is the same merge request process our engineers already know:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PolicyAsCode_Martin/Fig02_Martin_PolicyAsCode.png?w=320&q=90&auto=format&fit=max&d...