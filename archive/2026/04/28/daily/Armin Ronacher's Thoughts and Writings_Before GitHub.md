---
title: Before GitHub
url: https://lucumr.pocoo.org/2026/4/28/before-github/
source: Armin Ronacher's Thoughts and Writings
date: 2026-04-28
fetch_date: 2026-04-29T05:05:44.979423
---

# Before GitHub

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Before GitHub

written on April 28, 2026

GitHub was not the first home of my Open Source software. [SourceForge
was](https://sourceforge.net/projects/pocoo/).

Before GitHub, I had my own Trac installation. I had Subversion repositories,
tickets, tarballs, and documentation on infrastructure I controlled. Later I
moved projects to Bitbucket, back when Bitbucket still felt like a serious
alternative place for Open Source projects, especially for people who were not
all-in on Git yet.

And then, eventually, GitHub became the place, and I moved all of it there.

It is hard for me to overstate how important GitHub became in my life. A large
part of my Open Source identity formed there. Projects I worked on found users
there. People found me there, and I found other people there. Many professional
relationships and many friendships started because some repository, issue, pull
request, or comment thread made two people aware of each other.

That is why I find what is happening to GitHub today so sad and so
disappointing. I do not look at it as just the folks at Microsoft making
product decisions I dislike. GitHub was part of the social infrastructure of
Open Source for a very long time. For many of us, it was not merely where the
code lived; it was where a large part of the community lived.

So when I think about GitHub’s decline, I also think about what came before it,
and what might come after it. I have written a few times over the years about
dependencies, and in particular about the problem of [micro
dependencies](/2016/3/24/open-source-trust-scaling/). In my mind, GitHub gave
life to that phenomenon. It was something I definitely did not completely
support, but it also made Open Source more inclusive. GitHub changed how Open
Source feels,
and later npm and other systems changed how dependencies feel. Put them
together and you get a world in which publishing code is almost frictionless,
consuming code is almost frictionless, and the number of projects in the world
explodes.

That has many upsides. But it is worth remembering that Open Source did not
always work this way.

## A Smaller World

Before GitHub, Open Source was a much smaller world. Not necessarily in the
number of people who cared about it, but in the number of projects most of us
could realistically depend on.

There were well-known projects, maintained over long periods of time by a
comparatively small number of people. You [knew the
names](/2024/3/31/skin-in-the-game/). You knew the mailing lists. You knew who
had been around for years and who had earned trust. That trust was not perfect,
and the old world had plenty of gatekeeping, but reputation mattered in a very
direct way. We took pride (and got frustrated) when the Debian folks came and
told us our licensing stuff was murky or the copyright headers were not up to
snuff, because they packaged things up.

A dependency was not just a package name. It was a project with a history, a
website, a maintainer, a release process, a lot of friction, and often a place in
a larger community. You did not add dependencies casually, because the act of
depending on something usually meant you had to understand where it came from.

Not all of this was necessarily intentional, but because these projects were
comparatively large, they also needed to bring their own infrastructure. Small
projects might run on a university server, and many of them were on SourceForge,
but the larger ones ran their own show. They grouped together into larger
collectives to make it work.

## We Ran Our Own Infrastructure

My first Open Source projects lived on infrastructure I ran myself. There was a
Trac installation, Subversion repositories, tarballs, documentation, and release
files served from my own machines or from servers under my control. That was
normal. If you wanted to publish software, you often also became a small-time
system administrator. [Georg](https://github.com/birkenfeld) and I ran our own
collective for our Open Source projects: [Pocoo](http://www.pocoo.org/). We
shared server costs and the burden of maintaining Subversion and Trac, mailing
lists and more.

Subversion in particular made this “running your own forge” natural. It was
centralized: you needed a server, and somebody had to operate it.
The project had a home, and that home was usually quite literal: a hostname, a
directory, a Trac instance, a mailing list archive.

When Mercurial and Git arrived, they were philosophically the opposite. Both
were distributed. Everybody could have the full repository. Everybody could
have their own copy, their own branches, their own history. In principle, those
distributed version control systems should have reduced the need for a single
center. But despite all of this, GitHub became the center.

That is one of the great ironies of modern Open Source. The distributed version
control system won, and then the world standardized on one enormous centralized
service for hosting it.

## What GitHub Gave Us

It is easy now to talk only about GitHub’s failures, of which there are currently
many, but that would be unfair: GitHub was, and continues to be, a tremendous
gift to Open Source.

It made creating a project easy and it made discovering projects easy. It made
contributing understandable to people who had never subscribed to a development
mailing list in their life. It gave projects issue trackers, pull requests,
release pages, wikis, organization pages, API access, webhooks, and later CI.
It normalized the idea that Open Source happens in the open, with visible
history and visible collaboration. And it was an excellent and reasonable
default choice for a decade.

But maybe the most underappreciated thing GitHub did was archival work: GitHub
became a library. It became an index of a huge part of the software commons
because even abandoned projects remained findable. You could find forks, and
old issues and discussions all stayed online. For all the complaints one can
make about centralization, that centralization also created discoverable memory.
The [leaders there once
cared](https://github.blog/news-insights/policy-news-and-insights/advancing-developer-freedom-github-is-fully-available-in-iran/)
a lot about keeping GitHub available even in countries that were sanctioned by
the US.

I know what the alternative looks like, because I was living it. Some of my
earliest Open Source projects are [technically still on
PyPI](https://pypi.org/project/Colubrid/0.9/), but the actual packages are gone.
The metadata points to my old server, and that server has long stopped serving
those files.

That was normal before the large platforms. A personal domain expired, a VPS
was shut down, a developer passed away, and with them went the services they
paid for. The web was once full of little software homes, and many of them are
gone [1](#fn-1).

## npm and the Dependency Explosion

The micro-dependency problem was not just that people published very small
packages. The hosted infrastructure of GitHub and npm made it feel as if there
was no cost to create, publish, discover, install, and depend on them.

In the pre-GitHub world, reputation and longevity were part of the dependency
selection process almost by necessity, and it often required vendoring. Plenty
of our early dependencies were just vendored into our own Subversion trees by
default, in part because we could not even rely on other services being up when
we needed them and because maintaining scripts that fetched them, in the pre-API
days, was painful. The implied friction forced some reflection, and it resulted
in different developer behavior. With npm-style ecosystems, the package graph can
grow faster than anybody’s ability to reason about it.

The problem that this type of thinking created also meant that solutions had to
be found along the way. ...