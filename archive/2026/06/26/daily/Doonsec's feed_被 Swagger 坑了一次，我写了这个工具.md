---
title: 被 Swagger 坑了一次，我写了这个工具
url: https://mp.weixin.qq.com/s/Vwy8WAVD4XfV5gR-nuvMxg
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:45:55.264228
---

# 被 Swagger 坑了一次，我写了这个工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/72I8gAalpPVUibvFib4wdNlSk5AzT7RdB0NrGymwYhH7Yp9YblUVCEhkBa10xJR8ebiaswEEWbo2vw8yDQ6f847W7AthFC4PgAdsUZkTtbM5lE/0?wx_fmt=jpeg)

# 被 Swagger 坑了一次，我写了这个工具

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近周末刚好有点空，就抽空写了一个 Swagger 自动测试脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPXf8EBWVicSE9IPP87ZjfIu89bqXJo6SotsBFoiaNYEJPWD0ic50seEzodzU93G6NbhtkVUuDRv1NYMN7pXzPjweyvlcUIh0U9WG8/640?wx_fmt=png&from=appmsg)

写它的起因很简单：做安全测试时，大多数 Swagger 插件都能快速地识别接口并自动发起请求，但总会遇到一些特殊场景，导致插件识别有误，只能手动修改、重新导入，甚至一个接口一个接口去尝试，不仅麻烦，还容易遗漏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPW1CupauALttPfIqibN387H4EUBQtibosDPBe7UzW6TFBzy90ibudqSANPMHr7ic4f0O9Uw1hSHhwUGL68YicWm2wIEk0EIFW7lpicvc/640?wx_fmt=png&from=appmsg)

就比如如下场景：basePath和paths重复，那么插件就会识别为/api/v1/api/v1。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPXXQCo1KY2xV5aLcEKGOmCEAuribXKBJdfO9UK1SDbIrvt0Hq2KnaGlMPEYzpcE9bCgIPxjibe6g0FLibWjnmTqBmCfQ9VXL8AS7U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVaibWVOCseDhWQl5V3Oxj1jc2GsTCoEzTBGibtTSSfWB650dcEkE6EmwOew578Ttr0gZVbJtZkeNqHySKA9CHG9LwL65ciafibEIg/640?wx_fmt=png&from=appmsg)

再比如swagger管理在a.com/swagger.json上，但是实际api接口却是在b.com上的情况，之前也有遇到。当然类似的场景还有很多，这里就不一一展开了。这些问题本质上都是Swagger 描述信息与真实接口存在偏差。遇到这种情况，如果不想手动一个个接口去尝试，那么这个脚本就能派上用场。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVptrX7dtUx66yvJsGPAryJUGM82KgG1ZFpM8a41KfsWvrO9WjibWlOCgfSmpvz8wuibwOncdkgJtqUlrGZkQib67J2ibnsz9JickP8/640?wx_fmt=png&from=appmsg)

脚本大概功能如下，简单解释就是这个脚本可以从线上链接读取，也可以从json文档中读取，只要符合规范。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPUJLttTF3W1Giaic0mTgriat9Q7bicWPcGYR7xOCbYEUNzIYIHAeQsVqd2KJoSdv8pDAKicRUwDePlPEx2TibYw6Pibovv2f5p0zkus8k/640?wx_fmt=png&from=appmsg)

其中容易误解的就是--spec-header和--api-header，之所以设置这2个是因为我遇到过，没有遇到过基本上可以忽略。

> --spec-header：swagger页面的认证，如果swagger页面需要认证，通过这个指定认证header。

> --api-header：这个是api认证头，测IDOR时用，有时候未授权访问可能效果不佳，但是IDOR却效果不错。

另外几个入参也简单解读一下。

> -b/--basepath：也就是我们前面看到的swagger页面中的basepath。

> -u/--url：指定和api拼接的url（如果swagger页面是正确的就不需要指定，只有不对应或者直接从文档中取的时候需要指定）

简单过完了入参的作用，还是用前面的例子来简单的看一下用法。出现前面的情况，不管是basepath多了还是少了，只要-b定义了优先以-b后的为主，那前面的多了一个api/v1，那就直接-b "" 传空就行，如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPUFw5YcibhIrCePK9ZGwbU7yOyr269q5IicFVpiawkL2gDYszSAon0OcU4NtIDQqHPHLNv0dsUUL9VY3aiaEEP0hdnZg4vlicerR88U/640?wx_fmt=png&from=appmsg)

至于结果采用md文档输出，另外中间的入参会根据类型自行补参。简单看看输出报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVqyAG44rQC9PuJ7U8L1P3ZWIBLRRPm72PjKp4z9aicT8yG7CiaGtewbicoSu8mO5gWkORiaOiaome2wbQictWIomDsUicH45icRnT11ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXxiaAMEONRmkZQiaTCQ51faPKAq81DZpPCjicxjYaqib6rhkiafzia4zxtFdyCdOvhiactkpf0AM9xZ5uQK9jeSmT2Q2piaMFI2EjibZMU/640?wx_fmt=png&from=appmsg)

自动补参，如下。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPWapkEXQUJvUwfhsaHPIYcsLNpHdExZTvXnoS4dHnlt6Xs8cnyPlwNPVBBlw7WhH4ibQmpY3WicP0gHbWibdeicHjPYDB6SOicmb0QI/640?wx_fmt=png&from=appmsg)

成功结果如下。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVavLYshyeOtcDxiaOgEvFBwS7l1FRmtmgnr5UdU0uCZBTBhhEGmiaeBQ1Q8Qsf1EpAVGibVQd7bCk3fIMCicZ3ry36cvfblLFU6Ko/640?wx_fmt=png&from=appmsg)

需要脚本的，回复公众号“swagger”即可获取完整脚本。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVMcDwKpfcwOcHc6OufflQ2I9wIYY3ycVgMejoGnN0ibsdPXce3sF57T4n365uHS6XTiarOQg2gjzA8ck5cYddkWkKGM1IgCp95E/0?wx_fmt=png)

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