---
title: Black Hat USA 2026：ATM供应链与TPM失守
url: https://mp.weixin.qq.com/s/xud6s9XbHbiYIhQGG3ZnoQ
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:21:10.826782
---

# Black Hat USA 2026：ATM供应链与TPM失守

# Black Hat USA 2026：ATM供应链与TPM失守

原创

Max Luo
Max Luo

白帽子罗棋琛

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 封闭 ATM 供应链的代价：从隐藏扇区到 TPM 失守

> Black Hat USA 2026 议题笔记：The Cost of Obscurity: Exploiting the ATM Supply Chain

ATM 安全经常被概括成几个醒目的名词：全盘加密、Secure Boot、TPM、预启动认证。每一项单独看都合理，组合起来却不自动等于可信启动。只要密钥恢复路径、失败回退、完整性校验和 TPM Policy 之间存在一处松动，攻击者就可能沿着“受保护”的启动链反向恢复秘密、修改磁盘，再让系统替他解密 Windows 分区。

Matt Burch 的公开课件与配套白皮书研究了 CryptWare CryptoPro Secure Disk for BitLocker。该组件作为第三方供应链进入 Diebold Nixdorf Vynamic Security Suite（VSS）的 ATM 安全栈。研究最终获得 9 个 CVE，其中白皮书称 4 个可形成未认证代码执行路径；全部问题经协调披露，并在 CryptoPro v7.7.4 中完成修复验证。

![议题课件封面](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP850uroNOv3OKolyniaqPOP3lRYlfqHeQ6oEcZCPIoykCwwl06rqTYhpQLzpIapAfxOy8gDCOUlWtDs2iatLrn30FdPN2YFURiazqQo/640?from=appmsg)

*图 1：研究对象不是 ATM 业务应用，而是位于 BitLocker 与预启动环境之间的第三方磁盘安全组件*

本文不复现 Ragavan 的磁盘解密、TPM 秘密提取、伪造 LUKS 头、构建替代 RootFS 或恢复 BitLocker 密钥命令；截图也不使用课件中出现的实际秘密值。内容聚焦供应链识别、信任链设计、修复验证与运营检测。任何 ATM 或支付设备测试都必须有资产所有者书面授权，并在隔离实验环境中完成。

## 1、封闭产品没有消失攻击面，只是隐藏了依赖关系

银行 ATM 软件通常只能通过采购与授权渠道获得，外部研究者很难搭建完整环境。这种封闭性可能降低普通扫描器的覆盖，却也让第三方组件长期缺少审视。

研究者没有先取得完整 VSS，而是从 Diebold Nixdorf 公开 EULA 识别供应链。2018 年 VSS 3.0 与 2024 年 VSS 4.5 的许可材料都列出了 CryptoPro SecureDisk，后者还记录了具体组件版本。

![通过 EULA 识别 ATM 软件供应链](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP852zgrBCTmdiciacFOFMF9EFUx10NdWibLVQB9noWrBrGTJsk70vfiboUzwRvQicZ7tc2aeVJYJNiavRg4hDGaibpoCW0uYPufUcjcpMtE/640?from=appmsg)

*图 2：法律与许可清单意外提供了关键 SBOM 线索，证明 CryptoPro 是上层 ATM 安全套件的组成部分*

这条路径揭示一个常见采购缺陷：金融机构拥有“ATM 型号—VSS 版本”的资产表，却没有“VSS—CryptoPro—预启动 Linux—UEFI 模块—开源库”的递归依赖图。上游供应商完成认证后，下游组件可能多年不进入漏洞管理。

最低限度的资产关系应能回答组件版本、部署镜像和修复责任：

yaml

```
asset_id:ATM-SG-004281platform:vendor:Diebold-Nixdorfproduct:Vynamic-Security-Suiterelease:"4.5"security_components:-supplier:CryptWareproduct:CryptoPro-SecureDisk-for-BitLockerdetected_version:"inventory-from-signed-package"minimum_approved_version:"7.7.4"roles: [preboot-auth, disk-encryption-wrapper, integrity-check]     evidence:package_digest:"sha256:REPLACE_WITH_MEASURED_VALUE"installed_at:"2026-07-14T02:20:00Z"source:golden-image-attestationowners:business:atm-platformpatch:endpoint-engineeringsecurity:payment-security
```

版本不能只来自管理界面或 EULA。需要从已签名安装包、磁盘镜像和运行时度量交叉验证，因为上层产品文档可能滞后于实际组件修订号。

## 2、CryptoPro 保护的是一条跨 UEFI、Linux 与 Windows 的启动链

CryptoPro 不是简单的 BitLocker 管理界面。课件列出的能力包括：包装 Microsoft BitLocker、向系统盘注入 Linux 分区、执行 UEFI/Linux/Windows 文件完整性检查，以及支持密码、硬件指纹、智能卡、PKI 和 Helpdesk 等预启动认证方式。

![CryptoPro 的跨系统安全架构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP8517wGql8JY1sYSbdMkI2o7g8WOXIMO3lFF6tEe1nia1qyAJIiabicbUUBtmaEICe24LzEic00yfLwpBbcUUVh5850470miaXoXtOzbs/640?from=appmsg)

*图 3：预启动 OS 先完成认证和完整性检查，再进入 Windows；加密引擎同时涉及厂商模块与 BitLocker*

磁盘大致包含 EFI System Partition、Windows 分区和末端 EDA Partition。EFI 内的 `bzImage` 又包含 Kernel、initramfs 与 `init.sh`，随后挂载 EDA 中的 Linux 环境和数据区。

![从 EFI 镜像进入 initramfs](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP851yKfkl3j9LPicPxypwIeZqbaiaf8X1Knx2Cia9eqH9BDm6iasu3uBhYy4Q1icYfiaonGWYcwc3TzrwkUrfgUyM9TYwqkQw4icxsbrW1E/640?from=appmsg)

*图 4：一块 ATM 系统盘跨越 UEFI、initramfs、Linux 与 Windows，任何阶段的“继续启动”都在为下一阶段背书*

威胁模型必须覆盖物理磁盘访问。ATM 部署在营业厅、商场或街边，机箱与存储介质不应被视为数据中心等强物理边界。对手若能离线复制或修改磁盘，系统仍应满足：

text

```
未授权磁盘修改    |    +--> Secure Boot 拒绝非授权启动组件    +--> Measured Boot 让 TPM Policy 无法解封密钥    +--> initramfs 对任何解密/完整性错误 Fail Closed    +--> DataStore 使用认证加密或独立 MAC 拒绝篡改    +--> Windows BitLocker 密钥不因可重放硬件指纹而恢复
```

任何一个“失败后尝试明文”“只检查魔数”“测量列表可由磁盘提供”的兼容路径，都会把密码学保证降级为启动脚本分支。

## 3、隐藏扇区不是安全边界，而是未登记的攻击面

研究最初从磁盘熵图发现异常：EDA Partition 的文件系统结束后仍有一段高熵数据。逆向 `MountFS` 后，研究者定位到分区尾部的 Layout Table；表中记录 NIX、Log Store、TPM 随机数据、TPM Data Block、DataStore 等多个不在普通文件系统目录里的区域。

![EDA 分区中的异常熵区域](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP852Rb9iaOnBRESN5gvP5hDZ3ZmtTibibzTgkic6JuJ34Im1LkWPGb7TrM0EficDnuqlBLlPQfhAOEHS1gpectCXdJ1MPOKYOCsTkhIMw/640?from=appmsg)

*图 5：文件系统视图与物理扇区视图不一致，分区尾部的高熵区域提示存在额外数据块*

![MountFS 读取隐藏布局表](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP851M2yaJRh00SKmNasyHMwEt7mOyibL3GMgt7jUfC6uD5Vx62HBibDPian2J4P6y57yloFFuaYOR74Wj1qaPBXI94YGEbcGexxHxW0/640?from=appmsg)

*图 6：所谓“隐藏”只是常规管理工具不会展示；运行时代码仍需要可重复定位，因此逆向后位置与结构都可恢复*

将秘密放进未分区扇区、保留块或固定偏移，最多是混淆。合法程序必须知道定位规则，攻击者分析同一二进制也能得到规则。更糟糕的是，这些区域往往绕过文件权限、EDR、文件完整性监控和普通备份审计。

ATM 基线检查应同时记录 GPT、分区、文件系统和未分配区域。下面的结构用于保存黄金镜像的区域摘要；不要在生产 ATM 上由远程脚本直接读取整盘，以免影响可用性和 PCI 范围：

json

```
{"disk_model":"approved-model","logical_sector_size":512,"gpt_digest":"sha256:...","regions":[{"name":"efi","start_lba":"baseline","length":"baseline","sha256":"..."},{"name":"windows","start_lba":"baseline","length":"baseline","bitlocker":true},{"name":"eda","start_lba":"baseline","length":"baseline","sha256":"..."},{"name":"vendor-reserved","start_lba":"baseline","length":"baseline","sha256":"..."}],"signed_by":"atm-golden-image-service"}
```

现场设备只采集只读元数据和抽样摘要，与黄金镜像比对；完整镜像分析放在维修或取证实验室完成。未知区域不应自动标记为恶意，但必须有供应商归属、内容用途和升级变化说明。

## 4、层层加密仍可能把密钥链暴露给离线分析

课件展示了 DataStore 的 AES-XTS 解密流程，以及一组存放 KEK、BitLocker Recovery Password、LUKS 密码和其他密钥材料的文件。系统硬件指纹参与 KEK/BEK 派生，最终恢复 BitLocker 相关秘密。

![DataStore 的 AES-XTS 数据路径](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP851ZelM9ibmGQPV7A9FvrpWBem1hax49YfSicuc3eianmicCrkjO83cZV4klZmmgTzqwnV6icZqyuKYRaS2nR0WiaZ1bXIjwiaE1NbCXM4/640?from=appmsg)

*图 7：XTS 可以保护磁盘扇区机密性，但不自动提供内容认证，也不能修复上游密钥材料可恢复的问题*

![DataStore 内的密钥文件层次](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP853icLIjIkFy5d0gTlJeBlTqiaSd1p7O7MgvqYhAfZcXKmSjtOYErxgWZgmbU9FYOk8T3SKQUoFiblgdaKKcDh5ZmBxxrsiaE4xta4Y/640?from=appmsg)

*图 8：密钥文件、派生表和硬件指纹形成多层依赖；攻击者只需找到一条可离线重建的完整路径*

硬件指纹由 CPUID、DMI、网卡、硬盘序列号和 PCI 信息等汇总而来。这类值适合资产关联，不是高熵秘密。虚拟机可以模拟，物理设备也可能被替换或读取。把它作为密码学 Key Material，不能提供与 TPM 内不可导出密钥相同的保证。

![硬件指纹参与密钥流程](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850RlOHz8iauG0ZE25TSkpZGnQia8IWkdAzvUHEgzs58xSghKnfgicjjNia8N7eTSrDXESHwkrGOgeWeq9VicmicQje38pQqmoNN7r3XI/640?from=appmsg)

*图 9：可枚举硬件属性经汇总后形成指纹；它能绑定配置，却难以抵御掌握磁盘和设备信息的对手*

安全的密钥层次应有清晰边界：根密钥在 TPM/HSM 中不可导出；磁盘数据密钥由随机数生成；封装密钥只在正确启动状态和授权身份下解封；恢复密钥进入独立的银行密钥托管系统，不出现在同一磁盘的“隐藏”区域。

yaml

```
atm_key_hierarchy:root_of_trust:location:TPM_or_HSMexportable:falsevolume_key:generated_by:CSPRNGstored_as:authenticated_wrapped_blobunseal_policy:require:-secure_boot_enabled-approved_firmware_measurements-approved_bootloader_measurements-approved_kernel_and_initramfs_measurements-device_identityrecovery_key:location:bank_central_key_escrowaccess:dual_controlstored_on_atm_disk:false
```

加密算法强度只保护它实际覆盖的边界。密钥可以从旁路路径恢复时，AES-256 与层数都不会补上设计缺口。

## 5、TPM 有效与否，取决于 Policy 是否绑定真实启动状态

TPM Seal 的目标不是“把密钥存进芯片”，而是“只有 PCR 反映批准启动状态时，芯片才释放密钥”。课件发现两个相互加强的问题：TPM 会话所需秘密可从离线 EDA Disk 恢复；默认解封策略只考虑 PCR-15，而它的基础度量域为空，未真正绑定平台启动状态。

![TPM 参与磁盘密钥释放](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4yRoMuNP850uU04OpmibxSic6t6p2gDM76naA8gw8sQFJCSFHWgWLlabob3cQW2AuPWGrIibjJibTom6gmECCurKtu9bBPz6VoETgz5CuQUYEbU/640?from=appmsg)

*图 10：TPM 是密钥释放决策点，但磁盘上仍保存了与会话、Handle 和 Policy 相关的数据*

课件还展示了一种自定义度量：多个 EFI 文件摘要先逐字节 XOR，再把结果用于 PCR 流程。XOR 具有交换性，相同文件集合换序不会改变结果；成对重复还会抵消。这不同于标准 PCR Extend 的链式哈希语义，难以证明准确执行顺序。

![自定义 PCR 度量逻辑](https://mmbiz.qpic.cn/mmbiz_jpg/4yRoMuNP853PsZgp3ov2eIlmtoucSMrdC0SicpapPA585JnDMgiaMSrHms3A4FTgcpRQpmMXSlziaAlkEWfKUicBPiaVOCiaTNY6DNyW017JAfPBo/640?from=appmsg)

*图 11：课件列出的 EFI 组件经 XOR 汇总；自定义“滚动”算法削弱了顺序与重复项的表达能力*

TPM Policy 评审不能只检查配置里 `UseTPM=true`。需要确认：使用哪些 PCR；PCR 值由谁扩展；是否覆盖固件、Secure Boot 状态、Boot Manager、内核、initramfs 与关键配置；Policy 是否由攻击者可修改的磁盘内容决定；失败时系统是否停止。

远程证明服务可使用设备身份和预登记 Golden Measurements 判断状态。以下是简化的验证接口，省略了 TPM Quote 的密码学解析细节，实际应使用成熟 TSS 库：

python

```
from dataclasses import dataclass   @dataclass(frozen=True)classAttestation:     device_id: str     boot_counter: int     nonce: bytes     pcr_digest: bytes     quote_signature: bytes     event_log_digest: bytesdefauthorize_unlock(att: Attestation, challenge: bytes, policy_store) -> bool:     device = policy_store.get_device(att.device_id)     if att.nonce != challenge:         returnFalseifnot tpm_verify_quote(device.ak_public, att):         returnFalseif att.boot_counter <= device.last_boot_counter:         returnFalse     expected = policy_store.approved_measurement(         device.model, device.firmware_release, de...