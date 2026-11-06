---
title: Apache Struts2 Tiles Plugin <=7.4.0 and >=6.3.0 Preparer Cache Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Nov/11
source: Full Disclosure
date: 2026-11-05
fetch_date: 2026-11-06T08:41:45.852441
---

# Apache Struts2 Tiles Plugin <=7.4.0 and >=6.3.0 Preparer Cache Vulnerabilities

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

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 Tiles Plugin <=7.4.0 and >=6.3.0 Preparer Cache Vulnerabilities

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 4 Nov 2026 22:34:51 +0000

---

```
The Apache Struts2 Tiles plugin version <=7.4.0 (and >=6.3.0) codebase includes a `ViewPreparer` construct, replete
with multiple ViewPreparer factories, that contains several important vulnerabilities including unsynchronised,
unbounded caches.  The lack of proper synchronisation means that certain factories will create caches that race,
risking lost cache entries, corrupted internal bucket states under load (this can result in infinite loops that consume
large amounts of compute or time, among other things), expensive duplicate `put(Object, Object)` calls, and similar
issues.  The lack of an eviction process means that the cache can grow to arbitrary lengths, consume excessive amounts
of memory, especially since the information system fails to utilise a starting size.  These problems are compounded by
the cache being `protected`, directly exposing it across the package and any inheriting classes, as well as attackers
being able to control the key (if, for example, the cache is dynamically managed and attackers can set part of the key
or leveraging the vulnerability discussed in `Apache Struts2 Core Arbitrary Code Execution via OGNL Sandbox Escape` (01
November 2026) to call to create preparers, call to getPreparer, etc.).

Importantly, this file appears to have come from an older, known vulnerable, known buggy version of Tiles that was
placed into the Apache Struts2 codebase, instead of the Tiles 3 version, when the Apaches Tiles project was retired and
archived into the Apache Attic and, as such, when the Apache Struts2 maintainers decided to import at least a subset of
the Tiles codebase into their own.  By sucking in the buggy version, however, the Apache Struts2 Tiles plugin contained
within said codebase inherits all issues that the imported code contained.

Examples
BasicPreparerFactory Race and Lack of an Eviction Process
The Apache Struts2 Tiles container is initialised as an application-scoped singleton resource.  Each request to the
server utilises a separate thread, with each thread having access to the Tiles singleton.  If the requests execute
Tiles definitions that require view preparers, they will simultaneously invoke the factory instance being used, so it
is important that the factory utilise thread-safe constructs.  The `BasicPreparerFactory`, which is the default Tiles
`ViewPreparer` factory, however, leverages an unsynchronised `HashMap` keyed by the preparer name.

At issue are a couple of things.  First, there is a time-of-check, time-of-use (TOCTOU) race condition in
`getPreparer(String, Request)` -- this requires a proper lock or an atomic/locking call or, in a multi-threaded
context, which is what happens in a Tiles workflow, it is prone to racing.  Second, there simply isn't a limit to the
size of the Map and the default capacity is used.

This was the original design of Tiles and was a known issue, which manifested itself in denial of service (DoS)
conditions in certain use cases, but was generally "mitigated" by having Tiles initialised and setup as part of the
server start up routine (although plenty of systems still leveraged a more dynamic approach) -- the service would read
the tiles configuration at start up, create and stuff the cache then, using a serial process.  This design, however,
was still suboptimal, buggy, and problematic, even when used in that way, resulting in several overhauls and,
eventually, settling in Tiles 3.  The old process, regardless, was suboptimal even from the most basic of perspectives
-- since it was a one-time, start-up cost (typically -- again, developers and the like were free to, and often did,
perform dynamic building), there was little reason to utilise the default capacity -- the desired size and capacity was
trivially calculable and known, so it could and should have been set thereto to prevent excessive memory use, with a
better-tuned automatic resizing threshold.  That, of course, however, was the least of the problems, which is why Tiles
3 shifted to a `ConcurrentHashMap` (realistically, a sub-optimal solution, as it is generally best to control your own
resources since such structures can still race via TOCTOU -- e.g., ` if (!map.containsKey(key)) map.put(key, value);`--
and similar coding constructs).

```java
    /**
     * Maps a preparer name to the instantiated preparer.
     */
    protected Map<String, ViewPreparer> preparers;

    /**
     * Constructor.
     */
    public BasicPreparerFactory() {
        this.preparers = new HashMap<>();
    }

    /**
     * Create a new instance of the named preparerInstance.  This factory
     * expects all names to be qualified class names.
     *
     * @param name    the named preparerInstance
     * @param context current context
     * @return ViewPreparer instance
     */
    public ViewPreparer getPreparer(String name, Request context) {
        if (!preparers.containsKey(name)) {
            preparers.put(name, createPreparer(name));
        }

        return preparers.get(name);
    }
```
Code snippet from struts2-tiles-plugin's
plugins/tiles/src/main/java/org/apache/tiles/core/prepare/factory/BasicPreparerFactory.java, lines 44-71
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](10)
[By Date](date.html#11)
[![Next](/images/right-icon-16x16.png)](12)

[![Previous](/images/left-icon-16x16.png)](10)
[By Thread](index.html#11)
[![Next](/images/right-icon-16x16.png)](12)

### Current thread:

* **Apache Struts2 Tiles Plugin <=7.4.0 and >=6.3.0 Preparer Cache Vulnerabilities** *Daniel Owens via Fulldisclosure (Nov 04)*

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

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.or...