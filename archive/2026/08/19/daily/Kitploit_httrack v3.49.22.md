---
title: httrack v3.49.22
url: https://kitploit.com/en/posts/github-xroche-httrack-34922
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:54:13.720727
---

# httrack v3.49.22

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F47043%2F743a2dda80b01656763b32e9cc350233eed798a1187128bcf5ff51e4ebc86470.png&w=3840&q=75)

New releaseAug 19, 2026

# httrack v3.49.22

Offline website copier that recursively downloads HTML, images, and files to create a browsable local mirror, with support for resuming and updating existing mirrored sites.

Share

# HTTrack Website Copier - Development Repository

[![CI](https://github.com/xroche/httrack/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/xroche/httrack/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/xroche/httrack)](COPYING)

## About

*Copy websites to your computer (Offline browser)*

![](https://assets.kitploit.com/production/public/readmes/placeholders/f0fc86cfe65f76d40e15aaec61704ec8220a56dc89d4be03c46f67cb31b9fa8c.svg)

*HTTrack* is an *offline browser* utility, allowing you to download a World Wide website from the Internet to a local directory, building recursively all directories, getting html, images, and other files from the server to your computer.

*HTTrack* arranges the original site's relative link-structure. Simply open a page of the "mirrored" website in your browser, and you can browse the site from link to link, as if you were viewing it online.

HTTrack can also update an existing mirrored site, and resume interrupted downloads. HTTrack is fully configurable, and has an integrated help system.

*WinHTTrack* is the Windows 2000/XP/Vista/Seven release of HTTrack, and *WebHTTrack* the Linux/Unix/BSD release.

## Website

*Main Website:*
<http://www.httrack.com/>

## Compile trunk release

A git checkout ships only the autotools sources, so `./bootstrap` (which runs
`autoreconf`) regenerates `configure` first; this needs autoconf, automake and
libtool. Released tarballs already include `configure`, so building from a
tarball skips `./bootstrap`.

root@kitploit:~

```
git clone https://github.com/xroche/httrack.git --recurse-submodules
cd httrack
./bootstrap
./configure --prefix=$HOME/usr && make -j8 && make install
```

Or use the one-shot wrapper (bootstrap + configure + make), which forwards its
arguments to `configure`:

root@kitploit:~

```
./build.sh --prefix=$HOME/usr
```

[Read more](/en/tools/github/xroche/httrack?expand=1)

## Categories

[General Purpose Utilities](/en/categories/general-purpose-utilities)[Information Gathering](/en/categories/information-gathering)[Crawler](/en/categories/crawler)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

httrack v3.49.22 — HTTrack Website Copier, copy websites to your computer (Official repository) | Kitploit