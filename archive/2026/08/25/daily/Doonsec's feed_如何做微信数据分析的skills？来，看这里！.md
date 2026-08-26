---
title: 如何做微信数据分析的skills？来，看这里！
url: https://mp.weixin.qq.com/s/CpqsDZ6UhQ0Em1HlzlPAgQ
source: Doonsec's feed
date: 2026-08-25
fetch_date: 2026-08-26T03:01:03.915256
---

# 如何做微信数据分析的skills？来，看这里！

# 如何做微信数据分析的skills？来，看这里！

美亚MCE在线
美亚MCE在线

美亚柏科

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/fsbDGCu9WrZExMeL5wX84TUcVly2iaXvR0ENxOWsicjich3Pjm235UOsNvyqZ65CRChPuXDEBic7MqsP48DdRljZcw/640?wx_fmt=gif&from=appmsg)

微信数据动不动就是**几十个 G**，翻聊天记录翻到眼花，人物关系靠脑补，资金往来靠 Excel 手工拉——这是不是很多兄弟办案的真实日常？

手机一多更崩溃：一台手机几百个联系人、每人几百条转账记录，光是把"谁和谁有关系、谁给谁转过钱"理清楚，就得熬好几个通宵，还不一定理得全。

但如果告诉你：**几分钟就能自动生成人物关系图谱和资金往来明细**，点一下人物节点，还能看到每一笔钱的数据出处——你信不信？

这期就带来实战玩法：**超级取证大师提取微信数据**＋对接**AI Agent**，让 AI 直接帮你出结果。先看效果图：

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/TMxE0qBEYpVk39gTM4X77Dr1UibYjfyavoq1xUgyCV5G0lHY43fIYFJN5mUky40GYicfJKWRpaicf6bfSc8l1pUDeMzia0awaz7FApUxibicEyD6U/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=1)

效果图：自动生成的可交互关系图谱

## 先搞懂两个词，后面就顺了👇

30 秒扫盲：skills 和 MCP 是啥

**🧩 skills（技能）**＝ 给 AI 的"岗位说明书"

告诉 AI"你是数据分析专家，遇到微信数据该怎么处理、输出什么格式"。有了它，AI 就知道这个活儿该怎么干，不用每次从头教。

**🔌 MCP（模型上下文协议）**＝ 给 AI 的"USB 接口"

让 AI 能直接连接超级取证大师、读取它提取出的数据，而不是把几十 G 的原始文件喂给 AI。

一句话总结：**skills 告诉 AI 怎么干，MCP 给 AI 工具用。**

## 整套流程长这样👇

四个环节，一条流水线

整套流程串起来就是一条"流水线"，四个环节各司其职：

![图片](https://mmecoa.qpic.cn/mmecoa_png/TMxE0qBEYpUMvz7otS4Uiajx64IuVCj8C7krQZqicQPg1Q8SwoXibMNy5dvB6O3z5lZSibMZh57rk4TDeLbNOZpGgIJ7w1282yOBT6PUBeWJ36Y/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=2)

整条链路不需要写代码，也不需要把原始数据"喂"给大模型——数据在本地，AI 只负责分析和出图。

## 接下来进入实操 👇

跟着 6 步走，从提示词到可点击的关系图谱

### 1DeepSeek 生成 skills 提示词

根据自己的实战经验，先在 **DeepSeek** 的专家模式下生成 skills 提示词。这一步比较吃**实战经验**——你想让 AI 实现什么场景，直接告诉它。

一个能"用"的提示词，建议说清楚这四件事：

🎭 **角色**：数据分析专家
📥 **输入**：微信聊天 / 转账 / 红包数据
📤 **输出**：可交互的 HTML 关系图谱
🔗 **关系维度**：同事、亲人、领导、情人等标签

经验描述得越具体，AI 生成的 skill 越贴合你的办案场景。

![图片](https://mmecoa.qpic.cn/mmecoa_png/TMxE0qBEYpV2zjxPCNlnUttVTLMdY1B4G8W8ny7Hc49GibddwrQxmmUw8b8CgfUTeU66cfglCkUwK8qMRSeIpXkiaibXjlCeNMcliaBzFOEib9Ks/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=3)

DeepSeek 专家模式下输入提示词

### 2复制 DeepSeek 输出的提示词

DeepSeek 生成完毕后，直接点击红框里的复制按钮，把提示词先存好备用。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/TMxE0qBEYpXgiaPpcRyQ7k3c2c26f9nQzHSRudR1Lg9SaUxxFJnAxwAlsgENaxMLwVTYVicicUtO1qGAkDQ7cT60FcpwxvxU80BYk1ic0plfwO0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=4)

复制 DeepSeek 生成好的提示词

### 3在 WorkBuddy 中触发 skills 生成

打开 **WorkBuddy**，在对话框中输入魔法指令"根据下方的提示词生成 skills:"，然后把刚才复制的内容粘到下方，发送。

WorkBuddy 会自动把这段提示词"翻译"成标准的 skills 格式，并加载到当前会话里——这一步不需要你懂任何代码。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/TMxE0qBEYpUVO9QRX5hzkg8d8PrGMmvvRhXPIxHm5twRd4Yw08xZXevxCk7UwyJf6nx52xrV5rEa0vUJnQ23nkEiaw8BnRMjnPdUic8Wu9DTE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=5)

在 WorkBuddy 中触发 skills 生成

### 4skills 生成成功，自动产出图谱

片刻即可看到生成成功的提示，右侧预览窗口还会同步出现关系图谱雏形——说明 skill 已经生效，接下来可以直接调用了。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/TMxE0qBEYpX1tJibGfCWrSxeibUicicP81Qa3s3k05scu0W4AxfGTJrd0S4Apiaate5ibFTWic7hMawbdhMjn6Mcpuiaica18wkBnxyW6qKBIIX4Q5GI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=6)

skills 生成成功，自动产出可视化图谱

### 5调用 MYOS MCP 工具分析微信数据

基于刚生成好的 skill，继续发送提示词：

> **"基于这个 skills，调用 MYOS 的 MCP 工具，分析超级取证大师提取的微信数据。"**

![图片](https://mmecoa.qpic.cn/mmecoa_png/TMxE0qBEYpXPOfZC9n8xib3UTicyK91SMAaXdW8IpGo4FMibbKcdzmShLWC3j1Nv4dzgPNxM96TiaHv2LiaiaiakceicfapsiaaIw3Z0dpvrO7yltXWo/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=7)

调用 MYOS MCP 开始分析微信数据

### 6生成完成，点击节点查看明细

生成完成后，一张完整的关系图谱就出来了。接下来可以这样用：

① 点击图谱中的**任一人物节点**；

② 查看该人物的**资金往来汇总**与**资金往来明细**；

③ 每条明细都带**数据出处**，可直接回溯到原始聊天/转账记录——证据链清晰，取证报告好写。

![图片](https://mmecoa.qpic.cn/mmecoa_png/TMxE0qBEYpXvM673icichTQP8ibWz2lic9icawq728mxbs91WUiaqv1KlXPIuholoOS4gM2ut6XUV1p6repWA8qB9XPMOWibajrUsbpsCABZibianTfs/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=8)

最终生成的关系图谱与边数据

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/TMxE0qBEYpUVF2DneRkgqNS8ibOpib0LuhRSF70UgBAxg5ccZufpl3UADSp4ibS8weA4urVZ5e0qMgUVzjoPJE0icnUHA9NLDwalT1Th82SLgz8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=9)

点击节点查看资金明细与证据出处

## 学会了能用在哪些场景👇

关系图谱 × 资金链路 × 数据出处

🧠 这张图，不只是"好看"

🧑‍🤝‍🧑 **人物关系图谱**：自动标注同事 / 亲人 / 领导 / 情人等关系标签
💰 **资金链路**：转账、红包往来自动汇总，资金流向一目了然
🔍 **数据出处**：每一笔往来都能点回原始记录，经得起复核

🚀 延伸玩法（抛砖引玉）

👥 团伙案件：找出通讯录里的"联络中枢"
💸 资金追踪：锁定资金的最终流向
🕐 时间线分析：案发前后谁和谁频繁联系
🔗 多案件串并：跨手机比对共同联系人

## 和传统方法比，差多少👇

一张表看懂效率差距

![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/TMxE0qBEYpWGIxOtEZEN5XWu9rHX5PSXGosdwyYV9o0hjlUWaUKCAn0bgMvwxM30N0orErEz17hq9TJc4iaKSKxI0jkVEP2DH3yyPV7siaFLM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=10)

当然，AI 出的是"分析辅助"，关键结论仍要回到原始数据复核——这也是为什么图谱里每条明细都保留了出处。

## 真实办案场景长什么样👇

一个案例讲透使用价值

📖 一个真实场景

某起案件里，嫌疑人的手机里有几百个联系人，人工翻了三天，只理出十几条关系，还有一堆"看着眼熟但想不起在哪见过"的转账。

用这套方法几分钟生成图谱后，发现所有资金都汇向同一个"中间人"账号——原来他就是团伙里的"财务管家"。

顺着他一查，整条资金链路全部浮出水面，省下的时间都用在了后续深挖上。

**📝 写在最后**

以上只是一个很简单的提示词，抛砖引玉——大家可以根据自己的**实际工作场景、工作经验和技战法**，让 AI 真正赋能办案。

**⚠️ 数据安全提醒：**如果数据比较敏感，有条件的同学建议调用**本地大模型**对数据进行处理，避免敏感信息外发。

**⚖️ 合规提醒：**取证数据来源必须合法合规（立案 / 授权），分析过程建议留存操作日志，确保证据链完整。

想直接套用提示词模板的，**评论区扣"1"**，下期整理一份可以直接用的出来～

觉得有用就点个赞、转发给需要的兄弟，让更多人少熬夜。

## 你可能想问的👇

几个高频问题一次说清

❓ 常见问题

**Q1：几十 G 的数据，AI 会不会很慢？**
A：不会。MCP 直连超级取证大师，AI 只读取需要分析的字段，原始文件不会整体喂给模型。

**Q2：需要多高的电脑配置？**
A：联网调用大模型，普通办公电脑就能跑；数据敏感的场景，改用本地大模型，对显存有一定要求。

**Q3：生成的图谱能保存下来吗？**
A：可以。输出是可交互的 HTML 文件，能直接保存、转发、打印，也可以作为分析报告的附件。

**Q4：只能分析微信吗？**
A：超级取证大师支持的通讯录、账单等数据都能对接，按同样的思路扩展 skill 即可。

转载自：美亚MCE在线

![图片](https://mmbiz.qpic.cn/mmbiz_gif/keicctSy9PHqqq0EMDqIGWAOHgx1TEQ60DAeFia3LgMsicbrS08owic42CBKGVQQGI7B08V82dSYcbib6xxbibrLYIypZFSCibxYQhKcmGqJluXufQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

**往期推荐**

RECOMMEND

1

[首发，邀你尝鲜！](https://mp.weixin.qq.com/s?__biz=MjM5NTU4NjgzMg==&mid=2651452648&idx=1&sn=9cdae1e92ad9de268f3502ec29c0bb22&scene=21#wechat_redirect)

2

[2026下半年取证备赛利器！超级取证大师免费试用4个月](https://mp.weixin.qq.com/s?__biz=MjM5NTU4NjgzMg==&mid=2651452633&idx=2&sn=11970cbc68747b1ec599c9515bb3b705&scene=21#wechat_redirect)

3

[鉴定实例→摩托车追尾小汽车致人死亡交通事故](https://mp.weixin.qq.com/s?__biz=MjM5NTU4NjgzMg==&mid=2651452634&idx=1&sn=d54c49ce0b5baa89e389522f59061139&scene=21#wechat_redirect)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fsbDGCu9WrYZQuCfqH33w1ujmA9Xxp39UpLryDJtrmBt7GpwHPJREX5OofZWNnjdTltA0O2ePa9BiawVEjn3PfQ/0?wx_fmt=png)

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