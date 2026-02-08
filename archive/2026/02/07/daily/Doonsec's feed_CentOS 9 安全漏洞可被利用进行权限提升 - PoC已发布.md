---
title: CentOS 9 安全漏洞可被利用进行权限提升 - PoC已发布
url: https://mp.weixin.qq.com/s/-3m3_nX_zP4OOhaL_7qHgA
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:13.205710
---

# CentOS 9 安全漏洞可被利用进行权限提升 - PoC已发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnvTNdxXCwevGel5BIRWW0xxMLZWhJ66iclzyKH9vO2nLyXzMqBy5AbhAeBUDiagZR0a0eUTI0PKMjg0y0MRxHJSG4JcnoO1sdWibE/0?wx_fmt=jpeg)

# CentOS 9 安全漏洞可被利用进行权限提升 - PoC已发布

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJntNMYeXGJmjaLibHL4OmcibRacjWiavLrX3pJ9xrK556mIuSAzEnFLvIBq0GNiaUghjYkjNIbJAHlcfyFLcJkbmdMGGHk1ceMQr3lI/640?wx_fmt=jpeg&from=appmsg)

近日，安全研究人员在CentOS 9系统中确认存在一个**关键性安全漏洞**，该漏洞允许**本地普通用户**无需任何特殊权限即可**将自身权限提升至root级别**，完全控制系统。

### 漏洞技术细节

该漏洞源于**Linux内核网络子系统**中的**释放后重用(UAF)**缺陷，具体存在于**CAKE(通用应用增强型)数据包调度程序**(`sch_cake`模块)中。此漏洞在2025年TyphoonPWN黑客竞赛中被评为**Linux类别第一名**，凸显其技术复杂性和严重性。

漏洞的核心问题在于CAKE队列规则处理数据包丢弃时的**逻辑错误**：

* **关键缺陷**：`cake_enqueue`函数在因缓冲区限制而**丢弃数据包**时，错误地向父调度程序返回`NET_XMIT_SUCCESS`(成功状态)
* **影响机制**：当HFSC(分层公平服务曲线)等类调度程序堆叠在CAKE之上时，会依赖此返回值
* **漏洞触发**：CAKE声称数据包已成功排队，HFSC保持对该类的引用，但实际数据包已被丢弃
* **最终结果**：导致**悬空指针**问题——HFSC仍认为该类处于活动状态，而实际内存已被释放

### 漏洞利用过程

根据SSD安全披露信息，已发布的**概念验证(PoC)代码**展示了完整的攻击链，攻击者可借此**完全控制系统**：

1. **KASLR绕过**：利用prefetch侧信道攻击确定内核代码的随机化位置
2. **堆喷射**：通过`sendmsg`系统调用向内核堆中注入大量"假"Qdisc对象，控制内存布局
3. **触发UAF**：使悬空指针指向攻击者控制的数据区域
4. **ROP链构建**：创建返回导向编程链劫持执行路径，覆盖`modprobe_path`变量
5. **权限提升**：以root权限执行任意脚本，完成权限提升

### 影响范围与风险评估

* **影响版本**：CentOS 9所有版本(特别是9.4及以上)
* **漏洞等级**：**CVSS评分9.3**(严重级别)
* **利用条件**：仅需**本地普通用户账户**，**无需特殊权限**
* **攻击复杂度**：中等(需要内核知识，但PoC已公开)
* **潜在影响**：攻击者可**安装后门**、**窃取敏感数据**或**完全控制系统**

值得注意的是，**该漏洞不仅影响CentOS 9**，还波及**所有使用相同内核版本的Linux发行版**，包括Ubuntu 24.04、Debian Trixie等主流系统。

### 修复与缓解措施

目前，**尚无官方补丁发布**，供应商仅表示修复工作"正在进行中"。

1. **系统加固**：

* **限制tc命令访问**：通过SELinux或AppArmor配置文件限制流量控制命令
* **禁用不必要的模块**：在`/etc/modprobe.d/`中添加配置禁止加载`sch_cake`
* **实施最小权限原则**：严格控制用户对系统命令的访问权限

1. **监控建议**：

* **监控内核日志**：关注与网络调度相关的异常事件
* **启用堆保护**：配置内核启用`CONFIG_SLAB_FREELIST_RANDOM`等保护机制
* **部署完整性检查**：使用AIDE或OSSEC监控关键系统文件变化

由于**PoC代码已公开**，攻击门槛大幅降低，强烈建议系统管理员**立即采取缓解措施**，避免系统遭受未经授权的root权限访问。同时，密切关注Linux内核安全公告，一旦官方补丁发布，应**立即应用更新**。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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