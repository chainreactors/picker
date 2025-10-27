---
title: Python &#x26; Notepad&#x2b;&#x2b;, (Sat, Sep 7th)
url: https://buaq.net/go-260753.html
source: unSafe.sh - 不安全
date: 2024-09-08
fetch_date: 2025-10-06T18:22:52.173615
---

# Python &#x26; Notepad&#x2b;&#x2b;, (Sat, Sep 7th)

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

![](https://8aqnet.cdn.bcebos.com/231ee5f1350ec50a89264fe50426d88e.jpg)

Python &#x26; Notepad&#x2b;&#x2b;, (Sat, Sep 7th)

PythonScript is a Notepad++ plugin that provides a Python interpreter to edit Notepad++ documents.
*2024-9-7 21:11:33
Author: [isc.sans.edu(查看原文)](/jump-260753.htm)
阅读量:18
收藏*

---

[PythonScript](https://npppythonscript.sourceforge.net/docs/latest/index.html) is a [Notepad++](https://notepad-plus-plus.org/) plugin that provides a Python interpreter to edit Notepad++ documents.

You install PythonScript in Notepad++ like this:

![](https://isc.sans.edu/diaryimages/images/20240907-084324.png)

![](https://isc.sans.edu/diaryimages/images/20240907-084414.png)

![](https://isc.sans.edu/diaryimages/images/20240907-084500.png)

![](https://isc.sans.edu/diaryimages/images/20240907-084529.png)

Use "New Script" to create a new Python script:

![](https://isc.sans.edu/diaryimages/images/20240907-084641.png)

As an example, I will create a template substitution script, something that I use often. You provide a substitution template as input, and then each line of the open document is substituted according to the given template.

First we create the script substitute.py:

![](https://isc.sans.edu/diaryimages/images/20240907-084923.png)

This is the template substitution script I developed:

```
def Substitute(contents, lineNumber, totalLines):
    contents = contents.rstrip('\n\r')
    if contents != '':
        editor.replaceLine(lineNumber, template.replace(token, contents))

token = notepad.prompt('Provide a token', 'Substitute token', '%%')
template = notepad.prompt('Provide a template', 'Substitute template', '')
if token != None and template != None:
    editor.forEachLine(Substitute)
```

You can paste it into Notepad++:

![](https://isc.sans.edu/diaryimages/images/20240907-091633.png)

I will now demonstrate the script on a new document I created in Notepad++: the list of today's top 10 scanning IP addresses:

![](https://isc.sans.edu/diaryimages/images/20240907-085812.png)

For each IP address, I want to generate a command that I will then execute.

The script can now be invoked to be executed on this open document like this:

![](https://isc.sans.edu/diaryimages/images/20240907-093325.png)

The first line of Python script substitute.py to be executed, is line 6 (*token = notepad.prompt...*). It prompts the user for a token string (default %%), this is a string that, when used in the template string, will be replaced by each line in the open document

![](https://isc.sans.edu/diaryimages/images/20240907-085841.png)

Line 7 prompts the user for a template string:

![](https://isc.sans.edu/diaryimages/images/20240907-085917.png)

When the user has not cancelled answering the prompts (tested in line 8), line 9 (*editor.forEachLine(Substitute)*) is executed: it runs function Substitute on each line of the document:

![](https://isc.sans.edu/diaryimages/images/20240907-085939.png)

Then I can copy/paste all these generated commands into a cmd.exe console:

![](https://isc.sans.edu/diaryimages/images/20240907-090043.png)

![](https://isc.sans.edu/diaryimages/images/20240907-090226.png)

This example is a bit contrived, as you could also use a for loop in the scripting shell to achieve the same result.

I also use this Python script often when I'm programming. Say that I want to hardcode this list of scanning IP addresses in a Python script. I can quickly create a Python list as follows:

![](https://isc.sans.edu/diaryimages/images/20240907-150202.png)

![](https://isc.sans.edu/diaryimages/images/20240907-150219.png)

![](https://isc.sans.edu/diaryimages/images/20240907-150246.png)

![](https://isc.sans.edu/diaryimages/images/20240907-150304.png)

And then I add the variable assignment statemnt and create a list:

![](https://isc.sans.edu/diaryimages/images/20240907-150350(1).png)

Didier Stevens

文章来源: https://isc.sans.edu/diary/rss/31240
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)