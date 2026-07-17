---
title: 密评高风险判定指引系列（二）：物理和环境安全与网络和通信安全高风险判定
url: https://mp.weixin.qq.com/s/ifEMkQ4W62a6AXOPqGQBvw
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:57:27.498097
---

# 密评高风险判定指引系列（二）：物理和环境安全与网络和通信安全高风险判定

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dOibzgvR2iaibplCglTwia2LA9Jaaibkk6yvicD9n056ePuo9XFOXFgVLRGZCTlDzdStAQosicmdXiayicibN9GlGNEMEqibibZy5zibE30XicPtwCwtaHjQM/0?wx_fmt=jpeg)

# 密评高风险判定指引系列（二）：物理和环境安全与网络和通信安全高风险判定

北京路劲科技有限公司

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**密评高风险判定指引系列（二）：物理和环境安全与网络和通信安全高风险判定**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaibr5oLibmUzk418Ks6QLKVB9BGxN3EIwBF5Q7rhTEScQ3nNYFfVfQZobpObdD9LduUOBoLZHx3Q1UKD8y10DmQkAEjgRh8VjSW5Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaibrB1W3g6GgwQbfpXYb1UUrHKgBcS8lpnGvFtor3uU2hqcgIreUiczQial1tiblr76Xic3tTncJf3PMQiaa1AdceVqQX1GIh9GQKP984/640?wx_fmt=png&from=appmsg)

上一期我们讲了通用要求，本期聚焦物理和环境安全与网络和通信安全两大层面。机房门禁没做密码鉴别是高风险？通信数据明文传输是高风险？一文说清！

![](https://mmbiz.qpic.cn/mmbiz_png/dOibzgvR2iaibrDRcVPXXQ7qysLJr2pZ6S03eqSUAtTnysXiaiaRy77JrxK9iaHwmphfJRuZJ4yGZibgfrPwlR99kTgGic2GxkzVhFYCYxK7llbRH0M/640?wx_fmt=png&from=appmsg)

**01**｜**物理和环境安全高风险判定**

1

**身份鉴别-重要区域物理访问**

**指标要求：** 采用密码技术进行物理访问身份鉴别，保证重要区域进入人员身份的真实性。

**适用范围：** 第二级及以上级别信息系统

**三大高风险问题：**

|  |  |  |
| --- | --- | --- |
| 序号 | 安全问题 | 通俗理解 |
| 1 | 存在第5章通用要求中的安全问题 | 算法/技术/产品本身就有问题 |
| 2 | 未采用密码技术对进入重要区域人员进行身份鉴别 | 门禁只是刷卡，没有动态口令、MAC或数字签名等密码机制 |
| 3 | 身份鉴别的密码技术实现机制不正确或无效 | 虽然用了密码技术，但配置/实现有问题，形同虚设 |

**可能的缓解措施：**

1. ✅ \*\*生物识别技术\*\*（如指纹、人脸）进行身份鉴别

2. ✅ \*\*专人值守 + 登记 + 视频监控\*\*实时监控

⚠️ **注意：** 这里的缓解措施可以**酌情降低风险等级**，但不能完全消除风险！

**风险评价：**

• 若未采用密码技术但用了生物识别 → 可酌情降低风险等级

• 若未采用密码技术但有专人值守+视频监控 → 可酌情降低风险等级

**聚力同行  勇往直前**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaibpZEanCNubhSvKkAaCXY0Bh825VacGUuDyR3byemBjsR5mWXiaMXeuPW1SIKeJs8awjMexLosFELLJeblc8Hs7yYehpcv2oMl3A/640?wx_fmt=png&from=appmsg)

**02**｜**网络和通信安全高风险判定**

1

**身份鉴别-通信实体**

**指标要求：** 采用密码技术对通信实体进行身份鉴别（三级）/双向身份鉴别（四级）。

**适用范围：** 第三级及以上级别信息系统

**四大高风险问题：**

|  |  |  |
| --- | --- | --- |
| 序号 | 安全问题 | 关键点 |
| 1 | 存在第5章通用要求中的安全问题 | 基础要求不满足 |
| 2 | 未采用密码技术对通信实体进行身份鉴别 | 没有MAC机制或数字签名 |
| 3 | 身份鉴别的实现机制不正确或无效 | 配了但没用 |
| 4 | 采用的密码产品未获商用密码认证证书 | 没"商密牌 |

**缓解措施：无**

**风险评价：高风险。**

2

**通信过程中重要数据的机密性**

**指标要求：** 采用密码技术保证通信过程中重要数据的机密性。

**适用范围：** 第三级及以上级别信息系统

**四大高风险问题：** 同上结构，核心在于：

• ❌ 未对通信中的重要数据进行加密

• ❌ 加密机制不正确或无效

• ❌ 密码产品未认证

**可能的缓解措施：**

• ✅ 在"应用和数据安全"层面对所有重要数据传输进行符合要求的密码保护

• ✅ 加密后的数据流能够覆盖网络通信信道

💡 **场景举例：** 如果网络层没有加密通信，但应用层对传输数据做了加密且覆盖全信道，可酌情降低风险等级。

**风险评价：** 存在上述问题但应用层做了加密覆盖 → 可酌情降级。

3

**安全接入认证**

**指标要求：** 采用密码技术对外部接入内部网络的设备进行接入认证。

**适用范围：** 第四级信息系统（最高级别要求）

**四大高风险问题：**

1. 存在第5章通用要求问题

2. 未对外部设备进行密码接入认证

3. 接入认证机制不正确或无效

4. 密码产品未认证

**缓解措施：无**

**风险评价：高风险。**

**聚力同行  勇往直前**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dOibzgvR2iaibrozibULic5XBcq3DNAhVe3t9L9icibgZYoWpX1E65pr6Hsgic3fibkibiaZK5qflOpoxgO6kliaHqdzC4oHtJVVXf4KdQCGRoY2Z2afX70/640?wx_fmt=png&from=appmsg)

**03**｜**关键知识对比表**

|  |  |  |  |
| --- | --- | --- | --- |
| 层面 | 适用级别 | 核心要求 | 是否有缓解措施 |
| 物理环境-身份鉴别 | 二级及以上 | 密码技术鉴别进入人员 | ✅ 有 |
| 网络通信-身份鉴别 | 三级及以上 | 通信实体双向鉴别 | ❌ 无 |
| 网络通信-数据机密性 | 三级及以上 | 传输数据加密 | ✅ 有 |
| 网络通信-安全接入 | 四级 | 外部设备接入认证 | ❌ 无 |

**聚力同行  勇往直前**

![](https://mmbiz.qpic.cn/mmbiz_png/dOibzgvR2iaibqh6ic9wNibo1pZQOqHq1oiaQ30OTx3lTMBzPHrhdnSm1SeHkkKFQ2e3oPoEJ5bicLiaqhkiamJ9sE15fs38MBPQmP4DjVj4RCZqYBKM/640?wx_fmt=png&from=appmsg)

**04**｜**本章小结**

1. \*\*物理安全\*\*是第二级就开始要关注的门槛，别以为只有三级以上才需要

2. \*\*网络通信安全\*\*是三级以上系统的"必考题"，身份鉴别和数据加密缺一不可

3. 注意区分\*\*哪些有缓解措施、哪些没有\*\*—没有缓解措施的问题就是"死线"，必须满足

**聚力同行  勇往直前**

**关注路劲科技，关注网络安全！**

**END**

关于我们：

北京路劲科技有限公司(Beijing Lujin Technology Co. , Ltd.)成立于2019年1月4日，是一家提供全面系统集成与信息安全解决方案的专业IT技术服务公司。公司秉承“为网络安全保驾护航”的企业愿景及“提升国家整体安全”的使命，依据风险评估模型和等级保护标准，采用大数据等技术手段，开展网络安全相关业务。公司致力于为各个行业的业务信息化提供软件和通用解决方案、系统架构，系统管理和数据安全服务、以及IT咨询规划、系统集成与系统服务等专业化服务。公司立足北京，走向全国，始终坚持“换位、细节、感恩”的核心价值观，以“共赢、共享、共成长”的经营理念为出发点，集合了一批敢于创新、充满活力、热衷于为IT行业服务的优秀人才，致力于成为您身边的网络安全专家。

关注路劲科技，关注网络安全！

公司：北京路劲科技有限公司

地址：北京市昌平区南邵镇双营西路78号院2号楼5层504

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NtJr88ib7G289lzeU7zcuibiaE16ia3QnZNFaLUhC4G67CuiaOqicnfj2D8icshWLysP9N9UAx3n0rI3N70CltBPP1SXA/0?wx_fmt=png)

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