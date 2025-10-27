---
title: Modernizing the toolbox for Cloudflare Pages builds
url: https://buaq.net/go-163803.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:35.490891
---

# Modernizing the toolbox for Cloudflare Pages builds

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/97719b30c3aac2d00325c47d6ea2567f.jpg)

Modernizing the toolbox for Cloudflare Pages builds

Loading...
*2023-5-17 21:0:37
Author: [blog.cloudflare.com(查看原文)](/jump-163803.htm)
阅读量:28
收藏*

---

Loading...

* [![Greg Brimble](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/09/Profile-Picture--Square-.jpg)](https://blog.cloudflare.com/author/greg-brimble/)

![Modernizing the toolbox for Cloudflare Pages builds](https://blog.cloudflare.com/content/images/2023/05/image2-22.png)

Cloudflare Pages [launched](https://blog.cloudflare.com/cloudflare-pages/) over two years ago in December 2020, and since then, we have grown Pages to build millions of deployments for developers. In May 2022, to support developers with more complex requirements, we opened up Pages to empower developers to [create deployments using their own build environments](https://blog.cloudflare.com/cloudflare-pages-direct-uploads/) — but that wasn't the end of our journey. Ultimately, we want to be able to allow anyone to use our build platform and take advantage of the git integration we offer. You should be able to connect your repository and have it *just work* on Cloudflare Pages.

Today, we're introducing a new beta version of our build system (a.k.a. "build image") which brings the default set of tools and languages up-to-date, and sets the stage for future improvements to builds on Cloudflare Pages. We now support the latest versions of Node.js, Python, Hugo and many more, putting you on the best path for any new projects that you undertake. Existing projects will continue to use the current build system, but this upgrade will be available to opt-in for everyone.

## New defaults, new possibilities

The Cloudflare Pages build system has been updated to not only support new versions of your favorite languages and tools, but to also include new versions by default. The versions of 2020 are no longer relevant for the majority of today's projects, and as such, we're bumping these to their more modern equivalents:

* **Node.js**' default is being increased from 12.18.0 to 18.16.0,
* **Python** 2.7.18 and 3.10.5 are both now available by default,
* **Ruby**'s default is being increased from 2.7.1 to 3.2.2,
* **Yarn**'s default is being increased from 1.22.4 to 3.5.1,
* And we're adding **pnpm** with a default version of 8.2.0.

These are just some of the headlines — check out [our documentation](https://developers.cloudflare.com/pages/platform/language-support-and-tools/?ref=blog.cloudflare.com) for the full list of changes.

We're aware that these new defaults constitute a breaking change for anyone using a project without pinning their versions with an environment variable or version file. That's why we're making this new build system opt-in for existing projects. You'll be able to stay on the existing system without breaking your builds. If you do decide to adventure with us, we make it easy to test out the new system in your preview environments before rolling out to production.

![Screenshot of the Cloudflare dashboard Pages project settings screen where you can configure the build system version.](https://blog.cloudflare.com/content/images/2023/05/image5-5.png)

Additionally, we're now making your builds more reproducible by taking advantage of lockfiles with many package managers. `npm ci` and `yarn --pure-lockfile` are now used ahead of your build command in this new version of the build system.

For new projects, these updated defaults and added support for pnpm and Yarn 3 mean that more projects will just work immediately without any undue setup, tweaking, or configuration. Today, we're launching this update as a beta, but we will be quickly promoting it to general availability once we're satisfied with its stability. Once it does graduate, new projects will use this updated build system by default.

We know that this update has been a long-standing request from our users (we thank you for your patience!) but part of this rollout is ensuring that we are now in a better position to make regular updates to Cloudflare Pages' build system. You can expect these default languages and tools to now keep pace with the rapid rate of change seen in the world of web development.

We very much welcome your continued feedback as we know that new tools can quickly appear on the scene, and old ones can just as quickly drop off. As ever, our [Discord server](https://discord.com/invite/cloudflaredev?ref=blog.cloudflare.com) is the best place to engage with the community and Pages team. We’re excited to hear your thoughts and suggestions.

## Our modular and scalable architecture

Powering this updated build system is a new architecture that we've been working on behind-the-scenes. [We're no strangers to sweeping changes of our build infrastructure](https://blog.cloudflare.com/cloudflare-pages-build-improvements/): we've done a lot of work to grow and scale our infrastructure. Moving beyond purely static site hosting with [Pages Functions](https://blog.cloudflare.com/cloudflare-pages-goes-full-stack/) brought a new wave of users, and as we explore [convergence](https://blog.cloudflare.com/pages-and-workers-are-converging-into-one-experience) with Workers, we expect even more developers to rely on our git integrations and CI builds. Our new architecture is being rolled out without any changes affecting users, so unless you're interested in the technical nitty-gritty, feel free to stop reading!

The biggest change we're making with our architecture is its modularity. Previously, we were using Kubernetes to run a monolithic container which was responsible for everything for the build. Within the same image, we'd stream our build logs, clone the git repository, install any custom versions of languages and tools, install a project's dependencies, run the user's build command, and upload all the assets of the build. This was a lot of work for one container! It meant that our system tooling had to be compatible with versions in the user's space and therefore new default versions were a massive change to make. This is a big part of why it took us so long to be able to update the build system for our users.

In the new architecture, we've broken these steps down into multiple separate containers. We make use of [Kubernetes' init containers feature](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/?ref=blog.cloudflare.com) and instead of one monolithic container, we have three that execute sequentially:

1. clone a user's git repository,
2. install any custom versions of languages and tools, install a project's dependencies, run the user's build command, and
3. upload all the assets of a build.

We use a [shared volume](https://kubernetes.io/docs/tasks/access-application-cluster/communicate-containers-same-pod-shared-volume/?ref=blog.cloudflare.com) to give the build a persistent workspace to use between containers, but now there is clear isolation between **system** stages (cloning a repository and uploading assets) and **user** stages (running code that the user is responsible for). We no longer need to worry about conflicting versions, and we've created an additional layer of security by isolating a user's control to a separate environment.

![A diagram of three sequential Kubernetes containers which all connect to a Kubernetes Shared Volume. They belong to a Kubernetes job which itself is run within a Kubernetes Node. The first container clones a user's git repository; the second installs languages, tools, dependencies and runs the build; and the ...