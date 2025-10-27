---
title: Detecting malicious Unicode
url: https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/
source: daniel.haxx.se
date: 2025-05-17
fetch_date: 2025-10-06T22:27:16.368870
---

# Detecting malicious Unicode

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2022/12/Screenshot-2022-12-13-at-23-14-42-Unicode-Utilities-Confusables.png)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Detecting malicious Unicode

[May 16, 2025](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [12 Comments](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/#comments)

In a recent educational trick, curl contributor James Fuller submitted a pull-request to the project in which he suggested a larger cleanup of a set of scripts.

In a later presentation, he could show us how not a single human reviewer in the team nor any CI job had spotted or remarked on one of the changes he included: he replaced an ASCII letter with a Unicode alternative in a URL.

This was an eye-opener to several of us and we decided we needed to up our game. We are the curl project. We can do better.

## GitHub

The replacement symbol looked identical to the ASCII version so it was not possible to visually spot this, but the diff viewer knows there is a difference.

In this GitHub website screenshot below I reproduced a similar case. The right-side version has the Latin letter ‘g’ replaced with the [Armenian letter co](https://www.compart.com/en/unicode/U%2B0581). They appear to be the same.

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/05/github-unicode-diff.png)

GitHub shows a diff. But what is actually the difference?

The diff viewer says there is a difference but as a human it isn’t possible to detect what it is. Is it a flaw? Does it matter? If done “correctly”, it would be done together with a *real* and expected fix.

The impact of changing one or more letters in a URL can of course be devastating depending on conditions.

When I flagged about this rather big omission to GitHub people, I got barely no responses at all and I get the feeling the impact of this flaw is not understood and acknowledged. Or perhaps they are all just too busy implementing the next AI feature we don’t want.

## Warnings

When we discussed this problem on Mastodon earlier this week, Viktor Szakats provided me with an example screenshot of doing a similar stunt with Gitea which quite helpfully highlights that there is something special about the replacement:

![](https://daniel.haxx.se/blog/wp-content/uploads/2025/05/gitea-unicode-diff.png)

Gitea warns that the replacement is using “ambiguous Unicode characters”

I have been told that some of the other source code hosting services also show similar warnings.

As a user, I would actually like to know even more than this, but at least this warns about the proposed change clearly enough so that if this happens I would get the code manually and investigate before accepting such a change.

## Detect

While we wait for GitHub to wake up and react (which I have no expectation will actually happen anytime soon), we have implemented checks to help us poor humans spot things like this. *To detect malicious Unicode.*

We have added [a CI job](https://github.com/curl/curl/blob/master/.github/scripts/spacecheck.pl) that scans all files and validates every UTF-8 sequence in the git repository.

In the curl git repository most files and most content are plain old ASCII so we can “easily” whitelist a small set of UTF-8 sequences and some specific files, the rest of the files are simply not allowed to use UTF-8 at all as they will then fail the CI job and turn up red.

In order to drive this change home, we went through all the test files in the curl repository and made sure that all the UTF-8 occurrences were instead replaced by other kind of escape sequences and similar. Some of them were also used more or less by mistake and could easily be replaced by their ASCII counterparts.

The next time someone tries this stunt on us it could be someone with less good intentions, but now ideally our CI will tell us.

## Confusables

There are plenty of tools to find similar-looking characters in different Unicode sets. One of them is provided by the Unicode consortium themselves:

<https://util.unicode.org/UnicodeJsps/confusables.jsp>

## Reactive

This was yet another security-related fix *reacting* on a demonstrated problem. I am sure there are plenty more problems which we have not yet thought about nor been shown and therefore we do not have adequate means to detect and act on automatically.

We want and strive to be proactive and tighten everything *before* malicious people exploit some weakness somewhere but security remains this never-ending race where we can only do the best we can and while *the other side* is working in silence and might at some future point attack us in new creative ways we had not anticipated.

That future unknown attack is a tricky thing.

## Update

(At 17:30 on the same day of the original post) GitHub has told me they have raised this as a security issue internally and they are working on a fix.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[git](https://daniel.haxx.se/blog/tag/git/)[github](https://daniel.haxx.se/blog/tag/github/)[Security](https://daniel.haxx.se/blog/tag/security/)[unicode](https://daniel.haxx.se/blog/tag/unicode/)

# Post navigation

[Previous PostSupported curl versions and end of life](https://daniel.haxx.se/blog/2025/05/14/supported-curl-versions-and-end-of-life/)[Next PostLeeks and leaks](https://daniel.haxx.se/blog/2025/05/16/leeks-and-leaks/)

## 12 thoughts on “Detecting malicious Unicode”

1. ![](https://secure.gravatar.com/avatar/185380e3440f9e104634e76fca51cbdbf1d2974c50bbf8e6eb8abd4525915790?s=34&d=monsterid&r=g) **Christian** says:

   [May 16, 2025 at 16:17](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/#comment-27164)

   GitHub just started to warn about hidden Unicode characters.
   <https://github.blog/changelog/2025-05-01-github-now-provides-a-warning-about-hidden-unicode-text/>

   1. ![](https://secure.gravatar.com/avatar/69fdca87edd17cee21ca2e79fc2ff671d644603c3dc27167430f3cd3dbab7ba8?s=34&d=monsterid&r=g) **[Daniel Stenberg](https://daniel.haxx.se/)** says:

      [May 16, 2025 at 17:52](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/#comment-27165)

      @Christian: yes they did, but that doesn’t help us here…
2. ![](https://secure.gravatar.com/avatar/982336a28b71ee6af3a43b720b191a89190f5a2ebd1477685ca4482c5c30b739?s=34&d=monsterid&r=g) **Bitl** says:

   [May 16, 2025 at 18:00](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/#comment-27166)

   I’d really like each code editor / viewer to highlight non 7bit ascii.
3. ![](https://secure.gravatar.com/avatar/76e5ed21301dba1dc8c7917a186ead51311ae7f2623d78c44697c1e043d1b42b?s=34&d=monsterid&r=g) **[Marek Knápek](https://about.me/marek.knapek)** says:

   [May 16, 2025 at 22:35](https://daniel.haxx.se/blog/2025/05/16/detecting-malicious-unicode/#comment-27168)

   About 15 years ago, I was affraid of similar thing. Not because security, but because possible mojibake. I was affraid that the same text file will cause havock when interpreted as cp1250 by one program and when interpret as cp437 or as UTF-8 by another program. One of the programs would be the compiler, other night be version control system or my text editor. I set my text editor (jEdit) to accept 7bit ASCII only in order to detect this. Happily the only thing it ever detected was … (three dots) vs … (unicode ellipsis) in code comments caused by Mac coworkers (I used Windows).
4. ![](https://secure.gravatar.com/avatar/363...