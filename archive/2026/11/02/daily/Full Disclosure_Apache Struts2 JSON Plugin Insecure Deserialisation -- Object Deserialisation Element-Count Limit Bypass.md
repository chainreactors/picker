---
title: Apache Struts2 JSON Plugin Insecure Deserialisation -- Object Deserialisation Element-Count Limit Bypass
url: https://seclists.org/fulldisclosure/2026/Nov/0
source: Full Disclosure
date: 2026-11-02
fetch_date: 2026-11-03T08:51:59.749507
---

# Apache Struts2 JSON Plugin Insecure Deserialisation -- Object Deserialisation Element-Count Limit Bypass

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Apache Struts2 JSON Plugin Insecure Deserialisation -- Object Deserialisation Element-Count Limit Bypass

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 29 Oct 2026 11:16:48 +0000

---

```
As of the current versions of the Apache Struts2 JSON Plugin (e.g., version 7.4.0 and the 7.5.0 snapshot dated 28
October 2026), attackers can bypass the element-count limit purported to protect Object deserialisation added to said
code as part of the WW-5618 and S2-072 "hardening controls".  Please note that this vulnerability and the attack string
is different than the previously reported bypass against the JSON array deserialisation, which was discussed in detail
via "Continued Apache Struts2 JSON Plugin Insecure Deserialisation" (28 October 2026) and "Maximised JSON Array Attacks
-- "Let the Commas Hit the Floor" Proof of Concept" (28 October 2026).  Said previous discussions pertained strictly to
bypassing protections on array deserialisation, with distinct code paths, mistakes, and attack strings.

Description:
The information system's JavaScript Object Notation (JSON) object parser enforces the `maxElements` resource limit by
checking the size of the `HashMap` being populated rather than by counting the number of key-value pairs actually being
parsed, so a payload consisting of entirely repeated keys never grows the map past a single entry while incurring both
memory and compute costs.

Impact:
An attacker who can send a request body to any endpoint protected by a `JSONInterceptor` configured with a
`maxElements` ceiling (including the default value) can construct a JSON object consisting of an arbitrarily large
number of duplicate-key pairs -- for example, the same key repeated hundreds of thousands of times -- bounded only by
the value of `struts.json.maxLength`, and have every pair be fully parsed, hashed, and boxed before the `maxElements`
check ever has a chance to trip since `Map.put(Object, Object)` with an already-present key never increases the value
`ret.size()`.

Attackers can force disproportionate CPU and allocation work, memory usage (similar to that discussed in "Continued
Apache Struts2 JSON Plugin Insecure Deserialisation" (28 October 2026) and "Maximised JSON Array Attacks -- "Let the
Commas Hit the Floor" Proof of Concept" (28 October 2026)) with a single request and exhaust server resources across
concurrent requests.  For example, attackers can build a single object containing 262,143 String-Double key-value pairs
(only limited by `struts.json.maxLength`, to a 2MB string), with a single request consuming over 46MB and taking ~37ms
to parse and build on a pre-warmed system (assume 64-bit HotSpot JVM running with compressed oops and 8-byte alignment,
which is a standard configuration).  Making several concurrent requests of such a nature can quickly create denial of
service conditions.

Examples:

Sample Vulnerable Code

`StrutsJSONReader.object()` in the `struts2-json-plugin` module, enforces the `maxElements` ceiling by comparing the
size of the `HashMap` being populated against the limit immediately before every `put(Object, Object)` call, as shown
below.

```java

    protected Map<String, Object> object() throws JSONException {

        if (this.depth >= this.maxDepth) {

            throw new JSONException("JSON object nesting exceeds maximum allowed depth ("

                    + this.maxDepth + "). Use " + JSONConstants.JSON_MAX_DEPTH + " to increase the limit.");

        }

        this.depth++;

        try {

            Map<String, Object> ret = new HashMap<>();

            Object next = this.read();

            if (next != OBJECT_END) {

                String key = (String) next;

                validateKeyLength(key);

                while (this.token != OBJECT_END) {

                    this.read(); // should be a colon

                    if (this.token != OBJECT_END) {

                        if (ret.size() >= this.maxElements) {

                            throw new JSONException("JSON object exceeds maximum allowed elements ("

                                    + this.maxElements + "). Use " + JSONConstants.JSON_MAX_ELEMENTS + " to increase
the limit.");

                        }

                        ret.put(key, this.read());

                        if (this.read() == COMMA) {

                            Object name = this.read();

                            if (name instanceof String nextKey) {

                                key = nextKey;

                                validateKeyLength(key);

                            } else {

                                throw buildInvalidInputException();

                            }

                        }

                    }

                }

            }

            return ret;

        } finally {

            this.depth--;

        }

    }

```

Code snippet from `struts-2-json-plugin`'s plugins/json/src/main/java/org/apache/struts2/json/StrutsJSONReader.java,
lines 156-196

Importantly, attackers can further couple this with the previously disclosed Apache Struts2 JSON Plugin `maxElements`
bypass in the `array()` method in the same class (please see the aforementioned Full Disclosure postings for details).
While attackers can choose from a variety of Objects, `Double` is the most damaging for this particular attack since
they incur the cost of building and boxing/unboxing and are never cached (unlike `Long` and `String` objects).
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **Apache Struts2 JSON Plugin Insecure Deserialisation -- Object Deserialisation Element-Count Limit Bypass** *Daniel Owens via Fulldisclosure (Nov 01)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/t...