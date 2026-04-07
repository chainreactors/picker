---
title: 微软披露攻击者正通过利用HTTP cookie来触发执行、传递指令并激活恶意功能
url: https://mp.weixin.qq.com/s/wG3XptvW8BkQP996vHrMcA
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:17.685925
---

# 微软披露攻击者正通过利用HTTP cookie来触发执行、传递指令并激活恶意功能

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX203X77lz5YxxxozOAWWxMIwHkHtyibZSr2SIniaWemQZfiarL9RXuyicoHz3LFLnFOgGJzlOEBe4Eniclj7NVTWdDPsQOcEOjdqSSU/0?wx_fmt=jpeg)

# 微软披露攻击者正通过利用HTTP cookie来触发执行、传递指令并激活恶意功能

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

##

微软Defender安全研究团队发现，攻击者正越来越多地利用HTTP cookie作为Linux服务器上PHP WebShell的控制通道，以实现远程代码执行。微软表示："这些WebShell不再通过URL参数或请求体暴露命令执行，而是依赖攻击者提供的cookie值来触发执行、传递指令并激活恶意功能。"

##

**Part01**

## ****隐蔽性增强的攻击手法****

该方法通过仅在特定cookie值出现时激活WebShell逻辑，使恶意代码在正常应用执行期间保持休眠状态，从而显著提升隐蔽性。微软指出，该行为可延伸至Web请求、计划任务及可信后台工作进程。攻击手法利用$\_COOKIE超全局变量在运行时获取cookie值的特性，无需额外解析即可处理攻击者输入。由于cookie混入正常Web流量中，该技术几乎不会触发任何告警。

**Part02**

## ****三种典型实现方式****

cookie控制型执行模型存在多种变体：

* 多层混淆加载器：PHP加载器在解析结构化cookie输入前执行多层混淆和运行时检查，最终执行编码的二级有效载荷
* 模块化重构脚本：PHP脚本分割结构化cookie数据以重构文件处理和解码函数等操作组件，有条件地将二级有效载荷写入磁盘并执行）
* **单标记触发器：PHP脚本使用单个cookie值作为标记，触发包括执行输入内容和文件上传在内的攻击者控制操作**

**Part03**

## ****自修复持久化机制****

至少存在一起案例显示，攻击者通过有效凭证或已知漏洞利用获得Linux托管环境的初始访问权限后，设置cron任务定期调用shell例程来执行混淆的PHP加载器。这种"自修复"架构使得即使清理措施删除了加载器，计划任务仍能反复重建，形成可靠的持久化远程代码执行通道。PHP加载器部署后，在正常流量中保持静默，仅在收到含特定cookie值的HTTP请求时激活。

微软补充道："将执行控制转移到cookie中，可使WebShell隐匿于正常流量，仅在有意交互时激活。通过cron重建实现持久化，与cookie门控激活分离，攻击者有效降低了操作噪音，并减少了常规应用日志中的可观测指标。"所有变体的共同点在于使用混淆技术隐藏敏感功能，并通过基于cookie的门控机制触发恶意行为，同时最小化交互痕迹。

**Part04**

## ****防御建议****

##

微软提出以下防护措施：

* 对托管控制面板、SSH访问和管理界面实施多因素认证
* **监控异常登录活动**
* **限制shell解释器执行**
* 审计Web服务器上的cron任务和计划作业
* **检查Web目录中的可疑文件创建**
* **限制托管控制面板的shell功能**

微软总结称："攻击者通过cookie复用成熟的WebShell技术，将控制逻辑转移到cookie中，可规避传统检测和日志监控。其并非依赖复杂漏洞利用链，而是利用环境中已有的合法执行路径（包括Web服务器进程、控制面板组件和cron基础设施）来部署和维护恶意代码。"

**参考来源：**

Microsoft Details Cookie-Controlled PHP Web Shells Persisting via Cron on Linux Servers

https://thehackernews.com/2026/04/microsoft-details-cookie-controlled-php.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1df9O3S7TcqYQ5TtfibKYusLhstH06qHkXsM712er2kqnjI8bykhu6xWMFStgejUxm8xOIKU6ibAmY2cojOAEcd3IawxVWR9UcM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651336627&idx=1&sn=980bb90fbcbc3a4df630ccd700eefbcf&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

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