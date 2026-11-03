---
title: Apache Struts2 REST Plugin Untrimmed `Accept` Header Tokens Break Content Negation Fallback
url: https://seclists.org/fulldisclosure/2026/Nov/1
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.647338
---

# Apache Struts2 REST Plugin Untrimmed `Accept` Header Tokens Break Content Negation Fallback

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 REST Plugin Untrimmed `Accept` Header Tokens Break Content Negation Fallback

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 29 Oct 2026 11:34:48 +0000

---

```
Description
The Apache Struts2 REST Plugin's `DefaultContentTypeHandlerManager.getHandlerForResponse(HttpServletRequest,
HttpServletResponse)` splits the `Accept` header on commas and passes each resulting token directly to
`findHandler(String)` without trimming leading or trailing whitespace.  `findHandler(String)` only retries a trimmed
lookup when a token contains a semicolon (`;`), so a token that merely carries a leading space has no such fallback and
fails the direct map lookup.

Impact
Any client that sends a standard, comma-space-separated `Accept` header -- the typical of most Hypertext Transfer
Protocol (HTTP) client libraries -- triggers this.  As the lookup fails silently, `getHandlerForResponse()` falls
through to the `defaultExtension` handler instead of the content type the caller actually requested, silently returning
a representation that the client neither asked for nor can necessarily parse.  In deployments that rely on content
negotiation to select between differently-scoped representations of the same resource -- such as a minimal public
representation served as the default extension against a fuller representation only intended for a specific,
explicitly-requested type -- this fallback can cause the wrong representation to be returned, degrading
interoperability and, where the two representations differ in which fields they expose, create a data-exposure
vulnerability (insecure serialisation).  While attackers cannot choose the default representation, they can abuse this
to search for insecure serialisation, data exposures, and similar information disclosure issues, as well as to see if
there is a difference between various representations and the default.  Importantly, the default representation and
ensuing serialisation library can be used against the information system (a trivial task).

Examples
Sample Code
`getHandlerForResponse(HttpServletRequest, HttpServletResponse)` splits the raw `Accept` header on commas and sends
each token to `findHandler(String)`, whose direct map lookup only has a trimming fallback when the token contains a
semicolon, as shown below.

```java
    /**
     * Gets the handler for the response by looking at the extension of the request
     * @param request The request
     * @return The appropriate handler
     *
     * WW-4588: modified to get a handler for the response side and auto generate the response type
     * from the Accept: header
     *
     */
    @Override
    public ContentTypeHandler getHandlerForResponse(HttpServletRequest request, HttpServletResponse res) {

        String extension = getExtensionIfPresent(request.getRequestURI());
        if (extension == null) {
            extension = defaultExtension;
            final String acceptHeader = request.getHeader("accept") ;
            if (acceptHeader != null) {
                final String[] types = acceptHeader.split(",");
                for (final String type : types) {
                    final ContentTypeHandler handler = findHandler(type);
                    if (handler != null) {
                        return handler;
                    }
                }
            }
        }
        return handlersByExtension.get(extension);
    }

    private ContentTypeHandler findHandler(final String type) {
        ContentTypeHandler handler = handlersByContentType.get(type);
        if (handler == null) {
            // strip off encoding and search again (e.g., application/json;charset=ISO-8859-1)
            final int index = type.indexOf(';');
            if (index != -1) {
                return handlersByContentType.get(type.substring(0, index).trim());
            }
        }
        return handler;
    }
```
Code snippet from `struts2-rest-plugin`'s
plugins/rest/src/main/java/org/apache/struts2/rest/DefaultContentTypeHandlerManager.java, lines 128-158
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

### Current thread:

* **Apache Struts2 REST Plugin Untrimmed `Accept` Header Tokens Break Content Negation Fallback** *Daniel Owens via Fulldisclosure (Nov 01)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")