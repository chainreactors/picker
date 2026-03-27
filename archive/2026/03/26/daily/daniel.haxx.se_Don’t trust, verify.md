---
title: Don’t trust, verify
url: https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/
source: daniel.haxx.se
date: 2026-03-26
fetch_date: 2026-03-27T04:31:36.902923
---

# Don’t trust, verify

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/04/checklist-2077020_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Don’t trust, verify

[March 26, 2026](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2026/03/26/dont-trust-verify/#comments)

Software and digital security should rely on *verification*, rather than trust. I want to strongly encourage more users and consumers of software to verify curl. And ideally require that you could do at least this level of verification of other software components in your dependency chains.

## Attacks are omnipresent

With every source code commit and every release of software, there are risks. Also entirely independent of those.

Some of the things a widely used project can become the victim of, include…

* *[Jia Tan](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)* is a skilled and friendly member of the project team but is *deliberately* merging malicious content disguised as something else.
* An established committer might have been breached unknowingly and now their commits or releases contain tainted bits.
* A rando convinced us to merge what looks like a bugfix but is a small step in a long chain of tiny pieces building up a planted vulnerability or even backdoor
* Someone blackmails or extorts an existing curl team member into performing changes not otherwise accepted in the project
* A change by an established and well-meaning project member that adds a feature or fixes a bug mistakenly creates a security vulnerability.
* The website on which tarballs are normally distributed gets hacked and now evil alternative versions of the latest release are provided, spreading malware.
* Credentials of a known curl project member is breached and misinformation gets distributed appearing to be from a *known* and *trusted source*. Via email, social media or websites. Could even be this blog!
* Something in this list is backed up by an online deep-fake video where a known project member seemingly repeats something incorrect to aid a malicious actor.
* A tool used in CI, hosted by a cloud provider, is hacked and runs something malicious
* While the primary curl git repository has a downtime, someone online (impersonating a curl team member?) offers a temporary “curl mirror” that contains tainted code.

In the event any of these would happen, they could of course also happen in combinations and in a rapid sequence.

## You can verify

curl, mostly in the shape of libcurl, runs in tens of billions of devices. Clearly one of the most widely used software components in the world.

People ask me how I sleep at night given the vast amount of nasty things that *could* occur virtually at any point.

There is only one way to combat this kind of insomnia: do everything possible and do it openly and transparently. Make it a little better this week than it was last week. Do software engineering right. Provide means for everyone to verify what we do and what we ship. Iterate, iterate, iterate.

If even just a few users verify that they got a curl release signed by the curl release manager and they verify that the release contents is untainted and only contains bits that originate from the git repository, then we are in a pretty good state. We need enough *independent* outside users to do this, so that one of them can blow the whistle if anything at any point would look wrong.

I can’t tell you who these users are, or in fact if they actually exist, as they are and must be completely independent from me and from the curl project. We do however provide all the means and we make it easy for such users to [do this verification](https://curl.se/docs/verify.html).

## We must verify

The few outsiders who verify that nothing was tampered with in the releases can only validate that the releases are made from what exists in git. It is our own job to make sure that what exists in git is *the real thing*. The secure and safe curl.

We must do *a lot* to make sure that whatever we land in git is okay. Here’s a list of activities we do.

1. we have a consistent code style (invalid style causes errors). This reduces the risk for mistakes and makes it easier to debug existing code.
2. we ban and avoid a number of “sensitive” and “hard-to-use” C functions (use of such functions causes errors)
3. we have a ceiling for complexity in functions to keep them easy to follow, read and understand (failing to do so causes errors)
4. we review all pull requests before merging, both with humans and with bots. We link back commits to their origin pull requests in commit messages.
5. we ban use of “binary blobs” in git to not provide means for malicious actors to bundle encrypted payloads (trying to include a blob causes errors)
6. we actively avoid base64 encoded chunks as they too could function as ways to obfuscate malicious contents
7. we ban most uses of Unicode in code and documentation to avoid easily mixed up characters that look like other characters. (adding Unicode characters causes errors)
8. we document everything to make it clear how things are supposed to work. No surprises. Lots of documentation is tested and verified in addition to spellchecks and consistent wording.
9. we have thousands of tests and we add test cases for (ideally) every functionality. Finding “white spots” and adding coverage is a top priority. curl runs on countless operating systems, CPU architectures and you can build curl in billions of different configuration setups: not every combination is practically possible to test
10. we build curl and run tests in over two hundred CI jobs that are run for every commit and every PR. We do not merge commits that have unexplained test failures.
11. we build curl in CI with the most picky compiler options enabled and we never allow compiler warnings to linger. We always use `-Werror` that converts warnings to errors and fail the builds.
12. we run all tests using valgrind and several combinations of sanitizers to find and reduce the risk for memory problems, undefined behavior and similar
13. we run all tests as “torture tests”, where each test case is rerun to have every invoked fallible function call fail once each, to make sure curl never leaks memory or crashes due to this.
14. we run fuzzing on curl: non-stop as part of Google’s OSS-Fuzz project, but also briefly as part of the CI setup for every commit and PR
15. we make sure that the CI jobs we have for curl never “write back” to curl. They access the source repository read-only and even if they would be breached, they cannot infect or taint source code.
16. we run `zizmor` and other code analyzer tools on the CI job config scripts to reduce the risk of us running or using insecure CI jobs.
17. we are committed to always fix reported vulnerabilities in the following release. Security problems never linger around once they have been reported.
18. we document everything and every detail about all curl vulnerabilities ever reported
19. our commitment to never breaking ABI or API allows all users to easily upgrade to new releases. This enables users to run recent security-fixed versions instead of legacy insecure versions.
20. our code has been audited several times by external security experts, and the few issues that have been detected in those were immediately addressed
21. Two-factor authentication on GitHub is mandatory for all committers

All this done in the open with full transparency and full accountability. Anyone can follow a...