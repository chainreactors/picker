---
title: AFL源码浅析
url: https://www.secpulse.com/archives/189852.html
source: 安全脉搏
date: 2022-10-27
fetch_date: 2025-10-03T20:58:29.549759
---

# AFL源码浅析

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# AFL源码浅析

[工具](https://www.secpulse.com/archives/category/tools)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-10-26

10,651

# 前言

`AFL`是一款著名的模糊测试的工具，最近在阅读`AFL`源码，记录一下，方便以后查阅。

# 环境

* • 项目：AFL
* • 编译项目：将编译的优化选项关闭，即改写成`-O0`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189852-1666750382.png "null")

# afl-gcc.c

使用`gdb`加载`afl-gcc`，并使用`set arg -o test test.c`设置参数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189852-1666750384.png "null")

2

## find\_as函数

* • `find_as`函数首先会通过`AFL_PATH`环境变量的值从而获得`AFL`对应的路径
* • 若上述环境变量不存在则获取当前`afl-gcc`所在的文件路径
* • 判断该路径下的`as`文件是否具有可执行权限

```
u8 *afl_path = getenv("AFL_PATH");
...
if (afl_path) {

    tmp = alloc_printf("%s/as", afl_path); //将AFL所在路径与字符as进行拼接

    if (!access(tmp, X_OK)) { //函数用来判断指定的文件或目录是否有可执行权限，若指定方式有效则返回0，否则返回-1
      as_path = afl_path;
      ck_free(tmp);
      return;
    }

    ck_free(tmp);

  }

  slash = strrchr(argv0, '/'); //在参数argv0所指向的字符串中搜索最后一次出现字符'/'

  if (slash) {

    u8 *dir;

    *slash = 0;
    dir = ck_strdup(argv0);
    *slash = '/';

    tmp = alloc_printf("%s/afl-as", dir); //将当前AFL所在的路径跟afl-as进行拼接

    if (!access(tmp, X_OK)) {
      as_path = dir;
      ck_free(tmp);
      return;
    }
...
```

## edit\_params函数

* • `edit_params`函数实际就是准备需要传入编译器的参数，如编译器的类型`gcc`或`clang`
* • 其次就是是否需要开启保护如`canary`等
* • 最后就是判断是否开启内存泄漏探测的工具，如`ASAN`，该工具是针对C/C++ 的快速内存错误检测工具

```
  ...
  cc_params = ck_alloc((argc + 128) * sizeof(u8*));

  name = strrchr(argv[0], '/'); //获取可执行文件名称
  if (!name) name = argv[0]; else name++; /*跳过路径符'/' */

  if (!strncmp(name, "afl-clang", 9)) { //判断编译器是否为clang
      ...
  }
  else {
    if (!strcmp(name, "afl-g++")) {
      u8* alt_cxx = getenv("AFL_CXX");
      cc_params[0] = alt_cxx ? alt_cxx : (u8*)"g++";
    } else if (!strcmp(name, "afl-gcj")) {
      u8* alt_cc = getenv("AFL_GCJ");
      cc_params[0] = alt_cc ? alt_cc : (u8*)"gcj";
    } else {
      u8* alt_cc = getenv("AFL_CC");
      cc_params[0] = alt_cc ? alt_cc : (u8*)"gcc"; //如环境变量没写入AFL_CC则默认使用gcc
    }
  }
  while (--argc) {
    u8* cur = *(++argv); //读取下一个参数

    if (!strncmp(cur, "-B", 2)) { //若参数是-B

      if (!be_quiet) WARNF("-B is already set, overriding"); //用于设置编译器的搜索路径

      if (!cur[2] && argc > 1) { argc--; argv++; }//继续读取下一个参数
      continue;

    }

    if (!strcmp(cur, "-integrated-as")) continue;

    if (!strcmp(cur, "-pipe")) continue;

#if defined(__FreeBSD__) && defined(__x86_64__)
    if (!strcmp(cur, "-m32")) m32_set = 1;
#endif

    if (!strcmp(cur, "-fsanitize=address") ||
        !strcmp(cur, "-fsanitize=memory")) asan_set = 1; //内存访问的错误

    if (strstr(cur, "FORTIFY_SOURCE")) fortify_set = 1;//缓冲区溢出问题的检查

    cc_params[cc_par_cnt++] = cur; //cc_params用于存放的参数

  }

  cc_params[cc_par_cnt++] = "-B"; //参数-B
  cc_params[cc_par_cnt++] = as_path; //afl-as的路径

  if (clang_mode)
    cc_params[cc_par_cnt++] = "-no-integrated-as";

  if (getenv("AFL_HARDEN")) {

    cc_params[cc_par_cnt++] = "-fstack-protector-all"; //canary保护

    if (!fortify_set)
      cc_params[cc_par_cnt++] = "-D_FORTIFY_SOURCE=2";

  }

  if (asan_set) {

    /* Pass this on to afl-as to adjust map density. */

    setenv("AFL_USE_ASAN", "1", 1);

  } else if (getenv("AFL_USE_ASAN")) {

    if (getenv("AFL_USE_MSAN"))
      FATAL("ASAN and MSAN are mutually exclusive");

    if (getenv("AFL_HARDEN"))
      FATAL("ASAN and AFL_HARDEN are mutually exclusive");

    cc_params[cc_par_cnt++] = "-U_FORTIFY_SOURCE";
    cc_params[cc_par_cnt++] = "-fsanitize=address";

  } else if (getenv("AFL_USE_MSAN")) {

    if (getenv("AFL_USE_ASAN"))
      FATAL("ASAN and MSAN are mutually exclusive");

    if (getenv("AFL_HARDEN"))
      FATAL("MSAN and AFL_HARDEN are mutually exclusive");

    cc_params[cc_par_cnt++] = "-U_FORTIFY_SOURCE";
    cc_params[cc_par_cnt++] = "-fsanitize=memory";
  }
  ...
      cc_params[cc_par_cnt++] = "-g";
  ...
    cc_params[cc_par_cnt++] = "-O3";
    cc_params[cc_par_cnt++] = "-funroll-loops";
    /* Two indicators that you're building for fuzzing; one of them is
       AFL-specific, the other is shared with libfuzzer. */
    cc_params[cc_par_cnt++] = "-D__AFL_COMPILER=1";
    cc_params[cc_par_cnt++] = "-DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION=1";
  }
  if (getenv("AFL_NO_BUILTIN")) {
    cc_params[cc_par_cnt++] = "-fno-builtin-strcmp";
    cc_params[cc_par_cnt++] = "-fno-builtin-strncmp";
    cc_params[cc_par_cnt++] = "-fno-builtin-strcasecmp";
    cc_params[cc_par_cnt++] = "-fno-builtin-strncasecmp";
    cc_params[cc_par_cnt++] = "-fno-builtin-memcmp";
    cc_params[cc_par_cnt++] = "-fno-builtin-strstr";
    cc_params[cc_par_cnt++] = "-fno-builtin-strcasestr";
  }
  cc_params[cc_par_cnt] = NULL;
}
```

**通过edit\_params函数后**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189852-1666750387.png "null")

4

可以传递给编译器的参数增加了`-B . -g -O3 -funroll-loops -D__AFL_COMPILER=1 -DFUZZING_BUILD_MODE_UNSAFE_FOR_PRODUCTION=1`这几项

## main函数

* • 首先调用`isatty`函数判断描述符是否为终端机以及是否为静默模式，即不打印任何信息，`SAYF`即输出函数用于输出提示字符
* • 接着通过`find_as`函数搜索`as`文件所在的路径
* • 接着通过`edit_params`函数编辑获取需要传入编译器的参数
* • 最后通过`execvp`函数启动`gcc`或其他编译器

```
  /*
    isatty函数用于判断文件描述词是否是为终端机
    获取AFL_QUIET的环境变量
  */
  if (isatty(2) && !getenv("AFL_QUIET")) { //判断是否静默模式
    /*
      #ifdef MESSAGES_TO_STDOUT
      #  define SAYF(x...)    printf(x)
      #else
      #  define SAYF(x...)    fprintf(stderr, x)
      #endif
    */
    SAYF(cCYA "afl-cc " cBRI VERSION cRST " by <lcamtuf@google.com>n");

  } else be_quiet = 1;

  if (argc < 2) { //参数个数小于两个

    SAYF("n"
         "This is a helper application for afl-fuzz. It serves as a drop-in replacementn"
         "...