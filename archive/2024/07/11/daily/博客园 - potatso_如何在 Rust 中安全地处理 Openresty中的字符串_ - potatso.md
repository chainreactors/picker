---
title: 如何在 Rust 中安全地处理 Openresty中的字符串? - potatso
url: https://www.cnblogs.com/potatso/p/18293583
source: 博客园 - potatso
date: 2024-07-11
fetch_date: 2025-10-06T17:38:27.328744
---

# 如何在 Rust 中安全地处理 Openresty中的字符串? - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [如何在 Rust 中安全地处理 Openresty中的字符串?](https://www.cnblogs.com/potatso/p/18293583 "发布于 2024-07-10 11:29")

# Hello World

Rust 以简洁高效安全而闻名，那么我们怎么集成到C 的项目中呢。尤其是字符串数据结构，该如何正确地交互。借此机会整理一下工作中遇到的难题，希望可以帮助大家走出坑。

我们先回顾一下 C 中字符串的结构。

在 C 语言中，字符是一个连续的内存地址空间以 `\0` 结尾。C 语言的字符串不会记录长度信息，而是遇到第一个`\0` 之前的地址空间作为长度信息。Rust 为了兼容C 的字符串，被称为 CStr。

但是在很多种语言中，如果遇到`\0` 作为结尾符，那么字符串中真的有`\0` 怎么办呢？所以 Nginx，lua 的字符串的数据结构，不光是一个连续的内存地址，而且还有字符串的长度信息。按照长度信息，从指针开始读取字符串就一定不会出错。Rust 中被称为 String。大概是这样

```
struct String {
    vec: Vec<u8>, // 存放字符串内容的内存空间
    len: usize, // 当前字符串长度
    capacity: usize, // 记录了当前 Vec 的容量,也就是可以存储的最大字节数。
}
```

C语言的字符串不支持动态扩容，每次扩容都需要自己申请一段新的内存，复制旧的内存到新的内存，并释放旧的内存。这个过程既繁琐，又容易出现内存问题。

Rust官方实现了这些功能，Rust 的字符串每次都已现有内存的 2 倍去扩容，并执行上述的操作。

# 在 Rust 中使用借用来表示 C 语言的字符串

Rust 的 String中的 vec 字段，指向传入的 C 语言内存地址即可。使用 Rust 的借用（Borrow）思想，可以很好地注明这类关系。但要注意的是，由于 Rust 的自动释放机制，在超出作用域后，Rust 会自动释放 String。而 Rust 无法正确的区分 String 中的 vec 是 C 语言管理的内存还是 Rust 管理的内存。这样就造成了著名的 double free 问题。所以我们要使用 `ManuallyDrop` 管理 Rust 中指向 C 语言的String。

# 在 Rust 中不要使用迭代器去遍历 Nginx/Lua 等字符串结构体

在 Rust 的 String 中，如果使用迭代器去遍历 Nginx的字符串，类似于下面的代码

```
while let Some(ch) = input_str.chars().nth(i){
	// todo!();
}

// or

for (i, b) in input_str.char_indices(){
	// todo!();
}
```

那么一定会出现问题的，下面我们来详细解释一下为什么。

在 Nginx ，或者 Openresty 中，存储字符串的时候不再以`\0`为结尾标志符。每个字符串都紧密相连。

但是在 Rust 中，**String 的迭代器在遍历字符串的时候，依旧使用`\0`为结尾标志符，那么就会造成，迭代器会不停地访问内存，甚至越界访问到Nginx 中其他字符串**。

因为 Rust 的 String，在申请或扩容内存空间的时候，会使用**`\0`**初始化内存空间。Rust 的

String 只不过是 C Str 的加强版，并且 Rust 的 String 一定会小于 Capacity，String 中一定保证有**`\0`。**

但是传入的 nginx 字符串却无法正常保证，为了安全考虑，请使用字符串的长度信息去便利字符串，我们可以改为

```
while i < input_str.len() {
    if let Some(ch) = input_str.chars().nth(i) {
	    // todo
    }
}
```

# CStr转换为 Rust 的字符串的时候，为了性能考虑，禁用 utf8 检查

原因很简单，Rust 不会在意你的字符串是什么编码。所以你在转换的时候，如果使用 utf8 检查，Rust 只是遍历字符串并检查是否符合 utf8 标准。

但是，这里你一定要正确区分，传入的内容是字符串，还是二进制流。如不正常区分，则会出现如下错误

```
thread 'test_detect_2' panicked at /rustc/07dca489ac2d933c78d3c5158e3f43beefeb02ce/library/core/src/str/mod.rs:666:13:
byte index 2 is not a char boundary; it is inside '\n' (bytes 1..2) of `
�H�

abc--`
```

# 正确地把 C字符串转换为 Rust String 的操作

为什么不转换为 Rust 的 Cstr？因为 CStr 其实还是 C 语言的表示，以`\0`为结尾符。那我们不如直接用 Rust 的 String，效果是一样的，并且还附带长度信息，在 WAF 中可以轻松应对 NULL 绕过攻击！

## 1. 阻止自动内存释放的 Rust 类型

```
/// 提供忽略自动 free 的字符串，防止 c 与 rust 在交互的时候，因为 rust 误拿到所有权而 free 内存，造成内存崩溃
#[derive(PartialEq, PartialOrd, Debug)]
pub struct ManuallyString {
    value: ManuallyDrop<String>,
}
```

为什么弄个这个结构体，而不是使用 `mem::forget`？为了方便，防止误操作而导致 double free。其二为了代码的整洁美观。

## 2. 使用 String::from\_raw\_part转换字符串

```
impl ManuallyString {
    pub fn new(data: *const c_char, len: usize) -> Self {
        ManuallyString {
            value: unsafe {
                ManuallyDrop::new(String::from_raw_parts(data as *mut u8, len, len))
            },
        }
    }
}
```

`String::from_raw_parts` 这个函数只是将 String 的 vec 内存空间设置为 C 的内存空间，并设置当前字符串长度信息

## 3. 使用字符串

```
impl Deref for ManuallyString {
    type Target = String;

    fn deref(&self) -> &String {
        &self.value
    }
}
```

我们为`ManuallyString` 实现 Deref trait 即可。这样很好的标识，字符串的所有权在当前ManuallyString中，使用者只是借用。超过作用于也不会触发 rust 的自动回收机制。

一句话概括，指向字符串的内存空间的所有权在 C 端，Rust只是借用！

graph LR
subgraph C Memory
C\_Memory["C Memory Space(Owner)"]
end
subgraph Rust
Manually["ManuallyString"]
subgraph Borrow
Borrow1["Borrow 1"]
Borrow2["Borrow 2"]
end
end
C\_Memory --> Manually["Manually Struct"]
Manually --> Borrow1
Manually --> Borrow2

posted @
2024-07-10 11:29
[potatso](https://www.cnblogs.com/potatso)
阅读(68)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202508/35695-20250830121216742-1062949948.jpg)](https://developer.huawei.com/consumer/cn/activity/digixActivity/digixcmsdetail/101750143863263087?ha_source=BKYQ3&ha_sourceId=89000408)

### 公告

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)