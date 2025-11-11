---
title: TEE.Fail侧信道攻击可破解CPU可信执行环境机密
url: https://www.4hou.com/posts/zAZ7
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-10
fetch_date: 2025-11-11T03:12:45.438568
---

# TEE.Fail侧信道攻击可破解CPU可信执行环境机密

TEE.Fail侧信道攻击可破解CPU可信执行环境机密 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# TEE.Fail侧信道攻击可破解CPU可信执行环境机密

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12207

收藏

导语：值得注意的是，即便启用了“密文隐藏”安全选项，针对AMD SEV-SNP的攻击依然有效。

学术研究人员开发出一种名为TEE.Fail的侧信道攻击技术，能够从CPU的可信执行环境（系统中安全性极高的区域）中提取机密信息，涉及英特尔（Intel）的SGX、TDX技术以及AMD的SEV-SNP技术。

该攻击方法是针对DDR5系统的内存总线介入式攻击，人们升级无需芯片级专业知识。

可信执行环境（TEE）是主处理器内的“机密计算”硬件，用于保障敏感数据的机密性与完整性，例如身份验证和授权过程中使用的加密密钥。这一环境与操作系统相互隔离，会创建受保护的内存区域，确保代码和数据能够安全运行。

研究人员指出，由于最新几代硬件在架构设计上的权衡取舍，英特尔SGX、TDX以及AMD SEV-SNP的现代实现版本，已不再如宣传般安全。

具体而言，可信执行环境已从客户端CPU拓展至采用DDR5内存的服务器级硬件，这类硬件采用了确定性AES-XTS内存加密技术，同时为追求性能与扩展性，移除了内存完整性保护和重放保护机制。

研究人员通过实验证实，可利用这些缺陷实施密钥提取与认证伪造。TEE.Fail是首个基于DDR5的密文攻击技术，延续了此前针对DDR4内存的WireTap和BatteringRAM等攻击研究。

**一、攻击实施流程与技术细节**

该攻击需满足两个前提：一是能够物理接触目标设备，二是拥有修改内核驱动程序所需的根级权限。研究人员在技术论文中解释，他们通过将系统内存时钟降至3200 MT/s（1.6 GHz），实现了信号的可靠捕获。

![rig.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251029/1761708186575843.jpg "1761707956119718.jpg")

窥探装置（右）和目标（左）

具体操作是在DDR5内存模块（DIMM）与主板之间，接入注册内存（RDIMM）转接卡和定制的探针隔离网络。

将介入装置与逻辑分析仪连接后，攻击者可记录DDR5的命令/地址信号及数据突发传输过程，从而获取物理DRAM（动态随机存取存储器）地址的读写密文。

![analuze.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251029/1761708189147966.jpg "1761708011102399.jpg")

TEE.fail 攻击期间的 DDR5 内存总线流量

针对英特尔SGX技术，研究人员需将虚拟地址中的数据强制导入单一内存通道，以便通过介入装置进行观测。

借助英特尔向内存地址转换组件开放的物理地址接口，研究人员能够“通过系统文件系统（sysfs）向用户空间进一步开放这一解码接口”。这让他们得以获取用于确定物理地址对应内存模块位置的关键信息。

不过，SGX依赖操作系统内核进行物理内存分配，因此研究人员“修改了内核的SGX驱动程序，使其能够接收虚拟地址与物理地址对作为参数，并存储在全局内核内存中”。

研究人员创建了一个SGX enclave，对特定虚拟内存地址发起密集的读写操作。通过这一方式，他们验证了内存介入装置捕获的加密密文，是物理内存地址及其内容的确定性函数。

他们解释道：“为验证加密的确定性，我们指令飞地对其内存中的固定虚拟地址执行一系列读写操作，并通过逻辑分析仪捕获每一步后的密文读取数据。”

由于AES-XTS加密技术会使同一信息每次加密都得到相同输出，研究团队向可观测的物理地址写入已知值，建立起密文与原始值的映射关系。

![enclavereads.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20251029/1761708192115362.jpg "1761708192115362.jpg")

来自 enclave 数据三次读取的密文

随后，通过触发并记录目标加密操作，观测中间表项的加密访问过程，恢复出每个签名对应的随机数（nonce）位。

结合恢复的随机数与公开签名，即可重构私钥签名密钥，进而伪造有效的SGX/TDX认证报告（quotes），冒充合法的可信执行环境。

研究人员采用相同方法，从运行在AMD SEV-SNP保护虚拟机中的OpenSSL中提取了签名密钥。值得注意的是，即便启用了“密文隐藏”安全选项，针对AMD SEV-SNP的攻击依然有效。

**二、攻击影响：多场景安全威胁实现**

研究人员展示的攻击案例包括：

1. 在以太坊BuilderNet上伪造TDX认证报告，获取机密交易数据与密钥，实现不可检测的抢先交易；

2. 伪造英特尔和英伟达的认证信息，使在可信执行环境外运行的工作负载呈现合法状态；

3. 直接从飞地中提取ECDH私钥，恢复网络主密钥，彻底破坏数据机密性；

4. 针对Xeon服务器实施攻击，获取用于验证设备身份的配置证书密钥（PCK）。

通过TEE.Fail攻击，研究人员证实能够控制可信执行环境的运行过程，并观测特定虚拟地址。不过该攻击属于复杂攻击，需物理接触目标设备，在现实场景中实用性有限，对普通用户而言暂不构成直接威胁。

目前，研究人员已于4月向英特尔、6月向英伟达、8月向AMD通报了相关发现。三家厂商均已确认问题存在，并表示正针对机密计算威胁模型研发缓解措施与适配方案，计划在TEE.Fail技术论文公开后发布官方声明。

文章翻译自：https://www.bleepingcomputer.com/news/security/teefail-attack-breaks-confidential-computing-on-intel-amd-nvidia-cpus/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?U83WSTYc)

#### 你可能感兴趣的

* [![]()

  TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)
* [![]()

  恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)
* [![]()

  Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
* [![]()

  8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
* [![]()

  黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
* [![]()

  超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)
  2025-11-10 12:00:00
* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)
  2025-11-06 12:00:00
* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
  2025-11-05 12:00:00
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
  2025-11-05 10:37:58

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [TEE.Fail侧信道攻击可破解CPU可信执行环境机密](https://www.4hou.com/posts/zAZ7)

  胡金鱼
* [恶意 npm 包针对 Windows、Linux、macOS 植入信息窃取器](https://www.4hou.com/posts/LG4W)

  胡金鱼
* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)

  胡金鱼
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)

  胡金鱼
* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)

  胡金鱼
* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)