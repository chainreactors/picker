---
title: 攻防演练中的快速打点思路小结
url: https://mp.weixin.qq.com/s/an4MjarYJI7eZIBuVntD8Q
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:42.901574
---

# 攻防演练中的快速打点思路小结

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XOPdGZ2MYOfwMciaXbSPeOGGbOc6ib0bC0h0enrEI7fg6u6mn7UfMMoXviaz5ScvicaHNr5wehkicqh1L39iaU2JasFg/0?wx_fmt=jpeg)

# 攻防演练中的快速打点思路小结

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于潇湘信安
，作者3had0w

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

**一、快速确定目标资产**

**1. 通过企业信息扩展资产范围**

* 使用**企查查、天眼查**等平台查询目标企业的子公司、母公司、关联公司及备案信息，获取域名、IP地址等关键资产线索。
* 利用**ICP备案查询**（如工具`ICP-Checker`）提取主域名和IP，生成FOFA等搜索引擎的查询语法（例如 `domain="xxx.com"`）。

**2. 多源资产测绘**

使用空间测绘平台（如 **FOFA、Hunter、360 Quake、Shodan**）通过以下语法批量获取资产：

```
domain="目标域名"ip="目标IP段"cert="证书特征"
```

工具推荐：`fofa_viewer`、`Tscan`、`Eeyes`（快速整理C段资产）。

**3. 自动化资产收集工具**

* 工具如 **dddd、jws-cli、OneForAll** 可自动实现子域名爆破、CDN识别、端口扫描、Web指纹识别，并整合多源数据去重。

**二、信息收集深度策略**

**1. 子域名与C段挖掘**

* 通过云悉、Sublist3r等工具爆破子域名，结合FOFA查询C段资产，发现旁站和隐藏服务。
* 利用DNS域传送漏洞、SSL证书反查等技术扩大资产范围。

**2. 端口与服务扫描**

* 使用 **Masscan、Nmap** 进行全端口扫描，结合 **Goby** 进行端口指纹识别和漏洞初步探测。
* 重点关注敏感端口（如6379 Redis、7001 WebLogic、445 SMB等）。

**3. 敏感信息泄露挖掘**

* 搜索Github、网盘、公开文档中的代码、配置文件和账号密码（如VPN默认口令）。
* 使用Google Hacking语法：

```
site:目标域名 intext:密码 | 默认口令 | 后台
```

**三、指纹识别与目标筛选**

**1. Web指纹识别**

工具：**EHole、TideFinger、Wappalyzer、Goby** 识别CMS、中间件、框架（如Shiro、Fastjson、OA系统）。

手动特征检查：

* HTTP头信息（Server、X-Powered-By）
* 根据特定文件（如 `favicon.ico`、`robots.txt`）的MD5值
* 报错页面内容（如Spring框架的默认错误页）

2、高危资产优先级

优先攻击以下系统：

* **GitLab公开项目（查看config、resources目录的敏感配置）**
* **Nacos/Jenkins/Nexus（默认口令或未授权访问）**
* **OA系统、VPN入口（弱口令爆破）**

利用工具如 **TscanPlus** 自动标记高价值目标（如存在反序列化漏洞的组件）。

**四、快速打点技巧**

**1. 漏洞利用优先级**

* 已知漏洞快速利用：使用Nuclei、POCbomber等工具批量检测Shiro、Fastjson、Log4j等通用漏洞。
* 弱口令爆破：针对后台登录口、数据库服务（如MySQL、Redis）、管理平台（如Nacos/nacos）进行爆破。

**2. 迂回攻击策略**

* 若正面防御严密，转向供应链攻击或边缘资产（如子公司、云上资产）。
* 利用云资产接管工具（如cloudTools）获取AK/SK，控制云服务器、存储桶等资源。

**3. 权限获取与维持**

* 获取Shell后，立即进行内网信息收集（如NetBIOS探测、ARP扫描）和横向移动。
* 使用CS、MSF等工具建立持久化通道，部署隐蔽后门（如内存马）。

**关键工具清单**

| 阶段 | 推荐工具 |
| --- | --- |
| 资产  收集 | FOFA/Hunter、OneForAll、Sublist3r、Eeyes |
| 端口  扫描 | Masscan、Nmap、Goby |
| 指纹  识别 | EHole、TideFinger、Wappalyzer、Goby |
| 漏洞  利用 | Nuclei、POCbomber、MSF、ShiroAttack |
| 弱口令爆破 | Hydra、Medusa、自定义字典 |

**总结**

攻防演练中快速打点的核心是 **“广度收集+精准筛选”，可**大致**分为以下3个阶段（仅供参考！）**：

* 1. 通过多源测绘和自动化工具最大化资产覆盖；
* 2. 利用指纹识别和优先级规则锁定高危目标；
* 3. 结合已知漏洞和弱口令进行快速突破。

**关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1) 还在等什么？赶紧点击下方名片开始学习吧 ![](https://mmbiz.qpic.cn/mmbiz_png/XOPdGZ2MYOeSsicAgIUNHtMib9a69NOWXw1A7mgRqqiat1SycQ0b6e5mBqC0pVJ3oicrQnCTh4gqMGiaKUPicTsUc4Tw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**下面是一则内部学习圈广告😜**

**别着急退，看完的师傅们有福了/doge**

欢迎师傅们加入内部网络安全学习圈子。圈子提供三大板块的内容：

**1**

**网络安全0→1学习路径**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1. 完整的「30+周安全学习任务路线图」公开，每周任务明确，清晰的学习重点和目标，从入门到进阶，由浅入深，循序渐进；
2. 学习内容涵盖：

* 常见的Web漏洞原理与利用
* 业务逻辑漏洞挖掘
* SRC实战技巧
* WAF绕过、代码审计、免杀钓鱼
* 内网渗透

  （Linux&Windows）提权与权限维持
* 隧道代理、域渗透、云安全、AI安全

3. 每周发布学习任务+参考资料+建议，学员可自主学习+实战练习；

**2**

**SRC漏洞专项挖掘**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

1. SRC漏洞知识库持续更新；
2. SRC挖掘技巧、分析方法、视频教程打包；
3. 分享优质挖矿案例，降低上手门槛，教你赚赏金。

**3**

**常态化内容更新**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

日常分享优质学习资源与攻防渗透技巧，包括但不限于：

1. 红队/蓝队安全攻防、免杀、钓鱼技巧、攻防渗透tips；
2. 学习路线推荐，教程、方法、技巧tips打包分享，实战视频、工具、手册一应俱全；
3. 根据网络安全初中级学习者水平，精选最有用的内容，不让你在信息洪流中迷路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYnqBadHPfYribO0Eh7AO6sZtibP7icnEL1CIv2ibPnlUibbBzpK1lImaQsiawxpEKD4wOE3B9tBMll0HBg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=81)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzD6B7ialvhZB0XJtGrrSiawmjIhv4ZRW4gTvdhQ1MkSTNvv530EOqSfKBQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDJKQUZRFgUp7micv32kZwQClN4Nrwjs2M136dAhEJzmbia2bZ17c7jRicw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDnJkibQvVicDW74QWJvoiaWOnsrGbwibCJWEkToaicK45yPzIlvD24jickxWA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDQL6MIsF3Yqiczbczx67Z76BjgaXGGn8anlibtj82icib29ZyuuP3N7s9gw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaj5Sgo33WiaHyVjXhiaDxpy2Ub3j8RH9oHDdjmiauN7IHrEh4eQHbZYgYw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=50)

此前的一下学习记录：

![图片](https://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuavfHUHVEFOGPwgcIyxvs5JeINcQEBnZT1hY0K4Pw7ya9o9gUkcFgaItIRibaMVQuXrhsthgdXELGQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=84)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYHyEqA6pDb8VLMp8HsIicKjibbR1viclLspl5Yne6f4QnlkOiao0R4iasZ71DOILPUe0XSzqOKuDdPPfw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=85)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaacJIuOWXhuibQcZiavltCSw4Uce8HJjKUHgQwKLmUyicQ16W3RibjnXgzw6ibRXYSxKeC4XebucKp1lA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=86)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYHyEqA6pDb8VLMp8HsIicKjTg4aY5w0eR7nPUKJ9qNEk5Y0COUibDSvmPKiaMVBo8Nrqgex2Gs0h9xA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=87)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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