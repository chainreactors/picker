---
title: IDA微码从mreg名获取数字编号
url: https://mp.weixin.qq.com/s/dVXzsxMs5cVBhD5htLRZcA
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:23:28.437063
---

# IDA微码从mreg名获取数字编号

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPM3FhppiaR9RjO18o8lrlyrKn2c57gkpma6VaHl9FRB4JfUFlZeuFpIGCpA0Bdm51GMTUdOOBuk3Lg/0?wx_fmt=jpeg)

# IDA微码从mreg名获取数字编号

原创

沈沉舟

青衣十三楼飞花堂

![]()

在小说阅读器中沉浸阅读

```
创建: 2026-01-09 12:12
链接: https://scz.617.cn/python/202601091212.txt
```

用IDA微码反控制流平坦化(CFF)时，可能碰上自己构造条件跳转minsn的情形。更复杂时，像"jcnd lnot(zf.1), @xxx"这种，minsn.l的类型是mop\_d。那如何构造"lnot(zf.1)"呢？我的实现如下:

```
def make_special_lnot ( ea ) :
    mop_l       = ida_hexrays.mop_t()
    mop_l.t     = ida_hexrays.mop_r
    mop_l.r     = 1
    mop_l.size  = 1

    mop_r       = ida_hexrays.mop_t()
    mop_r.t     = ida_hexrays.mop_z
    mop_r.size  = ida_hexrays.NOSIZE

    mop_d       = ida_hexrays.mop_t()
    mop_d.t     = ida_hexrays.mop_z
    mop_d.size  = 1

    minsn       = ida_hexrays.minsn_t( ea )
    minsn.opcode \
                = ida_hexrays.m_lnot
    minsn.l     = mop_l
    minsn.r     = mop_r
    minsn.d     = mop_d

    return minsn
```

有两处比较莫明其妙。一是mop\_d.size未设成NOSIZE，作为对比，mop\_r.t是mod\_z，mop\_r.size是NOSIZE。同样是mod\_z类型，为什么mop\_d.size特殊了？我也不知道，只知IDA就这么设的，可在调试IDAPython脚本时手工检查之。

另一处是mop\_l.r设为1，这是mreg zf的数字编号。微码有自己的mreg，不要与CPU的reg搞混。微码编程，操作的是mreg。mreg与reg之间有映射关系，在ida\_hexrays.py中看这几个函数:

```
reg2mreg
mreg2reg
get_mreg_name
```

目标样本是AARCH64，mreg zf的数字编号是1。起初我是在调试器中看来的，不方便，因为下次可能处理其他mreg。暂未找到合适的API，用了个笨但有效的办法，遍历数字，调用get\_mreg\_name()获取mreg名，手工建立id->name的映射表，封装函数从表中根据name获取匹配id。

```
MREG    = list(filter(lambda item: '^' not in item[1] and '[' not in item[1], ((i, ida_hexrays.get_mreg_name(i, 4)) for i in range(850))))

def get_mreg_id ( mreg ) :
    for id, name in MREG :
        if mreg == name :
            return id
    return None
```

遍历数字时，实测最大上限是850，若超过，将触发51283内部错。我看到的MREG长这样:

```
(0x0, 'cf'), (0x1, 'zf'), (0x2, 'nf'), (0x3, 'vf'), (0x4, 'pf'),
(0x5, 'cc'), (0x8, 'w0'), (0x10, 'w1'), (0x18, 'w2'), (0x20, 'w3'),
(0x28, 'w4'), (0x30, 'w5'), (0x38, 'w6'), (0x40, 'w7'), (0x48, 'w8'),
```

曾经懒得在调试器中看，已知w0是8，凭空猜测w0到w9按1步进；但看上表，错得离谱。幸亏取了全量映射。

最终make\_special\_lnot()中可以改写成

```
mop_l.r = get_mreg_id( 'zf' )
```

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPOa7YUszQ2zP2AFStE4UScicKMwhEqpde0j0FEheXVmbxSG8JFKDG3K8piaJjMHLjicL5zKemTibjvuQg/0?wx_fmt=png)

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