---
title: 從 Coupang 的個資外洩談內部威脅、金鑰管理與 JWT
url: https://blog.huli.tw/2026/03/19/coupang-insider-kms-and-jwt/
source: Huli's blog
date: 2026-03-19
fetch_date: 2026-03-20T04:07:56.354129
---

# 從 Coupang 的個資外洩談內部威脅、金鑰管理與 JWT

[Huli's blog](/)

[文章列表](/archives)
[分類](/categories)
[推薦閱讀](/recommend)
[關於我](/about)

目錄

[1  **到底怎麼打進去的？**](#到底怎麼打進去的)

---

[2  **金鑰管理的生命週期**](#金鑰管理的生命週期)

---

[3  **更安全的金鑰管理方式**](#更安全的金鑰管理方式)

---

[4  **使用 JWT token 的額外風險**](#使用-jwt-token-的額外風險)

---

[5  **結語**](#結語)

[English](/2026/03/19/en/coupang-insider-kms-and-jwt/)

如果有什麼想回饋的（如對文章或部落格的感想），除了留言以外也能填表單跟我說：[表單連結](https://forms.gle/XuWyRC5qtSd2ANta8)。若是對更多 JavaScript 知識有興趣，歡迎參考我的新書[《JavaScript 重修就好》](https://www.tenlong.com.tw/products/9786267757048)

# 從 Coupang 的個資外洩談內部威脅、金鑰管理與 JWT

2026年3月19日

[Security](/categories/Security/)

從去年 11 月開始，Coupang 個資外洩的事件就受到不少關注，一來是據傳外洩的資料數目龐大，二來這間公司也有在台灣設點。隨著調查進度持續推進，也有越來越多細節出現，甚至還被形容為[如同電影情節](https://ec.ltn.com.tw/article/breakingnews/5289937)，去河裡打撈硬碟。

最近跑去翻了韓國那邊出的報告發現寫得還滿詳細的，就寫一篇來聊聊這整件事情在技術上到底是怎麼做到的，以及在資安上又有哪些可以留意的地方。

## 到底怎麼打進去的？

先簡單整理一下整起事件的經過，讓大家有個基本脈絡，之後才能繼續談更細的地方。

目前台灣官方有兩篇聲明稿：

1. [Coupang酷澎台灣就近期酷澎韓國資安事件調查的最新說明](https://tw.coupangcorp.com/archives/5789/) （2025-12-25 發布）
2. [酷澎台灣：針對2025年11月29日公告個資事件之更新](https://tw.coupangcorp.com/archives/5954/) （2026-02-24 發布）

但有更多細節的其實是這篇只有英文跟韓文的官方聲明：[Update on Coupang Korea Cybersecurity Incident](https://www.aboutcoupang.com/English/news/news-details/2025/update-on-coupang-korea-cybersecurity-incident/) （2025-12-29 發布）

想了解更多技術細節的話，則需要看韓國科學技術情報通訊部（Ministry of Science and ICT，MSIT）在 2 月 10 號發表的調查報告，這篇寫得超級詳細：[Investigation Results on the Data Breach by a Former Coupang Employee](https://www.msit.go.kr/eng/bbs/view.do;jsessionid=iMyzX8C42zedbf27PtWxq844qjcyYy0VOCt74FEO.AP_msit_2?sCode=eng&mPid=2&mId=4&bbsSeqNo=42&nttSeqNo=1221&utm_source=perplexity)，本篇所引用的技術細節也都會來自於這個報告。

整起事件的開端發生於 2025 年 11 月 16 號，Coupang 收到了一封來自攻擊者的郵件，說因為系統漏洞的關係有一堆個資外洩，並且附上了相關截圖來證明。

而 Coupang 隨即展開調查，開始翻了翻 log，發現確實是有資料被偷走，就有了大家看到的新聞。目前整起事件已經差不多告一個段落，相關的結果都可以透過官方聲明稿跟新聞得知，這篇文章不會討論結果，只會專注於技術上的細節。

因此，我們關心的問題是：「這個攻擊者怎麼打進去的？」，先來看看他的身份。

> The attacker was identified as a former Coupang software developer (Staff Back-end Engineer) who, whlie employed at Coupang, was responsible for designing and developing user authentication systems for backup in the event of system failures.
> 攻擊者被確認為一名前 Coupang 軟體開發人員（資深後端工程師）。他在 Coupang 任職期間，負責設計與開發使用者認證系統，用於在系統故障時作為備援機制。

攻擊者是前員工，而且負責開發 auth 相關的系統。開頭講的寄信的人也是這個人，至於為什麼他要主動揭發自己的攻擊行為，這個報告跟新聞都沒有講。

在正常的登入流程中，驗證完帳號密碼以後，系統會發一個「electronic access badge」（報告原文就這樣寫），而接下來 server 就會用 signing key 驗這個 badge 是否合法。而攻擊者在 Coupang 工作時，直接取得了這把 signing key，所以本地就可以簽出一個合法的 badge，進而以任何人的身份登入。

這個 electronic access badge 聽起來很像是 JWT token，我自己試了一下 Coupang 台灣的網站，也發現拿來驗證身份的就是個 JWT token（CT\_AT\_TW），解出來會像這樣：

```
{
  "aud": [
    "https://www.tw.coupang.com"
  ],
  "client_id": "4cb7da11-c6d6-4ca3-875f-332cf489d5d",
  "exp": 1773067653,
  "ext": {
    "LSID": "a3788aeb-239c-453d-cd90-72ac345aa431",
    "fiat": 1773064052
  },
  "iat": 1773064052,
  "iss": "https://mauth.tw.coupang.net/",
  "jti": "043c2c37-c373-4b75-abbc-ad8e646bb490",
  "nbf": 1773064052,
  "scp": [
    "openid",
    "offline",
    "core",
    "core-shared",
    "pay"
  ],
  "sub": "556683653781741"
}
```

雖然我不知道 Coupang 內部的技術實作細節，也不能百分百確定是 JWT token，但由於簽 token 檢查身份這個機制以 JWT token 來講最合適，我們就先當作是 JWT token 吧，就算背後用的是其他的，流程也應該是類似的。

看到這邊，攻擊者怎麼打進去的已經很明顯了，那就是他還在工作的時候拿到了 signing key（或你也可以說是 JWT secret），所以離職之後就在外面用這個 signing key 自己簽 token，server 驗了合法就放它過，就登入到其他人的帳號了。登進去之後，就可以去 my profile 之類的頁面看到個資。

所以這其實並不是來自於外部的攻擊，不是外部駭客透過 auth 系統的漏洞打進來，而是 insider threat，是離職員工透過在職時拿到的內部資訊入侵系統。

接著我們可以從兩個角度來看這件事情，分別是企業內部的 key 為什麼會被一個開發人員拿到，以及 JWT token 當作 auth 驗證這個機制本身的風險。

## 金鑰管理的生命週期

金鑰很重要，這點大家都知道，而金鑰的生命週期其實有分很多階段：

1. 產生金鑰（Generate）
2. 金鑰保存（Store）
3. 金鑰分發（Distribute）
4. 金鑰使用（Use）
5. 金鑰輪替（Rotate）
6. 金鑰銷毀（Destroy）

一開始會碰到的就是要先產生一個 secret key，並確保產生的方式是安全的，這一步通常會強調要用安全的演算法、熵足夠的隨機數以及安全的環境等等。有問題的例子是用了不夠安全的隨機數（如 `Math.random()`），或者是在一個不安全的環境中產生金鑰，例如在開發者的本地環境產生。

產生完之後，要選擇安全的地方來保存，例如說存在 HSM 或者是存在 KMS 裡面；反例是直接明文存在某台主機上。

接著當系統要用這把 key 的時候，要能安全地把這把 key 從儲存的地方傳輸到使用的地方。反例就是直接在內網透過 HTTP 傳輸這把 key，能在內網攔截封包就能直接看到明文的 key。

再來使用的時候要用對，金鑰應該只被用於其設計的用途，並且要限制誰可以使用這把 key。例如說我產一把 key 然後每個系統都用同一把，那就是錯誤的使用方式，一旦被偷了每個系統都遭殃。應該是 auth 一把，payment 一把，或甚至同個系統內也會有多把 key。

話說從 Coupang 對外的聲明中可以看出，雖然他們 auth 的那把外洩，但是 payment 相關的服務是沒問題的，資料也沒有流出。韓國的調查報告中也指出影響範圍僅在 My Information 等頁面，不包含支付相關資訊。

最後則是跟淘汰 key 有關，要定期做 key rotation 把金鑰換掉，限制攻擊時間窗口，而把 key 完全銷毀之後要確保無法復原，這把 key 不能再次被使用。

這個生命週期中，任何一步有問題，都可能導致 key 的外洩。

以這次 Coupang 的案例看來，既然前員工可以碰到 key，那就代表應該是在前兩步出了錯，在調查報告裡面有指出現任員工的電腦中也有這個 key：

> A forensic examination of laptops used by current developers confirmed that the signing key, which was required to be stored exclusively within the key management system, had also been stored locally on developer laptops (via hardcoding)
> 對現任開發人員所使用筆記型電腦進行的鑑識分析確認，用於簽章的金鑰本應只儲存在金鑰管理系統中，但實際上也被以硬編碼（hardcoding）的方式儲存在開發人員的筆記型電腦本地端。

有許多公司在做金鑰管理時，可能都只考慮到了其中一半。例如說知道要用一些 Secret Manager 或是 vault 來保存金鑰，並且透過安全的方式傳輸給系統使用，但卻忽略了其他步驟，例如說金鑰產生。

這個 key 是怎麼產生的？有許多公司可能是 developer 本地產一個 key，接著把 key 丟給 SRE，SRE 配置到 vault 中。在這個流程中，key 其實已經被至少兩個內部員工知道了，而且這段也沒什麼 log 可以查，因為是在 key 被放入 vault 前做的事情。

當 key 被放到其他地方管理時，此時也可能 SRE 具有權限直接查看 key 的明文並偷走，但是 vault 系統應該會有 access log 可以往回追溯。但如果是在 key 被放進去之前就記錄下來，那就不會有紀錄，成了資安的破口。

雖然說 insider 的風險相對於其他類別並沒有這麼高，因為內部人士作惡通常更容易被查出來而且會面臨法律責任，可是一旦發生了，對公司名聲還是會造成極大的損害，就像這次 Coupang 的事件一樣。

## 更安全的金鑰管理方式

前面有提到許多公司對於 key 的保存是沒什麼問題的，但是在產生 key 這段做得不夠好，讓內部人士可以直接拿到 key，有了來自內部的風險。

因此，最安全的方式就是「沒有任何人知道這把 key 是什麼」。

「任何人」包括 SRE、資安長、CEO 或是開發者，所有人都不知道 key 到底是什麼。

舉例來說，如果你原本是讓 SRE 自己產生 key 再放到 AWS Secret Manager，可以改成直接用 AWS Secret Manager 的 [create-secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) 指令幫你產一個 key 並且儲存：

```
aws secretsmanager create-secret \
  --name jwt-secret \
  --generate-secret-string '{"PasswordLength":64}'
```

（只是拿 AWS 來舉例，你用其他雲的類似服務應該也都差不多）

如此一來，在 key 產生的時候就不會有人知道內容。

雖然這樣的方式比起剛剛那樣已經更安全了，但仔細想想會發現依然還有幾個問題。

第一，放在 AWS Secret Manager 中的 key 是可以被讀取的，你有 `secretsmanager:GetSecretValue` 權限就可以讀。所以若是有 SRE 具有這個權限，或是透過其他方式幫自己設定這個權限，一樣讀得到。

第二，系統因為要用這把 key，它肯定是讀得到的，那如果有開發者改了一段程式碼在 CI 或是系統啟動時把 key 的內容 dump 到 log 中，他一樣可以知道 key 的明文。

這兩種方式都會留下紀錄，如 AWS 權限變更的紀錄、讀取 key 的紀錄與程式碼的 commit 紀錄等等，而且第二種方式的攻擊前提也不低，通常把 code 推上去 production 之前需要過 PR review，印出來的時候也可能直接被 DLP 掃到。

但無關乎會不會留下證據，重點是如果內部人士有心作惡，還是拿得到的。

其中一種解決方式是先從 key rotation 做起，當可以碰到 key 的人員離職時，記得把相關的 key 都換過一輪以防外洩。儘管我們無法防止在職人員作惡，但至少保障離職之後就自動喪失所有權限，在職時接觸到的資訊或金鑰都無法再使用。

若是還想要再更安全，就算在職員工也不想讓他摸到 key，那就是把「系統需要拿到 key 才能加解密」這個前提拿掉，變成連加解密都不在系統本身做了，而是把這段代理到另外一個可信的地方。

這就是常見的 KMS（Key Management Service）專門在做的事情。

在這類型的服務中，你是拿不到 key 的，它只開放給你幾個 API，例如說：

1. Encrypt
2. Decrypt
3. Sign
4. Verify

所以你要加解密時，就是去呼叫 KMS 的 API 並且等待結果，在這流程中你根本不需要 key，從 key 的產生到使用，全部都是在 KMS 內部做的。

簡單來講，就是把這些 key 的相關操作獨立成一個子系統。

但若只是獨立成子系統，其實根本問題並沒有被解決，這個子系統也會再碰到同樣的問題，那就是 KMS 被 compromised 該怎麼辦？key 會不會洩漏？

若是想做到 key 真的完全不被洩漏（盡可能完全啦，但當然不是 100%），最終解法就是把 key 的管理都交給專門的硬體，也就是 HSM（Hardware Security Module），這些硬體是專門拿來保護 key 的，甚至有考慮到實體攻擊的風險，類似於電影裡看到的那種，保險箱金庫偵測到有人要入侵會自己銷毀之類的。

不過企業級的 HSM 應該是需要百萬台幣起跳，除了自己買 HSM 以外，雲端服務的 KMS 背後也可以搭配 Cloud HSM 來用，例如說 AWS 的 [KMS 文件](https://docs.aws.amazon.com/pdfs/kms/latest/cryptographic-details/kms-crypto-details.pdf)裡面就有寫到：

> If the Origin is AWS\_KMS, after the ARN is created, a request to an AWS KMS HSM is made over
> an authenticated session to provision a hardware security module (HSM) backing key (HBK).
> 如果 Origin 設為 AWS\_KMS，在建立 ARN 之後，系統會透過經過驗證的連線向 AWS KMS 的 HSM 發送請求，建立一把 HSM backing key。

話說 Secret Manager 跟 KMS 的概念某個層面有點類似，簡單講一下區別。

Secret Manager 只是管 secret 的，這個 secret 可以是你呼叫第三方 API 的 token，也可以是登入某個服務的 password，這些都是 secret，但卻不一定是「key」，這個 key 專門指的是密碼學上的 key。

而 Key Management Service 就是專門在管 key 用的，因此提供了加解密跟數位簽章相關的 API，圍繞著 key 在打轉，所以當然連 key 的產生跟整個生命週期都有顧慮到，這就是 Secret Manager 與 KMS 的不同。

簡單來說，Secret Manager 解決的是「如何安全地保存秘密資訊」，而 KMS 解決的是「如何安全地管理與使用密碼學金鑰」。

不過話說回來，為什麼我們要花這麼多的心力去保護這一把 key？那是因為以 JWT token 來說，一旦 private key 被拿走了，就可以直接偽造任意使用者的身份登入…等等，這件事情本身是不是怪怪的？

## 使用 JWT token 的額外風險

這篇 2016 年的經典文章 [Stop using JWT for sessions](http://cryto.net/~joepie91/blog/2016/06/13/stop-using-jwt-for-sessions/) 中有定義三個名詞：

1. Stateless JWT：session data 直接存到 JWT 裡
2. Stateful JWT：JWT 裡只存...