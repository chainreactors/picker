---
title: 美团，我日你仙人，还我相册
url: https://mp.weixin.qq.com/s/3c4VOHq2gZdIdJTd-2xkoA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:35:36.693355
---

# 美团，我日你仙人，还我相册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibroIiatwe16jmr1NiazL7gwxEnBrMM4fLVIT0FNrct7tuZd5RBvqeSqHicaSsxjHKNy9Fz9ShvgdDva5qXHpQ0PicWqSSUVCKnDIRA1xnKMAw/0?wx_fmt=jpeg)

# 美团，我日你仙人，还我相册

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器中沉浸阅读

# 美团，我日你仙人，还我相册

> 深度技术分析：美团APP删除用户相册事件

## 一、事件背景

美团APP删除用户照片的事件，相信大家都有所耳闻。官媒报道了，美团也承认了，但事情究竟是怎么发生的？中招的用户做了什么？美团为什么会有权限删除用户的照片？这些问题鲜有人做深入解答。

本文基于差评君与EBCDIY的技术分析，结合安卓系统存储机制的演变，深度剖析这一事件的来龙去脉。

![](https://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe2Gu8Lx1vaBToFf2eib4UqxUprZ8TbTy6e0xzia786GKWMls1XFrjeBhiaGriblqOMibpTmSiae2Yspfo5BYOCNdgibPFwsPnoPMvIf80/640?wx_fmt=png&from=appmsg)

## 二、谁最容易中招？

根据技术分析，以下用户群体最容易触发这个漏洞：

| 用户群体 | 系统版本 | 风险等级 | 原因 |
| --- | --- | --- | --- |
| 安卓老用户 | 安卓10及更早版本 | ⚠️ 高危 | 使用Shared Storage存储模式 |
| 华为老用户 | 鸿蒙4.2及以下 | ⚠️ 高危 | 鸿蒙4.2基于安卓10开发 |
| 安卓新用户 | 安卓11及以上 | ⚠️ 低风险 | Scoped Storage保护 |
| iPhone用户 | iOS全版本 | ✅ 安全 | 权限隔离机制完善 |
| 华为新用户 | 鸿蒙5.0及以上 | ✅ 安全 | 原生鸿蒙权限隔离 |

**结论**：这次bug是安卓独享的"moment"，iOS和原生鸿蒙用户大可放心。

## 三、技术原理：安卓存储机制演变

### 3.1 旧时代的Shared Storage（共享存储）

在安卓10及更早的版本中，安卓使用的是一种叫做Shared Storage（共享存储）的模式。

#### 什么是Shared Storage？

说白了就是一个"大通铺"——不同的APP可以轻易读取，甚至删除其他APP的文件，当然也包括存储在`DCIM`和`Pictures`目录下的系统公共图片目录。

#### 美团APP申请的权限

通过分析美团APP的`AndroidManifest.xml`文件，发现它请求了公共存储目录的读取和写入两个权限：

```
<!-- 读取外部存储权限 -->
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>

<!-- 写入外部存储权限 -->
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
```

#### 美团为什么需要这些权限？

美团申请这些权限有合理的业务需求：

1. 1. **写评价时**：需要读取相册目录选择照片上传
2. 2. **APP内拍照后**：需要通过写入权限把照片保存回相册目录

#### 问题出在哪里？

在正常情况下，这种授权虽宽泛但不致命。可一旦出现意外——比如美团解释的"第三方插件冲突导致缓存清理异常"——那就麻烦了。

**关键问题**：在Shared Storage模式下，APP一旦获得`WRITE_EXTERNAL_STORAGE`权限，它就有权限从自己的私有目录一路删到公共目录去！

### 3.2 新时代的Scoped Storage（分区存储）

从安卓10开始，谷歌学习了隔壁苹果iOS的逻辑，引入了新的Scoped Storage（分区存储/沙盒存储）设计，并在安卓11上正式强制推行。

#### Scoped Storage的核心变化

```
┌─────────────────────────────────────────────────────────────┐
│                    安卓10及以前（Shared Storage）              │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                      │
│  │  App A  │  │  App B  │  │  App C  │                      │
│  └────┬────┘  └────┬────┘  └────┬────┘                      │
│       │            │            │                            │
│       └────────────┼────────────┘                            │
│                    ▼                                         │
│         ┌─────────────────────┐                             │
│         │   公共存储区域       │  ← 任何APP都可以读写         │
│         │  (DCIM/Pictures等)  │                             │
│         └─────────────────────┘                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    安卓11及以后（Scoped Storage）             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                      │
│  │  App A  │  │  App B  │  │  App C  │                      │
│  └────┬────┘  └────┬────┘  └────┬────┘                      │
│       │            │            │                            │
│       ▼            ▼            ▼                            │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                      │
│  │ 沙盒 A  │  │ 沙盒 B  │  │ 沙盒 C  │  ← 各自独立，互不干扰  │
│  └─────────┘  └─────────┘  └─────────┘                      │
│                                                             │
│         ┌─────────────────────┐                             │
│         │   公共存储区域       │  ← 只能通过MediaStore访问    │
│         │  (DCIM/Pictures等)  │    且需要用户确认            │
│         └─────────────────────┘                             │
└─────────────────────────────────────────────────────────────┘
```

#### Scoped Storage的关键特性

1. 1. **沙盒隔离**：每个安卓APP都有自己专门的文件夹
2. 2. **读写自己的文件不再需要权限**
3. 3. **其他APP无法访问你的私有目录**
4. 4. **访问公共区域需要通过MediaStore接口**

#### 权限的变化

谷歌从安卓11开始正式废掉了`WRITE_EXTERNAL_STORAGE`权限对公共目录的写入能力：

```
// 安卓10及以前：可以直接删除公共目录的文件
File file = new File("/sdcard/DCIM/photo.jpg");
boolean deleted = file.delete(); // 返回 true，文件被删除

// 安卓11及以后：无法直接删除公共目录的文件
File file = new File("/sdcard/DCIM/photo.jpg");
boolean deleted = file.delete(); // 返回 false，删除失败！
```

### 3.3 MediaStore接口

那么怎么才能在安卓11以后的系统上删除相册图片呢？

答案是：通过一个新引入的名为**MediaStore**的管理接口。

#### MediaStore删除流程

```
// 通过MediaStore删除图片的标准流程
ContentResolver resolver = context.getContentResolver();
Uri imageUri = MediaStore.Images.Media.EXTERNAL_CONTENT_URI;

// 构建删除条件
String selection = MediaStore.Images.Media._ID + " = ?";
String[] selectionArgs = new String[]{ String.valueOf(imageId) };

// 执行删除
int deletedRows = resolver.delete(imageUri, selection, selectionArgs);
```

#### MediaStore的安全机制

MediaStore接口有一个关键特性——APP在调用它删除图片的时候，手机会在屏幕上**强制弹窗**，告诉用户有一个APP要删照片了。

```
┌────────────────────────────────────┐
│                                    │
│   ⚠️ 美团想要删除照片              │
│                                    │
│   美团正在请求删除以下照片：        │
│   • IMG_20240101_001.jpg          │
│   • IMG_20240101_002.jpg          │
│                                    │
│   [ 允许 ]      [ 拒绝 ]          │
│                                    │
└────────────────────────────────────┘
```

以谷歌相册为例，在安卓11之后的手机中，如果你通过谷歌相册删除存储的照片，你会收到一个巨大的弹窗提醒，让你对删除操作进行二次确认。

**结论**：正常情况下，美团APP是不可能在新系统上静默删除照片的。

## 四、美团删除照片的技术分析

### 4.1 老版本安卓（安卓10及以下）的删除过程

在低于安卓11的手机上，过程很简单：

```
┌─────────────────────────────────────────────────────────────┐
│                    老版本安卓删除流程                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Step 1: 美团APP申请外部存储读写权限                         │
│          ↓                                                  │
│  Step 2: 用户图方便给了授权                                  │
│          ↓                                                  │
│  Step 3: 后面的操作就是一路绿灯了                            │
│          ↓                                                  │
│  Step 4: 缓存清理bug触发，开始删除文件                       │
│          ↓                                                  │
│  Step 5: 从私有目录一路删到公共目录                          │
│          ↓                                                  │
│  Step 6: 用户相册照片被删除，无任何提示                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

#### 可能的触发场景

假设某天某个后端开发用AI写了一个有问题的缓存清理指令：

```
// 有问题的缓存清理代码示例
public void clearCache(String path) {
    File cacheDir = new File(path);
    // 错误：没有正确限制删除范围
    deleteRecursive(cacheDir);
}

private void deleteRecursive(File file) {
    if (file.isDirectory()) {
        for (File child : file.listFiles()) {
            deleteRecursive(child);  // 递归删除所有内容
        }
    }
    file.delete();  // 如果path传入错误，可能删除整个存储！
}
```

内部流程又比较草台班子，导致修改被一路审批通过并更新，用户的存储就被清理得干干净净了。

### 4.2 新版本安卓（安卓11及以上）的疑问

网上也有一些使用较新手机的用户声称照片被美团删掉了，这就有意思了。

#### 假设一：媒体管理应用权限（Manage Media）

从安卓11开始，系统引入了一个特殊的权限——**媒体管理应用（Manage Media）**。

```
<!-- 媒体管理权限声明 -->
<uses-permission android:name="android.permission.MANAGE_MEDIA"/>
```

它和普通的"访问照片与视频"权限不一样，是一个更高级的特殊权限，需要额外申请。

**权限效果**：假如APP被授予了这个权限，MediaStore接口在删除照片时就不会再弹出特殊确认了。

#### 假设二：管理外部存储权限（Manage External Storage）

另一个可能是管理外部存储（Manage External Storage）权限，同样是安卓11之后引进的特殊权限。

```
<!-- 管理外部存储权限声明 -->
<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>
```

这个权限为的是方便网盘类应用和第三方文件管理器能够继续在新系统上正常工作。

**权限效果**：一旦APP被授予了这个权限，就可以一键清空相册，并且和这次美团删除相册的表现一致。

#### 关键证据：只删除文件，不更新数据库

安卓系统里有一个用来管理媒体数据的数据库（MediaStore数据库）。

| 删除方式 | 文件是否删除 | 数据库是否更新 | 表现 |
| --- | --- | --- | --- |
| MediaStore接口删除 | ✅ 是 | ✅ 是 | 照片完全消失 |
| 直接文件删除 | ✅ 是 | ❌ 否 | 照片变成灰框框 |

**美团删除相册的表现**：只删除了照片文件本身，但是没有更新媒体数据库，导致手机相册里所有照片都变成了无法预览的灰框框。

这说明美团是通过**直接文件操作**删除的，而不是通过MediaStore接口。

### 4.3 真相是什么？

然而，在查看美团APP申请的权限清单时，发现美团**既没有请求MANAGE\_MEDIA权限，也没有请求MANAGE\_EXTERNAL\_STORAGE权限**。

这就引出了三种可能的推测：

#### 推测一：用户描述不准确

网上发帖的用户不太懂技术，描述有误。可能他们使用的是老版本...