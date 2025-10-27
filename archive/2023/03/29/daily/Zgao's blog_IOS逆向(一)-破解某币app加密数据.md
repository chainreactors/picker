---
title: IOS逆向(一)-破解某币app加密数据
url: https://zgao.top/ios%e9%80%86%e5%90%91%e4%b8%80-%e7%a0%b4%e8%a7%a3%e6%9f%90%e5%b8%81app%e5%8a%a0%e5%af%86%e6%95%b0%e6%8d%ae/
source: Zgao's blog
date: 2023-03-29
fetch_date: 2025-10-04T10:58:11.378807
---

# IOS逆向(一)-破解某币app加密数据

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# IOS逆向(一)-破解某币app加密数据

* [首页](https://zgao.top)
* [IOS逆向(一)-破解某币app加密数据](https://zgao.top:443/ios%E9%80%86%E5%90%91%E4%B8%80-%E7%A0%B4%E8%A7%A3%E6%9F%90%E5%B8%81app%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE/)

[3月 29, 2023](https://zgao.top/2023/03/)

### IOS逆向(一)-破解某币app加密数据

作者 [Zgao](https://zgao.top/author/zgao/)
在[[逆向](https://zgao.top/category/%E9%80%86%E5%90%91/)](https://zgao.top/ios%E9%80%86%E5%90%91%E4%B8%80-%E7%A0%B4%E8%A7%A3%E6%9F%90%E5%B8%81app%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE/)

最近帮朋友抓取某币圈大佬操盘的数据，但是关键数据被加密了。通过砸壳逆向分析后，用frida来hook解密函数进行抓取。逆向难度相对简单，适合入门学习。

![](https://zgao.top/wp-content/uploads/2023/03/IMG_40A309D4896B-1.jpeg)

文章目录

[ ]

* [难度](#%E9%9A%BE%E5%BA%A6 "难度")
* [工具环境](#%E5%B7%A5%E5%85%B7%E7%8E%AF%E5%A2%83 "工具环境")
* [抓包分析](#%E6%8A%93%E5%8C%85%E5%88%86%E6%9E%90 "抓包分析")
* [IDA分析maco文件](#IDA%E5%88%86%E6%9E%90maco%E6%96%87%E4%BB%B6 "IDA分析maco文件")
* [frida-trace hook CCCrypt](#frida-trace_hook_CCCrypt "frida-trace hook CCCrypt")
* [踩坑-文件生成位置](#%E8%B8%A9%E5%9D%91-%E6%96%87%E4%BB%B6%E7%94%9F%E6%88%90%E4%BD%8D%E7%BD%AE "踩坑-文件生成位置")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## 难度

★☆☆☆☆

## 工具环境

* 越狱IOS 14.4
* frida-ios-dump
* frida-trace
* IDA 7.7
* HTTP Catcher

## 抓包分析

找到某币圈大佬的操盘记录，来到持仓页面进行抓包。

![](https://zgao.top/wp-content/uploads/2023/03/IMG_CF02DC8117B8-1.jpeg)

ios的app抓包最简单的办法就是用HTTP Cathcer，为了方便直接转发到mac上。

![](https://zgao.top/wp-content/uploads/2023/03/image-19-1024x450.png)

可以看到请求参数是没有加密的，但是返回的关键数据都被加密了，但是无法判断加密算法的类型。

## IDA分析maco文件

这里使用frida-ios-dump进行砸壳，砸壳的过程就不说了。

![](https://zgao.top/wp-content/uploads/2023/03/image-20-1024x534.png)

找到maco可执行文件，这类文件很明显的特征是没有后缀名。拖入IDA中分析关键加解密函数。

![](https://zgao.top/wp-content/uploads/2023/03/image-21-1024x522.png)

搜索decrypt关键字，很容易就定位到解密函数位置，从函数名就能看出是使用的AES加密，所以问题就简单多了。

不管代码如何封装，最终肯定是调用IOS官方的加解密函数，所以直接hook CCCrypt即可，该函数的主要参数如下。

```
CCCryptorStatus CCCrypt(
    CCOperation op,          /* 加密：kCCEncrypt = 0，解密：kCCDecrypt = 1 */
    CCAlgorithm alg,        / 加密算法，如kCCAlgorithmAES128等 /
    CCOptions options,      / 加密选项，如kCCOptionPKCS7Padding等 /
    const void key,       / 加密密钥 /
    size_t keyLength,      / 加密密钥长度 /
    const void iv,         / 可选的初始化向量 /
    const void dataIn,     / 可选的输入数据 /
    size_t dataInLength,    / 输入数据长度 /
    void dataOut,          / 输出数据 /
    size_t dataOutAvailable,  / 输出数据可用长度 /
    size_t dataOutMoved)   / *实际输出数据长度 */
```

## frida-trace hook CCCrypt

```
frida-ps -U
```

查看当前应用的包名。

![](https://zgao.top/wp-content/uploads/2023/03/image-22-1024x607.png)

下面就是直接上frida进行hook关键解密函数。

```
frida-trace -FU -i CCCrypt
```

因为当前已经在前台运行了程序，所以就不用指定包名，直接hook即可。

![](https://zgao.top/wp-content/uploads/2023/03/image-23-1024x276.png)

执行frida-trace之后会自动生成一个模板，需要手动修改。

```
{
  onEnter: function (log, args, state) {
    log("进入加密函数了。。。。")
    log('CCCrypt(' +
      'op=' + args[0] +
      ', alg=' + args[1] +
      ', options=' + args[2] +
      ', key=' + args[3] +
      ', keyLength=' + args[4] +
      ', iv=' + args[5] +
      ', dataIn=' + args[6] +
      ', dataInLength=' + args[7] +
      ', dataOut=' + args[8] +
      ', dataOutAvailable=' + args[9] +
      ', dataOutMoved=' + args[10] +
    ')');
    //保存参数
    this.operation   = args[0]
    this.CCAlgorithm = args[1]
    this.CCOptions   = args[2]
    this.keyBytes    = args[3]
    this.keyLength   = args[4]
    this.ivBuffer    = args[5]
    this.inBuffer    = args[6]
    this.inLength    = args[7]
    this.outBuffer   = args[8]
    this.outLength   = args[9]
    this.outCountPtr = args[10]
    //this.operation == 0 代表是加密
    if (this.operation == 0) {
      log("进入加密函数了......")
      //打印加密前的原文
        console.log("In buffer:")
        console.log(hexdump(ptr(this.inBuffer), {
            length: this.inLength.toInt32(),
            header: true,
            ansi: true
        }))
        //打印密钥
        console.log("Key: ")
        console.log(hexdump(ptr(this.keyBytes), {
            length: this.keyLength.toInt32(),
            header: true,
            ansi: true
        }))
        //打印 IV
        console.log("IV: ")
        console.log(hexdump(ptr(this.ivBuffer), {
            length: this.keyLength.toInt32(),
            header: true,
            ansi: true
        }))
    }
  },

  onLeave: function (log, retval, state) {
    if (this.operation == 1) {
      // Show the buffers here if this a decryption operation
      log("进入解密函数了......")
      console.log(hexdump(ptr(this.outBuffer), {
          length: Memory.readUInt(this.outCountPtr),
          header: true,
          ansi: true
      }))
      console.log("Key: ")
      console.log(hexdump(ptr(this.keyBytes), {
          length: this.keyLength.toInt32(),
          header: true,
          ansi: true
      }))
      console.log("IV: ")
      console.log(hexdump(ptr(this.ivBuffer), {
          length: this.keyLength.toInt32(),
          header: true,
          ansi: true
      }))
    }
  }
}
```

这段代码可以当做模板直接复用。

执行frida-trace后，来到被需要抓取的页面，就会触发解密函数。此时通过hexdump解密出来的数据就是我们需要抓取的了。

![](https://zgao.top/wp-content/uploads/2023/03/image-24-1024x599.png)

但是hexdump只是方便我们查看，如何才能直接dump字符串的内容呢？这里就需要用到Memory.readCString()来读取字符数据。

同时根据需要，最终的目的是为了抓取数据。那么我们可以把解密后的数据写入到文件中进行保存。修改代码如下：

```
  onLeave: function (log, retval, state) {
    if (this.operation == 1) {
      log("进入解密函数了......")
      const jsonData = Memory.readCString(ptr(this.outBuffer));
      const fileName = Math.random().toString(36).substring(7) + ".json";
      const filePath = '/tmp/coin2/' + fileName
      log(filePath)
      log(jsonData)
      var file = new File(filePath, "w");
      file.write(jsonData);
      file.flush();
      file.close();
    }
  }
```

![](https://zgao.top/wp-content/uploads/2023/03/image-25-1024x667.png)

## 踩坑-文件生成位置

由于要保存解密后的数据，所以需要写文件。因为是在mac上执行的命令，所以一开始我误以为生成文件的位置也是在本机上。于是开始debug，发现写入文件的代码既不报错也找不到生成后的文件。在这里浪费了很多时间【我裂开】。

虽然修改代码和执行frida的命令是在mac上，但是脚本最终是在ios设备上执行的，所以frida代码中生成的文件也是在ios上。

![](https://zgao.top/wp-content/uploads/2023/03/image-26-1024x484.png)

目标是抓取一个用户的操盘数据，所以也不用写脚本，直接手动刷一遍即可dump所有交易记录了。

## 总结

本次IOS的逆向过程非常简单，主要是目标app没有做越狱检测，也没有使用魔改的加密算法，适合新手入门学习。

Post Views: 2,690

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 2条评论

###### test 发布于3:38 下午 - 4月 9, 2024

请问这是什么app呀，想拿来练手

[回复](https://zgao.top/ios%E9%80%86%E5%90%91%E4%B8%80-%E7%A0%B4%E8%A7%A3%E6%9F%90%E5%B8%81app%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE/?replytocom=7663#respond)

###### 匿名 发布于8:06 上午 - 3月 29, 2023

666666

[回复](https://zgao.top/ios%E9%80%86%E5%90%91%E4%B8%80-%E7%A0%B4%E8%A7%A3%E6%9F%90%E5%B8%81app%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE/?replytocom=5079#respond)

### 发表评论 [取消回复](/ios%E9%80%86%E5%90%91%E4%B8%80-%E7%A0%B4%E8%A7%A3%E6%9F%90%E5%B8%81app%E5%8A%A0%E5%AF%86%E6%95%B0%E6%8D%AE/#respond)

Δ

版权©2020 Author By : Zgao