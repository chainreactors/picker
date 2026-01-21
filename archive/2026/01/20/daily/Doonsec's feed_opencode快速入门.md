---
title: opencode快速入门
url: https://mp.weixin.qq.com/s/fwbZsaEzTDUhwz0ZCemZ-w
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:58.506879
---

# opencode快速入门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/olwnDibj8yicTWgNDmOeCsUicbpbEceiaPKlMKmqhvrbbyPM0n3cibzGn4M404GjPXRULibRMAuyZlMymhp8l2AujVBw/0?wx_fmt=jpeg)

# opencode快速入门

唐小风
唐小风

白帽子飙车路

![]()

在小说阅读器中沉浸阅读

### 0x01 项目opencode

https://github.com/anomalyco/opencode

##### unsetunset快速安装unsetunset

```
npm i -g opencode-ai@latest
```

##### unsetunset安装成功，配置文件unsetunset

![](https://mmbiz.qpic.cn/sz_mmbiz_png/olwnDibj8yicTWgNDmOeCsUicbpbEceiaPKlgwsicGsoMJZibFlqnjRoSVhMqbhzicyEpBxOjjTn3WFxAeKoP7wHhIxNw/640?wx_fmt=png&from=appmsg)

##### unsetunset配置opencode.jsonunsetunset

**参考上篇文章，本地启动API反代**

> C:\Users\用户名\.config\opencode\opencode.json

```
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "claude-proxy": {
      "npm": "@ai-sdk/anthropic",
      "name": "Claude本地反代",
      "options": {
        "baseURL": "http://127.0.0.1:8045/v1",
        "apiKey": "sk-8255a9da2af54562a1d81d5c862d8ea9"
      },
      "models": {
        "claude-opus-4-5-thinking": {
          "name": "claude-opus-4-5-thinking"
        },
        "gemini-3-pro-low": {
          "name": "gemini-3-pro-low"
        }
      }
    },
    "gemini-proxy": {
      "npm": "@ai-sdk/google",
      "name": "Gemini逆向本地反代",
      "options": {
        "baseURL": "http://127.0.0.1:8045/v1",
        "apiKey": "sk-8255a9da2af54562a1d81d5c862d8ea9"
      },
      "models": {
        "claude-opus-4-5-thinking": {
          "name": "claude-opus-4-5-thinking"
        },
        "gemini-3-pro-high": {
          "name": "gemini-3-pro-high"
        },
        "gemini-3-pro-image": {
          "name": "gemini-3-pro-image"
        }
      }
    }
  }
}
```

##### unsetunset查看配置unsetunset

```
/status
```

### 0x02 更新opencode

```
opencode upgrade
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/olwnDibj8yicTWgNDmOeCsUicbpbEceiaPKlpPB90d16P4QNoCuKfiaau4gYibyQaDG9a1VJJ6v5epwM7kVeOLPbusnw/640?wx_fmt=png&from=appmsg)

### 0x03 opencode中文指南

https://learnopencode.com

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/olwnDibj8yicT5CBIc3oBt4uUiaLqicrnSU8dibzPuAy866C8YgFLBo2RelPFNx5ibzwpbpTkiaTdeCOOiaZ4AQBib3Aplw/0?wx_fmt=png)

白帽子飙车路

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/olwnDibj8yicT5CBIc3oBt4uUiaLqicrnSU8dibzPuAy866C8YgFLBo2RelPFNx5ibzwpbpTkiaTdeCOOiaZ4AQBib3Aplw/0?wx_fmt=png)

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