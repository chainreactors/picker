---
title: When a Single Text File Breaks a Trust Boundary (Bug Bounty writeup)
url: https://infosecwriteups.com/when-a-single-text-file-breaks-a-trust-boundary-bug-bounty-writeup-824c1e2dc9f0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-30
fetch_date: 2026-08-31T07:52:20.624884
---

# When a Single Text File Breaks a Trust Boundary (Bug Bounty writeup)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-a-single-text-file-breaks-a-trust-boundary-bug-bounty-writeup-824c1e2dc9f0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-a-single-text-file-breaks-a-trust-boundary-bug-bounty-writeup-824c1e2dc9f0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-824c1e2dc9f0---------------------------------------)

·

1. [The Feature](/?source=post_page-----824c1e2dc9f0---------------------------------------#e02f "The Feature")
2. [A Missing Validation Step](/?source=post_page-----824c1e2dc9f0---------------------------------------#fc3d "A Missing Validation Step")
3. [Building a Proof of Concept](/?source=post_page-----824c1e2dc9f0---------------------------------------#efe7 "Building a Proof of Concept")
4. [Source Directory Takeover](/?source=post_page-----824c1e2dc9f0---------------------------------------#6f88 "Source Directory Takeover")
5. [File Enumeration](/?source=post_page-----824c1e2dc9f0---------------------------------------#017d "File Enumeration")
6. [Arbitrary File Read](/?source=post_page-----824c1e2dc9f0---------------------------------------#cd5a "Arbitrary File Read")
7. [Arbitrary File Write](/?source=post_page-----824c1e2dc9f0---------------------------------------#02e0 "Arbitrary File Write")
8. [Why This Matters](/?source=post_page-----824c1e2dc9f0---------------------------------------#2fa5 "Why This Matters")
9. [Root Cause Analysis](/?source=post_page-----824c1e2dc9f0---------------------------------------#bae6 "Root Cause Analysis")
10. [Recommended Fix](/?source=post_page-----824c1e2dc9f0---------------------------------------#74ca "Recommended Fix")
11. [Final Thoughts](/?source=post_page-----824c1e2dc9f0---------------------------------------#43b2 "Final Thoughts")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-824c1e2dc9f0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--824c1e2dc9f0---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--824c1e2dc9f0---------------------------------------)

[Vulnerability Research](https://medium.com/tag/vulnerability-research?source=post_page---header_tags--824c1e2dc9f0---------------------------------------)

[Application Security](https://medium.com/tag/application-security?source=post_page---header_tags--824c1e2dc9f0---------------------------------------)

[Path Traversal](https://medium.com/tag/path-traversal?source=post_page---header_tags--824c1e2dc9f0---------------------------------------)

# When a Single Text File Breaks a Trust Boundary (Bug Bounty writeup)

[![julichaan](https://miro.medium.com/v2/resize:fill:64:64/1*mA3V4fl-hVsZvAcKlu4iwQ.png)](https://medium.com/%40espadar.julian?source=post_page---byline--824c1e2dc9f0---------------------------------------)

[julichaan](https://medium.com/%40espadar.julian?source=post_page---byline--824c1e2dc9f0---------------------------------------)

4 min read

·

2 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D824c1e2dc9f0&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-a-single-text-file-breaks-a-trust-boundary-bug-bounty-writeup-824c1e2dc9f0&source=---header_actions--824c1e2dc9f0---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

During a recent security review, I encountered an interesting vulnerability in an open-source tool that, at first glance, appeared to be implementing a completely legitimate feature.

The feature was simple: allow users to place the application’s working directory inside a subdirectory of a larger repository. Nothing unusual there.

However, after tracing the code path responsible for resolving that directory, I discovered that a single text file could completely redefine where the application believed its source data lived.

The result was a path traversal condition that allowed the application to operate on arbitrary locations outside the intended repository boundary.

## The Feature

The application supports a special file that allows users to relocate the effective source directory.

The implementation looked conceptually similar to this:

```
switch data, err := readFile(".special-root-file"); {
case fileNotFound:
    sourceDir = originalSourceDir
default:
    sourceDir = originalSourceDir.Join(
        trimSpace(data),
    )
}
```

At first glance, this seems harmless.

The problem is that the value read from the file is joined directly to the original directory without any validation that the resulting path remains inside the repository.

Since path joining functions typically normalize sequences such as:

```
../../../
```

the final path can end up pointing somewhere entirely different from what the developer originally intended.

## A Missing Validation Step

Consider a file containing:

```
../../../../../../some/other/location
```

After path normalization, the application no longer operates inside its repository.

Instead, it treats the attacker-controlled destination as the new source directory.

The crucial issue is not the traversal itself.

The issue is that no validation occurs after the path is resolved.

The application trusts the final path without verifying whether it remains inside the expected boundary.

## Building a Proof of Concept

To validate the behavior, I created an isolated test environment.

First, I prepared a directory outside the application’s normal working tree and placed a file containing sensitive-looking data:

```
mkdir -p /tmp/source
mkdir -p /tmp/outside
```

```
echo "TOP-SECRET-CONTENT" > /tmp/outside/dot_leaked-secret
```

Next, I configured the special root file:

```
printf '../outside' > /tmp/source/.special-root-file
```

Once the application processed that file, every subsequent operation began interacting with the external directory rather than the original source directory.

## Source Directory Takeover

When querying the effective source path, the application reported:

```
/tmp/outside
```

instead of:

```
/tmp/source
```

At that point, control of the source directory had effectively been transferred.

## File Enumeration

Files located exclusively in the external directory became visible through the application’s normal management commands.

The repository itself did not contain those files.

## Get julichaan’s stories in ...