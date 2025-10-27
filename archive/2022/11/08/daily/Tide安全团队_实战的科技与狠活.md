---
title: 实战的科技与狠活
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247501752&idx=1&sn=4d10831fbecb426e22b742e6ff4cff3b&chksm=ce5de5d9f92a6ccf3fc0b1ca0c8cdc5caf4877a574eac255eb2e4458dd9366bc070dd3462105&scene=58&subscene=0#rd
source: Tide安全团队
date: 2022-11-08
fetch_date: 2025-10-03T21:56:43.028865
---

# 实战的科技与狠活

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RXRyljVo5f13FNjfuy26Qqa16Nmu3xyst8pgzwgOicjz4LYWj3WCFV9ke9y9dicvficO4V1kA599uvRQ/0?wx_fmt=jpeg)

# 实战的科技与狠活

原创

那个少年

Tide安全团队

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXu3bXekvbOVFvAicpfFJwIOcQOuakZ6jTmyNoeraLFgI4cibKrDRiaPAljUry4dy4e2zK8lUMyKfkGg/640?wx_fmt=png)

## 0x01前言

在一次攻防中遇到了一个系统，过程平平无奇但是也费了些时间，这里简单的记录下。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqabkNzgmUalR7eSvViaL5ZSt0e3NO05ed2V4klxZ4X981WicV434Z7kMng/640?wx_fmt=png)

## 0x02目标

这次的目标看着就是平平无奇

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaNOYrHDfLnHS4VzZlhlHdDl6WibdyYnxTsqT3o3GheKRKQwZ63BITXWA/640?wx_fmt=png)

我一勺～(不是) 一手弱口令直接进入后台,在后台一处功能点存在文件上传

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26Qqa9fNLt8WadSABEeAzWammvCe3UCbY8NG7dFytjo7ibowN3Hibscg0IumQ/640?wx_fmt=png "null")

## 0x03科技

马不停蹄开始冲刺

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaFxnlf0VVuYVeicj16ObQEKERrHCe4F37BILIF7exZicQ95HYCXHGicLtg/640?wx_fmt=png)

内容为图片，显然有waf检测后缀，没啥好办法一个个进行测试过程就直接省略了。结论：在"filename"最后位置加一个“ " ”直接就可以绕过。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26Qqan0gia0BtxOZicVn0iasNblQ6yXILGN2oKfwdgHJiaXZABVpryH0Gia3tpvw/640?wx_fmt=png)

既然存在waf检测后缀那肯定也存在内容检测，直接上免杀马，就在自我感觉良好的时候免杀马分分钟被烂了。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaW26X0mflhULmyzfFVSJick9yahrPZI0rUkia1fdiccPxaxCh2HzNMFhoQ/640?wx_fmt=png)

这样那就只能和后缀一样一点一点进行测试，这里使用二分法测试下到底是哪儿触发了waf的规则被拦截然后再想办法进行绕过。经过测试有三个点触发waf规则 1、：<%后面跟任何字母都不行(<%try-------)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26Qqax7kKfqWO384M1vY6aSzb9W28t72pWAmb2Oia9MibFmaKia9ufu4PM4aOw/640?wx_fmt=png "null")

2、：`<%@ Page Language="CS" %>` 有它就不行猜测也是和1类似。3、：中间代码位置`new System.IO.MemoryStream(); object o.....`

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaSW7C4Hia8EZzw4W9sm8tIu7pS5ZT9jj4eG60m2ibntwnzPyrYuYJMrRw/640?wx_fmt=png "null")

1和3可以使用同一种方式绕过:利用注释添加脏字符

```
/*asdasd--------asdas*/
```

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaU2oB96Kcn2amk3xsC48G5o7eiahDxVoWa2yf6pXuNRulTE7icemNibiaJg/640?wx_fmt=png)

2可以使用另一种方式进行替换

```
 <script            language=csharp runat=server>
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RXRyljVo5f13FNjfuy26Qqa8A7DdjdKhCbJPe2HjNwPMOL6pv5IsgvziayGgWwNvMUN6iboWaPSqvKg/640?wx_fmt=jpeg)

成了！

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqasfacnNXviclvLrZEgwVyVJJuR9EPoUA4D98xsSfd42utAueZnvER1uw/640?wx_fmt=png)

## 0x04狠活

说是狠活其实也就是巧合 执行命令"whoami" iis权限 再执行其他命令然后发现已经没一点反应了，但是shell还在 emmmm

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaicY5oypicsTibMhSLmSlbsPSMn0IibPibPksE41IMxYjb6DzV0oFmXYj0Ig/640?wx_fmt=png "null")

然后发现哥斯拉自带的“sweetpotato”可以提权并执行命令，但是只能执行一个然后就卡死，所以需要一个简单高效的命令一次搞定（todesk），上传todesk-->sweet potato执行安装-->文件管理查看配置文件-->成功连接。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXRyljVo5f13FNjfuy26QqaicxuS03TdibQZZSziao8j32lBMyrPkFibKtjG25kRMUvlO7pKtQYDWN9gw/640?wx_fmt=png)

总算搞定。

E

N

D

**关**

**于**

**我**

**们**

Tide安全团队正式成立于2019年1月，是新潮信息旗下以互联网攻防技术研究为目标的安全团队，团队致力于分享高质量原创文章、开源安全工具、交流安全技术，研究方向覆盖网络攻防、系统安全、Web安全、移动终端、安全开发、物联网/工控安全/AI安全等多个领域。

团队作为“省级等保关键技术实验室”先后与哈工大、齐鲁银行、聊城大学、交通学院等多个高校名企建立联合技术实验室，近三年来在网络安全技术方面开展研发项目60余项，获得各类自主知识产权30余项，省市级科技项目立项20余项，研究成果应用于产品核心技术研究、国家重点科技项目攻关、专业安全服务等。对安全感兴趣的小伙伴可以加入或关注我们。

![](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RUGxmZ0l89buUNbyVALKxic2nM7hnDCkAKIrjKhdcDfVkGq3PxNzgs7m55BBMwmicc0AvFpYcrd6J6Q/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

Tide安全团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXKdic2aeSueSKVcSe4bg4FWpNcMVuVlfknlaOFhE5qxE5QhwDUrw1tAb8eibJcxIbqPicibfnAZibfg4A/0?wx_fmt=png)

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