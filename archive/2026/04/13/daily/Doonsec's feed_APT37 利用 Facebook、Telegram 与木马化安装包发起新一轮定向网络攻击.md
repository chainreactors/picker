---
title: APT37 利用 Facebook、Telegram 与木马化安装包发起新一轮定向网络攻击
url: https://mp.weixin.qq.com/s/TihNB_o3a7aH-IEFpWDTAQ
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:41:36.812490
---

# APT37 利用 Facebook、Telegram 与木马化安装包发起新一轮定向网络攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7PtNF8sIYJOqBq4tpk4UBIib4erxSBWfpHRU87r35FibkYM3e10rTHkic4gkLV6fC7Mnpga8rQRyaFc6lLtwQ9RyKacoZMNPEpibOM/0?wx_fmt=jpeg)

# APT37 利用 Facebook、Telegram 与木马化安装包发起新一轮定向网络攻击

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

APT37正在发动一项新的定向入侵活动，利用Facebook、Telegram以及被篡改的Wondershare PDFelement安装程序，悄悄获取访问权限并窃取敏感数据，这些数据很可能来自国防相关目标。

该行动显示了APT37社会工程和规避技术的持续演进，要求基于行为的EDR能够识别进程注入、滥用云存储和图像伪装的负载，超越简单签名。

运营商先发送好友请求，随后通过一对一的Messenger聊天建立信任，使用定制话题，最终将对话转移到Telegram等“更安全”的渠道。

该行为者以分享加密军事武器文件为借口，声称需要专用的PDF浏览器，并敦促受害者安装该浏览器以打开文件。

Genians安全中心分析了APT37利用两个自称来自平壤和平泰的Facebook账户，在袭击前识别和筛查特定目标的活动。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7NGyux1DmibKf05icVicZ6Syesl0Pxl4R2icaglmce6EUrKpWyYCCSmucCADgQuT3hufDsnPx1XOqaeMxECQtoiaPzBYnOAmdZtFxXw/640?wx_fmt=png&from=appmsg)

该恶意包裹以密码保护的ZIP（例如“m.zip”）通过Telegram发送，内含假PDF查看器执行文件、多个军事主题诱饵PDF以及一个韩语“说明”文本文件，使用朝鲜风格拼写如“콤퓨터”、“프로그람”和“화일”，支持朝鲜的关联。

## **PDFelement安装程序被篡改**

这个“专用查看器”实际上是一个经过精心修改的Wondershare PDFelement安装程序，名为“Wondershare\_PDFelement\_Installer（PDF\_Security）.exe”，模仿了正规文件名，但加上了“（PDF\_Security）”作为伪装。

与官方安装程序不同，被篡改的文件缺少有效的Wondershare数字签名，表明被修改，导致缺乏签名成为防守方的关键IOC。

在内部，演员保持了正常安装程序的行为，仅通过在 .text 部分末尾的代码洞中插入大约 2 KB 的 shellcode 并优先重定向执行，从而改变了 PE 的入口点。

shellcode 在运行时构建通往“%windir%\System32\dism.exe”的路径，通过基于 PEB 的哈希例程解析 API。它在启动 dism.exe 时以悬挂状态启动，然后通过 VirtualAllocEx、WriteProcessMemory 和 CreateRemoteThread 向内存注入解密的有效载荷。

完成恶意程序后，控制会回到原始入口点，从而执行合法的 PDF 元素设置，掩盖了入侵的行为。

![](https://mmbiz.qpic.cn/mmbiz_png/BicXBAdicJy7PheHq5SHlzf2sUcP2u37P2XrTo8FJlSfIMeAedWibh5szt2FiaLohaibx2VaUd0YmIWDmVxnWiago5wuRCticuLAZkUpSKfJgib9JJI/640?wx_fmt=png&from=appmsg)

壳码包含一个51字节的XOR加密blob，运行时在合法日本房地产信息服务（具体为首尔分支路径）上解码为C2 URL，结尾为“1288247428101.jpg”。

虽然它使用.jpg扩展并看似请求图像，但响应被视为异或加密的第二阶段有效载荷，而非媒体内容。

第一次异或通过使用前导字节作为密钥解密下载数据，并验证结果是否以标准x86函数序言字节（55 8B）开始，若验证失败则循环重试。

威胁行为者保留了被篡改安装器的主要功能，仅修改了入口点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7OtYPQsmJXibNTY0wIOJHhAibz9K2sM8eic1BaQ1DoxpAYKzCDKc04kAbfN7kD5ggCf0fXZCIU9no9CppVqtoXWPRao1o0Xab72icc/640?wx_fmt=png&from=appmsg)

第二层解密使用4字节密钥重建去除MZ/PE签名的PE映像，映射并纯内存运行，完成一个完全无文件的多阶段执行链。

## **类似RokRAT的后门**

最终有效载荷与APT37的RokRAT后门系列非常相似，后者具备系统侦察、命令执行和截图功能，且有滥用合法云服务用于C2的历史。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BicXBAdicJy7NVDf43zTqeNda3d4qPRziaxBdTQtv2v8Itqpy5CRHkYVhFiaiczNARyYH44SDVtG59J5rgQfkTuHB4FAPC115g2shtHu4cbgicnJ4/640?wx_fmt=png&from=appmsg)

该恶意软件收集主机信息、运行进程、磁盘布局、公共IP和地理位置，并窃取截图、文档和手机音频录音，扩展名包括DOC、XLS、PPT、PDF、HWP、TXT、M4A和AMR。

命令与控制通过 Zoho WorkDrive 的 OAuth2 API 实现，多个客户端 ID、客户端秘密和刷新令牌被硬编码，以融入正常业务流量，类似于此前报道的 APT37 活动，使用 Zoho 作为隐形 C2。

收集到的数据在上传前会用AES-256-CBC加密，植入体还会检测特定安全产品，可以投放假冒的“OfficeUpdate.exe”更新器，并循环使用多个用户代理字符串以进一步混淆网络行为。

该活动的手法与APT37从HWP和LNK交付的RokRAT向云备份、无文件植入物和多阶段异或加密加载器的演变相符，包括多次滥用Zoho WorkDrive用于C2。

同一天创建的Facebook账号、韩语标记、基础设施重叠，以及历史上使用Zoho账号和朝鲜式诱饵，进一步支持了与朝鲜相关集群的归属。

鉴于大量使用被篡改的安装程序、进程注入签名二进制文件、云C2以及伪装成图像的有效载荷，仅签名控制不足;组织必须部署基于行为的EDR，并强力地围绕父子进程链遥测、未签名的“更新”二进制文件、可疑dism.exe活动。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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