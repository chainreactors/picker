---
title: 第四届黄河流域公安院校电子物证个人赛手机取证（火眼）
url: https://mp.weixin.qq.com/s/mtUiRuFe2IaCgxcia55-0Q
source: Doonsec's feed
date: 2026-08-07
fetch_date: 2026-08-08T03:20:32.533467
---

# 第四届黄河流域公安院校电子物证个人赛手机取证（火眼）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A8DiammjC4XCI43ibrAXdGyrVkeIgyfvGoVvqFRVmX3coOGNSXW4Jic5OJ2YLPtBEsGa1wNOiavwNpYCiarHtYVO5GBU0200D8jsxM1kcp10zq2k/0?wx_fmt=jpeg)

# 第四届黄河流域公安院校电子物证个人赛手机取证（火眼）

怪叔叔
怪叔叔

取证与溯源

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 🏆 2026第四届黄河流域公安院校电子物证个人赛 — 手机取证（火眼）

---

💡 **报告元数据**

* **首席取证官**：`yagami`
* **任务目录**：`/mnt/d/文档/hermes-work/2026黄河流域手机取证火眼/`
* **生成时间**：2026-08-07
* **生成模式**：完整型取证交付 Writeup

## 🛠️ 工具链与环境底座

### 1. 算力与架构

| 组件分类 | 部署详情 |
| --- | --- |
| **自动化编排** | Hermes Agent |
| **基座大模型** | Qwen3.6-27B-Q6\_K\_MTP.gguf (custom) |
| **运行架构** | 本地（WSL on Windows） |

### 2. 任务信息

| 字段 | 值 |
| --- | --- |
| **案件编号** | 20260805075342X |
| **案件名称** | 黄河流域手机 |
| **检材类型** | ADB backup tar（Mobile.tar） |
| **取证平台** | 火眼 GoldenEyes V4（GES CLI） |
| **检材挂载** | `/evidence_mounts/eid-1/` → `C:\hlnet\1-1785887696` |
| **GES URL** | http://127.0.0.1:8446（动态端口） |
| **题目数量** | 10题（Q1-Q10） |
| **完成度** | 10/10 全部已验证 |

## 📊 考题最终答案汇总看板

| 题号 | 核心考点 | 权威标准答案 | 状态 | 等级 | 核心证据链检索摘要 |
| --- | --- | --- | --- | --- | --- |
| Q1 | AI聊天应用搜索会话取证 | DeepSeek | 🟢 已验证 | L2 | DeepSeek Chat UUID后缀数据库chat\_session\_list表title字段匹配 + shared\_prefs host\_app\_id确认软件名 |
| Q2 | 邮箱收件箱注册邮件取证 | 2026-03-01 | 🟢 已验证 | L2 | 网易邮箱大师收件箱CSV搜索"欢迎注册拓鑫任务平台"邮件发送时间 + APK列表包名交叉验证 |
| Q3 | 日历Events表刷单投入统计（多选） | A, B, C, D | 🟢 已验证 | L2 | calendar.db Events表title/description金额提取，区分单次投入与累计总额 |
| Q4 | 日历Events表总投入计算 | 15万 | 🟢 已验证 | L2 | Events表完整投入明细累加 + 受害人自述"总共被骗了15万"交叉验证 |
| Q5 | 多APP账户信息交叉验证（多选） | A, B, D | 🟢 已验证 | L2 | "与你"APP账号信息 + Soul账号信息 + 网易邮箱路径确认 + 全数据grep排除法 |
| Q6 | Download目录压缩包证据提取 | 诈骗账户信息.txt | 🟢 已验证 | L2 | storage/emulated/0/Download/证据备份.zip → python3 zipfile解压查看文件列表 |
| Q7 | 百度地图搜索地点取证（多选） | A, B, D | 🟢 已验证 | L2 | /case/1/百度地图/搜索地点/data.csv 32条记录精确匹配选项 |
| Q8 | 照片EXIF GPS反地理编码 | 海口市 | 🟢 已验证 | L2 | data/storage/emulated/0/DCIM/Camera/IMG\_20260703\_141855.jpg EXIF GPS + nominatim反向地理编码 |
| Q9 | 米家智能家居设备型号提取 | qjiang.acpartner.ac02 | 🟢 已验证 | L2 | device\_tca\_config.db device\_config\_v3\_access model字段 + device\_action\_configs\_v3动作关联确认 |
| Q10 | JPEG文件strings隐写URL提取 | https://pay-demo.virtualpay.com/pay/orderNo=ORD260710594721 | 🟢 已验证 | L2 | com.uneed.yuni/files/重要.jpg strings命令提取HTTP URL |

## ⚔️ 深度取证与解题全链路复盘

### 🧩 Q1 受害人曾搜索过"兼职APP推荐"，使用的搜索软件是什么？

* **标准答案**：`DeepSeek`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

题目要求找出受害人搜索"兼职APP推荐"时使用的软件。初步在浏览器数据目录和快手数据库中搜索未果，后发现DeepSeek Chat应用的数据库文件名含UUID后缀（`deepseek_chat_b9accab9-e632-40ef-850f-fec135cd03f6.db`），主库`deepseek_chat.db`只有app\_user\_info表，实际会话数据在UUID后缀的数据库中。遍历所有`.db`文件查找`chat_session_list`表，在该表中精确匹配到"兼职APP推荐"会话记录。通过shared\_prefs中的`header_custom_240734.xml`确认host\_app\_id为"DeepSeek[675113]"。

* **💡 关键证据**：

+ **FINDING-Q1-001**：`deepseek_chat_b9accab9-e632-40ef-850f-fec135cd03f6.db`的`chat_session_list`表中存在记录：`308be25c-503d-40ad-8733-150390c8e561|兼职APP推荐|SYSTEM|10|1783592253|...`
+ **交叉验证**：`header_custom_240734.xml`中`host_app_id="DeepSeek[675113]"`

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line# 复制DeepSeek UUID数据库ges copy /evidence_mounts/eid-1/Mobile.tar/Mobile/data/com.deepseek.chat/databases/deepseek_chat_b9accab9-e632-40ef-850f-fec135cd03f6.db --dest .
# 查询chat_session_list表sqlite3 deepseek_chat_b9accab9-e632-40ef-850f-fec135cd03f6.db "SELECT * FROM chat_session_list WHERE title LIKE '%兼职%';"# 输出: 308be25c-503d-40ad-8733-150390c8e561|兼职APP推荐|SYSTEM|10|1783592253|...
# 交叉验证软件名ges read /evidence_mounts/eid-1/Mobile.tar/Mobile/data/com.deepseek.chat/shared_prefs/header_custom_240734.xml# 输出: host_app_id="DeepSeek[675113]"
```

* **📋 控制台回显**：

```
ounter(line308be25c-503d-40ad-8733-150390c8e561|兼职APP推荐|SYSTEM|10|1783592253|1783592123.936|1783592266.459|14|5|0|default
```

* **验证闭环**：chat\_session\_list表title字段精确匹配 + shared\_prefs host\_app\_id确认软件名称，双源交叉验证。
* **⚠️ 修正复盘**：DeepSeek Chat数据库文件名含UUID后缀是核心陷阱——主库`deepseek_chat.db`只有app\_user\_info表，实际会话数据在UUID后缀的数据库中。如果只查主库会漏掉所有聊天会话。

---

### 🧩 Q2 受害人是哪一天注册的"拓薪任务"APP？

* **标准答案**：`2026-03-01`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

题目问"拓薪任务"APP的注册日期。首先在APK列表中确认包名为`com.tuoxin.task`，名称为"拓鑫任务"（注意是"拓鑫"而非"拓薪"）。然后在网易邮箱大师的收件箱中搜索"注册"关键字，定位到第29行邮件：主题"欢迎注册拓鑫任务平台"，发件人`noreply@tuoxinapp.com`，发送时间`2026-03-01 09:28:14`。

* **💡 关键证据**：

+ **FINDING-Q2-001**：收件箱CSV第29行记录：主题"欢迎注册拓鑫任务平台"，发件人`拓鑫任务平台<noreply@tuoxinapp.com>`，发送时间`2026-03-01 09:28:14`
+ **交叉验证**：APK列表中包名`com.tuoxin.task`，名称"拓鑫任务"，版本号3.2.1

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line# 搜索收件箱中的注册邮件ges read /case/1/网易邮箱大师/zdashuai0709@163.com(zdashuai0709@163.com)/收件箱/data.csv --limit 82 | grep "注册"# 输出: 第29行 主题"欢迎注册拓鑫任务平台",发件人noreply@tuoxinapp.com,发送时间2026-03-01 09:28:14
# 交叉验证APK列表ges read /case/1/App分析/APK列表/data.csv --limit 200 | grep "tuoxin"# 输出: 68,拓鑫任务,com.tuoxin.task,3.2.1,7.92 MB,
```

* **验证闭环**：注册邮件发送时间 + APK列表包名确认，双源交叉验证。

---

### 🧩 Q3 根据日历中记录的内容，受害人分别在刷单APP上投入了以下哪些金额（多选题）？

* **标准答案**：`A, B, C, D`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

从`calendar.db`的Events表中搜索含"投"、"赚"、"万"、"元"、"单"关键词的记录，逐条提取投入金额。关键记录包括：

* "第一单做完，赚了30" — 做了第一单**100元**的刷单任务（选项A ✓）
* "今天投了500，赚了150" — 做了**500**的单（选项B ✓）
* "投了3000，返利900" — 投了**3000**的高级单（选项C ✓）
* "投了5万进去，有点慌" — 转了**5万**做连单（选项D ✓）
* "交了2万保证金...总共10万了" — **10万是累计总额而非单次投入**（选项E ✗）

* **💡 关键证据**：

+ **FINDING-Q3-001**：calendar.db Events表7条刷单相关记录，明确区分单次投入金额与累计总额

* **🛠️ 核心命令**：

```
ounter(linesqlite3 calendar.db "SELECT title, description FROM Events WHERE title LIKE '%投%' OR title LIKE '%赚%' OR title LIKE '%万%' OR title LIKE '%单%';"
```

* **验证闭环**：Events表title和description字段直接提取金额，选项E(10万)是累计总额而非单次投入，排除。

---

### 🧩 Q4 截止2026-03-12，受害人共投入了多少资金？

* **标准答案**：`15万`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

从Events表完整记录中提取所有投入明细并累加：

* 100元(第一单) + 500元(第二单) + 3000元(高级单) + 50000元(连单) + 30000元(修复金) + 20000元(保证金) + 50000元(最后一笔) = **153600元**

日历中受害人自述"去派出所报案...总共被骗了**15万**"，与计算结果153600元取整一致。

* **💡 关键证据**：

+ **FINDING-Q4-001** + **FINDING-Q4-002**：Events表完整投入明细累加 = 153600元，受害人自述"总共被骗了15万"

* **🛠️ 核心命令**：

```
ounter(lineounter(linesqlite3 calendar.db "SELECT title, description FROM Events ORDER BY dtstart;"# 关键记录: "去派出所报案|越想越不对，一早去派出所报案，总共被骗了15万"
```

* **验证闭环**：Events表逐条累加(153600元) + 受害人自述"总共被骗了15万"交叉验证。

---

### 🧩 Q5 以下哪些账号或昵称是该受害人的？（多选题）

* **标准答案**：`A, B, D`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

通过多APP账户信息交叉验证：

* A. 张大帅 — "与你"APP账号信息表确认昵称"张大帅"(ID:1195155160385462272) ✓
* B. 哈哈小飞侠 — Soul APP账号信息表确认昵称"哈哈小飞侠"(ID:208235612) ✓
* C. 海阔天空 — 全数据grep排除，未在任何APP中找到 ✗
* D. zdashuai0709@163.com — 网易邮箱大师账户路径确认 ✓
* E. Zhangmouren — 全数据grep排除，未在任何APP中找到 ✗

* **💡 关键证据**：

+ **FINDING-Q5-001**：多APP账户信息交叉验证 + 全数据grep排除法

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineges read /case/1/与你/张大帅(1195155160385462272)/账号信息/data.csv# 输出: 1195155160385462272,1195155160385462272,张大帅,,,,
ges read /case/1/Soul/哈哈小飞侠（208235612）/账号信息/data.csv# 输出: 208235612,TndVS3M0Q0xrRXZnQkp2UDhiV2VUdz09,哈哈小飞侠,,,,
ges grep "海阔天空" --path /case/1/ → 无匹配ges grep "Zhangmouren" --path /case/1/ → 无匹配
```

* **验证闭环**：3个正向确认（与你APP、Soul、网易邮箱）+ 2个反向排除（全数据grep），五选项全覆盖。

---

### 🧩 Q6 压缩包中的文件名称为？

* **标准答案**：`诈骗账户信息.txt`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

在`storage/emulated/0/Download/`目录中发现`证据备份.zip`(380 bytes)，复制到本地后用Python zipfile解压，压缩包内含唯一文件`诈骗账户信息.txt`。

* **💡 关键证据**：

+ **FINDING-Q6-001**：`storage/emulated/0/Download/证据备份.zip`解压后含1个文件"诈骗账户信息.txt"

* **🛠️ 核心命令**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineges ls /evidence_mounts/eid-1/Mobile.tar/Mobile/storage/emulated/0/Download/# 输出: 6c8bc91fe99145c6b508f2b824611b12.png, 证据备份.zip
ges copy .../证据备份.zip --dest artifacts/python3 -c "import zipfile; z=zipfile.ZipFile('证据备份.zip'); print('\n'.join(z.namelist()))"# 输出: 诈骗账户信息.txt
```

* **验证闭环**：ges ls定位zip文件 + python3 zipfile解压查看文件列表。

---

### 🧩 Q7 受害人搜索过以下哪些地方？（多选题）

* **标准答案**：`A, B, D`
* **状态等级**：🟢 已验证 / **L2**
* **解题主线**：

从火眼解析的百度地图搜索地点CSV中读取32条记录，与选项逐一比对：

* A. 新街口 (2026-07-05) ✓
* B. 夫子庙 (2026-0...