---
title: 探讨利用AI技术对源代码安全保护的冲击（下）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500375&idx=1&sn=e3afae19daa9e67d972135ec419a4b10&chksm=fa5217e9cd259efffe8c7014491eca3071675c937705d09e362c9ac5649c7c16fe0ac8396b4f&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-16
fetch_date: 2025-10-04T09:45:51.618608
---

# 探讨利用AI技术对源代码安全保护的冲击（下）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJFrElIMia46xP1DqQBTeel9uXicWc6r0YnMsasv9NNTngJOYSRSotrUvA/0?wx_fmt=jpeg)

# 探讨利用AI技术对源代码安全保护的冲击（下）

原创

HhhM

山石网科安全技术研究院

**#****0****1**

**前言‍‍‍‍‍**

上文询问了gpt一些简单的问题，并且介绍了代码保护，那么本文就AI是否能破除代码保护做进一步测试。‍

**#****02****‍**

**正文‍‍‍‍‍**

需要知道chatgpt与官方开放的openai api接口他们在智能方面也是有所区别，笔者就一段简单的混淆代码分别询问chatgpt和api，得到的结果是截然不同的。

询问代码如下：

```
<?php function TeBB($CBUbH)
{
$CBUbH=gzinflate(base64_decode($CBUbH));
 for($i=0;$i<strlen($CBUbH);$i++)
 {
$CBUbH[$i] = chr(ord($CBUbH[$i])-1);
 }
 return $CBUbH;
 }eval(TeBB("U1QEAu60lMwCxdKsvDRNLRsIR6OiokK/tKAgNz9ZP6UgT8MGAA=="));?>
```

比较简单的混淆，大部分小伙伴还是可以理清它的一个混淆逻辑，主要就是base64+gzip，ord-1，其实会发现，为方便各位观看这里给出源码：

```
<?php
echo time();
echo 'www.toolnb.com';
?>
```

那么接下来问问gpt看看它的回答：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJNibib4jpo6oo5XQ4cJQ2QktFNWaOD1ehVsNw6XWdXSCF1agpsMwuw83A/640?wx_fmt=png)

第一次询问将完整的代码发送后得到的是对于代码的解释，就我发送的询问以及给出的这段解释而言并没有什么瑕疵。那么这段代码要还原混淆，一个办法就是获取到TeBB函数执行后的返回值，也就是eval的参数，那么如此来询问gpt：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJfsgeHgD8cibJ0PnXia89UZicftoVyzvp172VoUkBy5VJ95PRTPpueL1Pw/640?wx_fmt=png)

会发现gpt给出了一个不算答案的答案，并没有回答到核心点，也没有给出我们想要的内容，那么来看看openai api给出的答案：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJErENeCdicHtico4xDy7dXIdNbxPV8s0b1YefJKqgdJjibDp1VibVicwPtUw/640?wx_fmt=png)

很明显，智能了很多，但在第一次的回复中发现有些许问题，这个ai在胡乱编造内容，我的程序源代码为第二次回复的内容，但在第一次回复中ai明显不清楚正确的参数值，并且给出了一个看似正确的hello world！

很显然，就比较简单的代码混淆而言，ai还是可以识别，但准确率还有待进一步确定，接下来给ai提点难度。

源码还是上文中的源码，混淆后代码如下：

```
$O00OO0 = urldecode("%6E1%7A%62%2F%6D%615%5C%76%740%6928%2D%70%78%75%71%79%2A6%6C%72%6B%64%679%5F%65%68%63%73%77%6F4%2B%6637%6A");
$O00O0O = $O00OO0 {
    3
}.$O00OO0 {
    6
}.$O00OO0 {
    33
}.$O00OO0 {
    30
};
$O0OO00 = $O00OO0 {
    33
}.$O00OO0 {
    10
}.$O00OO0 {
    24
}.$O00OO0 {
    10
}.$O00OO0 {
    24
};
$OO0O00 = $O0OO00 {
        0
    }.$O00OO0 {
        18
    }.$O00OO0 {
        3
    }.$O0OO00 {
        0
    }
    .$O0OO00 {
        1
    }.$O00OO0 {
        24
    };
$OO0000 = $O00OO0 {
    7
}.$O00OO0 {
    13
};
$O00O0O. = $O00OO0 {
        22
    }.$O00OO0 {
        36
    }
    .$O00OO0 {
        29
    }.$O00OO0 {
        26
    }.$O00OO0 {
        30
    }.$O00OO0 {
        32
    }.$O00OO0 {
        35
    }.$O00OO0 {
        26
    }.$O00OO0 {
        30
    };
eval($O00O0O("JE8wTzAwMD0iSERsdXpXalhGcVRheGVHU1V0Wm5KTm9zWXJWQ0loT01iTHZ5UW1SY2RrUEtpQXBnZkV3QmplcGNObWZJRHduZGFsR3ZXUkVQRkhpT0NxcnlvZ1l6UU1CdGhaVmJVVGt4SkFTTHVLc1hrZTlzZGpBeEVtSGlRdFgwZG0xcHh5VDd5WnJmZEc4TEYzVTNVdDUwUTI5T1Fab2NDMjlSRk5PPSI7ICAKICAgICAgICBldmFsKCc/PicuJE8wME8wTygkTzBPTzAwKCRPTzBPMDAoJE8wTzAwMCwkT08wMDAwKjIpLCRPTzBPMDAoJE8wTzAwMCwkT08wMDAwLCRPTzAwMDApLCAgICAKICAgICAgICAkT08wTzAwKCRPME8wMDAsMCwkT08wMDAwKSkpKTs=")); ?>
```

无论是gpt还是api给出的都是废话文学，以gpt为例：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJwsOvsRVEias6JM8k0gDLDPaynmOHhicWmrfzk0oPzv8P6NyvOPNSd8mA/640?wx_fmt=png)

尽管给出了些许解释，但显得那么苍白无力，有用的只有那句“它可能会执行恶意代码”。那么稍显智能的API的回答是？

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJvKUUialTlch5mgdzz9AmNMIKvQ0BM211KjJ5r5BQkTGWAw38KXLCtQw/640?wx_fmt=png)

好吧，看起来有些不同，它将urldecode里面的url编码解码了，但是对于解混淆而言没有任何帮助。

它将输入的代码原样返回同时解释了eval可能造成的问题，而api则直接返回我输入的代码并且没有其他解释，在这方面来看gpt反而更热情些？

**#****03****‍**

**解释OPCODE‍**

上文文末提到了OPCODE，本着严谨的态度，我又思考了一下，AI它既然是经过大量训练，那么也许能够胜任一些对于我们人类比较复杂且耗时，但本质上不难，只需要大量重复的工作即可完成的任务，那么此时自然想到PHP执行时的中间语言OPCODE。

opcode是php语言里供zend引擎执行的一种中间代码，可以把它类似于java中的字节码、或者python中的字节码对象pycodeobject。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJibHicoOibGomxM1lZiaMNLnsF5c4uMU4CuvyzQXbialnHqP3KbHBZ4dr1Kw/640?wx_fmt=png)

PHP Performance I: Everything You Need to Know About OpCode Caches – Engine Yard Developer Center

解释器执行(ZendVM)过程即是执行一个基本单位op\_array内的最小优化opcode，按顺序遍历执行，执行当前opcode，会预取下一条opcode，直到最后一个RETRUN这个特殊的opcode返回退出。

在针对代码保护的破解中有时候我们无法获取到源代码，只能获取到中间代码也就是OPCODE，但目前网络上没有公开的OPCODE还原方案或者项目，如果AI能够破这个局，那么对于代码保护而言又是一个新的挑战。

那么在网络上很容易查询到各个OPCODE对应的含义，此处展开内容稍多，用一个示例较好理解，以代码为例：

```
<?php
echo “hello world”;
?>
```

对应的OPCODE如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJQk2THaDhBnfibQtBmnXZWWXWv0MAaoRH2kuCKn8B7vF6GPqyVib7G6ibg/640?wx_fmt=png)

那么如何得到如上图中所谓的OPCODE？这时候就用到一个工具/扩展，VLD。安装方式搜索引擎很容易搜索到，安装完成后使用如下命令：

```
php -dvld.active=1 test.php
```

此时就会输入类似如下内容:

```
inding entry points
Branch analysis from position: 0
1 jumps found. (Code = 62) Position 1 = -2
filename:       D:\xxx\xxx\xxx\test.php
function name:  (null)
number of ops:  2
compiled vars:  none
line     #* E I O op                           fetch          ext  return  operands
-------------------------------------------------------------------------------------
  40     0  E >   ECHO                                                     3
         1      > RETURN                                                   1

branch: #  0; line:    40-   40; sop:     0; eop:     1; out0:  -2
path #1: 0,
3
```

那么会发现只要我们能拿到这一段OPCODE，将之逆向后即可还原PHP代码，那么上文也提到了OPCODE混淆，遇到此类混淆时VLD会失效，但可以通过魔改VLD去获取到实际执行的OPCODE。

那么需要知道一点，这种OPCODE与PHP代码都是有一一对应的，交给ai来干也许会有意外之喜，那么直接用上比较聪明的openai api：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJHzELajKu5L8r3U0pfeIchvQ7YnYg2j4Hr764EpCNpAmoUOvaNHclibA/640?wx_fmt=png)

好吧，api由于长度过长会卡很久最后导致没有响应，而显然这opcode的还是过长了，既然支持上下文，那么尝试换一段稍短些的OPCODE，再用上下文把它分割一下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJ8nibibmibQMjiauZnJAGPg5IXzT0zwhNIGWHV98cAgwic5RvezibJtNZst2w/640?wx_fmt=png)

好的，给出了正确的代码，而让我比较意外的是chatgpt由于支持文本较长，我给出一段较长的OPCODE反而能得到相对正确的答复：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJYjdru8k1aGLuvng3Tgick23Xwoq8AxoGphhrBkmBicMNkkyCF3J4nbFA/640?wx_fmt=png)

第一次的回答没有给出源代码，但经过进一步的询问后，在第二次回复中就完整的还原了代码：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRk6IlqcMJZcGNeBJbMkkeJOcJGaRCLALD770EMt5O8xhmjM4cibYcEc38xzEKroXex1YExbL91rtg/640?wx_fmt=png)

尽管，有些明显的缺陷，但已经算是还原了代码，人工的调整一下即可，就它给出的回答来看用来辅助还原是足够了。

实际上笔者写了个OPCODE还原PHP代码的半成品用来在平时遇到混淆代码时可以辅助着还原，而目前的AI已经初步具备OPCODE还原能力，就我个人认为AI对于OPCODE还原度已经很高了，让我对于AI后续的发展有进一步的期待。

**#****04****‍**

**后话‍‍‍‍‍**

就以上对于AI的使用感受，AI对于PHP代码保护的破解目前来看，且门槛相对较高，需要步步调教才能将之破解，例如上文的混淆，在不熟悉混淆解密方式的情况下，无法得知混淆的入口为eval函数，门槛低的如在线破解网站（上传文件-》自动破解-》下载破解后的源码）；但对于单纯需要花费时间，只需要机械性地还原的内容，如OPCODE，使用AI将大大提高破解效率。‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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