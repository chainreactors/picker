---
title: 全球流行勒索病毒家族加解密算法详解
url: https://mp.weixin.qq.com/s/iL2BhMn6HQwHJScWj12mNw
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:33.131581
---

# 全球流行勒索病毒家族加解密算法详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/M5H82XuSHY5OOIJeiclWqReTkvxnakkQuguLu70AmC26VBiavXge1pMVzKZ9eyAcwaQeR5dc1MuWPxTVss9Oe273SHgjAO9S5icCaBvvY3yKs4/0?wx_fmt=jpeg)

# 全球流行勒索病毒家族加解密算法详解

原创

pandazhengzheng
pandazhengzheng

安全分析与研究

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 目录

* 一、通用勒索病毒加密范式
* 二、核心加密算法数学原理
* 三、加密算法演进时间线
* 四、主流勒索病毒家族加密架构深度解析
* 五、加密算法对比总表
* 六、解密可行性全景评估
* 七、勒索病毒解密方法与工具原理详解
* 八、密钥生命周期与应急响应窗口
* 九、防御与响应建议

---

## 一、通用勒索病毒加密范式

### 1.1 混合加密体系架构

所有现代勒索软件均采用**混合加密体系（Hybrid Cryptography）**，结合对称加密的高效性与非对称加密的安全性：

![](https://mmbiz.qpic.cn/mmbiz_png/M5H82XuSHY4HyD3vIRmZWMvHeYm08yJ2nPic6wia6Tyia4icrLl4bYiambqMYUCDSDzeWufdfQgTpCZY34zgTpBAwEWia4qrwYciaGkfvH13iaMiaibmQ/640?wx_fmt=png&from=appmsg)

| 组件 | 算法类型 | 典型算法 | 作用 | 关键风险点 |
| --- | --- | --- | --- | --- |
| **文件加密层** | 对称加密 | AES-128/256（CBC/CTR模式）、Salsa20、ChaCha20 | 快速加密海量用户文件 | 密钥若未被擦除或泄露，存在离线解密可能 |
| **密钥封装层** | 非对称加密 | RSA-2048/3072/4096、ECC（secp256k1）、ElGamal | 加密对称密钥，确保仅攻击者私钥可解封 | RSA密钥长度不足（<2048）或实现缺陷可被破解 |
| **密钥派生层** | KDF | PBKDF2、HKDF、Scrypt | 从密码/硬件指纹生成加密密钥 | 硬编码盐值或低迭代次数易被暴力破解 |
| **密钥存储层** | 内存/磁盘 | 内存明文、注册表加密存储、文件尾部嵌入、C2下发 | 控制密钥生命周期与传输路径 | 内存残留密钥是应急响应黄金窗口 |

### 1.2 加密流程通用模型

```
勒索病毒加密通用流程:

  ① 密钥生成
     随机数生成器(CSPRNG) / C2远程下发 → 生成对称密钥(AES/ChaCha20)
     → 对称密钥长度: AES-128(16B) / AES-256(32B) / ChaCha20(32B)

  ② 密钥封装
     对称密钥 → RSA/ECC公钥加密 → 密文密钥(仅攻击者私钥可解)
     → RSA封装: C = M^e mod N (M=对称密钥, e=公钥指数, N=模数)
     → ECC封装: 共享密钥 = d_A × Q_B (ECDH密钥协商)

  ③ 文件遍历与加密
     遍历文件系统 → 跳过系统关键文件 → 对称加密每个文件
     → AES-CBC: C_i = E_K(P_i ⊕ C_{i-1}), C_0 = IV
     → AES-CTR: C_i = P_i ⊕ E_K(Counter+i)
     → ChaCha20: C_i = P_i ⊕ ChaCha20(Key, Nonce, Counter+i)
     → 加密后修改文件后缀 → 写入勒索信

  ④ 密钥销毁
     内存清零(SecureZeroMemory) → 删除卷影副本(vssadmin)
     → 覆写原始文件 → 擦除密钥残留痕迹

  ⑤ 勒索通知
     桌面壁纸修改 → 勒索信(含Tor支付链接) → 倒计时威胁
```

> **关键洞察**：**92.3%的勒索软件在加密完成后主动清除内存中的对称密钥**（来源：AV-TEST 2025勒索软件行为白皮书），使得"内存转储+密钥提取"成为唯一高价值解密路径——但该操作需在进程存活且未触发密钥轮换前完成。

---

## 二、核心加密算法数学原理

### 2.1 AES（Advanced Encryption Standard）

**数学基础**：基于有限域 GF(2⁸) 上的代换-置换网络（SPN）

```
AES加密流程 (以AES-128为例):
  输入: 128位明文P, 128位密钥K
  输出: 128位密文C

  ① 密钥扩展 (Key Expansion)
     K → RoundKeys[0..10] (11个128位轮密钥)
     每轮使用Rijndael密钥调度算法派生

  ② 初始轮密钥加 (AddRoundKey)
     State = P ⊕ RoundKeys[0]

  ③ 主轮循环 (Round 1-9, 每轮4步):
     a) SubBytes:  S盒代换 (基于GF(2⁸)上的乘法逆元)
                     S(x) = A·x⁻¹ + b (A为8×8矩阵, b=0x63)
     b) ShiftRows: 行移位 (第i行左移i字节)
     c) MixColumns: 列混合 (基于GF(2⁸)上多项式乘法)
                     c(x) = {03}x³ + {01}x² + {01}x + {02}
     d) AddRoundKey: State ⊕ RoundKeys[i]

  ④ 最终轮 (Round 10, 无MixColumns):
     SubBytes → ShiftRows → AddRoundKey → C

AES-CBC模式 (勒索软件最常用):
  C_0 = IV (16字节随机初始化向量)
  C_i = AES_Encrypt_K(P_i ⊕ C_{i-1})
  解密: P_i = AES_Decrypt_K(C_i) ⊕ C_{i-1}

AES-CTR模式 (并行加密,更快):
  C_i = P_i ⊕ AES_Encrypt_K(Nonce || Counter+i)
  解密: P_i = C_i ⊕ AES_Encrypt_K(Nonce || Counter+i)
  → 注意: CTR模式加密和解密操作完全相同!
```

**勒索软件中的AES使用**：

| 家族 | AES变体 | 模式 | 密钥长度 | 每文件密钥 | 特殊实现 |
| --- | --- | --- | --- | --- | --- |
| WannaCry | AES | CBC | 128位 | 否(每主机1个) | Windows CryptoAPI |
| Makop | AES | CBC | 256位 | 否(30秒轮换) | 自定义实现 |
| GlobeImposter | AES | CBC/ECB | 128位 | 是(2.0+) | 部分版本ECB模式(不安全) |
| STOP/Djvu | AES | CBC | 128位 | 否 | 密钥派生自硬件ID |
| Conti | AES | CBC | 256位 | 否 | 多线程并行加密 |

### 2.2 ChaCha20流密码

**数学基础**：基于ADD-ROTATE-XOR（ARX）运算的流密码，Salsa20改进版

```
ChaCha20加密流程:
  输入: 256位密钥K, 96位Nonce, 明文P
  输出: 密文C

  ① 初始状态矩阵 (4×4, 每元素32位):
     State[0]  = "expa"    State[1]  = "nd 3"    State[2]  = "2-by"    State[3]  = "te k"
     State[4..7] = K[0..3]  (密钥, 128位)
     State[8..11] = K[4..7]  (密钥, 128位)
     State[12] = Counter   State[13..15] = Nonce[0..2]

  ② 20轮Quarter Round运算 (10次双轮):
     每轮包含4次 Quarter Round:
     a += b;  d ^= a;  d <<<= 16
     c += d;  b ^= c;  b <<<= 12
     a += b;  d ^= a;  d <<<= 8
     c += d;  b ^= c;  b <<<= 7
     (其中 += 是模2³²加法, ^= 是XOR, <<< 是循环左移)

  ③ 生成密钥流:
     KeyStream_i = State + ChaCha20_Round(State, Counter+i)

  ④ 加密:
     C_i = P_i ⊕ KeyStream_i  (逐字节异或)
     解密: P_i = C_i ⊕ KeyStream_i  (加密=解密,对称操作)
```

**ChaCha20 vs AES对比**（勒索软件选择依据）：

| 维度 | AES-256 | ChaCha20 |
| --- | --- | --- |
| 速度(无AES-NI) | ~5 cycles/byte | ~1.5 cycles/byte |
| 速度(有AES-NI) | ~0.6 cycles/byte | ~1.5 cycles/byte |
| 硬件加速 | AES-NI指令集 | 无(纯软件即可快速) |
| 检测规避 | AES-NI可被EDR监控 | 无特殊指令特征，更隐蔽 |
| 勒索软件采用 | 传统家族(WannaCry/Makop) | 现代家族(LockBit3.0/BlackCat) |

### 2.3 Salsa20流密码

**数学基础**：ChaCha20的前身，ARX结构，NotPetya使用

```
Salsa20核心函数:
  与ChaCha20的区别:
  - Quarter Round中循环左移位数不同: (7,12,17,19) vs ChaCha20的(16,12,8,7)
  - 初始状态矩阵排列不同
  - 安全性: Salsa20/20(20轮)仍安全,但ChaCha20更优(扩散更快)

NotPetya中的Salsa20:
  密钥 = 硬编码种子 ⊕ 当前时间戳
  加密目标 = NTFS MFT (主文件表)
  → Salsa20(Key, Nonce=0, MFT_data)
  → MFT加密后文件系统瘫痪,文件无法定位
```

### 2.4 RSA非对称加密

**数学基础**：基于大整数分解困难性

```
RSA密钥生成:
  ① 选择两个大素数 p, q (各1024/2048位)
  ② 计算 N = p × q (模数, 2048/4096位)
  ③ 计算欧拉函数 φ(N) = (p-1)(q-1)
  ④ 选择公钥指数 e (通常65537 = 2¹⁶+1)
  ⑤ 计算私钥指数 d = e⁻¹ mod φ(N)
  → 公钥: (e, N)    私钥: (d, N)

RSA加密 (密钥封装):
  C = M^e mod N
  其中 M = 对称密钥(AES/ChaCha20 Key)
  → C写入文件尾部或勒索信

RSA解密 (需私钥):
  M = C^d mod N
  → 无私钥则需分解N=p×q (RSA-1024可行, RSA-2048+不可行)

RSA-OAEP填充 (现代实现):
  M_pad = OAEP_Encode(M, seed)
  C = M_pad^e mod N
  → OAEP提供语义安全性,防止选择密文攻击
```

**勒索软件中的RSA使用**：

| 家族 | RSA密钥长度 | 公钥来源 | 私钥存储 | 暴力分解可行性 |
| --- | --- | --- | --- | --- |
| WannaCry | 2048 | 硬编码 | C2服务器 | 不可行(2¹¹²运算量) |
| STOP(旧版) | **1024** | 硬编码 | C2服务器 | **可行** (<72小时,普通工作站) |
| STOP(新版) | 2048 | 硬编码 | C2服务器 | 不可行 |
| Makop | 2048 | 硬编码 | C2服务器 | 不可行 |
| Conti | 3072 | 本地生成+C2 | C2服务器 | 不可行(更强) |

### 2.5 ECC椭圆曲线加密

**数学基础**：基于椭圆曲线离散对数问题（ECDLP）困难性

```
ECC密钥协商 (ECDH, LockBit 3.0使用):
  曲线: secp256k1 (y² = x³ + 7 mod p)
  → 与比特币使用相同曲线

  ① 攻击者生成长期密钥对: (d_A, Q_A = d_A × G)
  ② 每次感染生成临时密钥对: (d_B, Q_B = d_B × G)
  ③ 共享密钥: K = d_A × Q_B = d_B × Q_A = d_A × d_B × G
  ④ 用K派生AES/ChaCha20密钥: HKDF-SHA256(K, salt, info)

  优势 vs RSA-2048:
  - 密钥更短: 256位ECC ≈ 3072位RSA安全强度
  - 运算更快: 椭圆曲线点乘 vs 大数模幂
  - 带宽更小: 公钥仅33字节(compressed) vs RSA 256字节
```

### 2.6 密钥派生函数（KDF）

```
PBKDF2 (GlobeImposter 4.0使用):
  DK = T1 ∥ T2 ∥ ... ∥ Tdklen/hlen
  Ti = F(Password, Salt, c, i)
  F(Password, Salt, c, i) = U1 ⊕ U2 ⊕ ... ⊕ Uc
  U1 = PRF(Password, Salt ∥ INT(i))
  Uj = PRF(Password, U_{j-1})
  → c=迭代次数(越大越慢), Salt=盐值(硬编码则可提取)

HKDF (LockBit 3.0使用):
  ① Extract: PRK = HMAC-Hash(salt, IKM)
  ② Expand: OKM = T(1) ∥ T(2) ∥ ...
     T(i) = HMAC-Hash(PRK, T(i-1) ∥ info ∥ i)
  → IKM=输入密钥材料, salt=设备UUID, info="LOCKBIT3"
  → 输出: ChaCha20密钥(32字节)
```

---

## 三、加密算法演进时间线

| 时代 | 时间段 | 核心特征 | 代表家族 | 密钥管理特点 |
| --- | --- | --- | --- | --- |
| **弱密钥时代** | 2017-2019 | RSA-1024/硬编码公钥 | WannaCry、STOP(旧版)、GlobeImposter | 密钥长度不足，硬编码公钥可提取 |
| **密钥管理演进** | 2019-2022 | KDF派生/密钥轮换/C2管控 | Makop、GlobeImposter4.0、LockBit2.0 | 引入PBKDF2/定时轮换，暴力破解成本激增 |
| **现代加密时代** | 2022-2026 | ChaCha20/ECC/HSM/AI变异 | LockBit3.0+、AI辅助变种 | C2动态管控+HSM保护，离线解密几乎不可能 |

---

## 四、主流勒索病毒家族加密架构深度解析

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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