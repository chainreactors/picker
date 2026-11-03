---
title: Apache Struts2 REST Plugin Fails to Properly Parse Chunked	Requests
url: https://seclists.org/fulldisclosure/2026/Nov/2
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.547016
---

# Apache Struts2 REST Plugin Fails to Properly Parse Chunked	Requests

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 REST Plugin Fails to Properly Parse Chunked Requests

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 29 Oct 2026 12:33:43 +0000

---

```
Description
The Apache Struts2 REST Plugin's (version 7.4.0 and below) `ContentTypeInterceptor.intercept(ActionInvocation)` only
deserialises a request body and enforces the `struts.rest.content.maxLength` bound when
`HttpServletRequest#getContentLength()` returns a positive value.  `getContentLength()` returns `-1` whenever the
`Content-Length` header is absent, which normal and appropriate for any Hypertext Transfer Protocol (HTTP) request sent
with `Transfer-Encoding: chunked`, so the entire body-processing branch -- including the bounded-reader size check --
is skipped for every such request.

Impact
Any client that sends a chunked-encoded request body causes the action to be invoked as though no body had been sent at
all, with every body field silently left unbound and no exception, warning, or rejection raised to either the caller or
the server logs.  While a potentially minor or major detail, it is important to note that because the interceptor fails
to parse the request body, the `struts.rest.content.maxLength` guard provides no protection whatsoever, as the
`BoundedReader` that enforces it sits inside the branch that chunked requests never enter.  An attacker can, as such,
submit an arbitrarily large chunked body without the configured size ceiling ever being consulted, and any downstream
logic that assumes a submitted field was bound -- default-initialisation checks, business validation keyed to a
now-absent value, and the like -- will silently fall back to whatever behaviour applies when the field was never set.
It is important to note that the downstream logic is application-specific and that your application may do something
terribly wrong or may not depending on your specific code -- Apache's Struts2 REST Plugin merely introduces the
unexpected pathway -- and that interceptor ordering, additional interceptors, etc., may cause the body to still be
parsed and deserialised, only that the Apache Struts2 REST Plugin will not take part in such activities, which may
further complicate the severity calculation (if, for example, data flows through the REST Plugin and then into a custom
JSON deserialiser via another interceptor, the assumed "protections" of the REST Plugin would never have taken place
and the default path of your code may assume an INDEX or similar request).

Examples
Sample Code
`intercept(ActionInvocation)` guards the entire body-deserialisation and size-enforcement block on
`request.getContentLength() > 0`, so a chunked request -- for which `getContentLength()` legitimately returns `-1` --
falls straight through to `invocation.invoke()` with the body never read.

```java
    public String intercept(ActionInvocation invocation) throws Exception {
        HttpServletRequest request = ServletActionContext.getRequest();
        ContentTypeHandler handler = selector.getHandlerForRequest(request);

        Object target = invocation.getAction();
        if (target instanceof ModelDriven) {
            target = ((ModelDriven<?>) target).getModel();
        }

        if (request.getContentLength() > 0) {
            BoundedReader reader = new BoundedReader(openBodyReader(request), maxLength);
            try {
                applyRequestBody(invocation, handler, target, reader);
            } catch (Exception e) {
                if (reader.limitExceeded()) {
                    throw requestBodyTooLarge();
                }
                throw e;
            }
            if (reader.limitExceeded()) {
                throw requestBodyTooLarge();
            }
        }
        return invocation.invoke();
    }
```
Code snippet from `struts2-rest-plugin`'s
plugins/rest/src/main/java/org/apache/struts2/rest/ContentTypeInterceptor.java, lines 114-138, with line 123's `if
(request.getContentLength() > 0)` gating both `applyRequestBody()` and every `BoundedReader`/`maxLength` check; nothing
in this method, or any upstream code, separately inspects `Transfer-Encoding` and handles chunked encoding

Sample Dynamic Testing
The following was against the rest-showcase codebase, running Struts 7.5.0-SNAPSHOT, built on 28 October 2026.  The
first, an ordinary `Content-Length`-bearing submission, correctly binds `clientName` and creates a new order.  The
second, a byte-identical JavaScript Object Notation (JSON) body sent with `Transfer-Encoding: chunked` and no
`Content-Length` header, is never bound onto the model at all -- `validate()` fires against `clientName`'s untouched
Java default and the action rejects the request with only the ordinary field-validation error a caller would see for a
genuinely empty submission.  Importantly, how the information system behaves is dependent on the information system,
itself, so while the rest-showcase example behaves as such, yours may do something considerably worse.

```http
POST /rest-showcase/orders HTTP/1.1
Host: 127.0.0.1:8383
Content-Type: application/json
Accept: application/json
Content-Length: 47

{"clientName":"CalibrationNormal","amount":11}
```
Request -- an ordinary, `Content-Length`-bearing submission

```http
HTTP/1.1 201
Location: http://127.0.0.1:8383/rest-showcase/orders/6
```
Response -- `201`; the order is created with `clientName` correctly bound from the submitted body

```http
POST /rest-showcase/orders HTTP/1.1
Host: 127.0.0.1:8383
Content-Type: application/json
Accept: application/json
Transfer-Encoding: chunked

2f\r
{"clientName":"CalibrationChunked","amount":22}\r
0\r
\r

```
Request -- the byte-identical JavaScript Object Notation (JSON) body, now sent with `Transfer-Encoding: chunked` and
without a `Content-Length` header

```http
HTTP/1.1 400
Content-Type: application/json;charset=UTF-8

{"actionErrors":[],"fieldErrors":{"clientName":["The client name is empty"]}}
```
Response -- `400`; `clientName` was never bound, so `validate()` rejects the request as though an empty body had been
submitted with no indication that the chunked encoding itself was the cause; a subsequent `GET
/rest-showcase/orders.json` confirms that no order named `CalibrationChunked` was ever created whilst the first
request's `CalibrationNormal` order (`id: 6`) is present

Steps to Reproduce
Run the following self-contained script against a running rest-showcase deployment. It creates one order via an
ordinary request, attempts to create a second via a chunked request, confirms the chunked attempt was never bound, and
cleans up the one order it legitimately created, independently re-verifying the cleanup succeeded.

```python
#!/usr/bin/env python3
"""Standalone reproduction for "`Content-Length` Guard Skips Chunked Request
Body Processing" against the struts2-rest-plugin's ContentTypeInterceptor,
exercised live through rest-showcase's OrdersController.

Requires `pip install requests`.
"""
import sys
import time
import requests

BASE_URL = "http://127.0.0.1:8383/rest-showcase";

def chunked_body(payload: bytes):
    # A generator body forces requests/urllib3 to send Transfer-Encoding:
    # chunked with no Content-Length header at all -- the standard
    ...