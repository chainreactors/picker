---
title: 利用Framework Patch过掉BL锁状态检测
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458565095&idx=1&sn=9e066fba7b187aee2d84c91d2a3f9bf4&chksm=b18d896d86fa007b55404112d65165f688d2c0541ea52919fd9fd14f5d095f9913245b25a9c7&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-29
fetch_date: 2025-10-06T17:41:13.446048
---

# 利用Framework Patch过掉BL锁状态检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm92sejDicRva9sUemobAh9jbMs2hZicRezxFZDWWQGzxVJYtiaxa7b257EQ/0?wx_fmt=jpeg)

# 利用Framework Patch过掉BL锁状态检测

sffool

看雪学苑

```
一

介绍
```

该项目源自Github外国大佬。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9ibKc1B1rUqBjWVicqiaI6bv4tQIBmkZ2wfY1q3yzibib6bwSk8x3Q40YibtA/640?wx_fmt=png&from=appmsg)

**项目链接：**

GitHub - chiteroman/FrameworkPatch: Modify framework.jar to build on system level a valid certificate chain

（https://github.com/chiteroman/FrameworkPatch）

PS：
原项目自带教程，但是只有英文版教程，并且教程详尽程度对我这样的小白不是很友好，所以写了这篇小白向的教程。大佬or有安卓开发经验的师傅可以直接看Github原项目。

## 作用

对于已解锁BL的手机，这个项目通过对手机根目录下`/system/framework/framework.jar`这个文件进行修改来过掉BL锁状态检测。

如果仅利用项目自带的keybox，可以过掉非硬件检测or密钥检测的BL锁状态验证，对付大部分软件，是没有问题的，而且目前有BL锁检测的软件其实很少。
如果你有谷歌下发的keybox，那么利用该项目，你可以近乎完美的过掉BL锁状态检测。

注意，对`TEE损坏`的手机没有效果！！！例如OPPO/一加等品牌手机，解锁BL就会使TEE假死。

本教程只有前者，就是教如何使用该项目。

我也不知道如何向谷歌申请下发keybox（我还是一个无安卓开发经验的小白）。

## 存在的问题

◆目前检测BL的软件还是较少

◆完美隐藏BL状态需要谷歌下发的密钥

◆与`Kitsune Magisk`的`Su List`有冲突

◆和`Shamiko`模块有冲突

◆影响性能？

◆未知的问题

## 研究价值

目前，有些安卓游戏是存在检测BL状态的。
以此为依据在设备上使用不同严格程度的检测方案。
之后，或许会有更多的软件对BL锁状态进行检测。
故，还是有一些研究价值。

```
二

教程
```

**所需设备和工具：**

◆1台已Root的安卓手机（装有Magisk/Apatch等）

◆Termux 或者 ZeroTermux

◆MT管理器和密钥认证APP

◆`Framework Patch`Github链接（https://github.com/chiteroman/FrameworkPatch）及`Framework Patcher Go`GitHub链接（https://github.com/changhuapeng/FrameworkPatcherGO）

◆Magisk模块模板`framework-modify`

◆科学上网

部分所需工具：
百度网盘（https://pan.baidu.com/s/1LtwGXQn5NOYGoPuGIyq3fA?pwd=ew6v）
有FrameworkPatcherGO，模块模板，密钥认证APP
其他工具请自行准备

该教程内容不需要电脑就可以实现
Magisk模块模板我会提供附件（非本人制作）

**该项目有风险，请做好救砖的准备！！！**

## 内容预览

1.配置Termux编译环境。

2.使用Termux编译所需`dex。`

3.利用`Framework Patcher Go`模块自动修改`framework.jar`中的`dex`（部分手机到此就已结束）。

4.手动修改`framework.jar`中的`dex`（部分手机的framework.jar无法使用`FrameworkPatcherGo`模块自动修改并安装）并制作模块。

## 效果预览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9PSfDibIfZbjIXl1CmvUtYsrzVpFsic3pDozvNMic9IKe1Mf8ibib9bog2pA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9bdrNGPUBpLicsglxISnrn9ibugN1hGzn1WUSs96nrzLeRtlKPxwut1Pg/640?wx_fmt=png&from=appmsg)

第一张图为安装前，第二张图为安装后（使用项目自带证书，故会显示来自AOSP的根证书，非完美隐藏）。

## 配置Termux编译环境

###

### 换国内源

使用Termux执行

```
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list
pkg update
```

###

### 安装Java和配置Android编译环境

大量参考该文章（https://blog.csdn.net/Mingyueyixi/article/details/136014207）。

如果之后想在手机上利用Termux编译APK项目的，推荐观看下。

```
#安装git
pkg install git -y
#安装openssh
pkg install openssh -y
#安装Java—sdk—17
pkg install openjdk-17 -y
```

请科学上网：

```
curl -O https://googledownloads.cn/android/repository/commandlinetools-linux-11076708_latest.zip

ANDROID_HOME=~/android/sdk
mkdir -p $ANDROID_HOME/latest
unzip `ls |grep "commandlinetools-linux.*_latest.zip"` -d $ANDROID_HOME
# cmdline-tools 的产物需要移动到cmdline-tools/latest目录中，这是android sdk固定的路径组织形式
# 压缩包没有包含在latest文件夹中，自己移动一下
mv $ANDROID_HOME/cmdline-tools/* $ANDROID_HOME/latest
mv $ANDROID_HOME/latest $ANDROID_HOME/cmdline-tools
```

MT管理器打开`/data/user/0/com.termux/files/home/`

创建文件，名字是`.bashrc`

填入以下内容：

```
echo "用户："$(whoami)

if pgrep -x "sshd" >/dev/null
  then
   echo
   #echo "sshd运行中..."
  else
    sshd
    echo "自动启动sshd"
fi
export ANDROID_HOME=~/android/sdk
export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$PATH
```

Termux执行如下命令：

```
cd ~
source .bashrc
```

然后彻底关闭Termux，重新打开。继续，由于我们只需要编译，故执行第三条命令即可。

```
#查看sdk列表
#sdkmanager --list
#安装安卓14平台开发工具
#sdkmanager --install "platforms;android-34"
#安装支持安卓14的构建工具
sdkmanager --install "build-tools;34.0.0"
```

接下来，我们下载arm版本的sdk工具（google编译的安卓sdk没有arm版本 ）。

```
cd ~
curl -LJO https://github.com/lzhiyong/android-sdk-tools/releases/download/34.0.3/android-sdk-tools-static-aarch64.zip

#根据构架选择，一般用上面那个就行了，如果更改了，需要把解压命令也更改下
#curl -LJO https://github.com/lzhiyong/android-sdk-tools/releases/download/34.0.3/android-sdk-tools-static-arm.zip

unzip android-sdk-tools-static-aarch64.zip -d ./armtools
# 下载的是34版本的，所以，覆盖到34版本的目录
mkdir -p ~/android/sdk/platform-tools
cp -p ./armtools/build-tools/*  ~/android/sdk/build-tools/34.0.0
cp -p ./armtools/platform-tools/*  ~/android/sdk/platform-tools
```

git项目

注意科学上网

```
cd ~
git clone https://github.com/chiteroman/FrameworkPatch.git
```

##

## 编译dex

这里需要科学上网。并且，执行所需时间较长，耐心等待

最后，这里执行完了，还不算完。会有报错，请勿担心。

```
cd ./FrameworkPatch
echo "sdk.dir=$ANDROID_HOME" > local.properties
chmod +x ./gradlew
./gradlew build
```

执行后，你会看到如下报错：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm92cshibjv5Ntg8ENsFZ3iaGnibEymcFLtqZCjpoxuAR0JZHUT09x7VfElQ/640?wx_fmt=png&from=appmsg)

不急，执行以下命令替换aapt2。

```
TARGET="/data/user/0/com.termux/files/home/.gradle/caches/transforms-4"
find "$TARGET" -type f -name "aapt2" | while read -r aapt2_file; do
    cp -f ~/android/sdk/build-tools/34.0.0/aapt2 "$aapt2_file"
done
```

接下里继续编译。

```
./gradlew assembleRelease
cp -f app/build/intermediates/dex/release/minifyReleaseWithR8/classes.dex ~
```

我们打开`/data/user/0/com.termux/files/home/，`就可以看到有一个dex文件，留着备用。

## `Framework Patcher Go`模块自动修改

从`Framework Patcher Go`GitHub链接（https://github.com/changhuapeng/FrameworkPatcherGO）上下载模块。

MT管理器打开zip，将`classes.dex`添加到zip中的`/META-INF/com/google/android/magisk/dex/`文件夹下，然后Magisk刷入模块，它会自动修改系统自带的`framework.jar`中的`dex，`然后以面具模块的形式替换系统原来的`framework.jar。`

PS：过程中需要按音量上下键的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm911UkSP7e7chXXnh6Tu7Dw2e1ULJ8sg2TYAVw6ibBgicBb0OXJpcOWyeA/640?wx_fmt=png&from=appmsg)

**注意，注意，注意**

前面都是按音量上键，但到了最后，你看到：

```
This step is not required unless your device crashes after installing this module.
Do you want to apply this step?
```

这两行英语后，请按音量下键。

等待刷完。请提前做好救砖准备，如TWRP，音量键救砖模块等等。

如果最后按音量下键后，是会卡开机页面的，则救砖，然后继续刷入模块。

但在最后选择按音量上键，如果正常开机，那么到这里就结束了。

但如果还是无法开机，那就只能手动修改`framework.jar`中的`dex。`请看接下来的教程。

## 手动修改`framework.jar`

文件路径：`/system/framework/framework.jar，`复制文件到某个路径下，不要直接修改系统路径下的jar。

MT管理器打开jar
`查看`——`Dex编辑器++`——`全选`

接下来，**搜索方法名**：`engineGetCertificateChain`

###

在方法的末尾附近应该有如下几行代码：

```
const/4 v4, 0x0
aput-object v2, v3, v4
return-object v3
```

类似结构，但寄存器的值可能是不一样的。

如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9R4iccxQTC8myrrjeCOK93sppaqHWibbI23s5pOeo9zDpiaqYezmxeVK5w/640?wx_fmt=png&from=appmsg)

我们在`return-object XX`前加入：

```
invoke-static {XX}, Lcom/android/internal/util/framework/Android;->engineGetCertificateChain([Ljava/security/cert/Certificate;)[Ljava/security/cert/Certificate;
move-result-object XX
```

将`XX`替换为对应的值。

如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9LRACfsaXQ91HSzrQ0rWymRibhuYoZacyrdSm82wWo6rOr0gbgdQFXBw/640?wx_fmt=png&from=appmsg)

保存返回。

### **搜索方法名：**`newApplication`

可以看到有两个结果。我们先点开第一个，如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9Mr3GHs7D6m7RtJTpEf12buc9ekO7x7PicPmwUuqSj9kEOMa6tZ2PgDg/640?wx_fmt=png&from=appmsg)

存在类似代码：

```
.param XX，"context" #Landroid/content/Context;
```

在方法末尾`return`之前添加以下代码：

```
invoke-static {XX}, Lcom/android/internal/util/framework/Android;->newApplication(Landroid/content/Context;)V
```

将`XX`替换为寄存器。

如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9HSPB5BjA57eAPybObXoPibYP4YU2LhLJAznd2XwicwkEmOFjMzLbyibxw/640?wx_fmt=png&from=appmsg)

保存，看第二个搜索结果。

如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HUiac7n5UV2bMmGOjAibEicm9lRSJvG8VPDvLb3t3tAkWv9Kzt5Kq5s1As7p3oa7QUcyMPfyfWkakuw/640?wx_fmt=png&from=appmsg)

看到和刚刚不同，有p1，p2，p3。

我们还是和第一个一样，选择绿色高亮文本为`context`的那一行对应的寄存器。

在方法末尾`return`之前添加以下代码：

```
invoke-static {XX}, Lco...