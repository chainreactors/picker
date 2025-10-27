---
title: Escaping well-configured VSCode extensions (for profit)
url: https://buaq.net/go-150725.html
source: unSafe.sh - 不安全
date: 2023-02-24
fetch_date: 2025-10-04T07:55:41.762457
---

# Escaping well-configured VSCode extensions (for profit)

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

![](https://8aqnet.cdn.bcebos.com/cb266b0429e1eb82234d7c21b7d7b137.jpg)

Escaping well-configured VSCode extensions (for profit)

By Vasco FrancoIn part one of this two-part series, we escaped Webviews in real-
*2023-2-23 21:0:42
Author: [blog.trailofbits.com(查看原文)](/jump-150725.htm)
阅读量:35
收藏*

---

***By Vasco Franco***

[In part one](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/) of this two-part series, we escaped Webviews in real-world misconfigured VSCode extensions. But can we still escape extensions if they are well-configured?

In this post, we’ll demonstrate how I bypassed a Webview’s `localResourceRoots` by exploiting small URL parsing differences between the browser—i.e., the [Electron](https://www.electronjs.org/)-created Chromium instance where VSCode and its Webviews run—and other VSCode logic and an over-reliance on the browser to do path normalization. This bypass allows an attacker with JavaScript execution inside a Webview to read files anywhere in the system, including those outside the `localResourceRoots`. Microsoft assigned this bug `CVE-2022-41042` and awarded us a bounty of $7,500 (about $2,500 per minute of bug finding).

## Finding the issue

While exploiting the vulnerabilities detailed in the [last post](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/), I wondered if there could be bugs in VSCode itself that would allow us to bypass any security feature that limits what a Webview can do. In particular, I was curious if we could still exploit the bug we found in the SARIF Viewer extension (vulnerability 1 [in part 1](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/)) if there were stricter rules in the Webview’s `localResourceRoots` option.

From [last post](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/)’s SARIF viewer exploit, we learned that you can always exfiltrate files using DNS prefetches if you have the following preconditions:

* You can execute JavaScript in a Webview. This enables you to add `link` tags to the DOM.
* The CSP’s `connect-src` directive has the `.vscode-resource.vscode-cdn.net` source. This enables you to `fetch` local files.

**…Files within the `localResourceRoots` folders, that is!** This option limits the folders from which a Webview can read files, and, in the SARIF viewer, it was configured to limit, well… nothing. But such a permissive `localResourceRoots` is rare. Most extensions only allow access to files in the current workspace and in the extensions folder (the default values for the `localResourceRoots` option).

Recall that Webviews read files by fetching the `<https://file+.vscode-resource.vscode-cdn.net>` “fake” domain, as shown in the example below.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-8.58.45-AM.png?resize=690%2C80&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-8.58.45-AM.png?ssl=1)

Example of how to fetch a file from a VSCode extension Webview

Without even looking at how the code enforced the `localResourceRoots` option, I started playing around with different path traversal payloads with the goal of escaping from the root directories where we are imprisoned. I tried a few payloads, such as:

* `/etc/passwd`
* `/../../../../../etc/passwd`
* `/[valid_root]/../../../../../etc/passwd`

As I expected, this didn’t work. The browser normalized the request’s path even before it reached VSCode, as shown in the image below.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.08.22-AM.png?resize=690%2C333&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.08.22-AM.png?ssl=1)

Unsuccessful fetches of the `/etc/passwd` file

I started trying different variants that the browser would not normalize, but that some VSCode logic might consider a valid path. In about three minutes, to my surprise, I found out that using `%2f..` instead of `/..`  allowed us to escape the root folder(!!!).

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.12.46-AM.png?resize=690%2C178&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.12.46-AM.png?ssl=1)

Successful fetch of the `/etc/passwd` file when using the / character URL encoded as `%2f`

We’ve escaped! We can now fetch files from anywhere in the filesystem. But why did this work? VSCode seems to decode the `%2f`, but I couldn’t really understand what was happening under the hood. My initial assumption was that the function that reads the file (e.g., the `fs.readFile` function) was decoding the `%2f`, while the path normalization function did not. As we’ll see, this was not a bad guess, but not quite the real cause.

## Root cause analysis

Let’s start from the beginning and see how VSCode handles `vscode-resource.vscode-cdn.net` requests—remember, this is not a real domain.

It all starts in the [service worker](https://github.com/microsoft/vscode/blob/d00804ec9b15b4a8ee064f601de1aa4a31510e55/src/vs/workbench/contrib/webview/browser/pre/service-worker.js#L170-L324) running on the Webview. This service worker intercepts every Webview’s request to the `vscode-resource.vscode-cdn.net` domain and transforms it into a `postMessage('load-resource')` to the main VSCode thread.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.24.03-AM.png?resize=690%2C563&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.24.03-AM.png?ssl=1)

Code from the Webview’s service worker that intercepts fetch requests that start with `vscode-resource.vscode-cdn.net` and transforms them in a `postMessage` to the main VSCode thread ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/browser/pre/service-worker.js#L170-L373))

VSCode will handle the `postMessage('load-resource')` call by building a URL object and calling `loadResource`, as shown below.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.25.57-AM.png?resize=690%2C382&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.25.57-AM.png?ssl=1)

VSCode code that handles a `load-resource postMessage`. Highlighted in red is the code that decodes the fetched path—the first reason why our exploit works. ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/browser/webviewElement.ts#L357-L375))

Notice that the URL path is decoded with `decodeURIComponent`. This is why our `%2f` is decoded! But this alone still doesn’t explain why the path traversal works. Normalizing the path before checking if the path belongs to one of the roots would prevent our exploit. Let’s keep going.

The `loadResource` function simply calls `loadLocalResource` with `roots: localResourceRoots`.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.28.51-AM.png?resize=690%2C158&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-22-at-9.28.51-AM.png?ssl=1)

The `loadResource` function calling `loadLocalResource` with the `localResourceRoots` option ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/b...