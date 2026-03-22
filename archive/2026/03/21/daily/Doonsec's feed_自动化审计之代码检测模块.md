---
title: 自动化审计之代码检测模块
url: https://mp.weixin.qq.com/s/_L6uJtgscXPboqvrNTHmrw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:13:15.259405
---

# 自动化审计之代码检测模块

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XhbqU4MQaickwKCKFibdgaQECpxYPSSOf80B0Iyibfbt06QtaEvSPOJfHlOvCZbQAjcIiapx71fM3tFTib4tJSX1Iqia7VZWdWCwxQCWIWbSnibgicc/0?wx_fmt=jpeg)

# 自动化审计之代码检测模块

原创

goddemon
goddemon

goddemon的小屋

![]()

在小说阅读器中沉浸阅读

## 前言：

填个坑，记得25年写过一篇文章

基于模型训练+规则进行识别SQL语句，其实本质上就是代码检测模块，这里简单讲讲。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XhbqU4MQaickYibia7iblbqp3sYRuW2QY3rfib1zOCtmu66WR8QFh4DwTNy5w14bfT5ib1JyibdibeMNiaMicrLWLmNB6QUKPUQ3LnMscr81QytkskJFI/640?wx_fmt=png&from=appmsg)

当时很多人没看懂，不过也很正常，这种代码检测模块目前

在安全领域相关的目前见到的文章还是比较少。

对于这个检测模块断断续续加数据改架构改了很久，之前不想聊这个的技术细节，以及不想去写，现在因为这个模块的一些东西基本上写了很多了，所以对于这个方面的有一些细节可以简单聊聊了。

## 正文：

### 先谈为啥要引进代码检测：

对于代码审计人员而言，不知道大家审代码的时候有没有遇到过这种情况，对于常见的sink方案。

即已经能确定的sink点,比如readobject这种反序列化漏洞其实是很好实现的，按道理来说直接一个source-->sink。

![](https://mmbiz.qpic.cn/mmbiz_png/XhbqU4MQaicmYm6BCYKpqyr2c0o91a88wnMBgY7KYZSyicfrJ5Y4msZibDzsDL73PGTYsuJCeMshrlJPNnvbBb5NX0b7wsCfvicGiarPghgAyiaia0/640?wx_fmt=png&from=appmsg)

可以查找出相关的调用关系，然后自己去手动跟是否可到达即可，这种大概率是可以审出来的，且查找出来的链大概率不会特别多，可以手动去跟，进而加快审计速度。

但是如果对于SQL注入又或者说是加了过滤的文件上传，又或者说是自写的业务代码，包括越权，权限绕过这种情况，又该如何玩呢？

比如拿sql注入

这种的sql注入呢 他的sink该如何定义呢？定义常见的执行函数吗？

比如定义execSqlQueryToMap吗？

那么会导致查出来一堆以及人家就是正常的sql语句执行函数，比如下面这种

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XhbqU4MQaicmvAuTsXiaj5icGDFMUU2UVcjkQfgN4iaR54PdRECuib3k4oySsnawyz30CKIApsgw7HdzYHN0NqsqXqnKVXsT7DIMfna2k54kCWBo/640?wx_fmt=png&from=appmsg)

这个代码是调用了execSqlQueryToMap，但是他也确实做了预编译处理，进而导致无法sql注入。

这样的话如果还是按照常规的思路去做source->sink。

那么会导致一堆误报，人去审也会导致审到吐，因为这样的调用栈对于一个大体量的系统而言，往往查出来就是几k条往上走。

因此迫切需要一个解，来实现解决这个问题，来引入如何快速识别一个系统的业务sink的问题。

最开始采用的方案是调用ai通用大模型的思路去做，比如chatgpt这些模型等等，但是很快我发现了问题。

问题1：误报率很高

又或者换句话来说，是很吃模型的能力，如果你采用调用普通的模型gpt3，又或者国内的deepseek模型等等，会产生一堆误报。

如果采用顶级的模型会相对好点但还是会有，大模型有个很坑的幻觉问题，当你同时给很多条同类型的操作的时候，他会突然冷不丁的给你来个误报，这个你就得加个prompt去限制，但是还是无法完全杜绝。

问题2：token消耗问题

对于一个业务系统而言，提取出的sql相关的操作就是动不动上万条，哪怕去重后都至少会涉及到w条以上的，这种对于个人研究人员而言token是遭不住的。

![](https://mmbiz.qpic.cn/mmbiz_png/XhbqU4MQaicmbHibUQs4CsXvmbArrTNzTBz3FgKDd1HicIF59dTWSbo6gM52soA5cL1JObYq5tic8Wc7vyIupZkibJJ2GKGcxnfcPjTYRc2Zkb0Q/640?wx_fmt=png&from=appmsg)

问题3：时间成本问题，采用这种方式，时间成本动不动就是一晚上或者几个小时，对于个人研究审计代码而言，这个时间成本是遭不住的。

因此代码检测模块就衍生出来了。

这里只讲最早期的版本原理为：

版本二和版本3以及现有版本暂时先不讲。

### ast规则+re正则规则+机器学习利用相似度匹配版本：

原理图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/XhbqU4MQaicnmEiauHL7RCJTLHcRgBL0BnaR0pPnEQ3KibIpVMHGVngiabVYdwNia4krxmulOuAccdibSR1uvAvpLrfL7bElrnywQL9LyWhS4wRCk/640?wx_fmt=png&from=appmsg)

#### 对于AST分析引擎而言核心原理：

1、提取变量赋值与变量拼接等。

2、利用re正则提取出代码中的漏洞sink点。

3、利用ast+第一步的变量赋值和变量拼接来进行判断是否可流入漏洞sink点，给一个数据评分。

#### 对于数据集匹配引擎而言核心原理：

1、定义一堆不同的漏洞样本数据集。

![](https://mmbiz.qpic.cn/mmbiz_png/XhbqU4MQaicmedZSd30ibNm6PicctpRO6vljbViat83icYQicMoQmskypRXgiacrN7ElRE0wXKOLCf9TxicscyC6XmjrribTaFkiarWRfC99MymUZia3r0/640?wx_fmt=png&from=appmsg)

具体内容为

这里以sql注入为例

非漏洞样本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XhbqU4MQaicnBYMQOhY8oa4PYf1JKg1ox2vxDj8BoxvduyPQwQPwpOSic7TZNd45Uficgd8o54XbCz3R1s52OTrMTKlLQBsHSEuCGknJ6ibUYW8/640?wx_fmt=png&from=appmsg)

漏洞样本：

![](https://mmbiz.qpic.cn/mmbiz_png/XhbqU4MQaicl38n3v8BTzloricFm7RpZZ4ibT1BWrQCDHH9Nn1HEFVqyHlbspmQE9IGiargHVLicflpgEAicmZRGVuic7rzOQ56gQ6fgSFmuoA8JEk/640?wx_fmt=png&from=appmsg)

2、相似度匹配：

具体原理为对输入需要检测的代码，比如我输入的代码为需要检测sql注入的

提取这个需要待检测的样本的具体代码，然后将这个具体代码进行对比数据样本里面的代码，每一个数据的样本都与他进行相似度匹配，进行计算分数。

这个算法的核心原理：

①Token Jaccard 相似度

即将2段代码的所有代码片段都拆分为词，然后取交集，并集，来进行分析是否相似，本质上就是通过代码片段相似来进行计算的。

具体可以参考gpt生成的代码来讲清楚

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(linedef jaccard_similarity(text1, text2):    # 1. 简单分词 (实际项目中通常用 Jieba 等库)    set1 = set(text1.split())    set2 = set(text2.split())
    # 2. 计算交集和并集    intersection = set1.intersection(set2)    union = set1.union(set2)
    # 3. 计算比值    if len(union) == 0:        return 0.0    return len(intersection) / len(union)
# 测试s1 = "我 喜欢 吃 苹果"s2 = "他 喜欢 吃 苹果"print(jaccard_similarity(s1, s2)) # 输出: 0.75 (交集3个: 喜欢,吃,苹果 / 并集4个: 我,他,喜欢,吃,苹果) -> 3/5 = 0.6 (修正: 并集是5个词)
```

②漏洞特征匹配：

引入这个是为了解决token jaccard相似度的一个很大的问题

因为由于token jaccard是根据拆分代码片段变成词来进行了，这种算法有个很坑人的点。

比如那么假设2段代码他的其他代码是相似的，但是核心的sql注入代码不是相似的，那么按照这个算法他的相似度还是会很高。

因此就需要引入这个漏洞特征匹配来进行分析了，即对关键的漏洞特征代码进行token计算，这个可以给的权值分数更高，进而去解决误报。

如sql

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(linesql_feature_sets = [    # (特征 1, 特征 2, 特征 3, 基础分数)    (r'StringBuilder|StringBuffer|StrBuilder', r'\.append\s*\(', r'listToString\s*\(', 0.9),    (r'StringBuilder|StringBuffer|StrBuilder', r'\.append\s*\(', r'String\.format\s*\(', 0.85),    (r'StringBuilder|StringBuffer|StrBuilder', r'\.append\s*\([^"]*\+', None, 0.8),]
```

综合计算分数和漏洞判定分数：

定义一个分数判断逻辑来进行给置信度

可以这样理解,这个可以自己去优化以及更改，最后根据这个综合分数来进行判定是否存在漏洞即可。

![](https://mmbiz.qpic.cn/mmbiz_png/XhbqU4MQaiclUOspUSPCVggvJibcp0nK48RxCtIluC5uKeobwZZNXUwLlLaqaO31hDYibHBzkv7wWNrppaibjicWz6Yl58715ibricXa5ANXsTZic2M/640?wx_fmt=png&from=appmsg)

采用这种模式最后可以给出一个大概的sink排查

### 结果与优劣势：

比如最后结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XhbqU4MQaiclc84ViapwJeX6abuQdRF2ibw4PuibqMhCMXARYsS8Dp9XLwqic9ySMSEdmE2IKYzZgMD6ly7KX3YtJHVJKOib6q8neX73qiangjgXGo/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/XhbqU4MQaicmaYtqrESOpvjx8Tib2bGv3YSStbmhrXUMZ8o6iaAFIgcFdSNMibdWMf0lGdIrEo9icEIPYe9ElRFnMSJITqeIkDwH6wYGFuibTWmpM/640?wx_fmt=png&from=appmsg)

然后正常source->sink查询即可，即可解决业务代码sink的问题。

采用这种方案与大模型相比的优势：

①识别时间跟大模型的相比更短

②硬件资源成本更低。

③误报可以自己去调，自己去加样本即可。

劣势自然也有：

①核心就是这个-->依赖样本和规则比较严重，需要自己去加规则加数据集。

②无法识别"语义相似但文本不同"的代码。

但是我个人实测来看是优于通用大模型的，而且能相对解决我的问题，而至于数据样本这些的问题，对我自身而言，其实没那么严重，构造训练即可。

而且更好的方案有没有呢，那肯定是有的。

所以建议去思考思考以及学习下，只能说在有些方面并不是通用大模型才是最优解。

组合每个的优劣势才是最优解。

至于这种漏洞检测模块的效果，只能说各位看官自己思考吧，反正个人利用这种思路挖出了很多业务的漏洞，比如成功在某知名系统，w来条sql业务里面找到了存在sql注入的点，最后形成前台rce。

## 后文：

还有很多很多想法没实现，没写完。

比如针对自己方案的代码审计模型训练，针对自己思路的skills开发，慢慢加油写，加油学了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XhbqU4MQaiclMYEZMPFbXtFNxafn3T87fs9C2D50zXFQjDw8Tjr2lIGv30xlF0G8olxuaBVzfLaf5evZbMK4rm33yucMIUaLD8czefgecvX8/640?wx_fmt=png&from=appmsg)

一起加油吧

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC53bFMu9V46j0P22R8JoWCTHPFgflsUZ0ZtjByk6kI0NGBBYVpT1KBQJhYiazTzFPicR0CShTsWCg3Q/0?wx_fmt=png)

goddemon的小屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BYtyQicN4iaC53bFMu9V46j0P22R8JoWCTHPFgflsUZ0ZtjByk6kI0NGBBYVpT1KBQJhYiazTzFPicR0CShTsWCg3Q/0?wx_fmt=png)

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