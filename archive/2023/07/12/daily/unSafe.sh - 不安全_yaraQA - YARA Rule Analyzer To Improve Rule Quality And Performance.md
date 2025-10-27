---
title: yaraQA - YARA Rule Analyzer To Improve Rule Quality And Performance
url: https://buaq.net/go-171752.html
source: unSafe.sh - 不安全
date: 2023-07-12
fetch_date: 2025-10-04T11:51:38.412558
---

# yaraQA - YARA Rule Analyzer To Improve Rule Quality And Performance

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

yaraQA - YARA Rule Analyzer To Improve Rule Quality And Performance

YARA rules can be syntactically correct but still dysfunctional. yaraQA tries to find and report the
*2023-7-11 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-171752.htm)
阅读量:28
收藏*

---

YARA rules can be syntactically correct but still dysfunctional. yaraQA tries to find and report these issues to the author or maintainer of a YARA rule set.

I'm going to extend the test set over time. Each minor version will include new features or new tests.

Use a baseline to only see new issues (not the ones that you've already reviewed). The baseline file is an old JSON output of a reviewed state.

Example rules with issues can be found in the `./test` folder.

binary 0 in front or a space after the string). Every additional byte helps." }, { "rule": "Demo\_Rule\_3\_Fullword\_FilePath\_Section", "id": "SM3", "issue": "The rule uses a string with the modifier 'fullword' but it starts and ends with two backslashes and thus the modifier could lead to a dysfunctional rule.", "element": { "name": "$s1", "value": "\\\\ZombieBoy\\\\", "type": "text", "modifiers": [ "ascii", "fullword" ] }, "level": "warning", "type": "logic", "recommendation": "Remove the 'fullword' modifier" }, { "rule": "Demo\_Rule\_4\_Condition\_Never\_Matches", "id": "CE1", "issue": "The rule uses a condition that will never match", "element": { "condition\_segment": "2 of", "num\_of\_strings": 1 }, "level": "error", "type": "logic", "recommendation": "Fix the condition" }, { "rule": "Demo\_Rule\_5\_Condition\_Short\_String\_At\_Pos", "id": "PA1", "issue": "This rule looks for a short string at a particular position. A short string represents a short atom and could be rewritten to an expression using uint(x) at position.", "element": { "condition\_segment": "$mz at 0", "string": "$mz", "value": "MZ" }, "level": "warning", "type": "performance", "recommendation": "" }, { "rule": "Demo\_Rule\_5\_Condition\_Short\_String\_At\_Pos", "id": "PA2", "issue": "The rule contains a string that turns out to be a very short atom, which could cause a reduced performance of the complete rule set or increased memory usage.", "element": { "name": "$mz", "value": "MZ", "type": "text", "modifiers": [ "ascii" ] }, "level": "warning", "type": "performance", "recommendation": "Try to avoid using such short atoms, by e.g. adding a few more bytes to the beginning or the end (e.g. add a binary 0 in front or a space after the string). Every additional byte helps." }, { "rule": "Demo\_Rule\_6\_Condition\_Short\_Byte\_At\_Pos", "id": "PA1", "issue": "This rule looks for a short string at a particular position. A short string represents a short atom and could be rewritten to an expression using uint(x) at position.", "element": { "condition\_segment": "$mz at 0", "string": "$mz", "value": "{ 4d 5a }" }, "level": "warning", "type": "performance", "recommendation": "" }, { "rule": "Demo\_Rule\_6\_Condition\_Short\_Byte\_At\_Pos", "id": "PA2", "issue": "The rule contains a string that turns out to be a very short atom, which could cause a reduced performance of the complete rule set or increased memory usage.", "element": { "name": "$mz", "value": "{ 4d 5a }", "type": "byte" }, "level": "warning", "type": "performance", "recommendation": "Try to avoid using such short atoms, by e.g. adding a few more bytes to the beginning or the end (e.g. add a binary 0 in front or a space after the string). Every additional byte helps." }, { "rule": "Demo\_Rule\_6\_Condition\_Short\_Byte\_At\_Pos", "id": "SM3", "issue": "The rule uses a string with the modifier 'fullword' but it starts and ends with two backslashes and thus the modifier could lead to a dysfunctional rule.", "element": { "name": "$s1", "value": "\\\\Section\\\\in\\\\Path\\\\", "type": "text", "modifiers": [ "ascii", "fullword" ] }, "level": "warning", "type": "logic", "recommendation": "Remove the 'fullword' modifier" } ]" dir="auto">

```
[
```

文章来源: http://www.kitploit.com/2023/07/yaraqa-yara-rule-analyzer-to-improve.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)