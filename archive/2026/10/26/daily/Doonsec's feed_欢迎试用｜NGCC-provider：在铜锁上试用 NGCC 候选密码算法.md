---
title: 欢迎试用｜NGCC-provider：在铜锁上试用 NGCC 候选密码算法
url: https://mp.weixin.qq.com/s/G3aOu--TZeSKUTEDG6k57A
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:58:37.905154
---

# 欢迎试用｜NGCC-provider：在铜锁上试用 NGCC 候选密码算法

# 欢迎试用｜NGCC-provider：在铜锁上试用 NGCC 候选密码算法

铜锁密码学社区
铜锁密码学社区

天威诚信

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](http://mmbiz.qpic.cn/mmbiz_gif/jewDP7fMjicTn2CYAUIlhqregRredYP9RaeMCIZ9ooK9U7qKwPkHttuic3N8ZdG9W38VAeGFWAu9EUqal7TaAX9w/640?wx_fmt=gif&wxfrom=10005&wx_lazy=1&tp=webp)

NGCC（新一代商用密码算法全球征集活动）由商用密码标准研究院（ICCS，www.niccs.org.cn）于 2025 年启动。目前ICCS第一轮已经收到数以百计的提案。

NGCC提案包括签名、加密等多种算法，而实际生活中HTTPS等应用往往是签名、加密结合使用的，这数百种提案便产生了数以万计种可能的组合。为了方便大家在实际应用中试用和研究 NGCC 密码提案，不用头疼的分别编译、测试，**铜锁社区推出了新项目 NGCC-provider**。通过这个项目，大家可以一站集成各种NGCC提案算法，开展算法功能测试和应用验证。例如只要在TLS命令行中指定如下参数：

```
-groups kem-01 -sigalgs sig-02
```

就可以使用01号密钥封装算法，和02号签名算法配合实现TLS握手，是不是很方便！

目前，项目已接入多种 NGCC KEM 和签名提案，支持通过标准 EVP API 和命令行使用。可以测试密钥生成、密钥封装与解封装、签名验签等密码功能，也可以验证证书签发、证书链验证，以及 TLS 1.3 中的密钥交换和身份认证。

**欢迎大家动手试用，也欢迎一起参与项目建设！**

使用过程中遇到问题，或对功能和使用方式有建议，欢迎提交 **Issue** 和**Pull Request**，参与算法适配、平台兼容、测试用例和文档完善。尤其欢迎提案团队参与，协助核对实现版本、参数配置和测试结果！

项目地址：github.com/Tongsuo-Project/NGCC-provider

## 免责声明：

本项目密码算法代码来自 NGCC 提案，功能测试通过不代表方案安全，项目不对方案安全性作保证，仅用于研究和测试！

▼

铜锁社区推出 NGCC-provider 项目，为 NGCC（新一代商用密码算法全球征集）候选算法的集成验证提供了一条务实的路径：将数百个提案算法汇聚为统一的开源实现，通过标准 EVP API 与命令行即可开展功能测试与应用验证。在商用密码算法从征集走向标准化的过程中，这类开源基础设施的价值会越来越明显。

天威诚信与铜锁开源社区渊源，可以追溯到社区治理体系建立起点。

2023年12月，铜锁开源社区项目管理委员会在无锡举办的2023开放原子开发者大会上宣告成立，由蚂蚁集团、阿里云、天威诚信、360等单位联合发起，天威诚信首席安全官兼副总经理李延昭担任PMC委员，参与社区的项目管理与发展规划。

此后，天威诚信持续参与社区治理：2024年4月出席PMC成立首年的第一次季度研讨会并作专业分享，同年12月又成为新成立的铜锁密码学开源社区工作委员会成员单位。

NGCC 候选算法的征集与验证，是商用密码体系面向未来的一次重要演进。作为铜锁PMC委员单位，天威诚信将持续参与社区建设，也欢迎关注商用密码算法演进企业试用NGCC-provider，共同为新一代商用密码算法标准化贡献力量。

**更多企业动态推荐**

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jewDP7fMjicRv9lwdnP5ETAvsV2gOWZLSWCREXTs20yYl95AbNBTyGrUicPCycwoMG7ejzrmS8HI3DiaLEbse0M5Q/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=jp7ngg5b&tp=webp#imgIndex=4)

＋

# [电子认证新规落地！天威诚信参编，以合规实践助力行业规范发展](https://mp.weixin.qq.com/s?__biz=MzU4MzY5MzQ4MQ==&mid=2247543644&idx=1&sn=4cd4effd2911129194aafebf4fb8ecb6&scene=21#wechat_redirect)

＋

# [再获殊荣 | 天威诚信荣登国家专精特新“小巨人”企业名单](https://mp.weixin.qq.com/s?__biz=MzU4MzY5MzQ4MQ==&mid=2247542857&idx=1&sn=8c979f15123b1521d78e025100b15dce&scene=21#wechat_redirect)

＋ [天威诚信与浪潮数字企业签署战略合作协议，共筑数智可信新生态](https://mp.weixin.qq.com/s?__biz=MzU4MzY5MzQ4MQ==&mid=2247543900&idx=1&sn=31dbb1e73d3f27082dbe1489df1207da&scene=21#wechat_redirect)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jewDP7fMjicR5wMV5OtcTjwaVHeybp8xUc8PrDUyoIhdaJDzjKRhN68FUicNo9icLcz7xYFz0JJEddQYSOzPNUl8Q/0?wx_fmt=png)

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