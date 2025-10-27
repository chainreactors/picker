---
title: 记一次攻防演练通过SQL注入和RCE拿下靶标的故事
url: https://forum.butian.net/share/4529
source: 奇安信攻防社区
date: 2025-09-04
fetch_date: 2025-10-02T19:35:45.123438
---

# 记一次攻防演练通过SQL注入和RCE拿下靶标的故事

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 记一次攻防演练通过SQL注入和RCE拿下靶标的故事

想不到什么好标题

![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751530020492-a51635f7-907f-477b-8097-706080c47a9e.png "null")
1 依旧加密起手
--------
板块是比较熟悉的板块，起手一个加密包：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751530751822-586e92de-b18a-4b14-a437-45a4c02b38de.png "null")
简单打个断点找下加解密：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751530680359-90c89a5f-11c0-4f76-95dc-3a8afa318511.png "null")
简单测试下果然有注入，那么就要开始表演了。
2 臣乃亡国之臣
--------
加解密好解决，套个mitmproxy就可以，脚本我也写过了，在这篇文章里有详细操作过程：
[\# 记又一次曲折的集团SQL注入](https://mp.weixin.qq.com/s?\_\_biz=MzIxOTQ1OTY4OQ==&mid=2247485284&idx=1&sn=65e3e300fd3629c6403afa240a711d2d)
如果懒得自己写脚本也可以用笔者的这个项目，封装了一些常用功能，记得点STAR：
<https://github.com/AugustineFulgur/mitmproxySecurityScripts>
说实话我更喜欢基于加密的SQL注入，不用费脑子绕WAF。套上mitmproxy，sqlmap直接启动，但是跑了好几次都没有测出注入。
难道是我的判断错了？再简单手注下很明显不是啊：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751532194915-342d05bb-c6fd-461f-bbca-0db4e8f21a3c.png "null")
那就根据手注判断下数据库类型，然后加个dbms缩小下范围。根据USER命令马上定位到MSSQL，EZ~
但是加上dbms，加上technique和一些防止json失效或干扰sqlmap的脚本之后还是没法注出来，数次尝试之后为了跑这个破注入重装一上午python的我发出了破如防的声音：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751530020492-a51635f7-907f-477b-8097-706080c47a9e.png?x-oss-process=image%2Fformat%2Cwebp "null")
这下好了高兴早了，又™要手注了^ ^。
3 披甲转战南北
--------
### 换点
首先，一个系统一般只会存在1.0个2.无数个注入点。这个点不行那就换一个~换了一个我认为比较容易出效果的点，跑倒是跑出来了，是个臭盲注：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751534037808-a44bd71a-0ad6-475a-8eec-8610c2a0348e.png "null")
盲注就盲注吧，也不是不能用，但是真的太慢了（这里网好卡）。于是先放下看看别的。
### 换系统
搞到一半接到通知，靶标是此IP的另一个端口。那就存在通过数据库找到靶标系统账密的可能。SQLMAP这边开始跑库名表名，然后看看靶标系统。
![靶标.jpg](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751534363760-7122f32b-553f-46f6-acc4-3608eceaac2b.png "null")
靶标.jpg
简简单单的入口。试试登陆，不出意料也是加密的，只是长得稍微有点奇怪：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751534556448-16d3e596-a341-4372-a4ed-86b87ca2ca4c.png "null")
这个也简单，多花时间再看看咋加密的就行。
第一步是个简单的AES，这个就不多说了：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751534862539-d2e35780-cd66-41d2-93ca-77f33a55cf89.png "null")
第二步是个RSA，然后在加密前面放了个$，那就不奇怪了。
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751535085612-b0d3e621-c931-416a-acb5-7cf82881584a.png "null")
然后就是常见的先爆破再找API。这里很明显也是没爆破出来。
此时SQLMAP已经跑得差不多了，库名能跑，但一跑表名就拉闸，语句也没法执行：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751536043467-8dad1f0f-a324-4e34-9db3-2e3c02fb6ee2.png "null")
简而言之就是一个拉如闸，数据数据不出，权限权限也没有，凉凉啊。
4 朕非亡国之君
--------
我们都知道，入口点上一般没有什么好东西。在没有额外信息的情况下也不必要死死耗着，最优的解法是再过一遍入口系统，寻找入口系统和靶标系统（它们毕竟是同一个IP上的系统并且一个ToC一个ToB）之间的联系点。由于入口系统十分脆弱=&gt;我很相信靶标系统也存在这样的脆弱点，只是我们需要~一双慧眼~
入口系统中有一些查询水表的API，但是除了普遍存在注入之外没什么值得注意的。提取API出来后，找到一个看上去和SQL注入强相关的API：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751864171430-365d769b-4e04-4bb3-91a6-62ef39f75299.png "null")
这边再拼凑一下参数，反复尝试之后发现这个API的功能貌似是直接查询一个表所属内容（没有图，全是加密也没啥意思），请求json格式是这样：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751536288048-fd244963-026a-4d49-ae11-46a7152d66fe.png "null")
其中item为列名，tablename为表名，condition和orderitem为条件和排序。这就要回顾我之前的思路，\*\*“存在通过数据库找到靶标系统账密的可能”\*\*，那岂不是查到user表就行？
不过理想很丰满显示很骨感，不知道是权限不够还是没猜对，找了半天一个其他tablename都没找出来。
这时候就需要来自其他系统的信息。回到靶标系统的前端，果然靶标系统也有一些API能够查询整个表，只不过这里没有权限。综合靶标系统和入口系统的表名（都是"a\\_\\*\\*\\*\\*"格式）可以基本断定两个系统共用了一个数据库。但是由于这里泄露的表名十分的通人性，为例如a\\_log、a\\_money、a\\_pay，这样a\\_+英文的格式，a\\_user、a\\_account这样的表名不存在才很奇怪吧？
我几乎已经相信这样的表名是存在的了（不可能一堆单词一个都没用上），这说明不是我表名猜的不对，而是API权限不对。
再次搜索两个系统的API，终于又发现了一个带有tablename查询的端点，这里一试直接结束：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751537366228-08de622f-bd70-480d-8714-ef9314080d12.png "null")
由于查的是整个表，超管账号和靶标直接到手，完事儿下班~
5 朱由检最想看到的一集
------------
本来以为交了靶标就没事了，但是leader貌似想要更进一步。
首先从靶标系统的背景流量中发现了第三个系统：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751616314015-118dcd35-429c-40ac-bc12-8e9e1644f7b6.png "null")
并且还直接做了个登陆操作，这就很有意思了：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751864142370-60527b1a-e92a-451b-921b-c4a3900aa56c.png "null")
复制登陆token进入第三个系统左翻翻，右看看，我嘞个豆这不是地图吗：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751617035761-50ed8956-a27d-432b-a17b-a1e7d479e548.png "null")
马上打开控制台，小搜一波geoserver：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751617080115-7061751e-683e-4b07-bac0-52881e2196a5.png "null")
正中靶心，虽然没出路径，但起码说明了系统里有个geoserver存在。这必须狠狠滴上强度^ ^。
经过一番小猜中猜大猜疯狂猜之后，自然也是shell了：
![](https://cdn.nlark.com/yuque/0/2025/png/32358243/1751615919759-78359b39-d7d9-4dbf-afc6-8acdaadbf807.png "null")
这下是真下班，over~

* 发表于 2025-09-03 09:00:02
* 阅读 ( 2128 )
* 分类：[WEB安全](https://forum.butian.net/community/Web)

2 推荐
 收藏

## 1 条评论

[![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b9e534117404dd9e2a3e4641ef974170eed91cf.jpg)](https://forum.butian.net/people/19026)

**[c铃儿响叮当](https://forum.butian.net/people/19026)**
2025-09-03 10:57

重生之我在大明打HVV

* [0 条评论](#comment-2745)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![阿斯特](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b99df3b5f15d200a029ce5360cf8966dca8278b.jpg)](https://forum.butian.net/people/13618)

[阿斯特](https://forum.butian.net/people/13618)

公众号：重生之成为赛博女保安

11 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![阿斯特](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b99df3b5f15d200a029ce5360cf8966dca8278b.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---