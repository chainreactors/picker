---
title: 2026 年第六届 FIC 全国网络空间取证大赛初赛解题思路|服务器与手机部分|Hermes自动化分析
url: https://mp.weixin.qq.com/s/daVvCIwtEq9jiMTJf_6dWA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:57:16.291451
---

# 2026 年第六届 FIC 全国网络空间取证大赛初赛解题思路|服务器与手机部分|Hermes自动化分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RPq1g3ib528ial7iaMcribFTMtBMvA7icib8icPbU1scamnA8wxPYbN54x8wFCtA9IeAx7y0vz1icTiaQ4AWZT1XrzKwUqyWzae9R0xxwW85r925HyNI/0?wx_fmt=jpeg)

# 2026 年第六届 FIC 全国网络空间取证大赛初赛解题思路|服务器与手机部分|Hermes自动化分析

原创

0xSec笔记本
0xSec笔记本

0xSec笔记本

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 📢 免责声明

本文所述技术仅用于合法授权的安全研究、教学演示及防御机制开发。作者及发布平台不承担因读者误用、滥用本内容所导致的任何法律责任。请严格遵守《中华人民共和国网络安全法》及相关法律法规。

> 本文使用 Hermes 自动化取证框架对赛题进行分析，完整还原从 E01 镜像到交易数据提取的全流程。
>
> 感觉现在取证 AI Agent 单论分析优势实在是太强了！！！

# 检材3（服务器）& 检材2（手机）思路|答案未验证，仅供参考

---

## 检材3 - 服务器取证

### 题目1：该服务器主机操作系统版本为

**解题思路：** 挂载 EWF 镜像后，直接读取 `/etc/os-release` 文件，从 `PRETTY_NAME` 字段获取完整版本信息。

**答案：**`Debian GNU/Linux 13 (trixie)`

---

### 题目2：该服务器根分区硬盘的uuid号为

**解题思路：** 读取 `/etc/fstab`，找到挂载点为 `/` 的条目，提取其 `UUID=` 字段值。

**答案：**`3231e52f-5e15-44c4-b224-e29cb4201c0e`

---

### 题目3：服务器中最新的docker镜像的创建时间为

**解题思路：** 从 Docker 数据目录中查找容器配置文件（`hostconfig.json` 或 `config.v2.json`），提取其中的 `Created` 字段时间戳。

**答案：**`2026-04-16T10:09:05.106037938Z`

---

### 题目4：该服务器根观光路径为

**解题思路：** 读取 Nginx 配置文件 `/etc/nginx/sites-available/default`，找到 `root` 指令所指向的路径。

**答案：**`/var/www/html/maccms10`

---

### 题目5：网站后台管理入口对应的文件名为

**解题思路：** 查看 Nginx 配置中的 `index` 指令，结合 rewrite 规则，确认实际入口文件。后台控制器位于 `application/admin/controller/Index.php`，对应入口为 `Index.php`。

**答案：**`Index.php`

---

### 题目6：网站设置的icp备案号为

**解题思路：** 读取站点主配置文件 `/var/www/html/maccms10/application/extra/maccms.php`，提取 `site_icp` 字段。

**答案：**`icp1919810`

---

### 题目7：网站主域名

**解题思路：** 同上，从 `maccms.php` 中提取 `site_url` 字段。

**答案：**`www.2026fic.forensix`

---

### 题目8：分类3的英文标识

**解题思路：** 读取运行时缓存文件（`/var/www/html/maccms10/runtime/cache/` 目录下的 PHP 缓存），搜索 `分类3` 关键字，找到对应的 `type_en` 字段。

**答案：**`fenlei3`

---

### 题目9：站点设置页面模板路径

**解题思路：** 查看后台 `System.php` 控制器，找到 `fetch('admin@system/config')` 调用，对应模板文件实际路径为 `application/admin/view/system/config.html`。

**答案：**`/var/www/html/maccms10/application/admin/view/system/config.html`

---

### 题目10：伪静态规则配置文件的 SM3 哈希值

**解题思路：** 对 `application/route.php` 执行 `openssl dgst -sm3` 命令，直接计算 SM3 摘要。

**答案：**`959a39b5ed4304ef1a60ec3db463f07b438c14c4c1b748cceae80309262d6dea`

---

### 题目11：数据库服务器 IP 地址

**解题思路：** 先从 `application/database.php` 中获取数据库主机名 `mytidb`，再读取 `/etc/hosts` 文件，找到 `mytidb` 对应的 IP 映射。

**答案：**`10.0.3.100`

---

### 题目12：使用的容器技术

**解题思路：** 检查 `/etc/docker/daemon.json` 文件是否存在且内容合法，确认系统安装并配置了 Docker，`data-root` 指向 `/data`。

**答案：**`Docker`

---

### 题目13：4000 端口备份数据库版本

**解题思路：** 在可读的镜像文件范围内，遍历日志、配置、服务文件等，搜索 TiDB 相关版本字符串及 4000 端口信息，未能从当前可读证据中定位到有效版本号。

**答案：** 未能从当前可读证据中确定

---

### 题目14：注册行为最多的日期

**解题思路：** 遍历所有 Nginx 访问日志（含 `.gz` 压缩文件），用正则匹配包含 `register`、`/user/reg`、`signup` 等关键词的请求路径，按日期统计请求次数，取最高频日期。

**答案：**`15/Apr/2026`

---

### 题目15：后台最后登录的 IP 地址

**解题思路：** 遍历所有 Nginx 访问日志，筛选路径中含 `/user.php/admin/` 的请求，按时间排序后取最后出现的 IP 地址。

**答案：**`192.168.226.1`

---

### 题目16：根分区文件系统类型

**解题思路：** 从 `/etc/fstab` 中，根分区挂载条目的文件系统类型字段即为答案。

**答案：**`Btrfs`

---

### 题目17：已安装的数据库服务软件

**解题思路：** 读取 `/var/lib/dpkg/status`，依次搜索 `mariadb-server`、`postgresql-18`、`redis-server`、`sqlite3` 等包名，确认状态为 `install ok installed`。

**答案：**`MariaDB、PostgreSQL、Redis、SQLite`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528j2CMNZdXkpnickCiaawibRfsBfLMMKCwjXg1eRmb3HLMFWgUlf0wyGvrXpymA0PYo4YmItbDUJ1KkqaF1aZebBiaicYjwA6QiciaUYcQ/640?wx_fmt=png&from=appmsg)

## 检材2 - 手机取证

### 题目1：手机型号

**解题思路：** 读取 `ThunderForensic.json` 取证报告，提取 `Device.Model` 字段。

**证据：**/home/kali/Desktop/检材2-手机/ThunderForensic.json

**答案：**`Redmi Note 7 Pro`

---

### 题目2：计划前往迪拜的日期

**解题思路：**  /home/kali/Desktop/检材2-手机/data/user/0/com.miui.notes/databases/todo.db

**命中内容：** 2026.06.06 乘坐飞机去 dubai

**答案：** 2026.06.06

---

### 题目3：与网站搭建人员沟通所用 APP 的安装日期

**解题思路：** 从 `/data/system/packages.xml` 中找到包名 `com.talk.uuuim`，提取其 `it`（install time）字段的十六进制时间戳 `19d8b6fd571`，转换为 Unix 毫秒时间戳后换算为 UTC 时间。

**答案：**`2026-04-14 10:00:55.409 UTC`（北京时间 `2026-04-14 18:00:55.409`）

---

### 题目4：沟通所用 APP 的聊天数据库路径

**解题思路：** 定位包名 `com.talk.uuuim` 的数据目录，在 `databases/` 子目录下找到以哈希命名的 SQLite 数据库文件。

**答案：**`/data/user/0/com.talk.uuuim/databases/9628874a3c6b403593766496fa985893.db`

---

### 题目5：囤积数据的数据库解密密码

**解题思路：** 定位 `com.livevideo.hotclub` 的本地数据库 `hotclub_data.db`，尝试直接打开，发现无需密码即可读取表结构与数据，不存在 SQLCipher 加密。

**答案：** 未检出独立数据库解密密码

---

### 题目6：云服务器商家收款备用钱包地址

**解题思路：** 分析 `HotClub_v2.1.6.apk`，提取 `assets/config.dat`，根据代码中的解密逻辑（AES/ECB/PKCS5Padding，密钥 `hotclub_2026_sec`）解密后，从 JSON 结果中提取 `wallet` 字段。

**答案：**`TXqH7sVn8bR4kL2mN9pW6xJ3cY5dF1gA`

---

### 题目7：给网站架构人员第一次路由的交易哈希前6位

**解题思路：** 在聊天数据库、日志文件、相关文本中搜索交易哈希/txid 等关键词，未发现可直接确认的首笔交易哈希记录。

**答案：** 未检出

---

### 题目8：李安弘主动向 AI 提问次数

**解题思路：** 打开 `com.pocketpalai/pocketpalai.db`，查询 `messages` 表，筛选 `author` 字段为用户 ID（`y9d7f8pgn`）的记录并计数。

**答案：**`5次`

---

### 题目9：AI 软件调用的本地模型及版本

**解题思路：** 在 `pocketpalai.db` 中查询 `local_pals` 表的 `default_model` 字段，提取模型名称与文件名。

**答案：**`SmolVLM-500M-Instruct (Q8_0)`（完整标识：`ggml-org/SmolVLM-500M-Instruct-GGUF/SmolVLM-500M-Instruct-Q8_0.gguf`）

---

### 题目10：无人机飞行所在县

**解题思路：** 遍历 `dji.go.v5` 数据目录下的数据库与缓存文件，尝试提取飞行坐标记录并反查行政区划，未能抽取到确定落点的县级数据。

**答案：** 未检出县级地点

---

### 题目11：最近安装的视频类 APP 声明的敏感权限

**解题思路：** 对最近安装的视频 APP（`HotClub_v2.1.6.apk`，包名 `com.livevideo.hotclub`）进行 APK 解包，解析 `AndroidManifest.xml`，提取所有涉及用户隐私的 `uses-permission` 条目。

**答案：**

* • `READ_CONTACTS`
* • `READ_SMS`
* • `READ_CALL_LOG`
* • `READ_PHONE_STATE`
* • `ACCESS_FINE_LOCATION`
* • `ACCESS_COARSE_LOCATION`
* • `CAMERA`
* • `READ_EXTERNAL_STORAGE`
* • `WRITE_EXTERNAL_STORAGE`

---

### 题目12：网络不可用时加载的本地离线页面路径

**解题思路：** 逆向分析 HotClub APK 的 `MainActivity`，找到 `WebView.loadUrl()` 调用，提取网络不可用时的回退 URL。

**答案：**`file:///android_asset/www/index.html`

---

### 题目13：上传地址编码方式及完整 URL

**解题思路：** 在 HotClub APK 的 `DataUploader` 类中找到 `Base64.decode` 调用，提取编码字符串 `aHR0cHM6Ly9hcGkuc3AtbGl2ZTg4LmNvbS9jb2xsZWN0L3VzZXJkYXRh`，Base64 解码得到完整 URL。

**答案：** 编码方式：`Base64`；完整 URL：`https://api.sp-live88.com/collect/userdata`

---

### 题目14：存储用户信息的表名

**解题思路：** 直接打开 `hotclub_data.db`，查看建表语句，找到包含 `device_id`、`imei`、`phone_number`、`contacts_data` 等隐私字段的表。

**答案：**`user_collection`

---

### 题目15：config.dat 解密后的 USDT 钱包地址

**解题思路：** 从 APK 代码中定位解密逻辑：算法为 AES/ECB/PKCS5Padding，密钥种子为 `hotclub_2026_sec`，对 `assets/config.dat` 解密后解析 JSON，提取 `wallet` 字段。

**答案：**`TXqH7sVn8bR4kL2mN9pW6xJ3cY5dF1gA`

---

### 题目16：APP JS 层暴露的获取通讯录方法

**解题思路：** 分析 APK 中的 `NativeBridge` 类，提取通过 `addJavascriptInterface` 暴露给 WebView JS 层的方法签名，找到与通讯录相关的方法。

**答案：**`getContactsList()`

---

### 题目17：主上传服务器不可用时的备用服务器域名和端口

**解题思路：** Java 层代码中确认备用地址来自 native 方法 `DataUploader.getBackupEndpoint()`，实际逻辑位于 `lib/arm64-v8a/libsecurity.so`。需对该 SO 文件进行 JNI 逆向分析提取字符串，当前步骤未完成。主上传域名已确认为 `api.sp-live88.com`。

**答案：** 未完全提取，需进一步逆向 `libsecurity.so`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RPq1g3ib528hSL8bAuqZt40o2mCTe4EEj57iaCWb835hAObwgVCvWRZT24mDfXSACyVBRcZ9q5WaKgaC2pnEfVfBWssfBehRfocyULR9Fe2rA/640?wx_fmt=png&from=appmsg)

PS：里面的题目与答题格式可能存在偏差，欢迎指正！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1ADJCFZ0CSJbicoSblA0gAvoYITOib8ZQQ2h18ibU2NmibdWJMyU1Vmqxh0KTnw0tWymLTVSoibpTlUheiaaXcOzXNibg/0?wx_fmt=png)

0xSec笔记本

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1ADJCFZ0CSJbicoSblA0gAvoYITOib8ZQQ2h18ibU2NmibdWJMyU1Vmqxh0KTnw0tWymLTVSoibpTlUheiaaXcOzXNibg/0?wx_fmt=png)

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