---
title: Level up your Solidity LLM tooling with Slither-MCP
url: https://blog.trailofbits.com/2025/11/15/level-up-your-solidity-llm-tooling-with-slither-mcp/
source: The Trail of Bits Blog
date: 2025-11-15
fetch_date: 2025-11-16T03:18:43.908946
---

# Level up your Solidity LLM tooling with Slither-MCP

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Level up your Solidity LLM tooling with Slither-MCP

[Benjamin Samuels](https://x.com/thebensams)

November 15, 2025

[blockchain](/categories/blockchain/), [mcp](/categories/mcp/), [slither](/categories/slither/), [tool-release](/categories/tool-release/)

Page content

* [How Slither-MCP works](#how-slither-mcp-works)
  + [Example: Simplifying an auditing task](#example-simplifying-an-auditing-task)
* [Simple setup](#simple-setup)
* [Licensing](#licensing)

We’re releasing [Slither-MCP](https://github.com/trailofbits/slither-mcp), a new tool that augments LLMs with Slither’s unmatched static analysis engine. Slither-MCP benefits virtually every use case for LLMs by exposing Slither’s static analysis API via tools, allowing LLMs to find critical code faster, navigate codebases more efficiently, and ultimately improve smart contract authoring and auditing performance.

## How Slither-MCP works

Slither-MCP is an MCP server that wraps Slither’s static analysis functionality, making it accessible through the Model Context Protocol. It can analyze Solidity projects (Foundry, Hardhat, etc.) and generate comprehensive metadata about contracts, functions, inheritance hierarchies, and more.

When an LLM uses Slither-MCP, it no longer has to rely on rudimentary tools like grep and `read_file` to identify where certain functions are implemented, who a function’s callers are, and other complex, error-prone tasks.

Because LLMs are probabilistic systems, in most cases they are only probabilistically correct. Slither-MCP helps set a ground truth for LLM-based analysis using traditional static analysis: it reduces token use and increases the probability a prompt is answered correctly.

### Example: Simplifying an auditing task

Consider a project that contains two ERC20 contracts: one used in the production deployment, and one used in tests. An LLM is tasked with auditing a contract’s use of `ERC20.transfer()`, and needs to locate the source code of the function.

Without Slither-MCP, the LLM has two options:

1. Try to resolve the import path of the ERC20 contract, then try to call `read_file` to view the source of `ERC20.transfer()`. This option usually requires multiple calls to `read_file`, especially if the call to `ERC20.transfer()` is through a child contract that is inherited from ERC20. Regardless, this option will be error-prone and tool call intensive.
2. Try to use the grep tool to locate the implementation of `ERC20.transfer()`. Depending on how the grep tool call is structured, it may return the wrong ERC20 contract.

Both options are non-ideal, error-prone, and not likely to be correct with a high interval of confidence.

Using Slither-MCP, the LLM simply calls `get_function_source` to locate the source code of the function.

## Simple setup

Slither-MCP is easy to set up, and can be added to Claude Code using the following command:

```
claude mcp add --transport stdio slither -- uvx --from git+https://github.com/trailofbits/slither-mcp slither-mcp
```

It is also easy to add Slither-MCP to Cursor by adding the following to your `~/.cursor/mcp.json`:

```
{
  "mcpServers": {
    "slither-mcp": {
      "command": "uvx --from git+https://github.com/trailofbits/slither-mcp slither-mcp",
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

Figure 1: Adding Slither-MCP to Cursor

For now, Slither-MCP exposes a subset of Slither’s analysis engine that we believe LLMs would have the most benefit consuming. This includes the following functionalities:

* Extracting the source code of a given contract or function for analysis
* Identifying the callers and callees of a function
* Identifying the contract’s derived and inherited members
* Locating potential implementations of a function based on signature (e.g., finding concrete definitions for `IOracle.price(...)`)
* Running Slither’s exhaustive suite of detectors and filtering the results

If you have requests or suggestions for new MCP tools, [we’d love to hear from you](https://github.com/trailofbits/slither-mcp/issues).

## Licensing

Slither-MCP is licensed AGPLv3, the same license Slither uses. This license requires publishing the full source code of your application if you use it in a web service or SaaS product. For many tools, this isn’t an acceptable compromise.

To help remediate this, we are now offering dual licensing for both Slither and Slither-MCP. By offering dual licensing, Slither and Slither-MCP can be used to power LLM-based security web apps without publishing your entire source code, and without having to spend years reproducing its feature set.

If you are currently using Slither in your commercial web application, or are interested in using it, please [reach out](https://www.trailofbits.com/contact/).

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

#### Page content

* [How Slither-MCP works](#how-slither-mcp-works)
  + [Example: Simplifying an auditing task](#example-simplifying-an-auditing-task)
* [Simple setup](#simple-setup)
* [Licensing](#licensing)

#### Recent Posts

* [Level up your Solidity LLM tooling with Slither-MCP](/2025/11/15/level-up-your-solidity-llm-tooling-with-slither-mcp/)
* [How we avoided side-channels in our new post-quantum Go cryptography libraries](/2025/11/14/how-we-avoided-side-channels-in-our-new-post-quantum-go-cryptography-libraries/)
* [Building checksec without boundaries with Checksec Anywhere](/2025/11/13/building-checksec-without-boundaries-with-checksec-anywhere/)
* [Balancer hack analysis and guidance for the DeFi ecosystem](/2025/11/07/balancer-hack-analysis-and-guidance-for-the-defi-ecosystem/)
* [The cryptography behind electronic passports](/2025/10/31/the-cryptography-behind-electronic-passports/)

© 2025 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Mainroad](https://github.com/Vimux/Mainroad/) theme.