---
title: 允许函数接收 ChatGPT 响应
url: https://buaq.net/go-175456.html
source: unSafe.sh - 不安全
date: 2023-08-27
fetch_date: 2025-10-04T11:59:06.378367
---

# 允许函数接收 ChatGPT 响应

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

允许函数接收 ChatGPT 响应

允许您挂钩 JavaScript API 并定义一个函数来接收在 chat.openai.com 上执行的对话框的响应。使用Tampermonkey等访
*2023-8-26 14:2:5
Author: [blog.upx8.com(查看原文)](/jump-175456.htm)
阅读量:14
收藏*

---

![](https://blog.oimo.io/wp-content/uploads/2023/04/chatgpt-hook.png)

允许您挂钩 JavaScript API 并**定义一个函数来接收在 chat.openai.com 上执行的对话框的响应。**

[**使用Tampermonkey**](https://www.tampermonkey.net/)等访问[chat.openai.com](https://chat.openai.com/)时执行以下脚本。或者，您可以直接从控制台运行它。

```
(function() {
    if (window.__hooked) {
        return;
    }
    window.__hooked = true;
    let msg = null;
    const OrigTextDecoder = TextDecoder;
    TextDecoder = class {
        constructor() {
            this.orig = new OrigTextDecoder(...arguments);
        }

        decode() {
            const res = this.orig.decode(...arguments);
            try {
                msg = JSON.parse(res).message.content.parts[0];
            } catch (e) {
            }
            if (msg != null && res == "[DONE]") {
                if (window.ongpt) {
                    window.ongpt(msg);
                }
                msg = null;
            }
            return res;
        }
    };
})();
```

之后，您可以通过在全局上下文中`ongpt`定义函数来接收回复。

```
function ongpt(message) {
    console.log("message: " + message);
}
```

当您想要处理原始字符串而不是渲染结果时可以使用。

## 当它停止移动时

由于规格变更而停止工作的可能性很大，但如果是微小的变更

```
msg = JSON.parse(res).message.content.parts[0];
```

这周围

```
res == "[DONE]"
```

我认为如果你修复了这个区域，你就可以再次使用它。**通过在函数中设置断点来查看JSON结构，替换****响应对应的部分，并在结束信号到来时让它流动`msg``ongpt`**。

如果不再`TextDecoder`使用，就放弃它。

文章来源: https://blog.upx8.com/3805
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)