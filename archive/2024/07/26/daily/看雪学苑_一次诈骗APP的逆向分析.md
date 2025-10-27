---
title: 一次诈骗APP的逆向分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564954&idx=1&sn=7db08f67e0a0c494cab87f2b6344875f&chksm=b18d89d086fa00c644c7c7797311a14c47a4f6599abada11c655c21e3416d15feb3b4e53cffc&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-26
fetch_date: 2025-10-06T17:43:01.148081
---

# 一次诈骗APP的逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZhqk2nB14q1nQR74qUu5D48gHTichTorPHc6tEaXWRFfmJe4wxZApicjw/0?wx_fmt=jpeg)

# 一次诈骗APP的逆向分析

touful

看雪学苑

```
一

APP介绍
```

最开始朋友给我的时候，让我帮他找个ip，我还以为是个取证题目，最后发现，找到的ip和域名都是存活的，嘶，那就有意思啦。

拿到手发现就6M多，我想，这怎么可能能luo聊，和朋友沟通发现，这只是在luo聊软件中推广的软件，封面做得就很low，甚至连APP icon都不愿意放一个，名称叫《羞密基地》。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZTenibtXiaiaY4NbLnC5hibdMRy4TOghicKVwKt7TY7yASfzUGTjcCZlkqVw/640?wx_fmt=other&from=appmsg)

怎么越看越像一个CTF题目呢，好劣质的感觉。

最开始没仔细看反编译结果前我还以为真能进去呢，还要了当时被诈骗的房间号，结果发现一直卡在那，感觉不对劲，又回去仔细看了看。

```
二

逆向分析
```

核心逻辑全在MainActivity里面，一点多的都没有（除了一些工具类）。

```
if (ActivityCompat.checkSelfPermission(this, "android.permission.SEND_SMS") != 0 && ActivityCompat.checkSelfPermission(this, "android.permission.READ_SMS") != 0 && ActivityCompat.checkSelfPermission(this, "android.permission.READ_PHONE_NUMBERS") != 0 && ActivityCompat.checkSelfPermission(this, "android.permission.READ_PHONE_STATE") != 0) {
            showUserInfo("App所需基本权限, \n请允许，未允许将无法提供服务！");
            return;
        }
```

要了一堆基本用不到的权限，符合我对诈骗APP的固有印象。

然后事情就开始离谱了起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZhxZpibjQ238WeibDHGSN1B6usUeqibDS1bkmG6ZZctDRbj8EpBhrGOmJQ/640?wx_fmt=webp&from=appmsg)

这么多参数，看不得看死，直接抓包吧，本来我是觉得没什么的，一抓包给我吓了一跳。

这里通过静态分析可以看出，走的全是http，甚至不用配置证书。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZXuQ2H6U2LSCxqd4Ry2BOribt6qfnKs6vGIiaBAss5S9ceTep5iaSgp98w/640?wx_fmt=other&from=appmsg)

这里两个外网服务器，下载文件下来之后，发现就是简单的base64，没有额外加密，就能拿到ip和端口。扫描一下ip，从服务器上没看出什么有用信息，就尝试动态分析呗。

最开始还是一贯性的想上frida，但是抓包明显更简单，那就fiddler吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZkicq6YMUZJ0mPeTeTVDSDp5iaSPpCnVf7wJiapBXMgqtHqeujlJc3L1Aw/640?wx_fmt=other&from=appmsg)

基本逻辑和分析得一样，通过两个txt文件拿到真实服务器的地址，其中108是用来记录post参数的，之前图中的device、phone number等数据。

149这个ip是用来上传手机中的照片的，会导致敏感信息的泄露。最开始我是忽略了这部分的，post参数确实太显眼了一点。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZQIqJFHThN53XYFubch4ZwHPYLZ8TQmic2oqBdzRFRsFTTud1iaibZgLibw/640?wx_fmt=other&from=appmsg)

从fiddler中dump出数据，上010恢复成jpg格式我才发现事情的不对劲。虽然这是专门做逆向root过的机器，但是上面还是有一些照片！唉，所以说，淹死的都是会水的。

```
三

伪造请求
```

知道了整体逻辑，接下来就是逆他自己的加密算法了。

每个post的参数都经过了AESUtils.encryptBase64()加密了一次，对称密码，直接看看他代码怎么写的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZpKIPGeIYtuUfd0bN8LHYTxJYfP3oJsFrIO1So6lDicibztn7lrnV1DeA/640?wx_fmt=other&from=appmsg)

顾名思义，AES、Base64，真就只有这两个算法。

唯一上的保护就是密钥了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZUia0vojPPvsSAnE0pEcF4sZyiaNpnw3IzI8m1bhric5sLwvu7DCoB83XA/640?wx_fmt=other&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FcbJP9mWQoINGKozqklkKZadUrrBcYMFvlicPSnrV1nczETlkurz0s4fTCGOLiard41Uh7zUfxgjzw/640?wx_fmt=other&from=appmsg)

虽然这保护和没保护也没什么区别就是了。

那就直接找密钥呗，没什么说的。

```
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.lang.String;
public class Main {
    public static byte[] subBytes(byte[] src, int begin, int count) {
        byte[] bs = new byte[count];
        for (int i = begin; i < begin + count; i++) {
            bs[i - begin] = src[i];
        }
        return bs;
    }
    public static byte[] GetKeySeed(String seed, int keylen) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA1");
        MessageDigest rd = MessageDigest.getInstance("SHA1");
        byte[] keyst = md.digest(seed.getBytes(StandardCharsets.UTF_8));
        return subBytes(rd.digest(keyst), 0, keylen);
    }
    public static void  main(String[] args) throws IOException, NoSuchAlgorithmException {
        String KeyPrivate = "kGfIzsWnQBvW";
        String SaltPrivate = "3s1Zj1hvDi90";
        byte[] arr =new byte[16];
        arr=GetKeySeed(KeyPrivate + SaltPrivate, 16);
        for (int i = 0; i < arr.length; i++) {
             System.out.printf("0x%02X,", arr[i] & 0xFF);
        }
        System.out.println("\n"+arr.length);
    }
}
```

python写出解密脚本：

```
aeskeyarr=[0x4C,0x2C,0x00,0xA9,0x80,0x35,0x96,0x36,0x78,0x7A,0x45,0xD3,0xC9,0xB1,0x1E,0x2E,]
aeskey=b""
#aeskey=0x4C2C00A980359636787A45D3C9B11E2E
for i in aeskeyarr:
    aeskey+=bytes([i])
from Crypto.Cipher import AES
import base64
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\5'
    return str.encode(value)  # 返回bytes
def enc(text):
    text = add_to_16(text)
    aes = AES.new(aeskey,AES.MODE_ECB)
    en_text = base64.b64encode(aes.encrypt(text))
    return en_text.decode()
def dec(text):
    text=text.encode()
    aes = AES.new(aeskey, AES.MODE_ECB)
    tmp=base64.b64decode(text)
    en_text = aes.decrypt(tmp)
    return en_text.decode()
```

找到加密逻辑伪造请求就简单了，直接post就行了，反正是诈骗APP，想怎么来就怎么来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Fic0jo2Hu76p5858SiceSyULWY3RBlPRd8BdhkGbUcsTuarWvpkH94oTYQ265kAssye7GstcV3SDCg/640?wx_fmt=png&from=appmsg)

**看雪ID：touful**

*https://bbs.kanxue.com/user-home-974558.htm*

\*本文为看雪论坛优秀文章，由 touful 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GHxf07w1PYL5PTBo9YHekzTDFlgKmnxOR73qgSmWiamQPpJic8z8x12ZoHNot5zIxzfkTibr9hsxKEg/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564546&idx=2&sn=6446a19937b02964c69ed7054f6d0161&chksm=b18d874886fa0e5efcf867d5e14ba1e0270e78a8c47b25532152b118fd98db8790bd20ace089&scene=21#wechat_redirect)

**# 往期推荐**

1、[UnrealEngine POLYGON 全逆向笔记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564856&idx=1&sn=904dd1ab3f274c3482d65d70601ba81b&chksm=b18d887286fa0164bae684f6bdda0e79672b9286baa1348fce6b41319876e12439c134c0bc5c&scene=21#wechat_redirect)

2、[inlinehook心得分享](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564677&idx=1&sn=dae269b12b2c9ef136e2f46e630304b5&chksm=b18d88cf86fa01d92b25e18c10984f422b68ee7ddb75878730f3f5275d2d48b7a07e67ac95c3&scene=21#wechat_redirect)

3、[PWN入门-2-LibC取物-Ret2LibC](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564568&idx=1&sn=f6f369138f3c2efab15f30973f1a0c49&chksm=b18d875286fa0e44f1ffbaff14a75c7be29743d822403a702d0c87ee9a8a9673c4e2c04f0b6f&scene=21#wechat_redirect)

4、[HITCON CTF 2024 re AntiVirus wp clamav bytecode signature逆向](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564547&idx=2&sn=1ae148ef7d72e7a0707f3c6eddf31dd0&chksm=b18d874986fa0e5f23a08684c44f7dfbe93bd3690b2c0951d2ef70445fbcd45e08d35f5980e4&scene=21#wechat_redirect)

5、[House of orange的进一步利用（house of orange+）](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458564546&idx=1&sn=7f1801ef02129d0459b6dd9da1e97816&chksm=b18d874886fa0e5e3c16e8399befaec775b9c375d8f3f70c187b1fe2a935d54a702c2e168c8e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Go5pAEkLqrtwq3Iwjg6SGicRu4AiayLHCy5peREQesnwkRFbdLWiaSyzgp8KibicUjJykQWiawhZ8LCtFQ/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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