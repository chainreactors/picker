---
title: iOS安全开发中的Frida检测
url: https://www.anquanke.com/post/id/314115
source: 安全客-有思想的安全新媒体
date: 2025-12-31
fetch_date: 2026-01-01T03:35:24.254878
---

# iOS安全开发中的Frida检测

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# iOS安全开发中的Frida检测

阅读量**17544**

发布时间 : 2025-12-31 17:09:17

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

作者：luoyanbei[@360src](https://github.com/360src "@360src")

随着移动应用安全机制的不断加强，以 Frida 为代表的动态插桩工具，已成为移动端逆向分析的主流手段。相比反汇编、class-dump 等静态分析方式，Frida 几乎可以在不修改 App 本体的情况下，实时注入代码、Hook 任意函数、篡改参数与返回值，甚至直接操控业务逻辑执行流程。

在越狱的iOS设备上，Frida 可以通过 frida-server 以最高权限运行；在非越狱设备上，也可以通过 Frida Gadget、调试注入、重签名等方式完成动态分析。

在实际攻击场景中，Frida 已被广泛用于：
• 绕过登录、风控、反作弊等安全校验
• Hook 网络层以抓取或篡改敏感接口数据
• 直接调用内部私有方法，伪造正常业务流程
• 分析加密算法、关键参数生成逻辑
• 对安全检测逻辑本身进行反制与绕过

在 iOS App 中系统性地识别 Frida 的运行痕迹、注入特征和行为特征，并构建多层次的防御与对抗策略，已经成为移动端安全中不可回避的一环。本文将结合实际逆向与对抗经验，从安全开发的角度讲解frida检测相关特征。

## 1、检测frida默认端口号

如果设备上运行了 frida-server，并且使用默认端口号27042，App 尝试连接 127.0.0.1:27042，连接成功 说明当前环境下存在Frida使用27042端口。
具体检测端口代码：

```
#import <sys/socket.h>
#import <arpa/inet.h>
#import <fcntl.h>
#import <unistd.h>
#import <errno.h>

BOOL isFridaPortReallyOpen(void) {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) return NO;

    // 非阻塞
    fcntl(sockfd, F_SETFL, O_NONBLOCK);

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(27042);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    int ret = connect(sockfd, (struct sockaddr *)&addr, sizeof(addr));
    if (ret < 0 && errno != EINPROGRESS) {
        close(sockfd);
        return NO;
    }

    fd_set wfds;
    FD_ZERO(&wfds);
    FD_SET(sockfd, &wfds);

    struct timeval tv;
    tv.tv_sec = 0;
    tv.tv_usec = 300 * 1000; // 300ms

    ret = select(sockfd + 1, NULL, &wfds, NULL, &tv);
    if (ret <= 0) {
        close(sockfd);
        return NO;
    }

    // 关键：检查 SO_ERROR
    int so_error = 0;
    socklen_t len = sizeof(so_error);
    getsockopt(sockfd, SOL_SOCKET, SO_ERROR, &so_error, &len);

    close(sockfd);

    return so_error == 0;
}
```

调用方式

```
if (isFridaPortReallyOpen()) {
    NSLog(@"Frida 默认端口可访问");
    // 触发风控 / 上报
}
```

基于 Frida 默认端口号（27042）的检测并非绝对可靠。一方面，理论上该端口可能被其他进程占用，从而在极少数情况下产生误报；另一方面，Frida 本身支持通过参数或二次编译的方式修改默认监听端口，一旦攻击者对 Frida Server 进行了“魔改”或端口重定向，该检测方式就可能被直接绕过。

因此，端口号检测更适合作为低成本、快速命中的辅助判断条件，而不应作为唯一的判定依据。将其与虚拟内存特征检测等更底层、更难完全抹除的手段进行组合使用，才能在实际对抗中获得更稳定、可信的检测效果。

## 2、检测app虚拟内存特征

当 Frida 附加到 iOS App 时，Frida 的代码、数据、JS runtime、字符串全部被加载到“目标 App 进程的虚拟内存空间”中。
Frida 的 JavaScript Runtime 会把“脚本字符串”放入内存，例如：
require(“frida-objc-bridge”)
frida/runtime/core.js
Frida.\_loadObjC();

这些字符串来源于：
• 内置 JS 脚本（core.js）
• bridge 初始化代码
• RPC 协议字符串（frida:rpc）

JS 引擎必须把字符串展开为明文才能执行，所以这些字符串一定存在于堆或只读区。

（1） Frida attach 的真实技术路径

以最典型的 frida-server attach为例：

1. frida-server（系统进程）：
   * 通过**task\_for\_pid()** 拿到目标 App 的 task port
2. 在目标 App 中：
   * 创建远程线程（**thread\_create\_running**）
   * 调用**dlopen()** / Mach-O loader
3. Frida Agent 被加载：
   * 成为目标 App 的一个 dylib
   * 由 dyld 映射进App 的 VM

（2）app被frida附加后的特征关键词

| 序号 | 关键词 | 用途 |
| --- | --- | --- |
| 1 | frida\_gadget | 这是 Frida 在 native 层的“模块身份标识” |
| 2 | /frida-core/lib/gadget/gadget.vala | 错误定位，日志，断言信息 |
| 3 | frida/runtime/core.js | 定义：Module / Memory / Interceptor、RPC、调度器 |
| 4 | frida\_agent\_main | Agent 的 native 入口，相当于 main() / init |
| 5 | frida\_dylib\_range= | 这是 Frida 内部“自我感知内存边界”的关键字符串 |
| 6 | /frida-core/lib/agent/agent.vala | 错误定位，日志，断言信息 |
| 7 | frida:rpc | Agent <->Client 的通信协议前缀，JS / Native 双向调用标识 |
| 8 | Frida.\_loadObjC(); | 注册 ObjC / Java runtime，安装 hook handler |
| 9 | require(“frida-objc-bridge”); | Java / ObjC 方法解析，class 枚举，selector hook |
| 10 | /frida-core/lib/payload/spawn-monitor.vala | 错误定位，日志，断言信息 |
| 11 | FridaAgentRunner | 负责启动 JS runtime，管理 lifecycle |
| 12 | FridaSpawnHandler | 处理 spawn / attach 事件，与 server 协同 |
| 13 | FridaPortalClient | Agent RPC / IPC 客户端，与 frida-server 通信 |
| 14 | FridaAgentController | Agent 总控，管理模块、脚本、session |
| 15 | frida.Error. | JS Error 类型，Native → JS 异常封装 |

（3）内存检测frida特征

检测函数 `checkAppMemoryForFrida` 的工作流程：

1) 初始化

* 获取当前进程 task，自地址 0 开始遍历虚拟内存区域。
* 调用 `init_self_image_range` 记录自身镜像范围，后续跳过本进程主二进制区域。

2) 遍历内存区域

* 使用 `vm_region_64` 逐段获取区域起始地址、大小和保护属性。
* 如果区域属于自身镜像则跳过；非 `VM_PROT_READ` 区域也跳过。

3) 读取并扫描

* 为区域大小分配缓冲区，`vm_read_overwrite` 读取该区域内容。
* 遍历明文特征数组 `kFridaPlainList`（包含 Frida 相关字符串，如 `frida_gadget`、`frida/runtime/core.js`、`FridaAgentRunner` 等），对每个特征调用 `memory_contains` 在该缓冲区内查找。

4) 命中处理与日志

* 如命中，`hitCount++`，并使用 `dladdr` 获取当前区域地址对应的模块路径，提取文件名，记录日志：
  + 内存检测到的特征
  + 地址（十六进制）
  + 模块名
  + hitCount

5) 后续与回调

* 释放缓冲区，继续下一个区域；若 `vm_region_64` 失败则结束循环。
* 扫描结束：若 `hitCount > 0` 且传入了 `onDetected`，则执行回调；最后返回 `hitCount`。

```
#include <string.h>
#include <stdio.h>
#include <mach/mach.h>
#include <mach-o/dyld.h>
#include <dlfcn.h>
#include <mach-o/dyld.h>
#include <mach-o/loader.h>
#include <sys/sysctl.h>
#include <unistd.h>
#include <stdbool.h>

static void *self_image_start = NULL;
static void *self_image_end   = NULL;

// 根据内存地址查找所属的模块名称（使用 dladdr）
static const char *find_module_for_address(vm_address_t addr) {
    Dl_info info;
    if (dladdr((void *)addr, &info)) {
        if (info.dli_fname) {
            return info.dli_fname;
        }
    }
    return "unknown";
}

// 日志文件相关
static NSString *ProtecToolLogFilePath(void) {
    static NSString *logPath = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        NSArray<NSString *> *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
        NSString *docDir = paths.firstObject ?: NSTemporaryDirectory();
        logPath = [docDir stringByAppendingPathComponent:@"protec_log.txt"];
    });
    return logPath;
}

static void ProtecToolWriteLog(NSString *message) {
    if (message.length == 0) return;
    NSString *line = [message stringByAppendingString:@"\n"];
    NSData *data = [line dataUsingEncoding:NSUTF8StringEncoding];
    if (!data) return;

    NSString *path = ProtecToolLogFilePath();
    NSFileManager *fm = [NSFileManager defaultManager];
    if (![fm fileExistsAtPath:path]) {
        [data writeToFile:path atomically:YES];
    } else {
        NSFileHandle *fh = [NSFileHandle fileHandleForWritingAtPath:path];
        if (!fh) return;
        @try {
            [fh seekToEndOfFile];
            [fh writeData:data];
        } @catch (__unused NSException *e) {
        } @finally {
            [fh closeFile];
        }
    }
}

void ProtecToolClearLogFile(void) {
    NSString *path = ProtecToolLogFilePath();
    if (!path) return;
    NSFileManager *fm = [NSFileManager defaultManager];
    if ([fm fileExistsAtPath:path]) {
        [fm removeItemAtPath:path error:nil];
    }
}

NSString *ProtecToolReadLog(void) {
    NSString *path = ProtecToolLogFilePath();
    if (!path) return @"";
    NSError *error = nil;
    NSString *content = [NSString stringWithContentsOfFile:path encoding:NSUTF8StringEncoding error:&error];
    if (!content || error) {
        return @"";
    }
    return content;
}

#define PTLog(fmt, ...) do { \
    NSString *msg__ = [NSString stringWithFormat:(fmt), ##__VA_ARGS__]; \
    NSLog(@"%@", msg__); \
    ProtecToolWriteLog(msg__); \
} while(0)

static void init_self_image_range(void) {
    if (self_image_start) return;

    Dl_info info;
    if (!dladdr((void *)&init_self_image_range, &info))
        return;

    self_image_start = info.dli_fbase;

    for (uint32_t i = 0; i < _dyld_image_count(); i++) {
        if (_dyld_get_image_header(i) == info.dli_fbase) {
            const struct mach_header_64 *mh =
                (const struct mach_header_64 *)_dyld_get_image_header(i);
            intptr_t slide = _dyld_get_image_vmaddr_slide(i);

            uintptr_t maxEnd = 0;
            const struct load_command *cmd =
                (const struct load_command *)((uintptr_t)mh + sizeof(*mh));

        ...