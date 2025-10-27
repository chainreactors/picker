---
title: How I made $64k from deleted files — a bug bounty story
url: https://medium.com/@sharon.brizinov/how-i-made-64k-from-deleted-files-a-bug-bounty-story-c5bd3a6f5f9b
source: Over Security - Cybersecurity news aggregator
date: 2025-07-12
fetch_date: 2025-10-06T23:51:04.930087
---

# How I made $64k from deleted files — a bug bounty story

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc5bd3a6f5f9b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40sharon.brizinov%2Fhow-i-made-64k-from-deleted-files-a-bug-bounty-story-c5bd3a6f5f9b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40sharon.brizinov%2Fhow-i-made-64k-from-deleted-files-a-bug-bounty-story-c5bd3a6f5f9b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# How I made $64k from deleted files — a bug bounty story

[![Sharon Brizinov](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*ige6rmROiTbiYkmz)](/%40sharon.brizinov?source=post_page---byline--c5bd3a6f5f9b---------------------------------------)

[Sharon Brizinov](/%40sharon.brizinov?source=post_page---byline--c5bd3a6f5f9b---------------------------------------)

14 min read

·

Apr 22, 2025

--

24

Listen

Share

**TL;DR** — I built an automation that cloned and scanned tens of thousands of public GitHub repos for leaked secrets. For each repository I restored deleted files, found dangling blobs and unpacked *.pack* files to search in them for exposed API keys, tokens, and credentials. Ended up reporting a bunch of leaks and pulled in around $64k from bug bounties 🔥.

## Outline

* Background
* Git internals
* Collecting Targets
* Building the Automation
* Findings & Payments
* Summary

## Background

My name is [Sharon Brizinov](https://www.linkedin.com/in/sharonbrizinov/), and while I usually focus on low-level vulnerability and exploitation research in OT/IoT devices, I occasionally dive into bug bounty hunting.

Many researchers in the bugbounty space look for leaked secrets, often scanning GitHub repositories for exposed credentials. This approach isn’t new, but I wanted to explore a different angle-recovering secrets from allegedly deleted files. Developers often forget that Git history retains everything, even after files are removed from the working directory.

To test this, I scanned tens of thousands of repositories from thousands of companies, searching for sensitive information hidden in past commits. The results were alarming-I discovered numerous deleted files containing API tokens, credentials, and even active session tokens that had not been revoked. Reporting these findings led to significant security improvements for the affected companies, and in the end, I earned a total of $64,350 in bug bounty rewards.

In this blog I will try to describe my journey from collecting all the Github repositories, building the automation, and finding & reporting on leaking secrets.

## Git internals

*First thing first, I highly recommend reading* [*How git Internally works*](https://octobot.medium.com/how-git-internally-works-1f0932067bee) *by Octobot. It’s a great easy-to-read resource to understand better git.*

Git is a distributed version control system that tracks changes in files and allows multiple developers to collaborate on a project. It maintains a complete history of all changes, enabling users to revert to previous states, branch off for feature development, and merge changes efficiently. At its core, Git operates as a content-addressable filesystem where each version of a file is stored as a unique object in a repository.

Everything Git tracks (files, folders, commits, etc.) is stored as an **object**, identified by its **SHA-1 or SHA-256 hash** (depending on config).

There are four object types in Git:

* **Blob** → File content
* **Tree** → Directory structure
* **Commit** → Snapshot + metadata
* **Tag** → Annotated tag object

**Git Blobs and Packs**

A **blob** (binary large object) is how Git stores the **content of a file**, *without any filename or path info*. When Git first stores an object, it writes it as a “*loose object”*, like this:

```
.git/objects/ab/cdef1234567890...
```

Where *ab* is the first 2 hex characters of the SHA and *cdef1234567890…* is the rest. The binary data stored inside is a zlib-compressed data that corresponds to a single file.

To optimize storage and performance, Git periodically (loose objects ≥ 6700 by defualt) compresses many loose objects into a pack file:

```
.git/objects/pack/pack-<hash>.pack
```

*.pack* files are complex beasts with very [interesting structure](https://www.alibabacloud.com/blog/597391). Luckily we don’t really need to fully understand how it is constructed, since we can use *git-unpack-objects* to unpack any *.pack* file.

![]()![]()

How to identify pack and blob files: 50 41 43 4B — PACK | 78 01 — start of a zlib compressed blob (images taken using [HexShare](https://hex.pov.sh/))

Sometimes unreferenced objects (aka dangling objects) will be created in our git repository. These are valid but unreferenced objects (commits, blobs, trees, or tags) that remain in the `.git/objects/` directory but are no longer reachable from any branch, tag, stash, or reflog. They are typically created when history is rewritten (for example by doing `git commit --amend`, `rebase`, `reset`, or branch deletion), leaving old objects behind. Although not part of the active history, Git retains them temporarily (by default, 2 weeks) for potential recovery. You can find them using `git fsck --dangling`

**Git Commit History**

Each commit in Git represents a snapshot of the repository at a given point in time. Commits are immutable and are identified by a SHA-1/SHA-256 hash. They store:

* A reference to a tree object, which represents the file structure at that commit.
* Pointers to parent commits, forming a directed acyclic graph (DAG) of repository history.
* Metadata, including the author, timestamp, and commit message.

Git stores commits efficiently using delta compression, meaning it only records changes rather than full copies of files.

Press enter or click to view image in full size

![]()

Commit — tree — blob relationship (Image taken from [here](https://thecustomizewindows.com/2014/07/add-web-interface-git-repository-shared-hosting/))

**Deleted Files and Why They Can Be Recovered**
When a file is deleted using *git rm* or simply removed from the working directory and committed, it disappears from the latest snapshot but still exists in the repository’s history. This happens because:
- *Git Commit History is Immutable*: Once a commit is created, its data is stored in *.git/objects* and remains there even if it’s no longer referenced by any branch or tag. Unreferenced (dangling) objects aren’t removed immediately — they’re typically retained for around two weeks before being eligible for garbage collection.
- *References (Refs) Keep Objects Alive*: Git maintains references in the heads, tags and remotes directories, so even if a file is removed in a later commit, older commits (=*trees*) still contain the file.

To completely remove a file from history, one must rewrite history using tools like [git filter-branch](https://git-scm.com/docs/git-filter-branch), [*git-filter-repo*](https://github.com/newren/git-filter-repo) or by manually rebasing and running garbage collector (with prune) to clear unreachable objects — good luck with that. However, if the repository is public, the file may already be copied or cloned elsewhere so finding and r...