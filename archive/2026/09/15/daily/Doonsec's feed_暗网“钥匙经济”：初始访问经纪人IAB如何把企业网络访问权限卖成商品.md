---
title: 暗网“钥匙经济”：初始访问经纪人IAB如何把企业网络访问权限卖成商品
url: https://mp.weixin.qq.com/s/MizRp9lmyZhvDEHKqyDbMw
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:02:05.812353
---

# 暗网“钥匙经济”：初始访问经纪人IAB如何把企业网络访问权限卖成商品

# 暗网“钥匙经济”：初始访问经纪人IAB如何把企业网络访问权限卖成商品

夜组OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

初始访问经纪人IAB的工作是网络犯罪中一门分工明确的生意。

以下文章来源于夜组ATO
，作者NightTeam

![](https://wx.qlogo.cn/mmhead/wzJhLVPsrd1WXxicg7oFeBUcp42pjRCZI9NRusxQ60gP2qLGL4icrrQIr6NyRb44B4hCbrfVB9VII/0)

**夜组ATO**
.

全面监控网络空间初始访问权限和账户接管威胁情报（Account Takeover Intelligence），实时预警安全风险，保护您的数字资产免受攻击。DarkCTI 威胁情报平台：dark.libaisec.com

网络犯罪早已不是单打独斗。在暗网论坛上，一批被称为**初始访问经纪人（Initial Access Brokers，IAB）**的人，专门把企业网络的“入门钥匙”做成商品出售：VPN 账号、域用户、RDP 会话，有时还打包管理员权限。买家可能是技术一般、跨不过第一道门的团伙，也可能是能力很强、只想省掉侦察和突破时间的专业攻击者。本质只有一句：**网络犯罪是一门分工明确的生意。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/U272mo6c5zjtuPQqv4eRSkglAQmkxNQRCyGSVicUMG59KibTGb6PzY3zBAASWuO7HYM0kzgEIiaZVmlG3DBmzVvWvwLZ8pFZJPKjxtadeYUEa0/640?wx_fmt=webp&from=appmsg)

Rapid7 在 2025 年 8 月发布的《Access Brokers Report》，梳理了 Exploit、XSS、BreachForums 三大论坛在 2024 年 7 月 1 日至 12 月 31 日的交易帖，把这门生意的结构摊开：卖的不只是“能登进去”，很多时候已经是**深度失陷后的成品。**

## 一、“初始访问”往往并不初始

报告最刺眼的数字是：**71.4% 的交易不只卖一种访问向量，还附带特权；其中近 10% 是多种向量和权限的捆绑包。** 也就是说，买家接手时，重活往往已经做完——域内立足、提权、多条通道备份，都可以写进商品描述。Rapid7 首席科学家 Raj Samani 的判断很直白：IAB 并不满足于摸到一扇门就走，他们会在网里转一圈，再把“能用、好用、耐用”的访问卖出去。对防守方而言，问题不再是“有没有暴露”，而是**能否在入侵升级之前把信号抓住。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U272mo6c5zgem3FDBWjYJLUt8FqbdicWeoB2yK7Vicz57bNny4J45iakt06GNqKfKlEuGD5VXNnYsv9VBtZAbMNwpgVYvQBAib1ibdCu66WQ3RuU/640?wx_fmt=webp&from=appmsg)

这带来一种双重侵害：企业先被经纪人踩点、驻留，再被买家二次利用。更糟的是，两边的非法访问，很多时候都没被现有安全方案及时发现。经纪人离场前自己顺走了什么，通常也无从核实。

## 二、最畅销的三把钥匙：VPN、域用户、RDP

半年样本里，最常见的初始访问向量（IAV）高度集中：

| 访问类型 | 占比 | 典型短板 |
| --- | --- | --- |
| VPN | 23.5% | MFA 缺失或形同虚设 |
| 域用户（Domain User） | 19.9% | 权限过大、密码复用 |
| RDP | 16.7% | 公网暴露、会话无人盯 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/U272mo6c5zjSG2D9KxBFp7SlgbrpWyASgC3F6AdbuJUW3aGpxd7XeNomdzIQBZiaJkyjiadmGlykVibdNlxF7cXxicOIA1LpCH2oGMJbEoFDZRI/640?wx_fmt=webp&from=appmsg)

这三类也正是IAB事件响应里反复撞上的薄弱点。近四分之三的挂牌提供多种向量可选，约一成直接卖组合包——商品形态已经接近“入侵套件”，而不是一张孤零零的账号。

定价并不神秘。均价大约 **2700 美元**，近 **40% 落在 500–1000 美元**。门槛低，意味着买家池更大：不必是国家级团队，也能买到进企业网的第一脚。价格大致跟目标营收挂钩，广告里也可能注水；奇怪的是，MSP 等供应链节点并未明显溢价——经纪人与买家更盯最终目标，第三方只是跳板，还要再花功夫，市场就不愿多付钱。

受害者身份几乎无法从帖子里稳定还原。小国、行业极窄、营收数字很扎眼的公司偶尔能对上号，大多数广告故意模糊，执法预警和企业自查都很难对号入座。

## 三、论坛会关，生意会迁

XSS 在研究窗口之后被打掉，写作时仍未稳定回归；BreachForums 几起几落（含 2025 年 5 月前后的重建叙事）；Exploit 则更像长寿的老市场。头部卖家会换马甲、换场子。英国籍嫌疑人 **IntelBroker** 一度以 BreachForums 为主要货架，甚至短暂控场，后于 2025 年 2 月在法国被捕，美国检方指控于同年 6 月公开。执法能打断品牌、动摇信任，却很难一次性掐断需求。

新冒出来的“XSS 继承者”“BreachForums 新站”往往被圈内人怀疑是钓鱼或执法控场。信任下降本身就是一种打击：交易摩擦变大，货不对板、卷款、渗透的风险上升。但这不等于市场消失，只是从集中广场改成更散、更谨慎的柜台。

## 四、对企业意味着什么

IAB 把攻击链拆成可交易模块：**突破外包、利用内化、变现专业化。** 防守如果还按“单一黑客从外往里打”来建模，就会漏掉“钥匙已经在货架上”这一环。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U272mo6c5zhv0F5gCAs4aPM3ma7cjv48R4BZMibptPeEtYTUjwShl33nlutwTVOibPo5pAQKKkkKgOJErHstGibHtBqwDg4d8fUXA9HPTq2jxo/640?wx_fmt=webp&from=appmsg)

可落地的优先级并不花哨：

1. **把 MFA 真正打到 VPN、RDP 和关键域账号上**——这是市场上出货最多的三类货。
2. **把暴露管理与检测响应当成一件事**：异常登录、新会话、权限跃迁，要和资产、身份、威胁情报在同一条工作流里对上，而不是各看各的告警。
3. **红队专门打“被卖掉的那种入口”**：废弃账号、默认口令、对公网敞开的 RDP、没有会话审计的远程通道。
4. **默认假设：一旦出现在货架上，企业已被折损两次**——需要按已失陷去查驻留与横向，而不是只修那一扇被挂牌的门。

## 五、结语

暗网访问经济把企业网络变成标价商品：平均两三千美元，常常不到一千，就能买到带特权的“初始”访问。论坛会被端掉，经纪人会被抓，货架却会换地方重新摆上。对企业来说，最贵的不是那把被卖掉的钥匙，而是钥匙易手之后、告警仍沉默的那段时间。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U272mo6c5ziaJdcV6SlPdjrmiabBoTvKS8vtm0dxOBfY6UBpAJhoYMSDqI515oZ5fM53grk5tqwKZfjD5tYtc1oA5QYCjSkqmH9dBYemtKXUQ/640?wx_fmt=webp&from=appmsg)

把身份认证做硬、把暴露面收干净、把情报嵌进检测，并不能消灭地下市场，但可以让“卖得出去的访问”变少、变贵、变容易露馅。这才是和这门生意对打时，防守方还能抓住的杠杆。

## ATO账户接管情报系统

以上威胁事件由ATO情报情报系统实时监测发现，订阅会员即可查看威胁情报详情。

![dark.libaisec.com](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U272mo6c5zgGXh5QjBH4yKcicOjGicE4rcbkk5aAMsiaXgzicW3FkCRyLmFI5l9iaBBMvuKHiaBAHhID74LpWHaOEXEic1Q1WmDuN8pE8M3sZmS28g/640?wx_fmt=webp&from=appmsg)

dark.libaisec.com

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A1AjQiarwFHPJibeWbc1nhED6yPPhcfplNAzMjXJx106p9J3HaRZUNyBAhECfklMPvyOsReia0qaVV8A/0?wx_fmt=png)

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