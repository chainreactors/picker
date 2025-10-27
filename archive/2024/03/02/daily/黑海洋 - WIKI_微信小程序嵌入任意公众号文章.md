---
title: 微信小程序嵌入任意公众号文章
url: https://blog.upx8.com/4085
source: 黑海洋 - WIKI
date: 2024-03-02
fetch_date: 2025-10-04T12:11:41.301931
---

# 微信小程序嵌入任意公众号文章

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 微信小程序嵌入任意公众号文章

发布时间:
2024-03-01

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
23581

其实是去年做的事情了，现在想起来做一个记录。

## 背景

小程序可以使用 `webview` 组件来嵌入 web 内容，对于常规域名需要通过域名所有权认证，对于微信公众号文章需要发布公众号与小程序关联，这在部分情况下是无法实现的（显示非自有公众号文章）。

所以，我们需要一个中间人来帮我们实现这个功能。

## 实现思路

当然就是实现一个反向代理了，能够反代 `mp.weixin.qq.com` 的内容。

## 实现方法

因为需求比较简单，还不至于到写代码的地步，用 nginx 实现就好。

```
server
    {
        server_name mp-proxy.example.com;

        # listen block

        location /
        {
            proxy_pass https://mp.weixin.qq.com/;
        }
    }
```

NGINX

然后访问一下就会有靓仔发现，我这个图片怎么显示不出来呢。

通过 `network` 可以看到图片请求由于 `cors` 限制导致失败，但是为什么普通的 `GET` 请求会被 `cors` 限制呢？

通过 `initiator` 观察可以看到请求是为了实现懒加载由 `script` 动态插入的 `<img>` 标签发出的。那么问题就来了，为什么这个 `<img>` 需要 `cors` 检查？

这里就需要一些简单的前端知识，[mdn](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXIubW96aWxsYS5vcmcvZW4tVVMvZG9jcy9XZWIvSFRNTC9BdHRyaWJ1dGVzL2Nyb3Nzb3JpZ2lu)，在跨域条件下，默认 `<img>` 加载的图片资源会被认为是 `tainted` 的，除非为 `<img>` 加上 `crossorigin` 属性，会在请求中要求 `cors` 检查，并在浏览器进行 `cors` 校验。

在公众号文章场景下，并不存在需要 `canvas` 的场景，所以我们可以将 `crossorigin` 属性移除，以此来绕开 `cors` 限制。这里可以通过在 `source` 中搜索，将所有 `crossOrigin` 搜索出来，进行替换（主要就是几处 js）。

然后将 `html` js link 指向 nginx，在 nginx 对 js 内容进行替换，顺便去掉所有的 `referrer`。

注意如果需要替换内容，需要禁止 `gzip` 等压缩，否则内容无法被替换。

## 最终实现

```
server
    {
        server_name mp-proxy.weshine.club;
        include weshine.ssl;

        location /s/
        {
            add_header Referrer-Policy no-referrer;
            sub_filter 'origin-when-cross-origin' 'no-referrer';
            sub_filter 'strict-origin-when-cross-origin' 'no-referrer';
            sub_filter 'crossorigin="anonymous"' '';
            sub_filter 'res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/assets/weui' mp-proxy.weshine.club/ass/weui;
            sub_filter 'res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/assets/appmsg.' mp-proxy.weshine.club/ass/appmsg.;
            proxy_set_header Accept-Encoding '';
            proxy_pass https://mp.weixin.qq.com/s/;
        }
        location /mp/
        {
            proxy_pass https://mp.weixin.qq.com/mp/;
        }

        location /ass
        {
            sub_filter 's.setAttribute("crossOrigin","Anonymous")' '1';
            sub_filter 'e.crossOrigin="anonymous"' '1';
            sub_filter 't.crossOrigin="anonymous"' '1';
            sub_filter_types 'application/x-javascript';
            sub_filter_once off;
            proxy_set_header Accept-Encoding '';
            proxy_pass https://res.wx.qq.com/mmbizappmsg/zh_CN/htmledition/js/assets;
            proxy_buffering        on;
            proxy_cache            mp_proxy;
            proxy_cache_valid      200  1d;
        }
    }
```

这样就完工了。当然还有部分优化点，比如部分 js 文件过大，可以只留下需要的 js，其他的内容全部 302 出去。这里就不展开了。

1. ![crism](https://gravatar.loli.net/avatar/avatar/17e6d8777fa6242e9f7ad7170b508eb0?s=32&r=&d=)

   **crism**

   2024-08-30 11:46:52

   [回复](https://blog.upx8.com/4085/comment-page-1?replyTo=30114#respond-post-4085)

   测试了下上面的脚本 好像代理不成功 浏览器跨域不报错了 但是图片还是不显示
   文章地址 https://mp.weixin.qq.com/s/l77HFX6Kb6acQB0LoFjWbA

[取消回复](https://blog.upx8.com/4085#respond-post-4085)

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