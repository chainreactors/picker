---
title: Mirroring GitHub projects in 2023
url: https://a13xp0p0v.github.io/2023/01/29/mirroring-github-projects.html
source: Alexander Popov
date: 2023-01-30
fetch_date: 2025-10-04T05:10:00.103545
---

# Mirroring GitHub projects in 2023

[![](/img/favicons/a13xp0p0v_ava.png) Alexander Popov](/)
[ ]

[About](/about/)[Articles](/articles/)[Conference Talks](/conference_talks/)

# Mirroring GitHub projects in 2023

Jan 29, 2023

For many reasons, I want to mirror my public GitHub projects on other collaboration platforms. This short article describes my difficulties with it and a working solution.

![](/img/Alice.jpg)

For a year, I used the [GitHub](https://github.com/)->[GitLab](https://about.gitlab.com/) pull mirroring. It could copy the code, tags, and discussions in issues and pull requests, which was nice. But some time ago, I noticed that my GitLab branches fall behind the origin. I signed in to GitLab and saw this annoying banner:

[![GitLab banner](/img/gitlab_banner.png)](/img/gitlab_banner.png)

GitLab pull mirroring disappeared from some of my repositories. Enabling it again with Free Tier is not possible anymore.

![](/img/gitlab_pull_mirroring.png)

Buying GitLab Premium Tier is not possible for anyone from Russia. Even a free trial is not allowed. So I started to look at other mirroring solutions:

* Running a self-hosted GitLab or [Forgejo](https://forgejo.org/) server couldn't suit me well, because I didn't want to host my open-source projects on an isolated server.
* I checked [Chinese Gitee](https://gitee.com) and didn't like its limited support for English localization.
* I looked at the [Radicle p2p network](https://radicle.xyz) for software development. But its "powerful blockchain-based functionalities" looked too radical to me.
* Then I looked at [Codeberg](https://codeberg.org/). It's driven by a non-profit organization promoting FOSS ideas. I like them much more than Microsoft. But in March 2020, they disabled mirroring due to a [lack of resources](https://blog.codeberg.org/mirror-repos-easily-created-consuming-resources-forever.html). They say: "Mirror repos: easily created, consuming resources forever." :(
* I also checked [SourceHut](https://sourcehut.org) (thanks to [paulmairo](https://twitter.com/_paulmairo) for the idea). It doesn't suit me well because:
  1. It provides only paid services.
  2. Its workflow looks incompatible with GitHub: Sourcehut uses plain-text email for reporting bugs, creating tickets, and submitting patches.
* I checked [Salsa](https://salsa.debian.org) (thanks to [Mic\_92](https://twitter.com/Mic_92) for the idea). It's a collaborative development server for Debian based on the GitLab software. At first, I registered an account. Several days later, Salsa administrator enabled it and I managed to copy one of my projects from GitHub to Salsa. But it turned out that the pull mirroring feature at Salsa is disabled, similarly to [gitlab.com](https://about.gitlab.com/). I [asked about it](https://salsa.debian.org/salsa/support/-/issues/326) on the Salsa issue tracker but didn't get any reply.
* Then I created the [mirrors](https://gitflic.ru/user/a13xp0p0v) for my GitHub projects at [GitFlic](https://gitflic.ru), a small proof-of-concept collaboration platform. But it doesn't have CI and can't copy the information from GitHub issues and pull requests. Obviously, not a final solution.
  [![GitFlic mirroring](/img/gitflic_mirroring.png)](/img/gitflic_mirroring.png)

To sum up, I didn't find any popular code collaboration platform that could provide full-featured mirrors for my GitHub projects. So I decided to look at this task from another angle: how can I manually back up the info from the GitHub issues and pull requests?

My first idea was to turn the discussions into a part of the code. Shortly, I found a nice project [gh2md](https://github.com/mattduck/gh2md), which can help with it. gh2md grabs the information from GitHub issues and pull requests and turns it into a Markdown document.

Under the hood, it uses GraphQL API provided by GitHub, so I had to generate a GitHub personal access token with public access. See the [GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for more info.

[![GitHub access token](/img/github_access_token.png)](/img/github_access_token.png)

Now my projects contain the `issues.md` file with a [backup of issues/PRs](https://github.com/a13xp0p0v/kconfig-hardened-check/blob/master/issues.md). It's possible to use gh2md in GitHub Actions and update `issues.md` automatically. But for now, I refrain from giving write repository access to the GitHub Actions workers.

For a moment, I thought about a GitHub Actions script generating a pull request with the updates of `issues.md`. Shortly, I realized that it was not a clever idea: this new PR would make the CI script update `issues.md` once again and generate another PR :) That can be called a GitHub Actions spammer.

Another option is to keep GitHub issues in the git storage of the project: the [git-bug](https://github.com/MichaelMure/git-bug) tracker can do the job (thanks to [Sergey Bronnikov](https://twitter.com/estet) for the link):

[![git-bug](/img/git-bug.png)](/img/git-bug.png)

Anyway, after committing the Markdown backup of GitHub issues and PRs, I decided to create clone repositories at Codeberg and then do a **git push both** to GitHub and Codeberg. GitHub->Codeberg migration of my projects worked well. It copied all the info from the origin. So Codeberg would be the ideal solution for me if it had a pull mirroring feature… Alas!

But what to do with out-of-date issues/PRs at Codeberg? Deleting and recreating projects manually would be a dirty hack, and I didn't like it.

[![Codeberg mirroring](/img/codeberg_mirroring.png)](/img/codeberg_mirroring.png)

I looked through repo settings and found a workaround: Codeberg provides options for using an external issue tracker! I set the URL format and numbering for the external issues, disabled the Codeberg pull requests, and now have the correct links to GitHub issues and PRs from Codeberg repositories.

[![Codeberg repo settings](/img/codeberg_links.png)](/img/codeberg_links.png)

Now it is a more or less working solution. If something goes wrong with GitHub, I will enable the internal issue tracker and pull requests at Codeberg.

[![Codeberg mirroring 2](/img/codeberg_mirroring-2.png)](/img/codeberg_mirroring-2.png)

That's all. Maybe this story will be useful to somebody.

## Contacts

* alex.popov@linux.com
* [a13xp0p0v](https://twitter.com/a13xp0p0v)
* [@a13xp0p0v@infosec.exchange](https://infosec.exchange/%40a13xp0p0v)
* [a13xp0p0v](https://github.com/a13xp0p0v)
* [a13xp0p0v](https://t.me/a13xp0p0v)
* [a13xp0p0v](https://www.linkedin.com/in/a13xp0p0v)