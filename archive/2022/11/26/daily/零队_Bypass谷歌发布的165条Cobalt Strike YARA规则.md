---
title: Bypass谷歌发布的165条Cobalt Strike YARA规则
url: https://mp.weixin.qq.com/s?__biz=MzU2NTc2MjAyNg==&mid=2247484869&idx=1&sn=f7078c93be2f1341f443ff5d02a37eb1&chksm=fcb78740cbc00e56295e1075812d6c91df6b7be6a2be33e59de415d035c5cdeff3084182e637&scene=58&subscene=0#rd
source: 零队
date: 2022-11-26
fetch_date: 2025-10-03T23:50:00.379072
---

# Bypass谷歌发布的165条Cobalt Strike YARA规则

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhxIaia4kwz4nWH64YlfjibPrBvR6eHtzosp3t1ce88IVYCSdmcico4H5Skw/0?wx_fmt=jpeg)

# Bypass谷歌发布的165条Cobalt Strike YARA规则

原创

归零

零队

## 前言

近日，谷歌云威胁情报团队开源了一组YARA规则，以帮助防御者标记和识别Cobalt Strike及其版本。(https://cloud.google.com/blog/products/identity-security/making-cobalt-strike-harder-for-threat-actors-to-abuse)

## 试一波

项目地址：https://github.com/chronicle/GCTI/tree/main/YARA

使用自己的加载器上线，写个脚本批量扫一下：

```
import os

path = "C:\Users\xxx\Desktop\YARA\CobaltStrike"

def scan(path):

    file_list = os.listdir(path)

    for file in file_list:
        fullPath = os.path.join(path,file)
        cmd = "C:\Users\xxx\Desktop\YARA\yara64.exe " + fullPath + " 11200"
        result = os.popen(cmd).read()
        if result:
            print(result)

if __name__ == '__main__':
    scan(path)
```

结果如下（sleep和执行命令前后结果一致）：

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhxvN0T200N6cw0URFGv8ycWHZ3L0k9bNZcBTR9q4s9d2y59Tt6SopZNw/640?wx_fmt=png)

命中两条规则：

```
CobaltStrike__Sleeve_Beacon_x64_v4_5_variant

CobaltStrike__Sleeve_BeaconLoader_MVF_x64_o_v4_3_v4_4_v4_5_and_v4_6
```

嗯，确实精准，下面开始bypass……

## CobaltStrike\_\_Sleeve\_Beacon\_x64\_v4\_5\_variant

这条规则出自：CobaltStrike\_\_Resources\_Beacon\_Dll\_All\_Versions\_MemEnabled.yara

具体如下：

```
rule CobaltStrike__Sleeve_Beacon_x64_v4_5_variant
{
  meta:
    desc="Cobalt Strike's sleeve/beacon.x64.dll Versions 4.5 (variant)"
    rs1 = "8f0da7a45945b630cd0dfb5661036e365dcdccd085bc6cff2abeec6f4c9f1035"
    author = "gssincla@google.com"

  strings:
    /*
      41 B8 01 00 00 00 mov     r8d, 1
      8B D0             mov     edx, eax
      49 8B CA          mov     rcx, r10
      48 83 C4 28       add     rsp, 28h
      E9 E8 AB FF FF    jmp     sub_1800115A4
      8B D0             mov     edx, eax
      49 8B CA          mov     rcx, r10
      E8 1A EB FF FF    call    f_UNK__Command_92__ChangeFlag
      48 83 C4 28       add     rsp, 28h
    */
    $version_sig = { 41 B8 01 00 00 00 8B D0 49 8B CA 48 83 C4 28 E9 E8 AB FF FF
                     8B D0 49 8B CA E8 1A EB FF FF 48 83 C4 28 }

    /*
      80 34 28 ??       xor     byte ptr [rax+rbp], 2Eh
      48 FF C0          inc     rax
      48 3D 00 10 00 00 cmp     rax, 1000h
      7C F1             jl      short loc_180018E1F
    */

    $decoder = { 80 34 28 ?? 48 FF C0 48 3D 00 10 00 00 7C F1 }

  condition:
    all of them
}
```

特征出自beacon.x64.dll，改dll特征需要注意一点：不能影响程序功能，那么最简单的方式就是找那些两条指令交换顺序是不影响的

比如$version\_sig中`mov edx, eax`和`mov rcx, r10`，可参考我之前的文章（[https://mp.weixin.qq.com/s/5HYELRGm6XClvJ1ZHBHVKg](https://mp.weixin.qq.com/s?__biz=MzU2NTc2MjAyNg==&mid=2247484793&idx=1&sn=7fe81d74d8ff8ab0cd8e791c6204c5d7&scene=21#wechat_redirect)）

接下来掏出心爱的ida，找到对应的地方：

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhxSmzicwQSicbwKFJ5WLB5mX46W1ic74R6CYU6dIUZCLpovmw3L1Ge2b6CA/640?wx_fmt=png)

修改后：

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhx7TsClqndrWLFxcjscI028asn27NuPt6icuvmxo2UgmQ9DmohoxEWwTg/640?wx_fmt=png)

而$decoder中检测的是配置信息的xor功能，可参考我之前的文章（[https://mp.weixin.qq.com/s/fhcTTWV4Ddz4h9KxHVRcnw](https://mp.weixin.qq.com/s?__biz=MzU2NTc2MjAyNg==&mid=2247484689&idx=1&sn=8cf9c031f3d926c155ee5c018941b416&scene=21#wechat_redirect)）

```
80 34 28 ??       xor     byte ptr [rax+rbp], 2Eh
48 FF C0          inc     rax
48 3D 00 10 00 00 cmp     rax, 1000h
7C F1             jl      short loc_180018E1F
```

这里段程序只有4行，看上去是没法用之前的方法改了，实际上进行一个简单分析后，同样是能改掉特征的，而且比较简单，汇编比较熟的童鞋应该很快就能发现，这里就不公开了，留给大家思考 o(\*≧▽≦)ツ

验证一下，由于rule CobaltStrike\_\_Sleeve\_Beacon\_x64\_v4\_5\_variant是all of them，而$version\_sig已经bypass了，所以这里改成$version\_sig or $decoder

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhx90e9jhXiazjbm62xibvkMTbbykoM9ysZSiaxjqk458icz3Xff2veaMRQGQ/640?wx_fmt=png)

成功bypass

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhxWroeNNeK0M5CLlbjnLzUBtduoCfanIrVEWZqNI3ZG4hAX6GSNwKewg/640?wx_fmt=png)

## CobaltStrike\_\_Sleeve\_BeaconLoader\_MVF\_x64\_o\_v4\_3\_v4\_4\_v4\_5\_and\_v4\_6

这条规则出自：CobaltStrike\_\_Sleeve\_BeaconLoader\_all.yara

具体如下：

```
rule CobaltStrike__Sleeve_BeaconLoader_MVF_x64_o_v4_3_v4_4_v4_5_and_v4_6
{
  meta:
    desc="Cobalt Strike's sleeve/BeaconLoader.MVF.x64.o (MapViewOfFile) Versions 4.3 through at least 4.6"
    rs1 = "9d5b6ccd0d468da389657309b2dc325851720390f9a5f3d3187aff7d2cd36594"
    author = "gssincla@google.com"

  strings:
    /*
      C6 44 24 58 4D mov     [rsp+98h+var_40], 4Dh ; 'M'
      C6 44 24 59 61 mov     [rsp+98h+var_3F], 61h ; 'a'
      C6 44 24 5A 70 mov     [rsp+98h+var_3E], 70h ; 'p'
      C6 44 24 5B 56 mov     [rsp+98h+var_3D], 56h ; 'V'
      C6 44 24 5C 69 mov     [rsp+98h+var_3C], 69h ; 'i'
      C6 44 24 5D 65 mov     [rsp+98h+var_3B], 65h ; 'e'
      C6 44 24 5E 77 mov     [rsp+98h+var_3A], 77h ; 'w'
      C6 44 24 5F 4F mov     [rsp+98h+var_39], 4Fh ; 'O'
      C6 44 24 60 66 mov     [rsp+98h+var_38], 66h ; 'f'
      C6 44 24 61 46 mov     [rsp+98h+var_37], 46h ; 'F'
      C6 44 24 62 69 mov     [rsp+98h+var_36], 69h ; 'i'
      C6 44 24 63 6C mov     [rsp+98h+var_35], 6Ch ; 'l'
      C6 44 24 64 65 mov     [rsp+98h+var_34], 65h ; 'e'
    */

    $core_sig = {
      C6 44 24 58 4D
      C6 44 24 59 61
      C6 44 24 5A 70
      C6 44 24 5B 56
      C6 44 24 5C 69
      C6 44 24 5D 65
      C6 44 24 5E 77
      C6 44 24 5F 4F
      C6 44 24 60 66
      C6 44 24 61 46
      C6 44 24 62 69
      C6 44 24 63 6C
      C6 44 24 64 65
    }

    // These strings can narrow down the specific version
    //$ver_43 = { 96 2C 3E 60 }         // Version 4.3
    //$ver_44_45_46 = { D2 57 86 5F }   // Versions 4.4, 4.5, and 4.6

  condition:
    all of them
}
```

cs会根据profile中allocator选项选择相应的反射加载器，对应三种申请内存的方式：HeapAlloc、MapViewOfFile 和 VirtualAlloc

这里我使用的是MapViewOfFile，再次拿起心爱的ida，打开BeaconLoader.MVF.x64.o，找到对应的位置：

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhx7ugU3gjIYPttwqdLRxQYEyJRlSv19ic982WLibcGSbOhj3Wl8nJ1CBMA/640?wx_fmt=png)

这可太简单了，直接把顺序打乱就行，不影响

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhxk5FoEic5iavLIymHraRicEB7FZvs2S63h0kcR7VfPe7a1gJFySNO5AGAw/640?wx_fmt=png)

验证一下，全部bypass：

![](https://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvcfrKx62vAJK6gAlemsBMhx2zmGEuvIJ9kHHAicD68hI66IiaD4AthK7pnLaVquHcWzjHur6PSBwEicg/640?wx_fmt=png)

## 结语

每只CS的体质不同（profile、linstener、架构、魔改等），命中的规则也不同，本文只是抛砖引玉。

不要给我提什么：哎呀你还用cs啊，我们都换别的啦，我们都自研啦巴拉巴拉，我只是觉得对于很多平民玩家，缝缝补补能用，不就行了吗？

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvdDYpdiaricAd5y5ibdKbyQXzYT5KdD5Rr4u2LovtPjN4ib62qR6cia02C2ssbBKXBjyYjS1TGY6b51sbQ/0?wx_fmt=png)

零队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qr5uyVXdEvdDYpdiaricAd5y5ibdKbyQXzYT5KdD5Rr4u2LovtPjN4ib62qR6cia02C2ssbBKXBjyYjS1TGY6b51sbQ/0?wx_fmt=png)

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