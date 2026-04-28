---
title: 新的Windows RPC漏洞允许攻击者在所有Windows版本中提升权限
url: https://mp.weixin.qq.com/s/3xuBkR0gVs9Zp7pgQSJ4Kw
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:25:47.864985
---

# 新的Windows RPC漏洞允许攻击者在所有Windows版本中提升权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnv7SpoHeBaVAGBop1rY4LZQLJ0Zia0Oic7kIs6K2hvn9iaQTfVrw7RBaCGpIo1Wed0WmJfREoyXEAt3qhVEzxtNyb4pE6RxbIgG0M/0?wx_fmt=jpeg)

# 新的Windows RPC漏洞允许攻击者在所有Windows版本中提升权限

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnvXnZ5I5ADbLbicQD1E9ia79CJ9xDEib54AbM1WtbNkvcoVsh0fvJa0UicvIg9c3pMySXCicXUbyM2gOazZugkv046GG0XYfZ5ich3Oc/640?wx_fmt=png&from=appmsg)

PhantomRPC——Windows远程过程调用（RPC）中新发现的架构漏洞，可实现本地权限提升至SYSTEM级别访问，可能影响所有Windows版本。

该研究由卡巴斯基应用安全专家Haidar Kabibo于2026年4月24日在Black Hat Asia 2026上发布，详细介绍了五种不同的利用路径，其中无一获得微软的补丁修复。

PhantomRPC并非传统的内存损坏漏洞或单一组件中的逻辑缺陷。相反，它利用了Windows RPC运行时（rpcrt4.dll）处理连接到不可用RPC服务器时的架构设计弱点。

当高权限进程尝试向离线或禁用的服务器发起RPC调用时，RPC运行时不会验证响应服务器是否合法。

这意味着，控制低权限进程（如以NT AUTHORITY\NETWORK SERVICE身份运行的进程）的攻击者可以部署一个恶意RPC服务器，模仿合法端点并拦截这些调用。

**恶意RPC服务器（卡巴斯基）**

核心滥用依赖于RpcImpersonateClient API。当特权客户端以高伪装级别连接到伪造服务器时，攻击者的服务器调用此API来接管客户端的安全上下文——直接从低权限服务账户提升至SYSTEM或Administrator。

**五种利用路径**

研究人员确定了五种具体的攻击场景：

* **gpupdate.exe强制** —— 执行gpupdate /force会触发组策略客户端服务（以SYSTEM身份运行）向TermService发起RPC调用。如果TermService被禁用，攻击者的伪造RPC服务器将拦截调用，获得SYSTEM级别访问权限。
* **Microsoft Edge启动** —— 当msedge.exe启动时，它会以高伪装级别触发对TermService的RPC调用。等待伪造端点的攻击者无需任何强制即可从Network Service提升至Administrator。
* **WDI后台服务** —— 诊断系统主机（WdiSystemHost）以SYSTEM身份运行，每5-15分钟定期轮询TermService。无需用户交互；攻击者只需等待自动调用。
* **ipconfig.exe和DHCP客户端** —— 执行ipconfig.exe会触发对DHCP客户端服务的内部RPC调用。在DHCP被禁用且伪造服务器就位的情况下，Local Service攻击者可提升至Administrator。
* **w32tm.exe和Windows时间** —— Windows时间可执行文件首先尝试连接到不存在的命名管道\PIPE\W32TIME。攻击者可以在不禁用合法W32Time服务的情况下暴露此端点，然后伪装任何运行该二进制文件的特权用户。

**微软的回应——无补丁**

该漏洞于2025年9月19日报告给微软安全响应中心（MSRC）。

微软在20天后回应，将该问题归类为中等严重性，理由是攻击需要SeImpersonatePrivilege权限——而Network Service和Local Service账户默认已拥有此权限。

卡巴斯基报告称："未分配CVE编号，且该案例在未安排修复的情况下被关闭。"

**在补丁发布前，防御者可采取以下措施：**

* 启用基于ETW的RPC监控，检测RPC\_S\_SERVER\_UNAVAILABLE错误（事件ID 1）与来自特权进程的高伪装级别相结合的情况。
* 在可行的情况下启用被禁用的服务（如TermService），使合法端点被占用而无法被劫持。
* 将SeImpersonatePrivilege权限限制为仅严格需要的进程；不要将其授予自定义或第三方应用程序。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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