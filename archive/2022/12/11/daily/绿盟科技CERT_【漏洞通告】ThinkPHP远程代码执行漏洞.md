---
title: 【漏洞通告】ThinkPHP远程代码执行漏洞
url: https://mp.weixin.qq.com/s?__biz=Mzk0MjE3ODkxNg==&mid=2247487885&idx=1&sn=58d14a5a85ba194e4fbde5cebd91b1b2&chksm=c2c64686f5b1cf90623db665cdddf6b71670130a643c839a3c4e33c5cf4787c05079dee43cd2&scene=58&subscene=0#rd
source: 绿盟科技CERT
date: 2022-12-11
fetch_date: 2025-10-04T01:12:36.469011
---

# 【漏洞通告】ThinkPHP远程代码执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecrVU6ox0nspKAyCqgATIeWgOUEEO1ZWAJTyYSlZcMfoa4w6qkW8cPdEo9S5BOG8Emy7Q5Bp4UTluw/0?wx_fmt=jpeg)

# 【漏洞通告】ThinkPHP远程代码执行漏洞

NS-CERT

绿盟科技CERT

**通告编号:NS-2022-0030**

2022-12-10

|  |  |
| --- | --- |
| **TA****G：** | **ThinkPHP、远程代码执行** |
| **漏洞危害：** | **攻击者利用此漏洞可实现任意执行命令** |
| **版本：** | **1.0** |

**1**

**漏洞概述**

近日，绿盟科技CERT监测到网上公开披露了Thinkphp远程代码执行漏洞的利用细节。由于Thinkphp 程序中存在传入参数检查缺陷，当Thinkphp开启了多语言功能，未经身份验证的攻击者可以通过 get、header、cookie 等位置传入参数，实现目录穿越及文件包含，最终通过 pearcmd 文件包含trick实现远程代码执行。漏洞细节已公开，请相关用户尽快采取措施进行防护。

ThinkPHP 是一个免费开源的，快速、简单的面向对象的轻量级PHP开发框架 。

绿盟科技CERT已成功复现此漏洞：

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecrVU6ox0nspKAyCqgATIeWgmRJfSOq5V4Nv8zsU2ReGXX0rKLu1s3ibfVVueyI4z7HVGytUyzvPLOg/640?wx_fmt=png)

参考链接：

https://blog.thinkphp.cn/3078655

**SEE MORE →**

**2****影响范围**

**受影响版本：**

* v6.0.0 <= ThinkPHP <= v6.0.13
* v5.1.0 <= ThinkPHP <= v5.1.41
* v5.0.0 <= ThinkPHP <= v5.0.24

**不受影响版本：**

* ThinkPHP >= v6.0.14
* ThinkPHP = v5.1.42

**3****漏洞排查**

**步骤1**、执行以下命令，查看ThinkPHP的版本信息：

|  |
| --- |
| php think version |

![](https://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecrVU6ox0nspKAyCqgATIeWgGocmfMSLkiaN63mYfzJnN9zCbGiaiaKebw82eeLmCWgjZjqDVew2uv8sQ/640?wx_fmt=png)

若在影响范围内，则产品可能受该漏洞影响。

**步骤2**、查看ThinkPHP是否开启多语言功能

①Thinkphp6：

查看app/middleware.php中以下内容是否有注释，若无注释，则ThinkPHP开启了多语言功能，产品受此漏洞影响

|  |
| --- |
| \think\middleware\LoadLangPack::class |

②Thinkphp5：

查看app/middleware.php，若存在以下内容，则ThinkPHP开启了多语言功能，产品受此漏洞影响

|  |
| --- |
| 'lang\_switch\_on'=> true |

**4****漏洞防护**

**4.1 官方升级**

目前官方已发布安全版本修复此漏洞，建议受影响的用户及时升级防护：

https://github.com/top-think/framework/releases/tag/v6.0.14

**4.2 临时防护措施**

若无法进行升级，用户可以通过以下方式进行规避防护。

1、Thinkphp6：

查看app/middleware.php，将以下内容进行注释

|  |
| --- |
| \think\middleware\LoadLangPack::class |

2、Thinkphp5：

查看app/middleware.php，将'lang\_switch\_on'=> true改为以下内容

|  |
| --- |
| 'lang\_switch\_on'=>false |

    3、重启Thinkphp

**END**

![](https://mmbiz.qpic.cn/mmbiz_png/qR4ORTNELImFwJM2rh6GKbnrurdFA28jJ8chUPyC1U6aW3jhenqEiaXkmeGVmfOnvAJy8j3My901JQ7emHaicYzA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**声明**

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qR4ORTNELImFwJM2rh6GKbnrurdFA28jib7icfic0lJJHh3eLRpIXiaia08KqOSEibBsz64vlOH9aqicu3lmjccEeAFWQ/640?wx_fmt=jpeg)

**绿盟科技CERT**∣微信公众号

![](https://mmbiz.qpic.cn/mmbiz_jpg/VvfsuOanecrVU6ox0nspKAyCqgATIeWgzFmycfC7sic1V6vkHPtODZfz4T3LfOH1Id38QDDxIEXiazed4emev3cg/640?wx_fmt=jpeg "绿盟科技CERT公众号.jpg")

![](https://mmbiz.qpic.cn/mmbiz/Hu8hctxHqSW0nSJn8p8OHVEQwHicSwTibFJMBE650AxdzfISoeY8woe2QsgCINIBrccBOOUft2HuU0GsNQWibSG7g/640?wx_fmt=png)

长按识别二维码，关注网络安全威胁信息

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoicvhEy80SjuIeB8aHInNEXXaMDSZpHyeWx4Aer9yLmHDvnjTFT44XkicnIAuF0AiaicLA6ZKFiaXCCicg/0?wx_fmt=png)

绿盟科技CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VvfsuOanecoicvhEy80SjuIeB8aHInNEXXaMDSZpHyeWx4Aer9yLmHDvnjTFT44XkicnIAuF0AiaicLA6ZKFiaXCCicg/0?wx_fmt=png)

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