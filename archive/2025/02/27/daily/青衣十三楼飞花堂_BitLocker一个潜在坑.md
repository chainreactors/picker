---
title: BitLocker一个潜在坑
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247488010&idx=1&sn=ed68f50343b7b4a3717e932d187b1149&chksm=fab2d135cdc55823726c00e686cf35bee8ad78969e25d9a7b266a31460d7333dba8c849230ea&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2025-02-27
fetch_date: 2025-10-06T20:36:26.833228
---

# BitLocker一个潜在坑

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPMTpAV6d4EWic2cWf3qxiaiaufg4J3MtRVldcVCFOPhMA9b5585YT4Ra3V0a9UFxAEf2hSth0wcEO9aw/0?wx_fmt=jpeg)

# BitLocker一个潜在坑

原创

clan

青衣十三楼飞花堂

2025-02-20

clan最近说了件他自己碰上的事。

他的系统是Win11的某个版本。因为其他原因，临时改了BIOS/UEFI中Secure Boot相关配置，后来回滚设置。重启Win11时，提示输入BitLocker恢复密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPMTpAV6d4EWic2cWf3qxiaiaufGSpSG3Z6VEIrBIHSicVSyB8ia7FyM0UxjoJ3Xfw8BLPEtJoibmiaRibcanA/640?wx_fmt=jpeg&from=appmsg)

若是保存生效后立即回滚BIOS/UEFI设置仍触发BitLocker恢复密钥，就很坑了。万幸，他主动启用BitLocker时曾备份密钥到微软云端，靠此抢救成功。有TPM的BitLocker密钥备份应该强制，微软对此事的风险提示不够强。

他说的这个现象我未实际遇上或验证过，但我想起另一件事。之前有朋友遭遇蓝屏死机，自己上网乱找解决方案，其中有涉及调整BIOS/UEFI设置；他按那些扯淡方案操作后，触发BitLocker恢复密钥。接着，他回滚BIOS/UEFI设置，仍提示BitLocker恢复密钥，无法状态改出。交到我手上，几番挣扎，回天无力。由于不在第一现场，无法精确还原过程，如今看到clan的遭遇，不排除同一原因。

写在此处，提个醒，这种事，不怕一万怕万一。若BitLocker启用中，手动备份密钥是王道。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

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