---
title: Waf-Bypass - Check Your WAF Before An Attacker Does
url: https://buaq.net/go-155332.html
source: unSafe.sh - 不安全
date: 2023-03-27
fetch_date: 2025-10-04T10:45:24.384449
---

# Waf-Bypass - Check Your WAF Before An Attacker Does

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

![](https://8aqnet.cdn.bcebos.com/d318f69c10bff37ce89e67abfc616773.jpg)

Waf-Bypass - Check Your WAF Before An Attacker Does

WAF bypass Tool is an open source tool to analyze the security of any WAF for False Positive
*2023-3-26 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-155332.htm)
阅读量:91
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgL3MLHu1cARwXIirYVPLX_4TlTK1evGLBNS7jVThufKErSdgIWSx7KQkobRZxVEvGnEi74WWDJ1cziEoefKuvYGqRyDMmQ88CNopkcs5ppKa3rqEqmskizyvmfCyrrR35j97E6sHFYbvqy2Xw-uBfv_kAq-1kVhSyJhjpkBTRmIOtMVUjEWpRzOJSNRg=w640-h496)](https://blogger.googleusercontent.com/img/a/AVvXsEgL3MLHu1cARwXIirYVPLX_4TlTK1evGLBNS7jVThufKErSdgIWSx7KQkobRZxVEvGnEi74WWDJ1cziEoefKuvYGqRyDMmQ88CNopkcs5ppKa3rqEqmskizyvmfCyrrR35j97E6sHFYbvqy2Xw-uBfv_kAq-1kVhSyJhjpkBTRmIOtMVUjEWpRzOJSNRg)

WAF bypass Tool is an open source tool to analyze the security of any WAF for False Positives and False Negatives using predefined and customizable payloads. Check your WAF before an attacker does. WAF Bypass Tool is developed by Nemesida WAF team with the participation of community.

## How to run

> It is forbidden to use for illegal and illegal purposes. Don't break the law. We are not responsible for possible [risks associated](https://www.kitploit.com/search/label/Risks%20Associated "risks associated") with the use of this software.

### Run from Docker

The latest waf-bypass always available via the [Docker Hub](https://hub.docker.com/r/nemesida/waf-bypass "Docker Hub"). It can be easily pulled via the following command:

```
# docker pull nemesida/waf-bypass
```

### Run source code from GitHub

```
# git clone https://github.com/nemesida-waf/waf_bypass.git /opt/waf-bypass/
# python3 -m pip install -r /opt/waf-bypass/requirements.txt
# python3 /opt/waf-bypass/main.py --host='example.com'
```

#### Options

* `'--proxy'` (`--proxy='[http://proxy.example.com:3128](http://proxy.example.com:3128 "http://proxy.example.com:3128")'`) - option allows to specify where to connect to instead of the host.
* `'--header'` (`--header 'Authorization: Basic YWRtaW46YWRtaW4=' --header 'X-TOKEN: ABCDEF'`) - option allows to specify the HTTP header to send with all requests (e.g. for authentication). Multiple use is allowed.
* `'--user-agent'` (`--user-agent 'MyUserAgent 1/1'`) - option allows to specify the HTTP User-Agent to send with all requests, except when the User-Agent is set by the payload (`"USER-AGENT"`).
* `'--block-code'` (`--block-code='403' --block-code='222'`) - option allows you to specify the HTTP status code to expect when the WAF is blocked. (default is `403`). Multiple use is allowed.
* `'--threads'` (`--threads=15`) - option allows to specify the number of parallel scan threads (default is `10`).
* `'--timeout'` (`--timeout=10`) - option allows to specify a request processing timeout in sec. (default is `30`).
* `'--json-format'` - an option that allows you to display the result of the work in JSON format (useful for integrating the tool with security platforms).
* `'--details'` - display the False Positive and False Negative payloads. Not available in `JSON` format.
* `'--exclude-dir'` - exclude the payload's directory (`--exclude-dir='SQLi' --exclude-dir='XSS'`). Multiple use is allowed.

## Payloads

Depending on the purpose, payloads are located in the appropriate folders:

* FP - False Positive payloads
* API - API testing payloads
* CM - Custom HTTP Method payloads
* GraphQL - GraphQL testing payloads
* LDAP - LDAP Injection etc. payloads
* LFI - Local File Include payloads
* MFD - multipart/form-data payloads
* NoSQLi - NoSQL injection payloads
* OR - [Open Redirect](https://www.kitploit.com/search/label/Open%20Redirect "Open Redirect") payloads
* RCE - [Remote Code Execution](https://www.kitploit.com/search/label/Remote%20Code%20Execution "Remote Code Execution") payloads
* RFI - Remote File Inclusion payloads
* SQLi - SQL injection payloads
* SSI - Server-Side Includes payloads
* SSRF - Server-side request forgery payloads
* SSTI - Server-Side Template Injection payloads
* UWA - Unwanted Access payloads
* XSS - Cross-Site Scripting payloads

### Write your own payloads

When compiling a payload, the following zones, method and options are used:

* URL - request's path
* ARGS - request's query
* BODY - request's body
* COOKIE - request's cookie
* USER-AGENT - request's user-agent
* REFERER - request's referer
* HEADER - request's header
* METHOD - request's method
* BOUNDARY - specifies the contents of the request's boundary. Applicable only to payloads in the MFD directory.
* ENCODE - specifies the type of payload encoding (`Base64`, `HTML-ENTITY`, `UTF-16`) in addition to the encoding for the payload. Multiple values are indicated with a space (e.g. `Base64 UTF-16`). Applicable only to for `ARGS`, `BODY`, `COOKIE` and `HEADER` zone. Not applicable to payloads in API and MFD directories. Not compatible with option `JSON`.
* JSON - specifies that the request's body should be in JSON format
* BLOCKED - specifies that the request should be blocked (FN testing) or not (FP)

Except for some cases described below, the zones are independent of each other and are tested separately (those if 2 zones are specified - the script will send 2 requests - alternately checking one and the second zone).

For the zones you can use `%RND%` suffix, which allows you to generate an arbitrary string of 6 letters and numbers. (e.g.: `param%RND=my_payload` or `param=%RND%` OR `A%RND%B`)

You can create your own payloads, to do this, create your own folder on the '/payload/' folder, or place the payload in an existing one (e.g.: '/payload/XSS'). Allowed data format is JSON.

#### API directory

API testing payloads located in this directory are automatically appended with a header `'Content-Type: application/json'`.

#### MFD directory

For MFD (multipart/form-data) payloads located in this directory, you must specify the `BODY` (required) and `BOUNDARY` (optional). If `BOUNDARY` is not set, it will be generated automatically (in this case, only the payload must be specified for the BODY, without additional data (`'... Content-Disposition: form-data; ...'`).

If a `BOUNDARY` is specified, then the content of the `BODY` must be formatted in accordance with the RFC, but this allows for multiple payloads in `BODY` a separated by `BOUNDARY`.

Other zones are allowed in this directory (e.g.: `URL`, `ARGS` etc.). Regardless of the zone, header `'Content-Type: multipart/form-data; boundary=...'` will be added to all requests.

Waf-Bypass - Check Your WAF Before An Attacker Does
![Waf-Bypass - Check Your WAF Before An Attacker Does](https://blogger.googleusercontent.com/img/a/AVvXsEgL3MLHu1cARwXIirYVPLX_4TlTK1evGLBNS7jVThufKErSdgIWSx7KQkobRZxVEvGnEi74WWDJ1cziEoefKuvYGqRyDMmQ88CNopkcs5ppKa3rqEqmskizyvmfCyrrR35j97E6sHFYbvqy2Xw-uBfv_kAq-1kVhSyJhjpkBTRmIOtMVUjEWpRzOJSNRg=s72-w640-c-h496)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/03/waf-bypass-check-your-waf-before.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)