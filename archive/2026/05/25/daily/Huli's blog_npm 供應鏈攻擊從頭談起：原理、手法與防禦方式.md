---
title: npm 供應鏈攻擊從頭談起：原理、手法與防禦方式
url: https://blog.huli.tw/2026/05/25/dive-into-npm-supply-chain-attack/
source: Huli's blog
date: 2026-05-25
fetch_date: 2026-05-26T06:09:39.934364
---

# npm 供應鏈攻擊從頭談起：原理、手法與防禦方式

[Huli's blog](/)

[文章列表](/archives)
[隨意聊](/notes)
[分類](/categories)
[關於我](/about)

目錄

[1  **從安裝一個套件開始**](#從安裝一個套件開始)

---

[2  **安裝到有問題的套件會怎樣？如何防禦？**](#安裝到有問題的套件會怎樣如何防禦)

---

[3  **如何不安裝到有問題的套件**](#如何不安裝到有問題的套件)
[3.1  第一招：延遲下載](#第一招延遲下載)
[3.2  第二招：鎖定版本](#第二招鎖定版本)
[3.3  第三招：先掃描再下載](#第三招先掃描再下載)

---

[4  **細節中的魔鬼：那些 registry 以外的套件**](#細節中的魔鬼那些-registry-以外的套件)

---

[5  **阻止 git 與 direct URL**](#阻止-git-與-direct-url)

---

[6  **誠心推薦 pnpm 以及我的 npm 設定**](#誠心推薦-pnpm-以及我的-npm-設定)

---

[7  **總結**](#總結)

[English](/2026/05/25/en/dive-into-npm-supply-chain-attack/)

如果有什麼想回饋的（如對文章或部落格的感想），除了留言以外也能填表單跟我說：[表單連結](https://forms.gle/XuWyRC5qtSd2ANta8)。

# npm 供應鏈攻擊從頭談起：原理、手法與防禦方式

2026年5月25日

[Security](/categories/Security/)

2026 年 5 月 19 日，拿來做圖表的套件 antv 遭到攻擊，最新版本被植入惡意程式。

5 月 13 日，前端圈很熱門的 TanStack 系列 repo 也遭到攻擊。

4 月 1 日，每週有一億次下載的 axios 也同樣被攻擊，被發布了惡意版本。

大概每隔一個月或甚至一週就會看到供應鏈攻擊的新聞，而被攻擊的對象也不只有 npm，Python 的 PyPI、.NET 的 NuGet、甚至是 Docker Hub 或是開發者在用的 VSCode extension，也全部都是目標。

在這個前提下，開發者該如何保護自己？

這篇主要來談談針對 npm 的供應鏈攻擊，先從原理開始聊起，接著來談談攻擊手法，以及防禦方式。

## 從安裝一個套件開始

當你執行 `npm install express` 時，背後發生了哪些事情？（實際上更複雜，我們簡化一下）。

首先呢，由於沒有指定版本，因此 npm 會先去找 express 這個套件的最新版本，以我寫文章當下為例，是 11 天前發布的 5.2.1。

![express 最新版本](/img/dive-into-npm-supply-chain-attack/p1.png)

於是，express 的 5.2.1 版本就先下載到你的電腦裡了。

接著，express 本身也有依賴其他套件，這些套件都定義在它的 [package.json](https://github.com/expressjs/express/blob/v5.2.1/package.json) 裡面，可以看到還不少：

```
{
  "dependencies": {
    "accepts": "^2.0.0",
    "body-parser": "^2.2.1",
    "content-disposition": "^1.0.0",
    "content-type": "^1.0.5",
    "cookie": "^0.7.1",
    "cookie-signature": "^1.2.1",
    "debug": "^4.4.0",
    "depd": "^2.0.0",
    "encodeurl": "^2.0.0",
    "escape-html": "^1.0.3",
    "etag": "^1.8.1",
    "finalhandler": "^2.1.0",
    "fresh": "^2.0.0",
    "http-errors": "^2.0.0",
    "merge-descriptors": "^2.0.0",
    "mime-types": "^3.0.0",
    "on-finished": "^2.4.1",
    "once": "^1.4.0",
    "parseurl": "^1.3.3",
    "proxy-addr": "^2.0.7",
    "qs": "^6.14.0",
    "range-parser": "^1.2.1",
    "router": "^2.2.0",
    "send": "^1.1.0",
    "serve-static": "^2.2.0",
    "statuses": "^2.0.1",
    "type-is": "^2.0.1",
    "vary": "^1.1.2"
  }
}
```

下一步 npm 就會根據這份定義去下載每一個套件，並且要是「正確版本」。

版本號這東西通常都是 `a.b.c`，例如說 `1.1.0` 或是 `2.3.3` 這種，第一個數字是 major release，通常代表著 breaking change，也就是你從 `1.2.0` 升級到 `2.0.0` 的時候，有些 API 會變，因此直接升級專案可能會壞掉。

而最後的那個版本號如 `2.3.0` 到 `2.3.1`，通常就是修個小 bug，如果有新功能就會動中間的，如 `2.3.0` 到 `2.4.0`。

以 `"body-parser": "^2.2.1"` 為例，這個 `^` 是表示「不接受 breaking change」，因此 `^2.2.1` 能接受任何 `2.x.x` 的版本，這也是最常用的表示方法。

所以，若是你實際去測試，會發現最後安裝到的 `body-parser` 是 `2.2.2` 版本，因為最新的就是 `2.2.2`，而且符合 `^2.2.1` 的定義。

以另外一個上面寫的 `"content-disposition": "^1.0.0"` 為例，最新的版本是 `2.0.0`，而最後安裝到的是 `1.1.0`，因為 `1.1.0` 才符合 `^1.0.0` 的定義。

![依賴解析](/img/dive-into-npm-supply-chain-attack/p2.png)

而這些 express 所依賴的套件，本身也可能會有其他依賴，因此就這樣不斷安裝，直到所有依賴都安裝完成為止。

當你執行完 `npm install express` 以後，會在 terminal 上看到總共安裝了多少個套件：

```
added 66 packages, and audited 67 packages in 2s
```

我們先停在這裡，講到目前為止，這個安裝過程可能會有哪些問題？

第一，我們安裝的 `express` 最新版本如果有問題，我們就中招了。

第二，`express` 中任何一個依賴有問題，我們也中招了。那 66 個套件裡面只要有一個最新版本是駭客發布的，我們也會安裝到。

這就是供應鏈攻擊的由來，尤其 JavaScript 生態系常被人詬病的就是本身提供的功能太少，導致開發者要裝一大堆小套件來處理這些常用功能。

例如說我們想知道 HTTP status code 與 message 的關係，如 404 對應到 `Not Found`，在 npm 上有個每週 1.5 億次下載的套件 [statuses](https://www.npmjs.com/package/statuses) 專門在處理，而它的核心其實就是個 code 到 message 的 JSON 檔案。

相同的需求，在 Go 裡面你可以直接 [http.StatusText](https://pkg.go.dev/net/http#StatusText)，在 Python 裡面可以 [HTTPStatus(404).phrase](https://docs.python.org/3/library/http.html#http.HTTPStatus)，都有官方提供的 library，但是在 JavaScript 的生態系中沒這種東西，只能靠社群維護的套件。

因為缺少了這些官方函式庫，所以一堆功能都是靠 npm 上的套件堆起來的，只要任何一個小套件被攻擊，在安裝的時候就會裝到惡意套件。以攻擊者的角度來看，攻擊一個套件，可以影響到成千上萬個，怎麼想都很划算。

除了上面兩種，還有另一個問題是：「我們自己不小心安裝到錯的套件」。

例如說 express 多打一個 s，變成 expresss，就會安裝到別的套件。因此駭客可以先註冊很多打錯字的套件，放惡意程式碼在裡面，你不小心打錯字就會中招，這種攻擊手法叫做 typosquatting。

偷偷跟你說，每週有將近 600 人會多打一個 s，但慶幸的是這個套件是空的：

![expresss 的下載次數](/img/dive-into-npm-supply-chain-attack/p3.png)

有些服務會禁止註冊這種名字相近的，或是有些善良的資安人員會先註冊起來，以免其他人打錯或是被有心人士註冊走，例如說與知名套件 mongoose 一字之差的 [mongose](https://www.npmjs.com/package/mongose)，以前就被發起攻擊，因此後來被 npm 團隊註冊起來放著：

![mongose](/img/dive-into-npm-supply-chain-attack/p4.png)

## 安裝到有問題的套件會怎樣？如何防禦？

既然是安裝套件，那只要不用它應該就不會有問題吧？雖然多打一個字安裝到錯的，但是在用的時候寫對就會發現套件不存在，只要沒用到套件，應該很安全吧？

在 npm 生態系底下，只要裝到惡意套件就直接 game over 了。

原因是，npm 有提供各種 [scripts](https://docs.npmjs.com/cli/v11/using-npm/scripts) 可以跑，如 `postinstall`，只要在套件裡面指定好，在你安裝完套件以後，寫在 `postinstall` 裡的 shell script 就會被執行。

postinstall 的正常用法是在套件安裝完之後，自動再去下載需要的東西，像是拿來做瀏覽器自動化的 [puppeteer](https://github.com/puppeteer/puppeteer/blob/af1b9be6b6a178f7ea6e197f738ca3cf99d786f7/packages/puppeteer/package.json#L42)，它的 postinstall 寫著 `node install.mjs`，會去跑一個幫你下載瀏覽器的腳本，把環境設置好。

那不正常用法就是把惡意程式碼埋在 postinstall 裡面，像是 [axios](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package) 被攻擊的事件中，就是有個子依賴指定了 postinstall，會跑 `node setup.js`，然後 `setup.js` 含有惡意程式碼，安裝即中招。

那我們該怎麼防禦呢？

在 npm 裡面有一個參數可以設定：[ignore-scripts](https://docs.npmjs.com/cli/v11/commands/npm-install#ignore-scripts)，配成 true 的話，就可以關掉這些 pre/post 系列的 hook，不會執行。這個參數預設是 false，所以記得要主動設定。

而 pnpm 從 v10 開始就預設阻止這些 scripts 的執行，你要主動把套件加到 `allowBuilds` 的清單裡面才能跑。當初還有開了一個 GitHub 的討論串以及投票：[Should we block lifecycle script of dependencies during installation? #8918](https://github.com/orgs/pnpm/discussions/8918)，有七成的人選應該預設擋掉。

而 bun 的策略則是內建一個信任清單，預設只有這清單裡面的套件才可以執行 script，目前有 300 多個套件在上面：[src/install/default-trusted-dependencies.txt](https://github.com/oven-sh/bun/blob/main/src/install/default-trusted-dependencies.txt)

雖然說 bun 在開發者體驗跟安全性之中取得了一個平衡，但我還是更喜歡 pnpm 的做法，直接把全部擋掉，開發者要明確 approve 才會執行。

話說這種「安裝套件後可以執行腳本」的功能也不是 npm 獨有的，隔壁的 RubyGems 也有類似的功能。而這個機制也會有相同問題，就是安裝到惡意套件直接 game over，因此在 4 月份的時候，他們也加上了兩個 option 可以把這個行為關掉：[Add –no-build-extension and –no-install-plugin options to gem install #9473](https://github.com/ruby/rubygems/pull/9473)。

但因為預設開啟怕會有現有專案壞掉，所以預設是關的，跟 npm 一樣要開發者主動開啟才有用。

以 npm 來說，我們可以新增一個 user-level 的 npm config 放在 `~/.npmrc`，就不需要每個資料夾重複指定了：

```
# 不執行 postinstall 等腳本
ignore-scripts=true
```

## 如何不安裝到有問題的套件

若是安裝到了惡意套件，惡意套件可以經由那些 script 直接執行程式碼；就算我們把這功能關掉，若是我們的產品用到了這些套件，那產品本身也會被污染，到時候你的網站就可能被植入惡意程式。

「把 script 關掉」算是第二層防禦，而第一層防禦，也就是大家最想要達成的，其實是：「不要安裝到惡意套件」，只要不安裝到就沒事了。

那要怎麼盡量做到這件事呢？有三個方法。

### 第一招：延遲下載

既然有駭客鎖定供應鏈進行攻擊，那自然也會有相對應的資安廠商來注意這塊進行防禦。

例如說開頭提到的 TanStack，在被攻擊後的 20 分鐘內就被 StepSecurity 發現，而 axios 也是約 1 小時後被發現，在惡意版本發布後的 3 小時被 npm 移除。

因為這些資安公司的努力以及自動化偵測，這類的攻擊通常在幾小時之內就能被發現，並且 npm 也會盡快移除，避免更多人下載到惡意套件。

也就是說，如果我們在安裝的時候指定「我只下載 24 小時前發布的套件」，就能大幅降低下載到惡意套件的可能性（當然不是 100% 解決這問題，畢竟沒人發現的話一樣會下載到）。

pnpm 中有一個 [minimumReleaseAge](https://pnpm.io/settings#minimumreleaseage) 的設定，從 v11 開始預設為 1440 分鐘，也就是一天。所以當 codex 問你要不要更新你說好，安裝完以後又問你要不要更新一直鬼打牆，就是因為版本發布還沒過一天，所以沒裝到（真實案例，我自己碰到過一兩次，後來才發現原來是因為這個）。

在 npm 中也有個 [min-release-age](https://docs.npmjs.com/cli/v11/commands/npm-install#ignore-scripts)，單位是天，效果也是一樣的，預設是空的。

bun 也有 [minimumReleaseAge](https://bun.com/docs/runtime/bunfig#install-minimumreleaseage)，單位是秒（bun 是秒，pnpm 是分鐘，npm 是天，你們是約好要故意不一樣的嗎⋯），預設也是空的。

所以如果你用 pnpm v11 以上的版本，預設就不會下載一天內發布的套件，能夠降低安裝到惡意套件的可能性。

若是用 npm，我也建議設定一下這個值，我自己是設定 3 天，更保險一點：

```
# 不執行 postinstall 等腳本
ignore-scripts=true

# 不下載 3 天內發布的套件
min-release-age=3
```

不過設定這個參數以後會碰到另一個問題，那就是若是有漏洞，這個修復的版本你也無法即時裝上，必須等個幾天或是在安裝時手動先把這個 config 蓋掉，例如說 `npm install -g @openai/codex --min-release-age=0`。

我自己覺得可以看漏洞的嚴重程度以及是否能被攻擊，若是被利用的可能性低的話，等個幾天會比較好。畢竟不能被利用的漏洞風險可控，相比之下安裝到惡意程式的風險會更高一點。

舉例來說，現在很多套件雖然偶爾有一些 high 的漏洞，但若是你仔細看，會發現是特定狀況或是某個功能有問題，而你用的套件或你的產品本身不一定有用到這個功能，這狀況就可以等個幾天再來修。

若是 React2Shell 那種就另當別論，盡快修復才是上策。

### 第二招：鎖定版本

基本上同一個版本是沒辦法被覆蓋的，例如說 `2.0.0` 是安全的，那它就是安全的，駭客要發布惡意版本只能升一個版號變成 `2.0.1`。所以，只要下載過安全的版本，下次再下載也會是安全的（除非 registry 本身被駭啦）。

當我們執行完 `npm install express` 之後，除了會下載套件以外，還會產生另一個檔案叫做 `package-lock.json`，這就是鎖定版本用的 JSON。

舉例來說，`express` 的依賴有 `body-parser`，寫著 `^2.2.1`，而 `body-parser` 目前最新相容的版本是 `2.2.2`，安裝後 lockfile 就會寫死 `2.2.2`：

```
{
  "node_modules/body-parser": {
    "version": "2.2.2",
    "resolved": "https://registry.npmjs.org/body-parser/-/body-parser-...