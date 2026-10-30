---
title: Continued Apache Struts2 JSON Plugin Insecure Deserialisation
url: https://seclists.org/fulldisclosure/2026/Oct/49
source: Full Disclosure
date: 2026-10-29
fetch_date: 2026-10-30T07:56:41.548117
---

# Continued Apache Struts2 JSON Plugin Insecure Deserialisation

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

[![Previous](/images/left-icon-16x16.png)](48)
[By Date](date.html#49)
[![Next](/images/right-icon-16x16.png)](50)

[![Previous](/images/left-icon-16x16.png)](47)
[By Thread](index.html#49)
[![Next](/images/right-icon-16x16.png)](50)

![](/shared/images/nst-icons.svg#search)

# Continued Apache Struts2 JSON Plugin Insecure Deserialisation

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 27 Oct 2026 16:59:24 +0000

---

```
Summary
Thus far we have written extensively about the rampant number of insecure JavaScript Object Notation (JSON)
deserialisers available today, like in "Struts2 and Related Framework Array/Collection DoS" (26 October 2025) and "JSON
Deserialiser Unconstrained Resource Consumption Quick Overview" (07 March 2026), along with a naïve proof of concept
script that demonstrated what we were talking about -- "JSON Deserialiser Unconstrained Resource Consumption Proof of
Concept" (29 August 2026).  Today we will continue analyse the Apache Struts2 JSON plugin, which serves as a clear case
study in how shallow input limits fail to protect against underlying architectural memory amplification bugs.

As previously mentioned, this vulnerability has existed and been known/exploited by members of this team across
numerous deserialisers for decades.  JSON and alternative format parsers (such as CBOR or multi-part forms) are
near-universally susceptible to this issue.  Some formats allow what we call "skip counting", which Apache Struts' base
deserialiser did for many years, but many simply do not properly control for memory growth as the parser deserialises
the data.  These flaws can be used to cause denial of service conditions, bypass authentication, inject unintended data
into the information system, and so much more based on what you do, how you do it, and what your goals are.  This work
will continue to focus on the DOS aspect to keep things simple and because it allows us to discuss the issue across
systems, rather than in specific contexts and use cases.

Evaluation of the WW-5618 and S2-072 Hardening Controls
First, let's walk through the timeline.  In October 2025, we reported the "greater issue" and, on 16 January 2026, we,
via VulnCheck, attempted to properly disclose the vulnerability to Apache.  Apache classified it as "not a
vulnerability" and, instead, took it as an opportunity to "harden" the code by putting in a few basic checks via PR
#1625 (https://github.com/apache/struts/pull/1625) and PR #1626 (https://github.com/apache/struts/pull/1626) (tracked
collectively as WW-5618, which shipped as version 6.9.0 on 27 April 2026 and version 7.2.1 on 15 June 2026).  In short,
on 17 March 2026 (after our second writing on the matter), they added in:

  *   struts.json.maxElements (default: 10,000)
  *   struts.json.maxDepth (default: 64)
  *   struts.json.maxLength (default: 2,097,152)
  *   struts.json.maxStringLength (default: 262,144)
  *   struts.json.maxKeyLength (default: 512)

In addition to each of those, the development team added input validation checks inside of `StrutsJSONreader`
(`JSONReader` was, effectively, renamed thereto as part of the aforementioned pulls -- it is now simply an interface)
that

  *   check the String length as it is built up (inside of `string(char)`)
  *   check the String length of a Map key (inside of `object()`)
  *   check the array depth when deserialising a collection, array, or similar object that is represented in JSON as a
JSON array (inside of `array()`)
  *   check the number of elements in the collection, array, or similar object that is represented in JSON as a JSON
array (inside of `array()`)

Later, Apache issues S2-072 in a further attempt to improve the input validation process.  The implementation, however,
fails to close the gap, due in part to the boundary checks being applied in isolation to individual collection
instances during recursion, rather than thereacross.  Today we'll look at the `array()` changes and how they have,
effectively, solved little, leaving information systems vulnerable to the same vulnerability that we continue to
discuss.

The Code
The following is taken directly from the official Apache Struts repository --
https://raw.githubusercontent.com/apache/struts/refs/heads/main/plugins/json/src/main/java/org/apache/struts2/json/StrutsJSONReader.java
 (27 October 2026):

    protected List<Object> array() throws JSONException {
        if (this.depth >= this.maxDepth) {
            throw new JSONException("JSON array nesting exceeds maximum allowed depth ("
                    + this.maxDepth + ").  Use " + JSONConstants.JSON_MAX_DEPTH + " to increase the limit.");
        }
        this.depth++;
        try {
            List<Object> ret = new ArrayList<>();
            Object value = this.read();

            while (this.token != ARRAY_END) {
                if (ret.size() >= this.maxElements) {
                    throw new JSONException("JSON array exceeds maximum allowed elements ("
                            + this.maxElements + ").  Use " + JSONConstants.JSON_MAX_ELEMENTS + " to increase the
limit.");
                }
                ret.add(value);

                Object read = this.read();
                if (read == COMMA) {
                    value = this.read();
                } else if (read != ARRAY_END) {
                    throw buildInvalidInputException();
                }
            }

            return ret;
        } finally {
            this.depth--;
        }
    }

The Process
First, to understand where they continue to go wrong, we have to understand how they operate:

  1.  Input traverses to StrutsJSONReader via a call to the public "read(String)" method.
  2.  It sets up an iterator, starts it on the first character, sets the depth to `0`, and then runs `read()`.
  3.  `read()`coordinates tokenisation and, upon seeing `[` outside of quotes (single or double), passes tokenisation
to `array()`, which is the code above.
  4.  `array()` checks its depth and, if too great, it throws an exception, otherwise it continues.
  5.  `array()` increments `depth`.
  6.  `array()` creates a new `ArrayList` to store the elements.
  7.  `array()` tokenises, via `read()` calls, until either its array has too many elements (at which point an
exception is thrown) or the array is ended (either via `]`, which is positive, or rude termination of the iterator).
  8.  `array()` decrements `depth` and returns the array to the caller.

The Deep Defect: Tracking Flaws & Heap Amplification
The problem with this process is that it protects only against a very small set of inputs.  For example, the obvious
array-of-arrays attack currently means that you can have 10,000^64 (or 1 x 10^256) elements via an array-of-arrays
structure because the limit checks are scoped per-instance of a single array context inside the recursion.

Understanding that the default maximum length is two megabytes (struts.json.maxLength), and assuming that a victim does
not adjust that value, we are talking about roughly 690,000 elements if the JSON is merely an array-of-arrays of empty
strings, or 419,000 elements if the JSON is an array-of-arrays of nulls or two-character Strings.  With those numbers,
you really only need a nesting depth of 2 to build a structure holding 100,000,000 elements - which is 10,000 * 10,000
and far more than fits the payload bill.

But that's not the full story.  We know that a pointer -- regardless of to what it points -- takes...