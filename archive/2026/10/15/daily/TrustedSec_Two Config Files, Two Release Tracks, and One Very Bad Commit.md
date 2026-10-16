---
title: Two Config Files, Two Release Tracks, and One Very Bad Commit
url: https://trustedsec.com/blog/two-config-files-two-release-tracks-and-one-very-bad-commit
source: TrustedSec
date: 2026-10-15
fetch_date: 2026-10-16T06:37:34.187566
---

# Two Config Files, Two Release Tracks, and One Very Bad Commit

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
* [Two Config Files, Two Release Tracks, and One Very Bad Commit](https://trustedsec.com/blog/two-config-files-two-release-tracks-and-one-very-bad-commit)

October 15, 2026

# Two Config Files, Two Release Tracks, and One Very Bad Commit

Written by
Justin Bollinger

Password Audits
Penetration Testing
Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/TwoConfigFilesReleaseTracksPart3_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1791203040&s=d424fd683df0f3c4c2a290b622344b69)

Table of contents

* [Your Config is Now Two Files](#Config)
* [The Local Model that Wasn't Local](#Local)
* [Eight Flags that Remember](#Flags)
* [Can You Trust the Tags?](#Trust)
* [The Name on PyPI is a Trap](#Trap)
* [Tests That Could Not Fail](#Fail)
* [Where to Start](#Where)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#4f703c3a2d252a2c3b720c272a2c246a7d7f203a3b6a7d7f3b27263c6a7d7f2e3d3b262c232a6a7d7f293d20226a7d7f1b3d3a3c3b2a2b1c2a2c6a7d7e692e223f742d202b36721b38206a7d7f0c20212926286a7d7f0926232a3c6a7d0c6a7d7f1b38206a7d7f1d2a232a2e3c2a6a7d7f1b3d2e2c243c6a7d0c6a7d7f2e212b6a7d7f00212a6a7d7f192a3d366a7d7f0d2e2b6a7d7f0c202222263b6a7c0e6a7d7f273b3b3f3c6a7c0e6a7d096a7d093b3d3a3c3b2a2b3c2a2c612c20226a7d092d2320286a7d093b3820622c2021292628622926232a3c623b3820623d2a232a2e3c2a623b3d2e2c243c622e212b6220212a62392a3d36622d2e2b622c202222263b "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ftwo-config-files-two-release-tracks-and-one-very-bad-commit "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Two%20Config%20Files%2C%20Two%20Release%20Tracks%2C%20and%20One%20Very%20Bad%20Commit%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Ftwo-config-files-two-release-tracks-and-one-very-bad-commit "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ftwo-config-files-two-release-tracks-and-one-very-bad-commit&mini=true "Share on LinkedIn")

*Part 3 of 3. [Part 1](https://trustedsec.com/blog/whats-new-in-hate-crack-since-2-0) is the reference for every attack and feature added to hate\_crack since 2.0. [Part 2](https://trustedsec.com/blog/hashcatrosetta-reading-the-rosetta-stone-of-password-cracking) is the deep dive into HashcatRosetta. This post is the plumbing: where configuration lives now and why it moved, how releases get cut, and the afternoon I pushed my private notes to a public repository.*

## Story Time

On July 30, a `prek` pre-push hook corrupted my git index.

The mechanism is a stash and restore cycle. The hook stashes your working tree so the checks run against what you're actually pushing, then restores it afterward. When that cycle went wrong, the index it handed back was not the index I'd built. The commit that came out of it deleted 85,280 lines across roughly 165 files and staged a pile of gitignored, local-only paths: `CLAUDE.md`, `.claude/`, `docs/plans/`, `docs/superpowers/`.

Those paths were not gitignored by accident. I purged them from this repository's history on July 25, five days earlier, specifically because `trustedsec/hate_crack` is public and those files are my working notes.

It reached the public remote before I force-pushed it away.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/hate-crack_Bollinger/Fig01_Bollinger_h-c-config-tags.png?w=320&q=90&auto=format&fit=max&dm=1790884353&s=a151d2b472863ffe199d9d33a8bdcc7a)

The Call is Coming From Inside the House

The part that stings is how little was standing in the way. `detect-private-key` was the only secret-scanning gate in the whole project, and it does not look at any of this. CI had nothing at all. The publication boundary existed in a `.gitignore` file and in my head, and `git add -f` walks straight past the first one.

So, the boundary is enforced at commit time now, by two scripts in `.github/scripts/`.

`check-publication-boundary.sh` refuses any commit that adds or modifies one of those paths. The important detail is that it reads the staged changeset out of the index with `git diff --cached --name-only --diff-filter=ACMRT` rather than consulting `.gitignore`, because forcing past `.gitignore` is precisely the failure mode it exists to catch. Deletions stay allowed, so an accidentally tracked boundary file can still be removed. There is no override, and that's deliberate.

`check-mass-deletion.sh` aborts any commit deleting more than 50 tracked files. No commit in the last 400 in this repository's history deleted more than one, so 50 sits two orders of magnitude above real work while still catching a whole-tree wipe. When you genuinely mean it, `HATE_CRACK_ALLOW_MASS_DELETE=1` is the escape hatch, and it's the right one to reach fo...