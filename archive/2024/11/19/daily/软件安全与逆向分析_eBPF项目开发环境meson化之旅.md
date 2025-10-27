---
title: eBPF项目开发环境meson化之旅
url: https://mp.weixin.qq.com/s?__biz=MzU3MTY5MzQxMA==&mid=2247484711&idx=1&sn=6951876677f66ad559fc06abbe8cbbe3&chksm=fcdd052acbaa8c3c22dc2ffb38667175a37a4d25917376a9f0518c15b5cc045f1a8ffe355924&scene=58&subscene=0#rd
source: 软件安全与逆向分析
date: 2024-11-19
fetch_date: 2025-10-06T19:18:54.787684
---

# eBPF项目开发环境meson化之旅

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/k9S5z61JPnapvCqB5dP5zWd3VXzz2ZWU4EI0S6rHpG3qHgbuKM7WeCflB5biaicp7f3kfCIw3c4YhYP3hosAj7eg/0?wx_fmt=jpeg)

# eBPF项目开发环境meson化之旅

原创

非虫

软件安全与逆向分析

使用meson管理工程是真的香，受Frida的启发，我试着将eBPF开发环境meson化。

首先，是libbpf的meson化。这个基础库当时研究使用的时候才0.8版本，现在都1.5了。

直接上代码。

```
project('libbpf', 'c', version: 'v1.5.0')libbpf_extra_cflags = [  '-D__user=',  '-D__force=',  '-D__poll_t=unsigned',]output_dir = 'output'libbpf_sources = files(  'src/bpf.c',  'src/bpf_prog_linfo.c',  'src/btf.c',  'src/btf_dump.c',  'src/btf_iter.c',  'src/btf_relocate.c',  'src/elf.c',  'src/features.c',  'src/gen_loader.c',  'src/hashmap.c',  'src/libbpf.c',  'src/libbpf_errno.c',  'src/libbpf_probes.c',  'src/linker.c',  'src/netlink.c',  'src/nlattr.c',  'src/relo_core.c',  'src/ringbuf.c',  'src/str_error.c',  'src/strset.c',  'src/usdt.c',  'src/zip.c')libbpf_static = static_library(  'bpf_static',  sources: libbpf_sources,  c_args: libbpf_extra_cflags,  include_directories: include_directories('include', 'include/uapi', 'src'),  install: true,)libbpf_dep = declare_dependency(  link_with: [libbpf_static],  include_directories: include_directories('.'),)dep_libelf = dependency('libelf', fallback: ['libelf', 'libelf_dep'])dep_zlib = dependency('zlib', fallback: ['zlib', 'zlib_dep'])libbpf = library(  'bpf',  sources: libbpf_sources,  c_args: libbpf_extra_cflags,  include_directories: include_directories('include', 'include/uapi', 'src'),  dependencies: [dep_libelf, dep_zlib],  install: true,)pkg = import('pkgconfig')pkg.generate(  name: meson.project_name(),  description: 'eBPF library',  version: meson.project_version(),  url: 'https://github.com/libbpf/libbpf',  libraries: libbpf,  libraries_private: libbpf_static,  subdirs: ['libbpf'],)meson.override_dependency('libbpf', libbpf_dep)
```

一些eBPF开发程序，还用到很多第三方库，比如libzip、libepf、argp等。前两者Frida就有移植，直接拿来使用就可以了。argp是gnulib的一部分。我也移植了一下。

```
# Copyright (c) 2024-2025 fei_cong(https://github.com/feicong/ebpf-course)project('argp', 'c', version: '1.0', license: 'GPL-3.0-or-later')# Gnulib requires some specific compiler arguments, generally to suppress warnings# and add GNU extensions if needed.argp_extra_cflags = [  '-Wall',  '-Wextra',  '-Wno-unused-parameter',  '-D_GL_CONFIG_H_INCLUDED',  '-DHAVE_CONFIG_H',  '-D_GNU_SOURCE',  '-include', 'config.h',  # Ensure config.h is included first as required]# Include the Gnulib header directorygnulib_inc = include_directories('src')# Source files from Gnulib's argp implementationargp_sources = files(  'src/argp-ba.c',  'src/argp-eexst.c',  'src/argp-fmtstream.c',  'src/argp-fs-xinl.c',  'src/argp-help.c',  'src/argp-parse.c',  'src/argp-pv.c',  'src/argp-xinl.c',  'src/getopt.c',  'src/getopt1.c',  'src/argp-pvh.c')# Configuration checks similar to CMake checkscc = meson.get_compiler('c')# Check for headershave_mempcpy_h = cc.has_header('mempcpy.h')have_strcase_h = cc.has_header('strcase.h')have_strchrnul_h = cc.has_header('strchrnul.h')have_strndup_h = cc.has_header('strndup.h')have_sysexits_h = cc.has_header('sysexits.h')have_unistd_h = cc.has_header('unistd.h')# Check for symbols and functionshave_asprintf = cc.has_function('asprintf')have_mempcpy = cc.has_function('mempcpy')have_random = cc.has_function('random')have_sleep = cc.has_function('sleep')have_strerror_r = cc.has_function('strerror_r')have_putc_unlocked = cc.has_function('putc_unlocked')have_fputs_unlocked = cc.has_function('fputs_unlocked')have_fwrite_unlocked = cc.has_function('fwrite_unlocked')have_strcasecmp = cc.has_function('strcasecmp')have_strchrnul = cc.has_function('strchrnul')have_strndup = cc.has_function('strndup')have_program_invocation_short_name = cc.has_function('program_invocation_short_name')have_program_invocation_name = cc.has_function('program_invocation_name')have_ssize_t = cc.has_type('ssize_t', dependencies : cc.find_library('c', required : false))# Generate config.h using the resultsconfig_h = configuration_data()config_h.set('HAVE_CONFIG_H', 1)config_h.set('HAVE_MEMPCPY_H', have_mempcpy_h)config_h.set('HAVE_STRCASE_H', have_strcase_h)config_h.set('HAVE_STRCHRNUL_H', have_strchrnul_h)config_h.set('HAVE_STRNDUP_H', have_strndup_h)config_h.set('HAVE_SYSEXITS_H', have_sysexits_h)config_h.set('HAVE_UNISTD_H', have_unistd_h)config_h.set('HAVE_ASPRINTF', have_asprintf)config_h.set('HAVE_MEMPCPY', have_mempcpy)config_h.set('HAVE_RANDOM', have_random)config_h.set('HAVE_SLEEP', have_sleep)config_h.set('HAVE_STRERROR_R', have_strerror_r)config_h.set('HAVE_DECL_PUTC_UNLOCKED', have_putc_unlocked)config_h.set('HAVE_DECL_FPUTS_UNLOCKED', have_fputs_unlocked)config_h.set('HAVE_DECL_FWRITE_UNLOCKED', have_fwrite_unlocked)config_h.set('HAVE_STRCASECMP', have_strcasecmp)config_h.set('HAVE_STRCHRNUL', have_strchrnul)config_h.set('HAVE_STRNDUP', have_strndup)config_h.set('HAVE_DECL_PROGRAM_INVOCATION_SHORT_NAME', have_program_invocation_short_name)config_h.set('HAVE_DECL_PROGRAM_INVOCATION_NAME', have_program_invocation_name)config_h.set('HAVE_SSIZE_T', have_ssize_t)# Write out config.hconfigure_file(  input: 'config.h.in.meson',  output: 'config.h',  configuration: config_h)argp_lib = static_library(  'argp',  sources: argp_sources,  c_args: argp_extra_cflags,  include_directories: gnulib_inc,  install: true,)argp_dep = declare_dependency(  link_with: argp_lib,  include_directories: gnulib_inc,)pkg = import('pkgconfig')pkg.generate(  libraries: argp_lib,  name: 'argp',  description: 'Gnulib argp library',  version: '1.0',  url: 'https://www.gnu.org/software/gnulib/',  subdirs: ['gnulib'],)meson.override_dependency('argp', argp_dep)
```

接下来就是引用它们到项目到中使用了。

两个项目的代码在这里：

https://github.com/feicong/libbpf

https://github.com/feicong/argp

![](https://mmbiz.qpic.cn/sz_mmbiz_png/k9S5z61JPnapvCqB5dP5zWd3VXzz2ZWU84vpLeup3KYlmwkicamOToZZwtIA3sHcPzSU7Ozlk6UCVib5zcKXCzsg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

软件安全与逆向分析

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/k9S5z61JPnagibFHbJibmtyCM7IOiajRiaM0NuA7VKhACWn9uohpR26icDoZHQ4zxQH0vURtcmFkh5vzR5icYmY6cmibg/0?wx_fmt=png)

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