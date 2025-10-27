---
title: A whole new Quick Edit in Cloudflare Workers
url: https://buaq.net/go-163801.html
source: unSafe.sh - 不安全
date: 2023-05-18
fetch_date: 2025-10-04T11:38:34.257385
---

# A whole new Quick Edit in Cloudflare Workers

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

![](https://8aqnet.cdn.bcebos.com/94ed7ddc8a77747aeccde7e27f7d35ff.jpg)

A whole new Quick Edit in Cloudflare Workers

Loading...
*2023-5-17 21:0:57
Author: [blog.cloudflare.com(查看原文)](/jump-163801.htm)
阅读量:50
收藏*

---

Loading...

* [![Samuel Macleod](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/04/IMG_5133.jpg)](https://blog.cloudflare.com/author/samuel/)
* [![Adam Murray](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/04/adam_headshot-1.jpg)](https://blog.cloudflare.com/author/adam-murray/)

![A whole new Quick Edit in Cloudflare Workers](https://blog.cloudflare.com/content/images/2023/05/image1-42.png)

Quick Edit is a development experience for Cloudflare Workers, embedded right within the Cloudflare dashboard. It’s the fastest way to get up and running with a new worker, and lets you quickly preview and deploy changes to your code.

We’ve spent a lot of recent time working on upgrading the *local* development experience to be as [useful as possible](https://blog.cloudflare.com/miniflare-and-workerd/), but the Quick Edit experience for editing Workers has stagnated since the release of [workers.dev](https://blog.cloudflare.com/just-write-code-improving-developer-experience-for-cloudflare-workers/). It’s time to give Quick Edit some love and bring it up to scratch with the expectations of today's developers.

Before diving into what’s changed—a quick overview of the current Quick Edit experience:

![](https://blog.cloudflare.com/content/images/2023/05/download-11.png)

We used the robust [Monaco editor](https://microsoft.github.io/monaco-editor/?ref=blog.cloudflare.com), which took us pretty far—it’s even what VSCode uses under the hood! However, Monaco is fairly limited in what it can do. Developers are used to the full power of their local development environment, with advanced IntelliSense support and all the power of a full-fledged IDE. Compared to that, a single file text editor is a step-down in expressiveness and functionality.

## VSCode for Web

Today, we’re rolling out a new Quick Edit experience for Workers, powered by [VSCode for Web](https://code.visualstudio.com/docs/editor/vscode-web?ref=blog.cloudflare.com). This is a huge upgrade, allowing developers to work in a familiar environment. This isn’t just about familiarity though—using VSCode for Web to power Quick Edit unlocks significant new functionality that was previously only possible with a local development setup using [Wrangler](https://blog.cloudflare.com/10-things-i-love-about-wrangler/).

![](https://blog.cloudflare.com/content/images/2023/05/download--1--7.png)

### Support for multiple modules!

Cloudflare Workers released support for the [Modules syntax](https://blog.cloudflare.com/workers-javascript-modules/) in 2021, which is the recommended way to write Workers. It leans into modern JavaScript by leveraging the ES Module syntax, and lets you define Workers by exporting a default object containing event handlers.

```
export default {
 async fetch(request, env) {
   return new Response("Hello, World!")
 }
}
```

There are two sides of the coin when it comes to ES Modules though: exports *and imports*. Until now, if you wanted to organise your worker in multiple modules you had to use Wrangler and a local development setup. Now, you’ll be able to write multiple modules in the dashboard editor, and import them, just as you can locally. We haven’t enabled support for importing modules from npm yet, but that’s something we’re actively exploring—stay tuned!

![](https://blog.cloudflare.com/content/images/2023/05/download--2--6.png)

### Edge Preview

![](https://blog.cloudflare.com/content/images/2023/05/download--3--4.png)

When editing a worker in the dashboard, Cloudflare spins up a preview of your worker, deployed from the code you’re currently working on. This helps speed up the feedback loop when developing a worker, and makes it easy to test changes without impacting production traffic (see also, [wrangler dev](https://blog.cloudflare.com/announcing-wrangler-dev-the-edge-on-localhost/)).

However, the in-dashboard preview hasn’t historically been a high-fidelity match for the deployed Workers runtime. There were various differences in behaviour between the dashboard preview environment and a deployed worker, and it was difficult to have full confidence that a worker that worked in the preview would work in the deployed environment.

That changes today! We’ve changed the dashboard preview environment to use the same system that powers [`wrangler dev`](https://blog.cloudflare.com/announcing-wrangler-dev-the-edge-on-localhost/). This means that your preview worker will be run on Cloudflare's global network, the same environment as your deployed workers.

### Helpful error messages

In the previous dashboard editor, the experience when your code throws an error wasn’t great. Unless you wrap your worker code in a try-catch handler, the preview will show a blank page when your worker throws an error. This can make it really tricky to debug your worker, and is pretty frustrating. With the release of the new Quick Editor, we now wrap your worker with error handling code that shows helpful error pages, complete with error stack traces and detailed descriptions.

![](https://blog.cloudflare.com/content/images/2023/05/download--4--4.png)

### Typechecking

TypeScript is incredibly popular, and developers are more and more used to writing their workers in TypeScript. While the dashboard editor still only allows JavaScript files (and you’re unable to write TypeScript directly) we wanted to support modern typed JavaScript development as much as we could. To that end, the new dashboard editor has full support for [JSDoc TypeScript syntax](https://www.typescriptlang.org/docs/handbook/type-checking-javascript-files.html?ref=blog.cloudflare.com), with the TypeScript environment for workers (link) preloaded. This means that writing code with type errors will show a familiar squiggly red line, and Cloudflare APIs like HTMLRewriter will be autocompleted.

![](https://blog.cloudflare.com/content/images/2023/05/download--5--4.png)

## How we built it

It wouldn’t be a Cloudflare blog post without a deep dive into the nuts and bolts of what we’ve built!

First, an overview—how does this work at a high level? We embed VSCode for Web in the Cloudflare dashboard as an `iframe`, and communicate with it over a [`MessageChannel`](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel?ref=blog.cloudflare.com). When the `iframe` is loaded, the Cloudflare dashboard sends over the contents of your worker to a VSCode for Web extension. This extension seeds an in-memory filesystem from which VSCode for Web reads. When you edit files in VSCode for Web, the updated files are sent back over the same `MessageChannel` to the Cloudflare dashboard, where they’re uploaded as a previewed worker to Cloudflare's global network.

As with any project of this size, the devil is in the details. Let’s focus on a specific area —how we communicate with VSCode for Web’s `iframe` from the Cloudflare dashboard.

The [`MessageChannel`](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel?ref=blog.cloudflare.com) browser API enables relatively easy cross-frame communication—in this case, from an iframe embedder to the iframe itself. To use it, you construct an instance and access the `port1` and `port2` properties:

```
const channel = new MessageChannel()

// The MessagePort you keep a hold of
channel.port1

// The MessagePort you sen...