---
title: phpstan v2.2.9
url: https://kitploit.com/en/posts/github-phpstan-phpstan-229
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:08.197559
---

# phpstan v2.2.9

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2759/7d0b13c555436928d3eedaf3459dfc17355e5f1aed654b3f07fb34d971435db9.png)

New releaseAug 22, 2026

# phpstan v2.2.9

PHP Static Analysis Tool - discover bugs in your code without running it!

Share

# PHPStan - PHP Static Analysis Tool

![PHPStan](https://assets.kitploit.com/production/public/readmes/2759/c0a3c14f704bdfeb8be2a59b7f9893b5a6da9fe192960f7078342e0ce841ab83.png)

[![Build Status](https://github.com/phpstan/phpstan/workflows/Tests/badge.svg)](https://github.com/phpstan/phpstan/actions)
[![Latest Stable Version](https://poser.pugx.org/phpstan/phpstan/v/stable)](https://packagist.org/packages/phpstan/phpstan)
[![Total Downloads](https://poser.pugx.org/phpstan/phpstan/downloads)](https://packagist.org/packages/phpstan/phpstan/stats)
[![License](https://poser.pugx.org/phpstan/phpstan/license)](https://choosealicense.com/licenses/mit/)
[![PHPStan Enabled](https://img.shields.io/badge/PHPStan-enabled-brightgreen.svg?style=flat)](https://phpstan.org/)

---

PHPStan focuses on finding errors in your code without actually running it. It catches whole classes of bugs
even before you write tests for the code. It moves PHP closer to compiled languages in the sense that the correctness of each line of the code
can be checked before you run the actual line.

**[Read more about PHPStan »](https://phpstan.org/)**

**[Try out PHPStan on the on-line playground! »](https://phpstan.org/try)**

## Sponsors

Want your logo here? [Learn more »](https://phpstan.org/sponsor)

### Gold Sponsors

[![Matt Mullenweg](https://assets.kitploit.com/production/public/readmes/2759/a2e91000c4f6277f8d3e1219b66f930e0ef84c59cc21600ed8303348049ce0e7.png)](https://ma.tt/)

[![Mojam](https://assets.kitploit.com/production/public/readmes/2759/bf753e36570a1c1ae49c1d95efb9962d5fd101037e3ef495c928b5da4881f4ff.png)](https://mojam.co/)

[![CHECK24](https://assets.kitploit.com/production/public/readmes/2759/6d8934bad47bab395ccf8a5fa4e864e0edab8a9ca0df11230af1372b3d889a64.png)](https://www.check24.de/)

### Silver Sponsors

[![ShipMonk](https://assets.kitploit.com/production/public/readmes/2759/013ba2e7642ee9fb72b8df9e44fc5ebbf92423d55640eaa52d3fa8bdf2797df1.jpg)](https://www.startupjobs.cz/startup/shipmonk)
[![Shopware](https://assets.kitploit.com/production/public/readmes/2759/647dd764fe0a68709e98a0cdc9a7cbfe6294350690353ec97f78d13c100209fd.png)](https://www.shopware.com/en/)

### Bronze Sponsors

[![TheCodingMachine](https://assets.kitploit.com/production/public/readmes/2759/e19034fff2a59cec90d98774061513e5f49bf39d095368bfcf5d1e98c621c3fb.png)](https://coders.thecodingmachine.com/phpstan)

[![Private Packagist](https://assets.kitploit.com/production/public/readmes/2759/1ac2e0f30bb5851654864b0d2bb3b1c49a1d42e6f8349860bcdc901301c6293e.png)](https://packagist.com/?utm_source=phpstan&utm_medium=readme&utm_campaign=sponsorlogo)

[![CDN77](https://assets.kitploit.com/production/public/readmes/2759/e104ae0a1d13869f2839f73056d38bc5fc65ffdfc8290e1202f0c6000b3173b2.png)](https://www.cdn77.com/)

[![Blackfire.io](https://assets.kitploit.com/production/public/readmes/2759/a2dad75ddd57ef70f983770de442e40221e2d2e038415df19dc118dd971ab53d.png)](https://blackfire.io/docs/introduction?utm_source=phpstan&utm_medium=github_readme&utm_campaign=logo)

[![iO](https://assets.kitploit.com/production/public/readmes/2759/8b4d38e2fef9f229b998ce0d42c84c01769cde1e86bf78fefe40a34330c4f236.png)](https://www.iodigital.com/)

[![Fame Helsinki](https://assets.kitploit.com/production/public/readmes/2759/012132f964bd64c0c1e3c6f890e47211493872cf82e69876f518d01d199b1cde.png)](https://www.fame.fi/)

[![Belsimpel](https://assets.kitploit.com/production/public/readmes/2759/abd3bda35e58d35ee514ae6d5a58725af2b3baab229358c8f3b70f362b4b1fd7.png)](https://werkenbijbelsimpel.nl/en/about-us/)

[![Togetter](https://assets.kitploit.com/production/public/readmes/2759/e3fef308129df00d1d84d4acb82c733567e3e004c8b44e8838d87679f7bc389a.png)](https://togetter.com/)

[![RightCapital](https://assets.kitploit.com/production/public/readmes/2759/10d0c7275a4c45d0ce6f23ec940112d53bf8306a022e5480dc28d902dda98006.png)](https://join.rightcapital.com/?utm_source=phpstan&utm_medium=github&utm_campaign=sponsorship)

[![Shoptet](https://assets.kitploit.com/production/public/readmes/2759/4d1303101a5f0ef61b6eb4b2fec1947a773024496285621ed991450ef04b500c.png)](https://www.shoptet.cz/)

[![ZOL](https://assets.kitploit.com/production/public/readmes/2759/d5bc0beedc9731cfa0a81b2cfbbd2dc1bf301da12a93740e1275b8c1821739dc.png)](https://zol.fr?utm_source=phpstan)

[![Inviqa](https://assets.kitploit.com/production/public/readmes/2759/3939b8b54da5de17eeb2338f429525da802cf28a9b03dddd781b86199962e032.png)](https://inviqa.com/)

[![Route4Me: Route Optimizer and Route Planner Software](https://assets.kitploit.com/production/public/readmes/2759/6fc0d02e8a1641530f874b5183dbc0b0c16242db1ad9a665187ecbd1d36c7aaa.png)](https://route4me.com/)

[![Crisp.nl](https://assets.kitploit.com/production/public/readmes/2759/aa0f102f6c241da30d3776a127d4ad6ad86c65d2f485440208da3e095eb8c0a0.png)](https://www.crisp.nl/)

[![TicketSwap](https://assets.kitploit.com/production/public/readmes/2759/2965a223174df74370153a2682d32b4b894659e3603287247cef03bce10890b8.png)](https://jobs.ticketswap.com/)

[![campoint AG](https://assets.kitploit.com/production/public/readmes/2759/10bea4ef197db27023a26c7a06a48394c4cc6bb72d9dc3a8eeecd8bf147c0bad.png)](https://www.campoint.net/)

[![TestMu AI](https://assets.kitploit.com/production/public/readmes/2759/97304a93d4ae244dc841440ca84a909dbf79a53e9f305c7011d9957887b0154e.png)](https://www.testmuai.com/)

[**You can sponsor my open-source work on PHPStan through GitHub Sponsors and also directly.**](https://phpstan.org/sponsor)

One-time donations [through Revolut.me](https://revolut.me/ondrejmirtes) are also accepted. To request an invoice, [contact me](/cdn-cgi/l/email-protection#513e3f3523343b113c38232534227f322b) through e-mail.

## Documentation

All the documentation lives on the [phpstan.org website](https://phpstan.org/):

* [Getting Started & User Guide](https://phpstan.org/user-guide/getting-started)
* [Config Reference](https://phpstan.org/config-reference)
* [PHPDocs Basics](https://phpstan.org/writing-php-code/phpdocs-basics) & [PHPDoc Types](https://phpstan.org/writing-php-code/phpdoc-types)
* [Extension Library](https://phpstan.org/user-guide/extension-library)
* [Developing Extensions](https://phpstan.org/developing-extensions/extension-types)
* [API Reference](https://apiref.phpstan.org/)

## PHPStan Pro

PHPStan Pro is a paid add-on on top of open-source PHPStan Static Analysis Tool with these premium features:

* Web UI for browsing found errors, you can click and open your editor of choice on the offending line.
* Continuous analysis (watch mode): scans changed files in the background, refreshes the UI automatically.

Try it on PHPStan 0.12.45 or later by running it with the `--pro` option. You can create an account either by following the on-screen instructions, or by visiting [account.phpstan.com](https://account.phpstan.com/).

After 30-day free trial period it costs 7 EUR for individuals monthly, 70 EUR for teams (up to 25 members). By paying for PHPStan Pro, you're supporting the development of open-source PHPStan.

You can read more about it on [PHPStan's website](https://phpstan.org/blog/introducing-phpstan-pro).

## Code of Conduct

This project adheres to a [Contributor Code of Conduct](https://github.com/phpstan/phpstan/blob/master/CODE_OF_CONDUCT.md). By participating in this project and its community, you are expected to uphold this cod...