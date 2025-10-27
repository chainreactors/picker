---
title: 人人都需要一個 HTTP proxy 來 debug
url: https://blog.huli.tw/2025/04/23/everyone-need-a-http-proxy-to-debug/
source: Huli's blog
date: 2025-04-24
fetch_date: 2025-10-06T22:06:10.690374
---

# 人人都需要一個 HTTP proxy 來 debug

[Huli's blog](/)

[文章列表](/archives)
[分類](/categories)
[推薦閱讀](/recommend)
[關於我](/about)

目錄

[1  **DevTools 真的會不夠用嗎？是不是你不會用？**](#devtools-真的會不夠用嗎是不是你不會用)
[1.1  重新導向前的請求細節看不到](#重新導向前的請求細節看不到)
[1.2  WebSocket 連線握手失敗找不到原因](#websocket-連線握手失敗找不到原因)

---

[2  **簡單好用的 HTTP Proxy**](#簡單好用的-http-proxy)
[2.1  把 Burp Suite 當 Proxy App 來用](#把-burp-suite-當-proxy-app-來用)
[2.2  用 mitmproxy 搭配腳本動態改變內容](#用-mitmproxy-搭配腳本動態改變內容)

---

[3  **結語**](#結語)

[English](/2025/04/23/en/everyone-need-a-http-proxy-to-debug/)

如果有什麼想回饋的（如對文章或部落格的感想），除了留言以外也能填表單跟我說：[表單連結](https://forms.gle/XuWyRC5qtSd2ANta8)。若是對更多 JavaScript 知識有興趣，歡迎參考我的新書[《JavaScript 重修就好》](https://www.tenlong.com.tw/products/9786267757048)

# 人人都需要一個 HTTP proxy 來 debug

2025年4月23日

[Web](/categories/Web/)

身為每天都要與網頁打交道的前端工程師，熟悉 DevTools 的使用是相當合理的。每當接 API 出問題時，就按下快捷鍵打開 DevTools，切到 Network 分頁，找到紅色的那一行，右鍵複製成 cURL 貼到群組裡面，讓後端自己找找問題。

但不曉得大家有沒有碰過 DevTools 不夠用的狀況，這時該怎麼辦？

## DevTools 真的會不夠用嗎？是不是你不會用？

舉幾個我實際碰過的案例，如果 DevTools 能解決那當然是最方便的，但我解決不了（也有可能是我不會用就是了）。另外，底下的 DevTools 指的都是 Chrome DevTools，或許其他瀏覽器的不會有這些問題。

### 重新導向前的請求細節看不到

很多實作 OAuth 相關服務的網站在登入完成後，會跳轉到 redirect url 並且帶著一個 code，而這時有些網站會拿 code 去交換 access\_token，然後再帶著 access\_token 跳轉到下一個頁面。如果 code 交換 access\_token 這一步有問題，該怎麼 debug 呢？

Chrome DevTools 在跳轉到其他頁面時，預設會把 console 跟 network 的東西都清空。有一個選項叫做「Preserve log」，把它勾起來以後看似問題就解決了，但其實沒有。

大家可以隨便找一個網頁，打開 DevTools 並且把保留 log 勾起來，然後執行以下程式碼：

```
fetch('https://httpbin.org/user-agent')
    .then(() => window.location = 'https://example.com')
```

當跳轉完成以後，雖然 Network 那邊確實可以看到這個請求，但點進去以後只會看到「Failed to load response data」：

![看不到請求](/img/everyone-need-a-http-proxy-to-debug/p1.png)

這個問題從 2012 年就有人回報了，好不容易等了十幾年，2023 年底時說這個在 2024 的 roadmap 上，但目前依然沒有任何動靜：[DevTools: XHR (and other resources) content not available after navigation.](https://issues.chromium.org/issues/40254754)。

總之呢，在這個情境之下，看不到 response 基本上沒辦法 debug，很不方便。

### WebSocket 連線握手失敗找不到原因

雖然我們平常在用 WebSocket 時，只需要一行程式碼就可以建立連接，但背後其實是分了兩步。

第一步會發出一個 HTTP Upgrade 請求，完成以後才切換到 WebSocket 連線。雖然大多數狀況之下第一步都會成功，那如果第一步失敗會怎樣呢？

我們可以請 AI 寫一個很簡單的 demo 出來：

```
寫一個 nodejs websocket server，然後用一個 nginx 擋在前面
nginx 的作用是當 url 含有 ?debug 的時候要回傳 500 錯誤

當 websocket 連線後會往 client 自動發送 hello 的 message

最後要包裝成可以用 docker compose 跑起來
```

等 AI 產完之後用 docker 跑起來，一樣隨便開個網頁建立連接，會發現帶有 debug 的那個連線請求，你只知道失敗了，卻完全不知道原因：

![看不到原因](/img/everyone-need-a-http-proxy-to-debug/p2.png)

這個錯誤訊息甚至跟你隨便連一個沒開的 port 一樣，完全不知道為什麼會失敗，這樣也很難跟後端說問題在哪裡。

以上是兩個我有印象的範例，但實際開發中應該碰過更多更多，基本上都是只靠 DevTools 來看 Network 沒辦法解決的問題，要嘛是看不到，要嘛看到的東西不太對。

## 簡單好用的 HTTP Proxy

既然沒辦法靠 DevTools，那只能依賴更底層的工具了，例如說 HTTP Proxy！有些工具會在你本機起一個 proxy，這樣流量就會都經過它，自然而然就能看到所有的請求了，就不必再受限於 DevTools。

而且另一個好處是有地方可以互相對照，如果 proxy 顯示的跟 DevTools 顯示的不同，就有可能是 DevTools 顯示的東西有問題。

因此，誠心推薦大家找個 HTTP Proxy 來用，我自己用過的有這三個：

1. [Charles](https://www.charlesproxy.com/)
2. [Burp Suite](https://portswigger.net/burp/communitydownload)
3. [mitmproxy](https://mitmproxy.org/)

以前我剛接觸 proxy 時用的是 Charles，接觸到資安以後就改成用第二個 Burp Suite 了。它其實是個可以拿來做各種資安相關測試的工具，但我覺得你只拿來做 proxy 也沒問題，非常方便。

第三個 mitmproxy 是開源且免費的，知名度也很高，我偶爾也會用但是用的方式不太一樣，這個晚點再講。

### 把 Burp Suite 當 Proxy App 來用

先到官網下載個免費的社群版：<https://portswigger.net/burp/communitydownload>

打開之後按下 Next 然後 Start Burp，就會看到主畫面。你會發現它的功能很多，但我們先切到「Proxy」頁籤底下「HTTP history」這一頁就行了：

![Burp 畫面](/img/everyone-need-a-http-proxy-to-debug/p3.png)

然後那顆很顯眼橘色的「Open Browser」點下去，就會開啟它自帶的 Chrome 瀏覽器，可以用這個瀏覽器訪問任何一個網頁，例如說 example.com。

接著切回工具，就會發現 HTTP history 裡面記錄著所有請求的原始內容跟 response：

![請求紀錄](/img/everyone-need-a-http-proxy-to-debug/p4.png)

如此一來，前面提過的跳轉案例跟 WebSocket 握手失敗，都可以在這邊看到原始請求內容，錯誤一目瞭然：

![原始內容](/img/everyone-need-a-http-proxy-to-debug/p5.png)

如果未來你碰到有些請求看不到，那就是被預設的 filter 篩選掉了，點 Filter settings 那邊選 show all 後 apply，應該就能看到了。

（若是有碰到不安全的連線等問題，需要先安裝憑證，請參考：[Installing Burp’s CA certificate](https://portswigger.net/burp/documentation/desktop/external-browser-config/certificate)）

以上就是 Burp Suite 做為 HTTP Proxy 的基本介紹。如果你不想用它提供的 Chrome，也可以自己設置電腦或是瀏覽器的 proxy，它預設會在 8080 port。

舉例來說，我在 Mac 上會再裝一個 Chrome Canary 專門拿來 debug，用這個指令可以開啟並且設定好 proxy 位置：

```
open -a "Google Chrome Canary" --args --proxy-server="http://localhost:8080"
```

如此一來就能用自己熟悉的瀏覽器 debug 了。

話說 Burp Suite 還有很多其他功能啦，例如說重放請求或是暴力破解等等，不過我覺得一般工程師把它當 proxy 來用就已經幫助很大了。對完整功能有興趣的話可以參考 HackerCat 所寫的 [Web滲透測試 – Burp Suite 完整教學系列](https://hackercat.org/burp-suite-tutorial/web-pentesting-burp-suite-total-tutorial)。

### 用 mitmproxy 搭配腳本動態改變內容

mitmproxy 的安裝過程我就不多說了，可以參考[官方文件](https://docs.mitmproxy.org/stable/overview-getting-started/)或是跟 AI 協作自己裝起來，安裝完之後也記得訪問一下 `http://mitm.it` 下載並安裝憑證，才能攔截到 HTTPS 的流量。

都安裝完以後，執行 `mitmproxy` 就能夠把 proxy 跑起來了，會看到一個 CLI 的介面。

那既然 Burp Suite 已經很好用了，什麼時候會用到 mitmproxy 呢？它有個好用的功能是可以透過簡單的 Python 腳本去客製化 proxy 的行為，非常方便。

舉例來說，假設因為某些原因，測試環境無法完全模擬正式環境，但你又不可能直接把 code 上到正式環境去測試。這時就可以用 proxy 動態替換 production 的 response，在本機模擬一些行為。

雖然 Chrome 也有[覆蓋 response](https://developer.chrome.com/docs/devtools/override) 的功能，但限制比較多，例如說內容只能固定等等。我們自己用 proxy 搭配腳本，絕對是更彈性而且自由度更高的選擇。

底下是一個簡單的 mitm 腳本，目的是把我部落格的 script.js 用本機的來替換：

```
from mitmproxy import http
import requests

URL_MAPPINGS = {
    "https://blog.huli.tw/js/script.js": "http://localhost:5555/script.js",
}

def request(flow: http.HTTPFlow) -> None:
    for url in URL_MAPPINGS:
        if flow.request.pretty_url.startswith(url):
            replacement_url = URL_MAPPINGS[url]

            replacement_response = requests.get(replacement_url)

            flow.response = http.Response.make(
                200,
                replacement_response.content,
                {"Content-Type": "application/javascript"}
            )
            return
```

用這個指令就可以跑起來：

```
mitmproxy -s proxy.py
```

接著用前面講過的指令打開一個設定好 proxy 的瀏覽器：

```
open -a "Google Chrome Canary" --args --proxy-server="http://localhost:8080"
```

再用瀏覽器訪問 `https://blog.huli.tw`，就能夠看出 script 的內容已經被替換。

## 結語

以上就是我平常自己會使用到的一些 proxy 以及使用方法。

太過依賴於瀏覽器不是件好事，只要瀏覽器沒有顯示，就不知道該怎麼辦。但前端工程師身為第一線，絕對是有辦法拿到整個 request 與 response，才能進一步釐清問題。以後若是碰到瀏覽器上看不到請求的問題，可以試試看使用 proxy 來拿到完整的請求以及響應。

除了電腦的網頁之外，手機也可以用，可以在 Android 上設定 proxy 連到同個 Wi-Fi 的電腦上，接著在手機上安裝憑證，就能攔截手機的流量。

最後再講一個小訣竅，在 Mac 的 CLI 執行指令時加上 `https_proxy=http://localhost:8080` 就能夠配置 proxy，如 `https_proxy=http://localhost:8080 cursor .`，就可以把 Cursor IDE 的流量都導到 proxy 去。

[#Web](/tags/Web/)

[不需要括號跟分號的 XSS](/2025/09/15/xss-without-semicolon-and-parentheses/)

[VS Code Material Theme 不是惡意軟體——安全的線該畫在哪？](/2025/03/16/vscode-material-theme-is-not-a-malware/)

### 評論

© 2025 Huli
Powered by [Hexo](http://hexo.io/) & [Minos](https://github.com/ppoffice/hexo-theme-minos)

[GitHub](https://github.com/ppoffice/hexo-theme-minos "GitHub")

繁體中文

[English](/2025/04/23/en/everyone-need-a-http-proxy-to-debug/)