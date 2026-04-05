---
title: 虾聊——我的工作流怎么做的让OpenClaw机器人能稳定工作
url: https://mp.weixin.qq.com/s/VyIiccKtyVo6Th9RZmF3Lg
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:35:07.400428
---

# 虾聊——我的工作流怎么做的让OpenClaw机器人能稳定工作

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OY6GQJgbWJ1jHpCR2MO6NWiaAiaefqZNuX54oYcjVNqbCbK8GFicEE5d2nHWVyW0rxNIFAOEFa07RlCSA0S4rHPo3MN5JPKicRAuw/0?wx_fmt=jpeg)

# 虾聊——我的工作流怎么做的让OpenClaw机器人能稳定工作

原创

狗哥
狗哥

黑白之道

![]()

在小说阅读器中沉浸阅读

##

> 经验分享：如何通过编写稳定程序（新闻抓取、邮件管理、Agent通讯），让大模型只做决策与总结，省Token、提效率、可调试

### 一、痛点：提示词像一门充满歧义的高级语言

我们向AI描述一个任务时，实际上是用自然语言写了一段“代码”。但这段“代码”的执行环境极不稳定：

* **“获取今天新闻”** → AI可能尝试爬网站（被屏蔽）、调API（没给Key）、或者直接说“无法浏览”。
* **“帮我看看邮箱里有没有重要邮件”** → AI不知道你的邮箱服务器、账号密码，更无法安全访问。
* **“让Agent A 发消息给Agent B”** → 每个新Agent都要重新教它怎么配置邮件/微信/飞书，重复造轮子。

结果就是：**同样一句话，不同时间、不同环境，产出千差万别**。大模型把大量token浪费在“尝试-失败-再尝试”上，而我们还很难调试。

### 二、解决方案：为每个“歧义”编写一个程序，然后让大模型调用程序

**核心原则**：

1. **确定性的任务（网络请求、文件读写、邮件收发、计算）全部交给程序**。程序有日志、有错误处理、有重试，一次写好，永久稳定。
2. **大模型只做两件事**：① 理解用户意图，决定调用哪个程序（编译）；② 对程序返回的结构化数据做筛选、总结、推荐。
3. **程序统一封装为API或MCP工具**，所有Agent共享同一套能力，Agent之间通过这套程序间接通讯（例如通过共用的邮件程序发送内部通知）。

下面用两个具体例子说明。

---

### 例子A：获取新闻并筛选 —— 把“抓取”程序化

#### 原方式（纯大模型）

* 用户：“今天有什么值得看的科技新闻？”
* AI：尝试访问多个网站，可能被反爬，可能解析出广告，即使成功也返回大量原始HTML（消耗上千token），最后勉强总结几条，还时常漏掉重要来源。

#### 新方式：编写新闻程序 + 大模型筛选

**1. 编写稳定新闻程序** (`news_fetcher.py`)

```
# 调用NewsAPI或固定RSS源，输出结构化JSONimport requestsdef get_latest_news():    try:        response = requests.get('https://gnews.io/api/v4/top-headlines?token=YOUR_KEY&lang=zh')        data = response.json()        articles = [{'title': a['title'], 'source': a['source']['name'], 'url': a['url']} for a in data['articles']]        return articles    except Exception as e:        log_error(f"新闻获取失败: {e}")        return []   # 失败时返回空，不干扰大模型
```

2. 封装为API (`GET /api/news/latest`)
返回格式：

```
{"status":"success","news":[{"title":"...","source":"...","url":"..."}]}
```

3. OpenClaw调用流程

* 用户指令 → 机器人调用 `GET /api/news/latest`（仅消耗少量token获取标题列表）
* 将标题列表发给大模型：“请从中选出3条最值得阅读的，并说明理由”
* 大模型返回精炼推荐 → 输出给用户

**效果**：成功率接近100%，每次调用token仅需几十（标题列表）+ 几百（总结），且出错时可查新闻程序的日志。

---

### 例子B：邮件管理与Agent间通讯 —— 统一邮件接口，所有Agent共享

#### 痛点场景

* 你有多个Agent（比如“新闻助手”、“运维监控”、“客服机器人”），它们都需要**发送邮件通知**或**读取收件箱处理请求**。
* 如果每个Agent都单独配置SMTP/IMAP，不仅重复劳动，而且密码散落各处，一旦需要更换邮箱服务器，所有Agent都要改。
* Agent之间如果需要通过邮件协作（例如“监控Agent”发警报邮件给“值班Agent”），传统方式要求每个Agent都知道对方的邮箱地址和发送逻辑。

#### 新方式：编写统一邮件程序，暴露简单接口

**1. 邮件程序** (`mail_service.py`)

python

```
# 封装发邮件、读邮件、标记已读等import smtplib, imaplib, email
class MailService:    def __init__(self, config):        self.smtp_server = config['SMTP_SERVER']        self.imap_server = config['IMAP_SERVER']        self.username = config['EMAIL']        self.password = config['PASSWORD']
    def send_email(self, to, subject, body):        # 稳定的发送逻辑，包含重试和日志        try:            with smtplib.SMTP_SSL(self.smtp_server, 465) as server:                server.login(self.username, self.password)                msg = f"Subject: {subject}\n\n{body}"                server.sendmail(self.username, to, msg)            return {"status": "sent", "to": to}        except Exception as e:            log_error(f"发送失败: {e}")            return {"status": "error", "message": str(e)}
    def read_unread(self, folder="INBOX"):        # 读取未读邮件，返回结构化列表        # ... 实现细节        return [{"from": x, "subject": y, "body_preview": z}]
```

2. 封装为API或MCP工具

* **发邮件API**：`POST /api/mail/send`，参数 `to, subject, body`
* **读邮件API**：`GET /api/mail/unread`，返回未读邮件列表
* **删除/归档API**：可选

**3. 所有Agent直接调用**

* **新闻Agent**：筛选出好文章后，调用 `POST /api/mail/send` 把摘要发到你的私人邮箱。
* **运维Agent**：检测到CPU过高，调用同一个API发报警邮件。
* **客服Agent**：每5分钟调用 `GET /api/mail/unread`，检查客户发来的问题，然后调用大模型回复，再通过API发回邮件。

**4. Agent间的内部通讯通过邮件程序实现**

* 假设“监控Agent”需要通知“日志分析Agent”处理某个异常。
* 监控Agent调用 `POST /api/mail/send`，收件人填 `log-analyzer@yourdomain`（这个邮箱由日志Agent轮询读取）。
* 日志Agent调用 `GET /api/mail/unread` 获取该邮件，解析指令，执行任务，最后同样通过API回发结果。
* **完全不需要两个Agent知道彼此的配置**，只需要约定邮件主题格式。邮件程序充当了可靠的消息队列。

**效果对比**：

| 维度 | 每个Agent单独配置邮件 | 统一邮件程序接口 |
| --- | --- | --- |
| 配置成本 | N个Agent需配置N次 | 只配置一次，所有Agent共享 |
| 安全性 | 密码散落在多个Agent配置中 | 密码仅存在于邮件程序，对外不暴露 |
| Agent间通讯 | 需互相知道地址和协议 | 通过共用的邮件服务解耦 |
| 更换邮箱服务器 | 修改所有Agent | 只改邮件程序一处 |
| 调试 | 每个Agent看自己的日志 | 所有邮件操作集中在同一份日志 |

---

### 三、如何快速落地：API/MCP封装示例（以邮件程序为例）

python

```
# mail_api.py - 使用FastAPIfrom fastapi import FastAPI, HTTPException, Headerfrom pydantic import BaseModelfrom mail_service import MailService
app = FastAPI()mail = MailService(load_config())   # 单例，所有请求共用
class SendRequest(BaseModel):    to: str    subject: str    body: str
@app.post("/api/v1/mail/send")async def send_email(req: SendRequest, x_api_key: str = Header(...)):    if not verify_key(x_api_key):        raise HTTPException(401)    result = mail.send_email(req.to, req.subject, req.body)    return result
@app.get("/api/v1/mail/unread")async def get_unread(x_api_key: str = Header(...)):    result = mail.read_unread()    return {"status": "ok", "emails": result}
```

然后在OpenClaw中，任意Agent都可以通过`http_request`动作调用这些接口。

---

### 四、进阶：Agent间更高效的内部通讯（非邮件）

如果觉得邮件延迟较高，可以同样原理封装**Redis Pub/Sub**或**消息队列（RabbitMQ）**，暴露为API：

* `POST /api/mq/publish` → 发送消息到某个频道
* `GET /api/mq/subscribe?channel=xxx` → 长轮询或WebSocket接收消息

这样Agent之间可以实现毫秒级的内部通讯，且同样保持“一次编写，所有Agent共用”。

---

### 五，实际一点也不难，我给你一个实例。

### 我给openclaw一台虚拟机，我跟他说“去部署一个EMAIL服务程序，新建20个邮箱，安装那个安全性高的，不要出安全问题的Email 服务，完成之后将邮箱收发地址，帐号，密码生成文档发我。服务器IP，用户名，密码。sshpassw登陆安装“

### 一会安装完了会给我一个文档，

###

###

### 我将这个文档发给trae 跟他说：”写程序，

是一个收发邮件的插件，可以收发邮件，可以收发附件，可以读取邮件，内容，标题，来源，主题。

测试流程，一。你用给你提供的邮箱，相互发邮件，测试是否能收发？二。你用给你的邮箱相互发附件，看是否能收发。

最后，提供接口的地址和接口的使用方式和使用文档”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Ofjib1R3AO2tv0LWCmpuxTjpHUjyjL6p30ObpHtWyicMxLDkVubBcdRMChGsWpbwCJyMLaVcNZODM2bnR7qrkSbVE5OuDKYib6Is/640?wx_fmt=png&from=appmsg)

###

### 六、总结：把大模型从“执行者”变成“指挥官”

通过以上两个例子（新闻获取、邮件管理/Agent通讯），你应当能体会到：

* **每一个模糊的自然语言指令（“获取新闻”、“发邮件”）背后，都应该对应一个确定的程序**。程序负责所有不稳定的、需要权限的、重复性的工作。
* **大模型不再需要去学习如何配置SMTP、如何处理反爬**，它只需要学会“调用这个API”即可。这大大节省了token，也提升了成功率。
* **所有Agent共享同一套工具集**，新加入的Agent不需要重复配置任何环境，直接调用已有API，Agent间通讯也通过统一消息接口解耦。

**最终效果**：你的OpenClaw机器人集群将像微服务一样清晰 —— 每个Agent是轻量级的“决策单元”，背后是稳定的“能力API”。任何问题，查程序日志即可定位；任何新需求，写一个新API，所有Agent立刻能用。

这，就是将“提示词从歧义语言编译成程序调用”的真正威力。

真正能工作的openclaw一定是能稳定输出的，每次让他做事，知道他的结果不走样，这样才能真正工作起来。想要结果可控就要把控流程。没有什么高科技的活让龙虾去做，就是日常的琐事，每定时要做的事。这些交给龙虾，我们可以完全不参与。有创新的事只能自己全程参与控制才能不走样。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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