---
title: 源鉴SCA4.7 重磅发布| 国内首创全链路可达性分析，新一SCA能力天花板！
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247520622&idx=2&sn=ce8d33ce6c886bd651c76f68e3be6eff&chksm=c144e3d3f6336ac5ae0b8c3b2effb92c5635854fbfba982f124c5f4725151c44e14143d57c43&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-10-19
fetch_date: 2025-10-06T18:53:10.519635
---

# 源鉴SCA4.7 重磅发布| 国内首创全链路可达性分析，新一SCA能力天花板！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4HaWUxLXUiaia6ZGSx1PicxMQ1jDuq0ply8hPdYOUQWVol1F3EQLHuyeyQw/0?wx_fmt=jpeg)

# 源鉴SCA4.7 重磅发布| 国内首创全链路可达性分析，新一SCA能力天花板！

Xmirror

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4Hx7dIRoGg3MNxBMdblXKicchl0RKmGfn1TpB4Ypb5wO7hm0XhI3nblJg/640?wx_fmt=jpeg&from=appmsg)

**01**

**被漏洞淹没的安全团队**

SCA用户苦误报久矣。

一个小型项目就会依赖数十个甚至数百个开源库，而对于大型企业应用程序而言，这个数字会指数型暴涨，达到千万级组件、上亿级依赖关系，相应的，与这些依赖项相关的漏洞数量随之激增。

当SCA检出数万个应用程序漏洞时，用户不得不面临这些问题：

* 所有这些漏洞都是真实存在、可被利用的吗？
* 如果存在，哪些漏洞实际威胁更大、应当优先修复？
* 如果要修复，这些漏洞具体定位在哪？

业内通常给出的解决方案是，漏洞可达性分析，即分析项目代码中某漏洞的触发函数在代码中是否被实际调用。

不过，这还远远不够。

让我们像攻击者一样思考，完整的攻击路径是怎样的？

首先是找到系统中可以被利用的入口点（如开放的API、网络端口等），然后通过这些入口逐步深入到系统的内部漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4HfeSIL53cpaRbh4nbz9LXdJyhTgP4JbYOQHakCu6QiaPmfpWELcunRbw/640?wx_fmt=png&from=appmsg)

反过来说，如果过程中任一环节是不可达的，那么漏洞的实际可利用性就大大降低。

**场景1：**在一个不对外暴露的内部系统中，可能存在多个漏洞函数被内部代码调用，但这些漏洞由于没有外部接口暴露，攻击者很难直接利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4Hk4dAZiaH2BBaQhyEFUFIb7gIqE6mkibVEsmfPTLBdE5uWI5Kjyib3sLpA/640?wx_fmt=png&from=appmsg)

**场景2：**攻击者可以通过外部接口与系统交互，但项目中依赖的带有漏洞的组件并没有在代码中被实际调用。即使漏洞存在于依赖的组件中，代码也并没有使用该组件中的漏洞部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4HEt37jKgjIuibmj4iabSqmNRDsaovfIO7BjSibssEh4vmdZ2hveWsFA06A/640?wx_fmt=png&from=appmsg)

**场景3：**攻击者能够通过外部接口访问系统，并且系统确实调用了带有漏洞的组件，但是漏洞所在的具体函数并没有被调用。

一

![](https://mmbiz.qpic.cn/mmbiz_png/CG0Yq45Q5P3xfuNicG4yictPqGTf01KGFbiaOWwwD7B5zmZlhIicr4cwhfPAdzhRd1kIcmx4Kaw8wBmML7JnFZC9icQ/640?wx_fmt=png)

漏洞大杀器：全链路可达性分析+供应链情报

## 悬镜源鉴SCA在国内率先提出全链路可达性分析+供应链情报的解决思路：外部可达、组件可达、函数级漏洞可达，三层可达性分析，并结合悬镜XSBOM提供的供应链情报视角，带来前所未有的可见性和精准定位。

1、外部可达：源鉴SCA分析应用中存在的组件漏洞是否可以通过外部访问路径（比如通过对外开放的http服务、tcp/udp服务等）被触发，如一个Java Web应用通过Spring框架暴露了特定的API，如果这些API连接到存在漏洞的函数，则该漏洞为外部可达。

2、组件可达：源鉴SCA可分析开源组件是否被自研代码引入并调用，通过对源码或字节码进行静态分析，列出可达组件的所有调用点，以证明该组件在运行中是可以被实际调用。

3、函数级漏洞可达：源鉴SCA引擎深度联动悬镜灵脉SAST，精准识别在代码中被实际使用的漏洞函数，并给出该漏洞在被检测应用中的完整函数调用链路。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4HB6IHFKXDnqSdXYtttuUyHa5JnOPPYoBTVJuRpSnOzc4qsN6J5XdgOA/640?wx_fmt=jpeg&from=appmsg)

**02**

**精细化许可合规治理**

#

# 数据显示，国内企业软件项目中，含超危和高危许可协议的项目占比达16.8%。因软件产品未遵循开源许可证相关条款规定，会造成版权侵权、专利侵权、商标侵权和许可证冲突等合规风险。

截至目前，悬镜源鉴SCA4.7版本收录开源许可证数量扩充至3000+，针对许可证的各许可条款以及许可责任提供详细的说明：

* 细化许可证兼容分析，包括具有相同条款名称但有相反责任的不同许可条款冲突的条款详情。
* 新增许可证系列概念：为简化合规治理，源鉴SCA将每个许可证都被分组为具有相似特征和风险的许可证系列，提供一组标准系列，例如AGPL、互惠、弱互惠等共6个许可系列；同时支持自定义添加、编辑许可证系列等功能，以满足企业法律审查人员的个性化要求。

**03**

**超全应用场景**

随着开发环境的多样化，开发者使用不同的语言和工具链来构建应用，源鉴SCA 4.7版本在支持开发语言、开发环境、检测对象上持续扩展，覆盖更多应用场景。

一

![](https://mmbiz.qpic.cn/mmbiz_png/CG0Yq45Q5P3xfuNicG4yictPqGTf01KGFbiaOWwwD7B5zmZlhIicr4cwhfPAdzhRd1kIcmx4Kaw8wBmML7JnFZC9icQ/640?wx_fmt=png)

iOS移动应用格式支持

● iOS漏洞与合规风险检测：源鉴SCA支持深度检测移动应用格式 IPA(IOS App Store Package) 文件，精确识别IOS中引入的C、C++、Swift/Objective-C组件及其版本，并检测组件版本相应的漏洞、许可证合规性问题，帮助开发者确保他们使用的第三方库和组件是安全合规的，减少发布到App Store时由于违规而被拒的风险。

● iOS敏感信息检测：源鉴SCA能够检测 IPA 文件中是否包含敏感信息（如用户身份验证信息、密钥等）及其存放路径，防止用户数据外泄，帮助开发者遵守iOS应用开发的隐私要求。

一

![](https://mmbiz.qpic.cn/mmbiz_png/CG0Yq45Q5P3xfuNicG4yictPqGTf01KGFbiaOWwwD7B5zmZlhIicr4cwhfPAdzhRd1kIcmx4Kaw8wBmML7JnFZC9icQ/640?wx_fmt=png)

Android移动应用格式支持

在移动应用程序（如Android APK文件）中，APK中的 Dex 文件包含了 Android 应用的字节码，源鉴SCA 4.7版本

● 提升Dex文件检测性能：大幅提升Android应用的漏洞检测速度，特别是在处理大型应用时，提高工具的运行效率。

● 提升二进制解析精准度：完善文件头识别，准确解析各类不同的文件格式，防止因解析错误而导致的漏洞误报漏报。

一

![](https://mmbiz.qpic.cn/mmbiz_png/CG0Yq45Q5P3xfuNicG4yictPqGTf01KGFbiaOWwwD7B5zmZlhIicr4cwhfPAdzhRd1kIcmx4Kaw8wBmML7JnFZC9icQ/640?wx_fmt=png)

ArkTS鸿蒙语言支持

鸿蒙是华为开发的操作系统，ArkTS 是其特有的编程语言。源鉴SCA 4.7版本新增对ArkTS语言的支持，帮助开发者在鸿蒙生态下检测其代码和依赖库中的组件漏洞，保障鸿蒙平台应用的安全性和合规性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4H4J459nZ6OEPrtiaoiaxlGaqyJmdZ3DibibBl1QQk1t7LaXicfIA39W41vkA/640?wx_fmt=png&from=appmsg)

##

一

![](https://mmbiz.qpic.cn/mmbiz_png/CG0Yq45Q5P3xfuNicG4yictPqGTf01KGFbiaOWwwD7B5zmZlhIicr4cwhfPAdzhRd1kIcmx4Kaw8wBmML7JnFZC9icQ/640?wx_fmt=png)

本地开发环境支持

##

## ● 提供本地CLI真实构建工具：通过使用开发者的本地环境进行代码构建和分析，源鉴SCA 4.7版本能够捕获更多精准的组件信息，避免因环境差异导致的误报或漏报。

● 区分开发环境和生产环境依赖：开发环境中的依赖通常只在开发或测试过程中使用，而生产环境中的依赖直接影响产品的安全性和性能，区分两者可以帮助开发者专注于修复生产环境中可能引发风险的漏洞，减少不必要的修复工作，优化资源分配。

一

![](https://mmbiz.qpic.cn/mmbiz_png/CG0Yq45Q5P3xfuNicG4yictPqGTf01KGFbiaOWwwD7B5zmZlhIicr4cwhfPAdzhRd1kIcmx4Kaw8wBmML7JnFZC9icQ/640?wx_fmt=png)

扩展集成-制品库支持

制品库是 CI/CD 流程中的重要一环，源鉴SCA 4.7版本在支持多个代码仓库、私服仓库、镜像仓库等基础上，新增支持蓝鲸CPack制品库的制品文件来源，对构建产物中的依赖进行自动化扫描和分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqoGTyy5YVHLDicTDY82NrR4HhxHpJdibiaopqDllLiazZA8Xic8VhBlTn2LSJTZia5uZoobGfbAvK4GnjQQ/640?wx_fmt=png&from=appmsg)

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqos5a6Z5B6UrU0VmoicIP7IvuJWmXe2HBJ3ZUZuPdpG4uUiaVrTFajxtY0AIjWcrWUDDeC0EFT2waicg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513339&idx=1&sn=759f859d0cf7dd748d3dd83ce49cf4cc&chksm=c144c646f6334f5017581206b0da2af90d539c921614514e3eb40f6c80d846bece0e6b521067&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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