---
title: 从一张浴室照到具体门牌号，这家AI公司把室内照片变成侦查线索
url: https://mp.weixin.qq.com/s/uzB3ckEHKBXbYyoQpuLITw
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:13.091690
---

# 从一张浴室照到具体门牌号，这家AI公司把室内照片变成侦查线索

# 从一张浴室照到具体门牌号，这家AI公司把室内照片变成侦查线索

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 刷社交平台时随手拍的一张浴室，墙上的瓷砖、半掩的毛巾架、窗外露出来的一截树，搁在过去顶多算生活碎片。现在有一类AI会盯着这些像素看几秒钟，然后告诉你这是在美国哪个城市哪条街，甚至具体到哪间民宿、哪栋公寓。

这不是科幻设定。Boston公司Graylark做的Raven，前身叫GeoSpy，已经把这套能力卖进了洛杉矶警局和Miami-Dade县警局。它最近新长出来的本事，是光凭一张室内照片，反推出照片拍在哪套房子里。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqjHDY9C3QFoQTiaApwSzcFSJjDxpT1hNjf8fhonudp057PNiavqB4dESteXhBhspkbtRysmMeWDhjibxxVDCqu4ncibOyBiavXsV8o/640?wx_fmt=png&from=appmsg)

Graylark的创始人Daniel Heinen之前在国防领域做应用AI，干的是嵌入式自主、GPS失效环境下的导航、任务规划。最初的灵感来自一篇用机器学习打GeoGuessr的论文，那个游戏就是看街景猜地点。论文作者没开源代码，他们索性自己搓了一个。最早的GeoSpy很朴素，上传一张图，返回一个预测地点加一段解释，2023年平安夜上线。Heinen把它发到Reddit，以为只有一帮技术爱好者会玩，结果头三个月就攒下一百万累计用户。

真正让公司转向的是用户构成。一部分人在玩GeoGuessr，一部分人纯粹好奇，但有相当一块来自执法和政府，他们拿GeoSpy处理真实案子里的图，这些图往往没有GPS，没有显眼地标，上下文几乎为零。

Raven把GeoSpy那套定位能力扩成了一个工作台，几块拼在一起。最基础的一环叫Find Region，上传一张图，不需要坐标也不需要元数据，系统直接在地图上给出按可能性排序的地区候选。

上传图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqial9icXzuRsjIb1AVNLKxePIBiaLu283WJ9picGDTvG8fic08T6kvvbV6M9zJwlWfibeWmyALVZ0qjPnYcglOVdqSFib5FbSwbQUPvw/640?wx_fmt=png&from=appmsg)

显示位置和结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoTzGEDIicBcq9FFq6W8iaibm7zaVq7uzKW8jrDT3sn6btOPtxXAYyzNddArH8wLoENPDyITNro71P6tO0VEtOjcE60mxosBOJoX0/640?wx_fmt=png&from=appmsg)

官方演示用的是一条Facebook上的二手车挂牌，蓝色Dodge Charger停在住宅前院，模型把范围圈到了Arizona州Glendale一带，相似度72%。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrFyApPYmufUOnzdm1qJfOjcdvYn1rIZibba1sibqkB33qsbcOI1EQzYrH3XiczhMibfy8wzjIsRicVWabnlqC18icjQQWqSBW1oB4wQ/640?wx_fmt=jpeg)

线索的起点往往就是这么一张不起眼的挂牌照片

接着是Find Street，把地区缩到街道级别。系统把候选街景和原图并排摆出来，交给人工逐张比对。演示里最终核对到Phoenix北87街4226号，两侧分别是原始挂牌照和Google街景，白色SUV的位置、车道走向、门口灌木都对得上。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpH7vB82pozibjDUgK9Zfmr1FU2EsaeROL5NFud48c3oxSceP7rZLia46RJ2iczouMpJrGpd8j3Ma3K3icCZCDxIWBuAeQQ315MAMQ/640?wx_fmt=jpeg)

区域候选落在地图上，原图被钉在旁边

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDqiaRDYFgTuPfxXPzES7ibY3bdvj3ehKdia8BEA06gM7rxUIepnuCZkjvIxoOic5uXGLqOiblaoXf5vGO8ZZwcTqiarpwa3GTEEGiaNJo/640?wx_fmt=jpeg)

街道级并排比对，确认候选门牌

所有看过的线索最后汇到一个叫Cases的工作台，来源图、AI结果、标注点、笔记全叠在一张地图上，一桩案子就是一张图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpBicjYj8ybwgyibZvcs85wt5pTWnByhm4LHIG1tWnmdBtckpEA0tIQFU2SFRV8Fjkv8HQ4enlAI8jJT0icVcrxaiaBRoQqvCpQczs/640?wx_fmt=jpeg)

案件工作台：一张图串起所有来源与人工标注

真正让它最近上新闻的是Find Property和Short-Term Rental ID这两块。前者把室内或室外照片匹配到受支持城市里的候选地址，后者更猛，直接拿一张室内照或视频帧去比对全球几百万条短租挂牌。

有人截了一张建筑内洗衣机烘干机的照片，传进Raven选Find Property并圈定地区，几秒钟后地图放大到North Carolina的Charlotte，右边结果第一名写着“Renovated! Walk Uptown/located in 2 Hot Spots!”，这句话原封不动来自当地某条Airbnb挂牌，点进去照片是同一套房子。比对界面里系统在两张洗衣房照片之间连出148处对应特征，晾在架子上的清洁剂瓶子、两台洗衣机、旁边的马桶都被逐点对齐。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDozVwfAeFVAzS2IS9y2z2UKSThoT3bibqy8H4vL8zic4YScHUrZjfQGB7rzy3FSibjKBnIXeImCNBicPJFQI6cL8nk6JIuvgned1Ug/640?wx_fmt=png)

洗衣房两张照片被找出148处匹配特征，逐点连线

另一段演示里，一张来自社交媒体的浴室照被指到California的Montecito，结果名“Montecito Miramar Beach House on the Sand”，同样照搬自Vrbo挂牌。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqbgdnrmr3hDHqOACyZvnwgrqnZmPMibZSEFHgG7ibzIEPb16Ue1cdA9Ds9LnP0IkewDXCfmF1dRo5ISoZdLes5zkg66qEqDhW7M/640?wx_fmt=png&from=appmsg)

浴室照在10个区域里被框出90处对应特征

这跟大家熟悉的以图搜图不是一回事。以图搜图是拿一张图去全网找一模一样的图，Raven做的是从照片里挑出独特特征，再去Airbnb、Zillow这类地方找大概率属于同一处房产的其他照片，哪怕那些照片角度不同、时间隔了一阵。界面里有一句“city-specific property AI to determine an address”，说明这种房产检索不是全球撒网，而是给单个城市专门训一个模型，Miami-Dade县警局拿到的就是一个为该县单独训练的定制模型。

除了定位，Raven还有两块招牌本事。一块是Identify Car，光凭驾驶舱内饰或者糊成一团的监控帧，返回品牌、车型、年款的排序候选。官方演示里，一张随手拍的方向盘照片被认出是McLaren Artura 2025，置信度90%；一段运动模糊、低分辨率、没车牌的监控画面，识别出Chrysler Pacifica 2004，同样90%。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqic9DMzfdniaSVEBK4KZ8KEyZL5cCYHq3iby6TUbicKqLf01KqwmIbBArcocHNPA3LVxtbf4uD6z9Ztnh3PpT0xNclTXRygL3Lyu0/640?wx_fmt=jpeg)

一张驾驶舱照识别出McLaren Artura 2025

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrtiaj3e3x7ibiboHSFRWuYtaCH1gIzQvtoXqAicCFFUlQeob0elYsHyDicAJrSehTKtw2s1Kgvjo6KicEFVzZ08ybrZjCnPHgJqwlIQ/640?wx_fmt=jpeg)

模糊监控帧也能排序出车型与年款

另一块是Verify Image，Beta阶段，专门判断一张图是不是AI生成或被改过。它把生成概率、换脸信号、各生成器的置信度并排列在照片旁边，演示里那张人像被判“Likely AI-generated”，最接近的模型是Wan，置信度61%。官方反复强调这只是signals（信号），不是verdict（定论），最终拍板的是人。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrKInIYjrueWk5YUTOg8SCsTCLwQBw9xdgwWZCHQLLhxqXCvibbpgwIZ8R7JMQricG2gsU4dRxLSna0BGbjjewsMTI12dKEVD0iaA/640?wx_fmt=jpeg)

图像真伪评估：给出的是信号而不是判决

还有一块Live Intelligence，从一个邮箱或电话号码出发，把公开能查到的账号、评价、图片、地点钉到地图上。官方写明只调用公开信息，不碰私信，不做设备追踪，每条结果都带来源和日期。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDpS2CfECLVwqlrm6JSwNib2FhJDTZKUDCSO1Ay9MjrxHFhGMOvpv5xn01eKg4oMzibhan6GIibSSATEjibgNSetm0oia1hbLZyicjLKw/640?wx_fmt=jpeg)

从一个标识符展开到公开账号与地点

这件事反直觉的地方在于，过去大家以为保护照片隐私只要删掉EXIF、剥掉GPS就行。Raven的思路压根不看这些外挂信息，它直接读像素本身。

Graylark拿几百万张带地理标签的图训练视觉模型，模型自己摸索哪些视觉线索和地点相关。最早它盯的是建筑风格、土壤、植被这一类户外标记，后来把同一套思路推进了室内。

Heinen跟科技媒体Indicator聊过那段著名的“oh shit”时刻。第一代GeoSpy做不到室内定位，他们训第二代时，随手拿女友在浴室的自测试了一下，系统直接把pin钉在San Francisco。他当时觉得荒谬，一张浴室照而已，转头去Zillow上狂截图喂进去，十张里有九张能猜中正确城市。他的推测是，训练集里本以为全是户外图，其实混进了大量室内画面，聚会拍的、台面上食物拍的，模型不知道怎么就学到了室内装潢和地理位置之间的对应关系。

视频演示

这家公司把这类探索叫side quest（支线任务），GeoSpy本身当年就是支线，认车能力也起源于Las Vegas大都会警局调查员一句随口的提问：能不能从一张很难的图里把车认出来。产品哲学上有个刻意的设计，Raven给的是investigative lead（调查线索），不是自动判决，所有结果都带排序和相似度，留足上下文给人复核，最后的判断必须走正常办案流程去印证。用Heinen的话说，强大的AI应该帮受训人员更好地推理，而不是让他们把判断交给一个黑箱。

技术好用，不代表数据来路干净。

404 Media今年10月查到，Raven能匹配到的房源照片，分别来自Airbnb、Zillow和Vrbo。

Airbnb回话说保护社区隐私很重要，挂牌照片本来就不带位置元数据，房东可以只显示大概位置，地址要等预订确认后才给，平台也有技术手段限制自动抓取，它和Graylark没有任何合作，服务条款禁止抓取，正在审视这件事。Zillow表态抓取违反使用条款，必要时会走法律途径。Vrbo没有回应。

执法端的实际效果也没有宣传得那么神。Miami-Dade县警局公共事务办公室的Joseph R. Peguero Rivera对媒体说，到目前为止GeoSpy的使用很有限，基本是探索性的，在少量案子里过了一遍，没有带来任何重大突破或逮捕，也没有哪个案子的结果是完全或主要靠这个工具得出的。

更早的2025年1月，它还几乎对所有人开放，公司Discord服务器里有人公然求助，想拿工具跟踪女性。媒体联系Graylark的第二天，公司就把权限收紧到只对政府机构和企业用户。投资人名单里还出现过Alexandr Wang的名字，他现在是Meta的AI负责人，这件事Heinen在X上自己提过。

把这些线索拼起来，其实是在说一件事：照片的隐私边界已经变了。

你发出去的一张生活照，删掉元数据、打码、裁掉地标，在这种模型面前未必真的安全。瓷砖的颜色、窗外的植被、汽车内饰的款式、门口路面的材质，都可能成为定位线索。对调查人员来说，这是把“无从下手的一张图”变成“可以去核实的线索”的效率工具；对普通人来说，也意味着随手分享的室内场景、民宿照片，正在变成可以被反向追溯的数字脚印。

技术本身没有善恶，Graylark把判断权留给人、只做线索不做判决的设计，是这套工具少见的克制。但当一家公司能从一张浴室照反推到具体门牌号，而它训练用的数据还和几大房源平台各执一词，这条线到底划在哪里，恐怕不是一家公司能单独回答的。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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