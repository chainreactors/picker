---
title: WebSocket协议漏洞02_IDOR越权与DoS拒绝服务实战
url: https://mp.weixin.qq.com/s/Lkz7_t09Cj0YoHT5spSPWw
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:54:15.149876
---

# WebSocket协议漏洞02_IDOR越权与DoS拒绝服务实战

# WebSocket协议漏洞02\_IDOR越权与DoS拒绝服务实战

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NBQraFfaST4WVYCvx1oib0PMiaW7ztHpeInH4PLwxF4mCrEeic9Jm1gvHar4vEVraiaJ1rianibT9LOicuWicsjUIYibcLQ3LOuXD2GdZE/640?from=appmsg)
> **导语**：上篇拆了握手那一刻的八大致命风险，这篇聊握手之后。WebSocket 一旦升级成功，后续每条消息帧都是红队的游乐园——聊天/通知里的 IDOR 越权读写，能让 A 看见 B 的私信；连接洪泛 DoS 能把网关内存打满。本文基于 harsh-bothra/learn365 day14 实战清单展开。

---

## 一、IDOR 越权：换个 sid 就把别人私信翻出来

WebSocket 通道一旦建立，服务端靠"业务参数"识别"你是谁、要看哪条消息"。这些参数往往写在帧 payload 的 JSON 里，和 HTTP 参数一样可改——这就是 WebSocket 版的 IDOR（Insecure Direct Object Reference，不安全直接对象引用）。

### 1.1 测试步骤

harsh-bothra 给的红队清单非常直接，落到 Burp 里就是这套动作：

1. 浏览器里打开应用，登录攻击者账号 A，找到 WebSocket 通信端点。
2. 在 Burp Suite 拦截 WebSocket 消息（Burp 1.6+ 已原生支持 WS 拦截和修改）。
3. 在消息帧里翻 payload，找形如 `"sid": "用户A的ID"`、`"uuid": "..."`、`"role": "user"`、`"orderId": "10086"` 之类的字段——任何能唯一定位一个实体/对象的参数都是目标。
4. 把这个字段值改成目标受害者 B 的 ID，重放帧。
5. 看 A 的客户端有没有收到"按理只该 B 收到"的消息——收到就是 IDOR。

### 1.2 真实攻击链：聊天室的 sid 越权

原文给的典型场景：聊天应用里，攻击者给受害者发一条消息。帧里带 `"sid": "<攻击者自己的用户ID>"`。改成受害者的 sid 重放——A 的客户端收到"来自 B 的消息"，但 B 啥也没干。这就是经典的 IDOR。

更狠的还有：

* **读取类越权**：帧里带 `"orderId": "1001"`，改成 `1002`、`1003` 顺序遍历，把别人的订单详情全部拉下来。
* **写类越权**：金融场景里把 `"accountId": "self"` 改成 `"accountId": "victim"`，转账消息照常发出。
* **角色提升**：帧里 `"role": "user"` 改成 `"role": "admin"`，后台可能就直接放行管理操作。
* **跨租户越权**：SaaS 多租户系统里 `"tenantId": "tnt_A"` 改成 `"tnt_B"`，直接读别人租户的数据。

### 1.3 和 HTTP IDOR 一样套路

所有 HTTP 工作流里 IDOR 的检查项，全部用一遍就行：

* 水平越权：同权限用户之间 ID 互换。
* 垂直越权：低权限 ID 改高权限 ID。
* 遍历枚举：自增 ID 顺序遍历。
* UUID 类：UUID v1 可推断时间戳，v4 也可能被泄露泄露的会话表反查。
* 加密 token 类：JWT/session ID 改成别人的。

工具配合：

| 工具 | 用途 |
| --- | --- |
| Burp Suite | WS 拦截 + 修改 + 重放 |
| WebSocket Turbo Intruder | 高速批量重放帧 |
| mitmproxy + WS 插件 | 命令行抓包改包 |
| wsfuzzer / WS-Attacker | 协议级模糊测试 |

![WebSocket IDOR 测试示意图](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PJlIeg6xSWVSd80Cc1ZhBGlfynaUOJVHcia5zYVicQblbuTMEuLtGUqicsZhTjupk715gKGsdssgBzp7XZ2YOvJ495Ry33J7iaNBc/640?from=appmsg "WebSocket IDOR 测试示意图")

---

## 二、DoS 拒绝服务：把网关内存打到 OOM

WebSocket 设计上是长连接，服务端要为每个连接分配 fd、内存、状态机资源。攻击者只要能批量起连接，就能把服务端资源吃满。

### 2.1 连接洪泛

原文里第一条："WS allows any number of connections to the target server."

这就是连接洪泛的根因。攻击者开一台机器，挂上万条空闲长连接，服务端就得上万份 socket buffer + 状态表。Web 应用网关常见连接上限在 1k-10k，几秒就能打满。

实测套路：

```
# 用 Python 一行起 5000 个空闲 WS 连接
python3 -c "
import asyncio, websockets
async def hold():
    while True:
        try:
            async with websockets.connect('wss://target/chat') as ws:
                await ws.recv()  # 阻塞等消息
        except: pass
async def main():
    await asyncio.gather(*[hold() for _ in range(5000)])
asyncio.run(main())
"
```

或用现成工具：

* **WebSocket Flooder**（GitHub 一堆）：并行起几千连接，每个发 ping 保活。
* **Slowloris-WS**：发半个握手包挂住，让服务端在 SYNC\_WAIT 状态堆积。
* **黄金眼**：先用慢速建立大量连接占用 fd，再触发服务端业务处理，把 CPU 也吃光。

### 2.2 应用层 DoS

原文第二条："Try sending multiple requests to initiate a WS connection in a short time."

这条更阴险。WebSocket 握手是 HTTP Upgrade，服务端收到请求要走完握手 + 业务校验 + 用户鉴权 + 状态初始化才会进入稳定连接态。如果业务逻辑重（比如握手成功要查 DB、要分配内存、要发欢迎消息），攻击者可以：

* 1 秒内发起 1 万次握手请求，服务端 CPU 全耗在握手处理上。
* 握手成功后立刻发畸形帧，触发服务端解析异常抛出，CPU 浪费在异常处理。
* 发巨型帧（payload 几 GB），服务端要么 OOM，要么协议栈崩。

更阴的是"应用级卡顿"——握手后立刻断开循环重连，让服务端反复执行"建连-分配资源-断连-回收"，中途还插几个慢帧，最后变成 GC 不停、服务端响应延迟 P99 从 50ms 涨到 5s。

### 2.3 攻击分类图

![WebSocket DoS 攻击链路图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MSqHKsh13EXaxKEn9w8ia62gPhXfkn3MoJZk76RYBFJK4sI51cx5hcVuOCicTuFdyKaozSSEIJib6VGK7TsgoH2N2zz2ibpJoXAr0/640?from=appmsg "WebSocket DoS 攻击链路图")

---

## 三、纵深防御：服务端必须做的五件事

### 3.1 IDOR 侧

1. 服务端**永远不信任帧里带的 ID**，必须从会话 token 解析出"真实用户"，再用这个用户去查对象——而不是用帧里传过来的 ID。
2. 所有读写操作走"我的对象/他的对象"鉴权层，水平越权直接 403。
3. 业务 ID 用不可预测的 ID（UUID v4、雪花 ID、自增 ID 加密混淆），不让攻击者枚举。
4. 关键操作加二次校验（转账 / 删除 / 修改权限必须重新输密码或二次确认）。
5. WS 服务器侧**日志全留**：每条帧的发送者、目标值、操作类型全部审计，事后追溯。

### 3.2 DoS 侧

1. **连接数限速**：单 IP / 单用户最大并发连接数（比如 ≤ 100），超过直接 RST。
2. **握手速率限制**：单 IP 握手 QPS 上限，超出返回 429。
3. **帧大小限制**：单帧 payload 上限（常见 64KB-1MB），超出直接断连。
4. **空闲超时**：超过 N 分钟无消息自动关闭，回收 fd 和内存。
5. **边缘 WAF 兜底**：CDN / WAF 层先把畸形握手挡掉，不要让业务网关直接面对公网洪流。

---

## 四、回顾与下篇预告

day13 拆了握手那一刻的八大致命风险，day14 这两条路径是握手成功之后红队最爱打的——IDOR 把权限打穿，DoS 把资源打满。两类问题在传统 HTTP 工作流里也有，但放到 WebSocket 上反而更危险，因为攻击者更容易"潜伏"在长连接里慢挖。

下篇 day15「Prototype Pollution」，把 JavaScript 对象污染放到原型链上玩——这玩意儿一旦和 Web 模板、Node 后端、JS 沙箱混在一起，杀伤力比 WebSocket 这两篇加起来还大。

---

**原文出处**：harsh-bothra/learn365 · day14 **延伸阅读**：OWASP WebSocket Security · PortSwigger WebSocket labs

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PMk6U8ibdy6SE8I9cDrgk2dXsKLxfic1hOJE1LKhz9tbvvW5ItlJP9ZicxP4uIA5ryXqBocJrPbyicEEjFfZf2g2FfJqia15sic4suU/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6PaKkALgrjgV4YmEr4Q8gv1sUAXjj3EZKZcGnaWQyJibholgRXep6Yqwdf6FY7iadnsMXZt25d6V2rrqBKzszVqSoG1TRgAnPoLo/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OZRQR7czq1ZkfvD1fibGhU54WFTNiaxM8U4GCpzdppHwSoChXVXPHxNLzky1S8JaXoWw2uL9yNPpibzVBUlTHiaNInS0LCuo5F99Y/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MAROTaiaQT6rIoXs8NGR08yxB3TV5x4dnjYN9bqtQPBlRC5Or94aibxMtUptXYnMcFBh5iaqud1MYVic5f0YbwxpEcPtASf2MDO6A/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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