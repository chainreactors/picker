---
title: Apache Struts2 Core Cross-Origin Protection Exemption Miskeyed to a Deployment-Wide Path
url: https://seclists.org/fulldisclosure/2026/Nov/3
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.451135
---

# Apache Struts2 Core Cross-Origin Protection Exemption Miskeyed to a Deployment-Wide Path

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 Core Cross-Origin Protection Exemption Miskeyed to a Deployment-Wide Path

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 29 Oct 2026 13:34:55 +0000

---

```
Description
Apache Struts2 Core version 7.4.0 and below's `FetchMetadataInterceptor`, `CoepInterceptor`, and `CoopInterceptor` each
compare their `exemptedPaths` configuration -- a per-interceptor-reference, administrator-supplied set of paths
intended to exempt specific actions from the corresponding cross-origin protection -- against
`HttpServletRequest.getContextPath()`.  `getContextPath()` is fixed for the entire deployed web application and is
identical on every request regardless of which action or servlet path is being invoked, so it cannot distinguish one
action from another.

Impact
An administrator who configures `exemptedPaths` expecting it to exempt a specific action or endpoint, instead is
configuring a value that can never match the real, single, deployment-wide context path returned on genuine traffic, so
the per-action exemption never takes effect and the intended protection remains enforced everywhere, including on the
endpoint the administrator believed was exempted.  More importantly, if an administrator's configured exemption string
happens to coincide with the application's actual context path -- such as if an administrator assumes that the
parameter takes a path-like value and supplies the deployment's own root or an equally-named segment --
`exemptedPaths.contains(contextPath)` evaluates to `true` on every single request to the application and Fetch Metadata
request filtering, the Cross-Origin Embedder Policy (COEP) header, and the Cross-Origin Opener Policy (COOP) header are
all silently disabled for the entire deployment (well beyond the endpoint that the administrator intended to exempt),
disabling the protections that such code is intended to provide across the entire application.

Examples
Sample Code
All three interceptors, each in `struts2-core`, apply the identical pattern -- a per-action `exemptedPaths` set
compared against the deployment-wide `getContextPath()` rather than against anything that actually varies per action.

```java
    private final Set<String> exemptedPaths = new HashSet<>();
    private final ResourceIsolationPolicy resourceIsolationPolicy = new StrutsResourceIsolationPolicy();

    @Inject(required = false)
    public void setExemptedPaths(String paths) {
        this.exemptedPaths.addAll(TextParseUtil.commaDelimitedStringToSet(paths));
    }

    @Override
    public String intercept(ActionInvocation invocation) throws Exception {
        ActionContext context = invocation.getInvocationContext();
        HttpServletRequest request = context.getServletRequest();

        addVaryHeaders(invocation);

        String contextPath = request.getContextPath();
        // Apply exemptions: paths/endpoints meant to be served cross-origin
        if (exemptedPaths.contains(contextPath)) {
            return invocation.invoke();
        }
```
Code snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/interceptor/FetchMetadataInterceptor.java,
lines 55-73

```java
    @Override
    public void beforeResult(ActionInvocation invocation, String resultCode) {
        HttpServletRequest req = invocation.getInvocationContext().getServletRequest();
        final String path = req.getContextPath();

        if (exemptedPaths.contains(path)) {
```
Snippet from `struts2-core`'s core/src/main/java/org/apache/struts2/interceptor/CoepInterceptor.java, lines 59-63

```java
    @Override
    public void beforeResult(ActionInvocation invocation, String resultCode) {
        HttpServletRequest request = invocation.getInvocationContext().getServletRequest();
        String path = request.getContextPath();

        if (isExempted(path)) {
```
Code from `struts2-core`'s core/src/main/java/org/apache/struts2/interceptor/CoopInterceptor.java, lines 61-65
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

### Current thread:

* **Apache Struts2 Core Cross-Origin Protection Exemption Miskeyed to a Deployment-Wide Path** *Daniel Owens via Fulldisclosure (Nov 01)*

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