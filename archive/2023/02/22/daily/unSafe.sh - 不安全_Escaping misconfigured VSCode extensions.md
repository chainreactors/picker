---
title: Escaping misconfigured VSCode extensions
url: https://buaq.net/go-150388.html
source: unSafe.sh - 不安全
date: 2023-02-22
fetch_date: 2025-10-04T07:41:08.997150
---

# Escaping misconfigured VSCode extensions

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

![](https://8aqnet.cdn.bcebos.com/8ae5ff5bc591fd23e5c4a84de46228a4.jpg)

Escaping misconfigured VSCode extensions

TL;DR: This two-part blog series will cover how I found and disclosed three vulne
*2023-2-21 21:0:50
Author: [blog.trailofbits.com(查看原文)](/jump-150388.htm)
阅读量:33
收藏*

---

**TL;DR:** This two-part blog series will cover how I found and disclosed three vulnerabilities in VSCode extensions and one vulnerability in VSCode itself (a security mitigation bypass assigned [CVE-2022-41042](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-41042) and awarded a $7,500 bounty). We will identify the underlying cause of each vulnerability and create fully working exploits to demonstrate how an attacker could have compromised your machine. We will also recommend ways to prevent similar issues from occurring in the future.

A few months ago, I decided to assess the security of some VSCode extensions that we frequently use during audits. In particular, I looked at two Microsoft extensions: SARIF viewer, which helps visualize static analysis results, and Live Preview, which renders HTML files directly in VSCode.

Why should you care about the security of VSCode extensions? As we will demonstrate, vulnerabilities in VSCode extensions—especially those that parse potentially untrusted input—can lead to the compromise of your local machine. In both the extensions I reviewed, I found a high-severity bug that would allow an attacker to steal all of your local files. With one of these bugs, an attacker could even steal your SSH keys if you visited a malicious website while the extension is running in the background.

During this research, I learned about VSCode Webviews—sandboxed UI panels that run in a separate context from the main extension, analogous to an iframe in a normal website—and researched avenues to escape them. In this post, we’ll dive into what VSCode Webviews are and analyze three vulnerabilities in VSCode extensions, two of which led to arbitrary local file exfiltration. We will also look at some interesting exploitation tricks: leaking files using DNS to bypass restrictive Content-Security-Policy (CSP) policies, using `srcdoc` iframes to execute JavaScript, and using DNS rebinding to elevate the impact of our exploits.

In an upcoming blog post, we’ll examine a bug in VSCode itself that allows us to escape a Webview’s sandbox even in a well-configured extension.

## VSCode Webviews

Before diving into the bugs, it’s important to understand how aVSCode extension is structured. VSCode is an Electron application with privileges to access the filesystem and execute arbitrary shell commands; extensions have all the same privileges. This means that if an attacker can execute JavaScript (e.g., through an XSS vulnerability) in a VSCode extension, they can achieve a full compromise of the system.

As a defense-in-depth protection against XSS vulnerabilities, extensions have to create UI panels inside sandboxed Webviews. These Webviews don’t have access to the NodeJS APIs, which allow the main extension to read files and run shell commands. Webviews can be further limited with several options:

* `enableScripts`: prevents the Webview from executing JavaScript if set to `false`. Most extensions require `enableScripts: true`.
* `localResourceRoots`: prevents Webviews from accessing files outside of the directories specified in `localResourceRoots`. The default is the current workspace directory and the extension’s folder.
* `Content-Security-Policy`: mitigates the impact of XSS vulnerabilities by limiting the sources from which the Webview can load content (images, CSS, scripts, etc.). The policy is added through a meta tag of the Webview’s HTML source, such as:

Sometimes, these Webview panels need to communicate with the main extension to pass some data or ask for a privileged operation that they cannot perform on their own. This communication is achieved by using the `postMessage()` API.

Below is a simple, commented example of how to create a Webview and how to pass messages between the main extension and the Webview.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-21-at-9.20.57-AM.png?resize=690%2C901&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-21-at-9.20.57-AM.png?ssl=1)

Example of a simple extension that creates a Webview

An XSS vulnerability inside the Webview should not lead to a compromise if the following conditions are true: `localResourceRoots` is correctly set up, the CSP correctly limits the sources from which content can be loaded, and no `postMessage` handler is vulnerable to problems such as command injection. Still, you should not allow arbitrary execution of untrusted JavaScript inside a Webview; these security features are in place as a defense-in-depth protection. This is analogous to how a browser does not allow a renderer process to execute arbitrary code, even though it is sandboxed.

You can read more about Webviews and their security model in [VSCode’s documentation for Webviews](https://code.visualstudio.com/api/extension-guides/webview#security).

Now that we understand Webviews a little better, let’s take a look at three vulnerabilities that I found during my research and how I was able to escape Webviews and exfiltrate local files in two VSCode extensions built by Microsoft.

## Vulnerability 1: HTML/JavaScript injection in Microsoft’s SARIF viewer

[Microsoft’s SARIF viewer](https://marketplace.visualstudio.com/items?itemName=MS-SarifVSCode.sarif-viewer) is a VSCode extension that parses SARIF files—a JSON-based file format into which most static analysis tools output their results—and displays them in a browsable list.

Since I use the SARIF viewer extension in all of our audits to triage static analysis results, I wanted to know how well it was protected against loading untrusted SARIF files. These untrusted files can be downloaded from an untrusted source or, more likely, result from running a static analysis tool—such as CodeQL or Semgrep—with a malicious rule containing metadata that can manipulate the resulting SARIF file (e.g., the finding’s description).

While examining the code where the SARIF data is rendered, I came across a suspicious-looking snippet in which the description of a static analysis result is rendered using the `ReactMarkdown` class with the `escapeHtml` option set to `false`.

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-17-at-6.04.45-PM.png?resize=690%2C34&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-17-at-6.04.45-PM.png?ssl=1)

Code that unsafely renders the description of a finding parsed from a SARIF file ([source](https://github.com/microsoft/sarif-vscode-extension/blob/7215629a48bebb9bd36324549c34c7d58979a048/src/panel/details.tsx#L41))

Since HTML is not escaped, by controlling the `markdown` field of a result’s message, we can inject arbitrary HTML and JavaScript in the Webview. I quickly threw up a proof of concept (PoC) that automatically executed JavaScript using the `onerror` handler of an `img` with an invalid source.

[![Portion of a SARIF file that triggers JavaScript execution in the SARIF Viewer extension](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-16-at-4.20.57-PM.png?resize=690%2C117&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/Screenshot-2023-02-16-at-4.20.57-PM.png?ssl=1)

Portion of a SARIF file that triggers JavaScript execution in the SARIF Viewer extensi...