---
title: 以UniswapV2为例模拟DeFi闪电贷
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247497602&idx=1&sn=78ed28824e05917801e650b8997ea014&chksm=fa52223ccd25ab2aa03bbc4465b321a18fd8d36af0cb60792e7afabc5cd31a81cfab4ba888e6&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-11-25
fetch_date: 2025-10-03T23:44:25.956953
---

# 以UniswapV2为例模拟DeFi闪电贷

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRfBBeZOgcOlXJ1icm2ZSOaQgdJiaSJ0H06OPumKCVUuYS5dSfyibdSIY0sfIGUcc7ep7ogyHgszDxbw/0?wx_fmt=jpeg)

# 以UniswapV2为例模拟DeFi闪电贷

原创

核心基础实验室

山石网科安全技术研究院

**0****1**

**简介**

在DEFI领域中的闪电贷指的是无抵押的借贷，它的实现是靠以太坊中交易的原子性特性，是一种新的金融创新。用户可以在一个原子交易中完成借款和还款。它让任何套利行为不再有成本限制，我们以UniswapV2的闪电贷为例，实际操作一下闪电贷。

**0****2**

**源码解析**

UniswapV2闪电贷的逻辑在UniswapV2Pair.sol文件UniswapV2Pair合约的swap函数中：

```
function swap(uint amount0Out, uint amount1Out, address to, bytes calldata data) external lock {
      // 确保至少一个数量大于0
        require(amount0Out > 0 || amount1Out > 0, 'UniswapV2: INSUFFICIENT_OUTPUT_AMOUNT');
        // 获取两种代币的储备量
        (uint112 _reserve0, uint112 _reserve1,) = getReserves(); // gas savings
        // 确保要有足够的余额
        require(amount0Out < _reserve0 && amount1Out < _reserve1, 'UniswapV2: INSUFFICIENT_LIQUIDITY');

        uint balance0;
        uint balance1;
        { // scope for _token{0,1}, avoids stack too deep errors
        address _token0 = token0;
        address _token1 = token1;
        // 发送地址不能为这两个token合约
        require(to != _token0 && to != _token1, 'UniswapV2: INVALID_TO');

        // 发送代币
        if (amount0Out > 0) _safeTransfer(_token0, to, amount0Out); // optimistically transfer tokens
        if (amount1Out > 0) _safeTransfer(_token1, to, amount1Out); // optimistically transfer tokens

        // 如果data有长度，则调用to的接口进行闪电贷
        if (data.length > 0) IUniswapV2Callee(to).uniswapV2Call(msg.sender, amount0Out, amount1Out, data);

        // 获取合约中两种代币的余额
        balance0 = IERC20(_token0).balanceOf(address(this));
        balance1 = IERC20(_token1).balanceOf(address(this));
        }

    // amountIn = balance - (_reserve - amountOut)
        // 根据取出的储备量、原有的储备量及最新的余额，反求出输入的金额
        uint amount0In = balance0 > _reserve0 - amount0Out ? balance0 - (_reserve0 - amount0Out) : 0;
        uint amount1In = balance1 > _reserve1 - amount1Out ? balance1 - (_reserve1 - amount1Out) : 0;
        // 确保输入的金额至少有一个大于0
        require(amount0In > 0 || amount1In > 0, 'UniswapV2: INSUFFICIENT_INPUT_AMOUNT');
        { // scope for reserve{0,1}Adjusted, avoids stack too deep errors

        // 调整后的余额 = （1 - 0.3%）* 原余额
        uint balance0Adjusted = balance0.mul(1000).sub(amount0In.mul(3));
        uint balance1Adjusted = balance1.mul(1000).sub(amount1In.mul(3));

        // 新k值应该大于旧的k值，增加值为手续费
        require(balance0Adjusted.mul(balance1Adjusted) >= uint(_reserve0).mul(_reserve1).mul(1000**2), 'UniswapV2: K');
        }

    // 更新储备量
        _update(balance0, balance1, _reserve0, _reserve1);
        emit Swap(msg.sender, amount0In, amount1In, amount0Out, amount1Out, to);
    }
```

可以发现在swap函数中，pair合约会首先发送给调用者本合约中的两种代币的所有余额:

```
// 发送代币
        if (amount0Out > 0) _safeTransfer(_token0, to, amount0Out); // optimistically transfer tokens
        if (amount1Out > 0) _safeTransfer(_token1, to, amount1Out); // optimistically transfer tokens
```

接着判断了传入参数data的参数，如果该参数的长度大于0则调用调用者的闪电贷接口：

```
if (data.length > 0) IUniswapV2Callee(to).uniswapV2Call(msg.sender, amount0Out, amount1Out, data);
```

这里需要调用者合约实现了IUniswapV2Callee接口中的uniswapV2Call函数:

```
interface IUniswapV2Callee {
    function UniswapV2Call(address sender, uint amount0, uint amount1, bytes calldata data) external;
}
```

接着就会进入到调用者的UniswapV2Call函数，在该函数中完成其他套利逻辑，并发送回相应数量的代币给pair合约。

之后swap函数会判断合约中两种代币的数量是否满足k值，若不满足，则回退整个交易。如果满足，则完成这个闪电贷。

**0****3**

**场景模拟**

现在有3个ERC20代币：USDC、USDT、WETH，并且他们两两之间有一个交易对，一共是3个交易对，这3个交易对中代币的数量为：

USDC-USDT：100000：100000

WETH-USDT：100000：100000000

WETH-USDC：100000：100000000

现在有一个uniswap的用户A，想用900000wei的USDC换USDC。正常情况下USDC和USDT的相对价格应为1:1，并且现在交易对的池子中的两种代币的数量也想等，但是用户A输入进去的USDC数量过大，相比之下交易对池子流动性过浅，导致滑点大幅移动，只能取出9000左右的USDT。

由于USDC-USDC交易对滑点的大幅移动，此时两种代币的数量比值达到10:1，相应的价格也变为10:1，存在套利机会。

套利者从WETH-USDT池子中借出90000wei的USDT，再用得到的90000wei的USDT去USDC-USDT池子中去换USDC，因为在这个池子中usdt的价格是usdc的10倍，所以可以换到900000的USDC。这时再用得到的USDC到WETH-USDC的池子换取WETH，能换出大约900wei的WETH，最后再发送100wei的WETH到WETH-USDT的pair合约，还上闪电贷。最后0成本获取约900wei的WETH。

**04**

**实战**

首先创建3个ERC20代币的合约：

```
contract WETH is ERC20("WETH", "WETH") , Ownable {
    function mint(address _to, uint256 _amount) public onlyOwner {
        _mint(_to, _amount);
    }
}

contract USDT is ERC20("USDT", "USDT") , Ownable{
    function mint(address _to, uint256 _amount) public onlyOwner {
        _mint(_to, _amount);
    }
}

contract USDC is ERC20("USDC", "USDC") , Ownable{
    function mint(address _to, uint256 _amount) public onlyOwner {
        _mint(_to, _amount);
    }
}
```

```
const [owner] = await ethers.getSigners();

  const USDC = await hre.ethers.getContractFactory("USDC");
  const usdc = await USDC.deploy();
  await usdc.deployed();
  await usdc.mint(owner.address, 100000100000);
  console.log(`usdc: ${usdc.address}`);

  const USDT = await hre.ethers.getContractFactory("USDT");
  const usdt = await USDT.deploy();
  await usdt.deployed();
  await usdt.mint(owner.address, 100000100000);
  console.log(`usdt: ${usdt.address}`);

  const WETH = await hre.ethers.getContractFactory("WETH");
  const weth = await WETH.deploy();
  await weth.deployed();
  await weth.mint(owner.address, 20000000);
  console.log(`weth: ${weth.address}`);
```

创建Uniswap工厂合约，并创建交易对并注入相应的流动性：

```
await factory.createPair(weth.address, usdc.address);
  await factory.createPair(weth.address, usdt.address);
  const wethUsdtPair = await factory.callStatic.getPair(weth.address, usdt.address);
  console.log(`wethUsdtPair: ${wethUsdtPair}}`);

  const Router = await hre.ethers.getContractFactory("UniswapV2Router");
  const router = await Router.deploy(factory.address, owner.address, owner.address);
  await router.deployed();
  console.log(`router: ${router.address}`);

  await usdc.approve(router.address, 9999999999999);
  await usdt.approve(router.address, 9999999999999);
  await weth.approve(router.address, 9999999999999);

  await router.addLiquidity(
    usdc.address,
    usdt.address,
    100000,
    100000,
    0,
    0,
    owner.address,
    1768095287
  );

  await router.addLiquidity(
    weth.address,
    usdt.address,
    100000,
    100000000,
    0,
    0,
    owner.address,
    1768095287
  );

  await router.addLiquidity(
    weth.address,
    usdc.address,
    100000,
    100000000,
    0,
    0,
    owner.address,
    1768095287
  );
  console.log(`add liquidity fin`);
```

创建一个合约并使用该合约用900000USDC去池子中换USDT：

```
contract Victim {
    address public owner;
    address public usdc;
    address public usdt;

    constructor(address _usdc, address _usdt) public {
        owner = msg.sender;
        usdc = _usdc;
        usdt = _usdt;
    }

    function exchangeUsdcToUsdt(address _router) public {
        require(msg.sender == owner);
        USDC Usdc = USDC(usdc);
        Usdc.approve(_router,900000);
        address[] memory path = new address[](2);
        path[0] = usdc;
        path[1] = usdt;
        IUniswapV2Router02(_router).swapExactTokensForTokens(
            900000,
            0,
            path,
            address(this),
            block.timestamp + 10000
        );
    }
}
```

```
// Victims have 900000 wei usdc
  const Victim = await hre.ethers.getContractFactory("Victim");
  const victim = await Victim.deploy(usdc.address, usdt.address);
  await victim.deployed();
  console.log(`dev victim fin : ${victim.address}`);

  await usdc.mint(victim.address, 900000);

  // Victims want to exchang usdc to usdt
  await victim.exchangeUsdcToUsdt(router.address);
  console.log(`victim fin `);
```

现在出现了套利机会，我们再创建套利机器人合约并进行套利:

```
contract Bot {

    address public owner;
    address public usdc;
    address public usdt;
    address public weth;
    address public wethUsdtPair;
    address public router;

    constructor(address _usdc, address _usdt, address _weth, address _router) public {
        owner = msg.sender;
        usdc = _usdc;
        usdt = _usdt;
        weth = _weth;
        router = _router;
    }

    function attack(address _pair) public {
        require(msg.sender == owner);
    ...