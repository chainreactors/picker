---
title: 【2025春节】解题领红包初级题(windows + android)
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141810&idx=1&sn=7cd85d8bc111074b833f5b7623b79c57&chksm=bd50a6e68a272ff0f2f306d1087de7fcd319cf15795c85408342c438b40ee020e87f1dc83beb&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2025-02-20
fetch_date: 2025-10-06T20:35:38.453163
---

# 【2025春节】解题领红包初级题(windows + android)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJ2hsK03sCRKXzYoWPKTQvhvXYRAvotesD9C6aCfZA8CSFgckxqdPeJ3tPKELJoVpXlEISHBOXafg/0?wx_fmt=jpeg)

# 【2025春节】解题领红包初级题(windows + android)

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：geesehoward**

一、windows初级题

初级题，100%应该不会有壳，先运行起来随便输入，看看报什么错误
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJ2hsK03sCRKXzYoWPKTQvhQslBHsukQS60cYCddmdMyoiclibWNrbmAWAAsy1AatAU7j1MUGjO202A/640?wx_fmt=png&from=appmsg)

搜一下x32dbg重新启动程序并搜索字符串
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJ2hsK03sCRKXzYoWPKTQvh4KjlKwsoibodUPPlUczoSUHia1eLeF5U1Bly2f71a5RqCPaSic3czuCCQ/640?wx_fmt=png&from=appmsg)

前面有一个je，前面还有一个cmp esi edi，在次下断点并运行，esi的值是6，edi的值是1B(27)，显然不等，将je改为jne，继续运行
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJ2hsK03sCRKXzYoWPKTQvhgMUiavyfWLzz8lmTK1ON14n2QJKUNDjnXhVrQQavJqn5SNoKicGaEvcg/640?wx_fmt=png&from=appmsg)

不停的向下跟，一个27次的循环结束后，flag会出现在ebp-40的地址里，后面会被复制给ECX
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJ2hsK03sCRKXzYoWPKTQvhHQeuCpDdvh1lwNsEqrXyUUfKMibtzhHuZIIaVZ1Tsaj5CjByaUXdjNw/640?wx_fmt=png&from=appmsg)

至此，flag已经找到了，复制输入，成功！
![](https://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZJ2hsK03sCRKXzYoWPKTQvhjDtEdyxlic83u23FISwvRFKUbrQHKlBw4AOu4zN7qPIt7KlgmPokrXQ/640?wx_fmt=png&from=appmsg)

其实这个程序是先检查字符串长度是否为27，然后再将6b83537e8a30477b3e59362e4c293535340c5b5a5c797f5073747e进行计算，还原成答案，与输入进行比对，如果换成用输入反向计算去与目标字符串比对，难度无疑对新手不太友好。

flag是按位加算的，写成C代码逻辑如下

```
int main(int argc, char** argv){unsigned char encFlag[] = {0x6b, 0x83, 0x53, 0x7e, 0x8a, 0x30, 0x47, 0x7b        , 0x3e, 0x59, 0x36, 0x2e, 0x4c, 0x29, 0x35, 0x35        , 0x34, 0x0c, 0x5b, 0x5a, 0x5c, 0x79, 0x7f, 0x50        , 0x73, 0x74, 0x7e    };unsigned char flag[28] = { 0 };int edx = 0x7e9;//2025int v90 = 0x80000000;for (int i = 0; i < 27; i++)    {int eax = (0x41C64E6D * edx + 0x1E240) % (int)v90;        edx = eax;long long tmp = (long long)eax * 0x4ec4ec4f;        eax = (tmp >> 32) & 0xFFFFFFFF;        eax = eax >> 3;        eax = ((eax + ((unsigned int)eax >> 0x1F)) & 0xff) * 0x1A;        flag[i] = encFlag[i] + ((eax & 0xFF) - (edx & 0xFF)) & 0xFF;    }
printf("%s\n", flag);}
```

二、Android初级题

往年红包只玩windows和web，今年web题少，心血来潮发现工具不足啊。

初级题先试试手吧

首先，apk拖入jadx，查找个人代码部分，发现有两个FoldFragment，FoldFragment1在播放三折叠的宣传MP3，没有连个字符串都没有。文本打开mp3，也没有flag。目标转向FoldFragment2，代码里发现了3个base64的字符串，使用的地方都用同一个接口去解码，直接复制在线解码，发现不是明文。调用接口跟进去发现是xxtea加解密，正己大神还贴心的把加密接口也写进去了。

跟踪接口调用并整理的到如下Java代码

```
import java.io.IOException;
import sun.misc.BASE64Decoder;
public class calcFlag {        private static String YYLX = "my-xxtea-secret";        private static String m7483db(String value) throws IOException {            BASE64Decoder decoder = new BASE64Decoder();        byte[] decode = decoder.decodeBuffer(value);        byte[] bytes = YYLX.getBytes("UTF-8");        String retStr = new String(m7488de(decode, bytes), "UTF-8");        return retStr;    }
        private static byte[] m7488de(byte[] data, byte[] key) {        return data.length == 0 ? data : toByteArray(m7487de(toIntArray(data, false), toIntArray(m7484fK(key), false)), true);    }
    static int[] m7487de(int[] iArr, int[] iArr2) {        int length = iArr.length;        int i = length - 1;        if (i < 1) {            return iArr;        }        int i2 = iArr[0];        for (int i3 = ((52 / length) + 6) * (-1640531527); i3 != 0; i3 -= -1640531527) {            int i4 = (i3 >>> 2) & 3;            for (int i5 = i; i5 > 0; i5--) {                int i6 = iArr[i5 - 1];                i2 = iArr[i5] - (((i2 ^ i3) + (i6 ^ iArr2[(i5 & 3) ^ i4])) ^ (((i6 >>> 5) ^ (i2 << 2)) + ((i2 >>> 3) ^ (i6 << 4))));                iArr[i5] = i2;            }            int i7 = iArr[i];            i2 = iArr[0] - (((i2 ^ i3) + (iArr2[i4] ^ i7)) ^ (((i7 >>> 5) ^ (i2 << 2)) + ((i2 >>> 3) ^ (i7 << 4))));            iArr[0] = i2;        }        return iArr;    }
    static int[] toIntArray(byte[] bArr, boolean z) {        int length = (bArr.length + 3) / 4;        int[] iArr = new int[length + (z ? 1 : 0)];        int length2 = bArr.length;        for (int i = 0; i < length2; i++) {            int i2 = i / 4;            iArr[i2] = iArr[i2] | ((bArr[i] & 0xFF) << ((i % 4) * 8));        }        if (z) {            iArr[length] = bArr.length;        }        return iArr;    }
    private static byte[] toByteArray(int[] iArr, boolean z) {        int length = iArr.length * 4;        if (z) {            length = iArr[iArr.length - 1];        }        byte[] bArr = new byte[length];        for (int i = 0; i < length; i++) {            bArr[i] = (byte) ((iArr[i / 4] >> ((i % 4) * 8)) & 255);        }        return bArr;    }
    private static byte[] m7484fK(byte[] bArr) {        byte[] bArr2 = new byte[16];        System.arraycopy(bArr, 0, bArr2, 0, bArr.length > 16?16:bArr.length);        return bArr2;    }
        public static void main(String[] args) throws IOException {                // TODO Auto-generated method stub                String flag = m7483db("2hyWtSLN69+QWLHQ");                String flag2 = m7483db("hjyaQ8jNSdp+mZic7Kdtyw==");                System.out.println(flag + flag2);        }
}
```

flag拼接方法是因为试过了知道怎么用才这么写的，直接调用三次分别解三个更全面。

****-官方论坛****

www.52pojie.cn

**👆👆👆**

公众号**设置“星标”，**您**不会错过**新的消息通知

如**开放注册、精华文章和周边活动**等公告

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZK0l7v6mmrudZKXzpdM1WcomgJQnibvLzBUFRSurSkmIfl0ZrDNvSy3MszKNY3XOkcuUbWp31HMjLQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

吾爱破解论坛

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/LFPriaSjBUZLyxib6edSK27iajkxL2xVZoS1Lbnzjavd2ZDp2KicftN0Tq7vEcJMlLG3chkhj7NcSTEMoLGTRjqDaA/0?wx_fmt=png)

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