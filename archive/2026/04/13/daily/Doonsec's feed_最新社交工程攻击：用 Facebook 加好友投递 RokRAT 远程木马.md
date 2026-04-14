---
title: 最新社交工程攻击：用 Facebook 加好友投递 RokRAT 远程木马
url: https://mp.weixin.qq.com/s/caz8nyiJ0cEptXNFXP8u0g
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:39:48.599849
---

# 最新社交工程攻击：用 Facebook 加好友投递 RokRAT 远程木马

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwk9sFX0lRumQgWcl5mHeHwEj2E3JTTn90QYx10mjls0JGmd6ON2r2qGHibbxSeuVLHR9JFVYz46bR6Jkv0cQnicVxadxSE1qnFHrM/0?wx_fmt=jpeg)

# 最新社交工程攻击：用 Facebook 加好友投递 RokRAT 远程木马

原创

Ravie Lakshmanan
Ravie Lakshmanan

泷羽Sec-Norsea

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#### APT37 最新攻击手法：利用 Facebook 社交工程投递 RokRAT 远程木马

4月13日，韩国安全公司 `Genians Security Center（GSC）` 发布技术报告，披露朝鲜关联 `APT` 组织 `APT37`（又称 ScarCruft、Reaper、Ricochet Chollima） 正在开展一场高度规避的多阶段社交工程攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4T1PVwJicwk939Iz3w56zp1UIzkb4hF8gdFZ2Eecw8bw8ZawHx4dWabBIfD686cwKC4ibibmcnPX0KCiccMV9dAP7nSwRg8ExyfdPA8QYKKgo1M/640?wx_fmt=jpeg&from=appmsg)

攻击者不再依赖传统的钓鱼邮件，而是直接在 `Facebook` 上主动添加目标为好友，通过建立信任、转移对话，最终诱导受害者安装被篡改的 PDF 阅读器，从而植入功能强大的远程访问木马 RokRAT。

这起攻击再次展现了 `APT` 组织在社交工程与供应链投递上的高超技巧。

攻击背景与组织画像`APT37` 是朝鲜 `Reconnaissance General Bureau（RGB）`下属的长期活跃网络间谍组织，自 2012 年以来持续针对韩国、美国及相关领域的智库、学术界、军工企业和政府机构实施情报窃取活动。

其核心武器 `RokRAT` 是一款云端托管的远程访问木马（RAT），核心功能稳定，已在过去多年多次渗透实战中被反复使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4T1PVwJicwkicIJI8yjEfbF8Y7MialPic71NIXsn8074sGtufQJV0UTHw823JHADCnRnaA89rgODdawv50WF2D9MicqswpbKGSZIqeEsiaZKB66BA/640?wx_fmt=png&from=appmsg)

### 完整攻击链路详解（6 步）

#### 1.脸书社交工程阶段

##### 攻击者创建了两个 脸书 账号：

* `“richardmichael0828”`
* `“johnsonsophia0414”`两个账号均于 2025 年 11 月 10 日 创建，位置设置为`（Pyongyang）`和`（Pyongsong）`。他们主动发送好友请求，通过聊天建立信任后，将对话从 脸书 转移到 Messenger，再进一步引导至 纸飞机。

#### 2.诱导下载恶意压缩包

攻击者“需要查看加密军事文件”为由，发送一个 ZIP 压缩包，声称内含重要文档。压缩包包含：

* 被篡改的 `Wondershare PDFelement` 安装程序（嵌入加密 shellcode）
* 4 个正常 PDF 文档（作为诱饵）
* 一份安装说明文本

#### 3.初始执行阶段

受害者运行被篡改的 `PDFelement` 安装程序后，嵌入的加密 `shellcode` 被触发，与 C2 服务器 japanroom[.]com（一个被渗透的房地产信息服务网站）建立通信。

#### 4.第二阶段载荷投递

C2 服务器下发一个伪装成 JPG 图片的文件 1288247428101.jpg，实际为第二阶段载荷。

#### 5.最终载荷释放

JPG 文件执行后释放 RokRAT 木马。

#### 6.持久化与数据窃取

`RokRAT` 使用合法但被攻陷的 `Zoho WorkDrive` 作为 C2 服务器，支持以下高级功能：

* 屏幕截图
* 通过 cmd.exe 执行远程命令
* 收集主机信息与系统侦察
* 伪装恶意流量，绕过 360 Total Security 等安全软件检测

攻击亮点与规避技术

* 合法软件篡改：`Wondershare PDFelement` 被植入 `shellcode`
* 合法基础设施滥用：使用真实企业网站作为 C2
* 文件扩展名伪装：JPG 图片实际为恶意载荷
* 社交工程高度精准：利用“加密军事文件”这一高可信度借口
* 多平台通信转移：`Facebook → Messenger → Telegram`，降低被平台封禁风险

GSC 评估称：“这是一种高度规避的组合策略，融合了合法软件篡改、合法网站滥用以及文件扩展名伪装。”

![](https://mmbiz.qpic.cn/mmbiz_jpg/4T1PVwJicwk9fkic8ElUngzxDziaPjiblZw62QwqBKBJ1kuicIewGQianhdTuDrrdmNH5PdPj2Fb3pXf3q4e1MtW4l2m6ib95y9nKxC7gNTStJZkOU/640?wx_fmt=jpeg&from=appmsg)

### 安全启示与防御建议

1. **社交媒体层面**：不要轻易接受陌生人的 Facebook 好友请求，尤其是自称“军事”“情报”“加密文档”相关话题时，务必提高警惕。
2. **软件下载**：只从官方渠道下载 PDF 阅读器等常用工具，避免点击不明链接提供的安装包。
3. **端点防护**：部署 EDR/XDR 工具，重点监控异常进程、网络通信和文件执行行为。
4. **意识教育**：对员工进行针对性社交工程培训，强调“预设场景”（Pretexting）的危害。
5. **多因素验证**：所有社交账号开启两步验证，减少账号被冒用风险。

该恶意软件利用 `Zoho WorkDrive` 作为 C2 服务器——`Zscaler ThreatLabz` 于 2026 年 2 月在代号为 `Ruby Jumper` 的攻击活动中也详细描述了这一策略——使其能够捕获屏幕截图、通过“cmd.exe”执行远程命令、收集主机信息、执行系统侦察，并逃避一些知名安全软件等安全程序的检测，同时伪装恶意流量。

`全球安全委员会`表示：“其核心功能一直保持相对稳定，并在多次行动中反复使用。

这表明，RokRAT 较少关注改变其核心功能，而更多地关注改进其投放、执行和规避流程。”

## 学习交流群

刚加入网络安全行业的小白，可以加入学习交流群，大家一起互相学习，互相进步，不会的难题大家一起学习，一起攻克。

想要进学习交流群的师傅们，可以后台扫描二维码添加好友，我再拉你进群（Ps：防止广告进群）。想要学习工具的师傅，可以扫描进帮会，获取渗透工具合集。

![](https://mmbiz.qpic.cn/mmbiz_jpg/IkpoxULsr9dEclFnKnAAurt1AlnO1HBLiaRymULG1ibJJhXlNjMH1rd1SgQQWIyFBVTRMteWWfiby3FCWfpB7n2oA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

泷羽Sec-Norsea

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/IkpoxULsr9fbWSl52zKqe5AN711UM8IFNbS9rZLM7reGeUZs0XqdtM8X5L5mdRibicHpxmu3iaPGct9UztVKAT6AA/0?wx_fmt=png)

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