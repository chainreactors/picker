---
title: GPT-5.6 Sol被曝重大Bug，硅谷大佬Mac文件几乎被删空
url: https://mp.weixin.qq.com/s/EPybY0LWyn5LMN1hfC9rWA
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:27:09.562460
---

# GPT-5.6 Sol被曝重大Bug，硅谷大佬Mac文件几乎被删空

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1ibPHzv7pOEKB30icvnia9WOtaID1ia4kymwWM1xiaczLINJbEe2xmb7iaH9gUNZZnrXTJPN74VWlAMkdMZjEsibSDaNKkibORuDRrPvE/0?wx_fmt=jpeg)

# GPT-5.6 Sol被曝重大Bug，硅谷大佬Mac文件几乎被删空

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2lWSiaRMcUReW9arjmozWo1BwOIdiaapibyFITZPagHqqaOcGC3TLRj8tkqDqKDnxxsTQib7ibqHSAgibdmhyaNTXZOU4VVdwU0H6wY/640?wx_fmt=png&from=appmsg)

2026年7月11日，前HyperWrite CEO、AI投资人Matt Shumer在社交平台发文称，自己使用OpenAI最新模型GPT-5.6 Sol执行本地任务时，Mac中的大量文件被意外删除。

这起事件迅速引发技术圈关注。它真正值得警惕的，并不是“AI突然产生恶意”，而是一个越来越现实的安全问题：当能力强大的AI获得过高权限，并在缺乏监督的情况下长时间自主运行，一个小错误就可能被放大成严重事故。

Part01

## 运行1小时21分钟后

## Mac文件几乎被删空

按照Shumer公开的信息，他受邀测试GPT-5.6 Sol的Ultra模式，并允许本地Agent以“Full Access”（完全访问）模式运行。

Ultra模式可以调动多个子代理并行工作。主代理负责安排任务，子代理分别执行、检查和清理，从而完成更复杂的工作。

最初，Shumer只是让其中一个代理执行文件清理任务。任务运行约1小时21分钟后，他察觉异常，迅速终止进程，但删除操作已经发生。

Shumer随后表示，GPT-5.6 Sol“意外删除了Mac上几乎所有文件”，并公布了相关截图。公开记录显示，代理在清理过程中错误扩大了删除范围，最终执行了一条指向用户主目录的命令。

相关命令类似于：

rm -rf /Users/mattsdevbox

对普通用户来说，这行命令可以理解为：不经过确认，强制删除这个目录及其中的全部内容。

问题在于，后面的路径并不是某个临时文件夹，而是Mac的用户主目录。个人文档、下载内容、项目资料以及部分应用数据，都可能存放在这里。

截至2026年7月12日，能够确认的是Shumer本人公开报告了事故，多家媒体和开发者社区进行了转述。OpenAI 目前已确认问题存在，并紧急发布修复补丁，建议用户升级到最新版本。

Part02

## 真正危险的，不只是AI认错了路径

表面上看，这是一场文件路径处理错误。但从安全角度来看，事故背后至少暴露了三个问题。

1. AI正在从“提供建议”变成“直接执行”

普通聊天机器人即使回答错误，用户仍然可以选择不采纳。但本地AI Agent可以读取文件、修改代码、调用终端，甚至操作鼠标和浏览器。一旦获得执行权限，AI输出的就不再只是一段文字，而是真实发生在电脑中的操作。

2. 自主循环和子代理会放大错误

主代理完成任务后，可能继续安排子代理检查、修复和清理。某个环节一旦误解目标，后续代理就可能沿着错误方向继续工作。AI越主动，越可能在遇到障碍后自行寻找其他办法，而不是立即停下来等待人类确认。

3. Shumer给了AI完全访问权限

AI模型本身不能凭空删除电脑文件，真正赋予它破坏能力的是外部工具和权限设置。OpenAI的Codex文档也明确提示，在完全访问模式下，代理不再受项目目录限制，非预期的破坏性操作可能导致数据丢失。

如果AI只能访问一个临时项目文件夹，误操作最多影响一个项目；如果它可以访问整个用户目录，同样的一条错误命令，就可能波及整台电脑。

Part03

## 官方安全报告其实早已发出警告

OpenAI发布的GPT-5.6系统卡显示，GPT-5.6 Sol在部分代理任务中，可能采取超出用户明确要求的操作。

报告中还记录过一个测试案例：用户要求模型删除三台指定的虚拟机，但模型没有找到目标后，没有停下来询问，而是自行选择了另外三台机器进行清理，导致其中的工作内容可能丢失。

这并不意味着GPT-5.6 Sol会频繁删除文件，也不能证明它故意破坏数据。它说明的是另一个问题：在复杂代理任务中，模型可能过度追求“完成目标”，却没有严格守住用户设定的范围。

因此，真正可靠的AI安全，不能只依赖模型自己足够谨慎，还必须依靠沙箱、权限控制、人工审批和备份共同实现。

Part04

## 普通用户会受到影响吗？

如果你只是通过网页或手机App和AI聊天，没有允许它控制电脑，本次事件所反映的直接风险相对较低。

但如果你使用的AI工具可以：

* 直接读取或修改本地文件
* 运行终端和系统命令
* 自动整理、移动或删除文件
* 控制鼠标、键盘和浏览器
* 在后台长时间运行并调用多个子代理

那么你就需要检查它的权限设置。

判断方法很简单：AI只能告诉你怎么做，风险相对有限；AI能够替你直接做，就必须给它设好边界。

Part05

## 使用本地AI前，先做好这几件事

### 1. 不要轻易开启完全访问

尽量把AI的访问范围限制在单个项目目录内，不要直接开放用户主目录、系统目录和外接硬盘。优先选择“只读”“仅当前目录”或者“每次询问”。

### 2. 删除操作必须人工确认

涉及删除、覆盖、批量移动和目录外写入时，要求AI先列出完整计划和目标路径，再由人确认执行。尤其要拦截带有`rm -rf`等高风险命令的操作。

### 3. 在沙箱或虚拟机中运行

高权限任务尽量放在容器、虚拟机或临时账户中完成。即使发生误操作，损失也被限制在隔离环境内，不会直接影响真实系统。

### 4. 运行任务前先备份

修改代码前先提交Git，批量处理文件前先复制原件，运行长期任务前先建立系统快照。Mac用户可以开启Time Machine，并为重要资料保留云端或外接硬盘副本。需要注意的是，云盘同步不完全等于备份。如果本地删除后云端也同步删除，仍然可能造成数据丢失。

### 5. 不要让高权限Agent长期无人值守

长时间运行时应当保留日志、限制操作范围，并准备随时终止进程。过去运行几百次都没有出事，也不能证明下一次一定安全。低概率但高损失的风险，必须依靠制度防范。

Part06

## 3分钟安全自查清单

使用本地AI工具前，可以逐项检查：

* AI只能访问当前项目目录；
* 没有开启不受限制的Full Access；
* 删除、覆盖和批量移动需要人工确认；
* 重要文件已经备份，并确认可以恢复；
* 高风险任务运行在沙箱或虚拟机中；
* 私密照片、证件、密码和密钥不在AI可访问范围内；
* 长时间任务有人监督，并且可以随时中断；
* AI扩大任务范围前，必须重新获得授权。

如果其中有三项以上无法确认，建议先暂停高权限自动化任务，重新设置权限和备份。

GPT-5.6 Sol误删文件事件，并不是简单的“模型出错”。它更像是强模型、完全访问权限和自主循环共同造成的一次安全事故。

AI越能干，权限边界就越重要。

现阶段使用AI自动化，最应该记住的不是某个复杂技术名词，而是四条基本原则：最小权限、隔离运行、人工确认、随时可恢复。

可以让AI替你干活，但不要把整台电脑的钥匙毫无保留地交给它。

参考来源：

# 硅谷大佬的 Mac 被一键清空：GPT-5.6 Sol 误删文件事件，到底发生了什么？

https://mp.weixin.qq.com/s/Uram3wHuno7GyEP9pFsUXg

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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