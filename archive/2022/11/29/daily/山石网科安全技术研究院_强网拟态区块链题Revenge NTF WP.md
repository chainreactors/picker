---
title: 强网拟态区块链题Revenge NTF WP
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247497614&idx=1&sn=63926ef47c34db6d7ec3fd7db3102a98&chksm=fa522230cd25ab261496e078a45710eaf0309df82463dc1b80bcd20277f744cc2762840c07d8&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-11-29
fetch_date: 2025-10-03T23:59:47.255379
---

# 强网拟态区块链题Revenge NTF WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTVNnT3oj2kiauAqj68VVVncfWypR3DbUmXpvf2ZqGvic9icpnRlllfbfKAzYwQBS1nibjqlo5bIibNpFA/0?wx_fmt=jpeg)

# 强网拟态区块链题Revenge NTF WP

原创

核心基础实验室

山石网科安全技术研究院

第五届“强网”拟态防御国际精英挑战赛

线上预选赛区块链题

**一、源码**

```
pragma solidity 0.8.16;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CtfNFT is ERC721, Ownable {
    constructor() ERC721("CtfNFT", "NFT") {
        _setApprovalForAll(address(this), msg.sender, true);
    }

    function mint(address to, uint256 tokenId) external onlyOwner {
        _mint(to, tokenId);
    }
}

contract CtfToken is ERC20 {
    bool airdropped;

    constructor() ERC20("CtfToken", "CTK") {
        _mint(address(this), 100000000000);
        _mint(msg.sender, 1337);
    }

    function airdrop() external {
        require(!airdropped, "Already airdropped");
        airdropped = true;
        _mint(msg.sender, 5);
    }
}

struct Order {
    address nftAddress;
    uint256 tokenId;
    uint256 price;
}
struct Coupon {
    uint256 orderId;
    uint256 newprice;
    address issuer;
    address user;
    bytes reason;
}
struct Signature {
    uint8 v;
    bytes32[2] rs;
}
struct SignedCoupon {
    Coupon coupon;
    Signature signature;
}

contract CtfMarket {
    event SendFlag();
    event NFTListed(
        address indexed seller,
        address indexed nftAddress,
        uint256 indexed tokenId,
        uint256 price
    );

    event NFTCanceled(
        address indexed seller,
        address indexed nftAddress,
        uint256 indexed tokenId
    );

    event NFTBought(
        address indexed buyer,
        address indexed nftAddress,
        uint256 indexed tokenId,
        uint256 price
    );

    bool tested;
    CtfNFT public ctfNFT;
    CtfToken public ctfToken;
    CouponVerifierBeta public verifier;
    Order[] orders;

    constructor() {
        ctfToken = new CtfToken();
        ctfToken.approve(address(this), type(uint256).max);

        ctfNFT = new CtfNFT();
        ctfNFT.mint(address(ctfNFT), 1);
        ctfNFT.mint(address(this), 2);
        ctfNFT.mint(address(this), 3);

        verifier = new CouponVerifierBeta();

        orders.push(Order(address(ctfNFT), 1, 1));
        orders.push(Order(address(ctfNFT), 2, 1337));
        orders.push(Order(address(ctfNFT), 3, 13333333337));
    }

    function getOrder(uint256 orderId) public view returns (Order memory order) {
        require(orderId < orders.length, "Invalid orderId");
        order = orders[orderId];
    }

    function createOrder(address nftAddress, uint256 tokenId, uint256 price) external returns(uint256) {
        require(price > 0, "Invalid price");
        require(isNFTApprovedOrOwner(nftAddress, msg.sender, tokenId), "Not owner");
        orders.push(Order(nftAddress, tokenId, price));
        emit NFTListed(msg.sender, nftAddress, tokenId, price);
        return orders.length - 1;
    }

    function cancelOrder(uint256 orderId) external {
        Order memory order = getOrder(orderId);
        require(isNFTApprovedOrOwner(order.nftAddress, msg.sender, order.tokenId), "Not owner");
        _deleteOrder(orderId);
        emit NFTCanceled(msg.sender, order.nftAddress, order.tokenId);
    }

    function purchaseOrder(uint256 orderId) external {
        Order memory order = getOrder(orderId);
        _deleteOrder(orderId);
        IERC721 nft = IERC721(order.nftAddress);
        address owner = nft.ownerOf(order.tokenId);
        ctfToken.transferFrom(msg.sender, owner, order.price);
        nft.safeTransferFrom(owner, msg.sender, order.tokenId);
        emit NFTBought(msg.sender, order.nftAddress, order.tokenId, order.price);
    }

    function purchaseWithCoupon(SignedCoupon calldata scoupon) external {
        Coupon memory coupon = scoupon.coupon;
        require(coupon.user == msg.sender, "Invalid user");
        require(coupon.newprice > 0, "Invalid price");
        verifier.verifyCoupon(scoupon);
        Order memory order = getOrder(coupon.orderId);//(address=fakeNFT, id=3, price=1) orderID = 0
        uint price = order.price; // price=1
        _deleteOrder(coupon.orderId); // del 0
        IERC721 nft = IERC721(order.nftAddress); // fakeNFT address
        address owner = nft.ownerOf(order.tokenId);// fakeNFT fake ownerOf market
        ctfToken.transferFrom(coupon.user, owner, price);// msg.sender market 1
        IERC721(getOrder(coupon.orderId).nftAddress).safeTransferFrom(owner, coupon.user, order.tokenId);
        _deleteOrder(coupon.orderId);
        emit NFTBought(coupon.user, order.nftAddress, order.tokenId, coupon.newprice);
    }

    function purchaseTest(address nftAddress, uint256 tokenId, uint256 price) external {
        require(!tested, "Tested");
        tested = true;
        IERC721 nft = IERC721(nftAddress);
        uint256 orderId = CtfMarket(this).createOrder(nftAddress, tokenId, price);
        nft.approve(address(this), tokenId);
        CtfMarket(this).purchaseOrder(orderId);
    }

    function win() external {
        require(ctfNFT.ownerOf(1) == msg.sender && ctfNFT.ownerOf(2) == msg.sender && ctfNFT.ownerOf(3) == msg.sender);
        emit SendFlag();
    }

    function isNFTApprovedOrOwner(address nftAddress, address spender, uint256 tokenId) internal view returns (bool) {
        IERC721 nft = IERC721(nftAddress);
        address owner = nft.ownerOf(tokenId);
        return (spender == owner || nft.isApprovedForAll(owner, spender) || nft.getApproved(tokenId) == spender);
    }

    function _deleteOrder(uint256 orderId) internal {
        orders[orderId] = orders[orders.length - 1];
        orders.pop();
    }

    function onERC721Received(address, address, uint256, bytes memory) public pure returns (bytes4) {
        return this.onERC721Received.selector;
    }
}

contract CouponVerifierBeta {
    CtfMarket market;
    bool tested;

    constructor() {
        market = CtfMarket(msg.sender);
    }

    function verifyCoupon(SignedCoupon calldata scoupon) public {
        require(!tested, "Tested");
        tested = true;
        Coupon memory coupon = scoupon.coupon;
        Signature memory sig = scoupon.signature;
        Order memory order = market.getOrder(coupon.orderId);
        bytes memory serialized = abi.encode(
            "I, the issuer", coupon.issuer,
            "offer a special discount for", coupon.user,
            "to buy", order, "at", coupon.newprice,
            "because", coupon.reason
        );
        IERC721 nft = IERC721(order.nftAddress);
        address owner = nft.ownerOf(order.tokenId);
        require(coupon.issuer == owner, "Invalid issuer");
        require(ecrecover(keccak256(serialized), sig.v, sig.rs[0], sig.rs[1]) == coupon.issuer, "Invalid signature");
    }
}
```

**二、分析**

首先查看获取flag的条件：

```
function win() external {
        require(ctfNFT.ownerOf(1) == msg.sender && ctfNFT.ownerOf(2) == msg.sender && ctfNFT.ownerOf(3) == msg.sender);
        emit SendFlag();
    }
```

调用者需要获取这3个nft。

这3个nft在market合约中被mint:

```
constructor() {
        ctfToken = new CtfToken();
        ctfToken.approve(address(this), type(uint256).max);

        ctfNFT = new CtfNFT();
        ctfNFT.mint(address(ctfNFT), 1);
        ctfNFT.mint(address(this), 2);
        ctfNFT.mint(address(this), 3);

        verifier = new CouponVerifierBeta();

        orders.push(Order(address(ctfNFT), 1, 1));
        orders.push(Order(address(ctfNFT), 2, 1337));
        orders.push(Order(address(ctfNFT), 3, 13333333337));
    }
```

1号mint给了NFT合约，价格为1wei，2号和3号mint给market合约。orders为一个订单列表，里面增加了3个订单，分别给3个NFT定价1，1337，13333333337wei，支付使用的ERC20token为CtfToken：

```
contract CtfToken is ERC20 {
    bool airdropped;

    constructor() ERC20("CtfToken", "CTK") {
        _mint(address(this), 100000000000);
        _mint(msg.sender, 1337);
    }

    function airdrop() external {
        require(!airdropped, "Already airdropped");
    ...