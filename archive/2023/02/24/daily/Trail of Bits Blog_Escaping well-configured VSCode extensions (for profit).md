---
title: Escaping well-configured VSCode extensions (for profit)
url: https://blog.trailofbits.com/2023/02/23/escaping-well-configured-vscode-extensions-for-profit/
source: Trail of Bits Blog
date: 2023-02-24
fetch_date: 2025-10-04T07:58:24.842210
---

# Escaping well-configured VSCode extensions (for profit)

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Escaping well-configured VSCode extensions (for profit)

[Vasco Franco](https://github.com/Vasco-jofra)

February 23, 2023

[vulnerability-disclosure](/categories/vulnerability-disclosure/)

[In part one](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/) of this two-part series, we escaped Webviews in real-world misconfigured VSCode extensions. But can we still escape extensions if they are well-configured?

In this post, we’ll demonstrate how I bypassed a Webview’s `localResourceRoots` by exploiting small URL parsing differences between the browser—i.e., the [Electron](https://www.electronjs.org/)-created Chromium instance where VSCode and its Webviews run—and other VSCode logic and an over-reliance on the browser to do path normalization. This bypass allows an attacker with JavaScript execution inside a Webview to read files anywhere in the system, including those outside the `localResourceRoots`. Microsoft assigned this bug `CVE-2022-41042` and awarded us a bounty of $7,500 (about $2,500 per minute of bug finding).

## Finding the issue

While exploiting the vulnerabilities detailed in the [last post](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/), I wondered if there could be bugs in VSCode itself that would allow us to bypass any security feature that limits what a Webview can do. In particular, I was curious if we could still exploit the bug we found in the SARIF Viewer extension (vulnerability 1 [in part 1](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/)) if there were stricter rules in the Webview’s `localResourceRoots` option.

From [last post](https://blog.trailofbits.com/2023/02/21/vscode-extension-escape-vulnerability/)’s SARIF viewer exploit, we learned that you can always exfiltrate files using DNS prefetches if you have the following preconditions:

* You can execute JavaScript in a Webview. This enables you to add `link` tags to the DOM.
* The CSP’s `connect-src` directive has the `.vscode-resource.vscode-cdn.net` source. This enables you to `fetch` local files.

**…Files within the `localResourceRoots` folders, that is!** This option limits the folders from which a Webview can read files, and, in the SARIF viewer, it was configured to limit, well… nothing. But such a permissive `localResourceRoots` is rare. Most extensions only allow access to files in the current workspace and in the extensions folder (the default values for the `localResourceRoots` option).

Recall that Webviews read files by fetching the `https://file+.vscode-resource.vscode-cdn.net` “fake” domain, as shown in the example below.

[![](/img/wpdump/8b4200cfd68173bfd86a0112b4d56cfc.png)](/img/wpdump/8b4200cfd68173bfd86a0112b4d56cfc.png)

Example of how to fetch a file from a VSCode extension Webview

Without even looking at how the code enforced the `localResourceRoots` option, I started playing around with different path traversal payloads with the goal of escaping from the root directories where we are imprisoned. I tried a few payloads, such as:

* `/etc/passwd`
* `/../../../../../etc/passwd`
* `/[valid_root]/../../../../../etc/passwd`

As I expected, this didn’t work. The browser normalized the request’s path even before it reached VSCode, as shown in the image below.

[![](/img/wpdump/7883a763654a363b024a508a97f682ba.png)](/img/wpdump/7883a763654a363b024a508a97f682ba.png)

Unsuccessful fetches of the `/etc/passwd` file

I started trying different variants that the browser would not normalize, but that some VSCode logic might consider a valid path. In about three minutes, to my surprise, I found out that using `%2f..` instead of `/..` allowed us to escape the root folder(!!!).

[![](/img/wpdump/a71c93de2af788e785a16bb5f13b79f7.png)](/img/wpdump/a71c93de2af788e785a16bb5f13b79f7.png)

Successful fetch of the `/etc/passwd` file when using the / character URL encoded as `%2f`

We’ve escaped! We can now fetch files from anywhere in the filesystem. But why did this work? VSCode seems to decode the `%2f`, but I couldn’t really understand what was happening under the hood. My initial assumption was that the function that reads the file (e.g., the `fs.readFile` function) was decoding the `%2f`, while the path normalization function did not. As we’ll see, this was not a bad guess, but not quite the real cause.

## Root cause analysis

Let’s start from the beginning and see how VSCode handles `vscode-resource.vscode-cdn.net` requests—remember, this is not a real domain.

It all starts in the [service worker](https://github.com/microsoft/vscode/blob/d00804ec9b15b4a8ee064f601de1aa4a31510e55/src/vs/workbench/contrib/webview/browser/pre/service-worker.js#L170-L324) running on the Webview. This service worker intercepts every Webview’s request to the `vscode-resource.vscode-cdn.net` domain and transforms it into a `postMessage('load-resource')` to the main VSCode thread.

[![](/img/wpdump/a165cd7cdc4fdc5f9ec81ff081bfc2dd.png)](/img/wpdump/a165cd7cdc4fdc5f9ec81ff081bfc2dd.png)

Code from the Webview’s service worker that intercepts fetch requests that start with `vscode-resource.vscode-cdn.net` and transforms them in a `postMessage` to the main VSCode thread ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/browser/pre/service-worker.js#L170-L373))

VSCode will handle the `postMessage('load-resource')` call by building a URL object and calling `loadResource`, as shown below.

[![](/img/wpdump/6ff64f350e2773e08aafb50f8ebdfcb2.png)](/img/wpdump/6ff64f350e2773e08aafb50f8ebdfcb2.png)

VSCode code that handles a `load-resource postMessage`. Highlighted in red is the code that decodes the fetched path—the first reason why our exploit works. ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/browser/webviewElement.ts#L357-L375))

Notice that the URL path is decoded with `decodeURIComponent`. This is why our `%2f` is decoded! But this alone still doesn’t explain why the path traversal works. Normalizing the path before checking if the path belongs to one of the roots would prevent our exploit. Let’s keep going.

The `loadResource` function simply calls `loadLocalResource` with `roots: localResourceRoots`.

[![](/img/wpdump/38094d3fd3995ac85713083de7219b93.png)](/img/wpdump/38094d3fd3995ac85713083de7219b93.png)

The `loadResource` function calling `loadLocalResource` with the `localResourceRoots` option ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/browser/webviewElement.ts#L811-L816))

Then, the `loadLocalResource` function calls `getResourceToLoad`, which will iterate over each root in `localResourceRoots` and check if the requested path is in one of these roots. If all checks pass, `loadLocalResource` reads and returns the file contents, as shown below.

[![](/img/wpdump/c70513778cfd2647c270ac5663c518c1.png)](/img/wpdump/c70513778cfd2647c270ac5663c518c1.png)

Code that checks if a path is within the expected root folders and returns the file contents on success. Highlighted in red is the `.startsWith` check without any prior normalization—the second reason our exploit works. ([source](https://github.com/microsoft/vscode/blob/7666d7acd4cb7382c6e4749166f713d1226ccd99/src/vs/workbench/contrib/webview/browser/resourceLoading.ts#L45-L130))

There is no path normalization, and the root check is done with `resourceFsPath.startsWith(rootPath)`. This is why our path traversal works! If our path is `[valid-root-path]/../../../../../etc/issue`, we’ll pass the `.startsWith` check even though our path points to somewhere outside of the root.

In summary, two mistakes allow our exploit:

* The VSCode extension calls `decodeURIComponent(path)` on t...