---
title: 以太坊虚拟机create系列字节码解析
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499821&idx=1&sn=adfc9def3c3dffce1406c6b95a410cd9&chksm=fa521593cd259c8559dcb5b37db11c25a89a0a3c9df10d177789583605b26b59ae9e893fcd46&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-02-07
fetch_date: 2025-10-04T05:52:30.009970
---

# 以太坊虚拟机create系列字节码解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnS3vHnuZFv1fEIMwppHJ2iclJgvBEEob2JCwiaaovjV7M1ibax2dQUibnkasQF2tbdH6wA3Gsf1MTOxgg/0?wx_fmt=jpeg)

# 以太坊虚拟机create系列字节码解析

neicun

山石网科安全技术研究院

在合约中创建新的合约可以使用create字节码，目前create字节码一共有两个，分别是create和create2。

**0****1**

**create**

### 原理

create可以在合约执行的过程中部署新的合约。

go-ethereum中字节码的实现在instructions.go文件中：

在该文件中有create字节码的实现：

```
func opCreate(pc *uint64, interpreter *EVMInterpreter, scope *ScopeContext) ([]byte, error)
```

在这个函数中调用Create来创建合约：

```
res, addr, returnGas, suberr := interpreter.evm.Create(scope.Contract, input, gas, bigVal)
```

Create的实现：

```
// Create creates a new contract using code as deployment code.
func (evm *EVM) Create(caller ContractRef, code []byte, gas uint64, value *big.Int) (ret []byte, contractAddr common.Address, leftOverGas uint64, err error) {
 contractAddr = crypto.CreateAddress(caller.Address(), evm.StateDB.GetNonce(caller.Address()))
 return evm.create(caller, &codeAndHash{code: code}, gas, value, contractAddr, CREATE)
}
```

可以发现在计算地址时，使用了调用者的地址与调用者的nonce值，再看一下CreateAddress的实现：

```
// CreateAddress creates an ethereum address given the bytes and the nonce
func CreateAddress(b common.Address, nonce uint64) common.Address {
 data, _ := rlp.EncodeToBytes([]interface{}{b, nonce})
 return common.BytesToAddress(Keccak256(data)[12:])
}
```

可以发现地址是将调用者的地址与nonce组合后取其哈希值的前12位。

来测试一下：

```
contract Dev {

    CryptoTech public tec;

    function dev() public {
        tec = new CryptoTech();
    }
}

contract CryptoTech {

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

这里使用Dev合约来部署一个CryptoTech合约。首先先部署Dev合约并获取其地址：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnS3vHnuZFv1fEIMwppHJ2iclUg0nB6qQ3tPkgJN2bkURUuqgwiaYRVpRPXqJF2dPdibAbEdP5PTJPP7Q/640?wx_fmt=png)

获取到地址：0xd9145CCE52D386f254917e481eB44e9943F39138。

这里调用go-ethereum中的CreateAddress函数进行测试：

```
func TestCreate(t *testing.T) {
address := common.BytesToAddress(common.FromHex("0xd9145CCE52D386f254917e481eB44e9943F39138"))
var nonce uint64 = 1
contractAddr := crypto.CreateAddress(address, nonce)
fmt.Println(contractAddr)
}
```

获取到的地址为：0x5C9eb5D6a6C2c1B3EFc52255C0b356f116f6f66D

这时再调用dev函数，得到部署到的合约地址为：0x5C9eb5D6a6C2c1B3EFc52255C0b356f116f6f66D。与计算得到的一致。

### 存在的问题

新地址只与调用者地址与nonce有关，并且nonce只会从1开始递增，所以生成的地址是完全随机且无法控制的。

**02****‍**

**create 2**

原理

查看create2的实现：

```
// Create2 creates a new contract using code as deployment code.
//
// The different between Create2 with Create is Create2 uses keccak256(0xff ++ msg.sender ++ salt ++ keccak256(init_code))[12:]
// instead of the usual sender-and-nonce-hash as the address where the contract is initialized at.
func (evm *EVM) Create2(caller ContractRef, code []byte, gas uint64, endowment *big.Int, salt *uint256.Int) (ret []byte, contractAddrcommon.Address, leftOverGas uint64, err error) {
codeAndHash := &codeAndHash{code: code}
contractAddr = crypto.CreateAddress2(caller.Address(), salt.Bytes32(), codeAndHash.Hash().Bytes())
return evm.create(caller, codeAndHash, gas, endowment, contractAddr, CREATE2)
}
```

使用create2创建新合约的地址与调用者的地址，一个可以自定义的salt字段和待部署合约的codehash有关，再查看CreateAddress2的实现：

```
// CreateAddress2 creates an ethereum address given the address bytes, initial
// contract code hash and a salt.
func CreateAddress2(b common.Address, salt [32]byte, inithash []byte) common.Address {
return common.BytesToAddress(Keccak256([]byte{0xff}, b.Bytes(), salt[:], inithash)[12:])
}
```

可以看出计算新地址的过程为：

*address = keccak256(0xff + sender\_address + salt + keccak256(init\_code))[12:]*

测试：

```
contract Deployer {

   bytes public initCode;

   function  getInitCode() public {
       initCode = type(CryptoTech).creationCode;
  }

   function deploy(uint _salt) public returns(address){

       address addr;
       bytes memory bytecode = initCode;
       assembly {
           addr := create2(0, add(bytecode, 0x20), mload(bytecode), _salt)
      }
       return addr;
}
}

contract CryptoTech {

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

利用Deployer合约创建CryptoTech合约，首先创建Deployer合约：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnS3vHnuZFv1fEIMwppHJ2iclmYmibmkksrhJUjWE02rxjp47LHjOCvENfcHJdrZR2AMETaSHnP8pwuA/640?wx_fmt=png)

获取到地址：0xf8e81D47203A594245E36C48e151709F0C19fBe8

调用getInitCode获取合约字节码：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnS3vHnuZFv1fEIMwppHJ2iclV2jJrGtbGNoBUPwgOGKyTiaFDjTVxloNJL4ia1exFKsAyqg8ibtNKktjQ/640?wx_fmt=png)

使用CreateAddress2进行测试：

```
func TestCreate2(t *testing.T) {
devContractAddress := common.BytesToAddress(common.FromHex("0xf8e81D47203A594245E36C48e151709F0C19fBe8"))
initByteCode :=common.FromHex("0x608060405234801561001057600080fd5b506101b0806100206000396000f3fe608060405234801561001057600080fd5b50600436106100415760003560e01c806362cac514146100465780636d4ce63c146100505780638da5cb5b1461005a575b600080fd5b61004e61008e565b005b6100586100d0565b005b610062610156565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550565b3373ffffffffffffffffffffffffffffffffffffffff1660008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161461012857600080fd5b7f5d91a2ed2d89c7f53a48d7e2cd926f2b475e28e282ca9ad5421abee5dd6858e660405160405180910390a1565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff168156fea26469706673582212205a4428ae01fc5f6e0b749be6bb5c7852c8c6fdf8349e91e999f19604ac0a318f64736f6c63430007060033")
initCodeHash := crypto.Keccak256(initByteCode)

i := rand.Uint64()
salt := uint256.NewInt(i).Bytes32()
address := crypto.CreateAddress2(devContractAddress, salt, initCodeHash).String()
fmt.Println(address)
}
```

这里salt采用64位无符号的随机值：5577006791947779410

计算出的地址为：0x84d471Fa3D2bB782f62E107C7e74E9964aBE5d28

调用deploy函数：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnS3vHnuZFv1fEIMwppHJ2iclkZxrTVWdxf38ypnnljx1vJr9HT7Ks3zSrfghkZB9wGuIYFSehfpGCg/640?wx_fmt=png)

获取到的地址为：0x84d471Fa3D2bB782f62E107C7e74E9964aBE5d28

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnS3vHnuZFv1fEIMwppHJ2iclTVyuodsX5OvswGvnSribt5YTjgPzkoEBLRmX6z8YvHHxpAuS0eNNXow/640?wx_fmt=png)

与计算得到的地址相同。

### 存在的问题

使用create2可以使用相同的外部地址在不同的EVM链上部署相同的合约地址。

同时，create2根据init code来计算地址，只要新合约编译完成后就可以确定新的地址。

在UniwapV2中就使用create2字节码来创建新的交易对，这样可以保证能在交易对部署之前获取到地址：

```
function createPair(address tokenA, address tokenB) external returns (address pair) {
       require(tokenA != tokenB, 'UniswapV2: IDENTICAL_ADDRESSES');
      (address token0, address token1) = tokenA < tokenB ? (tokenA, tokenB) : (tokenB, tokenA);
       require(token0 != address(0), 'UniswapV2: ZERO_ADDRESS');
       require(getPair[token0][token1] == address(0), 'UniswapV2: PAIR_EXISTS'); // single check is sufficient
       bytes memory bytecode = type(UniswapV2Pair).creationCode;
       bytes32 salt = keccak256(abi.encodePacked(token0, token1));
       assembly {
           pair := create2(0, add(bytecode, 32), mload(bytecode), salt)
      }
       IUniswapV2Pair(pair).initialize(token0, token1);
       getPair[token0][token1] = pair;
       getPair[token1][token0] = pair; // populate mapping in the reverse direction
       allPairs.push(pair);
       emit PairCreated(token0, token1, pair, allPairs.length);
  }
```

但是init code本身包含constructor的参数，当构造函数参数不同时，无法在不同的链上部署相同的合约地址。

**03****‍**

**create 3**

曾有EIP-3173提案新增create3字节码，但至今还没有增加此opcode的计划。

create3创建合约只根据调用者地址与salt的决定，即使init code不同也可以部署在同一地址。

### 步骤

1. 假设多条链上已存在Create3 factory合约，并且合约地址相同。
2. 开发者发送交易到create3 factory合约，交易内容包含salt和新合约的 init code。
3. Create3 factory先使用create2部署fixed init code合约，称之为create2 proxy。因为sender address(create3 factory)，salt与写死的init code都相同，所以各链的crea...