---
title: Axios证实遭入侵源自“社会工程学”欺骗
url: https://mp.weixin.qq.com/s/fYrL78fCuA0edA4V05xzrg
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:52.028352
---

# Axios证实遭入侵源自“社会工程学”欺骗

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX35icQPu8biafM9CXeGSYMde5Caceeex73ibHgNfibCYOYjRYgSun3McgrsreYckBVuoRMpzp0AIOoic8uXTSlN26H1IUwIwVgKiczPU/0?wx_fmt=jpeg)

# Axios证实遭入侵源自“社会工程学”欺骗

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3ib3TjJXwrjfyf3UXA7EzuWGzCInnmZRmWSicscCz41zzjRcSrDl9M7UrhwZnXgLw1wvokj9cFdhH0OEkb1xvIhsMUaWDwvSe8E/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****恶意包植入远程访问木马****

2026年3月31日，两个恶意版本的流行JavaScript HTTP库Axios被短暂发布到npm仓库。这两个版本均包含隐藏依赖项，可在macOS、Windows和Linux系统上安装远程访问木马（RAT）。此次攻击并未利用Axios代码本身的漏洞，而是瞄准了更难防御的目标——维护该库的开发人员所持有的信任权限。这一事件暴露出开源供应链中"人为环节"的极度脆弱性。

攻击者针对Axios首席维护者Jason Saayman实施了精心策划的社会工程攻击。他们伪装成某知名企业的代表，以商务合作为由建立联系。为增强可信度，攻击者克隆了该公司身份信息，搭建了逼真的Slack工作区，并安排了多次伪装会议。在取得Saayman信任后，攻击者诱骗其安装可获取设备完全控制权的程序。

**Part02**

## ****供应链攻击波及数千项目****

攻击者随后窃取活跃浏览器会话和cookie，悄无声息地劫持了Saayman的npm和GitHub凭证。Socket.dev研究人员在恶意包发布后迅速识别并分析了攻击全貌。由于npm的传递依赖机制，除直接使用Axios的用户外，数千个隐式引用Axios的下游软件包同样受到影响，实际攻击范围远超表面所见，成为近年来最具隐蔽性的大规模供应链攻击事件。

值得注意的是，即便采用双重认证和基于OIDC的发布机制等强安全控制措施，也无法阻止此类攻击。攻击者直接通过Saayman被入侵的设备，使用其有效会话进行操作——从npm的视角看，所有行为均显示为合法操作。Saayman事后证实，攻击者的访问权限"完全不受现有防护措施影响"，因为现有发布流程无法检测维护者从自有设备发起的恶意行为。

**Part03**

## ****关键基础设施的维护困境****

Axios作为JavaScript生态中下载量最大的包之一，被广泛应用于生产环境应用、构建系统、CLI工具和基础架构层。多数团队并非主动选用它，而是通过深层依赖链间接引入。然而这个全球关键项目仅由少数个人维护，缺乏机构级安全资源或专职支持团队。这种困境在此次事件中暴露无遗。

事件发生后，Saayman立即采取行动：清除所有设备数据、重置全部凭证，并开始采用硬件安全密钥及改进的发布流程。他在GitHub公开评论中承认自己沦为"知名社会工程攻击"的受害者，坦承攻击者已完全控制其工作环境。其应对措施既体现了事件的严重性，也展现出重建安全体系的决心。

![Axios维护者事后恢复措施（来源：Socket.dev）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0RmOzEs5Cw0w4hwBsklFKPMv1EZ75JK8KhMd7swDpibrzEj67mqQWaa8mjrjiayRf5ZVm8kSeB7IW1FyZJUawiaicy2HkEC5kBibno/640?wx_fmt=jpeg&from=appmsg)

**Part04**

## ****长期威胁与防御建议****

此次攻击模式与著名的xz utils后门事件如出一辙——攻击者投入大量时间建立可信度后再实施攻击。这种长期布局的策略使纯技术防御手段失效，因为突破口是人而非软件。当控制维护者等同于控制其下的整个依赖树时，攻击者会不惜代价获取这种权限。

使用Axios的组织应立即审计依赖树，检查是否包含受感染的1.8.2和1.8.3版本并及时更新。开发者应采用依赖扫描工具监控异常版本变更。开源维护者（特别是管理流行软件包的人员）应当：部署硬件安全密钥、限制会话暴露时间，并将自有设备视为高价值基础设施进行防护。

**参考来源：**

Axios Maintainer Confirms The npm Compromise Was via a Targeted Social Engineering Attack

https://cybersecuritynews.com/axios-maintainer-confirms-the-npm-compromise/

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