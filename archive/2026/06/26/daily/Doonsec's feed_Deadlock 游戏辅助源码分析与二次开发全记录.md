---
title: Deadlock 游戏辅助源码分析与二次开发全记录
url: https://mp.weixin.qq.com/s/zyO03kXz2KS8VIkha_aF2Q
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:47:35.831967
---

# Deadlock 游戏辅助源码分析与二次开发全记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1lTVvrCDyKCyN2WZwibkmUJ0cWw9I6aJl2vpKww19xkHkdEVBNd9Kzl5RohYQ3nnEiao4lnpfyrHb0O2k3TmmwvwdTeibSSaLZ48/0?wx_fmt=jpeg)

# Deadlock 游戏辅助源码分析与二次开发全记录

刘宝
刘宝

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 一、前言

* 仅用于学习交流，勿用于非法用途
* Deadlock 是 Valve 基于 Source 2 引擎开发的 MOBA+射击游戏（Steam AppID: 1422450）。本文记录了对开源项目 Andromeda-DeadLock 的逆向分析、跨版本适配、源码修改与定制化开发的全过程，涵盖字节模式扫描、Schema 系统分析、ImGui 菜单汉化、自瞄骨骼数据生成、以及离线许可系统的设计与实现。

## 二、项目架构分析

### 2.1 整体结构

```
Andromeda-DeadLock-Base/ (VS DLL项目)
├── DllMain.cpp                    # DLL入口
├── DeadLock/
│   ├── Hook/                      # 12个MinHook引擎钩子
│   ├── SDK/                       # 逆向的Source2 SDK封装
│   │   ├── CFunctionList.hpp      # 19个字节模式函数查找
│   │   ├── CSchemaOffset.cpp      # 运行时Schema字段偏移解析
│   │   └── Interface/             # 引擎接口封装
│   └── Protobuf/                  # 94个预编译protobuf文件
├── AndromedaClient/
│   ├── Features/
│   │   ├── CAimbot/               # 自瞄 (轨迹预测/惯性/AntiFrog)
│   │   ├── CVisual/               # ESP (方框/骨骼/Chams/观战)
│   │   ├── CMisc/                 # 自动格挡/换弹
│   │   └── CHeroes/               # 英雄专属功能
│   └── GUI/                       # ImGui渲染菜单
└── GameClient/                     # 实体缓存/控制器封装
```

### 2.2 Hook 链分析

项目通过 MinHook 挂载了 12 个关键函数：

| Hook 点 | 所在 DLL | 用途 |
| --- | --- | --- |
| CreateMove | client.dll | 自瞄角度写入 |
| FireEventClientSide | client.dll | 游戏事件拦截 |
| OnAddEntity / OnRemoveEntity | client.dll | 实体缓存更新 |
| ParseMessage | engine2.dll | 网络消息解析（伤害事件） |
| OnClientOutput | engine2.dll | 客户端渲染回调 |
| GetMatricesForView | client.dll | 视图矩阵获取 |
| DrawModel | scenesystem.dll | Chams 模型上色 |
| Present / ResizeBuffers | GameOverlayRenderer64.dll | D3D11 渲染层注入 |

### 2.3 Schema 系统

这是项目最精巧的设计。Source 2 引擎提供了 `schemasystem.dll`，其中包含所有实体类的字段名→偏移映射。`CSchemaOffset.cpp` 在运行时遍历所有 TypeScope，动态读取 `CSchemaClassBinding` 结构的成员偏移，存入 `unordered_map<string, unordered_map<string, uint32_t>>`。

这意味着游戏更新导致实体字段偏移变化时，**无需重新逆向**，运行时自动解析。

### 2.4 字节模式系统

对于非 Schema 暴露的函数（如 `CalcWorldSpaceBones`、`ScreenTransform`），项目通过 `CBasePattern` 在 DLL 加载时执行 AOB（Array of Bytes）扫描定位：

```
// 示例：通过函数头字节码定位
CBasePatternScreenTransform = {
"ScreenTransform",
"33 C0 48 39 05 ? ? ? ? 0F 84", // 字节模式，?? 为通配符
    CLIENT_DLL,
0,
    SEARCH_TYPE_NONE
};
```

支持三种扫描类型：直接匹配、CALL指令追踪（`SEARCH_TYPE_CALL`）、LEA RIP相对寻址（`SEARCH_TYPE_PTR2`）。

## 三、跨版本适配

### 3.1 模式扫描器

拿到源码之后我想着能不能自己扫描进行适配，发现还真可以，使用AI进行批量文件扫描进行版本适配几乎可以无脑适配，但是适配之后骨骼和aimbot失效后续我也解决了！

编写了 Python 脚本 `pattern_scan.py`，通过 Boyer-Moore 风格的通配符匹配算法，一次性扫描所有目标 DLL：

```
# 核心扫描逻辑
def scan(data, pat_bytes, mask):
    n = len(pat_bytes)
    first_byte = pat_bytes[first_lit]  # 首个固定字节
    pos = data.find(first_byte)        # 快速定位候选
    ...
```

对 8 个 DLL 的 35 个模式进行批量扫描，输出命中/缺失/歧义三类结果。

### 3.2 结果

针对新版 Deadlock（ClientVersion 6536），扫描结果 **30/32 OK，0 MISS**，仅 CameraManager 和 CreateMaterial 存在歧义（2 处命中指向同一地址），确认无需修改即可运行。

## 四、源码修改

### 4.1 中文本地化

本人英文不好所以手动给他添加了所有的翻译工程，然后重新编译即可
![图片描述](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1FQhwC4Cnn62vo8RxFx13HwUdO2JiagfOP1SkBYL52Vu5glO6icfb82QvCEXgXa8KqP2syO7R3heawNjBHojgibXGbBJiaianPdz5A/640?wx_fmt=other&from=appmsg)

新增 `LangHelper.hpp` 翻译宏：

```
#defineL(en, cn) (GetMisc()->Language == 1 ? cn : en)
```

遍历 17 个菜单文件的数百处 `XorStr("English")` 替换为 `L("English", "中文")`。

同时为 ImGui 字体系统添加 CJK Merge Font（`msyh.ttc`），解决中文字符显示为方框的问题。

添加 `/utf-8` MSVC 编译标志，确保 UTF-8 字符串在 GBK 环境下正确编译。

### 4.2 DLL重命名

* 原始DLL编译出来的需要原始自带的注入器，但是我看了就是远程线程注入，而VITTLOCK的注入器是能够规避V社 DeadLock的检测，游戏我并没有去逆向，没那个实力，但是在测试过程中我尝试打开IDAPro 游戏并没有响应的措施进行阻拦，例如WeGame的黑客弹窗 闪退游戏这些措施；大牛可以自己逆向一下
* 由于没有使用原来的注入器，而是使用的VITTLOCK的注入器，所以将编译的Dll 更名为VITTLOCK.dll 即可，VITTLOCK是扫描同级目录VITTLOCK.dll 进行注入的；不过我怀疑他们用的也是同一套源码 因为注入之后界面几乎一样，他也只是加了一个静默自瞄（范围子弹命中，相关技术可浏览UC帖子 有大牛传授技术）
* `CHEAT_NAME`

  宏 → "L I V E L O C K"，即可修改标题名称
* Wrapper 控制台 ASCII Art → LIVELOCK 大字
* ImGui 窗口标题 → LIVE LOCK

###

### 4.3 配置持久化

* 因为我将dll和注入器exe进行了打包，方便部署本地；我想着避免dll和exe落地能使用着方便，大牛能直接断点api dump下完整文件
* 被我这么一搞他检测不到dll了文件貌似没创建成功，所以我重新修改了源码进行本地存储配置，方便下次加载直接加载配置文件，就不用每次都手动改配置了

原始代码通过 `GetDllDir()` 获取 DLL 所在目录作为配置路径。由于 DLL 被注入器提取到 `%TEMP%\随机目录`，注入完成后被全零覆盖删除，导致配置不保存。

修改 `CSettingsJson.cpp`，新增 `GetConfigDir()`：

```
static std::string GetConfigDir() {
    char path[MAX_PATH];
SHGetFolderPathA(nullptr, CSIDL_APPDATA, nullptr, 0, path);
    std::string dir = std::string(path) + "\\LiveLock\\";
CreateDirectoryA(dir.c_str(), nullptr);
    return dir;
}
```

配置保存到 `%APPDATA%\LiveLock\`，永久保留。
![图片描述](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3bWX6NnKEicuVOdjxdDJK4pdG0OcKqqjZianQXe3zcHLpKkdSgPLJD7tBibugkyFAQFXuIaXA8rwdZcc7jnYAUHUVZLbENrcmJLg/640?wx_fmt=other&from=appmsg)

### 4.4 自瞄骨骼 Fallback

原始项目依赖 `HeroSkeletonPairs.hpp` 中的预先提取的骨骼映射表。由于 BoneExtractor 源码缺失，初版使用空存根导致自瞄无法锁定目标。

* 添加了基于 `m_vecAbsOrigin() + Z偏移` 的无骨骼 Fallback；由于作者并没有发布骨骼数据这部分数据，所以只能自己做去找骨骼数据了，神通广大的UC果然有大神发布骨骼数据，我就直接拿来现成的直接提取出来就OK了，另外做了一个Fallback

```
// 无骨骼数据时，使用实体原点+垂直偏移估算各部位位置
Vector3 aimPos = pNode->m_vecAbsOrigin();
float zOff = (bone.slot == HitboxSlot::Head) ? 72.f :
             (bone.slot == HitboxSlot::Neck) ? 64.f : 48.f;
aimPos.m_z += zOff;
//-------------------------------------------------------------------
const auto* boneList = GetCL_Bones()->GetHitboxBones(pPawn, bone.slot);
if (boneList && !boneList->empty()) {
// 原版路径：精确骨骼坐标
for (const int16_t bid : *boneList) {
        pNode->GetBonePosition(bid, bonePos);  // ← 读骨骼矩阵
Trace_IsVisibleEx(..., bonePos);       // ← 射线检测
WorldToScreen(bonePos, screen);        // ← 投影到屏幕
    }
}
else {
// Fallback：用实体原点 + Z轴偏移估算
    Vector3 aimPos = pNode->m_vecAbsOrigin();  // ← 实体脚下坐标 (X, Y, Z↓)
    aimPos.m_z += 72.f;  // 头部：脚下 + 72 单位
// Neck: +64, Torso: +48, Arms: +38, Legs: +12

// 跳过 Trace_IsVisible（不需要射线检测，避免 Trace 系统兼容问题）
WorldToScreen(aimPos, screen);  // 直接投影
}
```

### 4.5 自瞄默认开关

`CAimbot.hpp` 中 `bool Active = false;` 改为 `true;`，避免用户找不到开关。

##

## 五、BoneExtractor 骨骼数据生成、VPK 逆向：从游戏文件中提取骨骼数据

从 UC 获取 Deadlock-BoneExtractor 源码，其对游戏 VPK 文件（Valve Pak）执行解析：

### 5.1 问题背景

Andromeda 的自瞄和骨骼 ESP 都依赖 `HeroSkeletonPairs.hpp` 中预先提取的骨骼数据：

```
// 每个英雄模型对应一份
struct ModelBoneData {
    vector<BonePair> pairs;         // 父子骨骼连接 (用于骨架线绘制)
    unordered_map<string, int> ids;  // 骨骼名 → 运行时 ID
    vector<int16_t> slotBones[5];   // Head/Neck/Torso/Arms/Legs 部位骨骼列表
};
```

VPK读取 → 遍历 4966 个 .vmdl\_c 条目
       → 过滤英雄模型路径
       → 解析 ValveResourceFormat 提取骨骼名称/ID
       → 构建 slotBones 部位分类 (Head/Neck/Torso/Arms/Legs)
       → 生成 C++ 头文件

源码仓库中的 `HeroSkeletonPairs.hpp` 仅包含一个空存根 `g_HeroModelData = {}`，因为完整的骨骼数据由 PreBuildEvent 调用 BoneExtractor 运行生成后填入。此步骤需要 .NET SDK 且 BoneExtractor 源码在主仓库中缺失的。直接编译后所有 `GetHitboxBones()` 调用返回 `nullptr`，导致自瞄无法锁定目标和骨骼 ESP 无法绘制。

### 5.2 方案对比

最初尝试了三种途径：

| 方案 | 方法 | 结果 |
| --- | --- | --- |
| IDA 提取 VITTLOCK.dll | 从 .rdata 段解析 STL 容器结构 | 数据嵌入在 133KB 静态初始化函数 `sub_180008530` 中，手动提取不现实 |
| 手写 VPK Python 解析器 | 按 VPK v2 二进制格式逐字节读取 | 成功定位目录树，但模型路径字符编码异常中止 |
| BoneExtractor 原版工具 | 从 GitHub 获取源码，配置 .NET 环境运行 | **成功生成 63 个英雄的完整数据** |

### 5.3 VPK 文件格式分析

Deadlock 的资源存储在 `game\citadel\pak01_dir.vpk`（索引文件，6.5MB）和 `pak01_000.vpk ~ pak01_270.vpk`（数据分片）中。

VPK v2 的文件头结构：

```
Offset  Size  Field
0x00    4     Magic =0x55AA1234
0x04    4     Version =2
0x08    4     TreeSize (目录树字节数)
0x0C    4     FileDataSectionSize
0x10    4     ArchiveMD5SectionSize
0x14    4     OtherMD5SectionSize
0x18    4     SignatureSectionSize
```

依赖 .NET 10.0 + ValveResourceFormat NuGet 包。生成 63 个英雄模型、总计 235KB 的 `HeroSkeletonPairs.hpp`。

**目录树定位**：`TreeOffset = FileSize - TreeSize`

### VPK 分析尝试

目录树中每个文件条目为 18 字节。

在等待 .NET 10 SDK 期间，手动解析了 VPK v2 二进制格式：

```
Offset  Size  Field
0x00    4     CRC32
0x04    2     PreloadBytes
0x06    2     ArchiveIndex (对应 pak01_XXX.vpk 的分片编号)
0x08    4     EntryOffset  (分片文件内的字节偏移)
0x0C    4     EntryLength  (压缩前大小)
0x10    2     Terminator =0xFFFF
```

条目按 `Extension → Path → Filename` 的三层树结构组织。遍历时以空字符串标记层级结束。

手动编写 Python VPK 解析器成功定位到扩展名 `vmdl_c` 下的 152 个英雄模型路径，但 `latin-1` 编码的目录名在 UTF-8 转换时触发 `UnicodeDecodeError`。

### 5.4 BoneExtractor 源码分析

工具的核心逻辑：

``...