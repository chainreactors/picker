---
title: 赶紧自查：你的 CS Server 可能正在“裸奔”，VT 上已经有人把配置扒出来了
url: https://mp.weixin.qq.com/s/nGZKPAdTRjcMPOv3D2SG-w
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:08.071277
---

# 赶紧自查：你的 CS Server 可能正在“裸奔”，VT 上已经有人把配置扒出来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBFJfrFHXFYCKLgh2Dp4LqUSrWlSteRGPn7tAkNRttVRaQMO4njOXsQRHeGmPQluNP5y50tDN4t08cibddhbic0RWbSTjOq26bTsY/0?wx_fmt=jpeg)

# 赶紧自查：你的 CS Server 可能正在“裸奔”，VT 上已经有人把配置扒出来了

原创

MaoKu
MaoKu

毛酷红队

![]()

在小说阅读器中沉浸阅读

> 如果你的 CS Server 还保留默认 stager 路径、checksum 回退，或者入口代理还在自动补 Host，那它大概率不是“藏得很好”，而是在公网裸奔。

## 前言：一次域名封禁，把问题全暴露了

这篇文章你可以先当成一次事故复盘来看，也可以当成一份自查清单来看。

因为最后定位出来的问题，并不是什么复杂漏洞，而是很多人部署 CS Server 时都会顺手留下的默认行为。

前两天在测试 Beacon 上线的时候，我碰到一个很反常的情况。

之前已经配置好、也确认能正常上线的 Listener，突然就不通了。最开始我以为是机器波动，结果本地一查，发现问题根本不在服务端，而是在域名本身：解析失效了。

这个域名是新买的，刚挂到一套新部署的 C2 Server 上没多久，结果就被供应商直接停用了。

给出的理由也很直接：该域名被用于恶意服务。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHADdRWQmoz7iaNHvewrr20EdjvNkv3DySYL3UACVn4nbKicZ8BTfqibgOoDcHxY5m8PbNERWOJpJBf1hoOhNKsphp4c2cqrhcJlQ/640?wx_fmt=jpeg&from=appmsg)

域名被封禁

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icLTHicH8iakBEqLSO9hEoBCnybicqOFhD5r5aYkEthgjQbLO3ia2u63lnhaDQf3zmOjYghiaCfVZpfZHwGwRQe3BXUNyHgiaZWs1SCiaZfngfl6fds/640?wx_fmt=jpeg&from=appmsg)

邮件回复

说实话，第一反应不是慌，而是疑惑。

因为从我们的视角看，这套服务刚上线，样本没有外泄，公网能看到的无非就是几次网络请求和响应。按理说，别人最多只能觉得“这个服务可疑”，怎么会这么快就被打上标签，甚至连服务端配置都被整理出来？

带着这个问题，我开始顺着线索往回查。

## 去 VT 看了一眼，事情比想象中更严重

在 VT 上查这个域名之后，结果并不乐观。

最早看到的是 8 个引擎标记恶意，后面再看时，标记数量还在继续增加。

但更让我在意的，不是这个数字本身，而是 Community 讨论区里已经有人贴出了相当详细的服务端信息，包括：

* • watermark
* • 通信 URI
* • User-Agent
* • Host Header
* • 协议和端口

这就说明，对方不是只做了一个“经验判断”，而是真的把二阶段返回的数据拿到手，并且把里面的配置给解析出来了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHQ6JicEKIlOJYP5ZjPGGqwiboiaobict7P8ZtobcyoJsib2icxIaZoOvibbAY9YKAicQF6fH5pqpZBlFic6HInD2YuN11hsIt4tXkRfOs8/640?wx_fmt=jpeg&from=appmsg)

VT 检测结果

![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBG1iazXGu2uY9hh7xqfcJzMxO4j1xibEqFvlkzfAyUhL2LndrRumr4ic18f6LtKeoWUNUScttWN5WdcSP4MUUDE9poDR15Luh0ib1Q/640?wx_fmt=jpeg&from=appmsg)

VT Community 信息

## 我当时最想不通的一件事

没有拿到样本，怎么会有人只靠网络层的请求，就把 profile 里的关键信息提出来？

后来把整条链路梳理清楚之后，这个问题反而没有那么神秘。

很多主动扫描脚本做的事情其实很简单：先去试探 stager 路径，拿到返回的 stage，再按照固定格式去解码和提取配置区。只要服务端肯把二阶段数据吐出来，watermark、URI、Host Header 这些信息，本来就在里面。

也就是说，问题不在于别人“猜”得有多准，而在于我们的服务端实际上把不该暴露的东西，太轻易地暴露出去了。

## 真正的问题，不止一个

这次复盘下来，我发现不是某一个点出了问题，而是几处默认行为叠在一起，最后把暴露面放大了。

### 1. 我们以为有 Host 过滤，实际上入口先帮忙补齐了

我们原本以为，后端会校验 Host，只有带着特定域名的请求才能命中真正的服务。

但实际部署里，443 入口前面挂了一层 Nginx 反向代理。关键问题在于，这层代理会自动把 `Host` 改写成后端期望的域名，再把请求继续转发出去。

这意味着，别人哪怕不是通过域名访问，而是直接打 `IP:443`，只要命中这层代理，请求照样会被“补齐”成一个看起来合法的后端请求。

换句话说，我们原本以为存在的域名限制，并没有真正发生在最外层入口，而是在代理转发之后才成立。

这也是为什么后来验证时发现，直接访问入口 IP 的 443 端口，一样能拿到数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBErofuFV6z59Db0l0C9dsD3iaBwNxDqan9803xseWV69J2l2GPDbUOiay5siavAibNBvh677swLwJgNQuo04zheV2a0bw6glib1qTYo/640?wx_fmt=jpeg&from=appmsg)

Nginx 配置

### 2. 服务端接受 checksum 回退，给了扫描器一个稳定入口

第二个问题出在 `fly-server` 的 stager 处理逻辑上。

之前的实现里，除了精确 URI 匹配之外，还保留了 checksum 回退逻辑。也就是说，就算外部不知道 profile 里真正写的 stager 路径，只要请求的是某些符合规则的路径，服务端依然可能把 stager 内容返回出去。

这种逻辑对兼容性友好，对主动扫描也同样友好。

对扫描器来说，它根本不需要知道真实 URI，只要批量打一遍这类常见探测路径，命中之后就能继续往下解码。

### 3. 即便去掉 checksum 回退，默认 `/stager` 和 `/stager64` 仍然能直接访问

更隐蔽的问题在第三层。

最开始我以为，既然 profile 里已经写了 `.http-stager.uri_x86` 和 `.http-stager.uri_x64`，那么外部只有知道这些具体路径，才能拿到对应的 stage。

后来翻代码才发现，事情不是这样。

在当时的实现里，profile 中的 `uri_x86` 和 `uri_x64` 并不是“替换默认路径”，而是在默认 `/stager`、`/stager64` 之外，再额外注册一遍。

也就是说，哪怕外部完全不知道 profile 里写了什么，只要直接去请求 `/stager64`，服务端一样会返回 stage。

这就解释了为什么有些信息看起来像是“被精准命中”，其实根本不需要知道自定义 URI。默认路径本身就是现成入口。

## 为什么别人能拿到 watermark 这些信息

走到这里，答案其实已经比较清楚了。

很多 C2 的二阶段内容本身就带着配置区，只要主动探测成功、把 stage 拿到手，后面的解析就是格式问题，不是猜谜问题。

我们自己复现之后，也确实重新拿到了类似信息，例如：

* • watermark：`666666666`
* • 通信 Host/Header
* • GET/POST URI
* • User-Agent
* • 端口与协议

这说明 VT Community 里那份 “C2 server info”，本质上并不是凭空猜出来的，而是从网络请求里拿到 stage 之后，按格式提取出来的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHNGm7qpR8Ukh1iccSplJX74PtYqpZU19horUvzJnzHkMxnQ4QKM0LnK1YQGiareIBylTVV0FVWXxibDByUicrS6MUiczgHu8mBYplk/640?wx_fmt=jpeg&from=appmsg)

探测结果

## 后来我们做了什么修正

问题定位清楚之后，修复方向反而很明确。

第一，`fly-server` 不再接受 checksum 回退路径。类似这类“碰运气”的探测入口被直接关掉了，请求只有精确命中已注册 URI 才会返回内容。

第二，stager 注册逻辑改成了“只允许 profile 里明确写出来的 URI”。默认 `/stager`、`/stager64` 不再自动注册，`uri_x86`、`uri_x64` 也不再是附加项，而是必填项。

第三，从部署层面看，入口代理不能再替后端自动补 `Host`。如果最外层还允许直接打 IP，再在代理里帮忙改 Host，那么所谓的 Host 限制就没有真正起到边界作用。

这几个动作做完之后，整条暴露链路才算真正被收紧。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icLTHicH8iakBHJWBBiabPCRFSwtKXIO6oIWGSHATj5xgaicicYdqsofnueC1hsRlXvolOaqqxfgVQh71kbIlh5blE28iccicOHJv5TWj7icBTcyicXNU/640?wx_fmt=jpeg&from=appmsg)

修复后验证

## 这次事情，最大的教训是什么

这次复盘最扎心的一点在于，问题并不来自什么很高级的对抗手段，而是来自我们自己留下的默认兼容行为。

很多时候，工程师会天然觉得：

* • 我已经自定义了 URI
* • 我已经做了 Host 过滤
* • 我没有泄露样本

所以外部应该很难把服务特征拿全。

但真实世界不是按“我以为”来运行的。

只要入口层还在无条件转发，只要服务端还保留默认路径，只要兼容逻辑还在偷偷兜底，主动扫描拿到配置就只是时间问题。

说得更直白一点：不是别人太神秘，而是我们给出去的东西，本来就比我们以为的要多。

## 最后

这次域名被封，表面上看是一次 IOC 暴露事件；往里看，其实是一次很典型的工程实现复盘。

它提醒我的不是“以后别买新域名”，而是：

不要把希望寄托在 profile 里那几行自定义配置上。真正决定暴露面的，往往是入口层怎么转发、服务端默认注册了什么、以及那些为了兼容留下来的回退逻辑。

如果这几个地方不收紧，域名换得再快，暴露方式也还是同一种。

## 检测脚本下载

如果你也想验证自己的服务端是否会被这类主动扫描命中，我把这次排查中用到的检测脚本整理出来了。

下载地址：

`https://github.com/Neo-Maoku/cs_stage_probe`

**关注我,获取最新免杀技术**

#FlyC2 #C2平台 #红队工具 #网络安全 #自研工具

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oy1G7849AibBQDlENZ5c4usy9QawIN8mFQb8IiafOnZ7tW5KFMQ8Z5aHlEIsEvIiciaYmcT6hPhxFWd92CW6QlcXhw/0?wx_fmt=png)

毛酷红队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oy1G7849AibBQDlENZ5c4usy9QawIN8mFQb8IiafOnZ7tW5KFMQ8Z5aHlEIsEvIiciaYmcT6hPhxFWd92CW6QlcXhw/0?wx_fmt=png)

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