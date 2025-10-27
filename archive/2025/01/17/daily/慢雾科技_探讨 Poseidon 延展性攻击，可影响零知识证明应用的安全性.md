---
title: 探讨 Poseidon 延展性攻击，可影响零知识证明应用的安全性
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500936&idx=1&sn=433dc45041abe0603c4c00d7a3db7ced&chksm=fddeba0fcaa9331903775c679192d7df3cb0be4b43575a5ac854e2f5dd19fb7c3465ca2299cf&scene=58&subscene=0#rd
source: 慢雾科技
date: 2025-01-17
fetch_date: 2025-10-06T20:11:26.414039
---

# 探讨 Poseidon 延展性攻击，可影响零知识证明应用的安全性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLa61ZTTib3VPVaJUAbPMWltHswIEaiaOgHDB3eZgtRiaSqQuv6f63Zy1uxTPpCjT69Pt3tNJT2D2kPag/0?wx_fmt=jpeg)

# 探讨 Poseidon 延展性攻击，可影响零知识证明应用的安全性

原创

慢雾安全团队

慢雾科技

**背景**

此前我们在[哈希函数的隐藏危险：长度扩展攻击与服务端验证的安全隐患](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247498380&idx=1&sn=e469b9cbc59392bcb3dbe5b3a10b505f&scene=21#wechat_redirect)一文中探讨过哈希函数的长度扩展攻击，指出了 md5/sha1/sha2 算法存在的延展性问题和可能带来的安全风险。

近日，有开发者在 X 上披露了存在于 Iden3 密码学库的一个哈希延展性问题。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLa61ZTTib3VPVaJUAbPMWltHcRh127aISOh3VAeCFYVTXrdicb0yjEzxZmcu3A8ia7cEBAibOny8ib6Drg/640?wx_fmt=png&from=appmsg)

(https://x.com/vdWijden/status/1877046148386451732)

慢雾安全团队对此问题展开了深入研究。

## **什么是 Poseidon**

Poseidon 是一种专为零知识证明系统优化设计的密码学哈希函数。它具有以下主要特点：

* 在有限域上运行，特别适合于基于算术电路的零知识证明系统
* 计算效率高，gas 消耗低
* 主要用于 Merkle 树构建和数据承诺方案
* 被广泛应用于 zkRollup、身份验证等区块链应用场景

例如在目前流行的 Snark 编程语言 Circom 中，就广泛使用了 Poseidon 算法。

## **Poseidon 的延展性**

Poseidon 哈希本身不具有延展性或长度扩展攻击(Length Extension Attack) 问题，这得益于 Poseidon 海绵构造的填充方式(Sponge Padding)[1]:

* 先在消息字符串后添加单个元素 1
* 然后根据需要添加足够多的 0 元素
* 直到消息长度是 (t-c) 的整数倍
* 其中 t 是状态宽度，c 是容量

与具有延展性的哈希对比（如 SHA256）：

```
SHA256(具有延展性):message -> [原始消息 | 填充长度] -> 迭代压缩函数 -> hash值攻击者可以继续使用最终状态继续添加数据
Poseidon(不具有延展性):message -> [固定t-1长度] -> 置换函数 -> hash值无法从hash值恢复内部状态
```

但 Iden3 实现的 Poseidon 库与标准算法却有一些区别，主要体现在它的数据填充方案不同，这也导致了它出现延展性问题。

我们来分析一下它的代码实现[2]：

```
// HashBytes returns a sponge hash of a msg byte slice split into blocks of 31 bytesfunc HashBytes(msg []byte) (*big.Int, error) {  // not used inputs default to zero  inputs := make([]*big.Int, spongeInputs)  for j := 0; j < spongeInputs; j++ {    inputs[j] = new(big.Int)  }  dirty := false  var hash *big.Int  var err error
  k := 0  for i := 0; i < len(msg)/spongeChunkSize; i++ {    dirty = true    inputs[k].SetBytes(msg[spongeChunkSize*i : spongeChunkSize*(i+1)])    if k == spongeInputs-1 {      hash, err = Hash(inputs)      dirty = false      if err != nil {        return nil, err      }      inputs = make([]*big.Int, spongeInputs)      inputs[0] = hash      for j := 1; j < spongeInputs; j++ {        inputs[j] = new(big.Int)      }      k = 1    } else {      k++    }  }
  if len(msg)%spongeChunkSize != 0 {    // the last chunk of the message is less than 31 bytes    // zero padding it, so that 0xdeadbeaf becomes    // 0xdeadbeaf000000000000000000000000000000000000000000000000000000    var buf [spongeChunkSize]byte    copy(buf[:], msg[(len(msg)/spongeChunkSize)*spongeChunkSize:])    inputs[k] = new(big.Int).SetBytes(buf[:])    dirty = true  }
  if dirty {    // we haven't hashed something in the main sponge loop and need to do hash here    hash, err = Hash(inputs)    if err != nil {      return nil, err    }  }
  return hash, nil}
```

HashBytes 函数用于对给定的字节切片 msg 进行海绵哈希(sponge hash)，并将其分割成 31 字节的块。首先，函数初始化了一个 inputs 切片，长度为 spongeInputs，并将每个元素设置为新的大整数 big.Int。这些未使用的输入默认设置为零。

假设有一个消息需要填充：

```
标准 Poseidon: [消息] + [1] + [0,0,0...]Iden3 实现: [消息] + [0,0,0...]
```

这种填充方案的区别看似微小，但在密码学中是很关键的。标准 Poseidon 通过添加 1 再补 0 的方式可以确保不同长度的输入消息会产生不同的哈希值，而纯补 0 的方式却会导致安全隐患。

## **漏洞危害**

Iden3 Poseidon 的延展性有哪些具体的危害，让我们写一个示例演示一下：

```
msg1 := []byte("9")hash1, _ := poseidon.HashBytes(msg1)fmt.Printf("Hash of 1: %s\n", hash1.String())fmt.Println("Value: ", new(big.Int).SetBytes(msg1))
msg2 := []byte("9\x00\x00\x00\x00")hash2, _ := poseidon.HashBytes(msg2)fmt.Printf("Hash of 9\\x00\\x00\\x00\\x00: %s\n", hash2.String())fmt.Println("Value: ", new(big.Int).SetBytes(msg2))
```

运行输出：

```
Hash of 9: 11642804437010365980265264676069673149904017141487814048230421306886008365708Value:  57Hash of 9\x00\x00\x00\x00: 11642804437010365980265264676069673149904017141487814048230421306886008365708Value:  244813135872
```

基于代码示例的结果，我们可以看到这个漏洞可能带来以下危害：

* **哈希碰撞：**利用延展性漏洞构造的不同输入值（57 和 244813135872）产生了相同的哈希值，这可能导致在零知识证明系统中出现验证绕过
* **数据完整性问题：**由于 Iden3 的实现采用了纯补 0 的填充方案，攻击者可能通过构造特定的输入来生成碰撞，从而破坏系统的安全性验证

这在实际应用中可能会影响：

* zkRollup、身份验证等依赖 Poseidon 哈希的区块链应用
* 使用 Circom 编写的智能合约

##

## **总结**

本文探讨了 Poseidon 哈希函数在 Iden3 密码学库中存在的延展性问题。Poseidon 是一种为零知识证明系统优化的哈希函数，虽然标准 Poseidon 不具有延展性，但 Iden3 的实现由于采用了纯补 0 的填充方案而非标准的填充方式，导致可能出现哈希碰撞问题，这对依赖 Poseidon 哈希的 zkRollup、身份验证等区块链应用以及使用 Circom 编写的智能合约都可能造成安全隐患。

**参考资料**

[1] https://eprint.iacr.org/2019/458.pdf

[2] https://github.com/iden3/go-iden3-crypto/blob/master/poseidon/poseidon.go

作者 | Johan

编辑 | Liz

**往期回顾**

[以小博大 —— UniLend 被黑事件分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500933&idx=1&sn=3f6f83f296e51b2befe35efb58807026&scene=21#wechat_redirect)

[慢雾：演员王星被骗事件相关聊天截图调查](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500907&idx=1&sn=1e629e1d6e96b48b3c5962aadba90a92&scene=21#wechat_redirect)

[2024 区块链安全与反洗钱年度报告解读之反洗钱态势和数据](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500849&idx=1&sn=a4c8a7404ac4c33d52ec625858d74fc6&scene=21#wechat_redirect)

[2024 区块链安全与反洗钱年度报告解读之朝鲜黑客和混币工具](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500849&idx=2&sn=03cec5bfbda8fc30283fb3e05ded7803&scene=21#wechat_redirect)

[2024 区块链安全与反洗钱年度报告解读之安全态势](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247500831&idx=1&sn=4974804d9f1a864c5fe5579c7d137dd0&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaa3Th7YiamUUBwq1Iiby9N9lWh3tKP2MVjM6L3UxtTnuUy6iaegsOP2IrqZYsIBM2v3XgC5O2JTbY5g/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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