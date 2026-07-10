---
title: 2026平航杯 手机取证题解析
url: https://mp.weixin.qq.com/s/FWkesuxTpUkDIXLhERfevw
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:54:28.744102
---

# 2026平航杯 手机取证题解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A8DiammjC4XCL7MCSh9EIwoeAO13kVtmmXN7Ez9g07P7yRJJtzDibyTice0k39icWNaacFSJNWKhVz2PbPK3LnxQN6belF7mT2nBwgFg9U85J2U/0?wx_fmt=jpeg)

# 2026平航杯 手机取证题解析

怪叔叔
怪叔叔

取证与溯源

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 🏆 2026平航杯手机取证 Writeup

---

💡 **报告元数据**

* **首席取证官**：`yagami`
* **任务目录**：`/mnt/d/文档/hermes-work/mobile-forensics/`
* **生成时间**：2026-07-08
* **生成模式**：完整型取证交付 Writeup

## 🛠️ 工具链与环境底座

### 1. 算力与架构

| 组件分类 | 部署详情 |
| --- | --- |
| **自动化编排** | Hermes Agent |
| **基座大模型** | Qwen3.6-27B-Uncensored-HauhauCS-Aggressive-Q6\_K\_P.gguf |
| **运行架构** | 本地 |

### 2. 任务信息

| 项目 | 详情 |
| --- | --- |
| **检材1** | 早起王手机 — Pixel 6, Android 14, Google/oriole (`/mnt/z/1-手机/早起王的手机/`) |
| **检材2** | 倩倩手机 — nova 12 Pro, HarmonyOS 6.0.0.380 (`/mnt/z/1-手机/倩倩的手机/`) |
| **检材3** | 倩倩手机逆向包 — RAR压缩包 (`/mnt/z/1-手机/倩倩手机逆向包.rar`) |
| **题目数量** | 17题 (Q1-Q17) |
| **完成状态** | 17/17 ✅ 全部完成并验证 |

## 📊 考题最终答案汇总看板

| 题号 | 核心考点 | 权威标准答案 | 状态 | 等级 | 核心证据链检索摘要 |
| --- | --- | --- | --- | --- | --- |
| Q1 | Android手机型号识别 | Pixel 6 | 🟢 已验证 | L1 | PhoneInfo JSON直接提取Model字段 |
| Q2 | 高德地图POI搜索记录取证 | 西湖 | 🟢 已验证 | L2 | PoiDetailUserBehavior.xml + pre\_set\_word\_local\_storage.xml双证据交叉 |
| Q3 | 微信FTS5加密数据库解密与加好友时间 | 2026-03-3015:13:08 | 🟢 已验证 | L2 | MMKV提取FTS密码→SQLCipher解密→FTS5MetaMessage系统消息时间戳 |
| Q4 | 微信朋友圈protobuf解码 | 麻薯小蛋糕 | 🟢 已验证 | L1 | SnsMicroMsg.db未加密，protobuf解码朋友圈内容 |
| Q5 | HarmonyOS备份元数据分析 | 6.0.0.380 | 🟢 已验证 | L1 | .info.json中BackupFileVersionInfo.versionName直接读取 |
| Q6 | SQLite WAL文件原始数据提取 | wxid\_uh5tfx2zi8yh22 | 🟢 已验证 | L1 | fts\_contact.db-wal原始WAL帧数据中搜索"舔狗"联系人记录 |
| Q7 | HarmonyOS备忘录AES-GCM解密 | 冰糖 | 🟢 已验证 | L2 | 备忘录cloud\_notes原文 + 截图交叉验证 |
| Q8 | 加密截图解密与视觉分析 | zero sievert | 🟢 已验证 | L1 | .tb文件xorEncrypt解密后截图视觉分析 |
| Q9 | HarmonyOS搜狐新闻数据库统计 | 33 | 🟢 已验证 | L1 | gen\_natural\_store.db主库sync\_data表精确COUNT查询 |
| Q10 | HarmonyOS逆向包module.json分析 | com.koishi.fpt | 🟢 已验证 | L1 | module.json中bundleName字段直接提取 |
| Q11 | ABC字节码字符串提取 | 6 | 🟢 已验证 | L1 | ABC字节码strings提取"密码长度至少为6位" |
| Q12 | ABC字节码加密后缀识别 | .tb | 🟢 已验证 | L1 | ABC字节码strings提取.tb后缀 |
| Q13 | ABC字节码文件类型分类统计 | 5 | 🟢 已验证 | L1 | ABC字节码中提取图片类型列表：jpg/jpeg/png/gif/webp共5种 |
| Q14 | SO模块NAPI方法数IDA反汇编验证 | 2 | 🟢 已验证 | L2 | IDA反汇编napi\_define\_properties count=2 + SO rodata交叉验证 |
| Q15 | SO rot13函数ROT+16发现与密码恢复 | 217cb94a01679e39 | 🟢 已验证 | L2 | IDA确认rot13=ROT+16 → vault\_prefs ROT-16逆运算恢复原始密码 |
| Q16 | xorEncrypt自定义算法解密JSON | 1472580369123 | 🟢 已验证 | L1 | xorEncrypt公式 `output[i]=data[i]^(key[i%k]+(i%k))` 解密notes JSON |
| Q17 | PNG文件末尾隐写数据提取 | flag{happy\_forensics\_2026!} | 🟢 已验证 | L1 | PNG IEND chunk后27字节隐藏flag数据 |

## ⚔️ 深度取证与解题全链路复盘

### 🧩 Q1 早起王的手机-1：手机型号

* **题目**：分析早起王的手机，手机型号为？【答案格式：Xiaomi13】
* **标准答案**：`Pixel 6`
* **状态等级**：🟢 已验证 / **L1**
* **解题主线**：早起王手机检材根目录下有 `PhoneInfo-1775206177238` JSON文件，直接读取Model字段即可。
* **💡 关键证据**：

+ PhoneInfo-1775206177238 JSON内容：`"Model":"Pixel 6"`, `"Device":"oriole"`, `"Brand":"google"`

* **🛠️ 核心命令**：

```
ounter(lineounter(linecat /mnt/z/1-手机/早起王的手机/PhoneInfo-1775206177238# Model: Pixel 6, Device: oriole, Brand: google
```

* **验证闭环**：从原始检材独立复现，JSON字段直接提取，无歧义。

---

### 🧩 Q2 早起王的手机-2：高德地图最可能去的景点

* **题目**：分析早起王的手机，早起王最近想旅行，结合高德地图搜索记录，他最可能去的景点是哪个？【答案格式：黄山】
* **标准答案**：`西湖`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：从root.tar中提取高德地图(`com.autonavi.minimap`)数据，查看shared\_prefs中的POI访问行为和预设搜索词。
* **💡 关键证据**：

+ **证据源1**：PoiDetailUserBehavior.xml 中最后访问的POI为 `"name":"杭州西湖风景名胜区"`
+ **证据源2**：pre\_set\_word\_local\_storage.xml 中预设搜索词 `"杭州西湖":1`

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(linemkdir -p /tmp/zqw-phone && cd /tmp/zqw-phonetar xf /mnt/z/1-手机/早起王的手机/root.tar --strip-components=3 data/data/com.autonavi.minimap/
cat shared_prefs/PoiDetailUserBehavior.xml# "name":"杭州西湖风景名胜区"
cat shared_prefs/pre_set_word_local_storage.xml# "杭州西湖":1
```

* **验证闭环**：双证据交叉验证 — POI访问记录 + 预设搜索词均指向"杭州西湖"，答案简化为"西湖"。

---

### 🧩 Q3 早起王的手机-3：加上倩倩微信的时间

* **题目**：分析早起王的手机，早起王在什么时间加上倩倩微信的？【答案格式：2025-08-1807:09:19】
* **标准答案**：`2026-03-3015:13:08`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

+ **阶段1 — FTS密码提取**：在微信MMKV配置文件中搜索FTS数据库加密密码
+ **阶段2 — SQLCipher解密**：用提取的密码解密FTS5IndexMicroMsg\_encrypt.db
+ **阶段3 — 好友验证消息定位**：在FTS5MetaMessage中查找最早的系统消息（好友验证通过）

* **💡 关键证据**：

+ **FTS密码来源**：`mmkv_private/ConfigStorage2` 中明文存储 `USERINFO_FTS_MASTER_DB_ENCRYPT_PWD_STRING → 20623a1`
+ **SQLCipher参数**：page\_size=4096, kdf\_iter=64000, hmac\_reserve=48, digest=sha1
+ **好友验证消息**：FTS5MetaMessage.docid=38: `aux_index=wxid_zuaa9igqlro22`, `talker=wxid_zuaa9igqlro22`, `timestamp=1774854788001`
+ **消息内容**：FTS5IndexMessage\_content docid=38: `"我通过了你的朋友验证请求，现在我们可以开始聊天了"`
+ **时间戳转换**：1774854788001 → 2026-03-30 15:13:08 (UTC+8)

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line# 阶段1: MMKV提取FTS密码grep -a "USERINFO_FTS_MASTER_DB_ENCRYPT_PWD_STRING" /tmp/zqw-wechat/data/data/com.tencent.mm/MicroMsg/bdf648ed55f29d2f2b30888e605a2a86/mmkv_private/ConfigStorage2# → USERINFO_FTS_MASTER_DB_ENCRYPT_PWD_STRING ... 20623a1
# 阶段2: SQLCipher解密FTS数据库DB="/tmp/zqw-wechat/data/data/com.tencent.mm/MicroMsg/bdf648ed55f29d2f2b30888e605a2a86/FTS5IndexMicroMsg_encrypt.db"sqlcipher "$DB" <<'EOF'PRAGMA key = '20623a1';PRAGMA cipher_page_size = 4096;PRAGMA kdf_iter = 64000;PRAGMA cipher_hmac_algorithm = HMAC_SHA1;PRAGMA cipher_kdf_algorithm = PBKDF2_HMAC_SHA1;.output /tmp/zqw-wechat/FTS5Index_plain.db.sql.dumpEOF# → 82张表，解密成功
# 阶段3: 查询好友验证消息grep "^INSERT INTO \"FTS5MetaMessage\" VALUES(38," /tmp/zqw-wechat/FTS5Index_plain.db.sql# → aux_index=wxid_zuaa9igqlro22, timestamp=1774854788001
grep "^INSERT INTO \"FTS5IndexMessage_content\" VALUES(38," /tmp/zqw-wechat/FTS5Index_plain.db.sql# → content = "我通过了你的朋友验证请求，现在我们可以开始聊天了"
# 时间戳转换python3 -c "from datetime import datetime,timezone,timedelta; ts=1774854788001; print(datetime.fromtimestamp(ts/1000,tz=timezone.utc).astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S'))"# → 2026-03-30 15:13:08
```

* **验证闭环**：FTS5MetaMessage中docid=38是该wxid最早的37条消息之一，内容为系统自动生成的好友验证通过消息。联系人索引建档时间(2026-04-01 15:23:33)晚于首次消息时间，确认为FTS异步索引延迟。
* **⚠️ 修正复盘**：最初误用联系人索引建档时间 2026-04-01 15:23:33 作为答案，后经交叉验证发现FTS5MetaMessage中最早消息时间为 2026-03-30 15:13:08，且内容为好友验证通过系统消息，修正为正确答案。

---

### 🧩 Q4 早起王的手机-4：倩倩2026年3月30号吃了什么

* **题目**：分析早起王的手机，倩倩在2026年3月30号吃了什么？【答案格式：西湖醋鱼】
* **标准答案**：`麻薯小蛋糕`
* **状态等级**：🟢 已验证 / **L1**
* **解题主线**：早起王手机中微信SnsMicroMsg.db未加密，直接查询倩倩(wxid\_zuaa9igqlro22)的朋友圈数据，protobuf解码后找到2026-03-30发布的内容。
* **💡 关键证据**：

+ SnsMicroMsg.db (protobuf解码): `createTime=1774857137` → 2026-03-30 15:52:17
+ 朋友圈内容：`"今天吃了麻薯小蛋糕 开心开心开心！"`

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineDB="/tmp/zqw-wechat/data/data/com.tencent.mm/MicroMsg/bdf648ed55f29d2f2b30888e605a2a86/SnsMicroMsg.db"sqlite3 "$DB" "SELECT snsId, userName, createTime, content FROM SnsInfo WHERE userName='wxid_zuaa9igqlro22' ORDER BY createTime DESC;"
python3 -c "from datetime import datetime; print(datetime.fromtimestamp(1774857137))"# 2026-03-30 15:52:17 — "今天吃了麻薯小蛋糕 开心开心开心！"
```

* **验证闭环**：从原始检材独立复现，SnsMicroMsg.db未加密直接查询，protobuf解码后内容明确。

---

### 🧩 Q5 倩倩的手机-1：系统版本

* **题目**：分析倩倩的手机，倩倩手机的系统版本是多少？【答案格式：5.2.3.123】
* **标准答案**：`6.0.0.380`
* **状态等级**：🟢 已验证 / **L1**
* **解题主线**：直接读取HarmonyOS备份元数据文件 `.info.json`，从中提取 `BackupFileVersionInfo.versionName`。
* **💡 关键证据**：

+ .info.json: `BackupFileVersionInfo.versionName = "6.0.0.380"`
+ versionCode = "60000380" 也对应 6.0.0.380

* **🛠️ 核心命令**：

```
ounter(lineounter(linepython3 -c "import json; info=json.load(open('/mnt/z/1-手机/倩倩的手机/备份/.info.json')); print(info['BackupFileVersionInfo']['versionName'])"# → 6.0.0.380
```

* **验证闭环**：从原始检材直接读取，无歧义。
* **⚠️ 修正复盘**：原答案 5.0.0.123 是推断值（无直接证据），实际应从 .info.json 直接读取为 6.0.0.380。

---

### 🧩 Q6 倩倩的手机-2："舔狗"的微信内部ID

* **题目**：分析倩倩的手机，"舔狗"的微信内部ID是多少？【...