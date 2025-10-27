---
title: HTTPLoot - An Automated Tool Which Can Simultaneously Crawl, Fill Forms, Trigger Error/Debug Pages And "Loot" Secrets Out Of The Client-Facing Code Of Sites
url: https://buaq.net/go-140754.html
source: unSafe.sh - 不安全
date: 2022-12-21
fetch_date: 2025-10-04T02:04:15.694880
---

# HTTPLoot - An Automated Tool Which Can Simultaneously Crawl, Fill Forms, Trigger Error/Debug Pages And "Loot" Secrets Out Of The Client-Facing Code Of Sites

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

![](https://8aqnet.cdn.bcebos.com/a0e206feb6e8ccf289789d1b02c43826.jpg)

HTTPLoot - An Automated Tool Which Can Simultaneously Crawl, Fill Forms, Trigger Error/Debug Pages And "Loot" Secrets Out Of The Client-Facing Code Of Sites

An automated tool which can simultaneously crawl, fill forms, trigger error/debug pages and
*2022-12-20 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-140754.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRn3EIF1gQCjJwKK5mmZQx9kaEN7K0M1NXtqfATj_vlnuFnYra5m7zHDQV9MPtJoiaCjafhXelO7uhX8UmawtZThq9VdcZGO5U0HhE0QIDRxEPgdCi4g2n7zNLRcCg8_8UVIbpUse4Fm4eWr8D-LqtA3NudWI7kv-duCrney-j75s23gKYOdrZX-Y9Ng/w640-h402/HTTPLoot.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRn3EIF1gQCjJwKK5mmZQx9kaEN7K0M1NXtqfATj_vlnuFnYra5m7zHDQV9MPtJoiaCjafhXelO7uhX8UmawtZThq9VdcZGO5U0HhE0QIDRxEPgdCi4g2n7zNLRcCg8_8UVIbpUse4Fm4eWr8D-LqtA3NudWI7kv-duCrney-j75s23gKYOdrZX-Y9Ng/s965/HTTPLoot.png)

An [automated](https://www.kitploit.com/search/label/Automated "automated") tool which can simultaneously crawl, fill forms, trigger error/debug pages and "loot" secrets out of the client-facing code of sites.

## Usage

To use the tool, you can grab any one of the pre-built binaries from the [Releases](https://github.com/redhuntlabs/HTTPLoot/releases "Releases") section of the repository. If you want to build the source code yourself, you will need Go > 1.16 to build it. Simply running `go build` will output a usable binary for you.

Additionally you will need two json files ([lootdb.json](https://github.com/redhuntlabs/HTTPLoot/blob/master/lootdb.json "lootdb.json") and [regexes.json](https://github.com/redhuntlabs/HTTPLoot/blob/master/regexes.json "regexes.json")) alongwith the binary which you can get from the repo itself. Once you have all 3 files in the same folder, you can go ahead and fire up the tool.

Video demo:

Here is the help usage of the tool:

```
$ ./httploot --help
```

### Concurrent scanning

There are two flags which help with the concurrent scanning:

* `-concurrency`: Specifies the maximum number of sites to process concurrently.
* `-parallelism`: Specifies the number of links per site to crawl parallely.

Both `-concurrency` and `-parallelism` are crucial to [performance](https://www.kitploit.com/search/label/Performance "performance") and reliability of the tool results.

### Crawling

The crawl depth can be specified using the `-depth` flag. The integer value supplied to this is the maximum chain depth of links to crawl grabbed on a site.

An important flag `-wildcard-crawl` can be used to specify whether to crawl URLs outside the domain in scope.

> **NOTE**: Using this flag might lead to infinite crawling in worst case scenarios if the crawler finds links to other domains continuously.

### Filling forms

If you want the tool to scan for debug pages, you need to specify the `-submit-forms` argument. This will direct the tool to autosubmit forms and try to trigger error/debug pages *once a tech stack has been identified successfully*.

If the `-submit-forms` flag is enabled, you can control the string to be submitted in the form fields. The `-form-string` specifies the string to be submitted, while the `-form-length` can control the length of the string to be randomly generated which will be filled into the forms.

### Network tuning

Flags like:

* `-timeout` - specifies the HTTP timeout of requests.
* `-user-agent` - specifies the user-agent to use in HTTP requests.
* `-verify-ssl` - specifies whether or not to verify SSL certificates.

### Input/Output

Input file to read can be specified using the `-input-file` argument. You can specify a file path containing a list of URLs to scan with the tool. The `-output-file` flag can be used to specify the result output file path -- which by default goes into a file called `httploot-results.csv`.

## Further Details

Further details about the research which led to the development of the tool can be found on our [RedHunt Labs Blog](https://redhuntlabs.com/blog/the-http-facet-httploot.html "RedHunt Labs Blog").

## License & Version

The tool is licensed under the MIT license. See LICENSE.

Currently the tool is at v0.1.

## Credits

The RedHunt Labs Research Team would like to extend credits to the creators & maintainers of [shhgit](https://github.com/eth0izzle/shhgit "shhgit") for the [regular expressions](https://www.kitploit.com/search/label/Regular%20Expressions "regular expressions") provided by them in their repository.

**[`To know more about our Attack Surface Management platform, check out NVADR.`](https://redhuntlabs.com/nvadr "An automated tool which can simultaneously crawl, fill forms, trigger error/debug pages and loot secrets out of the client-facing code of sites. (10)")**

HTTPLoot - An Automated Tool Which Can Simultaneously Crawl, Fill Forms, Trigger Error/Debug Pages And "Loot" Secrets Out Of The Client-Facing Code Of Sites
![HTTPLoot - An Automated Tool Which Can Simultaneously Crawl, Fill Forms, Trigger Error/Debug Pages And "Loot" Secrets Out Of The Client-Facing Code Of Sites](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRn3EIF1gQCjJwKK5mmZQx9kaEN7K0M1NXtqfATj_vlnuFnYra5m7zHDQV9MPtJoiaCjafhXelO7uhX8UmawtZThq9VdcZGO5U0HhE0QIDRxEPgdCi4g2n7zNLRcCg8_8UVIbpUse4Fm4eWr8D-LqtA3NudWI7kv-duCrney-j75s23gKYOdrZX-Y9Ng/s72-w640-c-h402/HTTPLoot.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/httploot-automated-tool-which-can.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)