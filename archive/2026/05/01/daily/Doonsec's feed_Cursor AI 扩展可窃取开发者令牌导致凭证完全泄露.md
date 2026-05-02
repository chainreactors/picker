---
title: Cursor AI 扩展可窃取开发者令牌导致凭证完全泄露
url: https://mp.weixin.qq.com/s/7pQrZyQLPcs-9T5PIhna0g
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:55:56.269924
---

# Cursor AI 扩展可窃取开发者令牌导致凭证完全泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1Tswn0Dxpytic7547WrCmr46uhh4jlojj5E8icf3TUicg3iaD6MIqQ0fRf3qfaQgAUicVePHFpm3guvabk5N0VtgUDib60KGSTPPusQ/0?wx_fmt=jpeg)

# Cursor AI 扩展可窃取开发者令牌导致凭证完全泄露

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0domqiaJS9TzaumjahMjLLKVpaiaibiaMLRpiaPsE98oV3AhWgfics6tWIS95aSLdCdReSyu3CUibfalOSf4XnOpWcPUwfePSfYMMaQI/640?wx_fmt=png&from=appmsg)

##

广泛使用的 AI 编程环境 Cursor 曝出高危访问控制漏洞（CVSS 8.2）。安全公司 LayerX 发现，该漏洞允许任何已安装的扩展秘密获取开发者的 API 密钥和会话令牌，导致凭证完全泄露，且整个过程不会触发任何警报，也无需用户交互。

##

**Part01**

## ****漏洞技术细节****

与大多数将敏感信息存储在操作系统受保护密钥链中的安全应用不同，Cursor 将这些凭证保存在未加密的本地 SQLite 数据库中，路径为：~/Library/Application Support/Cursor/User/globalStorage/state.vscdb。

由于 Cursor 未在扩展与数据库之间设置任何访问控制边界，任何已安装的扩展都可以读取该文件。攻击过程无需特殊权限，恶意扩展即可轻松提取数据库中的明文数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3njUKygVLGarzJoLiazDsPiawD2cUM8TbsLxoffdL0aWgwibuBMnMMiaMLneSicS5PicBTRJC62wQgFo7amGXvtiaqoIpcXdRV4mSh0o/640?wx_fmt=jpeg&from=appmsg)

典型攻击场景包含以下步骤：

* 攻击者发布一个看似正常的扩展，例如主题或效率工具。
* 开发者安装该扩展时，不会收到任何关于凭证访问权限的警告。
* 恶意扩展在后台静默查询 SQLite 数据库，获取 API 密钥和会话令牌。
* 窃取的数据被悄无声息地发送至攻击者控制的远程服务器。

**Part02**

## ****潜在危害****

由于许多开发者在 Cursor 中使用第三方 AI 服务，该漏洞可能造成以下严重后果：

* 会话令牌和后端服务访问权限完全暴露
* 关联的 OpenAI、Google 或 Anthropic 等 AI 账户遭到入侵
* 攻击者滥用被盗 API 密钥，导致巨额财务损失
* 私人数据、历史聊天记录及敏感代码元数据遭到未授权访问

**Part03**

## ****厂商响应与现状****

LayerX 于 2026 年 2 月 1 日向 Cursor 报告了该问题。Cursor 安全团队在 2 月 5 日确认了报告，但辩称：扩展与用户处于相同的本地信任边界，任何具有文件系统访问权限的本地应用都可能读取这些数据。

截至 2026 年 4 月 28 日，该漏洞仍未修复。厂商坚持认为，用户应自行确保只安装可信扩展。

安全专家强烈建议 Cursor 在扩展之间建立严格的隔离边界，并将敏感凭证迁移至加密的系统级存储，例如 Windows 凭证管理器或 macOS 钥匙串。在结构性修复发布之前，开发者应严格审计已安装的扩展，避免从市场下载未经验证的工具。

**参考来源：**

Cursor AI Extension Access Developer Tokens Leads to Full Credential Compromise

https://cybersecuritynews.com/cursor-ai-extension-access-developer-tokens/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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