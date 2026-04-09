---
title: 新型GPUBreach攻击通过GDDR6位翻转实现CPU权限完全提权
url: https://mp.weixin.qq.com/s/11mtcYtJXd-I9yqW7zeuxg
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:28:26.197522
---

# 新型GPUBreach攻击通过GDDR6位翻转实现CPU权限完全提权

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1MjWlbvpLZpzMjiaQ0SCrXgRMT5GZTVMDqgBVeRHMBYPICsRibagKaFCVXJYyspBNA8iaa0eIyFF5BQicvr6ch4Abmiauym7CbKfkg/0?wx_fmt=jpeg)

# 新型GPUBreach攻击通过GDDR6位翻转实现CPU权限完全提权

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX13egFicSOUolXhhq9NmBC5pRxj4ChiaqprTEhtWXbEdAyjicUz2ZYzUhBxxSflkjsLKhTrjA8jBWmZMO9s0aj47DsmaVOBnZALf8/640?wx_fmt=jpeg&from=appmsg)

##

## 最新学术研究发现了针对高性能图形处理器（GPU）的多重RowHammer攻击手段，攻击者可利用这些漏洞提升权限，在某些情况下甚至能完全控制主机系统。这些攻击技术被命名为GPUBreach、GDDRHammer和GeForge。

##

**Part01**

## ****攻击技术演进****

GPUBreach比先前的GPUHammer更进一步，首次证实GPU内存中的RowHammer位翻转不仅能导致数据损坏，还能实现权限提升并最终导致系统完全沦陷。多伦多大学助理教授、该研究合著者Gururaj Saileshwar在LinkedIn上表示："通过GDDR6位翻转破坏GPU页表，非特权进程可获得GPU内存的任意读写权限，进而利用NVIDIA驱动中的内存安全漏洞实现CPU权限完全提权——最终获得root shell。"

**Part02**

## ****突破IOMMU防护机制****

GPUBreach的显著特点在于无需禁用输入输出内存管理单元（IOMMU）即可实施攻击。IOMMU是通过防止直接内存访问（DMA）攻击和隔离各外设内存空间来保障内存安全的关键硬件组件。Saileshwar补充道："GPUBreach证明现有防护并不足够：通过破坏IOMMU允许缓冲区内的可信驱动状态，我们触发了内核级越界写入——完全绕过IOMMU保护而无需将其禁用。这对云AI基础设施、多租户GPU部署和HPC环境具有严重影响。"

**Part03**

## ****RowHammer攻击原理****

RowHammer是一种长期存在的动态随机存取存储器（DRAM）可靠性问题，通过对内存行的重复访问（即"锤击"）会产生电磁干扰，导致相邻行的位翻转（0变1或1变0）。这种现象破坏了现代操作系统和沙箱的基础隔离保障。DRAM制造商已实施纠错码（ECC）和目标行刷新（TRR）等硬件级缓解措施来应对此类攻击。

**Part04**

## ****GPU攻击技术发展****

2025年7月多伦多大学研究人员发表的研究将这种威胁扩展到了GPU领域。被称为GPUHammer的攻击是首个针对采用GDDR6显存的NVIDIA GPU的实际RowHammer攻击，它采用多线程并行锤击等技术克服了GPU架构特性带来的挑战（这些特性曾使GPU对位翻转免疫）。GPUHammer攻击成功会导致机器学习模型准确率下降，在GPU上运行时降幅可达80%。

GPUBreach则进一步通过RowHammer破坏GPU页表实现权限提升，获得GPU内存的任意读写能力。更重要的是，该攻击还被发现能从NVIDIA cuPQC泄露加密密钥、实施模型准确率降级攻击，以及在IOMMU启用状态下实现CPU权限提升。研究人员解释："受攻击的GPU通过DMA（利用页表项中的aperture位）访问IOMMU允许的CPU内存区域（GPU驱动自身的缓冲区）。通过破坏这些可信驱动状态，攻击触发了NVIDIA内核驱动中的内存安全漏洞，获得任意内核写入能力，最终用于生成root shell。"

**Part05**

## ****相关攻击技术对比****

GPUBreach的披露与另外两项研究——GDDRHammer和GeForge——同时出现，这些技术都围绕GDDR6 RowHammer导致的GPU页表破坏，并促进GPU端权限提升。与GPUBreach类似，这两种技术都能实现对CPU内存的任意读写访问。

GPUBreach的独特之处在于还能实现完整的CPU权限提升，使其成为更强大的攻击手段。特别是GeForge需要禁用IOMMU才能生效，而GDDRHammer通过修改GPU页表项的aperture字段，使非特权CUDA内核能够读写主机CPU的全部内存。两项GPU内存攻击技术的研发团队表示："主要区别在于GDDRHammer利用末级页表（PT），而GeForge利用末级页目录（PD0）。但两者都能实现劫持GPU页表转换以获取GPU和主机内存读写权限的相同目标。"

**Part06**

## ****缓解措施局限性****

目前应对这些攻击的临时缓解措施是在GPU上启用ECC。但值得注意的是，ECCploit和ECC.fail等RowHammer攻击已被证实能突破这种防护。研究人员警告："如果攻击模式引发超过两个位翻转（在DDR4和DDR5系统上已被证实可行），现有ECC无法纠正这些错误，甚至可能导致静默数据损坏。因此ECC并非对抗GPUBreach的万全之策。在目前不支持ECC的台式机或笔记本GPU上，据我们所知尚无已知的缓解方案。"

**参考来源：**

New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips

https://thehackernews.com/2026/04/new-gpubreach-attack-enables-full-cpu.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0BoYQFaEKibEe5x5vA7Nt2y5GrK420ck8h2br3pAshqL3C2gBcBzibxicXsGkMtOdWbOAsfgfRfuaftcw8pQJTdwE0YtUQicJKavA/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651336774&idx=1&sn=408127059513eb158f86aa2cfc845a5b&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

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