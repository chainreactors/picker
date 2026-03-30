---
title: 微信里养一只“龙虾”保姆级教程：让AI助手陪你聊天、替你干活
url: https://mp.weixin.qq.com/s/nLpZ5PFUOZT1slP5e9CViw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:15.664129
---

# 微信里养一只“龙虾”保姆级教程：让AI助手陪你聊天、替你干活

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7u5dN14picXr8ic43fRfrBKhV0M9tQ28icNmJKy9jaKsTgjKKiaM0D9oxian4UwNKZn9Q83icqckWJPB6adq2kBQqmcILaZjjL88Ugebf2Y3Ods1A/0?wx_fmt=jpeg)

# 微信里养一只“龙虾”保姆级教程：让AI助手陪你聊天、替你干活

mr wang
mr wang

黑客技术家园

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/wBb5fdnxUtWbzEQT65RpiaLBtjHDiaWQRSYCx5dhicDoHMVP42y7BjXnFgZM2IbMc7eAFnVn6ze4LqDD1E5NTdSoQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5cV1SlPibQ8JWPQGsofz2U8SmlmzOFPjX46bCIyu5BGW1ekcHhQdiaQyBfKrGWSAX5oA2icY5s7B5D4uIz8pQR5Jg/640?wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

你有没有幻想过这样的场景：打开微信，像跟朋友聊天一样，发条消息，电脑那边的AI就默默帮你把任务完成了？不用开终端，不用记命令，更不用在几个App之间切来切去。

今天，我就手把手教你，在微信里“养”一只叫 **OpenClaw** 的AI助手——它的图标是红色的，大家亲切地叫它“**龙虾**”。养好了，它就是你的贴身小帮手，随叫随到。

![](https://mmbiz.qpic.cn/mmbiz_jpg/7u5dN14picXpBUe5uLhDH1purr7MybYPvx5dUmFooUIbzafufLIg7V2IfxY0A9Vs1z9oPVa8XunrccQYpYBhoRXtPtibxbvd4vWLSrNbPA5K4/640?wx_fmt=jpeg&from=appmsg)

## 一、龙虾是什么？能吃吗？

OpenClaw是一个开源的AI智能体框架。你可以把它理解成一个**听话又能干的机器人**。它本身不会飞进你的微信，但我们可以给它搭一座桥，让它在微信里跟你“对话”。

> 敲黑板：微信里那个“ClawBot”插件，或者我们后面要配置的企业微信应用，只是龙虾的**电话线**。真正的龙虾，得先养在你的电脑或服务器上。别急，下面会教你怎么养。

## 二、两条路，选哪条？

目前有两种主流方式让龙虾住进微信，你可以根据自己的喜好来挑：

| 对比项 | 🚀 方案一：官方ClawBot插件 | 🏢 方案二：企业微信搭桥 |
| --- | --- | --- |
| **适合谁** | 想快速尝鲜的个人玩家 | 追求稳定、甚至团队共用 |
| **安全吗** | 官方插件，妥妥的 | 全程走企业微信官方通道，合规可靠 |
| **功能** | 单聊够用，但不能进群 | 可以进群聊、功能更完整 |
| **难度** | 几分钟搞定 | 需要一台服务器，稍花点心思 |
| **双端通用** | 只支持个人微信 | 个人微信和企业微信都能用 |

简单说：想体验“发条消息就搞定”的感觉，选方案一；想长期稳定、甚至让团队一起用，选方案二。

## 三、方案一：官方ClawBot插件（5分钟速成）

这是腾讯官方推出的插件，操作简单到像装个表情包。

### 先确认两件事

* 你的微信版本号 ≥ **8.0.70**（iOS已全面开放，安卓的小伙伴如果没看到入口，别急，文末有“邪修”小技巧）
* 你已经有了一只“龙虾”（也就是OpenClaw）跑在电脑上（本地或云端都行）

### 三步搞定

**第一步：找到ClawBot插件**

打开微信 → 点右下角「我」→「设置」→「插件」。如果看到「微信ClawBot」几个字，恭喜你，入口已经有了。如果暂时没有，说明还在灰度中，再等等，或者跳到文末看安卓“邪修”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/7u5dN14picXooXAmSYFQHgxjyClsFzZJTS0q7JUVOOzYwjJm64RueHRz1H3SQfs8RxzRcJNc1L4ibjuCRR9oK0icia12teib5fkdYc1fd7QqhLfw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7u5dN14picXpSialnDFCoKt6T09Nm6IGwkLSJymvxZAeZY9l7eGXY2Pb0l3MGvQrEehGD01AhZhwhGAVicAVveDublueJ8GS8QNaj3J9vN4GG8/640?wx_fmt=jpeg&from=appmsg)

**第二步：在电脑上执行一条命令**

打开你电脑的终端（Windows是cmd或PowerShell，Mac是终端），输入下面这行魔法：

bash

```
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

敲下回车，屏幕上会蹦出一个二维码。

**第三步：扫码，完成**

拿起手机，打开微信，扫一下这个二维码。搞定！现在你已经可以和龙虾聊天了。

---

### 安卓用户专属“邪修”小秘密

如果你还没被灰度到ClawBot插件，试试这个方法：

1. 在电脑终端执行上面的命令，扫码
2. 微信会收到一个更新提示（版本号不变），点更新
3. 更新完后，再去「插件」里看，ClawBot就出现了
4. 再扫一次二维码，就能正常使用

⚠️ 注意：用这个方法，每次关闭微信后可能需要重新扫码。鸿蒙系统的朋友，功能暂时不全，可以再等等。

---

## 四、方案二：企业微信搭桥（更稳、更强）

这套方案就像给龙虾配了个“正式工牌”，走的是企业微信官方通道，合规又放心。一次部署，个人微信和企业微信都能发号施令。

### 你需要准备：

* 一个企业微信账号（个人也能注册，填个虚拟公司名就行）
* 一台有公网IP的服务器（阿里云、华为云、腾讯云都行，2核2G配置就够）
* 一个大模型API密钥（推荐阿里云百炼，简单便宜）

### 详细步骤：一步一步养龙虾

#### 第一步：在服务器上安家

如果你用阿里云，可以直接选带OpenClaw镜像的轻量服务器，省事不少：

1. 买台轻量服务器，镜像选「OpenClaw」
2. 在控制台放行 **18789端口**（这是龙虾的“家门”）
3. 连接服务器，输入以下命令，告诉龙虾它住哪儿、怎么接待客人：

bash

```
openclaw init --mode cloud --port18789openclaw gateway start
```

#### 第二步：给龙虾装大脑（大模型API）

以阿里云百炼为例：

1. 登录百炼控制台，创建一个API-Key（开头是sk-sp-）
2. 在服务器上执行：

bash

```
openclaw config set models.providers.bailian.apiKey "你的API-Key"openclaw gateway restart
```

这样龙虾就有了思考能力，可以理解你的话、帮你干活。

#### 第三步：在企业微信里开个“门”（自建应用）

1. 登录企业微信管理后台 →「应用管理」→「自建」→「创建应用」
2. 随便起个名字，上传个头像
3. 记下三个关键信息：

* **CorpID**（企业ID）：在「我的企业」里找
* **AgentID**（应用ID）：在应用详情页
* **Secret**（应用密钥）：点击查看，**只显示一次！** 记得保存

#### 第四步：配置“门铃”（API接收）

1. 进入应用详情 →「开发配置」→「设置API接收」
2. 点击“随机获取”生成Token和EncodingAESKey，保存好
3. 回调URL填写：`https://你的公网IP:18789/wecom-app`（先别点保存）

#### 第五步：让龙虾认识这个门

打开浏览器，访问 `http://你的公网IP:18789`，这是龙虾的Web控制台。在对话框里发送：

text

```
请直接帮我安装企业微信应用的插件，插件名是@openclaw-china/wecom-app
```

安装完成后，把刚才记录的四个信息以JSON格式发给它：

json

```
{"wecom-app":{"enabled":true,"webhookPath":"/wecom-app","token":"你的Token","encodingAESKey":"你的EncodingAESKey","corpId":"你的CorpID","corpSecret":"你的Secret","agentId":"你的AgentID"}}
```

#### 第六步：告诉企业微信“龙虾是可信的”

回到企业微信应用详情页，找到「开发者接口」→「企业可信IP」，填入你的服务器公网IP。这一步如果不做，龙虾只能听到你说话，却没法主动回你。

#### 第七步：微信扫码，开门迎客

1. 在企业微信管理后台 →「我的企业」→「微信插件」，获取二维码
2. 用个人微信扫码关注
3. 在企业微信工作台打开你的应用，发条消息试试
4. 如果个人微信也收到了回复，恭喜！龙虾正式入住微信了。

## 五、龙虾能干啥？有啥讲究？

### ✅ 它能帮你：

* **收发消息**：文字、图片、文件，都能丢给它
* **远程干活**：提前装好skill，发条指令它就去执行
* **文件处理**：发给它一个PDF，它能帮你总结要点

### ❌ 它也有小脾气（重要！）

| 限制 | 怎么理解 |
| --- | --- |
| **文件只进不出** | 你可以发文件给龙虾，但它没法通过微信把处理好的文件发回给你。想拿回文件？可以用它提供的网页界面下载。 |
| **不进群聊** | 它只能跟你单聊，没法偷听群消息。如果想让它分析群消息，可以手动把聊天记录复制给它。 |
| **看不到你的隐私** | 它只能看到你和它的对话，看不到你的联系人列表、朋友圈、聊天记录，放心。 |
| **24小时保活** | 如果超过24小时没跟它说话，它主动发的消息可能会被丢掉。想让它随时在线？每天随便发句“在吗”就行。 |
| **一个微信只能养一只龙虾** | 但一只龙虾可以同时服务多个微信号。 |

### 💡 使用小妙招

* 由于微信不支持图文混合发送，建议先告诉龙虾“我待会发张图，帮我识别文字”，再发图，它会更听话。
* 你还可以给龙虾改名字、换头像，让它变成你喜欢的角色——比如“小管家”“猫娘”“赛博助手”……

##

## 六、常见问题快问快答

**问：ClawBot和元宝有啥区别？**

答：元宝是腾讯自己的AI；ClawBot只是个“电话线”，连的是你自己养的龙虾。龙虾的本事由你决定，自由度更高。

**问：会封号吗？**

答：官方插件方案和企业微信方案都走的是正规官方通道，合规可靠，放心用。

**问：要钱吗？**

答：ClawBot本身免费。费用主要是服务器租金（如果用云服务器）和大模型API调用（一般有免费额度，用起来很便宜）。

**问：收不到消息怎么办？**

答：检查服务器端口放通了没、可信IP配置了没。如果是官方插件，确认微信版本已经更新到8.0.70以上。

---

好了，现在轮到你动手了。如果你在养龙虾的路上遇到任何问题，欢迎在留言区吱一声，我们一起解决。

祝你早日拥有自己的微信AI助手，让生活和工作变得更轻松一点～ 🦞

![图片](https://mmbiz.qpic.cn/mmbiz_png/Y2s0iaw7BLib5uPuCRc4tgwhATQwpOIscFORxRMbMiamCjC3yLCricrAEsaSpKNnxde0Y2WGEKpRPcs13WtQes3lOw/640?wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

往期推荐

[轻轻松松学会deepseek入门到精通，附清华大学教程，各大平台为什么都陆续接入](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247497092&idx=1&sn=814a9cc25a155debd1e6ed34b6226985&scene=21#wechat_redirect)

[手把手教大家如何学习deepseek，附教程](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247497060&idx=1&sn=372c80adc03bf275106aaafab652013b&scene=21#wechat_redirect)

[一文读懂！DeepSeek R1超简易本地安装运行部署教程](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247497053&idx=1&sn=80ff408155ccaad99c460d95778adba4&scene=21#wechat_redirect)

[如何实现deepseek本地部署？详细教学deepseek本地环境搭建及设置](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247497053&idx=2&sn=b0a854a1bb19d4708d590e5159c94505&scene=21#wechat_redirect)

[DeepSeek爆火快来搭建私有ChatGPT\_deepseek成为你私有化](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496962&idx=1&sn=ad190b15e766558d2b057e80e5eb864d&scene=21#wechat_redirect)

[手把手教大家如何使用微信接入deepseek](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496992&idx=1&sn=ba4f0600e915ad3f911dd3dd9308ddc8&scene=21#wechat_redirect)

[手把手教大家学习DeepSeek新手必看！全功能详解与实操指南，带你逆袭成AI大神](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496962&idx=2&sn=464bca3a03a1e209a0aff4cedb8341ad&scene=21#wechat_redirect)

[Android手机微信怎么找回删除的好友？其实很简单只需要简单几步就可以搞定](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496703&idx=1&sn=79bf4b6fe407e5271f65f5f94917dd00&scene=21#wechat_redirect)

[记录恢复办法。作为手机领域的领头品牌iiphone手机如何恢复微信聊天记录，这招可以帮您搞定](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496703&idx=2&sn=5eee3a758b08d4348ad494f026c56759&scene=21#wechat_redirect)

[如何把iPhone手机iOS15降iOS14系统，教大家如何一步步的操作](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496615&idx=1&sn=44542bdbfc2aaaf091fc291ace4abdab&scene=21#wechat_redirect)

[苹果手机显示“更新验证失败 因为您不再连接到互联网”怎么办？](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496615&idx=2&sn=553aaf178afd8551127f9d1db141fd78&scene=21#wechat_redirect)

[如何使用ELK搭建社工库](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496357&idx=1&sn=61d4fb7bd34676bc2b55a7dd919d8aae&scene=21#wechat_redirect)

[常见社工破解WPA2密码方法及防范措施](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496357&idx=2&sn=9fdcf73386bdee57cce588adb9bf8051&scene=21#wechat_redirect)

[社工库辅助工具查询大全分享](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496357&idx=3&sn=76cc4d3c8ec1891936a17843bbc494e4&scene=21#wechat_redirect)

[如何用爱思助手给苹果iPhone手机免越狱修改虚拟定位教程](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496236&idx=2&sn=58af8bf01f4ca1186ffbb624f12b5451&scene=21#wechat_redirect)

[如何用安卓手机定位iPhone手机值得大家收藏哦](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=2247496236&idx=1&sn=217e5283a854500a97e95d09f4862309&scene=21#wechat_redirect)

[抖音IP属地是实时更新的吗？抖音ip地址是实时位置吗如何才能修改](https://mp.weixin.qq.com/s?__biz=MzI2OTk4MTA3Ng==&mid=22...