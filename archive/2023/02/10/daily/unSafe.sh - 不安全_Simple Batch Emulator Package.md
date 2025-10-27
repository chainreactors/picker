---
title: Simple Batch Emulator Package
url: https://buaq.net/go-148713.html
source: unSafe.sh - 不安全
date: 2023-02-10
fetch_date: 2025-10-04T06:12:33.611980
---

# Simple Batch Emulator Package

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

![](https://8aqnet.cdn.bcebos.com/f7c60f80c9fd7cc6ba16191ea7dab0e1.jpg)

Simple Batch Emulator Package

Skip to contentTo help in the analysis of malware which uses Windows batch
*2023-2-9 20:24:40
Author: [blog.cerbero.io(查看原文)](/jump-148713.htm)
阅读量:34
收藏*

---

[Skip to content](#content)

To help in the analysis of malware which uses Windows batch scripts we just released a package on Cerbero Store called “Simple Batch Emulator”. The name of the package is self-explanatory as it provides a basic emulator for batch scripts. The package is available to all commercial licenses of Cerbero Suite Advanced.

The following is a malicious OneNote document. All embedded files are automatically extracted thanks to the “OneNote Format” package.

[![](https://blog.cerbero.io/wp-content/uploads/2023/02/batchemu/1.png)](https://blog.cerbero.io/wp-content/uploads/2023/02/batchemu/1.png)

Two of the embedded files are batch scripts. We can execute the action to emulate the obfuscated batch code.

[![](https://blog.cerbero.io/wp-content/uploads/2023/02/batchemu/2.png)](https://blog.cerbero.io/wp-content/uploads/2023/02/batchemu/2.png)

In the output view we can see the hidden PowerShell code.

[![](https://blog.cerbero.io/wp-content/uploads/2023/02/batchemu/3.png)](https://blog.cerbero.io/wp-content/uploads/2023/02/batchemu/3.png)

The emulator can also be used programmatically:

```
from Pkg.SimpleBatchEmulator import *

script = r'''
set foo="hello"
echo %foo%
'''

emu = SimpleBatchEmulator(script)
emu.run()
```

The output of the code is:

```
echo: "hello"
```

The emulator allows single-step execution:

```
from Pkg.SimpleBatchEmulator import *

script = r'''
set foo="hello"
echo %foo%
'''

emu = SimpleBatchEmulator(script)
while emu.step():
    print("line:", emu.getCurrentLine(), "- variables:", emu.getVariables())
```

The output of the code is:

```
line: 1 - variables: {}
line: 2 - variables: {'foo': '"hello"'}
echo: "hello"
line: 3 - variables: {'foo': '"hello"'}
```

The “getCurrentLine” method returns the number of the line which is going to be executed by the next invocation of “step”. Therefore, the first line of the output reflects the state of the variables after the first line of the batch script, which in this case is an empty line.

## Post navigation

文章来源: https://blog.cerbero.io/?p=2524
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)