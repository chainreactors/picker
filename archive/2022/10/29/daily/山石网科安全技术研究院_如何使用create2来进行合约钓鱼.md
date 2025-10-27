---
title: 如何使用create2来进行合约钓鱼
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247497230&idx=1&sn=b67c506ad5aba0c66fe2539bd1a0cfa9&chksm=fa5223b0cd25aaa66ad3553d17b3de8d03d7723a0f05f980b720030fc27318735c7b3d1429dd&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-10-29
fetch_date: 2025-10-03T21:14:39.674891
---

# 如何使用create2来进行合约钓鱼

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRtMsIQoh2gByicZWrS2qVJBYUq7daavNPW7uicQkB0NmVhX4KXTmF7lfQAOmVaun0nHj8u9vBH8flA/0?wx_fmt=jpeg)

# 如何使用create2来进行合约钓鱼

原创

核心基础实验室

山石网科安全技术研究院

**如**

**何**

**部**

**署**

**合**

**约**

## **1.1   create**

在合约中部署合约可以使用create字节码，该字节码会通过部署合约的合约地址，nonce值来计算新合约的地址，计算公式为：

```
keccak256(rlp.encode(address, nonce))[12:]
```

在go-ethereum中的vm/evm.go中有该字节码的实现：

```
// Create creates a new contract using code as deployment code.
func (evm *EVM) Create(caller ContractRef, code []byte, gas uint64, value *big.Int) (ret []byte, contractAddr common.Address, leftOverGas uint64, err error) {
 contractAddr = crypto.CreateAddress(caller.Address(), evm.StateDB.GetNonce(caller.Address()))
 return evm.create(caller, &codeAndHash{code: code}, gas, value, contractAddr, CREATE)
}

// CreateAddress creates an ethereum address given the bytes and the nonce
func CreateAddress(b common.Address, nonce uint64) common.Address {
 data, _ := rlp.EncodeToBytes([]interface{}{b, nonce})
 return common.BytesToAddress(Keccak256(data)[12:])
}
```

在这个公式中，address和nonce都不能被控制，这意味着无法控制新合约的地址。

---

## **1.2   create2**

create2是在君士坦丁堡硬分叉中新加入的一个字节码，该字节码不再使用nonce，并且加入了可被控制的参数salt和init code。计算公式如下：

```
keccak256(0xff ++ address ++ salt ++ keccak256(init_code))[12:]
```

address为部署合约的工厂合约的地址，salt是一个32bytes长的混淆值，init\_code是合约的创建字节码。

create2的实现在vm/evm.go中：

```
// Create2 creates a new contract using code as deployment code.
//
// The different between Create2 with Create is Create2 uses keccak256(0xff ++ msg.sender ++ salt ++ keccak256(init_code))[12:]
// instead of the usual sender-and-nonce-hash as the address where the contract is initialized at.
func (evm *EVM) Create2(caller ContractRef, code []byte, gas uint64, endowment *big.Int, salt *uint256.Int) (ret []byte, contractAddr common.Address, leftOverGas uint64, err error) {
 codeAndHash := &codeAndHash{code: code}
 contractAddr = crypto.CreateAddress2(caller.Address(), salt.Bytes32(), codeAndHash.Hash().Bytes())
 return evm.create(caller, codeAndHash, gas, endowment, contractAddr, CREATE2)
}

// CreateAddress2 creates an ethereum address given the address bytes, initial
// contract code hash and a salt.
func CreateAddress2(b common.Address, salt [32]byte, inithash []byte) common.Address {
 return common.BytesToAddress(Keccak256([]byte{0xff}, b.Bytes(), salt[:], inithash)[12:])
}
```

合约的创建字节码部署合约的字节码，但是可以通过solidiity中的creationCode获取：

```
bytecodes = type(Test).creationCode;
```

现在create2中的参数都已经能被控制，理论上只要爆破salt，就可以获取想要的合约地址。

**授**

**权**

**钓**

**鱼**

在实际的web3应用中，用户经常要向其他合约进行授权，来操纵自己的资产。用户在对比合约地址时往往只会对比合约的前几位和后几位，而不去检查整个地址是否完全相同。现在的用户基本知道外部账户可以爆破出相似的地址，但对于合约地址就不太会有这方面的意识了。

所以只要部署出相似地址的恶意合约，就可以进行钓鱼攻击。

**爆**

**破**

**salt**

计算合约地址在Create2函数中：

```
contractAddr = crypto.CreateAddress2(caller.Address(), salt.Bytes32(), codeAndHash.Hash().Bytes())
```

使用的是crypto模块中的CreateAddress2函数：

```
func CreateAddress2(b common.Address, salt [32]byte, inithash []byte) common.Address {
 return common.BytesToAddress(Keccak256([]byte{0xff}, b.Bytes(), salt[:], inithash)[12:])
}
```

为了爆破salt，我们选择直接使用这个函数。

接着部署Deployer合约，并调用getInitCode获取init byte code。

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Deployer {

    bytes public initCode;

    function  getInitCode() public {
        initCode = type(Test).creationCode;
    }

    function deploy(uint _salt) public returns(address){

        address addr;
        bytes memory bytecode = type(Test).creationCode;
        assembly {
            addr := create2(0, add(bytecode, 0x20), mload(bytecode), _salt)
        }
        return addr;
  }
}
```

调用getInitCode就可以获取字节码：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRtMsIQoh2gByicZWrS2qVJBN77UjxAQK4dalEzo9aoEpDxGDGNuojsnLJsYun4ibG9NHGBfIUDnkUw/640?wx_fmt=png)

导入go-ethereum的common模块，该模块中有相关格式转化的工具，再将地址、字节码进行格式转化，并计算字节码的哈希值：

```
devContractAddress
:= common.BytesToAddress(common.FromHex("0x26b989b9525Bb775C8DEDf70FeE40C36B397CE67"))
initByteCode := common.FromHex("0x33ff")
initCodeHash := crypto.Keccak256(initByteCode)
```

使用rand包生成一个无符号的64位随机整数，并将该整数转化位bytes32的格式。再将这些变量作为参数输入CreateAddress2函数中，获取到的address就是计算出的地址：

```
i := rand.Uint64()
salt := uint256.NewInt(i).Bytes32()
address := crypto.CreateAddress2(devContractAddress, salt, initCodeHash).String()
fmt.Println(address)
```

只要不断重复这个过程并判断生成的地址是否满足我们的要求，就可以获取相应的salt：

```
func getAddress(devContractAddress common.Address, initCodeHash []byte, p string, s string) {
 for {
  i := rand.Uint64()
  salt := uint256.NewInt(i).Bytes32()
  address := crypto.CreateAddress2(devContractAddress, salt, initCodeHash).String()
  if strings.HasPrefix(address, p) && strings.HasSuffix(address, s) {
   fmt.Println(i)
   fmt.Println(address)
   fmt.Println()
  }
 }
}
```

**测**

**试**

首先编写待部署的测试合约：

```
contract Test {
    address public owner;
event Ev();

    function met() public {
        owner = msg.sender;
    }
    function get() public {
        require(owner == msg.sender);
        emit Ev();
    }
}
```

部署工厂合约，并获取测试合约的init byte code:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRtMsIQoh2gByicZWrS2qVJBPq3UUcoSPnZVOA518ol4umia1ymu05Xib89z8GO8eibkhF1W5UlEfNemA/640?wx_fmt=png)

这里设置生成的address开头为123，结尾为abc，开始爆破salt：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRtMsIQoh2gByicZWrS2qVJBUdUibIwRad5XtOniahS4kV5VyabTGvzj7TIKNFWhPepkFRTC9W8KM9cg/640?wx_fmt=png)

计算的出salt和地址，再将所得到的salt作为参数调用工厂合约的deploy函数：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRtMsIQoh2gByicZWrS2qVJBY5tdtQHbLKicyJiaiaKQBfE6jxibPmwv0kbVJtYN4Al9YBXqHLqoANyDTg/640?wx_fmt=png)

合约部署成功，并且生成的地址与计算出的一致。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRtMsIQoh2gByicZWrS2qVJB4SawEtUEIKxicJiaIicv0urKmqDFbPRR7Bk0PAIegxtxWtiagYnr4xUdIg/640?wx_fmt=png)

**END**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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