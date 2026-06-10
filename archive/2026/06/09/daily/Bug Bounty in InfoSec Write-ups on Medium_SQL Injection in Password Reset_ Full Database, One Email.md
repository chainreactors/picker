---
title: SQL Injection in Password Reset: Full Database, One Email
url: https://infosecwriteups.com/sql-injection-in-password-reset-full-database-one-email-f091269b9fec?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-09
fetch_date: 2026-06-10T06:15:30.703946
---

# SQL Injection in Password Reset: Full Database, One Email

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-in-password-reset-full-database-one-email-f091269b9fec&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-in-password-reset-full-database-one-email-f091269b9fec&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f091269b9fec---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f091269b9fec---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# SQL Injection in Password Reset: Full Database, One Email

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--f091269b9fec---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--f091269b9fec---------------------------------------)

7 min read

·

21 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Df091269b9fec&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsql-injection-in-password-reset-full-database-one-email-f091269b9fec&source=---header_actions--f091269b9fec---------------------post_audio_button------------------)

Share

**A** `ukey` **token in a forgot-password email handed me full read access to every record in their database. Reported in early 2025. Still live.**

Press enter or click to view image in full size

![]()

I had their entire database in my terminal output.

Every table. Every user record. Every password hash stored since the application went live — sitting in plaintext SQLMap blocks, scrolling faster than I could read.

The endpoint that gave me this was one I had nearly dismissed. A `ukey` parameter appended to a password reset link. Sent to me by the application itself, in an email, as part of its normal forgot-password flow.

I had spent two days testing everything else on this site. Login form. Search. Profile fields. GET parameters. POST bodies. I had run the full sweep. Found nothing.

It was in the one link I almost didn’t click.

## SQL Injection on a Dead Website? I Was Certain It Was There

The site had all the signatures. Wappalyzer confirmed MariaDB. The UI looked like it hadn’t been touched since 2014 — misaligned div containers, unsuppressed server warnings, error messages that came back in raw PHP output without any sanitization. Old sites with old codebases tend to have old assumptions about security. One of the oldest is that string concatenation in SQL queries is fine.

I was confident this site was vulnerable. I just could not find where.

I went through every visible input field I could find. Classic payloads — `'`, `' OR 1=1--`, `"OR"1"="1`, blind time-based delays. I ran SQLMap against every parameter that accepted user input. I tested GET parameters in the URL and POST bodies in Burp Suite. Login form. Search bar. Profile page. Contact form.

Nothing.

Not one error. Not one delay. Not one response that suggested the database was parsing my input differently. After two days of manual testing and an afternoon of automation, I was starting to think the Wappalyzer result was a false positive.

I almost moved on.

## The Forgot Password Form Broke the Wrong Way

I came back to the site one more time. No reason, really — just the kind of stubbornness that makes you keep a browser tab open for a week. I had not tested the forgot password flow yet. Not because I thought it was safe, but because I had not thought about it at all.

I opened the form and typed in a random Gmail address — not an email from the site’s own domain. Then submitted.

The page returned a PHP warning. Then a second PHP warning. Then a fatal error:

```
Warning: Trying to access array offset on null in /home/***/forgetpassword.php on line 15
Warning: Trying to access array offset on null in /home/***/forgetpassword.php on line 16
Fatal error: Uncaught mysqli_sql_exception: You have an error in your SQL syntax;
check the manual that corresponds to your MariaDB server version for the right syntax
to use near '$2y$10$...xU9AQ/EMry9Onw8OYNXh1ADng1prgi',1)' at line 1
in /home/***/forgetpassword.php:21
```

Press enter or click to view image in full size

![]()

The SQL query was being built around my input with string concatenation — no prepared statements, no parameterization. The forgot password function expected an email from the site’s own domain. When it received something else, the query broke and the full error surfaced.

That was a finding by itself. But I had not found what I came for.

I registered an account using a valid domain email, triggered the forgot password flow properly, and checked my inbox. The reset link arrived a few seconds later:

```
https://helloxyz.com/forgetpassword.php?ukey=<hash>
```

I read the URL. I read it again.

`ukey` was a bcrypt hash. `$2y$10$` — I could see the beginning of it before the path was cut off. The server was receiving this value in a GET parameter and using it to look up the user session.

I opened Burp Repeater and added a single quote to the end of the hash.

## The `ukey` Token — Full Database, One Payload

The server response came back immediately:

```
Fatal error: Uncaught mysqli_sql_exception: You have an error in your SQL syntax...
forgetpassword.php on line 21
```

The same error. Same line. The `ukey` parameter was hitting the database raw — no sanitization, no parameterized query, nothing between my modified value and the SQL interpreter.

## Get LordofHeaven’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I pointed SQLMap at the endpoint:

```
sqlmap -u "https://helloxyz.com/forgetpassword.php?ukey=HASH" \
  --level=5 --risk=3 --dbs --batch
```

Union-based injection. Error-based injection. Both techniques confirmed. Within a few minutes, SQLMap had listed every database on the server. I ran the table enumeration. Then the column dump.

User records. Admin credentials. Email addresses. Session tokens. Password hashes. Everything that had been stored since the application went live — fully readable, no authentication required beyond having the URL from a reset email.

I attempted to escalate. File read via `LOAD_FILE()`. OS command execution via `INTO OUTFILE` and UDF injection. None of the escalation paths opened — the MySQL user running the queries did not have file or super privileges. RCE was of...