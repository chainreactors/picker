---
title: 车机OTA包解密
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589307&idx=1&sn=f7c4f8fab0e756cd0249e052d5c9e9fe&chksm=b18c28f186fba1e7d1d9898dfb4a59f2e0f731ef62a963f087dce8c4aadaf8b4d9a194f654fc&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-06
fetch_date: 2025-10-06T20:36:06.783563
---

# 车机OTA包解密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX7jVo19yQEOBRCNSVb3q0QKbF4T1yWyKmCJ0lghrFfgFgrFZkHg1gng/0?wx_fmt=jpeg)

# 车机OTA包解密

ty1937

看雪学苑

我的车二代车机系统终于更新了，上了高德新版，有了红绿灯倒计时，盼了很久，终于更新了。

我就想着将OTA包里面的apk，直接提取出来，升级就行了，不需要更新车机系统了，结果失败！

拿到了心心念的OTA升级包，一打开。

哦豁~~~~

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXWdbZjsXNRZic9PicFDkibUhM8hXzCQMP5t9jopicadRQaib2lIibRPGTic00A/640?wx_fmt=other&from=appmsg)

它竟然做了加密的，好惨。

我就想着，既然这里做了加密，那么车机系统在拿到包后，肯定也需要进行解密才能去安装呀，于是带着好奇去看了看。

```
一

获取升级apk
```

##

在车机交流群里面，顺利拿到了负责车机升级的apk，拖进jadx 里面，找关键字，HuOs。

还真找到了：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXLrU4tZyZ5CnEvsPUnf01M2Pkcs91oz9ugNXFnj9RQApzlSd4qfibtibw/640?wx_fmt=other&from=appmsg)

这不就是我升级的路径，和包格式嘛 .zip

跟着调用栈一路静态分析，结果追到了解密方法：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX99MELLQPvvVXSibM3vFWpUZfGnnGfHhlguibIrBAYzMzTXiaiaVvXbAqBQ/640?wx_fmt=other&from=appmsg)

这里发现 包被进行了 "AES/CBC/PKCS5Padding" 的加密，车机系统拿到文件，进行解密后，再安装。

```
二

获取解密Key
```

##

又上一个步骤发现，是通过获取 "/system/bin/sd\_ivi\_data/ckey"  的值，然后使用 未宸 解密，对这个文件进行解密，获取前16 字节，作为系统包的aes key。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX4WawQgmY8FNhOo51Egj4RsZMEY3ltLicPeoibY4QdoUMUYdeZygf4hJA/640?wx_fmt=other&from=appmsg)

想要解密这个就得两个步骤：

1、获取到这个ckey 这个文件 （万能的车友群 把文件给了我）

2、拿到 whiteBox.decrypt 的代码实现逻辑 （万能的车友群 把文件给了我）

步骤2走了一些弯路。起初以为 whiteBox.decrypt  这个代码的实现是放在 boot-framework.vdex 、最后通过搜索，发现是放在boot-ext.vdex 里面的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXvVws6qE4Z13DeT7ibjIIP4X48A3sOBibDKwVnOIWAcKU4rb8lgumI8UQ/640?wx_fmt=other&from=appmsg)

这里就需要使用两个工具：

1.vdex 转为cdex

2.再将 cdex 转为dex

最终打开：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXwFonzymBibVFntpqLeBPu91Qx4090sZ6aeKlsooTTHY9mPoU57WiaX2A/640?wx_fmt=other&from=appmsg)

解密方法则是将文件的值，与一个key ，进到native 里面计算出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXFWlmMTk2NFUHv9DjH70SgbYWZLvgo6IkZ0Qxa4sDmChibSethmeBZibw/640?wx_fmt=other&from=appmsg)

那么我们还需要获取到这个token。

```
三

获取解密Key的解密token
```

##

通过静态分析，获取token的 通过获取升级 apk 下的一些文件值，在native 里面进行判断，最后返回出结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX0nzECd1gOwsdKluIx8qMJibgBSaGFXEYFUWKmI8mX3Vx0NUibqribibomg/640?wx_fmt=other&from=appmsg)

起初，我以为需要在native 里面进行计算，最后反编译进去一看。

好家伙只是将获取的数据进行了对比，然后直接返回token，想复杂了。

```
int __fastcall Java_com_weichen_whitebox_encrytion_WhiteBoxNativeImpl_connectionToNativeVerifyDigest(JNIEnv *a1, int a2, int a3, size_t a4, int a5, int a6, size_t a7, int a8, int a9, int a10, int a11)
{
  _DWORD *v13; // r9
  const char *v14; // r5
  const char *v15; // r10
  int v16; // r0
  const char *v17; // r5
  jbyte *v18; // r4
  jbyte *v19; // r6
  jstring (*v20)(JNIEnv *, const char *); // r2
  const char *v21; // r1
  const char *v23; // r4
  void *v24; // r9
  const char *v25; // r10
  jbyte *v26; // r4
  jbyte *v27; // r5
  const char *v28; // [sp+1Ch] [bp-2Ch]
  const char *v29; // [sp+24h] [bp-24h]

  v13 = malloc(0x20u);
  v14 = (*a1)->GetStringUTFChars(a1, a9, 0);
  v15 = (*a1)->GetStringUTFChars(a1, a5, 0);
  if ( !j_readFileFromApk(v14, v15, v13) )
  {
    _android_log_print(4, "LeosinAcsctl: digest", "can't find file, LINE = %d", 275);
LABEL_8:
    v20 = (*a1)->NewStringUTF;
    v21 = "can't find file";
    return (int)v20(a1, v21);
  }
  v29 = v14;
  v16 = j_calculateDigest(a1, v13, a10);
  if ( !v16 || (v17 = (const char *)v16, !v13[4]) )
  {
    _android_log_print(4, "LeosinAcsctl: digest", "unsupproted signAlg, LINE = %d", 281);
    v20 = (*a1)->NewStringUTF;
    v21 = "unsupproted signAlg";
    return (int)v20(a1, v21);
  }
  v18 = (*a1)->GetByteArrayElements(a1, a3, 0);
  v19 = (jbyte *)malloc(a4);
  qmemcpy(v19, v18, a4);
  if ( strncmp(v17, v19, a4) )
  {
    _android_log_print(4, "LeosinAcsctl: digest", "mainfiestFileDigest is wrong, LINE = %d", 290);
    v20 = (*a1)->NewStringUTF;
    v21 = "mainfiestFileDigest is wrong";
    return (int)v20(a1, v21);
  }
  (*a1)->ReleaseByteArrayElements(a1, (jbyteArray)a3, v18, 2);
  (*a1)->ReleaseStringUTFChars(a1, (jstring)a5, v15);
  free(v19);
  free(v13);
  v23 = (*a1)->GetStringUTFChars(a1, a8, 0);
  v24 = malloc(0x20u);
  if ( !j_readFileFromApk(v29, v23, v24) )
  {
    _android_log_print(4, "LeosinAcsctl: digest", "can't find file, LINE = %d", 301);
    goto LABEL_8;
  }
  v28 = v23;
  v25 = (const char *)j_calculateDigest(a1, v24, a11);
  v26 = (*a1)->GetByteArrayElements(a1, a6, 0);
  v27 = (jbyte *)malloc(a4);
  qmemcpy(v27, v26, a7);
  __android_log_print(4, "LeosinAcsctl: digest", "dexClassDigestLen is %d", a7);
  __android_log_print(4, "LeosinAcsctl: digest", "dexClassDigestArr is %s", v27);
  __android_log_print(4, "LeosinAcsctl: digest", "dexClassDigest is %s", v25);
  if ( !strncmp(v27, v25, a7) )
  {
    (*a1)->ReleaseByteArrayElements(a1, (jbyteArray)a6, v26, 2);
    (*a1)->ReleaseStringUTFChars(a1, (jstring)a8, v28);
    free(v27);
    free(v24);
    (*a1)->ReleaseStringUTFChars(a1, (jstring)a9, v29);
    v20 = (*a1)->NewStringUTF;
    v21 = "@ABCDEFG";
  }
  else
  {
    _android_log_print(4, "LeosinAcsctl: digest", "can't find file, LINE = %d", 313);
    v20 = (*a1)->NewStringUTF;
    v21 = "dexclass digest is wrong";
  }
  return (int)v20(a1, v21);
}
```

#

```
四

解密Key
```

##

#

# 前面既然已经拿到了 token ,那我们直接使用Unidbg 将 token 值，和ckey 的值传入，计算出结果即可。

```
public byte[] key() {
        String y2 = "decryptUsingNative([BLjava/lang/String;)[B";
        //参数1 ckey的值，参数2 token 值
        DvmObject<?> dvmObject = UmeJni.callStaticJniMethodObject(emulator, y2, Base64.getDecoder().decode("j3AR4u/J4hedDbN8gkrqbbj7ibVPSX695NCfhVxSQWc="), "@ABCDEFG");
        return (byte[]) dvmObject.getValue();
    }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX8AQIRz5pcUUXziaiaicYWxLqjVibD8amHb7G2Iku5S19dibkZGmwS9qPJrg/640?wx_fmt=other&from=appmsg)

```
五

解密
```

拿到key 了，返回第一步，使用AES/CBC/PKCS5Padding 解密，获得ota包。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXYTU5y6iadWlBqVWxOe8luRFkp3OnwRzRHJrADu50PJEnIZsVXTNpZaw/640?wx_fmt=other&from=appmsg)

然后使用 开源工具payload-dumper-go  将 payload.bin 提取出 system.img 即可：就拿到了高德地图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX7MT3yEISHVqB2ibrDx1kz0p4S9B2PKWEu868vCic9V3GhbEAjoZXq3lQ/640?wx_fmt=other&from=appmsg)

```
六

总结
```

##

整体弄下来，花了一下午的时间，最开始想的太难了，动手起来，多亏了万能的车群提供了相应的文件进行分析，万事开头难，做起来就顺了。整体分析难道不大，都是一些基础的调用，和简单的知识点结合就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXP6Qic0qWVNK2OYSBd1hggaxWeMuN3jfxmvtR4IbDXUmHlcaWbldon3Q/640?wx_fmt=png&from=appmsg)

看雪ID：ty1937

*https://bbs.kanxue.com/user-home-857508.htm*

\*本文为看雪论坛优秀文章，由 ty1937 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=21#wechat_redirect)

3、[野蛮fuzz：提升性能](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm=b18dc04386fa49557abc8c7e6ce3410dd4042ed88635c48961fda72b7fa4425698e56bb86ff6&scene=21#wechat_redirect)

4、[关于安卓注入几种方式的讨论，开源注入模块实现](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579138&idx=1&sn=fef09513ae9f594e68a503f69a312f4f&chksm=b18dc04886fa495e440990cd2dbddb24693452562e53bd8cb565063ddee921b7e288477f4eea&scene=21#wechat_redirect)

5、[2024年KCTF水泊梁山-反混淆](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579017&idx=2&sn=a97dacde8a6c913108999da8a96a667f&chksm=b18dc0c386fa49d57ce9f0ce6923690d6eb8efb3ccb8032e8c6b923184af3dd29b1b4471f9a2&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617p...