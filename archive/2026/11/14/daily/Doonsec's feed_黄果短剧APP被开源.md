---
title: 黄果短剧APP被开源
url: https://mp.weixin.qq.com/s/-GLotugb0mEt3aXY269XbQ
source: Doonsec's feed
date: 2026-11-14
fetch_date: 2026-11-15T08:36:47.251940
---

# 黄果短剧APP被开源

# 黄果短剧APP被开源

原创

星宇Sec
星宇Sec

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年11月，一个名为HGhub的仓库在GitHub上出现，短时间内拿到约8800个star和6300余次fork，随后又被作者主动清空。

## 一、事件经过

### 仓库的出现与爆发

2026年11月3日，仓库建立，首个提交信息为"feat: HGhub黄果短剧客户端首个开源版本"。此后进入高频迭代：到11月10日，主干累计88个提交，贡献者包括kkylin-si、WEP-56、WEP、leeguooooo、ker0491、LNP等十余人，提交内容覆盖macOS适配、iOS原生转屏、Android手势与硬件返回键、HLS播放稳定性、正文渲染加固、Linux构建等方向。

![HGhub界面截图](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpRfE5ZdWB6j3WnOCHXbF0KZvqq3TkjA66ibVSZ5Fz9wGZlKV9cLEjMynzyLbsczlKDQw9cxWGGC9SSFxPSBdDWNeT29xegR3cI/640?wx_fmt=webp&from=appmsg)

HGhub界面截图

### 仓库被清空

11月12日，作者清空全部代码、Release与构建记录，仓库只保留一份停更说明。说明中写明决定"出于个人原因停止维护"，并特意交代"我一切平安，没有被任何上游或机构处理"。

同一天，作者在Issue#64中补充了更完整的表述：

> 删库举措实属无奈，我需要保护上游与自身的安全。

> 或许未来，我会以全新的架构重构HGhub，通过JS插件机制加载数据源，使项目本身与具体的数据源实现解耦，从根本上改变原有的技术路线。

这段话透露了两个信息。一是下架的直接动因与上游和作者自身处境有关；二是作者对项目形态有过反思，认为把数据源硬编码进客户端是根本问题，后续希望用插件机制把"壳"和"源"拆开。

### 围绕事件的两种叙事

仓库清空后，X平台上出现一位用户（@kamrynchohon4）发布的长文，自称是"愤然离职的黄果码农"，详细描述在公司的经历，并声称自己是本项目的开源推动者。

作者在Issue#65中直接否认了这一说法：仓库的创建、维护和清空均由本人完成，与"离职开源"情节无关。同一份公告还指出，该长文推荐的若干站点（包括带huangguoduanju等相似域名的网站）并非项目或已知官方渠道，并说明项目与任何"黄果"官方团队不存在雇佣或合作关系。

因此，把这次开源理解为"某公司员工把自家App的代码放出来"，与公开记录不符。更准确的描述是：一位个人开发者把自己写的第三方客户端开源，随后因上游与自身安全考量主动下架，期间被卷入一段与事实不符的叙事。

### 许可证的两段历史

仓库的许可证在生命周期内发生过一次变化：

| 版本 | 许可证 |
| --- | --- |
| v1.0.1及更早 | MIT |
| v1.1.0起 | PolyForm Noncommercial 1.0.0 |

MIT允许商用，PolyForm Noncommercial明确禁止商业用途，包括销售、广告变现、卡密、VIP与付费解锁。已经按MIT取得的授权不因换证而撤回，这是许可证变更的一般规则。当前流通的代码副本若来自v1.1.0之后，适用非商业条款。

## 二、项目介绍

### 定位

HGhub是一个跨平台短剧客户端，支持Windows、macOS、Linux、Android与iOS五个平台。它不生产内容，也不运营服务端，只做一件事：把上游站点的网页接口与媒体流，包装成原生应用的体验。

技术栈如下：

| 层 | 技术 |
| --- | --- |
| 应用框架 | Rust、Tauri 2 |
| 界面 | React 19、TypeScript、Vite 7、Tailwind CSS 4 |
| 播放 | hls.js 1.6 |
| 网络 | reqwest、rustls |

仓库代码约9500行，前端约5000行TypeScript/TSX，Rust侧约4400行。

### 架构：前端管界面，Rust管网络与媒体

这个项目最值得研究的地方在于职责划分。WebView里的前端不直接访问上游，所有网络与媒体处理都下沉到Rust：

```
React页面与播放器
   │ invoke("api_*")                 │ fetch hg://localhost/{img,hls,seg}
   ▼                                 ▼
Rust命令层（api.rs）                 本地自定义协议（media.rs）
   │                                 │
   ▼                                 ▼
reqwest ── POST /api/edge/request ──► 上游站点
```

这样设计解决了三个WebView场景下的硬问题：

第一，CORS。上游的HLS分片与密钥不允许跨域读取，WebView里的`video`元素无法直接播放。客户端把整个媒体层搬到Rust，由本地协议`hg://localhost/seg?u=`代为请求，前端只看到同源地址。

第二，防盗链与加密。封面图是AES-128-CBC密文，m3u8里的key与分片带有时效签名。Rust侧负责解密封面、逐行改写播放列表，把`URI`属性与分片地址统一替换成本地协议地址，并保留原始签名查询串。

第三，地址策略。所有出站请求经过统一校验：只允许HTTP(S)，拒绝URL中的用户名密码，拒绝私网与回环地址，对DNS结果做固定与混合公私网整体拒绝，FakeIP段`198.18.0.0/15`作为明确例外放行。带凭据的POST不跟随重定向，避免307/308重发密码。

### 上游接口的信封结构

上游把全部业务接口收敛成一个网关：

```
POST https://<线路域名>/api/edge/request
{
  "method": "GET",
  "path": "/api/videos?page=1&size=20",
  "body": "<base64>",
  "content_type": "application/json"
}
```

客户端只实现这一个入口，其余接口都是填`path`。这也是为什么"切换线路"在实现上等价于换一个`base`：上游只是域名在变，请求链路与数据模型完全一致。

### 线路与会话

固定线路写死在`src-tauri/src/lines.rs`，为`https://huangguoai.com`与`https://huangguoai.ai`。镜像线路在运行时从地址发布页抓取`publish.js`解析得到，上限60条。

账号只对两个固定站点开放，镜像线路仅支持游客浏览。token与具体origin绑定，跨站切换会清除登录状态，在途请求持有自己的站点快照，避免旧token被带到新站点。

### 目录结构

```
src/                    界面、交互、状态管理与组件
  components/Feed.tsx   核心播放页，手势、面板、剧场模式
  components/VideoSurface.tsx  hls.js播放内核封装
  api.ts                接口封装与本地协议地址
  html.ts               正文清洗与图片代理
  store.tsx             Context状态管理
src-tauri/src/
  api.rs                Tauri命令层
  net.rs                网络层、信封请求、代理
  network_policy.rs     目标地址校验
  media.rs              封面解密、HLS代理、缓存
  lines.rs              线路与镜像
  session.rs            会话持久化
  playback_log.rs       播放诊断日志
scripts/                构建与回归脚本
tests/                  浏览器回归页面
docs/                   技术说明
```

## 三、编译前的统一准备

### 版本要求

| 依赖 | 版本 |
| --- | --- |
| Node.js | 22 |
| pnpm | 10 |
| Rust | 1.90或更高 |

### 获取代码与安装依赖

```
git clone <仓库地址见文末> HGhub
cd HGhub
pnpm install --frozen-lockfile
```

`pnpm-lock.yaml`已锁定全部依赖版本，务必使用`--frozen-lockfile`，否则可能拉到与代码不匹配的次版本。

项目在`.npmrc`与`pnpm-workspace.yaml`中固定了`node-linker=hoisted`。这是为exFAT等不支持符号链接的文件系统准备的，不要把依赖目录迁到不支持的卷上。

### 国内网络环境下的依赖加速

默认源在国内经常超时，构建前建议先把两处镜像配好。cargo配置放在项目内的`src-tauri/.cargo/config.toml`，不会影响系统的`~/.cargo`：

```
[source.crates-io]
replace-with = "rsproxy"

[source.rsproxy]
registry = "sparse+https://rsproxy.cn/index/"

[net]
git-fetch-with-cli = true
```

pnpm可以临时指定镜像：

```
pnpm config set registry https://registry.npmmirror.com
```

Rust工具链本身也能换镜像，设置环境变量后安装：

```
export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup
export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup
```

### 版本号维护

版本号只在`package.json`与`src-tauri/tauri.conf.json`两处维护，前端界面里的版本由Vite构建时注入`__APP_VERSION__`，避免写死后漂移。修改版本时两处必须同步，CI会按tag自动改写。

## 四、Windows

### 环境

* Visual Studio 2022生成工具，勾选"使用C++的桌面开发"
* WebView2运行时（Windows 10 1803以上通常已内置）
* Rust stable，目标`x86_64-pc-windows-msvc`
* Node.js 22、pnpm 10

### 构建

```
pnpm install --frozen-lockfile
pnpm tauri build --bundles nsis
```

### 产物

| 类型 | 路径 |
| --- | --- |
| NSIS安装包 | `src-tauri/target/release/bundle/nsis/*.exe` |
| 可执行文件 | `src-tauri/target/release/huangguo-client.exe` |

需要便携版时，把`huangguo-client.exe`单独取出即可，它不依赖安装目录。CI中的做法是把该文件重命名为`HGhub.exe`后打成zip。

### 注意

窗口配置为`decorations: false`，标题栏与边缘缩放热区由前端自绘，缩放热区只在Windows下启用。若自行修改窗口样式，需要同步检查`src/components/ResizeHandles.tsx`与`src/components/DesktopChrome.tsx`。

## 五、macOS

### 环境

* macOS 12以上
* Xcode或Command Line Tools
* Rust stable，按目标添加`aarch64-apple-darwin`与`x86_64-apple-darwin`
* Node.js 22、pnpm 10

```
rustup target add aarch64-apple-darwin x86_64-apple-darwin
```

### 构建

macOS使用独立配置`src-tauri/tauri.macos.conf.json`，该配置把窗口改为系统原生装饰并启用`titleBarStyle: Overlay`，红绿灯位置由`trafficLightPosition`指定：

```
# Apple Silicon
pnpm tauri build --config src-tauri/tauri.macos.conf.json --target aarch64-apple-darwin

# Intel
pnpm tauri build --config src-tauri/tauri.macos.conf.json --target x86_64-apple-darwin

# 通用二进制
pnpm tauri build --config src-tauri/tauri.macos.conf.json --target universal-apple-darwin
```

### 产物

| 类型 | 路径 |
| --- | --- |
| 应用包 | `src-tauri/target/<target>/release/bundle/macos/HGhub.app` |
| 磁盘映像 | `src-tauri/target/<target>/release/bundle/dmg/*.dmg` |

### 签名与首次打开

配置中的`signingIdentity: "-"`表示ad-hoc签名，适用于本地使用，不涉及开发者证书。未经公证的构建在其他机器上首次打开会被Gatekeeper拦截，可执行：

```
xattr -cr /Applications/HGhub.app
```

### 原生细节

macOS的红绿灯垂直居中通过AppKit读取按钮尺寸后重设窗口位置实现，代码在`src-tauri/src/macos_titlebar.rs`，仅在macOS目标编译。主窗口在该平台延迟创建，因此`tauri.macos.conf.json`中`create`为`false`。

## 六、Linux

### 环境

以Debian/Ubuntu为例：

```
sudo apt-get update
sudo apt-get install -y \
  libwebkit2gtk-4.1-dev libgtk-3-dev libsoup-3.0-dev librsvg2-dev \
  build-essential pkg-config libssl-dev patchelf \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
```

GStreamer系列包用于HLS解码。缺少`plugins-bad`与`libav`时，部分编码的流会黑屏或无声。

### 构建

```
pnpm install --frozen-lockfile
pnpm tauri build --bundles deb appimage
```

### 产物

| 类型 | 路径 |
| --- | --- |
| deb包 | `src-tauri/target/release/bundle/deb/*.deb` |
| AppImage | `src-tauri/target/release/bundle/appimage/*.AppImage` |

### 注意

自定义协议在Linux上使用`hg://localhost`，与Windows/Android的`http://hg.localhost`不同。`src-tauri/src/media.rs`的`LOCAL_ORIGIN`与前端`src/api.ts`的`LOCAL`必须一致，否则封面与视频全部无法加载。

部分Wayland环境与旧版WebKitGTK存在EGL初始化问题，表现为整窗黑屏。仓库的历史提交中有针对性的环境变量规避，若自行升级系统库后出现黑屏，可先用X11会话验证。

## 七、Android

### 环境

* JDK 17或更高（CI使用17，21亦可）
* Android SDK：`platform-tools`、`platforms;android-36`、`build-tools;36.0.0`
* Android NDK：`28.2.13676358`
* Rust目标：`aarch64-linux-android`、`armv7-linux-androideabi`、`i686-linux-android`、`x86_64-linux-android`

```
rustup target add aarch64-linux-android armv7-linux-androideabi \
  i686-linux-android x86_64-linux-android
```

### 安装SDK组件

```
export ANDROID_HOME=$HOME/Library/Android/sdk      # macOS
export NDK_HOME=$ANDROID_HOME/ndk/28.2.13676358

yes | "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" \
  "platform-tools" "platforms;android-36" "build-tools;36.0.0" \
  "ndk;28.2.13676358"
```

NDK版本需要与`tauri android init`期望...