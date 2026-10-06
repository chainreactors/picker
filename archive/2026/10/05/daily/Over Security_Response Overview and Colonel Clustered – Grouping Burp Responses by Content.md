---
title: Response Overview and Colonel Clustered – Grouping Burp Responses by Content
url: https://www.darknet.org.uk/2026/10/response-overview-colonel-clustered-burp-response-grouping/
source: Over Security
date: 2026-10-05
fetch_date: 2026-10-06T08:25:17.791643
---

# Response Overview and Colonel Clustered – Grouping Burp Responses by Content

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet.org.uk is a cybersecurity site online since 2000. It covers security tools, technical research and hacking news, alongside an archive of earlier posts.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / Response Overview and Colonel Clustered – Grouping Burp Responses by Content

# Response Overview and Colonel Clustered – Grouping Burp Responses by Content

Published October 5, 2026 |

Views: 81

Sorting an Intruder attack by status code and length finds the responses that differ in size, and misses the ones that differ only in what they say. In the example Drew Kirkpatrick uses to introduce Colonel Clustered, every response is the same size, yet for one ID value one of hundreds of lines differs – invisible in the length column.

![Burp Suite: Grouping responses by content. Two stacks of dark response cards and one separate orange-marked card; darknet.org.uk.](https://www.darknet.org.uk/wp-content/uploads/2026/10/burp-suite-response-overview-colonel-clustered-response-grouping-640x360.webp)

Response Overview and Colonel Clustered group Burp Suite responses by content to help identify unusual results.

Response Overview and Colonel Clustered are two [Burp Suite](https://www.darknet.org.uk/2007/01/burp-proxy-burp-suite-attacking-web-applications/) extensions that group responses by content instead. Response Overview files every eligible in-scope response as it arrives; Colonel Clustered groups a batch you send it.

Advertisement

## Response Overview: a threshold you set

Response Overview installs from the BApp Store, which lists version 1.6.0, updated 20 January 2026, for both Professional and Community.

The store’s instructions are short: add the target to scope, test as usual with any tool – Proxy, Scanner, Repeater, Intruder – then open the Response Overview tab, sort by any column and examine the small groups and unusual status codes. Right-click and choose **Hide item(s)** to clear what you have reviewed.

Each row is one representative response with its group size. A response is only compared with groups that share its HTTP status code, and within those it is measured against each group’s first member. It joins the first one it matches at the similarity threshold, 98% by default, or starts a new group.

By default it removes reflected request parameters before comparing – names and values longer than eight characters, with their decoded and encoded forms – so a long payload echoed back does not split a group.

By default it only looks at in-scope responses under 1 MiB – a limit you can change in its settings – and it skips uninteresting MIME types and file extensions and standard error pages from common web servers.

**What it can miss.** The similarity is a ratio in the style of Python’s difflib, computed on how often each byte occurs rather than on their order; the source says “ABBA and BAAB and BABA are all the same”.

Advertisement

Two responses that hold the same characters in a different arrangement can therefore land in one group, which a swapped pair of values in a table would do. Payloads of eight characters or fewer are not stripped, so short reflected input can still split groups.

Once 30 groups share a status code and body size, further responses with that status and size are skipped entirely, and the group sizes shown for them undercount – the source trades an accurate count for speed.

## Colonel Clustered: a threshold it picks

In Kirkpatrick’s walkthrough you run the Intruder attack to completion, select all the results, right-click and choose **Send to Colonel Clustered**, then switch to its “Col. Clustered” tab while the default Fast Scan runs.

The tab has four panes. Clusters, with their member counts and a separate Outliers group, sit top left; the members of whichever cluster you select sit below, with status code, length and Content-Type, sortable by column. The request and response viewers are on the right.

Read it from the small end: a single-member cluster, or an entry in Outliers, is the response that looked like nothing else. In the walkthrough he selects the single-member cluster and uses Burp Comparer to see exactly what differed.

Under the hood, each response is read by its Content-Type. HTML loses its tags and scripts, and its visible text is broken into five-character chunks, with digits sanitised so that changing IDs in a template do not split one page into many.

For JSON only the keys and their nesting are kept, ignoring the values. Anything binary is compared as five-byte sequences.

Identical token sets are merged, then the Fast Scan runs DBSCAN with the neighbour distance chosen by the Kneedle algorithm rather than by you. A slower Deep Analysis, started from a button, builds clusters hierarchically from Jaccard distances and sets its threshold from how the clusters merge.

**What it can miss.** The rules that keep templated pages together can also hide the difference you are fuzzing for, and this is the part I would check first.

A JSON response whose only change is a value – a different role, a different error string inside the same field – has the same keys as its neighbours and clusters with them. Sanitised digits mean a change confined to numbers, such as an ID, a count or a balance, may not separate a page either.

The author says the fast algorithm “worked well most of the time”. In his second example it lumped two clearly different responses into a large cluster, although Intruder’s size, status code and Content-Type columns would have shown them.

Deep Analysis put that pair in a cluster of their own. So when members of a large cluster differ in those columns, run Deep Analysis; it can be cancelled if it runs too slowly.

He gives O(n²) for the default and O(n³) for Deep Analysis, and would “hesitate to throw 50k responses at this plugin”, so send it a filtered slice of an attack.

## Side by side

|  | Response Overview | Colonel Clustered |
| --- | --- | --- |
| When it runs | Continuously, on eligible in-scope responses from any Burp tool | On demand, on the items you send it |
| Similarity threshold | Set by you, default 98% | Chosen automatically: Kneedle in Fast Scan; merge distances in Deep Analysis |
| What is compared | Byte frequencies; by default, reflected parameter names and values longer than eight characters are removed first | Content-aware tokens: visible text, JSON structure or bytes |
| Status code | Only responses with the same status are compared | Shown as a column; the README does not say it affects clustering |
| Can hide | The same bytes in a different order; short reflected payloads can split groups | Changed JSON values under unchanged keys; changes confined to digits |
| Getting it | BApp Store, Professional and Community | GitHub release jar or build; not in the BApp Store as of 29 September 2026 |

## Choosing between them

Response Overview is a background view of a whole engagement, available for Community from the BApp Store: set the scope, leave it running, and come back to the small groups.

If ordinary variation produces too many gro...