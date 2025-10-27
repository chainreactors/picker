---
title: 从Pegasus到Predator：iOS商业间谍软件的演进
url: https://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486250&idx=1&sn=daa031ff26b9773e0177492de181ba56&chksm=fb04c842cc7341547e24e5d3ef245e093b4f4fd5e1a07df102c384f7ea5aa4c1bee9213ba60f&scene=58&subscene=0#rd
source: 天御攻防实验室
date: 2025-01-26
fetch_date: 2025-10-06T20:10:14.844443
---

# 从Pegasus到Predator：iOS商业间谍软件的演进

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hPq2VZ0zUBAdPGWnnC2jtXwkpkSCzmSERu2E9wkhBiaPFKVJM1Gd4ko2DQPX7SrA3JyBmeNnfOBTPBwiagdr3kPQ/0?wx_fmt=jpeg)

# 从Pegasus到Predator：iOS商业间谍软件的演进

原创

天御

天御攻防实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBAwZQYIRcMGdob0eTGKx525Ddp9DrwAwWLOGwL1HNIwiayA2mzhHsdiakoCUfBmN7fib078lq2yjXTMg/640?wx_fmt=other)

## 本文基于iVerify研究团队负责人在著名黑客会议38c3上演讲内容整理而成。

##

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hPq2VZ0zUBAdPGWnnC2jtXwkpkSCzmSEdT4MDtReB7EjfLVotNbPg02ObqRXRpaKSBrdWCq8icPrbFk23bmLicXA/640?wx_fmt=png&from=appmsg)

## 演讲人介绍

各位尊敬的来宾，请允许我介绍Matthias Freelingsdorf先生。他现任iVerify研究团队负责人，曾就职于德国联邦铁路，专门负责智能手机和平板电脑安全，并为T-Systems开发安全产品。他的硕士论文研究iOS漏洞利用和恶意软件检测，并在黑帽会议（Black Hat）、LabsCon等多个重要会议上发表研究成果。他是iOS恶意软件领域的权威专家。除专业工作外，他也热衷于篮球运动和桌游。

## **演讲范围界定**

本次演讲将重点关注以下内容：

* 商业间谍软件的历史演进
* 当前检测iOS商业间谍软件的手段
* 行业现状分析
* 未来发展趋势展望

需要说明的是，本次演讲不会涉及：

* StockAware、Spouseware等大众市场监控软件
* 商业间谍软件的合法性或正当性讨论
* 越狱技术

## **核心概念界定**

### 商业间谍软件定义

在本演讲中，商业间谍软件特指：

1. 企业面向国家机构提供的攻击能力
2. 用于数据窃取的间谍软件植入物
3. 通常使用零点击或一键点击漏洞链
4. 经常使用零日漏洞感染最新版本iOS设备
5. 针对个别目标实施攻击

这类软件也被称为"私营部门攻击者"或"雇佣军间谍软件"。

### **研究重要性**

关注此议题的原因：

1. 已有多起针对公民社会、新闻工作者或企业的滥用案例
2. 过去八年中，公民社会领域已披露诸多滥用事件
3. 在iOS系统上难以检测
4. 涉及新颖或有趣的漏洞利用技术
5. 虽然感染概率较低，但一旦感染将造成重大影响
6. 已有受害者在感染后遭受人身伤害的案例（如Khashoggi事件）

## **与越狱技术的区别**

### 越狱特点：

* 目的：用户自主解放设备
* 安装方式：手动
* 目标客户：终端用户
* 影响群体：用户本人
* 系统变化：显著
* 易于检测

### 商业间谍软件特点：

* 使用零日漏洞
* 采用零点击攻击
* 面向政府机构
* 针对特定目标
* 隐蔽性强
* 难以检测

## **历史案例分析**

### Pegasus第一代（2016）

* 首个被公开分析的商业间谍软件案例
* 发现源于可疑短信分析
* 使用公开越狱技术
* 系统痕迹明显，易于检测

### Pegasus第二代（2021）

* 代号"强制入侵"
* 利用iMessage作为感染载体
* 实现零点击攻击
* 增强了痕迹清理能力
* 使用特定目录进行启动

### Pegasus第三代（2022-2023）

* 改进清理机制
* 伪装为系统进程
* 采用BlastPass漏洞链

### Hermit（2022）

* 通过侧载应用感染
* 与移动运营商合作
* 使用公开和非公开漏洞
* 首个使用应用程序作为感染载体的案例

### 三角行动（Operation Triangulation）

* 使用iMessage作为感染载体
* 通过网络和取证分析发现
* 使用过时的系统进程名称（导致暴露）
* 全面的痕迹清理机制

### Predator演进

#### 第一代（2021）

* 一键点击攻击
* 基于Python开发
* 同时支持Android和iOS
* 已实现基本的痕迹清理

#### 第二代

* 完全用Objective-C重写
* 使用WebKit零点击攻击
* 增强的验证和清理步骤
* 具备关机通知响应机制

## **技术趋势分析**

### **攻击方式演进**

* 从一键点击向零点击转变
* 放弃持久性模块
* 增强清理能力
* 难以获取完整样本

### 检测指标（IOC）分析

* 崩溃日志
* 电子邮件痕迹
* 文件痕迹
* 网络痕迹
* 进程痕迹

## **检测技术现状**

### iOS应用检测能力

* 极其有限
* 仅能检查已知文件路径
* 可监控网络流量
* 无法获取完整系统信息

### MDM检测能力

* 可获取已安装应用列表
* 适合检测Hermit类型攻击
* 功能受限

### 取证分析能力

* 可通过备份获取更多信息
* 需要用户交互
* 分析耗时
* 要求专业知识

### 系统诊断（SysDiagnose）

* 可获取全面系统信息
* 需要10-15分钟执行
* 需要用户配合

## **BlastPass案例深入分析**

### 攻击链分析

* HomeKit进程崩溃（25次）
* Messages Blaster服务崩溃（35次）
* 使用PKPass文件传递
* 包含NS表达式攻击载荷

### 技术特点

* 多阶段解密机制
* 利用XPC通信
* 智能的密钥传递方案
* 复杂的反检测机制

## **未来发展趋势**

### 预期变化

1. 攻击面转移：

* 转向第三方应用
* 扩展到其他苹果设备
* 探索新的攻击载体

2. 攻击策略调整：

* 多重漏洞利用
* 目标差异化处理
* 进一步提升隐蔽性

### 2025年期望改进

1. 苹果威胁通知改进：

* 提供恶意软件详情
* 包含IOC信息
* 明确攻击状态
* 提供时间框架

2. 检测能力提升：

* 增加端点安全框架
* 提供进程监控能力
* 改进取证支持

3. 行业协作：

* 加强防御方协作
* 共享恶意软件样本
* 统一分析技术
* 共享IOC信息

4. 研究需求：

* 商业间谍软件影响范围研究
* iOS攻击面研究
* 新设备取证技术研究
* 系统数据库文档完善

## **安全建议**

### 个人防护

* 启用锁定模式
* 定期重启设备
* 保持系统更新
* 定期进行取证分析

### 机构防护

* 建立设备管理制度
* 实施持续监控
* 加强用户培训
* 保持威胁意识

---

参考资料：

https://media.ccc.de/v/38c3-from-pegasus-to-predator-the-evolution-of-commercial-spyware-on-ios

**推荐阅读**

**闲谈**

1. [中国网络安全行业出了什么问题？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485457&idx=1&sn=d45cc35242cdc83e98b124531ea7c093&chksm=fb04cb79cc73426f21801f35912b626bf515dc2b9d85b3da578f8087d0a2960396ef1e6347bc&scene=21#wechat_redirect)
2. [国内威胁情报行业的五大“悲哀”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484999&idx=1&sn=485863f4e66a62f55aa69334c787e6f3&chksm=fb04c52fcc734c3919fc28c61a9b13488b89efe4c1ba5cb16f8f00f0c6e996c7f1df47984463&scene=21#wechat_redirect)
3. [对威胁情报行业现状的反思](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486063&idx=1&sn=11e005a726ced95e872e2ce7fb228ba2&chksm=fb04c907cc734011310b2cc58a4a6f1ac764ece04c7d7ca9f3e93f0849f92c5e891b32e4c58f&scene=21#wechat_redirect)
4. [安全产品的终局](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484846&idx=1&sn=35bab89f917f5043919e40893268d576&chksm=fb04c6c6cc734fd05c0423dc971a0578eb8b951ef1764be0a99e2bdd1c26b736d64cf61b6d77&scene=21#wechat_redirect)
5. [老板，安全不是成本部门！！！](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485908&idx=1&sn=b6cff013a1e9a9599bdde63ce56ecec0&chksm=fb04cabccc7343aac55b3c43020c855bade147461fece597f730bc0460e65c5610dd0f5d988b&scene=21#wechat_redirect)

**威胁情报**

1.[威胁情报 - 最危险的网络安全工作](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485331&idx=1&sn=0857185a1bc7ed04c2d1edc60cb93a34&chksm=fb04c4fbcc734dede0fd243984c30250ff7859f68a265b1a278ac72a5761ac0ccaf0038537ec&scene=21#wechat_redirect)
2.[威胁情报专栏 | 威胁情报这十年（前传）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484880&idx=1&sn=c2b5730f2a7011959096526ff775c8ac&chksm=fb04c6b8cc734fae9f6d2e0693cecd5fd594a01694d8e38bd95926cb88a0f627c3d5b2f36ea2&scene=21#wechat_redirect)
3.[网络威胁情报的未来](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485003&idx=1&sn=76253d23e51dde8dbf4d675b79ab43cf&chksm=fb04c523cc734c352490ca37f55f1c3a989d55807298cb308aa3c126e24816d6fda11a8766f1&scene=21#wechat_redirect)
4.[情报内生？| 利用威胁情报平台落地网空杀伤链的七种方法](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485042&idx=1&sn=afd1212b585f30bccdece8471fadd31d&chksm=fb04c51acc734c0c9fd0d1d388b7672defbe5ce17a10af58d3a5d336ba21fa21398b4ad860e2&scene=21#wechat_redirect)
5.[威胁情报专栏 | 特别策划 - 网空杀伤链](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484709&idx=1&sn=649a27516ca01baab49ce750e3502cc3&chksm=fb04c64dcc734f5becd252686228f6c3c2bd00bff52041e9dae6fde2008e1a43057989b9d16f&scene=21#wechat_redirect)
6.[以色列情报机构是如何远程引爆黎巴嫩传呼机的？](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486027&idx=1&sn=7d9215cbf71327fccda006c6c29938a3&chksm=fb04c923cc734035c661d4e3b93ad1e631fd55ee5a4ba7cd855c7e37bc513ca071860fdfb9b9&scene=21#wechat_redirect)
7.[对抗零日漏洞的十年（2014～2024）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486036&idx=1&sn=52131d932e8fe4f24db3d7bdf41625a0&chksm=fb04c93ccc73402a24144d8262153a73bc18c2098109a9885d2413dba9a33af83f8d664bc317&scene=21#wechat_redirect)
8.[零日漏洞市场现状（2024）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247486041&idx=1&sn=1c9dc7508ba7d09c8f7c88f3018bae1d&chksm=fb04c931cc734027d17b83f774416085b6c492306ccf49f76cb99fa1fbf8b03c7ff6af23a781&scene=21#wechat_redirect)

**APT**

1. [XZ计划中的后门手法 - “NOBUS”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485524&idx=1&sn=aa2b7b0d57b250e5cc101e5dcbebbca6&chksm=fb04cb3ccc73422a9fe22937b801eceb205ceaf8bf3b76a92143d575d55e5fd2eef5adfacb36&scene=21#wechat_redirect)
2. [十个常见的归因偏见（上）](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247484868&idx=1&sn=3d65e81115c967b165fa16021a211967&chksm=fb04c6accc734fba7c760fd14caaaf9a2d7991acc2557ee340e772ccbb805b30f1a46c793e8a&scene=21#wechat_redirect)
3. [抓APT的一点故事](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485237&idx=1&sn=9152fcb5f5b1f884e6da97ba9b04f69a&chksm=fb04c45dcc734d4bd8fbede2ae93dc52feeaaa11e215a3240bca32f3d43444a2c909e01a2814&scene=21#wechat_redirect)
4. [揭秘三角行动（Operation Triangulation）一](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485278&idx=1&sn=9def52d0d9063e86acb16533be2a52e8&chksm=fb04c436cc734d20b8c67348f7db21fa10921ad3826b37c713e847b73972f50de82b6c1f1e6b&scene=21#wechat_redirect)
5. [闲话APT报告生产与消费](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485325&idx=1&sn=d0219cfe811afe5e8fc8729c603de2bc&chksm=fb04c4e5cc734df3a8ad433a992172c1a9a0f236fd69550c72eb499e1202d23b81f32b379259&scene=21#wechat_redirect)
6. [一名TAO黑客的网络安全之旅](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485451&idx=1&sn=5f794deaaccf45e7d81958eba82cd556&chksm=fb04cb63cc73427538546f24b1be7cd78375a9017498efb3fd2da46de5c38c0d4599c2e01100&scene=21#wechat_redirect)
7. [NSA TAO负责人警告私营部门不要搞“黑回去”](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485250&idx=1&sn=a35def8b58f86f8a149e335f3df3a1c9&chksm=fb04c42acc734d3cdfd1e8f2ae852731c3569533ab8fa83bd0126b788ea20673a2f912cdf011&scene=21#wechat_redirect)
8. [我们为什么没有抓到高端APT领导者的荷兰AIVD](http://mp.weixin.qq.com/s?__biz=MzU0MzgyMzM2Nw==&mid=2247485961&idx=1&s...