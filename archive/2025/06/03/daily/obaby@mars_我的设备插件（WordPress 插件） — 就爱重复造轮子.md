---
title: 我的设备插件（WordPress 插件） — 就爱重复造轮子
url: https://h4ck.org.cn/2025/06/20925
source: obaby@mars
date: 2025-06-03
fetch_date: 2025-10-06T22:51:15.639566
---

# 我的设备插件（WordPress 插件） — 就爱重复造轮子

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 我的设备插件（WordPress 插件） — 就爱重复造轮子

2025年6月2日
[44 条评论](https://h4ck.org.cn/2025/06/20925#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/2024_06_13_12_01_IMG_3855-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/06/2024_06_13_12_01_IMG_3855-tuya.jpg)

这个假期事情有点多，也就没回老家。主要是自己最近也不想回，好处就是有点时间可以折腾自己喜欢的东西。

说的更直接点就是有时间瞎折腾，不过这第一次的效果并不是很好，例如录的视频，mic声音太小的，只能强行网上拉。录视频的时候发现原来的录屏工具注册失败了，变成了未授权。ScreenRecorderpro 7.0在双4k屏上尝试录制，直接崩溃了，升级到8.0发现注册没处理好，有的地方没搞。

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-02-150807-scaled.png)](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-02-150807.png)

新版变成了64位的，懒得去修改二进制文件了，直接修改hosts屏蔽掉服务器校验：

```
__int64 __fastcall CheckSNOnLine(unsigned int a1, unsigned int a2)
{
  __int64 v2; // rdx
  __int64 v3; // rbx
  const WCHAR *v4; // rax
  const WCHAR *v5; // rax
  __int64 v6; // rdx
  __int64 v7; // rax
  __int64 WebContent; // rax
  __int64 v9; // rsi
  __int64 v10; // rdx
  __int64 v11; // rdx
  unsigned int vars44; // [rsp+44h] [rbp+44h]
  __int64 vars48; // [rsp+48h] [rbp+48h] BYREF
  __int64 vars50; // [rsp+50h] [rbp+50h] BYREF
  __int64 vars58; // [rsp+58h] [rbp+58h] BYREF
  __int64 vars60; // [rsp+60h] [rbp+60h] BYREF
  __int64 vars68; // [rsp+68h] [rbp+68h] BYREF
  __int64 vars70; // [rsp+70h] [rbp+70h] BYREF
  __int64 vars78; // [rsp+78h] [rbp+78h] BYREF
  int vars8C; // [rsp+8Ch] [rbp+8Ch] BYREF
  __int64 vars90; // [rsp+90h] [rbp+90h] BYREF
  __int64 vars98; // [rsp+98h] [rbp+98h] BYREF
  __int64 varsA0; // [rsp+A0h] [rbp+A0h] BYREF
  __int64 varsA8; // [rsp+A8h] [rbp+A8h] BYREF
  __int64 varsB0; // [rsp+B0h] [rbp+B0h] BYREF
  __int64 varsB8; // [rsp+B8h] [rbp+B8h] BYREF

  vars48 = 0;
  vars50 = 0;
  vars58 = 0;
  vars60 = 0;
  vars68 = 0;
  vars70 = 0;
  vars78 = 0;
  varsB8 = 0;
  varsB0 = 0;
  varsA8 = 0;
  varsA0 = 0;
  vars98 = 0;
  vars90 = 0;
  sub_7CDDB0(&varsA0);
  sub_7CC140(&varsB8, a1, a2);
  LOBYTE(v2) = 1;
  v3 = sub_59E6D0(&qword_59D078, v2);
  sub_59E980(v3, -2147483646);
  *(_DWORD *)(v3 + 44) = 131097;
  if ( (unsigned __int8)sub_59EB90(v3, varsB8, 0) )
  {
    sub_59F9E0(v3, &varsA8, L"LastTime");
    sub_59F9E0(v3, &varsB0, L"SN");
  }
  sub_59E940(v3);
  sub_434690(&vars78, varsB0);
  if ( !vars78 )
  {
    sub_59E980(v3, -2147483647);
    *(_DWORD *)(v3 + 44) = 131097;
    if ( (unsigned __int8)sub_59EB90(v3, varsB8, 0) )
    {
      sub_59F9E0(v3, &varsA8, L"LastTime");
      sub_59F9E0(v3, &varsB0, L"SN");
    }
    sub_59E940(v3);
  }
  sub_410F80(&vars70, L"*************:", varsA8);
  v4 = (const WCHAR *)sub_410B40(vars70);
  OutputDebugStringW(v4);
  sub_410F80(&vars68, L"--------------:", varsB0);
  v5 = (const WCHAR *)sub_410B40(vars68);
  OutputDebugStringW(v5);
  if ( (unsigned int)sub_411190(varsA8, varsA0) )
  {
    sub_434690(&vars60, varsB0);
    sub_40FF60(&varsB0, vars60);
    if ( varsB0 )
    {
      if ( (unsigned __int8)sub_7CB9B0() )
      {
        sub_7CC030(&vars58);
        sub_4110B0(&vars98, 3, L"http://gilisoft.com/webtools/livecheck/IsValidKey.php?key=", varsB0, vars58);
        sub_40F8B0(&vars90);
        if ( (unsigned int)sub_7CB9E0() )
        {
          sub_4106C0(&vars50, vars98, 0);
          v7 = sub_4105E0(vars50);
          WebContent = CURL_GetWebContent(v7, &vars8C);
          v9 = WebContent;
          if ( vars8C > 0 )
          {
            sub_410BA0(&vars90, WebContent);
            CURL_FreeBuffer(v9);
            sub_434690(&vars48, vars90);
            sub_40FF60(&vars90, vars48);
          }
        }
        else
        {
          sub_7CBA00(&vars90, vars98);
        }
        if ( (unsigned int)sub_411190(vars90, L"expired") )
        {
          *(_DWORD *)(v3 + 44) = 131103;
          if ( (unsigned __int8)sub_59EB90(v3, varsB8, 0) )
            sub_59F940(v3, L"LastTime", varsA0);
          sub_59E940(v3);
          LOBYTE(v11) = 1;
          (*(void (__fastcall **)(__int64, __int64))(*(_QWORD *)v3 - 32LL))(v3, v11);
          vars44 = -1;
        }
        else
        {
          *(_DWORD *)(v3 + 44) = 131103;
          if ( (unsigned __int8)sub_59EB90(v3, varsB8, 0) )
            sub_59F940(v3, L"SN", &dword_7CE3DC);
          sub_59E940(v3);
          LOBYTE(v10) = 1;
          (*(void (__fastcall **)(__int64, __int64))(*(_QWORD *)v3 - 32LL))(v3, v10);
          vars44 = 0;
        }
      }
      else
      {
        vars44 = -1;
      }
    }
    else
    {
      LOBYTE(v6) = 1;
      (*(void (__fastcall **)(__int64, __int64))(*(_QWORD *)v3 - 32LL))(v3, v6);
      vars44 = 0;
    }
  }
  else
  {
    sub_40C4B0(v3);
    vars44 = -1;
  }
  sub_40F8B0(&vars48);
  sub_40F900(&vars50);
  sub_40F990(&vars58, 5);
  sub_40F990(&vars90, 6);
  return vars44;
}
```

反正，能用就ok拉：

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-02-151824.png)](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-02-151824.png)

今天上午，有点时间，有拿出上周搞的那个我的设备页面插件，这个东西其实最开始也是抄来的：

> [抄作业–我的设备](https://h4ck.org.cn/2024/07/17545)

前端时间，看大家都更新了，开始基于post类型来做展示，每个设备都是个单页能回复评论，忘了在谁那里看的了。总觉得有些过去强大了，虽然也是个插件。

最终还是决定自己找个轮子，于是就有了这个东西，使用插件生成的页面：

<https://h4ck.org.cn/my-devices>

[![](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-02-151307.png)](https://h4ck.org.cn/wp-content/uploads/2025/06/Screenshot-2025-06-02-151307.png)

整体页面样式沿用原来的，也不用在主题自定义添加css中添加样式了。新建页面，插入short code即可：

```
# Baby Device Manager

一个功能强大的WordPress设备管理系统插件，支持设备分组管理、设备信息管理、自定义排序、状态跟踪等功能。

## 功能特点

- 设备分组管理
  - 创建和管理设备分组
  - 自定义分组排序
  - 分组描述信息
- 设备管理
  - 添加/编辑/删除设备
  - 设备状态管理（在售、停售、已售出、维修中、已报废）
  - 设备图片和产品链接
  - 自定义设备排序
  - 设备描述信息
- 前端展示
  - 响应式布局
  - 按分组分类显示
  - 支持多种排序方式
  - 美观的界面设计
  - 支持自定义每行显示设备数量（1-6个）
- 其他功能
  - 图片管理：支持设备图片上传和显示
  - 产品链接：支持添加产品详情页链接
  - 状态跟踪：支持多种设备状态管理
  - 自定义排序：支持设备分组和设备的自定义排序

## 安装要求

- WordPress 5.0 或更高版本
- PHP 7.2 或更高版本
- MySQL 5.6 或更高版本

## 安装方法

1. 下载插件压缩包
2. 在WordPress后台进入"插件 > 安装插件"页面
3. 点击"上传插件"按钮，选择下载的压缩包
4. 安装完成后点击"启用插件"

## 使用方法

### 管理界面

1. 设备分组管理
   - 进入"设备管理 > 设备分组"
   - 添加新分组：填写分组名称、描述和排序值
   - 编辑现有分组：修改分组信息或删除分组
   - 排序值越小，显示越靠前

2. 设备管理
   - 进入"设备管理 > 添加设备"
   - 填写设备信息：
     - 设备名称
     - 所属分组
     - 设备描述
     - 设备状态
     - 设备图片URL
     - 产品链接
     - 排序值

### 前端显示

使用 shortcode 在页面或文章中显示设备列表：

1. 基本用法
```
【baby_devices】
```

2. 按分组显示
```
【baby_devices group="分组名称"】
```

3. 按状态显示
```
【baby_devices status="在售"】
```

4. 自定义排序
```
【baby_devices orderby="sort_order" order="ASC"】
```

5. 组合使用
```
【baby_devices group="厨房电器" status="在售" orderby="sort_order" order="ASC"】
```

6. 自定义每行显示数量
```
【baby_devices per_row="4"】
```

### Shortcode 参数说明

- `group`：按分组名称筛选
- `status`：按设备状态筛选
- `orderby`：排序字段
  - `sort_order`：按自定义排序（默认）
  - `created_at`：按创建时间
- `order`：排序方向
  - `ASC`：升序（默认）
  - `DESC`：降序
- `per_row`：每行显示设备数量（1-6个，默认：3）

### 设置

1. 在WordPress后台菜单中找到"设备管理 > 设置"
2. 设置每行显示设备数量（1-6个）
3. 点击"保存设置"按钮保存

## 注意事项

1. 首次启用插件时会自动创建必要的数据表
2. 删除插件时不会自动删除数据表，需要手动删除
3. 建议定期备份数据库
4. 图片URL需要是可访问的完整地址

## 更新日志

### 1.0.4
- 修复状态按钮样式问题
- 优化状态类名生成逻辑

### 1.0.3
- 添加新的设备状态选项
- 优化数据库表结构

### 1.0.2
- 更新数据库表结构
- 优化设备状态显示

### 1.0.1
- 添加设备显示设置功能
- 支持自定义每行显示设备数量

### 1.0.0
- 初始版本发布
- 支持设备分组管理
- 支持设备信息管理
- 支持自定义排序
- 支持前端展示

## 技术支持

如有问题或建议，请访问：
- 官方网站：https://h4ck.org.cn
- 问题反馈：https://h4ck.org.cn/contact

## 作者

- o...