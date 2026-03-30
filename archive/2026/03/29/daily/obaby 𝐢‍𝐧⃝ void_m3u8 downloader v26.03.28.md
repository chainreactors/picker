---
title: m3u8 downloader v26.03.28
url: https://zhongxiaojie.cn/2026/03/741/
source: obaby 𝐢‍𝐧⃝ void
date: 2026-03-29
fetch_date: 2026-03-30T04:38:30.680945
---

# m3u8 downloader v26.03.28

[![obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/wp-content/uploads/2026/01/new-logo-27.png)](https://zhongxiaojie.cn)

程序媛 / 独立开发者 / 智商不稳定的女神经

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

 [Menu](#mobilemenu)

* [❈闺蜜圈|Pink Daily❈](https://zhongxiaojie.cn/pinkdaily/)
* [❈说说|Tweet❈](https://zhongxiaojie.cn/tweet/)
* [❈留言|Talk❈](https://zhongxiaojie.cn/talk/)
* [❈集美们|Besties❈](https://zhongxiaojie.cn/besties/)
* [❈关于|About❈](https://zhongxiaojie.cn/about/)

[程序媛](https://zhongxiaojie.cn/category/code-girl/)

# m3u8 downloader v26.03.28

2026年3月29日 21:58
[16 条评论](https://zhongxiaojie.cn/2026/03/741/#comments)

[![](https://zhongxiaojie.cn/wp-content/uploads/2026/03/330A0371-scaled.jpg)](https://zhongxiaojie.cn/wp-content/uploads/2026/03/330A0371.jpg)

基于 **ffmpeg** 的 m3u8 / 归档页解析下载工具，支持单链接、批量 CSV/文本、自定义输出目录与 ffmpeg 路径。

| 参数 | 说明 |
| --- | --- |
| `-i` | 输入：直链 m3u8、含 `archives` 的归档详情页、或带 `cms_player` 的播放页；也支持 `.mp4` / `.avi` / `.mov` / `.mpeg` 直链（走 HTTP 分段下载，非 ffmpeg） |
| `-o` | 输出文件名（自动补 `.mp4`）；对部分模式用于覆盖默认标题名 |
| `-p` | 输出目录；可为本机路径或 UNC（如 `\\服务器\共享\目录`） |
| `-f` | 批量输入文件：`.csv` 或纯文本（每行一个链接） |
| `-m` | 指定 ffmpeg 可执行文件路径 |

**注意：** 必须提供 `-i` 或 `-f` 之一。

### 单条示例

```
python m3u8_downloader.py -i "https://example.com/video.m3u8?token=xxx" -o myvideo -p D:\Videos
```

批量 CSV

* 编码建议 **UTF-8（含 BOM 亦可）**，表头需包含列 **`link`**；可选列 **`name`**（用于在部分逻辑里拼接输出名后缀，空单元格按空字符串处理，不会出现 `nan` 文件名）。
* 会跳过空的 `link` 或内容为 `link` 的占位行。
* 按行 **顺序执行**：上一任务结束（含 ffmpeg）后才会处理下一行。

```
python m3u8_downloader.py -f list.csv -p "\\192.168.1.12\media\Videos"
```

```
纯文本列表
```

每行一个 URL，行为与逐次 `-i` 类似；可通过 `-o` 传入统一输出名（视链接类型而定）。

## 功能说明

### 链接类型与行为

1. **`.m3u8` 直链**
   使用 ffmpeg 拉流并 remux 为 `.mp4`（`-c copy`）。
2. **URL 中含 `archives`**（归档站 / bl05 类页面）
   请求页面，解析多个 `div.dplayer` 的 `data-config`，得到多路 m3u8；按路依次下载，文件名一般为 **页面标题 + 序号**，并经 `safe_mp4_filename` 净化。
3. **其它播放页**（非 archives）
   解析 `var cms_player = {...}` 的 JSON，取 `url` 作为 m3u8，再走 ffmpeg。
4. **`.mp4` 等直链**
   使用 `requests` 分段下载（`file_download.download_from_url`），带 tqdm 进度条，**不经过 ffmpeg**。

### 页面编码

抓取 HTML 时依次尝试 **UTF-8 → UTF-8-sig → gb18030**，减轻标题乱码。

### 输出文件名

* 去除 Windows 非法字符，过长截断并可带 crc 后缀兜底。
* 对「UTF-8 被误当成 latin-1」类乱码标题做启发式纠正（日志中可能出现 `[F] 标题疑似 UTF-8/latin-1 乱码，已尝试纠正`）。

### 覆盖策略

* 若目标 `.mp4` **已存在**（`os.path.isfile`），**跳过**该次下载。
* 调用 ffmpeg 时带 **`-n`**：不在终端交互询问覆盖；若因路径编码等导致检测不一致，ffmpeg 侧也会拒绝覆盖而非静默覆盖。

### 本地 m3u8 文件

`-f` 指向 `.m3u8` / `.m3u` 时，当前代码分支为占位（`pass`），尚未实现。

## 目录说明

| 路径（相对程序目录） | 用途 |
| --- | --- |
| `bin/ffmpeg.exe` | Windows 打包/放置 ffmpeg 的常见位置 |
| `download/m3u8_files` | 内部与 `make_dir` 相关的子目录逻辑 |
| `download/mp4` | 未指定 `-p` 时的默认输出目录 |

下载地址：

[https://www.123912.com/s/ucY7Vv-njQAA?pwd=HwGK#](https://www.123912.com/s/ucY7Vv-njQAA?pwd=HwGK)

---

[![闺蜜圈APP](/support/guimiquan-ads2.jpg)](https://guimiquan.cn "闺蜜圈APP")

**博客：** [obaby 𝐢‍𝐧⃝ void](https://zhongxiaojie.cn/)

**地址：** <https://zhongxiaojie.cn/>

**文章：** [《m3u8 downloader v26.03.28》](https://zhongxiaojie.cn/2026/03/741/)

[ffmpeg](https://zhongxiaojie.cn/tag/ffmpeg/)[m3u8](https://zhongxiaojie.cn/tag/m3u8/)[视频下载](https://zhongxiaojie.cn/tag/%E8%A7%86%E9%A2%91%E4%B8%8B%E8%BD%BD/)

[Previous Post](https://zhongxiaojie.cn/2026/03/746/)
[Next Post](https://zhongxiaojie.cn/2026/03/714/)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=initials&r=pg&initials=ob)

#### obaby

独立 APP 开发者
偶尔写点东西
希望与过往一刀两断

#### You may also like

2026年1月21日 09:29

#### [彻底解决WordPress站点健康问题](https://zhongxiaojie.cn/2026/01/197/)

2026年1月27日 20:59

#### [浅谈WordPress静态化](https://zhongxiaojie.cn/2026/01/270/)

2026年1月16日 14:08

#### [PHP 8 探针 粉萌版](https://zhongxiaojie.cn/2026/01/79/)

### 16 comments

1. ![](https://gg.lang.bi/avatar/d338080125e831382007b2806ba60868b624b12af166e18b1eb8192908c66649?s=64&d=initials&r=pg&initials=Ha) **[Hary](https://www.hxy.cc/)**说道：

   [2026年3月29日 10:11 下午](https://zhongxiaojie.cn/2026/03/741/#comment-2003)

   ![Level 3](https://badgen.h4ck.org.cn/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 146.0.0.0") Microsoft Edge 146.0.0.0 ![Android 10](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 10") Android 10 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   emmm一楼嘛，看不懂干啥的，楼下解释一下

   [回复](#comment-2003)
2. ![](https://gg.lang.bi/avatar/317001b83ce285c98688055eec49904178a7cba58865c14add64d6a9512377d9?s=64&d=initials&r=pg&initials=%E7%9A%AE%E7%9A%AE)

   [2026年3月29日 10:53 下午](https://zhongxiaojie.cn/2026/03/741/#comment-2004)

   ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 2](https://badgen.h4ck.org.cn/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 131.0.6778.200](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 131.0.6778.200") Google Chrome 131.0.6778.200 ![Android 16](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 16") Android 16 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   二楼也不懂，好像是看小电影的。具体楼下解释下。

   [回复](#comment-2004)
3. ![](https://gg.lang.bi/avatar/275669417e1ae8fa2d8e968aeba2f9baccbcdcf010d29d1dd9fa90dff1929fb5?s=64&d=initials&r=pg&initials=%E7%93%A6%E5%8C%A0)

   [2026年3月30日 6:21 上午](https://zhongxiaojie.cn/2026/03/741/#comment-2005)

   ![Level 2](https://badgen.h4ck.org.cn/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![WebView 4.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/android-webkit.png "WebView 4.0") WebView 4.0 ![Android 16](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/android.png "Android 16") Android 16 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   手机端，代码块内容跑出去了

   [回复](#comment-2005)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=initials&r=pg&initials=ob)

      [2026年3月30日 9:08 上午](https://zhongxiaojie.cn/2026/03/741/#comment-2012)

      ![公主](https://badgen.h4ck.org.cn/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.h4ck.org.cn/badge/角色/女王/red?icon=matrix) ![Queen](https://badgen.h4ck.org.cn/badge/精神状态/恬静/pink?icon=codebeat)

      ![Google Chrome 142.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 142.0.0.0") Google Chrome 142.0.0.0 ![Mac OS X  10.15.7](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X  10.15.7") Mac OS X 10.15.7 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      修复了

      [回复](#comment-2012)
4. ![](https://gg.lang.bi/avatar/35ff2d2f9c0dab8109ae2d6cbc13bd453323f85a8b2016542102976d19447d2d?s=64&d=initials&r=pg&initials=%E8%8F%B2%E5%85%8B)

   [2026年3月30日 6:33 上午](https://zhongxiaojie.cn/2026/03/741/#comment-2006)

   ![Level 2](https://badgen.h4ck.org.cn/badge/亲密度/Level 2/cyan?icon=codebeat)

   ![Google Chrome 146.0.0.0](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 146.0.0.0") Google Chrome 146.0.0.0 ![Mac OS X  26.4](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X  26.4") Mac OS X 26.4 ![cn](https://zhongxiaojie.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   这不巧了吗，三楼的我也不懂，原来技术文章可以这样回复

   [回复](#comment-2006)
5. ![](https://gg.lang.bi/avatar/0b3b8cb95165c8e438337c47068ca52924eb8c720204352f7173082960b42c74?s=64&d=initials&r=pg&initials=%E8%8A%B1%E9%9D%9E)

   [2026年3月30日 6:52 上午](https://zhongxiaojie.cn/2026/03/741/#comment-2007)

   ![Level 4]...