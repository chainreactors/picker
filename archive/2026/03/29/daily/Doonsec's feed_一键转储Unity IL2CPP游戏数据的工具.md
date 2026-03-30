---
title: 一键转储Unity IL2CPP游戏数据的工具
url: https://mp.weixin.qq.com/s/UzQuzN08ahtQQDIksC4LAw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:43:45.501082
---

# 一键转储Unity IL2CPP游戏数据的工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Wxusn17ibicDaeuniboSV5AanAECr0PJArh61glaCEv8l7S7mO6ianc7VnCcdaPGmPcosAYyEqv0aiaSZAnrYwwib17k7oYIAKt31PFrDSxyGD50I/0?wx_fmt=jpeg)

# 一键转储Unity IL2CPP游戏数据的工具

原创

CCMS
CCMS

哆啦安全

![]()

在小说阅读器中沉浸阅读

[游戏漏洞挖掘课程](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247497872&idx=3&sn=19fd397d09f1fc242daaed3d25557a10&scene=21#wechat_redirect)

[游戏反私服方案研究](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247484279&idx=3&sn=122b66ce4f5ba545ae5badc3f804fbd1&scene=21#wechat_redirect)

[手游逆向与防护(建议收藏)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247494363&idx=1&sn=6b65226777850b664e6ac643888f6bf9&scene=21#wechat_redirect)

[Unity手游无Root注入工具](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499408&idx=1&sn=5260012899e6425667e8d24a354dd9d7&scene=21#wechat_redirect)

[游戏黑灰产识别和溯源取证](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247490522&idx=1&sn=a4495f59642ff668d7d1e2a4ecf49cf5&scene=21#wechat_redirect)

[Unity Il2cpp手游逆向分析](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499565&idx=1&sn=54a1b2de7971becd51745d8888b7b087&scene=21#wechat_redirect)

[Unity手游资源校验移除工具](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499230&idx=1&sn=f9b01d2115bef33b038288dcafca9ea2&scene=21#wechat_redirect)

[分析免费游戏辅助的盈利方式](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247490452&idx=1&sn=0c69ac0558cd42aa1a6a722443ccd68f&scene=21#wechat_redirect)

[手游修改器锁机APP的逆向分析](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247493274&idx=1&sn=7b15b6961cea659cf8f2442f03a3046f&scene=21#wechat_redirect)

[Unity il2cpp游戏逆向分析浅析](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247498268&idx=1&sn=69d33d79b9cfaa404997e9058ca37d54&scene=21#wechat_redirect)

[Unity il2cpp游戏逆向分析技巧](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247497933&idx=1&sn=fdae713f6e26a146ea84ae5ab2349b4f&scene=21#wechat_redirect)

[游戏安全：某某游戏的反外挂检测](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247484250&idx=2&sn=5cf64c104f13d72a929a6e593e0bdf0a&scene=21#wechat_redirect)

[UABEA中文汉化版(游戏逆向分析工具)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499544&idx=1&sn=84290737b6c50621c45169f9126dbdbb&scene=21#wechat_redirect)

[UnityIl2CPP游戏逆向智能分析工具V3.5](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499617&idx=1&sn=d611f63058cf7240b0abf79933eb7c94&scene=21#wechat_redirect)

[手游安全之cocos2d-x的源码浅析(手游逆向与防护)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247487966&idx=1&sn=e7c917f4aa567e2a6cf07ff5b87637f3&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Wxusn17ibicDZlrkDh16wfnJr6cVPKcug0mTn95H7TibhmIhUg46oIy6Q59XicbLlJuOIibRibZU46dCo6GBlwH9jKyyVkHmR3fT0QKr9PNvicvbmc/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Il2CppDumper图形界面版本，主要目的是简化操作流程，方便用户从移动应用包中提取数据。

📌主要用途

用于从使用IL2CPP技术的Unity游戏（常见于Android的APK/APKS/XAPK/ZIP或解密的iOSIPA文件）中，自动提取并转储关键的代码结构信息（如CodeRegistration和MetadataRegistration），便于后续的分析工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Wxusn17ibicDaEl0y5WqNKUJVPyZqhfIibYn9KUFjjxKKf4r3Q1e63jMYfOqXu1yZ0Aq8guRJafTuqPq9NacfZR0Je04Cy5xDf5hNStTJ36oeY/640?wx_fmt=png&from=appmsg)

✨功能列表

图形化界面：基于Bunifu框架构建，提供深色主题的交互界面，操作直观。

拖放支持：支持将二进制文件（如libil2cpp.so）和global-metadata.dat文件拖放到对应区域进行选择。

一键自动处理：直接拖放APK、APKS、XAPK、ZIP或已解密的IPA文件到Start按钮上，工具会自动完成内部文件查找与转储。

手动选择模式：可分别通过Select按钮或拖放方式，手动指定binary文件（即so库）和global-metadata.dat文件，再进行转储。

![](https://mmbiz.qpic.cn/mmbiz_png/Wxusn17ibicDZCpl6mXa2O2Nor4kicNNII7ZDSdE95027PcePtibgrswKmqH6Zvysaic257PmsZXYqo4yZmS6Cr4WeuFbeaCE8RUJADlco4h7uqM/640?wx_fmt=png&from=appmsg)

🛠️使用方法

1.自动模式（推荐）

将目标文件（APK、APKS、XAPK、ZIP、解密IPA）直接拖放到界面上的Start按钮，工具会自动解析并开始转储。

2.手动模式

将二进制文件（如libil2cpp.so）拖放到第一个文本框，或点击Select选择

将global-metadata.dat文件拖放到第二个文本框，或点击Select选择

点击Start按钮开始转储

[SukiSU(Root隐藏绕过强检测)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499926&idx=1&sn=701da7506a6186812d0860edd1027b8b&scene=21#wechat_redirect)

[Rizin基于浏览器的逆向工程平台](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499941&idx=1&sn=8392dd2044017fe73d6a0c3560c34187&scene=21#wechat_redirect)

[Android设备取证V2.7(修复Bug)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499950&idx=1&sn=967a28e3c42f6433959d8b4163545db3&scene=21#wechat_redirect)

[Ubuntu虚拟机上部署OpenClaw](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499708&idx=1&sn=42297f94642c6462967b23ac4c4395ff&scene=21#wechat_redirect)

[OpenClaw安全防护工具(小龙虾漏洞检测)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499877&idx=1&sn=9775bc6b1e4f73243c6ecf9e72d5d969&scene=21#wechat_redirect)

[AI智能体 | 工作流 | Ubuntu环境一键部署OpenClaw](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499774&idx=1&sn=6586fd9a45ebf52555cabbbe24b32ec9&scene=21#wechat_redirect)

[OpenClaw常用命令大全：安装、配置、服务控制与技能管理](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499809&idx=1&sn=50c91cfcb095c504068b12f5723c54ba&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/Wxusn17ibicDZUwmRaMUnbibJqy1fbfrVk0rVB07t011hUllj3FhtHic0EZa6czbuwgDrq32ZvWw2aRvJo31L6MibsfEIibMSictMquYKv8URprib38/640?wx_fmt=png&from=appmsg)

⚠️重要提示

运行环境：需要Windows7及以上系统，并安装.NET6.0DesktopRuntime

```
https://dotnet.microsoft.com/en-us/download/dotnet/6.0
```

安全警告：部分杀毒软件可能误报，属于正常现象（因涉及游戏文件修改类工具）。

[SO逆向分析工具](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484131&idx=1&sn=33027b677ed2052713d0a4dd8e72e51e&scene=21#wechat_redirect)

[AI辅助逆向分析工具](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484115&idx=1&sn=33ea5653eb3a3dae5a6234195fc43220&scene=21#wechat_redirect)

[主流AI智能体与工作流框架](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484090&idx=1&sn=f3183b88ced078f8a365df3e987a142a&scene=21#wechat_redirect)

[逆向工程框架(智能逆向分析)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499916&idx=1&sn=cc2093ac3be70f7fa9652106f2497c37&scene=21#wechat_redirect)

[SukiSU(Root隐藏绕过强检测)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499926&idx=1&sn=701da7506a6186812d0860edd1027b8b&scene=21#wechat_redirect)

[Ubuntu环境一键部署OpenClaw](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484109&idx=1&sn=ec84d0a04c359e4b8e8c9923779ba7fd&scene=21#wechat_redirect)

[Android逆向工程师的“护城河”在哪？](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499851&idx=1&sn=6bedc2e025c8473aa519bba8aae46100&scene=21#wechat_redirect)

[手搓APK:从零手动编译Android安装包](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499918&idx=1&sn=3b0a5282973b17e0fadf5183cd26e3ca&scene=21#wechat_redirect)

[Android逆向反混淆方法(mapping.txt)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499936&idx=1&sn=b6368c4c714963a90b851c66a8d479d1&scene=21#wechat_redirect)

[从零到一:手把手教你反混淆Android代码](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499904&idx=1&sn=10059d5d713820e6d627df19c5438981&scene=21#wechat_redirect)

[OpenClaw安全防护工具(小龙虾漏洞检测)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499877&idx=1&sn=9775bc6b1e4f73243c6ecf9e72d5d969&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/Wxusn17ibicDYNOUdetd6SibibGjVykPDcWz4qne8Gybk0r04WwcOkoK8lTvib2HFvyKuUSTMhcZkqPxRNxPu4AsNOsbIVic0ZdicNIlNuHaViap2WY/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

[APP逆向分析工具V4.5](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484067&idx=2&sn=9b21e868b963fc20abb451f94e27cb0f&scene=21#wechat_redirect)

[智能分析产品(28款神器)](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484067&idx=1&sn=262926786fe00667e57c2475d0a7134e&scene=21#wechat_redirect)

[Android病毒分析工具V3.2](https://mp.weixin.qq.com/s?__biz=Mzg4OTU3NTI3OQ==&mid=2247484067&idx=3&sn=885f638ab52034ce650e5750a026bbb5&scene=21#wechat_redirect)

[Android逆向技能树(2026版)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499587&idx=1&sn=e87a25ae813f9fd8032bae90f2fec586&scene=21#wechat_redirect)

[移动安全调试分析工具(29款)](https://mp.weixin.qq.com/s?__biz=Mzg2NzUzNzk1Mw==&mid=2247499688&idx=1&sn=ff0c43ecbc0bdd82dbed72f65c6f22ee&scene=21#wechat_redirect)

[Android智能调试分析工具V7.5](https://mp.weixin.qq.com/s?__biz=Mzg4...