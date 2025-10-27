---
title: 從 2013 到 2023: Web Security 十年之進化與趨勢!
url: https://buaq.net/go-174296.html
source: unSafe.sh - 不安全
date: 2023-08-13
fetch_date: 2025-10-04T11:58:53.082825
---

# 從 2013 到 2023: Web Security 十年之進化與趨勢!

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

從 2013 到 2023: Web Security 十年之進化與趨勢!

TL;DR for Hackers & Researchers: this is a more conceptual talk for web developers. All are in Manda
*2023-8-12 16:0:0
Author: [blog.orange.tw(查看原文)](/jump-174296.htm)
阅读量:24
收藏*

---

TL;DR for Hackers & Researchers: this is a more conceptual talk for web developers. All are in Mandarin but you can check the slides [here](https://github.com/orangetw/My-Presentation-Slides#2023) if interested.

由於聽眾皆為網站開發者 (涵蓋前端、後端甚至架構師)，因此選用的攻擊手法力求簡單、可快速理解又有趣，不談到防禦手法也在因為短短 45 分鐘內絕對涵蓋不完，所以給自己訂下的小目標是: 只要有一項也好，如果開發者遇到同樣場景、腦中會跳出個紅色小框框警告好像有人講過，可以透過這樣的方式稍稍彌平網站開發者與資安從業人員間的差異，那我的目的就達成了!

[![](https://blogger.googleusercontent.com/img/a/AVvXsEics6XGN2a6fA0P6gktIpFf7fRAhtM6lzfj99aDB8zzfHXHIKxn6xsiMHFlsZBsTwduo4HHPnF2sMoZaHaQzXyg0wtvuUnphocyC2xhvu882NvEAuxvW5jzoROa6yTypvJ9o2xtxRXq3ZnmUPonVrWgDCMVJpYEgs2F-3zAsVWzvHj4FzEdr0Vzq3BAu3I=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEics6XGN2a6fA0P6gktIpFf7fRAhtM6lzfj99aDB8zzfHXHIKxn6xsiMHFlsZBsTwduo4HHPnF2sMoZaHaQzXyg0wtvuUnphocyC2xhvu882NvEAuxvW5jzoROa6yTypvJ9o2xtxRXq3ZnmUPonVrWgDCMVJpYEgs2F-3zAsVWzvHj4FzEdr0Vzq3BAu3I)

所以 Web Security 這十年到底有什麼發展呢? 如果要我用一個字形容，最貼切應該就是「捲」這個字了! Web Security 如今已經競爭到連一個位元組都要斤斤計較，例如 Nginx 經典的 [Off-by-Slash 問題](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf#toolbar=0&page=19)，到底什麼時候該加斜線什麼時候不該，相信懂得人都會露出會心一笑。

綜觀這十年間的 Web Security 發展，我總結出了以下四個趨勢 (以下純代表個人觀點，你可以不同意 :)

## 1. 架構層面的攻擊逐漸成為顯學

隨著網站架構日趨複雜，以往可以在 Single Server 下解決的問題，隨著 Reverse Proxy, Load Balance, Firewall, Cache Server 甚至 CDN 的引入都開始變得複雜，原有的網頁應用、網頁伺服器如何去跟這些新角色進行搭配，這些組合的互動如何引入新的攻擊面，這都是這十年來一直有人在探討的趨勢。 這裡我給出的案例是:

1. [Abusing HTTP hop-by-hop request headers](https://nathandavison.com/blog/abusing-http-hop-by-hop-request-headers) by Nathan Davison
   * [Case Study] [F5 iControl REST Endpoint Authentication Bypass Technical Deep Dive](https://www.horizon3.ai/f5-icontrol-rest-endpoint-authentication-bypass-technical-deep-dive/) by James Horseman
2. [Web Cache Deception Attack](https://omergil.blogspot.com/2017/02/web-cache-deception-attack.html) by Omer Gil
   * [Case Study] [Web Cache Deception Attack in PayPal Home Page](https://vimeo.com/249130093)
3. (遺珠之憾): [HTTP Desync Attacks: Request Smuggling Reborn](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) by James Kettle

## 2. 對底層邏輯重新梳理的攻擊

隨著資安意識、以及前後端框架的成熟，開發者已逐漸養成使用框架的習慣。為了因應這個趨勢，攻擊者不得不開始往框架、甚至程式語言底層挖掘，如早期的 SQL Injection，隨著 ORM 出現開始被大面積減緩，造成攻擊者開始往 ORM 實作尋找漏洞； 同理 XSS，隨著框架內建的保護已足以應付大部分的開發場景，攻擊者只能開始檢視實作玩起我繞你補的遊戲。

另一方面重新梳理一些便於開發者使用的框架邏輯也是這幾年發展的一個流派，例如在紅極一時的 [Spring4Shell](https://spring.io/security/cve-2022-22965) 漏洞表面上雖然問題出在 Data Binding 中，但認真梳理後會發現其主因還是在 Java Runtime 版本更新導致其底層內部機制改變受到影響。

在這個趨勢中我介紹了兩個針對程式語言底層的新攻擊手法:

1. [File Operation Induced Unserialization via the “phar://” Stream Wrapper](https://i.blackhat.com/us-18/Thu-August-9/us-18-Thomas-Its-A-PHP-Unserialization-Vulnerability-Jim-But-Not-As-We-Know-It-wp.pdf) by Sam Thomas
   * [Case Study] [LARAVEL <= V8.4.2 DEBUG MODE: REMOTE CODE EXECUTION](https://www.ambionics.io/blog/laravel-debug-rce)
2. [Prototype pollution attack in NodeJS application](https://github.com/HoLyVieR/prototype-pollution-nsec18/tree/master) by Olivier Arteau
   * [Case Study] [Exploiting prototype pollution – RCE in Kibana (CVE-2019-7609)](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/) by Michał Bentkowski

## 3. 不一致性所造成的攻擊面

隨著網站功能越趨複雜，資料在網站間的生命週期也越來越長! 一個使用者請求(一筆資料)可能經過中間層 Proxy/Cache Server 預處理、商業邏輯再處理、雲端 API 又處理，最後日誌伺服器又要再解釋一遍。 隨著處理資料的來源越多、各家來源對同一筆資料又存在著不同的解釋，解釋間的不一致就可能造成安全上的問題。

這幾年尤其有趣的是針對 RFC 解釋的攻擊，RFC 只定義了規範卻沒有說明該如何實作，造成不同實作間的差異造成問題，例如案例中光是 JavaScript 與 Erlang 對同一個 JSON 解讀的不一致就造成那麼多問題了，相信這也會是未來 Web Security 的重要趨勢之一!

1. [A New Era of SSRF - Exploiting URL Parser in Trending Programming Languages!](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf) by Orange Tsai
2. [Remote Code Execution in CouchDB](https://justi.cz/security/2017/11/14/couchdb-rce-npm.html) by Max Justicz

## 4. 跨應用組合所導致的新攻擊

在這個 Web 包山包海開發者什麼都要會的時代，傳統認為寫網站就不須接觸底層結果被 WebAssembly 打臉； 寫網站不須懂密碼學結果出現 Web 3.0，資訊安全從來都不只是一個單一學科，如果只熟悉自己的領域、很容易就會陷入思考誤區甚至被降維打擊! 這十年間 Web Security 也開始往跨應用的攻擊影響，無論是跨協議的組合、跨規範的誤用、跨領域的結合，甚至把不同的 Convention 組合在一起，例如 RFC 的命名規範剛好跟 HTTP 函數庫約定成俗的變數撞名所造成的資安漏洞，近幾年不時會冒出這種打破三觀的例子，讓人不得不佩服到底想像力多豐富才能把這八竿子打不著的東西組合再一起!

1. (Ticket Trick) [How I hacked hundreds of companies through their helpdesk](https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c) by Inti De Ceukelaire
2. [HTTPoxy Attack](https://httpoxy.org/)
3. [AvOracle: New Attack Vector Against Anti Virus](https://portswigger.net/daily-swig/av-oracle-new-hacking-technique-leverages-antivirus-to-steal-secrets) by Ryo Ichikawa and Ryota Shiga
4. (遺珠之憾) [Timeless Timing Attacks](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Timeless-Timing-Attacks.pdf) by Tom Van Goethem & Mathy Vanhoef

## 5. 當前端安全不只在前端…

本來整理四個打算點到為止就好，但總是很難把前端安全給移出發展趨勢外，反正四天王總會有五個人對吧! 就把前端安全當成大魔王吧。

伴隨 Web 2.0 / 3.0 的興起，網站開始以使用者為中心、儲存在使用者端的敏感資料也越來越多，這十年間從瀏覽器的興衰、新舊特性的加入到主流框架的切換，前端安全的發展其實完全可以自成一派、發展出許多酷炫技術，甚至倒還有那麼點鑽牛角尖的程度，不過由於前端安全很大一部分還是得基於使用者互動，往往相較之下比較不被那麼受到重視，但隨著 Headless Browser 以及 Electron-Based 桌面應用的發展這種偏見慢慢開始被打破!

首先是 Chromium 的廣泛應用，越來越多開發者會在伺服器端使用 Headless Browser 直接將網頁渲染成 PDF 或圖片，加上網頁爬蟲的盛行與測試的自動化，以往許多需要使用者互動的 XSS 現在都可以直接在伺服器端(或自動地)觸發，這些都是讓網頁前端安全與後端安全的邊界愈加模糊的一點。

另一個分水嶺則是 Electron-Based 桌面應用的流行 (當然手機 App 中的 Webview 同理)，當所有受歡迎的桌面應用例如 Slack, Discord, Trello, 甚至連寫程式用的 Visual Studio Code 都成為基於瀏覽器的桌面應用，以往被視為雞肋被認為只能竊取 Cookie 的 XSS 現在搖身一變，成為可以直接跳小算盤的高風險漏洞! 這裡可以看看 Microsoft Teams 的例子，如何透過一個 AngularJS 的特性在桌面應用中創造出 XSS、再透過 Prototype Pollution 完成整個攻擊鏈，透過一個訊息就可以完整控制受害者!

1. [How I Hacked Microsoft Teams and got $150,000 in Pwn2Own](https://speakerdeck.com/masatokinugawa/how-i-hacked-microsoft-teams-and-got-150000-dollars-in-pwn2own) by Masato Kinugawa

總是很懶得寫結語，總之、我相信 Web Security 還是會有下一個十年啦，攻擊也只會更精緻、更刁鑽，至於要持續學習? 躺平? 還是直接交給專業的，就交由各位自己決定囉!

文章来源: http://blog.orange.tw/2023/08/2023-webconf-the-evolution-of-web-security.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)