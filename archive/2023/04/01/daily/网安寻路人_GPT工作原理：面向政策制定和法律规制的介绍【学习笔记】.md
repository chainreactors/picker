---
title: GPT工作原理：面向政策制定和法律规制的介绍【学习笔记】
url: https://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499426&idx=1&sn=f95945716d171c1d5718408bd28cbb2e&chksm=97e94348a09eca5ef6c6aa088abeb88c8308e0d61e077319ea241567a91e5d3c309ab3821b8d&scene=58&subscene=0#rd
source: 网安寻路人
date: 2023-04-01
fetch_date: 2025-10-04T11:22:57.567223
---

# GPT工作原理：面向政策制定和法律规制的介绍【学习笔记】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6C3JXkX3IVbtNdz79ibuJaWRjtBxtmtRtVKcPtyd5oicbSCeicdkWhWV3A/0?wx_fmt=jpeg)

# GPT工作原理：面向政策制定和法律规制的介绍【学习笔记】

洪延青

网安寻路人

**编者按**

关于LLMs（大型语言模型）的风险和监管，本公号发布过以下文章：

1. [ChatGPT是网络上的一个模糊的JPEG文件（外专观点）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499037&idx=1&sn=edf919c148180dbce5fab395d737cb90&chksm=97e940f7a09ec9e1e5f9c62de2ba580d3e35c5d5a5c093c07b7dea83425d4fa6aeee24ca3c0f&scene=21#wechat_redirect)
2. [ChatGPT是如何劫持民主进程（外专观点）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499047&idx=1&sn=d03eecb21b9ebc57280cb2f07fc467a3&chksm=97e940cda09ec9db66b84ad7178bd7e9a52a2e71cb238e3b91ae495eb55acc94aaafd311d95c&scene=21#wechat_redirect)
3. [ChatGPT：欧洲禁止Replika "虚拟伴侣"聊天机器人应用（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499054&idx=1&sn=b53342145b2eaacdee56a017294201aa&chksm=97e940c4a09ec9d297cf8792919a347b9e119ab8e32c9fd89f2dd1083370f519faed22ce8c17&scene=21#wechat_redirect)
4. [ChatGPT背后的核心技术【好文转载】](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499104&idx=1&sn=c65ee739966ef5eaa307aa3d4fcad333&chksm=97e9408aa09ec99c49648d0e8cff4c10c4464ae52624c42d8a0631ffa4dd23ae33aeb2b2d626&scene=21#wechat_redirect)
5. [基辛格、施密特等：ChatGPT预示着一场智力革命（外媒编译）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499227&idx=1&sn=2e6e03d91c0c0011b435bbd187f9407d&chksm=97e94031a09ec927c1d179c35810e4964ce622e472bf1ca40d27983b25520ade36597e408345&scene=21#wechat_redirect)
6. [OpenAI数据处理协议-全文翻译](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499306&idx=1&sn=e8ec9c1cef1e529b0c8b8d4fa243c4e4&chksm=97e943c0a09ecad670e23f6009a4c13f0548345fe92abf98c4964d8aeae2d980ba4c48893da7&scene=21#wechat_redirect)
7. [欧盟《人工智能法案》如何监管GPT模型：选译](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499319&idx=1&sn=b2500f095599060cc4edd04c5802e637&chksm=97e943dda09ecacbb7d9b6921c64fcb88dac64b9ceb3af745555ae95ec0ee424021b53338fc9&scene=21#wechat_redirect)
8. [《GPT-4 ：通用人工智能的火花》论文内容精选与翻译（好文转载）](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499393&idx=1&sn=b31493fcc0611ca08590f25645717740&chksm=97e9436ba09eca7d7c4ce9a9709ccfc6415c6e9553884af13513766a29f24582dd5d18e27cff&scene=21#wechat_redirect)
9. [马斯克等人联名签署：《暂停巨型人工智能实验：一封公开信》](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247499404&idx=1&sn=07e07eb316f0fa9b4e93a9bcd13c34dc&chksm=97e94366a09eca7014db310d7b638c8e2423af97c9baf5334a3bae74c819ae1ef031fc052515&scene=21#wechat_redirect)

今天和大家分享的公号君的一个学习笔记，很不成熟，还需要继续迭代，而且难免有错误。

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6AsdnrG26sovjQ8tlJpcCHmJOPLJm0XYjA7PRyuT4FjvoQmsrZ9k3Ww/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6pygXDOribAqks1bXs7bfOZY6ppYCzBWiabsJlicsXUBtzicLwc2dzZ7dgA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6BhBTflDt0kwjPOsSM9TaWLSoEm2pZZwNonXrlauOMrDa1J1UyN33Ug/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6fZUP8NRqKH8eiajo8v8iclb96uzeLhALnSWyoWyy4uNicxh6OKnkMD79A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R69iapCkv3YwicnvuYppyCaXGOqNeHSUn5ibaygP54OD1icOkibcr8mmicBMcQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6US3JaponABQDic6lFevK7gqjt8W9j94M5Bnol52LSk9DmY2Ktsso36g/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6fnFI5XGjCMcBkGY5PZW8YFLniarG6Xjp94oQPqS8jeLpnUkhMN93DWg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R64UI2uoSgxGPMuvLWsNnFWaLwTyoysbb4ROGpDw7mGrPAs2qzkA3Jiag/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6BJSnRIcxpd8Jmbpibbd1TqP4MmwicNauLd0rtnKw9FtyEoB0ibicUHhVew/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6ZkO76nCDRiadSniaLoBPsjV5BtLyXchXCL4FNH4iam5Qg4w1oOkUvyz9A/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6oibib9QNNIZqc5VK0tiazELJUyMUWRdm1xScDicyNj1ajf4AGyDoCs7x7w/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R60Cicib8089KI42ibogM7w809HeEdY6ykd4qUTge5a6lhl33akRIBq0f4Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6Ue8oTl7rNRfBaOWVQne5XCg18dJJ1K7PT5C26o5zxkua7qsdFgmVNg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6GMEB4ibcXYcn6BOdAlMug1oKibR6MEIHCYgicwwK1M5I7mWrLT6L6VtRw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6k3NwImAOib8aFMReGqjNaFMd1s6s1kyuEnf2icyqcBN3H6ZXy9OVaNDA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/jErr674f9micia9Fl7p1HXGBjgBhvvp6R6p3ZgphL8WvOBWc0QHZfAerxLyj5aD2z9ODBFAb4ylYDqELfa2nV8CQ/640?wx_fmt=jpeg)

数据保护官（DPO）社群主要成员是个人信息保护和数据安全一线工作者。他们主要来自于国内头部的互联网公司、安全公司、律所、会计师事务所、高校、研究机构等。在从事本职工作的同时，DPO社群成员还放眼全球思考数据安全和隐私保护的最新动态、进展、趋势。2018年5月，DPO社群举行了第一次线下沙龙。沙龙每月一期，集中讨论不同的议题。目前DPO社群已超过400人。关于DPO社群和沙龙更多的情况如下：

DPO线下沙龙的实录见：

1. [数据保护官（DPO）沙龙第一期纪实](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485304&idx=1&sn=1104896fe7262911cdf814d38f5a8ef6&chksm=97eaba92a09d33842bd45dd48349da1bf82c2ae66ab1daa49cf2ca6ce9d0519f67675540e77e&scene=21#wechat_redirect)
2. [第二期数据保护官沙龙纪实：个人信息安全影响评估指南](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485350&idx=1&sn=2270d2ca1088625e8df21bf297962656&chksm=97eaba4ca09d335a44c595caa009c212492000e489627d9316a852069d112ee6bcd3f0b9e573&scene=21#wechat_redirect)
3. [第三期数据保护官沙龙纪实：数据出境安全评估](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485566&idx=1&sn=a9ae1fe9993ec67f6d934cc38c951478&chksm=97eab594a09d3c82e0602bc822b9b36ee5c0775c0b8ce05594aa1859d3166cd47df925e0b29a&scene=21#wechat_redirect)
4. [第四期数据保护官沙龙纪实：网络爬虫的法律规制](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485607&idx=1&sn=400e306ef2ce02e8fe982fd17c627634&chksm=97eab54da09d3c5b9eb9294524c22a6f1fad0ba57dc6de89cfc15d02e844b214781ca57c3164&scene=21#wechat_redirect)
5. [第四期数据保护官沙龙纪实之二：当爬虫遇上法律会有什么风险](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485607&idx=1&sn=400e306ef2ce02e8fe982fd17c627634&chksm=97eab54da09d3c5b9eb9294524c22a6f1fad0ba57dc6de89cfc15d02e844b214781ca57c3164&scene=21#wechat_redirect)
6. [第五期数据保护官沙龙纪实：美国联邦隐私立法重要文件讨论](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485797&idx=1&sn=5528fcc192cf4a7cec5e0165e16271f7&chksm=97eab48fa09d3d992b9eb00c16b0a79729a8b064719813dfa1e35dfcef6c897cfdffd526f6cc&scene=21#wechat_redirect)
7. [数据保护官（DPO）沙龙走进燕园系列活动第一期](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485814&idx=1&sn=c6688588a68c398391017572b04da327&chksm=97eab49ca09d3d8a3085ad977d0a1f87a273a400e19ad36184fb617670f389e34f77beff5abd&scene=21#wechat_redirect)
8. [第六期数据保护官沙龙纪实：2018年隐私条款评审工作](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485857&idx=1&sn=3f7c30e30343ac659a04220110d082fc&chksm=97eab44ba09d3d5d7476e873fbffbdf1a61bfb7daed272e21435e95dff6de6bcb63fcd831588&scene=21#wechat_redirect)
9. [第八期数据保护官沙龙纪实：重点行业数据、隐私及网络安全](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247485943&idx=1&sn=5d1fc65736ccbafe2c6a36e08fd53a23&chksm=97eab41da09d3d0b30b1bbbb23cf1db8f864e85b41312443124565958f06276234da9083cda6&scene=21#wechat_redirect)
10. [第九期数据保护官沙龙纪实：《个人信息安全规范》修订研讨](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247486023&idx=1&sn=bd7f0cb068c0b245a58123bedd4e4c01&chksm=97eab7ada09d3ebb4cf92a9394e1723031f7f62ecfd61302dcee81ace92ead22274d351bc043&scene=21#wechat_redirect)
11. [第十期数据保护官沙龙纪实：数据融合可给企业赋能，但不能不问西东](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247486096&idx=1&sn=b6e8f7dbea511408e038ba0a42b18369&chksm=97eab77aa09d3e6c1b96d1bfe7d779639d569e10dfeeec61df6292b81fca8da8cc9b06b6396c&scene=21#wechat_redirect)
12. [第十一期数据保护官沙龙纪实：企业如何看住自家的数据资产？这里有份权威的安全指南](http://mp.weixin.qq.com/s?__biz=MzIxODM0NDU4MQ==&mid=2247486324&idx=1&sn=d842d4caa75b76d2ff57395464f6719f&chksm=97eab69ea09d3f8837c0a33295926a652a9c336e2a4d83098c8c820dbe1b831ebdccf02bd1ec&scene=21...