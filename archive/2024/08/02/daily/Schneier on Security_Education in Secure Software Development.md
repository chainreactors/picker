---
title: Education in Secure Software Development
url: https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html
source: Schneier on Security
date: 2024-08-02
fetch_date: 2025-10-06T18:07:38.386500
---

# Education in Secure Software Development

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Education in Secure Software Development

The Linux Foundation and OpenSSF released a [report](https://www.linuxfoundation.org/press/linux-foundation-and-openssf-release-report-on-the-state-of-education-in-secure-software-development) on the state of education in secure software development.

> …many developers lack the essential knowledge and skills to effectively implement secure software development. Survey findings outlined in the report show nearly one-third of all professionals directly involved in development and deployment ­ system operations, software developers, committers, and maintainers ­ self-report feeling unfamiliar with secure software development practices. This is of particular concern as they are the ones at the forefront of creating and maintaining the code that runs a company’s applications and systems.

Tags: [security education](https://www.schneier.com/tag/security-education/), [software](https://www.schneier.com/tag/software/)

[Posted on August 1, 2024 at 7:03 AM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html) •
[13 Comments](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html#comments)

### Comments

Jaime •
[August 1, 2024 7:59 AM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439755)

In my opinion this is a result of how security specialists are integrated into most organizations. We usually pretend that since we have a security team, they’ll handle security.

It is rare to find an organization where the security team is allowed to act as a both a consultant to a development team, and to create metric and target that the development team are required to meet.

Usually, I see the security team require that development teams use static analysis tools and scan the test environment before deployment. This fixes some of the more common and easy to spot development mistakes, but does nothing for bad architecture and more subtle issues.

Clive Robinson •
[August 1, 2024 9:15 AM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439759)

@ Bruce, ALL,

This is not a exactly news, nor are the reasons behind it.

To be brief,

**“Managment see no short term profit in security, only delays to product delivery cycles”.**

The rest as they say follows on as a consequence.

I’ll let others “fill in” the veritable tsunami of reasons, but note there are now many many books addressing the issue, and they have all failed due to the way management behave.

My suggestion lock a few senior managers up for 20years+ and bankrupt them and their families, and you might see a change in the right direction.

bw •
[August 1, 2024 11:15 AM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439760)

This is no surprise to me. In my ~40 years coding I have met a few programmers who cared at all about security and most of those didn’t really know enough to create secure code/processes.

It keeps me busy and employed, so I’m not sure if I want to see any change 😉

anonymous •
[August 1, 2024 12:48 PM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439761)

And they expect this to survive the first manager with time constraints? I don’t.

Morley •
[August 1, 2024 2:44 PM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439763)

Oh ya, Computer Science is not Software Engineering. Or security related DevOps or IT. Nobody really teaches Software Engineering, last I knew. It would be great.

[William Thorpe](http://vapac.blogspot.com) •
[August 1, 2024 6:25 PM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439765)

Why am I seeing special case crawlers google bots on my page. I am a prison reform advocate

sitaram •
[August 1, 2024 8:53 PM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439768)

The “don’t care” attitude from management, that others have alluded to, is not just about profits. There’s also a huge unwillingness to take in knowledge that is not directly related to the job.

This manifests even in other ways — for example, normal people unwilling to pick a better password for their bank account or whatever.

David •
[August 2, 2024 5:37 AM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439773)

Once AI has replaced all of the business owners, system architects, designers, coders, testers and end users, then I’m sure secure coding practices will be automatically embedded in the development of every piece of software. After all there were no bugs in SkyNet.

Clive Robinson •
[August 3, 2024 1:24 PM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development.html/#comment-439792)

@ Bruce, ALL,

Re : Why Walled Gardens fail.

As most readers here are aware Apple and Google have “Walled Garden” repositories of Applications. It’s a game Microsoft desperately want to get into but got stymied by both the EU and Google.

Well Apple have been having a “Red Queens Race” with their walled garden for a number of reasons, but one that keeps popping up is “Bad Apps passing scrutiny” that in the blurb of both Apple and Google way back “could not / will not” happen.

Some of us here a little wiser than most gave at best hollow laughs to such blatant nonsense[1] designed to befuddled those with political influence.

The problem for Apple is “user expectations” from Apple talking security up as just one reason to justify their business models.

The problem is those that fall for the “Apple Security” nonsense generally are up in what were once known as ABC1 consumers. Thus Apple was the “honey pot most sweet” for those looking to gain unlawfully or dubious advantage that there was little or nothing Apple could do to stop it.

It’s getting to the point that even “Fan-boi Zines and Sites” are “dishing the dirt” on the nonsense.

For instance this little article from yesterday,

<https://9to5mac.com/2024/08/02/developers-trick-app-store-review/>

[1] I’ve mentioned it before, but back in the early 1930’s there were a series of mathematics papers that proved that there were limits on what “a computer could do” and what could be done with them before electromechanical or electronic computers had actually been invented and built (commercially that did not happen untill the J.Lyon’s Tea Shop company research gave rise to the “LEO” that was “cranking it out” less than twenty years later,

<https://www.theregister.com/2021/11/30/leo_70/>

ResearcherZero •
[August 5, 2024 3:03 AM](https://www.schneier.com/blog/archives/2024/08/education-in-secure-software-development....