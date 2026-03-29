---
title: [视频]3月-完全无法检测的Cobalt Strike在卡巴斯基上的表现
url: https://mp.weixin.qq.com/s/rDCswVj5oFdUzEA83YEIUQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:36:01.882310
---

# [视频]3月-完全无法检测的Cobalt Strike在卡巴斯基上的表现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibXL9MCj2GqMliamIEichkbzbb09CcAqqOmuVqhxVkFXzte0CV0Mgpm8ug3RsLLx2NhejO1NRBS0YwStNbTvicnGLSjyEVjm7Aw4qaUSJVxlzBs/0?wx_fmt=jpeg)

# [视频]3月-完全无法检测的Cobalt Strike在卡巴斯基上的表现

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器中沉浸阅读

### 一、演示

#### 技术涉及

* • 完全无法检测的Cobalt Strike
* • 高级DLL代理技术

#### 章节介绍

* • 第一部分：安装
* • 第二部分：生产环境的Cobalt Strike 和测试环境
* • 第三部分：使用高级DLL代理技术绕过kaspersky，自动进程注入及屏幕截图
* • 第四部分：内存扫描
* • 第五部分：原版Cobalt Strike
* • 第六部分：价格及用途

#### 历史相关：

* • [红队战术武库演示(1月)](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484601&idx=1&sn=f4999fd27213a121586f86882ba9f354&scene=21#wechat_redirect)
* • [完全无法检测的cobaltstrike更新](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484350&idx=1&sn=315be5bb352b68482ce277b76b6df5d1&scene=21#wechat_redirect)

### 二、使用场景

* • 模拟高级攻防，企业演练以提升安全意识。
* • 适用于廉政，公安等场景。

**提示**：该方案需签订红队工具销售与使用合规协议[1]

### 三、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

* • 仅可用于已获得书面授权的目标系统测试；
* • 遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

#### 推荐阅读

* • [Tigress和OLLVM混淆c代码](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485053&idx=1&sn=3b11589664ef3e5d0912655ac71898f9&scene=21#wechat_redirect)
* • [Lua作为攻击载体的技术分析](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485047&idx=1&sn=bab961b4ca0d9dd1a9454b3455eaa0a2&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV5](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485039&idx=1&sn=8ec2ff200c6d47d34f3ee7674ab5a963&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV4](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247485029&idx=1&sn=31ac67de9dac6b5f8bf994cd405f7f25&scene=21#wechat_redirect)
* • [[更新]红队加载器LoaderV3](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484984&idx=1&sn=deeff44bf9662665700e22650318c94e&scene=21#wechat_redirect)
* • [攻防必备，DLL代理自动化生成](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484664&idx=1&sn=161e2f5bd7433ff9404ac38ecc7724b9&scene=21#wechat_redirect)
* • [攻防必备，DLL侧载（白加黑）自动化生成](https://mp.weixin.qq.com/s?__biz=Mzk5MDE1MTY3OQ==&mid=2247484651&idx=1&sn=f51b71f50fa18120513848832a7bcdd0&scene=21#wechat_redirect)

#### 引用链接

`[1]` 红队工具销售与使用合规协议: *https://www.kdocs.cn/l/cqPic7iLh0hn*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/TxTGvuNE4vMI7CibneGnaTrUe8AO96ickclFib7VibicQZPEB6kJBcIGEmib8iaAjeoT30iaKayk1fd1ask6Z3ksINc84A/0?wx_fmt=png)

白帽子安全笔记2.0

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TxTGvuNE4vMI7CibneGnaTrUe8AO96ickclFib7VibicQZPEB6kJBcIGEmib8iaAjeoT30iaKayk1fd1ask6Z3ksINc84A/0?wx_fmt=png)

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