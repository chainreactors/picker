---
title: Auth Flows in a Partitioned World
url: https://buaq.net/go-158364.html
source: unSafe.sh - 不安全
date: 2023-04-13
fetch_date: 2025-10-04T11:33:25.804237
---

# Auth Flows in a Partitioned World

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

![](https://8aqnet.cdn.bcebos.com/faacb0ffefd4592fa87d90bf6e581534.jpg)

Auth Flows in a Partitioned World

Back in 2019, I explained how browsers’ cookie controls and privacy features present challenges
*2023-4-12 23:55:59
Author: [textslashplain.com(查看原文)](/jump-158364.htm)
阅读量:26
收藏*

---

Back in 2019, I explained how browsers’ cookie controls and privacy features present challenges for common longstanding [patterns for authentication flows](https://textslashplain.com/2019/07/05/challenges-with-federated-identity-in-modern-browsers/). Such flows often rely upon an **Identity Provider (IP)** having access to its own cookies both on top-level pages served by the IP *and* when the IP receives a HTTP request from an `XmlHttpRequest`/`fetch` or frame embedded in a **Relying Party** **(RP)**‘s website:

[![](https://textplain.files.wordpress.com/2023/04/image-17.png?w=1024)](https://textplain.files.wordpress.com/2023/04/image-17.png)

These auth flows will fail if the IP’s cookie is not accessible for *any* reason:

1. the cookie **wasn’t set** at all (blocked by a browser privacy feature), or
2. the cookie **isn’t sent** from the embedded context is blocked (e.g. by the browser’s “Block 3rd Party Cookies” option)
3. the cookie jar is **not shared** between a top-level IP page and a request to the IP from the RP’s page (e.g. [Cookie Partitioning](https://textslashplain.com/2022/07/27/new-recipes-for-cookies/#:~:text=The%20Easy%20Recipe%3A%20CHIPS))

While Cookie Partitioning is **opt-in** today, in late 2024, Chromium plans to start blocking all non-partitioned cookies in a 3rd Party context, meaning that authentication flows based on this pattern will no longer work. The IP’s top-level page will set the cookie, but subframes loaded from that IP in the RP’s page will use a cookie jar from a different **partition** and not “see” the cookie from the IP top-level page’s partition.

What’s a Web Developer to do?

### New Patterns

#### Approach 1: Subframe

The simplistic approach would be to have the authentication flow happen within the subframe that needs it. That is, the subframe to the IP within the RP asks the user to log in, and then the auth cookie is available within the partition and can be used freely.

Unfortunately, there are major downsides to this approach: every single relying party will have to do the same thing (no “single-sign on”), and worse, the user will have to be accustomed to entering their IP credentials within a page that *visually* has no relationship to the IP (because only the RP’s URL is shown in the browser UI). I would not recommend anyone build a design based on the user entering, for example, their `Google.com` password within `RandomApp.com`.

If we take that approach off the table, we need to think of another way to get an authentication token from the IP to the RP, which factors down to the question of “*How can we pass a short string of data between two cross-origin contexts?*” And this, fortunately, is a task which the web platform is well-equipped to solve.

#### Approach 2: URL Parameter

One approach is to simply pass the token as a URL parameter. For example, the `RP.com` website’s login button does something like:

```
window.open('https://IP.com/doAuth?returnURL=https://RP.com/AuthSuccess.aspx?token=$1', 'blank');
```

In this approach, the Identity Provider conducts its login flow, then navigates its tab back to the caller-provided “return URL”, passing the authentication token back as a URL parameter. The Relying Party’s `AuthSuccess.aspx` handler collects the token from the URL and does whatever it wants with it (setting it as a cookie in a first-party context, stores it in HTML5 `sessionStorage`, etc). When the token is needed to call an service requiring authentication, the Relying Party takes the token it stored and adds it to the call (inside an Auth header, as field in a POST body, etc).

One risk with this pattern is that, from the web browser’s perspective, it is nearly indistinguishable from [bounce tracking](https://github.com/privacycg/nav-tracking-mitigations/blob/main/bounce-tracking-explainer.md), whereby trackers may try to circumvent the browser’s privacy controls and continue to track a user even when 3rd party cookies are disabled. While it’s not clear that browsers will *ever* fully or effectively block bounce trackers, it’s certainly an area of active interest for them, so making our auth scheme look less like a bounce tracker seems useful.

#### Approach 3: postMessage

So, my current recommendation is that developers communicate their tokens using the HTML5 **[postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)** API. In this approach, the RP opens the IP and then waits to receive a message containing the token:

```
// rp.com
window.open('https://ip.com/doAuth?', '_blank');

window.addEventListener("message", (event) => {
    if (event.origin !== "https://ip.com") return;
    finalizeLoginWithToken(event.data.authToken);
    // ...
  },
  false
);
```

When the authentication completes in the popup, the IP sends a message to the RP containing the token:

```
// ip.com
function returnTokenToRelyingParty(sRPOrigin, sToken){
    window.opener.postMessage({'authToken': sToken}, sRPOrigin);
}
```

#### Approach 4: Broadcast Channel

Similar to the postMessage approach, an IP site can use HTML5’s [Broadcast Channel](https://developer.chrome.com/blog/broadcastchannel/) API to send messages between all of its contexts no matter where they appear. Unlike `postMessage` (which can pass messages beween any origins), a site can *only* use Broadcast Channel to send messages to its own origin. BroadcastChannel is [widely supported](https://caniuse.com/broadcastchannel) in modern browsers, but unlike `postMessage`, it is not available in Internet Explorer.

### Demo

You can see approaches #3 and #4 in use in [a simple Demo App](https://debugtheweb.com/test/auth/app.html).

Click the **Log me in! (Partitioned)** button in Chromium 114+ and you’ll see that the subframe doesn’t “see” the cookie that is present in the WebDbg.com popup:

[![](https://textplain.files.wordpress.com/2023/04/image-18.png?w=1024)](https://textplain.files.wordpress.com/2023/04/image-18.png)

Now, click the **postMessage(token) to RP** button in that popup and it will post a message from the popup to the frame that launched it, and that frame will then store the auth token in a cookie inside its own partition:

[![](https://textplain.files.wordpress.com/2023/04/image-19.png?w=1024)](https://textplain.files.wordpress.com/2023/04/image-19.png)

We’ve now used `postMessage` to explicitly share the auth token between the two IP contexts even though they are loaded within different cookie partitions.

### Shortcomings

The approaches outlined in this post avoid breakage caused by various current and future browser settings and privacy lockdowns. However, there are some downsides:

1. It requires effort on the part of the relying party and identity provider
2. By handling auth tokens in JavaScript, you can no longer benefit from the [httponly](https://textslashplain.com/2022/07/27/new-recipes-for-cookies/#:~:text=the%20HTTPOnly%20declaration%2C) option for cookies

-Eric

文章来源: https://textslashplain.com/2023/04/12/auth-flows-in-a-partitioned-world/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)