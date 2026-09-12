---
title: Black Hat USA 2026：LLM勒索恢复验证
url: https://mp.weixin.qq.com/s/6aZFiQamVYcHMsrp86PrSw
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:46:02.280631
---

# Black Hat USA 2026：LLM勒索恢复验证

# Black Hat USA 2026：LLM勒索恢复验证

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 用 LLM 把勒索恢复做成可验证工程

勒索事件进入恢复阶段后，最危险的误判之一，是把“找到密码学缺陷”当成“数据已经能安全恢复”。PoC 在一个文件上跑通，只能证明方向可能正确；生产恢复还要回答更多问题：同一存储是否被加密多次，间歇加密的 block layout 是否一致，如何判断候选 key，解密器中断后能否续跑，怎样确保不会把原本的明文再次 XOR 成垃圾。

Black Hat USA 2026 公开课件《Cracking the Chains》复盘了一起针对 Linux/Oracle 数据库环境的 Gunra 勒索事件。研究团队从二进制逆向入手，发现攻击者的 ChaCha20 key/nonce 生成代码错误地在循环内使用 `srand(time(0))`，使 32 字节 key 和 12 字节 nonce 都退化成重复字节，实际 key 搜索空间只剩 256。团队借助 LLM 解释反编译代码、重建算法、生成初版工具并辅助从 Python 移植到 C，最终把 100GB 的处理时间从约 16 小时降到 147 秒，并在事件发生后 81 小时恢复主要服务。

这不是“LLM 破解 RSA-4096”的故事。RSA 封装仍然没有被数学攻破；失效的是封装前的密钥生成。LLM 也不是独立做出恢复决策的主体，它参与了逆向解释、代码草拟和工程迭代，关键结论仍由样本、已知明文、文件结构和恢复后的可挂载性验证。

本文依据公开课件整理，不以现场参会视角叙述。示例仅用于已授权事件响应和离线副本，不应直接对唯一一份受损介质执行写操作。

## 1、恢复工作先从证据冻结开始

课件把事件处置压缩为四个环节：攻击分析、发现密码学缺陷、开发工具、恢复。这个顺序不能倒过来。没有先确认样本版本、参数和文件布局，就直接拿通用 decryptor 批量写盘，可能造成第二次不可逆破坏。

![从分析到恢复的闭环](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852MNGsWtzMBSRqzIRZ5BzL0F637OmknsKLmTQvgh9jzma09ud86RdS2jpicdpZSh6iarlBntWUIduldeT9PquNNpzCo2ReMVlNSg/640?from=appmsg)

*图 1：找到缺陷只是中点，后面还有工具工程化与恢复验证*

第一份操作对象应当是快照或只读镜像。为样本、keystore、脚本、加密卷和日志建立 manifest，并记录获取时间、源设备、时区与 hash：

bash

```
# 在取证工作站执行；源块设备应通过写保护或只读映射暴露 CASE_DIR="case-2025-0714"mkdir -p "${CASE_DIR}"/{evidence,work,logs} cd"${CASE_DIR}"sha256sum \   evidence/enc \   evidence/.keystore \   evidence/R3ADM3.txt \   evidence/volume01.img \   > case-2025-0714/logs/SHA256SUMS  lsblk -o NAME,RO,SIZE,MODEL,SERIAL,MOUNTPOINTS blockdev --getro /dev/mapper/volume01-ro  # 工作副本再次校验，不修改 evidence 原件cp --reflink=always evidence/volume01.img work/volume01-test.img sha256sum evidence/volume01.img work/volume01-test.img \   > logs/IMAGE_COPY_SHA256.txt
```

`cp --reflink` 是否可用取决于文件系统；不可用时应创建新的镜像副本或快照。任何 decryptor 都只允许写 `work/`，并在命令行显式传入独立输出路径。

## 2、先还原样本“做了什么”，不要只看勒索信

课件样本 `enc` 支持 `--limit`、`--ratio`、`--device` 和扩展名选择，能够面向普通文件或 raw block device。它跳过自己的 `R3ADM3.txt` 勒索信和已经带 `.ENCRT` 后缀的文件，避免同一遍历过程重复加密。

![加密器参数与行为](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP853Ijll7lGYIRQedZ867QEXIaQJGTUvBdDVj0VuuwjwXCG7Gc0swNicukLOoR6OylXdK5iazkYVRwyYMowVQWUgUuFrGwGRkxsYoU/640?from=appmsg)

*图 2：参数决定目标类型、加密上限与间歇加密比例，恢复器必须逐项对齐*

事件目录 `/root/crypt` 中还包含公钥、keystore、执行脚本和进度文件。值得注意的是，脚本里计划使用的参数与实际运行二进制不一致：二进制拒绝了部分选项，说明攻击者最后部署了另一个 build。恢复分析必须以**真实执行的 hash 和遥测**为准，不能以落地脚本推断全部行为。

可以把逆向结论先结构化，要求每个字段附证据来源：

yaml

```
sample_profile:sha256:REPLACE_WITH_ACTUAL_HASHbuild_id:unknownobserved_execution:host:db-node-07timestamp_utc:2025-07-13T15:49:00Zargv_source:auditdcrypto:stream_cipher:chacha20key_bytes:32nonce_bytes:12initial_counter_per_encrypted_chunk:1layout:encrypted_chunk_bytes:1048576plaintext_chunks_skipped:3byte_limit:unknownevidence:-decompiler_function:sub_REPLACE-entropy_map:logs/volume01.entropy.json-suffix_depth:2
```

`unknown` 比猜一个默认值更安全。恢复器只有在关键参数被样本、命令行日志或数据分布确认后，才允许从 dry-run 进入写输出阶段。

## 3、RSA没有失效，随机数生成把密钥空间压成了256

样本原本采用常见的 hybrid encryption：随机生成 32 字节 ChaCha20 key、12 字节 nonce，再把 key material、ratio 和 limit 一起用 RSA-4096 公钥封装进 512 字节 `.keystore`。没有攻击者私钥时，直接解 RSA 在计算上不可行。

![keystore中的密钥材料](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP852z37NCib9GiaKCicAcC8IoP3olSlv2BWTH9HvjYdic0MjoAnzictcyu28tPrvGLYDYJibauozVSib2eiasxOGCzqtulKjePs13SPVBuEQ/640?from=appmsg)

*图 3：RSA 保护的是 52 字节参数块；参数块生成前已经出现致命弱点*

反编译代码显示生成循环反复调用 `srand(time(0))`。循环在同一秒内完成，每次播种相同，随后取得的第一次 `rand()` 结果也相同，因此 key 和 nonce 的每个位置得到同一个 byte。

![循环内重复播种](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852wL3JJacerRan3NiaOWGPT0I3SSuibuHlChf72ibuTs4vNS3PamTYiaQabDhoTpx4I3Te61NDniaNLNE78zmGfnIaJYrDGMCzib6tR8/640?from=appmsg)

*图 4：问题不是单纯“时间种子可预测”，而是每个字节前重新播种，使每次都取同一序列的第一个值*

下面的最小模型只用于说明熵坍缩，不复刻特定 libc 的 `rand()`：

python

```
defflawed_material(first_prng_byte: int) -> tuple[bytes, bytes]:     ifnot0 <= first_prng_byte <= 255:         raise ValueError("candidate must be one byte")     key = bytes([first_prng_byte]) * 32     nonce = bytes([first_prng_byte]) * 12return key, nonce  candidates = [flawed_material(b) for b inrange(256)] assertlen({key for key, _ in candidates}) == 256
```

![256位密钥退化为8位](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853XhutkB6bFVd9DIVW6ncicqdAgme9UmZibUM41Hgpaydn31FQeAs3N1QULS0WrK9rRoD09rV6KGMG1fIsVic8Wl4hicTyAg0r3Zl0/640?from=appmsg)

*图 5：课件验证 key 的 32 个字节相同，实际只需枚举 256 个候选 byte*

若走时间戳路线，还必须使用与目标相同的 C runtime 和 `rand()` 实现；glibc、musl、不同平台的输出不应假定一致。重复字节路线则直接枚举最终 byte，绕开了文件 mtime 被修改和时间窗口过宽的问题。

## 4、间歇加密的布局比候选Key更容易毁掉数据

课件中的 `ratio=3` 表示加密 1MB，再跳过 3MB 明文，如此循环。熵图上会出现高熵与正常数据交替的条带。

![间歇加密熵图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP851lfIqdqOhib5dNgm1kRfIdV1Iq71TiconDzDyxGry8ysibrwJibLaKxM74Bu0zP8yibjib8vsG9ChUNtmo2oCqTB8hfPmUsvYyx0QBM/640?from=appmsg)

*图 6：高熵块显示被加密区间，低熵和结构化区域保留原始明文*

恢复器不能把 ChaCha20 keystream 从文件头连续跑到文件尾。材料指出，每个被加密的 1MB block 都以 counter 1 重新开始；中间 3MB 必须原样复制。对明文区错误执行 XOR，会把可恢复数据主动破坏。

![间歇加密逆向布局](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP850AaghvNmOunia4CVFtleq9nib0ucKC8nrVj8OBAaaSPdiaV4HE0C9N5N7DpCcfmiaThTJxtxAHibiaR0xzYXCAOhdKoPibZicqYkHvxWE/640?from=appmsg)

*图 7：恢复循环是 1MB decrypt、3MB copy，并受原始 limit 限制*

将布局与 cipher 实现分离，便于测试：

python

```
from collections.abc importCallable, Iterator  MiB = 1024 * 1024defregions(file_size: int, ratio: int, limit: int | None) -> Iterator[tuple[int, int, bool]]:     cursor = 0     encrypted_total = 0while cursor < file_size:         enc_len = min(MiB, file_size - cursor)         if limit isnotNone:             enc_len = min(enc_len, max(0, limit - encrypted_total))         if enc_len == 0:             yield cursor, file_size - cursor, Falsereturnyield cursor, enc_len, True         cursor += enc_len         encrypted_total += enc_len          skip_len = min(ratio * MiB, file_size - cursor)         if skip_len:             yield cursor, skip_len, False             cursor += skip_len  defrecover_stream(src, dst, plan, decrypt_chunk: Callable[[bytes], bytes]):     for offset, length, encrypted in regions(plan.size, plan.ratio, plan.limit):         src.seek(offset)         data = src.read(length)         iflen(data) != length:             raise IOError(f"short read at {offset}")         dst.seek(offset)         dst.write(decrypt_chunk(data) if encrypted else data)
```

这里故意不实现 ChaCha20，避免把未经核对的 nonce/counter 细节和布局逻辑耦合。实际 `decrypt_chunk` 应调用经过测试的密码库，并为每个 encrypted region 明确重置 counter。

## 5、LLM适合压缩工程时间，不适合签署恢复结论

课件把 LLM 的参与分成四类：辅助理解 Hex-Rays 输出、还原 keystream、生成和移植工具、协助验证。这个边界很务实。模型擅长解释控制流、补齐样板代码、对照 Python/C 逻辑，却不能从一段看似合理的反编译代码保证语义正确。

![LLM辅助工程流程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850sria4wbooGUH693qS8X2Jqx9h6qVI8B6YwMf2hibfpMX0av1qItxELHibiaPB7INmRSicliamicuB3cH6B11WYVVsdlzkNibKTcBytEY/640?from=appmsg)

*图 8：AI 位于工程循环中，最终验证仍由熵、magic bytes 和 known plaintext 完成*

给 LLM 的任务应当足够小，并带输入证据和验收测试：

text

```
任务：解释函数 sub_401A20 的 key/nonce 生成语义。  输入： - Ghidra/Hex-Rays 伪代码 - 对应汇编 basic block - imported symbols 与目标 libc 版本 - 两组动态跟踪中的 key buffer  输出约束： 1. 逐条区分“由代码证明”和“推测”； 2. 标出整数宽度、符号扩展、循环边界； 3. 生成最小单元测试，不生成批量覆盖磁盘代码； 4. 若伪代码与汇编冲突，以汇编为准并报告冲突。
```

任何由模型生成的恢复代码都应经过人工 code review、静态分析、sanitizer、已知向量和差分测试。恢复现场不接受“模型解释看起来对”作为证据。

## 6、正确Key的判定必须使用多信号验证器

256 次枚举本身几乎没有成本，困难在于自动判断哪个候选产生了正确明文。课件使用 entropy、magic bytes、ASCII ratio、byte diversity 与 UTF-8 解码组成验证 pipeline。

![候选密钥验证流水线](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP850w1wWDd4FiaNDzQv5byJLqVkdoYLQXyPUmAEcMkQOKy1YXxr4bp8Sqr4O2F2rVDwPFrJCGT7rCamM84iankBmbibwialDWF2MzVDw/640?from=appmsg)

*图 9：错误候选通常保持高熵噪声，正确候选则恢复格式头或可解释结构*

单个启发式会误判。压缩文件和加密数据库页本来就可能高熵，文本页也未必以 UTF-8 编码。验证器应根据资产类型加载 profile，并返回分项证据而不是一个神秘总分：

python

```
import math from collections import Counter from dataclasses import dataclass  MAGIC = {     "pdf": b"%PDF-",     "png": b"\x89PNG\r\n\x1a\n",     "zip": b"PK\x03\x04",     "oracle_reco": b"ORCLDISKRECO",     "oracle_data": b"ORCLDISKDATA", }  defentropy(data: bytes) -> float:     ifnot data:         return0.0     counts = Counter(data)     return -sum((n / len(data)) * math.log2(n / len(data)) for n in counts.values())  @dataclass(frozen=True)classVerdict:     accepted: bool     magic: str | None     entropy: float     printable_ratio: floatdefvalidat...