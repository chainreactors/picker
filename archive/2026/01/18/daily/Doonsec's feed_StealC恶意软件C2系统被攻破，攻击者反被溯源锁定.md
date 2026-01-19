---
title: StealC恶意软件C2系统被攻破，攻击者反被溯源锁定
url: https://mp.weixin.qq.com/s/xeyymrjI9c5ujL0R2aU20w
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:36:40.980789
---

# StealC恶意软件C2系统被攻破，攻击者反被溯源锁定

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38daAluefq6JJ5FMSbia6MVReghzfHhyetjOkrt1Hpa4yw9elIaHKM0YlxTia1lbuwb96zguYbyWUiaw/0?wx_fmt=jpeg)

# StealC恶意软件C2系统被攻破，攻击者反被溯源锁定

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38daAluefq6JJ5FMSbia6MVRNvnB4448JEfvaHfvdhqfOBu1H03tjhW9unHZxsEqAiaOwEu2zOnKYAQ/640?wx_fmt=png&from=appmsg)

近日，CyberArk Labs的安全研究人员成功利用StealC恶意软件基础设施中的漏洞，攻入攻击者C2系统，并通过其被盗的会话凭证反向锁定威胁主体身份。此次入侵暴露了以凭证窃取为核心的犯罪运营团队同样存在严重安全缺陷。

**Part01**

## ****跨站脚本漏洞击穿防御****

自2023年初以"恶意软件即服务"（Malware-as-a-Service, MaaS）模式运作的StealC信息窃取木马，因代码泄露暴露出其Web控制面板存在跨站脚本攻击漏洞。网络安全公司CyberArk Labs利用该漏洞，从专为窃取凭证设计的基础设施中获取系统指纹、监控活跃会话并截获身份认证凭证。

讽刺的是，这些专精于Cookie窃取的运营者竟未部署基础防护措施——例如httpOnly标志——导致其自身凭证因XSS攻击被劫持。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38daAluefq6JJ5FMSbia6MVRNCKgw42TgrNDSGibbMTP8JvZHYsRib3uELdRfYqPKV6VQ2TmoNRkkC8w/640?wx_fmt=png&from=appmsg)

**Part02**

## ******单人操控5000台感染设备******

通过对控制面板的渗透，研究人员追踪到代号"**YouTubeTA**"（YouTube威胁主体）的运营者。其日志显示：累计控制超过**5,000台感染设备**，窃取**39万组密码**及**3,000万条Cookie**。木马截取的受害者搜索记录表明，YouTubeTA通过入侵拥有成熟订阅基础的合法YouTube频道，诱导用户搜索Adobe Photoshop和After Effects的盗版软件，借此分发StealC。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38daAluefq6JJ5FMSbia6MVRVfpkDRxu0sqicpiakwSm8gwt0Ks3C75u1yF1Yr5QEho7hkuZmOH33icCA/640?wx_fmt=png&from=appmsg)

**Part03**

## ******精准锁定攻击者身份******

控制面板配置数据揭示其蓄意劫持内容创作者账户：系统特别标记了studio.youtube.com的凭证字段，意图扩大恶意软件分发网络。硬件指纹分析证实YouTubeTA为单人操作，所有会话均来自搭载**Apple M3芯片**的设备。其语言偏好设置为英语与俄语，时区数据指向东欧地区。

关键失误发生在该运营者短暂关闭VPN防护时，真实IP地址暴露——经溯源确认归属乌克兰网络服务商TRK Cable TV。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38daAluefq6JJ5FMSbia6MVR61bJGTibFv9bModvCSE4IwlXQeFiaM5ia9xBACCRONzZdT6Wg6yHoiag6A/640?wx_fmt=png&from=appmsg)

**参考来源：**

Researchers Gain Access to StealC Malware Command-and-Control Systems

https://cybersecuritynews.com/researchers-gain-access-to-stealc-malware-command-and-control-systems/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icIRaltrZVKxHyDE18c4IRVw3NnALmIwxqOb5mKhbDhBIRRU7MLD2zkbPgnNPvhyk5ibAhhLAavEIA/640?wx_fmt=png&from=appmsg)

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