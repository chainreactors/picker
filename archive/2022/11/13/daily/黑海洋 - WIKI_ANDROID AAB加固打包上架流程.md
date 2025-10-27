---
title: ANDROID AAB加固打包上架流程
url: https://blog.upx8.com/3084
source: 黑海洋 - WIKI
date: 2022-11-13
fetch_date: 2025-10-03T22:38:08.224316
---

# ANDROID AAB加固打包上架流程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# ANDROID AAB加固打包上架流程

发布时间:
2022-11-12

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
21407

针对Android aab 程序，需要加固上架GooglePlay的，可以参考下面的流程。

## 加固工具：VirboxProtector。 （加固工具不一定要用Virbox，也可以用其他的。这个只是个辅助）

如何加固：可使用界面工具直接加固，也可以使用命令行进行加固保护。

获取VirboxProtector：[https://shell.virbox.com/apply.html](https://blog.upx8.com/go/aHR0cHM6Ly9zaGVsbC52aXJib3guY29tL2FwcGx5Lmh0bWw)

### 1 VirboxProtector界面保护

#### 1.1函数选项

1、将aab/apk应用拖入到加壳工具中，界面解析aab/apk应用成功。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-4-1024x643.png)

2、选择，添加函数-》选中函数-》右键-》选择虚拟化-》确定。

dex虚拟化是将 DEX 方法中的字节码转换为自定义的虚拟机指令，由自定义解释器解释执行，保护后无法被还原。

VirboxProtector界面会显示默认函数为虚拟化，一般入口类的函数会默认勾选，核心函数需要根据自己需求选择。

> 注：VirboxProtector保护后的方法是独立的，不会因为一个方法选择保护，另一个方法选择不保护而导致程序出问题。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-5-1024x524.png)

#### 1.2 加密选项

包括dex加密、反调试、反注入、签名校验、模拟器检测、root检测、多开检测功能。

**输出信息**

1、默认输出文件名为\*\*\*.ssp.aab，存储在和原aab程序同级目录下。

2、也可以自行修改输出的文件名称，并另存到其他目录中。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-6-1024x644.png)

**设置选项**

1、dex加密，对 DEX 文件整体加密并隐藏，防止反编译。

```
建议：在Google Play上架，建议不勾选dex加密，否则可能提示“账号关联”。
解决：建议选择虚拟化方式保护dex文件里的函数。
```

2、反调试，多种系统相关的检测技术检测调试器，发现调试器后清场退出。

3、反注入，通过双进程 ptrace 守护技术，防止其它进程对 APK 进程附加调试或注入。

4、签名校验，校验开发者签名，防止二次打包。

```
注意：使用“签名校验”功能，必须勾选“启用签名”，才能保护成功。
```

5、模拟器检测，可以防止程序在模拟器中运行。

6、root检测，可以防止程序在root过后的手机上运行。

7、多开检测，可以防止程序多开分身。

**签名设置**

直接选择keystore文件，输入keystore密码、密钥别名和密钥密码。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-7.png)

#### 1.3 资源加密

该功能主要是加密 aab/apk 中的图片，配置，脚本等资源文件，防止被窃取 。

```
选择文件选项处，列表里展示的是支持的资源文件，可全选、可多选、也可自行选择单个文件
1.选择启用，表示选择的资源文件会被保护
2.不选择启用，表示选择的资源文件不会被保护
```

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-8.png)

#### 1.4 so库选项

对 SO 库中的代码段压缩加密，隐藏导入导出函数。

1、点击选择文件，选择自己需要保护的so库。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-9-1024x631.png)

2、隐藏符号表可以隐藏导出符号，根据自己需求选择是否勾选。

```
注：勾选“隐藏符号表”，so库需要全选，反之，so库若选择部分，“隐藏符号表”不建议勾选，否则运行可能会出问题。
```

#### 1.5 保护

**保存配置**

1、以上配置选择完成后，点击“保存选中配置”保存当前文件的设置，当同时保存多个程序的设置时，点击“保存所有配置”选项。

2、保存成功后，在程序（如demo.aab）的同级目录下会生成一个ssp配置文件（如demo.aab.ssp）。

**保护文件**

保存配置成功后，点击“保护选中项目”，保护成功后就i会在程序（如demo.aab）的目录下会生成保护后的程序（如demo.ssp.aab），当同时保护多个程序时，点击“保护所有项目”选项。

### 2 VBP命令行保护

1、VirboxProtector安装包安装完成后，找到virboxprotector\_con.exe的位置。

2、打开终端，运行virboxprotector\_con.exe。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-10.png)

3、使用Virbox Protector界面工具生成配置文件，参考以上设置，若无ssp配置时，则会采用默认配置。

```
命令如下：virboxprotector_con.exe <需要被保护的aab/apk> -o <输出文件的aab/apk>
```

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-11.png)

### 3 GooglePlay商店上架

1、打开Play管理中心，选择相应应用，创建正式版本。

2、“应用签名偏好设置”处进行选择。

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-12.png)

* 让Google管理并保护您的应用和签名密钥（推荐选项）

```
若选择此选项，则aab使用VBP加固时不要勾选“签名校验”，否则Google会重新二次签名导致aab应用运行崩溃
```

* 使用此开发者账号的另一个应用所用的同一密钥

```
1）若已经成功上架过应用程序，则可以进行选择，否则此选项将无法选择。
2）aab加固时若勾选“签名校验”选项，则选择的应用密钥也要和加固aab时所用的密钥文件一致，否则无法使用。
```

![](https://blog.virbox.com/wp-content/uploads/2022/04/image-13.png)

* 从Java密钥库导出并上传密钥

```
1）根据提示操作下载PEPK工具
2）输入命令：java -jar pepk.jar --keystore=D:\Desktop\android_keystore\test_vbp.keystore --alias=vbp.keystore --output=output.zip --include-cert --encryptionkey=eb10fe8f7c7c9df715022017b00c6471f8ba8170b13049a11e6c09ffe3056a104a3bbe4ac5a955f4ba4fe93fc8cef27558a3eb9d2a529a2092761fb833b656cd48b9de6a
3）上传生成的zip文件（--keystore指定的需要和aab加固时所选的keystore一致，才可以使用“签名校验”）
```

* 导出并上传密钥（不使用Java密钥库）

```
若aab加固可以勾选“签名校验”选项，keystore文件和密钥需要保持一致。
```

* 选择退出Play App Signing计划

```
选择此选项，无法上传aab应用。
```

3、上传加固后的aab应用。

4、发布版本。

### 4 aab应用安装

1、可以使用bundletool进行安装。

2、连接设备，执行命令生成apks。

```
命令：java -jar bundletool-all-1.7.0.jar build-apks --bundle=demo.aab --output=demo.apks --connected-device
由于生成apks过程必须要重新签名，所以aab加固时“签名校验”选项不能选择。
```

【注】若要选择签名校验，则生成apks包需要和加壳时设置的签名保持一致。

```
命令：java -jar bundletool-all-1.7.0.jar build-apks --bundle=demo.aab --output=demo.apks --ks=D:\Desktop\android_keystore\sense.jks（签名文件路径） --ks-pass=pass:密码 --ks-key-alias=别名 --key-pass=pass:别名密码 --connected-device
```

3、安装apks。

```
java -jar bundletool-all-1.7.0.jar install-apks --apks=demo.apks
```

4、安装成功，运行设备上的应用即可。

### 5 问题解答

#### 5.1 如何生成签名文件

2、若无keystore文件，可以重新生成。

```
参考命令如下：
keytool -genkey -alias 别名 -keyalg RSA -validity 36500 -keystore 文件命名
```

3、勾选“启用签名”，文件保护后会自动签名。

若不勾选，文件保护后，需要重新签名。

```
aab签名参考命令如下：
jarsigner -digestalg SHA1 -sigalg SHA256withRSA -keystore keystore文件 -storepass "密码" -keypass "别名密码!" "准备签名的文件" "别名"
```

#### 5.2 加固时提示签名失败

问题描述：加固时提示“签名设置错误”或“签名失败，请检查是否安装jdk1.8环境”

排查：点击“日志”->“显示实时日志窗口”，查看错误详细描述，基本上就可判断原因。

**注：要确保环境变量安装的jdk，不能只安装 jre**

1. ![黑核武器](https://gravatar.loli.net/avatar/avatar/10828412a1b70926cf0bb49dd0998dd4?s=32&r=&d=)

   **黑核武器**

   2022-11-20 02:19:01

   [回复](https://blog.upx8.com/3084/comment-page-1?replyTo=26740#respond-post-3084)

   哈哈哈哈

[取消回复](https://blog.upx8.com/3084#respond-post-3084)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")