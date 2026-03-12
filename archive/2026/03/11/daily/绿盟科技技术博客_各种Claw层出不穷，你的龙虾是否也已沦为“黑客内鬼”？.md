---
title: 各种Claw层出不穷，你的龙虾是否也已沦为“黑客内鬼”？
url: https://blog.nsfocus.net/%e5%90%84%e7%a7%8dclaw%e5%b1%82%e5%87%ba%e4%b8%8d%e7%a9%b7%ef%bc%8c%e4%bd%a0%e7%9a%84%e9%be%99%e8%99%be%e6%98%af%e5%90%a6%e4%b9%9f%e5%b7%b2%e6%b2%a6%e4%b8%ba%e9%bb%91%e5%ae%a2%e5%86%85/
source: 绿盟科技技术博客
date: 2026-03-11
fetch_date: 2026-03-12T04:08:51.076562
---

# 各种Claw层出不穷，你的龙虾是否也已沦为“黑客内鬼”？

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# 各种Claw层出不穷，你的龙虾是否也已沦为“黑客内鬼”？

### 各种Claw层出不穷，你的龙虾是否也已沦为“黑客内鬼”？

[2026-03-11](https://blog.nsfocus.net/%E5%90%84%E7%A7%8Dclaw%E5%B1%82%E5%87%BA%E4%B8%8D%E7%A9%B7%EF%BC%8C%E4%BD%A0%E7%9A%84%E9%BE%99%E8%99%BE%E6%98%AF%E5%90%A6%E4%B9%9F%E5%B7%B2%E6%B2%A6%E4%B8%BA%E9%BB%91%E5%AE%A2%E5%86%85/ "各种Claw层出不穷，你的龙虾是否也已沦为“黑客内鬼”？")[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "View all posts by NSFOCUS")

阅读： 47

AI智能体工具OpenClaw的爆火，催生出一个现象级的开发者生态。截至2026年3月，与OpenClaw功能属性相同、设计逻辑相似的衍生项目已超300个，成为高效开发范式下的典型代表。

但繁荣背后，安全隐患已全面凸显。大量类OpenClaw工具为追求便捷性与自动化，舍弃基础安全设计，导致超13.5万个公网实例处于无防护的“裸奔”状态，黑客自动化扫描、接管攻击已成为现实，原本的生产力工具，正面临沦为黑客“内鬼”的风险。

###

### **一、300余项目快速迭代，创新背后暗藏安全短板**

OpenClaw带动的开源AI智能体生态呈爆发式增长，目前在claw工具社区中已有超25个活跃项目被收录，贡献者超5000人，OpenClaw新变种持续涌现。其中，中国团队的创新成果尤为突出，在嵌入式、商业模式、云端集成等方向形成引领，展现出国内在该领域的技术实力。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/表1-300x198.png)

在高效开发的导向下，类OpenClaw项目普遍采用“先上线、后安全”的模式，导致架构性安全风险突出。不同工具变种的设计逻辑，形成了功能与安全的明确权衡，四类主流应用类型均存在难以规避的剩余风险。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/表2-300x173.png)

### **二、四大核心攻击面，成为黑客操控AI工具的关键路径**

尽管各类Claw工具的代码实现存在差异，但核心逻辑架构高度相似，输入、鉴权、执行、生态四大层面，成为黑客的主要攻击突破口，直接导致工具从生产力载体沦为窃取信息、破坏系统的“内鬼”。

**1.输入层：恶意指令注入，直接劫持工具逻辑**

这是AI智能体工具的核心安全威胁。类OpenClaw工具普遍具备自动读取邮件、网页、即时通讯消息的功能，黑客可通过发送含恶意指令的内容，让工具误将其判定为高优先级执行指令，进而完成信息窃取、操作篡改等行为。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图1-借助邮件的OpenClaw间接提示词注入-300x189.png)

图-借助邮件的OpenClaw间接提示词注入

**2.鉴权层：访问控制缺失，工具实例全网暴露**

大量开发者在部署工具时，忽视基础的访问权限设置，或为调试便捷关闭权限认证、使用简易验证令牌，加之工具对本地地址的默认信任机制，导致全球超13.5万个公网实例无有效防护，黑客通过简单的扫描手段，即可直接接管工具控制台。

**3.执行层：高权限无监督，操作风险无限放大**

类OpenClaw工具被赋予较高的系统操作权限，且多以主机高权限运行，同时多数工具未设置操作监督机制，也无工具调用的二次确认流程。一旦工具被注入恶意指令，其高权限将成为黑客的“攻击利刃”，轻易实现文件篡改、系统破坏等操作。

**4.生态层：插件供应链无管控，成为投毒重灾区**

插件市场是类OpenClaw生态的最大安全变量。黑客会发布功能诱人的插件，在底层代码中隐藏恶意程序，而工具本身缺乏插件代码审计和运行时行为监控能力，恶意插件一旦被安装，即可实现长期驻留，持续窃取信息或控制设备。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图2-恶意Skills-300x183.png)

图-恶意Skills

**核心洞察：**当前类OpenClaw工具均以自然语言解析、开放式外部工具调用为核心架构，且未做物理层面的沙箱隔离，因此无法从根本上规避恶意指令注入带来的系统级接管风险。

### **三、高危漏洞集中爆发，系统性安全风险凸显**

目前社区关注的重点多为插件生态的次生风险，但OpenClaw自身的代码质量缺陷、开发范式漏洞，才是引发系统性安全问题的根源。工具普遍存在输入验证缺失、访问控制不严、资源配置不当等问题，其GitHub仓库短期积压超6700个问题，维护响应滞后，进一步放大了安全风险。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/图3-OpenClaw从星标暴涨到连续RCR漏洞披露-300x183.png)

图-OpenClaw相关部分漏洞披露时间线

已有多个高危漏洞被披露，部分已获得CVE编号，攻击影响覆盖未授权访问、任意命令执行、权限提升等多个方面，对个人及企业资产安全构成严重威胁。绿盟科技大模型风险评估工具（AI-SCAN）可进行OpenClaw相关资产风险发现。

![](https://blog.nsfocus.net/wp-content/uploads/2026/03/表3-293x300.png)

### **四、分角色安全应对策略，构建全生命周期安全防护体系**

解决类OpenClaw工具的共性安全风险，核心是构建全生命周期、系统性的安全防护与评估能力：在设计阶段**严格遵循最小权限原则**，运行阶段**引入沙箱隔离机制，强化外部输入内容的过滤与管控，**同时建立工具资产的自动发现、**持续风险评估与动态加固能力**，推动AI智能体从“高危实验品”转变为可信、可控的生产力基础设施。

**个人用户和开发者：拒绝盲目部署，做好基础安全隔离**

1.不将工具部署在存储敏感数据、高价值认证凭据的主机上，优先选择虚拟机、容器、专用云服务器等隔离环境运行；

2.定期检查已安装的本地skills和插件，及时删除来源不明、功能存疑的插件，并将工具更新至最新版本；

3.云资源管理、加密资产操作等设计系统修改的高危操作，避免通过AI工具执行。

**企业安全团队：建立全流程治理体系，强化风险管控**

1.搭建AI智能体资产发现与治理能力，实现企业内部工具的精准识别、动态监测，做到安全风险早发现、早处置；

2.工具部署时强制实施网络隔离、严格身份认证，绑定本地访问地址，禁用默认无认证模式，遵循最小权限原则，限制工具的文件、网络及系统调用权限；

3.部署专业AI安全防护设备或沙箱隔离方案，对工具的所有输入、输出内容进行实时检测与过滤，拦截恶意操作；

4.建立智能体专用审计日志体系，完整记录工具调用、API请求、敏感操作等行为，支撑事后安全溯源与合规审计。

**开源社区和项目维护者：完善安全开发流程，筑牢生态安全防线**

1.强化安全开发生命周期实践，将安全设计、代码审计与功能迭代同步推进，从源头减少安全漏洞；

2.针对插件市场建立自动化检测机制，通过静态检测、代码语义分析、沙箱分析等手段，完善插件上架审核、人工抽检、用户举报响应体系；

3.建立标准化漏洞响应流程，对安全研究人员反馈的漏洞及时评估、修复，并同步发布安全公告，提醒用户做好防护。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/%E5%85%B3%E9%94%AE%E5%9F%BA%E7%A1%80%E8%AE%BE%E6%96%BD%E5%AE%89%E5%85%A8%E7%97%9B%E7%82%B9%E5%87%B8%E6%98%BE%EF%BC%8C%E6%91%84%E5%83%8F%E5%A4%B4%E5%AE%89%E5%85%A8%E5%A6%82%E4%BD%95%E7%A0%B4%E5%B1%80/)

### Meet The Author

NSFOCUS

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)