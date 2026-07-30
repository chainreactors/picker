---
title: Snowflake SQL Injection via Compile-Time Constant Folding with SYSTEM$WAIT
url: https://infosecwriteups.com/snowflake-sql-injection-via-compile-time-constant-folding-with-system-wait-81374a58e089?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-29
fetch_date: 2026-07-30T04:51:10.533388
---

# Snowflake SQL Injection via Compile-Time Constant Folding with SYSTEM$WAIT

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsnowflake-sql-injection-via-compile-time-constant-folding-with-system-wait-81374a58e089&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsnowflake-sql-injection-via-compile-time-constant-folding-with-system-wait-81374a58e089&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-81374a58e089---------------------------------------)

·

1. [The Starting Point](/?source=post_page-----81374a58e089---------------------------------------#a1c4 "The Starting Point")
2. [Snowflake runs your query in three phase](/?source=post_page-----81374a58e089---------------------------------------#a1a4 "Snowflake runs your query in three phase")
3. [Execution Failure vs Compilation Failure](/?source=post_page-----81374a58e089---------------------------------------#5cd5 "Execution Failure vs Compilation Failure")
4. [Why Normal Error-Based Payloads Failed](/?source=post_page-----81374a58e089---------------------------------------#2273 "Why Normal Error-Based Payloads Failed")
5. [The technique: SYSTEM$WAIT constant folding](/?source=post_page-----81374a58e089---------------------------------------#8faa "The technique: SYSTEM$WAIT constant folding")
6. [What Constant Folding Can and Cannot Reveal](/?source=post_page-----81374a58e089---------------------------------------#18e3 "What Constant Folding Can and Cannot Reveal")
7. [Fixing It](/?source=post_page-----81374a58e089---------------------------------------#b659 "Fixing It")
8. [Closing](/?source=post_page-----81374a58e089---------------------------------------#3ece "Closing")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-81374a58e089---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Bug Bounty

Bug Bounty Writeup

Bug Bounty Tips

Sql Injection

Snowflake

# **Snowflake SQL Injection via Compile-Time Constant Folding with** `SYSTEM$WAIT`

[![Alvin Ferdiansyah](https://miro.medium.com/v2/resize:fill:64:64/1*jCQW4Dcioim59s1E0JwOqQ@2x.jpeg)](https://alvinferd.medium.com/?source=post_page---byline--81374a58e089---------------------------------------)

[Alvin Ferdiansyah](https://alvinferd.medium.com/?source=post_page---byline--81374a58e089---------------------------------------)

7 min read

·

4 days ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D81374a58e089&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsnowflake-sql-injection-via-compile-time-constant-folding-with-system-wait-81374a58e089&source=---header_actions--81374a58e089---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

You have confirmed SQL injection against a Snowflake backend. The injected expression **executes**. The behavior is repeatable. The database is clearly processing your input.

**But you cannot extract a single value.** Every normal error-based extraction technique returns the same thing: HTTP 200, followed by an empty array. Only malformed payloads, such as an unmatched single quote, return a verbose SQL compilation error and even then, the response reveals parts of the generated query rather than the values you are trying to extract.

But perhaps the application is only hiding one category of database error. Snowflake produces another category earlier in the query lifecycle, and that second category still reaches the response. That gives us a path to go deeper and, eventually, reach full extraction. The technique in this write-up is about moving the failure from execution time to compilation time.

## The Starting Point

The vulnerable functionality was a reporting endpoint that generated dashboard data from a JSON request:

```
POST /api/v2/report/generate HTTP/1.1
Host: reports.[REDACTED].com
Content-Type: application/json
Authorization: Bearer <session_jwt>

{
...
...
  "filter_type": "1",
...
}
```

Under normal conditions, the endpoint returned several hundred rows. Injecting an expression into filter\_type changed the response:

```
{
  "filter_type": "1/(SELECT 0)"
}
```

The server responded with:

```
HTTP/1.1 200 OK
Content-Type: application/json

{"data":[]}
```

There was no stack trace, no database error, and no HTTP 500. Only an empty result.

The same thing happened with every standard extraction attempt:

```
1/(SELECT 0)                 → 200  {"data":[]}
TO_NUMBER(CURRENT_USER())    → 200  {"data":[]}
CAST(CURRENT_ROLE() AS INT)  → 200  {"data":[]}
1 AND 1=(SELECT 1/0)         → 200  {"data":[]}
```

This is where the injection can appear to become unreadable.

The payloads compile, begin executing, fail as intended, and then disappear into the same empty response.

So im starting to question further:

*Can I make Snowflake fail before execution begins?*

## Snowflake runs your query in three phase

A useful way to understand this behavior is to divide Snowflake query processing into three broad stages:

1. **Parsing.** Snowflake determines whether the SQL text is syntactically valid.
2. **Compilation.** it resolves identifiers, checks types, folds expressions, and builds the execution plan.
3. **Execution.** the compiled plan runs against the warehouse and accesses data.

Steps 1 and 2 happen before any data is touched. They run on the cloud services layer, and no warehouse is involved yet. Step 3 is where your query actually runs against tables, where runtime behavior occurs: scans, conversions involving row values, arithmetic failures, timeouts, and other failures produced while the plan is running.

This splits errors into two groups, and Snowflake numbers them differently:

```
Compilation errors → error code 0001, raised in step 2

Execution errors → error code 5001, raised in step 3
```

A compilation error means the query never ran. An execution error means it started running and then hit a problem.

## Execution Failure vs Compilation Failure

A reporting backend calls the database, and if the query blows up mid-flight it returns an empty result set so the dashboard renders instead of a stack trace. That handler almost always catches the **execution failure**, because that is the one that happens in normal operation: a bad row, a timeout, a type problem in the data.

Conceptually, the handler may behave like this:

```
Run query
    ↓
Execution succeeds  → return rows

Execution fails     → return []
```

But **compilation failures** are different. To the application they look like a bug in its own ...