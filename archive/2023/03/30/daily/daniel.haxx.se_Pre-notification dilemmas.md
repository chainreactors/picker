---
title: Pre-notification dilemmas
url: https://daniel.haxx.se/blog/2023/03/29/pre-notification-dilemmas/
source: daniel.haxx.se
date: 2023-03-30
fetch_date: 2025-10-04T11:07:57.358118
---

# Pre-notification dilemmas

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2023/03/message-in-a-bottle.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# Pre-notification dilemmas

[March 29, 2023](https://daniel.haxx.se/blog/2023/03/29/pre-notification-dilemmas/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2023/03/29/pre-notification-dilemmas/#comments)

In 2011 I started to send “pre-notifications” about pending [curl](https://curl.se/) security vulnerabilities to the [distros mailing list](https://oss-security.openwall.org/wiki/mailing-lists/distros) (back then it was still called *linux-distros*).

For several years we also asked them for CVE IDs for the new vulnerabilities that we were about to publish to the world. By notifying the distros ahead of time, the idea is that they get a little head-start to fix their curl packages so that at the day when we publish the vulnerabilities to the world, they can already provide curl upgrades.

The gap from us announcing a flaw until they offer curl upgrades could ideally be made a minimum.

The distros list’s rules forbid us to tell them more than 10 days before the planned release day. They call this an embargo as they are expected to not tell anyone who is not a mailing list member about these flaws.

During the last twelve plus years, I have told them about almost 130 pending [curl vulnerabilities](https://curl.se/docs/security.html) like this up until today.

## Secrets are hard

For an open source project that has all its processes and test infrastructure public and open there are several challenges with how to deal with secrets, such as vulnerabilities and their corresponding fixes.

We recently [updated our security process](https://github.com/curl/curl/pull/10719) in the curl project: we have noticed that we have previously – several times – landed fixes to security problems that were defective and in some cases did not even fix the reported problem correctly. I believe one reason for this is that we had this policy to make the fix into a (public) pull-request no earlier than 48 hours before the pending release. 48 hours is enough to make all the tests and CI verify the fix, but it is a very short time window for the community to react or be able to test and find any problems with the fixes before the release goes out.

As an attempt to do better we have tweaked our policy. If a reported security problem is deemed to be of severity low or severity medium, we will instead allow and rather push for turning the fix into a public pull-request much earlier. We will however not mention the security aspect of the fix in the public communication about the pull-request, but only talk about the bugfix aspect.

This will allow us to merge fixes earlier in the release cycle. To give the bugfixes more time to mature and ripe in the repository before the pending release. It should increase the chances that we can do follow-up fixes and truly make it a good correction by the time we do the next release. Hopefully it leads to better releases with fewer regressions.

Of course the risk with this is that a malicious user somewhere finds out about a vulnerability this way, earlier than 48 hours before a release, and therefore gets an extended time window to perform nefarious actions. That is also why we limit this method to severity low and medium issues, as the ones rated more serious are deemed too dangerous to risk.

## Policy vs policy

The week before we were about to ship the curl 8.0.0 release, I emailed the distros mailing list again like I have done so many times before and told them about the upcoming six(!) vulnerabilities we were about to reveal to the world.

This time turned out to be different.

Because of our updated policy where the fixes were already committed in a public git repository, the distros mailing list’s policy says that if there is a public commit they consider the issue to be public and thus they refuse to accept any embargo.

What they call embargo I of course call heads-up time.

I argue that while the fixes are public, the actual vulnerabilities and the security issues those fixes rectify are not. It takes a serious effort and pretty good insights to just *detect* that one or more of the commits for the pending release are done because of a security problem and then even more so if you want to convert that suspicion into an actual attack vector.

They maintain that while they could make an exception for me/us this time, this is an exception and their policy says this is not acceptable for embargos.

If we make commits public before telling distros, we may not “ask for an embargo”.

## So we won’t tell

I thought we were doing this *for their benefit*. I was under the impression that we actually helped distributors of open source operating systems by telling them ahead of time what was going to ship very soon that they might want to get a head-start on so that their users stay protected.

I have been told in very clear terms that they do not want to be notified about vulnerabilities ahead of time if the commits are public.

I have informed them that I will not tell them anymore until they change their minds because I think our updated security process can make our releases better and I think improving curl and making better releases is more important than telling distros ahead of time.

I cannot understand how this stubbornness makes anything better for them. For me, it takes away some amount of work so I will manage just fine. For curl users “in the wild”, this will probably mean that they will get security-patched curl releases from their distros a little slower in the future.

We rarely see curl vulnerabilities rated higher than medium so this means we will effectively stop emailing distros about pending flaws. We are still *allowed* to tell them about more criticality scored vulnerabilities but I must confess I feel less inclined to do that than I used to.

[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)[Security](https://daniel.haxx.se/blog/tag/security/)

# Post navigation

[Previous Posta Bloomberg donation](https://daniel.haxx.se/blog/2023/03/28/a-bloomberg-donation/)[Next Posttrurl manipulates URLs](https://daniel.haxx.se/blog/2023/04/03/introducing-trurl/)

## One thought on “Pre-notification dilemmas”

1. ![](https://secure.gravatar.com/avatar/7a89fc7d4fec933efed7b48c86daf4df759798a0f138c9f8b8d490020aa927cd?s=34&d=monsterid&r=g) **Harry Nyquist** says:

   [March 29, 2023 at 22:04](https://daniel.haxx.se/blog/2023/03/29/pre-notification-dilemmas/#comment-26670)

   This seems entirely reasonable. This reader is having a hard time being swayed by arguments about the Policy not justifying exceptions. Presumably this is based on concerns about a hypothetical slippery slopes of more people asking for exceptions.

   It seems to me that if the Policy finds itself preventing common sense sharing of information that benefits the distro, that may be a good time to adopt a more Wikipedia-like policy of seeing constructive contribution to the project as the actual goal, and Policy as a useful set of guidelines for the benefit of the project.

   If Policy is preventing positive contributions, contributions should take priority. And, perhaps, the guidelines should be updated to reflect that a hard set of rules fixed in advance may not have been able to predict the right way to handle the nuance of every potential future situation.

   One could become concerned, when a system of rules seems to take as its objective the app...