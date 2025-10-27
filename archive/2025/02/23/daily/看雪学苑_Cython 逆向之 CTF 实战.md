---
title: Cython 逆向之 CTF 实战
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589904&idx=1&sn=e20eee8cb5a86ee3d5096ef1bdec153d&chksm=b18c2a5a86fba34cf16fb10f2e0ff9f5e2562dc0ecd692c0a8ee03dc022c9039df2b7e7dcd8c&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-23
fetch_date: 2025-10-06T20:37:01.329433
---

# Cython 逆向之 CTF 实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s1BvMTW682AtGJaBvXwBSibXsPmlRib516oUnytsAicgRnS9icYkVwuTqUg/0?wx_fmt=jpeg)

# Cython 逆向之 CTF 实战

孤恒

看雪学苑

最近cython的CTF题目越出越多，要学会手撕cython才能ak逆向了。

```
一

实战
```

题目是ciscn中的一道题：rand0m，题目给了一个py文件和pyd文件。其中pyd文件相当于dll，可以在同目录下给py文件直接导入。需要注意的是如果python版本不对会报错，如下图：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s4pWh4OXRynExm9NJicaC37sibawYKTiadZDRuqHBbMXxnViawf9lm6wbiaA/640?wx_fmt=other&from=appmsg)

我们需要一个个版本进行尝试，这里建议使用conda环境，可以快速建立python环境和切换。这里使用3.12.5版本可以运行。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s4kyaJsMcVefvuCG7ryFibjg1QrCrl16TS4GUJWEhMIhQQpCnSF6sr2w/640?wx_fmt=other&from=appmsg)

进入正题，我们用IDA打开pyd文件，然后使用`shift+F12`查看字符串界面：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sWyFjkADaxEFP9tmYzezUg3qASxgEAicFoVcTmmXpuEHXITjcoSS5o7A/640?wx_fmt=other&from=appmsg)

注意到这里有几个rand0m开头的字符串，在题目给的py脚本中我们可以发现调用了rand0m.check函数，那么我们对rand0m.check按`x`进行交叉引用。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sDjrQGen1DK5IxJ7hPiadUVVvayvicbmDrY6KniamGWibAEpqC9MN81cUYA/640?wx_fmt=other&from=appmsg)

注意到这里有几个rand0m开头的字符串，在题目给的py脚本中我们可以发现调用了rand0m.check函数，那么我们对rand0m.check按x进行交叉引用。

这里一般会出现两行，第一行引用是这个函数的包装函数，第二行才是这函数的内部实现，我们看到第二行所在的函数。函数如下：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s1CDo76wZnAib6iaubtGVibwZ3TD9UpKphiaXJyxlvwrMGqY33qqDfwYNWw/640?wx_fmt=other&from=appmsg)

##

```
二

调试
```

我们下面进行调试，首先编写一个python文件去调用函数。这里注意要使用input，方便我们使用ida attach。

```
import rand0m
tmp = input()
gu = rand0m.check(tmp)
print(gu)
```

用python调用后，使用ida attach，直接搜索python，这里这个python.exe就是我们attach的目标，记得要在函数开头先下一个断点。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9shWwjO9zO12zwxaXnng78jZjPWfFeKSEQDEpg5PS6wgc1ZRAL6icSC5w/640?wx_fmt=other&from=appmsg)

attach之后会停止，我们需要让他运行起来：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9smqlIIeua3eFWru9PbOibToMjVBCLE1Ka90kicPYtF0XicGlibPypbc9aeQ/640?wx_fmt=other&from=appmsg)

然后在命令行的input这里随便输入一些东西，然后回车，发现断在了我们下的断点处。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s7kWfGjzZAtZia3QePpic36jjYenF3dT9lfJkPefqwHK6UyBZofA8jjlA/640?wx_fmt=other&from=appmsg)

我们看到下面，一个PyList\_New是创建一个新的列表，参数是8就代表创建8个。第二个关于`off_7FFE92BAB688[40]`这类指针里面会储存python中的硬编码数据。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sOQxkOibeW9pbTx2nkANZWIruRj7K91jMYv5IKc91EKA6Xp5YBYoia4Bw/640?wx_fmt=other&from=appmsg)

上图中硬编码数据可以通过ida的交叉引用查看，例如这里的`v10=off_7FFE92BAB688[40]`那么v10里面存的就是`304643896。`

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sHxa9a3YUTmSJOr85fJQsovbiag9TpWNIiaMRNibNgTaib8NFfTnjvc3nAA/640?wx_fmt=other&from=appmsg)

接下来往下分析的话主要是看ida中粉色的函数，其他函数可以暂时忽略，关于粉色的函数可以看对于《cython的基础逆向分析》*https://bbs.kanxue.com/elink@705K9s2c8@1M7s2y4Q4x3@1q4Q4x3V1k6Q4x3V1k6%5E5P5W2)9J5k6h3q4D9K9i4W2#2L8W2)9J5k6h3y4G2L8g2)9J5c8Y4c8Q4x3V1j5I4y4U0p5#2y4g2)9K6c8Y4c8A6L8h3g2Q4y4h3k6Q4y4h3j5I4x3K6p5I4i4K6y4p5c8%4g2p5i4K6t1#2x3@1b7%4d9i4q4E0P5r3k6Z5P5q4)9J5y4e0u0r3c8o6m8D9c8o6u0p5g2h3M7%4e0@1c8C8i4K6t1#2x3V1u0s2b7K6W2w2i4K6t1#2x3V1t1&6c8@1q4W2c8l9%60.%60.*的一些分析。这个程序主要是在`rand0m.rand0m`中进行处理，我们在`rand0m.rand0m`里的开头下断点。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9su13To7GCfybEGfIZHQ6js9ozaHx21ZbCzlKh1woq8T8icaZfAakEiaxA/640?wx_fmt=other&from=appmsg)

可以查看参数a2，参数a2是个结构体，进入是数据，可以使用快捷键`d`将db转为dp

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s3Xt6Ncl3CHufDHiaLQz8Fx01qqNx6F4Q9picn8GJmj0ZXEFicngRHVicZg/640?wx_fmt=other&from=appmsg)

就可以查看到相关的结构：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sqnER7jTyej9O3BNXsRrgo9tukEiaww6cnlARboIxPiclxgN5aYZnic5rg/640?wx_fmt=other&from=appmsg)

里面的结构体大概如下：

```
dq 标志
dq 数据类型
dq 未知 （我猜测是数据长度）
dq 数据 （如果是列表或者元组可能会有多个）
```

看到rand0m中第一个对数据操作的api，这里是PyNumber\_Xor也就是异或：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sfibTtED1Tia2Du8Bg9Ricqiax3z79Yx4zyzehFhl6HA2gbYMVhbHzueDdA/640?wx_fmt=other&from=appmsg)

查看v12可以发现是我们的输入，转为了16进制：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sicGGSytbWxQhu3Yn7ISIAYws4GkEncaWobV5XOhEKrjbuHYZc0KutLQ/640?wx_fmt=other&from=appmsg)

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sE1M5UlxniaqcYeBrrFyBKcEbsXyjefuC4S67v8xDRX1VCGx9KhZssrQ/640?wx_fmt=other&from=appmsg)

然后查看`off_7FFE9DAEB688[44]`是`2654435769`，那么我们可以开始手动还原函数：

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9stGYFDicsAwmtKUicxWicfF8cQKWKaXiak0tALCvU5qSGq8LVjETIQRthFg/640?wx_fmt=other&from=appmsg)

```
def rand0m(tmp):
    tmp1 = tmp ^ 2654435769
```

下一个是右移函数，可以进去查看，这里可以看第二个参数也可以看第三个参数，那么这里可以还原为`tmp2 = tmp >> 5。`

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sFa5rfre7SJ8mMNWjEaotSEeaqCkOQXA0FDEAmJFBypianmQWkg1AdrA/640?wx_fmt=other&from=appmsg)
![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sI0Qwp4W7ibt5v2aRu5GJKlfjPUaCrUMd7a45dXdNhpGj3Vz0oGibSnJw/640?wx_fmt=other&from=appmsg)

再往下走可以看见一个左移，这里依旧是查看`off_7FFE9DAEB688[32]`，那么可以还原为`tmp3 = tmp << 4`，可以查看v12里面的内容确定是哪个变量。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9shc9M3Agg8ylAu0jOic7VktmoJGgxZM9U6a3Umg8xKE8PEOELCsGK0xg/640?wx_fmt=other&from=appmsg)

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sSWc8hm3Lc0ic82tuX2aEIGxZ2cpQeTZWPMLvicZTeiceZl3QfSy0GFyMA/640?wx_fmt=other&from=appmsg)

然后是一个按位与，这里的v16就是`off_7FFE9DAEB688`，查看是`4198170623`，那么可以还原为`tmp4 = tmp3 & 4198170623：`

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s4LNMVE86Vo42hruicoyZKJX4m0Key89PgkYPonaEMKuhIaWhiaNcpImg/640?wx_fmt=other&from=appmsg)
![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9saSVuB2maSCkib0Ew7rgy1MwTx5LiaiayTLaoMiboniceHmeKOnqqD4SY2Qw/640?wx_fmt=other&from=appmsg)

接下来一个右移一个相加，这里不多赘述，可以这两行可以还原为`tmp5 = tmp2 >> 23`，`tmp6 = tmp4 + tmp5`

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sHialic1nTViceASDeSI0kC2YibqwDU0mLDBUePhHGXmOichibotZdMADJXiag/640?wx_fmt=other&from=appmsg)

再往后一个右移一个幂和求模，还原为`tmp7 = ((tmp1 >> 11) ** 65537) % 4294967293`

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sfFu1jdeGBlCxdSdvGo2RbkbOBuaEBMHEpfLBHjU8qwhnDagwA1Js6Q/640?wx_fmt=other&from=appmsg)
![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9s3Qz3BVNic3hpVLrOQoV3DjMiaGL1Uxm0yCgROt8XN5cGAhAUzd9xJAcg/640?wx_fmt=other&from=appmsg)

总结以上为：

```
def rand0m_by_gh(tmp):
    tmp1 = tmp ^ 2654435769
    tmp2 = tmp >> 5
    tmp3 = tmp << 4
    tmp4 = tmp3 & 4198170623
    tmp5 = tmp2 >> 23
    tmp6 = tmp4 + tmp5
    tmp7 = ((tmp1 >> 11) ** 65537) % 4294967293
    return (tmp7, tmp6)
```

然后我们可以通过返回值来验证结果，可以发现我们还原的结果与题目相同。

![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9snXv7tVMFKwEZ8Nia9IBkkQjpM3HmI6cfZsDfDMOcKickJJ3ur3iaLyLsw/640?wx_fmt=other&from=appmsg)

##

```
三

备注
```

注意在取值的时候要看静态中的`off_7FFE9DAEB688[32]`，cython在动态中的数据值长度32位中只有30位是有效的，所以有可能会出现数值高位与实际值不一样的情况。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXMGiagdtH3n5zMveAxPczrZ3e9pa4Ah5XZiaGCnd2cepGwVTRYsV6Wj4w/640?wx_fmt=png&from=appmsg)

看雪ID：孤恒

*https://bbs.kanxue.com/user-home-979192.htm*

\*本文为看雪论坛优秀文章，由 孤恒 原创，转载请注明来自看雪社区

# 往期推荐

1、[关于PAN-OS DoS(CVE-2024-3393)的研究](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589341&idx=1&sn=c57db95a9d3d5f4d3d5993b9e4d2398e&scene=21#wechat_redirect)

2、[某cocos2djs游戏jsc以及资源文件解密](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589336&idx=1&sn=bb18ed6fc3311db3e80bc5435a837817&scene=21#wechat_redirect)

3、[[SHCTF]easyLogin 出题小记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589327&idx=2&sn=163feb4414326003fc3f84b95ee8b8f6&scene=21#wechat_redirect)

4、[车机OTA包解密](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589307&idx=1&...