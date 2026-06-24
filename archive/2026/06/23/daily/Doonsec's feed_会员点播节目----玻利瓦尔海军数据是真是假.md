---
title: 会员点播节目----玻利瓦尔海军数据是真是假
url: https://mp.weixin.qq.com/s/_6YYPIcdZPyTWPQyHZ_cCw
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:01:32.916864
---

# 会员点播节目----玻利瓦尔海军数据是真是假

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T76uQD1Xd1r8ubrpWmiaCqaI7Gp3a3Kp513S3HOnbVDln3W718y5R7snKj2l7U4Y7wCjZfcIHVvSJcyPoiaEsj7DnEj2OhqibRsDbCAGUNWBts/0?wx_fmt=jpeg)

# 会员点播节目----玻利瓦尔海军数据是真是假

原创

bigeye\_sec
bigeye\_sec

大眼睛网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 会员点播节目----玻利瓦尔海军数据是真是假

注:本篇提到的完整数据和所使用的判定脚本,都可以在大眼睛空间发私信获取.

这个例子很典型,征得小伙伴同意,写出来供大家一起参考.

为什么说典型呢?

因为在两个前提下---一是看不懂玻利瓦尔的文字,二是对玻利瓦尔的社会背景没有基本体认---要判断一份情报文件的真假,其实是相当困难的.

那么,这种情况下到底该怎么识别?

有两个路数,一快,一慢.

快的路数,是看历史发帖.这个威胁行为者一共发了 6 篇帖子(5 个泄露帖 + 1 个售卖帖).5 个泄露帖中,其中一个"低收入人群"的帖子已经被证实为真,置信给他加一;而售卖帖只卖 100 美元,这个价格并不符合一般售卖的平均水平,置信给他减一.一加一减,正好抵消,光靠这条没法下判断.

那就再用慢的路数.

我们从这份海军数据的字段开始看起.

先看字段:

```
```
idevaluacion:评估ID, semestreid:学期ID, eidmarine:海军陆战队员ID, codgra:军衔代码, codarma:兵种代码, nombre:姓名, sexo:性别, ci:身份证号, fnac:出生日期, edad:年龄, codunidad:部队代码, unidad:部队, codcentro:中心代码, descentro:中心描述, cargo:职务, cmil:军官证号, fing:入伍日期, gradoid:军衔ID, armaid:兵种ID, antig:资历, antige:职级资历, feval:评估日期, desges:考核期描述, obsevaluador:评估员评语, detobseval:评估意见详情, apto:合格, condfis:体能状况, obsmedi:医疗意见, obsnota:成绩备注, cierre:关闭/归档, talla:身高, peso:体重, pesoid:体重分类ID, imc:体质指数(BMI), rimc:BMI范围, constitucion:体型, enutricion:营养状况, muneca:手腕围, pulso:脉搏, presion:血压, saturacion:血氧饱和度, covid:新冠状态, nat:游泳, fbs:俯卧撑/臂力, notafbs:俯卧撑成绩, natdos:游泳2, fab:仰卧起坐, notafab:仰卧起坐成绩, cdr:长跑, notacdr:长跑成绩, suma:总分, promedio:平均分, promepor:百分比平均分, respta:得分结果, porpta:得分率, usrins:录入用户, fechins:录入日期, fechaRegistro:注册日期, status:状态, value:数值, tipoPersona:人员类型, nom_comple:全名, codmarine:海军陆战队员代码, desges_original:原始考核期描述
```
```

字段如此详实,再好不过.字段越详实,我们就越有条件去做"一致性"判断.

对照这份文件,具体可以这样验:

1. 体测评分能不能自洽?

三项分数直接相加,应该等于总分(suma);总分再除以 3 取平均,应该等于平均分(promedio).一万多条数据里,没有一条算错的.这就是自洽---自洽,很重要.

人员 三项分数 suma(总分) 相加验证 promedio ÷3验证 DAYLER 100 / 100 / 100 300 ✓ 300 100.00 ✓ WILSON 100 / 70 / 65 235 ✓ 235 78.33 ✓ RONALD 80 / 80 / 60 220 ✓ 220 73.33 ✓

2. BMI 算得对不对?

BMI = 体重(kg) ÷ 身高(m)²,逐条一算,完全吻合.

 人员 身高(m) 体重(kg) 计算BMI 记录IMC 是否吻合 WILSON 1.66 85.00 30.85 30.85 ✓ DAYLER 1.60 76.00 29.69 29.69 ✓ RONALD 1.71 71.00 24.28 24.28 ✓

3. 年龄分布、姓氏分布对不对路?

男女比例约 9:1(符合军队情况),年龄集中在 20 岁到 62 岁(符合军队情况),没有一条重复,身份证格式也都符合玻利维亚身份证格式.

至于姓氏,谷歌一下就行:出现最多的是MAMANI、QUISPE、CHOQUE、CONDORI---这些都是玻利维亚高原地区原住民最典型的姓.

值得一提的是,上面 BMI 和体测日期各有一处错误.但这种错误明显是录入失误,而这类人为的小偏差,反而更印证了数据为真.换个角度想:如果是编造的假数据,要么会全对,要么会大批量出错,很难精细到去模拟这种细微的小偏差.

4. 军衔、军龄符不符合常理?

字段既然这么详实,那就连小孩子都会用的判断方法也能派上用场---年龄越大,军衔肯定越高,不可能 20 岁就当上将军.

那么具体看:COMANDATE 指挥官的年龄符合常理吗?ESSL 校长的年龄符合常理吗?司令部四个核心处室---人事处、情报处(情报部副部长)、作战处、后勤处---随便拎出几个,年龄符合常理吗?中央档案室负责人这种单位,年龄是否符合常理?

一一对照,都站得住脚.

5. 胖瘦评价对不对得上?

字段里有一项"胖瘦评价",可以拿它和 BMI 数值比对一下.写个小脚本判定,估计也没有问题.

综上:

这就是情报分析领域的"内在一致性"方法.

根据以上信息,其实就足以判断这份数据为真,置信度可以拉到很高.我们做到了---即便完全不懂目标国家的社会背景,也照样完成了对情报真假的判别.

结论:

不加入大眼睛,能行吗?

不学点外面看不见的知识,能行吗!

加入大眼睛论坛, 再也不怕暗网上当!

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YCugCES84DJcROwaz3tstQNAibgPqfGS2ok8rMk7zwso5sfA0xZNRPf4dwgS90hFPYZaztRobjfnmv7zTEjskoQ/0?wx_fmt=png)

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