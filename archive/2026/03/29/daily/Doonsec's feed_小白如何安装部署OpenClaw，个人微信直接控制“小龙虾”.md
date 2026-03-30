---
title: 小白如何安装部署OpenClaw，个人微信直接控制“小龙虾”
url: https://mp.weixin.qq.com/s/bVMSBm5xHuoR5Hg7hc-9tQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:18.649876
---

# 小白如何安装部署OpenClaw，个人微信直接控制“小龙虾”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7u5dN14picXo3mHknWjib04jfgZIbwyuoDzk4guPyaA4eVkhjT6dwTCjYzMYBicVKXDcAB2rWQPLT8kcR6iayicflcvTQYibcaozb8Chhic4KEdZRg/0?wx_fmt=jpeg)

# 小白如何安装部署OpenClaw，个人微信直接控制“小龙虾”

mr wang
mr wang

黑客技术家园

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/wBb5fdnxUtWbzEQT65RpiaLBtjHDiaWQRSYCx5dhicDoHMVP42y7BjXnFgZM2IbMc7eAFnVn6ze4LqDD1E5NTdSoQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/5cV1SlPibQ8JWPQGsofz2U8SmlmzOFPjX46bCIyu5BGW1ekcHhQdiaQyBfKrGWSAX5oA2icY5s7B5D4uIz8pQR5Jg/640?wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7u5dN14picXpRRhiaXQk5yLA73mAEEk3bUQAYGicoaoJeMWhEpniczL9Og2w1Q4C2psfzbkXibW7iczcaaso5TcRYZbia1H0LgJt9AhIOmwTzSE5Yw/640?wx_fmt=jpeg&from=appmsg)

教程 | 用1Panel五分钟部署OpenClaw，个人微信直接控制“小龙虾”

你是不是也想过：在微信里像跟朋友聊天一样，发条消息就能让服务器帮你干活？不用开电脑，不用记命令，更不用在好几个App之间切来切去。

今天这篇教程，就带你用 **1Panel** 这个可视化面板，**五分钟**把 OpenClaw（江湖人称“小龙虾”）部署好，然后用你的**个人微信**直接指挥它干活。

> 为什么叫“小龙虾”？因为 OpenClaw 的图标是红色的，长得像一只龙虾，大家就这么亲切地叫它了。

## 一、为什么推荐用1Panel部署？

传统的部署方式，要在命令行里敲一堆代码，光是配置环境就能劝退不少人。但有了1Panel，一切都变成了**点鼠标**：

* **可视化操作**：不用记命令，在网页上点几下就能完成部署
* **一键安装**：应用商店里直接装，跟手机下载App一样简单
* **多实例管理**：一台服务器可以同时跑多个“小龙虾”，互不干扰（适合团队使用）
* **合规安全**：全程走企业微信官方通道，不用担心封号

**核心亮点**：这套方案部署完成后，**个人微信和企业微信都能操控OpenClaw**。想用哪个用哪个，灵活又高效。

**使用1Panel安装OpenClaw**

① 登录1Panel服务器管理面板，创建模型账号，选择模型供应商并填写对应的API Key等信息。

![图2-DhuS.png](https://mmbiz.qpic.cn/mmbiz_png/7u5dN14picXricatNicsXMqPgM1qdIGUaBp7PIER4KGVCAPeOAf064JU7ZAHNIQUDJk2OQ7ZIMA1V1V74mMJNO2TibMicJ31JcYmcsbQOkQFMdDc/640?wx_fmt=png&from=appmsg)

② 模型账号创建完成后，依次选择“AI”→“智能体”，进入智能体创建页面，在这里配置WebUI端口、访问地址、模型供应商及模型账号，其他信息保持默认即可，点击“确认”按钮后等待部署完成。部署成功后，可以通过以下两种方式访问OpenClaw界面：

■ 直接在浏览器输入：https://[公网地址]:端口/#token=xxxxx，其中Token值可以在智能体列表的“Token”列点击“复制”按钮获取；

■ 或者在智能体列表的“端口”列点击“WebUI 端口: 18789”按钮，即可一键跳转。

![图3-cFbq.png](https://mmbiz.qpic.cn/mmbiz_png/7u5dN14picXqWQMujG9AkYghnqdJgQQzsWLbFAVBpXHLbUlMQ7F8XkialOFWIlTMZ8fTBaUu69lePDQ3p0rlsl69SagBA8LQKNicVWMgKw2MBA/640?wx_fmt=png&from=appmsg)![图4-xZiD.png](https://mmbiz.qpic.cn/sz_mmbiz_png/7u5dN14picXrITUhCYDMH810iarsJAo8icPHRNFgibWLsQBJamvszma4fFKqDicwBvicOfTG1ajOeKTLo1O52ooG81BxyPrh9GreZv9vX7zJXhIJk/640?wx_fmt=png&from=appmsg)![5-MKPh.png](https://mmbiz.qpic.cn/sz_mmbiz_png/7u5dN14picXpEFYibk7icFew3C4DRs3MDxsicmM347bqKZ25kT8PKdcuUcQiaicn9V7MnkziapZejLRiadf3pSBNT9RUacpwHsUHofCf7W5Cvbk3PRs/640?wx_fmt=png&from=appmsg)

③ 如果访问公网地址没有任何输出，进入OpenClaw工作目录，调整配置文件/opt/1panel/apps/openclaw/OpenClaw/data/caddy/Caddyfile和/opt/1panel/apps/openclaw/OpenClaw/data/conf/openclaw.json，补充公网访问地址和端口，具体如下图所示：

![6-JEBH.png](https://mmbiz.qpic.cn/sz_mmbiz_png/7u5dN14picXpjW2gGmicQ58Hibic9nM8B6ljHDm6buLpc4IdBBZ0KEmYR1NtnicIw05hyqBekjSywNnmiaUyUnOIRAtHmGa7dPbGtmuZJyuG5a06g/640?wx_fmt=png&from=appmsg)![7-rEQe.png](https://mmbiz.qpic.cn/sz_mmbiz_png/7u5dN14picXp4iazVEpNu47FnUtGM1EuAuZQbcJtFLSb0kzFraNGJra95ZawgNRdHXgXdkYbrMqPw3ZyZHfYiaUIpcMwawfxBUsyx11HNJ25bk/640?wx_fmt=png&from=appmsg)![8-Tkal.png](https://mmbiz.qpic.cn/sz_mmbiz_png/7u5dN14picXr9qvvpz3h6RVVVrxKT3L91Xsevicw7C7ACiaLib4iaEW7rl1cIUiakE04eZVwbicfXibia1r5zbxYB3ABPy55390qwibCbtqDmUibN4GWGY/640?wx_fmt=png&from=appmsg)

调整配置后记得重启OpenClaw，再次访问公网地址和端口，可以正常访问。

![9-Vzog.png](https://mmbiz.qpic.cn/mmbiz_png/7u5dN14picXqBClVAtXgA0G31xecKdicEBdSBrmyd6nXeeDibMpORE9IFprRbEVtSfS56sibOonCmcIYlf8kNtB4cljKvwrUyOj4oy540gdxtdY/640?wx_fmt=png&from=appmsg)

二、准备工作（缺一不可）

开始之前，请确认下面这几样东西都备齐了：

| 准备工作 | 说明 | 怎么获得 |
| --- | --- | --- |
| **一台有公网IP的服务器** | 用于运行小龙虾，需要能通过互联网访问 | 阿里云、腾讯云、华为云等都有轻量应用服务器，2核2G配置就够用，新用户常有免费试用或优惠 |
| **1Panel面板** | 管理服务器的图形化界面 | 还没装的话，下面会提供安装命令，一键搞定 |
| **大模型API Key** | 给小龙虾装“大脑”，让它能理解你的话 | 推荐阿里云百炼（免费额度多）、DeepSeek（便宜）或直接用Ollama搭本地模型（免费） |
| **企业微信账号** | 作为通信桥梁，让小龙虾能和微信互通 | 个人就能注册，填个虚拟公司名就行，完全免费 |

> ⚠️ **关于服务器**：如果你用的是自己家里的电脑（没有公网IP），新手不推荐，因为需要配置内网穿透，比较复杂。建议花几十块钱租一台云服务器，省心又稳定。

---

## 三、第一步：安装1Panel（有面板的跳过）

登录你的服务器（用SSH工具，比如Xshell、PuTTY，或者在云服务商网页上直接登录），执行以下命令：

bash

```
bash-c"$(curl-sSL https://resource.fit2cloud.com/1panel/package/v2/quick_start.sh)"
```

执行后，系统会自动下载并安装1Panel。**安装完成后，终端会输出类似这样的信息：**

text

```
========================= 安装完成 =========================面板地址: http://你的服务器IP:xxxxx账号: xxxxx密码: xxxxx===========================================================
```

**一定要把这几个信息保存下来！** 然后用浏览器打开面板地址，输入账号密码，就能进入1Panel的管理界面了。

> 💡 **小提示**：如果打不开面板，可能是服务器的防火墙没有放行对应端口。去云服务商控制台，找到“防火墙”或“安全组”，添加一条规则：**允许 TCP 端口 xxxxx 的入站流量**（xxxxx就是面板地址里显示的那个端口）。

---

## 四、第二步：添加大模型账号（给小龙虾装大脑）

小龙虾要能听懂人话、干得了活，得给它配一个“大脑”。这里以阿里云百炼为例（其他平台类似）：

1. 登录 **阿里云百炼控制台**（https://bailian.console.aliyun.com/）
2. 在左侧菜单找到「API-KEY管理」，点击「创建API-KEY」
3. 复制生成的API Key（格式像 `sk-xxxxxxxxxxxxx`），保存好
4. 回到1Panel，左侧菜单点击「AI」→「智能体」
5. 切换到「模型账号」标签页，点击「添加模型账号」
6. 填写：

* **模型供应商**：选择“阿里云百炼”
* **API Key**：粘贴刚才复制的Key
* **名称**：随便起一个，比如“我的大脑”

7. 点击「确认」，页面会提示“添加成功”

> 💡 **如果用的是其他模型**：DeepSeek、OpenAI、Ollama等也都支持，操作类似。如果你是本地跑模型（比如用Ollama），需要先配置好Ollama服务，然后在1Panel里选择“Ollama”供应商。

---

## 五、第三步：一键安装OpenClaw（小龙虾本尊登场）

模型账号配好了，接下来部署小龙虾：

1. 在1Panel的「智能体」页面，切换到「智能体」标签页
2. 点击「创建智能体」，会弹出一个配置窗口
3. 按照下面的表格填写参数：

| 参数 | 建议值 | 说明 |
| --- | --- | --- |
| **名称** | openclaw | 可以自定义，比如“我的小龙虾”，不影响使用 |
| **应用版本** | 最新版 | 默认就是最新的，不用改 |
| **WebUI端口** | 18789 | 这是小龙虾网页管理界面的访问端口，记得在防火墙放行 |
| **Bridge端口** | 18790 | 这是内部通信端口，一般不用改，但也建议放行 |
| **模型供应商** | 上一步添加的那个 | 下拉框里选你刚才添加的“我的大脑” |
| **Token** | 自动生成 | 用于访问WebUI时的身份验证，自动生成就行，你也可以自己填一个 |

4. 点击「确认」，系统会自动拉取镜像、安装部署
5. 等待1-3分钟，直到状态显示为「运行中」
6. 点击智能体列表右侧的「WebUI」按钮，就能进入小龙虾的聊天界面了

> ✅ **验证是否成功**：在WebUI的对话框里随便发条消息，比如“你好”，如果能正常回复，说明小龙虾已经活过来了！

---

## 六、第四步：配置企业微信自建应用（搭通信桥）

这是最关键的一步——给小龙虾搭一座桥，让它能跟微信通信。

### 1. 创建企业微信自建应用

* 打开企业微信管理后台（https://work.weixin.qq.com/），用你的企业微信账号登录（个人也能注册）
* 点击左侧「应用管理」→「自建」→「创建应用」
* 上传一个Logo（随便找个图片就行），填应用名称，比如“我的小龙虾”
* 创建成功后，你会看到应用详情页。**记录下三个关键信息**：

+ **AgentId**：页面上直接能看到
+ **Secret**：点击“查看”按钮，会显示一串字符，**只显示一次，务必保存！**
+ **CorpId**：在「我的企业」页面底部，有个“企业ID”，复制下来

### 2. 配置API接收（让企业微信知道小龙虾的地址）

* 在应用详情页，找到「接收消息」卡片，点击「设置API接收」
* 点击「随机获取」按钮，生成**Token**和**EncodingAESKey**，把这两个也保存好
* **回调URL**填写：`https://你的服务器公网IP:18789/wecom-app`（注意是https，不是http）
* ⚠️ **先别点保存**，等到后面步骤完成再回来点保存

> 🛡️ **安全提示**：如果你的服务器用的是云服务商，记得在防火墙里放行 **18789端口**，否则回调URL无法被访问。

### 3. 安装企业微信插件（让小龙虾学会说企业微信的话）

回到小龙虾的WebUI界面（http://你的服务器公网IP:18789），在对话框里发送下面这条消息：

text

```
请直接帮我安装企业微信应用的插件，插件名是@openclaw-china/wecom-app
```

等待3-5分钟，插件会自动安装完成。如果安装成功，小龙虾会回复类似“插件安装成功”的消息。

> 🐛 **如果没反应**：可能是网络问题，可以刷新一下页面，或者等1分钟再发一次。

### 4. 配置插件信息（告诉小龙虾你的企业微信参数）

把刚才保存的所有信息（AgentId、Secret、CorpId、Token、EncodingAESKey）打包成下面的JSON格式，发到小龙虾的对话框里：

json

```
{"wecom-app":{"enabled":true,"webhookPath":"/wecom-app","token":"你的Token","encodingAESKey":"你的EncodingAESKey","corpId":"你的CorpID","corpSecret":"你的Secret","agentId":"你的AgentID"}}
```

> 💡 **怎么替换**：把“你的XXX”替换成你实际保存的值，注意引号不要丢掉，JSON格式要正确。

发送后，小龙虾会处理这个配置。等它回复“配置添加成功”后，回到企业微信的API接收页面，点击「保存」。如果没报错，说明通信链路已经通了。

### 5. 配置可信IP（非常重要！）

在企业微信应用详情页，向下滚动找到「开发者接口」→「企业可信IP」，点击「配置」，填入你的**服务器公网IP**（就是你访问WebUI时用的那个IP）。

**这一步如果不做，小龙虾能听到你说话，但没法主动回你。** 因为企业微信要求主动发消息的服务器必须在可信IP列表中。

### 6. 测试一下

* 打开企业微信App（或者电脑版）
* 在「工作台」找到刚才创建的应用，点进去
* 发一条消息，比如“你好”
* 如果能收到小龙虾的回复，恭喜你，桥梁搭好了！

---

## 七、第五步：微信扫码，小龙虾住进你的个人微信

最后一步，把小龙虾请进你的个人微信：

1. 在企业微信管理后台，点击「我的企业」→「微信插件」
2. 上传一个Logo（推荐640×640像素），然后点击「获取邀请二维码」
3. 用你的**个人微信**扫码关注
4. 关注成功后，回到企业微信工作台的应用对话框，再发一条消息
5. 这时候，你的个人微信应该也同步收到了回复

搞定！现在你可以在个人微信里直接跟小龙虾聊天了，就像跟好友聊天一样。

> 🎉 **大功告成**：你可以在微信里对它说“帮我查一下天气”“翻译这段话”，或者让它执行你配置好的各种技能。

---

## 八、能干啥？有啥限制？

### ✅ 小龙虾能帮你：

* **收发消息**：文字、图片、文件都能丢给它
* **远程干活**：提前装好skill（技能），发条指令它就执行
* **文件处理**：发给它一个PDF，它能帮你总结要点；发给它一张图片，它能帮你识别文字

### ❌ 小龙虾暂时做不到：

| 限制 | 说明 | 解决办法 |
| --- | --- | --- |
| **文件只进不出** | 你可以发文件给它处理，但它没法通过微信把处理好的文件发回给你 | 想拿回文件？可以用WebUI界面下载 |
| **进不了群聊** | 只能跟你单聊，没法偷听群消息 | 想让它分析群消息？可以手动把聊天记录复制给它 |
| **看不到你的隐私** | 它只能看到你和它的对话，看不到你的联系人列表、朋友圈、聊天记录 | 放心，你的隐私是安全的 |
| **24小时保活限制** | 如果超过24小时没跟它说话，它主动发的消息可能会被丢弃 | 想让它随时在线？每天随便发句“在吗”就行 |
| **一个微信只能养一只龙虾** | 但一只龙虾可以同时服务多个微信号 | 团队用的话，可以给不同成员分配不同应用 |

### 💡 使用小妙招

* 微信不支持图文混合发送，建议先告诉它“我待会发张图，帮我做OCR”，再发图，它会处理得更准确
* 你还可以给它**改名字、换头像**——在WebUI的“设置”里可以自定义，把它变成“马总”“小助理”，甚至“猫娘”都行

---

## 九、常见问题（...