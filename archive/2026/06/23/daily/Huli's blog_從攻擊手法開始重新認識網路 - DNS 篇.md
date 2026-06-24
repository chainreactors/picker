---
title: 從攻擊手法開始重新認識網路 - DNS 篇
url: https://blog.huli.tw/2026/06/23/learn-network-from-attack-dns/
source: Huli's blog
date: 2026-06-23
fetch_date: 2026-06-24T06:05:01.417267
---

# 從攻擊手法開始重新認識網路 - DNS 篇

[Huli's blog](/)

[文章列表](/archives)
[隨意聊](/notes)
[分類](/categories)
[關於我](/about)

目錄

[1  **從 DNS cache poisoning 開始認識 DNS**](#從-dns-cache-poisoning-開始認識-dns)

---

[2  **喜傑獅事件**](#喜傑獅事件)

---

[3  **小紅書的封鎖與 RPZ**](#小紅書的封鎖與-rpz)

---

[4  **DNS cache poisoning 的原理**](#dns-cache-poisoning-的原理)

---

[5  **Black Ops 2008 – Its The End Of The Cache As We Know It**](#black-ops-2008-its-the-end-of-the-cache-as-we-know-it)

---

[6  **DNS Cache Poisoning Like it’s 2006**](#dns-cache-poisoning-like-its-2006)

---

[7  **難道 DNS 真的如此不安全？談 DNSSEC 與 DNS cookie**](#難道-dns-真的如此不安全談-dnssec-與-dns-cookie)

---

[8  **DNS 天生的缺陷與隱私保護**](#dns-天生的缺陷與隱私保護)

---

[9  **結語**](#結語)

[English](/2026/06/23/en/learn-network-from-attack-dns/)

如果有什麼想回饋的（如對文章或部落格的感想），除了留言以外也能填表單跟我說：[表單連結](https://forms.gle/XuWyRC5qtSd2ANta8)。

# 從攻擊手法開始重新認識網路 - DNS 篇

2026年6月23日

[Security](/categories/Security/)

「從攻擊手法開始重新認識網路」是一個新的系列文，比起從頭開始講起某個東西如何運作，我會直接先從攻擊手法開始切入，從這點去探討這個攻擊是怎麼做到的，又該如何防禦。

帶著這些問題去閱讀文章，可以更有意識地去理解現在要學的是什麼，待會看到的東西又是為了解決什麼問題。比起平鋪直敘的講解名詞，「從一開始就帶著問題閱讀」是我更想嘗試的方式。

這篇會聊聊 DNS 的運作原理、攻擊手法以及相對應的解法，話不多說直接開始。

## 從 DNS cache poisoning 開始認識 DNS

以前就聽過一種叫做 DNS 快取污染（DNS cache poisoning）的攻擊手法，能控制 DNS 的回答，例如說正常狀況下 `google.com` 應該是連到某個 IP 如 `142.250.21.139`，但若是有攻擊者污染了 DNS，可能會回答另一個 IP，使用者就會連到不同的位置。

有天我突然好奇了起來，這是怎麼做到的？又有什麼防禦方法。

要知道答案之前，我們必須先知道 DNS 這整個系統是怎麼運作的。

DNS 全名為 Domain Name System，中文翻叫域名系統，最廣為人知的、針對一般大眾的解釋，大概就是 DNS 就類似於電話簿，他會把 `google.com` 轉成 `142.250.21.139`，把 `github.com` 轉成 `20.27.177.113`，在網路世界中，最底層拿來發送封包的地址並不是網域，而是 IP，所以必須把網域解析成 IP。

一個更生活化的解釋是，DNS 伺服器像是個老練的計程車司機，你說要去 101，他就精準開到臺北市信義區信義路 5 段 7 號，幫你把這些地標的名稱轉成地址，送你到目的地。

那到底這背後具體都做了些什麼，你的電腦又是怎麼詢問 DNS server 的呢？

當你連上你家的路由器時，有些路由器會下發一個 IP 給你，跟你說你要使用 DNS 時，就用這個 IP 就對了。例如說知名的 `168.95.1.1` 是中華電信的 DNS server，每當你想查詢某個網域的 IP 是什麼的時候，就會去問他。

由於這個 server 負責把網域解析成 IP，通常稱為 DNS resolver，運作如下：

雖然對我們來說，就是問他就能得到答案，但其實背後運作不只如此。以我的網域 `blog.huli.tw` 來說，其實是一層一層的。當我們問中華電信時，中華電信會去問掌管所有 DNS 的服務：「root name server」，而這個服務會記錄 `.tw` 是誰管的，跟中華電信說：「去問他吧」。

於是接下來中華電信就去問管 `.tw` 的 TLD name server，這個 name server 查了 `huli.tw` 之後發現這個網域是由 `ken.ns.cloudflare.com` 管的，就再回說去找他們吧。

所以中華電信就再去問了 `ken.ns.cloudflare.com`，拿到了底下的結果：

```
blog.huli.tw.   300 IN  A 104.21.51.169
blog.huli.tw.   300 IN  A 172.67.183.1
```

就確認了 `blog.huli.tw` 對應到的 IP 有這兩個，就會回傳給我的瀏覽器，接著瀏覽器再自己選擇要連去哪裡。

由於整條鏈路中只有 `ken.ns.cloudflare.com` 知道最終結果，它又叫做 authoritative name server，中文翻叫「權威 DNS」。

整體流程如下方：

這個遞迴解析的過程滿長的，因此不可能每次都這樣，事實是每一個環節都有 cache 的存在，例如說瀏覽器就可能有自己的 cache，作業系統也有，中華電信提供的 DNS resolver 也是，所以並不會每一次都查完整個鏈路才能知道結果，只要碰到 cache 就會返回了。

而這個 DNS 快取污染打的就是 DNS resolver，也就是前面提到的中華電信 `168.95.1.1` 那台，若是我能污染 `google.com`，那中華電信的使用者在造訪 google 時，就會連去我的 server，可見這個攻擊的影響力之大。

DNS resolver 是負責把 domain 轉成 IP 的服務，只要知道這點，我們就可以先來談談兩個真實事件了。

## 喜傑獅事件

筆電品牌喜傑獅原本在官網推出「一讚折一元」的活動，但發現太多讚了所以臨時改規則並且提早關閉網站。由於有些在時間內的訂單也被取消，因此網友告上法院，最後判決喜傑獅敗訴。

這個案件我當時也滿關注的，雖然很多網友都覺得純粹是喜傑獅在無理取鬧，但對於部分被取消的訂單，我很好奇最後會怎麼判。根據喜傑獅的說法，他們已經關閉了網站，但是網友透過「網頁漏洞」連進來下單，因此是無效的。

那這個網頁漏洞到底是什麼？網頁又是怎麼關閉的？

關閉其實就是喜傑獅把他們的 DNS 紀錄拔掉，等快取失效之後，官網自然就連不進來了，你輸入網址之後會回一個錯誤。而所謂的「網頁漏洞」是網友自己修改本機的 `/etc/hosts` 檔案，把記錄加回去，就可以連回官網了，不需要靠 DNS resolver。

根據[臺灣士林地方法院小額民事判決114年度士消小字第5號](https://judgment.judicial.gov.tw/LAW_Mobile_FJUD/FJUD/data.aspx?ty=JD&id=SLEV,114,%E5%A3%AB%E6%B6%88%E5%B0%8F,5,20250930,1)，法官最後的見解為：

> 再者，倘被告有意拒絕一切訂單成立，應可逕將官網伺服器暫時離線，此由前述網友Facebook文章可知被告嗣後亦採此措施即明，則被告未將官網伺服器離線而僅單純將DNS與IP位址解連，猶如商家於營業中將門牌及招牌（DNS）暫時卸下，惟任何知悉商家實際位置（IP位址）之顧客尋覓上門，商家仍如常提供服務（成立訂單），自不能認為顧客有何詐欺行為或商家有何陷於錯誤可言。

就是你店家不想賣東西，應該把伺服器關掉離線，但你只是把 DNS 拿掉，網站還在。如同商家還在營業只是把招牌拿掉，但熟門熟路的顧客自己上門買東西也還是合理的。

我關注的點是「把 DNS 紀錄拿掉算不算關閉網站」，而且我想到一個假想的情境，假設某間公司的其中一個測試環境暴露在公網（IT 也說過應該放內網，但是某些人覺得要連 VPN 很麻煩，想說沒人會去找就放公網了），但是網址沒有公開，裡面所有物品的價格都是正常的一半。

有個路人透過某種方式找到這個網址下單了，會不會被認為是交易成立？

不知道是路人要舉證自己有足夠理由相信這網站是正常的所以才下單，還是公司要舉證這網站雖然暴露公網但非公開網站，不過後者以喜傑獅的判例來看可能行不通，會認為網站公開了就是公開。

## 小紅書的封鎖與 RPZ

前面提過若是可以讓 DNS resolver 把 `google.com` 解析到我的 IP，大家在連 Google 的時候就會跑過來我的 server，這算是惡意的攻擊。

但也有一種方式原理相同，做法也相同，卻被視為是善意的。

舉例來說，政府發現某個詐騙網站很猖狂，因此直接叫中華電信把它們的 domain 解析成政府單位的 IP，因此使用者連到該網站時，會顯示警告畫面，看不到原本的內容。

這個機制叫做 DNS RPZ（Response Policy Zone），財團法人台灣網路資訊中心有特別做一個網站來說明：[DNS RPZ 治理機制](https://rpz.twnic.tw/#/mechanism#main)，由各機關提出審核，審核通過之後台灣的各大電信就會特別把這筆紀錄解析的 IP 改掉，跳出警告畫面。

最有名的就是去年年底小紅書被封的案例了，當你用瀏覽器打開小紅書的網站後，會先看到一個憑證錯誤的頁面，點繼續之後會看到這個：

![被 RPZ 的網頁](/img/learn-network-from-attack-dns/p1.png)

而理解 DNS 是怎麼運作的之後，就能知道為什麼網路上流傳的繞過方法：「改 DNS resolver」可以成功。

儘管大家預設用的可能是中華電信的 DNS resolver，但這是可以改的，你可以改成 Google 提供的 `8.8.8.8`，也可以改成 Cloudflare 提供的 `1.1.1.1`，透過這兩個 DNS resolver，照樣可以連上小紅書。

好奇的話，你可以在自己電腦試一下，先透過 `168.95.1.1` 查詢小紅書的 IP，會得到 `140.111.246.32` 以及另一條 rpz 相關的說明：

```
dig @168.95.1.1 www.xiaohongshu.com A

;; ANSWER SECTION:
www.xiaohongshu.com.  300 IN  A 140.111.246.32

;; ADDITIONAL SECTION:
rpztw.      60  IN  SOA localhost. This.is.an.infringing.website.rpztw. 1781775121 60 60 86400 60
```

而透過 `8.8.8.8` 就是正常的 IP：

```
dig @8.8.8.8 www.xiaohongshu.com A

www.xiaohongshu.com.eo.dnse0.com. 60 IN A 43.170.214.10
www.xiaohongshu.com.eo.dnse0.com. 60 IN A 43.175.160.184
www.xiaohongshu.com.eo.dnse0.com. 60 IN A 43.175.164.195
www.xiaohongshu.com.eo.dnse0.com. 60 IN A 43.175.161.148
```

所以，DNS RPZ 跟真正意義上的封鎖還是有一段距離，原意是想保護民眾連線到違法的網站，但如果你不想被保護或是你知道你在幹嘛，只要改個 DNS 還是能連到，不會被城牆擋下來。

像這樣主動干預網路世界的行為，想當然耳也有許多法規以及制度上的討論，到底政府能介入到什麼程度？又該怎麼防止 RPZ 胡亂封鎖？也有人認為政府壓根就不該干預，網路世界應該是自由的。

而台灣的 RPZ 確實不小心封過許多重要服務，如 [Azure Web App](https://www.ithome.com.tw/news/170025) 或是 [WordPress](https://kheresy.wordpress.com/2024/04/25/wordpress-block-by-npa-part2/) 都慘遭過毒手。

想了解更多網路治理的話題，可以參考 [OCF 財團法人開放文化基金會](https://ocf.tw/p/infr/)或是[臺灣網路治理論壇 TWIGF](https://www.igf.org.tw/)，以前在臉書上也有一些公開的討論，如這個 [2023 對 RPZ 機制的討論](https://www.facebook.com/permalink.php?story_fbid=pfbid02Jow2BmwmrETdxbq3zoqyHu2mYaef2HyfZmBxx4rpMx5AdyUkY9n6VDYPVVZLwXtml&id=100000319282897)以及 [2025 小紅書被封的討論](https://www.facebook.com/permalink.php?story_fbid=pfbid02nFLnR3we43WX7UWqVsEYrApbAt4qoHn2T86scvQDoZ9YKNecAQFAbENEj4n6BNdMl&id=100000028617930)。

## DNS cache poisoning 的原理

把話題拉回 DNS cache poisoning，既然我們現在了解 DNS 的運作了，那到底這個污染是怎麼做到的？

前面提過 DNS resolver 會去 `ken.ns.cloudflare.com` 問 `blog.huli.tw` 的 IP，攻擊者是怎麼干預這個結果的？

歷史上出現過的第一個攻擊手法是：「買一送一」，第二個是：「搶答」。

首先，「問 `blog.huli.tw` 的 IP」這所謂的「問」，背後就是傳了個封包，而 DNS 走的協議是 UDP，所以對 DNS resolver 來說，就是傳了個封包給負責解析 `blog.huli.tw` 的 IP，假設是 `108.162.193.127`，內容寫著：

```
From: 168.95.1.1:53
To:   108.162.193.127:53

Question:
blog.huli.tw A?
Transaction ID: 12345
```

而正常狀況下，該 name server 收到以後會回答：

```
From: 108.162.193.127:53
To:   168.95.1.1:53

Transaction ID: 12345
Answer:
blog.huli.tw A 104.21.51.169
```

此時 resolver 驗證過 transaction ID 跟來源 IP 一致，就相信這個結果，把這個結果放到自己的快取中，下次有人再問就直接回答。

而第一種手法「買一送一」，負責解析 `blog.huli.tw` 的 name server 會在回傳的封包中偷偷送你其他 domain 的結果：

```
From: 108.162.193.127:53
To:   168.95.1.1:53

Transaction ID: 12345
Answer:
blog.huli.tw A 104.21.51.169
google.com A 104.21.51.169
```

等同於「雖然你沒問但我順便告訴你，`google.com` 的 IP 是這個喔」。

不過你必須要有一個負責解析域名的合法 name server 才有辦法攻擊，攻擊前提滿高的，一般人做不到，但是 30 年前發生過。

1997 年，Eugene Kashpureff 經營的 AlterNIC 負責一部分頂級域名的 DNS 解析，而他就是利用這個手法，去影響另一個 DNS 服務 `www.internic.net` 的解析結果。

這不是資安研究而是真的犯罪，所以被抓了，現在還可以找到紐約時報的報導：[From Jail and Boardroom, A Street Fight for the Internet](https://archive.nytimes.com/www.nytimes.com/library/cyber/week/110797kashpureff.html) 以及相關的[新聞稿](https://www.irational.org/APD/CCIPS/kashpurepr.htm)。

這個問題後來被修掉，多了一個叫「bailiwick checking」的機制，會檢查該 DNS 伺服器是否有權限回答這個網域的解析紀錄，不讓你買一送一了。

接著講第二種「搶答」，由於 resolver 驗證 transaction ID 跟來源 IP 一致就會信任結果，那反過來講，只要攻擊者能偽造這兩個東西，並且速度比原本的更快，那 resolver 就會相信這個造假的結果。

先來講偽造 IP 這件事情，所謂的 IP，最終就只是放在封包裡的一組字串，雖然 OS 會幫你填好，但你可以自己竄改一下，填入自己想要的 IP，就偽造成功了。

但是，像是 HTTP 那種走 TCP 的情境，開頭有個三向交握，你先發給對方，對方再發給你，這個第二步「對方發給你」，他會發到你偽造的目的地去，你就收不到，就沒辦法成功建立連接，所以就算偽造也沒用。

不過 DNS 是走 UDP，因此封包送出去就結束了，所以才能偽造成功。

除此之外，有些 ISP 有做過濾，當它發現你封包內的 IP 怪怪的，不是分配給你的網段，就會直接把封包丟掉，所以你根本傳不出去，這個機制叫 [BCP 38: Network Ingress Filtering](https://www.rfc-editor.org/info/rfc2827/)。

但這並不是強制的，所以找到沒有做 BCP 38 的 ISP 以後，你就能偽造來源 IP，把偽造的回應發給 DNS resolver。

那 transaction ID 呢？這是個 16 bit 的 ID，可能性只有 65536 種，就一直狂猜就好，只要猜到了就是你的，每次都隨機猜的話，猜 45426 次就有 50% 的機率至少中一次。

但這只是理論上的可行性而已，有個致命的缺點沒有考慮到。前面提過這些 name server 都是有 cache 的，...