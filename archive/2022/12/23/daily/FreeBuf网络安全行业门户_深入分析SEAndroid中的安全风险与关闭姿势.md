---
title: 深入分析SEAndroid中的安全风险与关闭姿势
url: https://www.freebuf.com/articles/endpoint/353271.html
source: FreeBuf网络安全行业门户
date: 2022-12-23
fetch_date: 2025-10-04T02:20:16.095707
---

# 深入分析SEAndroid中的安全风险与关闭姿势

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

深入分析SEAndroid中的安全风险与关闭姿势

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)
* [系统安全](https://www.freebuf.com/articles/system)

深入分析SEAndroid中的安全风险与关闭姿势

2022-12-22 16:17:20

所属地 北京

## 一、背景

`SEAndroid`是Google在Android系统上应用的一套以`SELinux`为基础核心的系统安全机制(下统称SElinux)。其最早发布于Android 4.3， 经过多年的发展， 目前已经成为了Android用户态安全的重要保障。

无恒实验室在近期的安全研究中，对于`SELinux`的攻击面和攻击方法有一些研究成果，特此分享给大家，希望与业内进行学习交流。

`SELinux（Security-Enhanced Linux）`是美国国家安全局（NSA）主导开发的Linux内核安全模块，为内核提供了`强制访问控制（MAC）`，项目于2000年发布到开源社区，并于2003年集成到上游 Linux 内核中。「所以说优秀的安全机制就是公开所有细节，依旧可以让攻击者束手无策 :)」

Linux默认的访问控制策略是`自主访问控制（DAC`，可以通过下面两张图来直观了解一下DAC与MAC的区别：![1671696634_63a410fad17bc7980af1a.jpg!small?1671696635699](https://image.3001.net/images/20221222/1671696634_63a410fad17bc7980af1a.jpg!small?1671696635699)

图片源自 https://blog.csdn.net/headwind\_/article/details/119704755

在`DAC`中，对象的拥有者可以任意修改或授予此对象相应的权限，且进程理论上所拥有的权限与执行它的用户的权限相同； 这导致如果一个以`root`权限运行的进程被攻破， 攻击者就可以借此在系统中畅行无阻。

而在`MAC`中， 为所有进程和文件都设置了安全上下文， 当用户执行某项操作时， 除了要通过`DAC`的检查， 还需要符合`MAC`中制定的规则； 因此即便是`root`进程，其权限也会被限制在特定范围内，这虽然不能完全防御攻击，但可以将损失降到最低。

## 二、SElinux的实现

SElinux的实现依赖于Linux内核的`安全模块框架（LSM）`，当内核对用户态访问做处理时，LPM会在 DAC检查之后预留钩子函数，SElinux就是通过此接口来实现MAC；因此Android平台权限是`DAC+MAC`，即两个权限管理独立存在，操作行为必须同时通过两种机制的检验才会被允许。

![1671696674_63a4112295253e7008988.png!small?1671696675155](https://image.3001.net/images/20221222/1671696674_63a4112295253e7008988.png!small?1671696675155)

https://www.kernel.org/doc/ols/2002/ols2002-pages-604-617.pdf

## 三、基本元素

### 3.1 标签

`SElinux`是一个基于标签的系统，所有的进程，文件，socket等都有标签。标签是一个四元组字符串**`user:role:type:level`**，其中我们主要关注的是`type`。

在 Android系统中，所有对象大致可以分为两类：

* 一种是`死`的（文件、端口、系统属性等被调用对象），例如：`u:object_r:proc:s0`
* 一种是`活`的（进程、App等调用资源的对象），例如：`u:r:vendor_init:s0`

查看标签的方法就是在常用命令后面加上-Z，如下：

`进程 ps -ZAu:r:vendor_init:s0 root 545 1 6728 2376 poll_sche+ 0 S init
u:r:zygote:s0 root 678 1 4308756 142888 poll_sche+ 0 S zygote64
文件 ls -lZdrwxr-x--- 2 root shell u:object_r:rootfs:s0 4096 2009-01-01 00:00 sbin
drwxr-xr-x 18 root root u:object_r:vendor_file:s0 4096 2009-01-01 00:00 vendor
属性 getprop -Z [DEVICE_PROVISIONED]: [u:object_r:default_prop:s0]
[aaudio.hw_burst_min_usec]: [u:object_r:exported_default_prop:s0]`

### 3.2 规则

有了`标签`之后，还需要编写`规则`来限制标签， 根据SELinux规范，完整的规则相关的语句格式为：

**`rule_name source_type target_type:class perm_set`**

* `rule_name 规则名`

  + `allow`： 允许主体对客体进行操作
  + `neverallow`：拒绝主体对客体进行操作
  + `dontaudit`： 表示不记录某条违反规则的决策信息
  + `auditallow`：记录某项决策信息，通常 SElinux 只记录失败的信息，应用这条规则后会记录成功的决策信息
* `source_type 主体`

  + `Domain`：一个进程或一组进程的标签。也称为域类型
* `target_type 客体`

  + `Type`：一个对象（例如，文件、套接字）或一组对象的标签
* `class 类别`

  + 要访问的对象的类型，例如文件、套接字等
  + 在`system/sepolicy/private/security_classes`中被定义
* `perm_set 动作集`

  + 要执行的操作，例如读取、写入等
  + 在`system/sepolicy/private/access_vectors`中被定义

下面结合例子说明一下：

`# 允许user域中的进程 读取 script标签中的file类型文件
allow user script:file {read};
# 不允许user域中的进程 写入 script标签中的file类型文件
neverallow user script:file {write};`

### 3.3 配置文件

SElinux编译后的`标签`和`规则`等文件会保存在每个分区的`etc/selinux`目录下：

`$ls -l system/etc/selinux
drwxrwxr-x 2 root root 4096 12月 9 15:53 mapping/
-rw-rw-r-- 1 root root 40561 12月 10 15:56 plat_file_contexts
-rw-rw-r-- 1 root root 8614 12月 10 15:56 plat_hwservice_contexts
-rw-rw-r-- 1 root root 7243 12月 9 15:53 plat_mac_permissions.xml
-rw-rw-r-- 1 root root 48646 12月 10 15:56 plat_property_contexts
-rw-rw-r-- 1 root root 1905 12月 10 15:56 plat_seapp_contexts
-rw-rw-r-- 1 root root 65 12月 10 15:55 plat_sepolicy_and_mapping.sha256
-rw-rw-r-- 1 root root 1623615 12月 10 15:55 plat_sepolicy.cil
-rw-rw-r-- 1 root root 19798 12月 10 15:56 plat_service_contexts
-rw-rw-r-- 1 root root 818418 12月 10 15:55 sepolicy_neverallows`

其中`plat_sepolicy.cil`中记录的是SElinux规则，`plat_sepolicy_and_mapping.sha256`为校验文件， 其余的文件中记录的都是标签数据。

## 四、SEAndroid安全风险

SElinux通过最大限度地限制系统中服务进程可访问的资源，以达到收敛攻击面，减小损失的目的；但其也不是万能的，开发遗留的调试接口、内核漏洞、错误的策略配置等问题都可能导致攻击者绕过SELinux的限制攻击系统。

### 4.1 自定义后门

所谓“敌在本能寺”， 有些厂商在开发时为了方便调试， 会预留关闭SElinux的`后门接口`， 如果这类`后门`在正式发布前没有删除， 就有可能被攻击者利用来关闭SElinux。

### 4.2 内核漏洞

SElinux主要限制用户态的操作，如果攻击者通过内核漏洞获得任意地址读写的能力，就可以通过覆写全局变量`selinux_enforcing`的方式将SElinux关闭。

为此，三星使用自研的`RKP(Real-time Kernel Protection)`机制，将敏感的全局变量放置在受保护的`kdp_ro节`，一定程度上缓解了此类攻击。

### 4.3 策略过于宽泛

SELinux中同样存在`人`引入的问题，如果将`敏感服务`开放给普通用户，或者对`System APP`、`Property`的权限划分不细致，就会导致受到攻击时的影响范围被扩大。

### 4.4 服务功能与SElinux策略不对齐

在Android系统中有些区域需要频繁的写入各类数据，如`/data/local/tmp`、`/sdcard`等，因此SElinux不会对这些位置做严格的限制， 普通用户权限就可以读写其中的数据。

原则上这些目录是不可以存放敏感数据的，如果研发人员将一些重要文件保存在这些目录下（如配置文件、隐私信息、升级固件等），就会存在被攻击者窃取篡改的风险。

## 五、SEAndroid关闭方式

上面介绍的都是在运行时绕过SElinux的方式，但在日常工作中还存在这样一种场景，我们需要在一台已解锁的Android设备上获取Root权限来进行测试；目前高版本Android 上有一些优秀的Root工具，例如`Magisk`、`KernelSU`等，但使用自动化工具终究是无法了解底层原理， 如果要手动ROOT设备，关闭SElinux就是十分关键的一步， 下面来介绍几种手动关闭SElinux的方法。

### 5.1 Patch Boot

下载Android设备对应的全量Rom包，解开Boot分区后可以发现其布局如下

`header # 内核运行参数 & 其他信息
kernel # Linux 内核
ramdisk.cpio # boot分区`

`header`的结构如下， 其中`cmdline`会传递给内核作为启动参数， 因此我们可以通过修改`cmdline`的方式，传入关闭SElinux的命令`enforcing=0 androidboot.selinux=permissive`。

`cmdline=
os_version=12.0.0
os_patch_level=2021-12`

不过在高版本Android系统中，很多厂商不再解析`cmdline`，通用性较差。

### 5.2 Patch Init

`init`是Linux Kernel启动后运行的第一个用户态进程，其功能主要是完成初始化、解析执行`init.rc`中定义的各种服务， 过程主要分为四个步骤：

`FirstStateMain`->`SetupSelinux`->`SecondStageMain`->`ueventd_main`

其中`SetupSelinux`阶段的关键函数如下：

* `LoadSelinuxPolicy`：加载sepolicy策略
* `selinux_android_restorecon`：重载sepolicy策略
* `SelinuxSetEnforcement`：设置SElinux开关

显然关键在于`SelinuxSetEnforcement`函数，其内部实现如下。

`void SelinuxSetEnforcement() {
bool kernel_enforcing = (security_getenforce() == 1);
bool is_enforcing = IsEnforcing();
if (kernel_enforcing != is_enforcing) {
if (security_setenforce(is_enforcing)) {
PLOG(FATAL) << "security_setenforce(" << (is_enforcing ? "true" : "false")
<< ") failed";
}
}
if (auto result = WriteFile("/sys/fs/selinux/checkreqprot", "0"); !result.ok()) {
LOG(FATAL) << "Unable to write to /sys/fs/selinux/checkreqprot: " << result.error();
}
}
bool IsEnforcing() {
if (ALLOW_PERMISSIVE_SELINUX) {
return StatusFromProperty() == SELINUX_ENFORCING;
}
return true;
}`

这里只需要Patch`IsEnforcing`使其永远返回`False`即可在`init阶段`关闭Selinux

### 5.3 重编译Kernel

依据`GPL`协议，厂商会开源修改的`Linux Kernel`，因此可以通过重编译内核的方式， 在编译时关闭SElinux。

具体方式为在内核配置文件.config中设置`CONFIG_SECURITY_SELINUX=n`。

### 5.4 Patch Kernel

如果厂商未开源内核，或者开源不彻底无法正常编译，也可以通过Patch的方式绕过SElinux

这里以`文件打开操作 open`为例，梳理SElinux的相关调用链

![1671696777_63a41189b5449662b2cbd.png!small?1671696778163](https://image.3001.net/images/20221222/1671696777_63a41189b5449662b2cbd.png!small?1671696778163)

图片源自 https://blog.csdn.net/bruk\_spp/article/details/107283935

当用户空间调用`open`打开文件时，会触发系统调用`do_dentry_open`，接着调用Linux LSM公共接口`security_file_open`，之后会走到SElinux处理open操作的函数`selinux_file_open`， 下一步SElinux会调用`avc公共函数`来实现权限检查和日志审计功能，如果发现操作越权，则会调用`avc_denied`来阻止该行为。

因此我们只需要将阻止操作的相关逻辑 Patch掉，就能够变相关闭 SElinux。

## 六、总结

总的来说，SElinux的引入极大的降低了针对用户态攻击所造成的损失, 即便通过漏洞获取了Root权限, 也会被限制在影响相对小的范围内。近年来，随着众多软硬件防护机制的引入，Android的安全性有了显著的提升；通过优秀的，可公开的安全机制来收敛攻击面，提升安全水位，这也是我们国产操作系统学习的榜样和努力实现的目标。

> 参考
>
> * https://source.android.com/security/selinux

# linux # 系统安全 # 安卓安全 # 内核

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

一、背景

二、SElinux的实现

三、基本元素

* 3.1 标签
* 3.2 规则
* 3.3 配置文件

四、SEAnd...