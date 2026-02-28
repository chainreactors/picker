---
title: 网络犯罪组织SLH以每通电话500-1000美元招募女性进行语音钓鱼
url: https://mp.weixin.qq.com/s/_9rULZOPvoQAAleqWHMztQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:53:36.097239
---

# 网络犯罪组织SLH以每通电话500-1000美元招募女性进行语音钓鱼

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX165HiaunkovvMrRpgSEX4jufBy7D18wv07dfKjREPTibEsSpqUCt7bXXUy5PW9Ejz1JmQBApDkoDX9BH3TkQRdrdoJrwua0JNJQ/0?wx_fmt=jpeg)

# 网络犯罪组织SLH以每通电话500-1000美元招募女性进行语音钓鱼

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1VH5V1qmLu0Z7aDEplFPC4LwBzk8PO8G76ZgLrzOLWcCt2bUYf5Zia2UxxHvvtibwQh6u2bBO5Uq5IqicdHRbJ7yh9RqSArkxIoU/640?wx_fmt=jpeg&from=appmsg)

##

## 臭名昭著的网络犯罪组织Scattered LAPSUS$ Hunters（SLH）正通过经济激励手段招募女性实施社会工程攻击。威胁情报公司Dataminr最新报告披露，该组织以每通电话500至1000美元的预付报酬，雇佣女性对IT服务台实施语音钓鱼（vishing）攻击，同时为攻击者提供预制话术脚本。

##

**Part01**

## ****社会工程攻击手段升级****

"SLH正通过专门招募女性实施语音钓鱼来扩充其社会工程攻击队伍，此举很可能是为了提高冒充服务台的成功率。"报告指出。这个由LAPSUS$、Scattered Spider和ShinyHunters组成的网络犯罪集团，长期采用高级社会工程技术绕过多因素认证（MFA），包括MFA提示轰炸和SIM卡劫持等手段。

**Part02**

## ****典型攻击流程剖析****

该组织的标准操作流程包括：伪装成企业员工联系服务台或呼叫中心，诱骗工作人员重置密码或安装远程监控管理（RMM）工具以获取远程访问权限。在获得初始访问后，Scattered Spider会横向移动至虚拟化环境，提权并窃取敏感企业数据。部分攻击最终会部署勒索软件。

攻击者还擅长使用Luminati、OxyLabs等合法住宅代理网络隐藏行踪，并利用Ngrok、Teleport、Pinggy等隧道工具及file.io、gofile.io等免费文件共享服务。Palo Alto Networks旗下Unit 42团队（追踪代号Muddled Libra）在本月报告中指出，该组织"极其擅长利用人类心理"，通过冒充员工尝试重置密码和MFA。

**Part03**

## ****云环境渗透技术****

网络安全公司调查发现，Scattered Spider在2025年9月的某次攻击中，通过致电IT服务台获取特权凭证后，创建并利用虚拟机进行Active Directory枚举等侦察活动，试图窃取Outlook邮箱文件和Snowflake数据库数据。Unit 42强调："该威胁组织在专注于身份盗用和社会工程的同时，还巧妙利用合法工具和现有基础设施隐藏行踪，其操作隐蔽且具有持久性。"

该组织还长期针对Microsoft Azure环境，利用Graph API获取云资源访问权限，并使用ADRecon等云枚举工具进行Active Directory侦察。

**Part04**

## ****企业防御建议****

鉴于社会工程已成为该组织主要入侵手段，企业应加强IT服务台人员培训，重点识别预制话术和专业语音伪装，实施严格身份验证流程，逐步淘汰基于短信的MFA方式，并在服务台交互后审计新用户创建或权限提升日志。Dataminr警告："此次针对性招募标志着SLH战术的精心演变，通过使用女性声音，该组织试图突破IT服务台人员常规识别模式，显著提升冒充攻击的成功率。"

**参考来源：**

SLH Offers $500–$1,000 Per Call to Recruit Women for IT Help Desk Vishing Attacks

https://thehackernews.com/2026/02/slh-offers-5001000-per-call-to-recruit.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3tSDVhn4H8MfzIKxtt4We0D52fia93Y5a2TI7y0t4j0PpiclCRBqdQCZWYrwG4B4hpaT2593sVoic8GylJKxPrgP1gyC1304Y78I/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335476&idx=1&sn=aa6cb0d69a88d29ad0c00c917bc49c3d&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX16d9YFd8C2ZLm5AxSaONt9eF8xcnfW9nhy3jyhoyrY28GWAnNeXJ0ojss2bj9w5V2asdI31nwVv2SUldtdhLfWuCE2l8fCzT8/640?wx_fmt=png&from=appmsg)

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