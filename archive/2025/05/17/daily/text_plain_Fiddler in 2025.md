---
title: Fiddler in 2025
url: https://textslashplain.com/2025/05/16/fiddler-in-2025/
source: text/plain
date: 2025-05-17
fetch_date: 2025-10-06T22:27:17.827167
---

# Fiddler in 2025

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Fiddler in 2025

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-05-162025-06-04](https://textslashplain.com/2025/05/16/fiddler-in-2025/)Posted in[dev](https://textslashplain.com/category/dev/), [fiddler](https://textslashplain.com/category/fiddler-2/)Tags:[debugging](https://textslashplain.com/tag/debugging/), [Fiddler](https://textslashplain.com/tag/fiddler/)

The Fiddler Web Debugger is now old enough to drink, but I still use it pretty much every day. Fiddler hasn’t aged entirely gracefully as platforms and standards have changed over the decades, but the tool is extensible enough that some of the shortcomings can be fixed by extensions and configuration changes.

[Last year](https://textslashplain.com/2024/11/24/fiddler-my-mistakes/), I looked back at a few of the mistakes and wins I had in developing Fiddler, and in this post, I explore how I’ve configured Fiddler to maximize my productivity today.

## Powerup with FiddlerScript & Extensions

#### Add a SingleBrowserMode button to Fiddler’s toolbar

By default, Fiddler registers itself as the system proxy and almost all applications on the system will immediately begin sending their traffic through Fiddler. While this can be useful, it often results in a huge amount of uninteresting “noise”, particularly for web developers hoping to see only browser traffic. Fiddler’s rich filtering system can hide traffic based on myriad criteria, but for performance and robustness reasons, it’s best not to have unwanted traffic going through Fiddler at all.

The easiest way to achieve that is to simply *not* register as the system proxy and instead just launch a single browser instance whose proxy settings are configured to point at Fiddler’s endpoint.

Adding a button to Fiddler’s toolbar to achieve this requires only a simple block of FiddlerScript:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | // Rules > Customize Rules, place this just inside the HANDLERS class… |
|  |  |
|  | // Add a button to Fiddler's UI for "Single Browser Mode", where only one browser window will |
|  | // send its traffic to Fiddler. |
|  | public static BindUIButton("SingleBrowserMode \uD83D\uDC40") |
|  | function LaunchSingleInstance() { |
|  | // Tell the system we're not the proxy anymore |
|  | FiddlerApplication.UI.actDetachProxy(); |
|  | // Launch a single browser instance pointed directly at Fiddler. |
|  | System.Diagnostics.Process.Start('msedge.exe', |
|  | '–user-data-dir="%temp%\\throwaway" –no-first-run –proxy-server=127.0.0.1:' + CONFIG.ListenPort.ToString() + " about:blank"); |
|  | } |

[view raw](https://gist.github.com/ericlaw1979/a39f743cc05daa6b77184057c01f7b6d/raw/15529ae0c553405ca180eaac92790a2a2c3ed54c/Single.js)
[Single.js](https://gist.github.com/ericlaw1979/a39f743cc05daa6b77184057c01f7b6d#file-single-js)
hosted with ❤ by [GitHub](https://github.com)

[![](https://textslashplain.com/wp-content/uploads/2025/05/image.png?w=236)](https://textslashplain.com/wp-content/uploads/2025/05/image.png)

A new button appears! #Awesomesauce

This button is probably the single most-valuable change I made to my copy of Fiddler in *years*, and I’m honestly a bit sick that I never thought to include this decades ago.

#### Disable ZSTD

[ZStandard](https://en.wikipedia.org/wiki/Zstd) is a very fast lossless compression algorithm that has seen increasing adoption over the last few years, joining `deflate/gzip` and `[brotli](https://textslashplain.com/2015/09/10/brotli/)`. Unfortunately, Telerik has not added support for Zstd compression to Fiddler Classic. While it would be *possible* to plumb support in via an extension, the simpler approach is to simply change outbound requests so that they don’t ask for this format from web servers.

Doing so is simple: just rewrite the `Accept-Encoding` request header:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | // Add just inside here: |
|  | // static function OnBeforeRequest(oSession: Session) { |
|  |  |
|  | // Don't request zstd content-encoding because Telerik didn't bother adding support. |
|  | if (oSession.RequestHeaders.ExistsAndContains("Accept-Encoding", "zstd")) { |
|  | oSession.RequestHeaders["Accept-Encoding"] = oSession.RequestHeaders["Accept-Encoding"].Replace(", zstd", ""); |
|  | } |

[view raw](https://gist.github.com/ericlaw1979/035821cfe22354d59bba3a83876eaf46/raw/54a1e672077af993ff78972ab48cf7f30185bb8e/no%20Zstd.js)
[no Zstd.js](https://gist.github.com/ericlaw1979/035821cfe22354d59bba3a83876eaf46#file-no-zstd-js)
hosted with ❤ by [GitHub](https://github.com)

#### Integrate with VirusTotal

Since moving to the Microsoft Defender team, I spend a lot more time looking at malicious files. You can integrate Fiddler into VirusTotal to learn more about any of the binaries it captures.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | public static ContextAction("Show Hashes") |
|  | function doHash(arrSess: Session[]) |
|  | { |
|  | for (var i: int=0; i<arrSess.Length; i++) |
|  | { |
|  | FiddlerObject.alert( |
|  | "\_MD5\_\n"+arrSess[i].GetResponseBodyHash("md5") + "\n\n" + |
|  | "\_SHA1\_\n"+arrSess[i].GetResponseBodyHash("sha1") + "\n\n" + |
|  | "\_SHA256\_\n"+arrSess[i].GetResponseBodyHash("sha256") + "\n" |
|  | ); |
|  | } |
|  | } |
|  |  |
|  |  |
|  | ContextAction("VirusTotal") |
|  | public static |
|  | function doVTCheck(arrSess: Session[]) |
|  | { |
|  |  |
|  | for (var i: int=0; i<arrSess.Length; i++) |
|  | { |
|  | var oS = arrSess[i]; |
|  | if (oS.bHasResponse) |
|  | { |
|  | Utilities.LaunchHyperlink(String.Format( |
|  | "<https://www.virustotal.com/en/file/>{0}/analysis/", |
|  | oS.GetResponseBodyHash("sha256").Replace("-",""))); |
|  | } |
|  | } |
|  | } |

[view raw](https://gist.github.com/ericlaw1979/f4ad91f5d7b3379ad237/raw/6c600a326e68f9c8b6cc0ecb7a8012670c01f2c1/HashSample.js)
[HashSample.js](https://gist.github.com/ericlaw1979/f4ad91f5d7b3379ad237#file-hashsample-js)
hosted with ❤ by [GitHub](https://github.com)

Beyond looking at hashes, I also spend far more time looking at malicious sites and binaries, many of which embed malicious content in base64 encoding. Fiddler’s **TextWizard** (`Ctrl+E`) offers a convenient way to transform Base64’d text back to the original bytes, and the Web Session List’s context menu’s “Copy > Response DataURI” allows you to easily base64 encode any data.

#### Add the NetLog Importer

If your goal isn’t to modify traffic with Fiddler, it’s often best not to have Fiddler capture browser traffic at all. Instead, direct your Chromium-based browser to [log its the traffic](https://textslashplain.com/2020/01/17/capture-network-logs-from-edge-and-chrome/) into a `NetLog.json` file which you can later import to Fiddler to analyze using the [Fiddler NetLog Importer](https://github.com/ericlaw1979/FiddlerImportNetlog/releases) extension.

[Learn about using F...