---
title: 侧信道检测APatch Root
url: https://mp.weixin.qq.com/s/LbOgpyEMkmBMbUIv4Qo8Mw
source: Doonsec's feed
date: 2026-01-20
fetch_date: 2026-01-21T03:30:40.644223
---

# 侧信道检测APatch Root

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rz4DMhMn0gyyxych22uPcTQ1icFJiam1DTmicXn8vZSN5PZibFGyQJDfUJDWLJ3YKicVZjicVWJYSyzyXlOH4J3oLzUg/0?wx_fmt=jpeg)

# 侧信道检测APatch Root

原创

ru1n
ru1n

网络空间威胁观察

![]()

在小说阅读器中沉浸阅读

# 侧信道检测APatch Root

## 摘要

APatch在内核中HOOK了truncate(45号)系统调用，作为应用层请求ROOT权限的接口。如下是相关代码，它的含义如下：

* • 挑选truncate作为后门调用, 安装HOOK
* • 取调用的key与cmd参数, 如果参数校验通过, 进入后门调用, 否则进入正常调用
* ![](https://mmbiz.qpic.cn/mmbiz_png/rz4DMhMn0gyyxych22uPcTQ1icFJiam1DTnyQeoP14XHBelymWLGficruxZ50CU9Q5GvY5N3bu7S8tmy5rWAt5Rvg/640?wx_fmt=png&from=appmsg)
* 后门系统调用代码

由此可以得出检验方法：

1. 1. 设置key, cmd参数, **尽可能多**的触发后门调用中的代码, 计算执行时间为T1
2. 2. 设置key, cmd参数, **尽可能少**的触发后门调用中的代码, 计算执行时间为T2
3. 3. 在正常环境中, T1与T2应该接近, 因为都会触发truncate的参数检验提前返回
4. 4. 在APatch环境中, T1与T2应该有较大相差值

## 实现细节

检测代码如下, 基本逻辑如下:

* • 要将执行线程绑定到固定CPU核心上, 避免线程切换CPU核心产生影响
* • 设置参数1为su, 参数2在1000-1005执行若干次, 计算时间T1
* • 设置参数1为su, 参数2在994-999执行若干次, 计算时间T2
* • 在APatch环境中, T1与T2存在较大差异, 因为T1会执行更多后门代码, T2在后门代码开头即会退出
* • 在正常环境中, T1与T2基本无差异, 因为会在truncate函数入口处由于su文件不存在退出

```
#define _GNU_SOURCE

#include <sched.h>
#include <stdio.h>
#include <unistd.h>

static inline uint64_t get_ticks() {
  uint64_t v;
  asm volatile("isb; mrs %0, cntvct_el0; isb" : "=r"(v) : : "memory");
  return v;
}

void bind_to_cpu(int cpu_id) {
  cpu_set_t cpuset;
  CPU_ZERO(&cpuset);
  CPU_SET(cpu_id, &cpuset);

  if (sched_setaffinity(0, sizeof(cpu_set_t), &cpuset) == -1) {
    perror("sched_setaffinity");
  } else {
    printf("Thread successfully bound to CPU %d\n", cpu_id);
  }
}

int get_current_cpu() {
  int cpu = sched_getcpu();
  if (cpu == -1) {
    perror("sched_getcpu");
    return -1;
  }
  return cpu;
}

uint64_t runner(int cmd) {
  char buffer[3] = "su";

  uint64_t t1 = get_ticks();
  for (int i = 0; i < 10000; i++) {
    syscall(45, buffer, cmd);
  }
  uint64_t t2 = get_ticks();
  return t2 - t1;
}

int main(int argc, char *argv[]) {
  // 绑定cpu核心, 避免切换cpu核心对结果的影响
  bind_to_cpu(0);

  uint64_t d1 = 0, d2 = 0;
  for (int i = 0; i < 5; i++) {
    d2 += runner(0x999 - i);
  }
  for (int i = 0; i < 5; i++) {
    d1 += runner(0x1000 + i);
  }
  printf("Duration for cmd 0x1000: %lu tk\n", d1);
  printf("Duration for cmd 0x500 : %lu tk\n", d2);
  uint64_t diff = d1 > d2 ? d1 - d2 : d2 - d1;
  printf("Delta percentage: %.2f%%\n",
         (double)diff / ((double)(d1 + d2) / 2) * 100.0);
  return 0;
}
```

如下图所示, APatch环境中T1 T2差异较明显, 正常环境中T1 T2差异不明显

![](https://mmbiz.qpic.cn/mmbiz_png/rz4DMhMn0gyyxych22uPcTQ1icFJiam1DTyVSk5C7mKfYABEKhWlphf4dPqYUL1pPq58anZaibTXZic6HwmHUicKibCg/640?wx_fmt=png&from=appmsg)

APatch环境

![](https://mmbiz.qpic.cn/mmbiz_png/rz4DMhMn0gyyxych22uPcTQ1icFJiam1DTtX0m0vdWYXFIbwczvXmKeEt6de4AjD2EWOn2P9Ok1p5iaWwoLG3uIRw/640?wx_fmt=png&from=appmsg)

正常环境

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/rz4DMhMn0gzs9FAU1pqX9XWSZWW6Pz50RdduibppwzZrrhOkqhmtXeMoU6JKDswZ6bgdjNCmrATrBG8Myice8SpQ/0?wx_fmt=png)

网络空间威胁观察

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rz4DMhMn0gzs9FAU1pqX9XWSZWW6Pz50RdduibppwzZrrhOkqhmtXeMoU6JKDswZ6bgdjNCmrATrBG8Myice8SpQ/0?wx_fmt=png)

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