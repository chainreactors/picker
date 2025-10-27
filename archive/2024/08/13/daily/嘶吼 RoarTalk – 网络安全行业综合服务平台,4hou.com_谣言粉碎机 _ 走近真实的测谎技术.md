---
title: 谣言粉碎机 | 走近真实的测谎技术
url: https://www.4hou.com/posts/GXPL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-13
fetch_date: 2025-10-06T18:03:40.669894
---

# 谣言粉碎机 | 走近真实的测谎技术

谣言粉碎机 | 走近真实的测谎技术 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 谣言粉碎机 | 走近真实的测谎技术

RC2反窃密实验室
[技术](https://www.4hou.com/category/technology)
2024-08-12 15:00:27

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)74940

收藏

导语：关于“测谎仪很有用”和“测谎仪无用”的相悖观点一直存在，在执法系统里，支持两类观点的人数尤为众多，那么，看到这里的你又是怎么认为的呢？

**声明：以下内容符合OSINT国际开源情报搜集定义，不涉及任何非法行为，仅供交流与参考。**

0x01 测谎仪的历史

测谎仪的历史可以追溯到19世纪末期，那时人们就开始意识到：撒谎可能会伴随着生理反应的变化。

早期的测谎方法主要是基于观察被试者的生理指标，比如心率、呼吸频率和皮肤电阻等。虽然这些方法不够精确，但它们启发了科学家进一步探索如何利用生理指标来识别撒谎。

莱昂纳德·基勒 (Leonarde Keeler) 是基勒测谎仪的发明者，他一生的大部分时间都在试图辨别人们是否说真话。如下图，他通过测谎仪认识了他的妻子凯瑟琳。

![1.2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664043112501.jpg "1717660427899083.jpg")

当时的芝加哥，因其帮派和惊人的凶杀率而被称为谋杀之城。1929年，为了扭转这座城市的声誉，市政府在西北大学建立了科学犯罪侦查实验室，这是美国第一个正式的刑事调查机构。基勒夫妇成为了该实验室的两位顶尖犯罪学家，莱昂纳德成为了实验室的测谎专家，凯瑟琳成为了笔迹分析专家。

在洛杉矶，基勒直接向该市改革派警察局长奥古斯特·沃尔默汇报，后者声称该机器将提供“改良、简化和人性化的三级”。沃尔默希望他的门生的机械创新能够让容易出错和暴力的审讯成为过去。

自此，莱昂纳德的机器有了一个正式的名称——**基勒测谎仪**——并在犯罪侦查实验室中内置了一个公共关系部门。两年之内，测谎成为西北实验室最赚钱的业务。

有趣的是，随着这种设备在检测欺骗和犯罪方面的成功，”基勒解释了原理，“在很大程度上归因于这种测试在招供方面所产生的心理效应。”

他的设备原本是为了简化警方的审讯，但却成为警察强制装备库中的另一个工具。

![1.3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664043209337.jpg "1717660535182890.jpg")

![1.4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664044650774.jpg "1717660558187485.jpg")

0x02 关于测谎仪的认知盲区

测谎仪测试的使用备受争议，因为其背后的逻辑并非“**万无一失**”。当一个人撒谎时，身体会发生一些明显的变化，但当一个人紧张时，类似的变化也可能会发生。

所以，测谎的核心问题是：

**当某人说谎时，你无法预期会出现何种生理反应。**

有的人说谎可能会不断出汗，而有的说谎者则可能会全身干燥。

有些人撒谎时会变得异常紧张，而另一些人则保持冷静。

所以说，经验丰富的说谎者甚至完全可能“愚弄”测谎仪。

![1.5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664045208767.jpg "1717663037120264.jpg")

![1.6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664046191594.jpg "1717663118316893.jpg")

此外，有时如果测谎仪测试中的问题没有得到充分的设计，或者进行测试的人可能经验不足执行得不好，便会很难评估测试结果是否正确。

即使是**CIA**的内部测谎也是如此。

![1.7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664046314248.jpg "1717663284138312.jpg")

那么，如果测谎仪不能完全准确地告诉我们一个人的诚实程度，那么使用它们还有什么意义呢？

**当然有意义，**虽然测谎仪测试的结果可能并不完全准确，但它们确实可以帮助警官或探员们做出进一步调查的选择。在充满挑战的情况下，即使是这样的线索也可能会帮助执法人员彻底破案！

在**TikTok**上有位号称前CIA探员的主播，一直在分享测谎仪的各种案例和使用心得，感兴趣的朋友可以关注下。

![1.8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664049613886.png "1717663314766955.png")

前几天在香港举办的**RC2**第一场「**企业内控监察专项课程**」里，由“前香港商业罪案调查科”和“前国际刑警”的两位阿Sir，给学员们传授了江湖风水师秘籍、肢体语言、微表情、语义分析知识，以及企业内审技巧、企业内鬼心理、笔迹案例、测谎流程……等内容~

但其中最受学员欢迎的，还是测谎仪的实测体验，哈哈~

![1.9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664049150341.jpg "1717663351971908.jpg")

![1.10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664050561179.jpg "1717663385116583.jpg")

0x03 眼睛是心灵的窗户

众多研究表明，人在受到惊吓、感到恐慌和撒谎的时候，眼球都会有瞳孔放大的自然反应。基于这个基本原理，就诞生了通过瞳孔变化来测谎的设备。

犹他州 **Converus** 公司的 **EyeDetect** 是一款已经投入使用的高科技测谎系统。这原理是通过捕捉不自觉的眼球运动来识别谎言。

受试者被要求回答一些正确或错误、或是或否的问题。当他们这样做时，眼球追踪软件会观察并研究他们的反应。然后五分钟内就会提供结果，据称准确度为 **86-88%**。

![1.11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664051429667.jpg "1717663909127918.jpg")

**EyeDetect**目前已被 50 个国家/地区的 600 多个客户使用，其中包括超过 65 个美国执法机构和全球近 100 个执法机构。其首席执行官托德·米克尔森(Todd Mickelsen)表示，当局和公司正在利用这项测试来筛查许多事情：

“*这些可能包括以前的犯罪记录、过去或现在的吸毒情况、未报告的纪律处分、在工作申请中撒谎、与恐怖分子的关系。*”

除此之外，一款基于眼部识别的测谎APP，也开始受到更多人的注意和欢迎。该APP宣称适用于企业的内部场景，Whatever，谁用谁知道

![1.12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664052164070.png "1717663954144848.png")

需要注意的是，测谎仪的合法性会因国家而异。

0x04 如何在测谎时表现良好

如果需要参与测谎仪测试且希望通过，那么，了解更多潜在的情况可以帮助做好心理准备，以获得准确的通过结果。以下是一些专家提示：

**·睡个好觉** – [安静可以减少焦虑]

**·避免服用药物和兴奋剂** – 例如，咖啡因会加速心率和血压。

**·仔细聆听** – 不要被模棱两可或令人困惑的问题困扰，应立刻要求澄清。

**·简单回答**– 不要过度思考反应，因为这会改变生理迹象。

**·保持静止** – 过度坐立不安会干扰出汗和呼吸测量。

**·正常呼吸** – 使用深腹式呼吸来控制神经并避免呼吸不规律。

**·想象成功** – 想象自己平静地通过测谎仪并给出真实的答案。

**·要诚实** – 如果自己是无辜的，撒谎只会损害自身相关的案件，所以应保持真实、自信地回答。

![1.13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664053212386.jpg "1717663992201416.jpg")

一开始，杨叔对于上面部分内容不是很理解，直到自己参与体验测谎仪后，才明白上述这些细节和身体状态真的会明显影响到测谎效果。

就比如原本你身体很OK，虽然外表镇静，但由于心理过于紧张，则脉搏就会出现强烈的抖动，甚至超出正常范围~

![1.14.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664054197120.jpg "1717664020545895.jpg")

0x05 测谎技术的未来

虽然测谎仪仍然存在争议，但新技术正在不断出现，有一天可能会更加准确。目前正在发展和测试的技术有：

**·脑电波分析**：即使用脑电图 (EEG) 来检测大脑中与欺骗相关的模式。

**·MRI 扫描**：功能性磁共振成像 (fMRI) 揭示了躺着时大脑的细微活动变化。

**·语音压力分析**：声音模式和波动可能表明撒谎，特别是在重复问题时。

**·微表情**：使用算法测量反映隐藏情绪的简短面部表情。

**·体温**：红外热成像追踪与说谎相关的难以察觉的增加。

![1.15.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20240606/1717664053870789.gif "1717664053870789.gif")

然而，大多数替代方案仍处于深度开发和测试阶段，**尚未证明更可靠**。

所以如需要使用到测谎仪，那么在出现绝对准确的方法之前，最好的选择是让自己学习了解测谎仪测试为何会出错的背后原因，并采取一些能够提高有效性的安全措施。

最后，

关于“**测谎仪很有用**”和“**测谎仪无用**”的相悖观点一直存在，在执法系统里，支持两类观点的人数尤为众多，那么，看到这里的你又是怎么认为的呢？

欢迎留言，欢迎分享测谎与被测谎经验~

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OEXhpvBV)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/portraits/182735b0219b1d7a63869aa0c554f245.png)

# [RC2反窃密实验室](https://www.4hou.com/member/33jn)

专注TSCM，物理安全和隐私保护~

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/33jn)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐...