---
title: 允许函数接收 ChatGPT 响应
url: https://blog.upx8.com/3805
source: 黑海洋 - WIKI
date: 2023-08-27
fetch_date: 2025-10-04T11:59:55.626060
---

# 允许函数接收 ChatGPT 响应

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 允许函数接收 ChatGPT 响应

发布时间:
2023-08-26

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
10146

![](https://blog.oimo.io/wp-content/uploads/2023/04/chatgpt-hook.png)

允许您挂钩 JavaScript API 并**定义一个函数来接收在 chat.openai.com 上执行的对话框的响应。**

[**使用Tampermonkey**](https://blog.upx8.com/go/aHR0cHM6Ly93d3cudGFtcGVybW9ua2V5Lm5ldC8)等访问[chat.openai.com](https://blog.upx8.com/go/aHR0cHM6Ly9jaGF0Lm9wZW5haS5jb20v)时执行以下脚本。或者，您可以直接从控制台运行它。

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

[取消回复](https://blog.upx8.com/3805#respond-post-3805)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")