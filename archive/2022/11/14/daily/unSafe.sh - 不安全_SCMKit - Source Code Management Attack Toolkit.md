---
title: SCMKit - Source Code Management Attack Toolkit
url: https://buaq.net/go-135419.html
source: unSafe.sh - 不安全
date: 2022-11-14
fetch_date: 2025-10-03T22:39:41.511731
---

# SCMKit - Source Code Management Attack Toolkit

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/fc372c14958ab745397b006ebc0a27f8.jpg)

SCMKit - Source Code Management Attack Toolkit

Source Code Management Attack Toolkit - SCMKit is a toolkit that can be used to attack SCM s
*2022-11-13 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-135419.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSFHzfp_0fwm8HENFxmHuIDfxDmOe-1lAo3YiqDCfxVfzb6JovdYIpJyMKGu03c1J-Yc7ADqT-v2LOMoalLkj7T-IWLlTLzh4puPwy8mlYpWn0SHrlbxzrcKaKu4yc6qIMb7nR6GTksEeO5FUPDQtdQyEMBWp1G7A__EpPOdun1x-dAs20Z162tVTgcg/w640-h418/h37.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSFHzfp_0fwm8HENFxmHuIDfxDmOe-1lAo3YiqDCfxVfzb6JovdYIpJyMKGu03c1J-Yc7ADqT-v2LOMoalLkj7T-IWLlTLzh4puPwy8mlYpWn0SHrlbxzrcKaKu4yc6qIMb7nR6GTksEeO5FUPDQtdQyEMBWp1G7A__EpPOdun1x-dAs20Z162tVTgcg/s486/h37.png)

**S**ource **C**ode **M**anagement Attack Tool**kit** - SCMKit is a toolkit that can be used to attack SCM systems. SCMKit allows the user to specify the SCM system and attack module to use, along with specifying valid credentials (username/password or API key) to the respective SCM system. Currently, the SCM systems that SCMKit supports are GitHub Enterprise, GitLab Enterprise and Bitbucket Server. The attack modules supported include reconnaissance, [privilege escalation](https://www.kitploit.com/search/label/Privilege%20Escalation "privilege escalation") and persistence. SCMKit was built in a modular approach, so that new modules and SCM systems can be added in the future by the information security community.

## Installation/Building

### Libraries Used

The below 3rd party libraries are used in this project.

| Library | URL | License |
| --- | --- | --- |
| Octokit | [https://github.com/octokit/octokit.net](https://github.com/octokit/octokit.net "https://github.com/octokit/octokit.net") | MIT License |
| Fody | [https://github.com/Fody/Fody](https://github.com/Fody/Fody "https://github.com/Fody/Fody") | MIT License |
| GitLabApiClient | [https://github.com/nmklotas/GitLabApiClient](https://github.com/nmklotas/GitLabApiClient "https://github.com/nmklotas/GitLabApiClient") | MIT License |
| Newtonsoft.Json | [https://github.com/JamesNK/Newtonsoft.Json](https://github.com/JamesNK/Newtonsoft.Json "https://github.com/JamesNK/Newtonsoft.Json") | MIT License |

### Pre-Compiled

* Use the pre-compiled binary in Releases

### Building Yourself

Take the below steps to setup Visual Studio in order to compile the project yourself. This requires a .NET library that can be installed from the NuGet package manager.

* Load the Visual Studio project up and go to "Tools" --> "NuGet Package Manager" --> "Package Manager Settings"
* Go to "NuGet Package Manager" --> "Package Sources"
* Add a package source with the URL `https://api.nuget.org/v3/index.json`
* Install the below NuGet packages
  + `Install-Package Costura.Fody -Version 3.3.3`
  + `Install-Package Octokit`
  + `Install-Package GitLabApiClient`
  + `Install-Package Newtonsoft.Json`
* You can now build the project yourself!

## Usage

### Arguments/Options

* **-c, -credential**  - credential for [authentication](https://www.kitploit.com/search/label/Authentication "authentication") (username:password or apiKey)
* **-s, -system**  - system to attack (github,gitlab,bitbucket)
* **-u, -url**  - URL for GitHub Enterprise, GitLab Enterprise or Bitbucket Server
* **-m, -module**  - module to run
* **-o, -option**  - options (when applicable)

### Systems (-s, -system)

* **github:** GitHub Enterprise
* **gitlab:** GitLab Enterprise
* **bitbucket:** Bitbucket Server

### Modules (-m, -module)

* **listrepo:** list all repos the current user can see
* **searchrepo:** search for a given repo
* **searchcode:** search for code containing keyword search term
* **searchfile:** search for filename containing keyword search term
* **listsnippet:** list all snippets of current user
* **listrunner:** list all GitLab runners available to current user
* **listgist:** list all gists of current user
* **listorg:** list all orgs current user belongs to
* **privs:** get privs of current API token
* **addadmin:** promote given user to admin role
* **removeadmin:** demote given user from admin role
* **createpat:** create personal [access token](https://www.kitploit.com/search/label/Access%20Token "access token") for target user
* **listpat:** list personal [access tokens](https://www.kitploit.com/search/label/Access%20Tokens "access tokens") for a target user
* **removepat:** remove personal access token for a target user
* **createsshkey:** create SSH key for current user
* **listsshkey:** list SSH keys for current user
* **removesshkey:** remove SSH key for current user
* **adminstats:** get admin stats (users, repos, orgs, gists)
* **protection:** get branch protection settings

### Module Details Table

The below table shows where each module is supported

| Attack Scenario | Module | Requires Admin? | GitHub Enterprise | GitLab Enterprise | Bitbucket Server |
| --- | --- | --- | --- | --- | --- |
| Reconnaissance | `listrepo` | No | X | X | X |
| Reconnaissance | `searchrepo` | No | X | X | X |
| Reconnaissance | `searchcode` | No | X | X | X |
| Reconnaissance | `searchfile` | No | X | X | X |
| Reconnaissance | `listsnippet` | No |  | X |  |
| Reconnaissance | `listrunner` | No |  | X |  |
| Reconnaissance | `listgist` | No | X |  |  |
| Reconnaissance | `listorg` | No | X |  |  |
| Reconnaissance | `privs` | No | X | X |  |
| Reconnaissance | `protection` | No | X |  |  |
| Persistence | `listsshkey` | No | X | X | X |
| Persistence | `removesshkey` | No | X | X | X |
| Persistence | `createsshkey` | No | X | X | X |
| Persistence | `listpat` | No |  | X | X |
| Persistence | `removepat` | No |  | X | X |
| Persistence | `createpat` | Yes (GitLab Enterprise only) |  | X | X |
| Privilege Escalation | `addadmin` | Yes | X | X | X |
| Privilege Escalation | `removeadmin` | Yes | X | X | X |
| Reconnaissance | `adminstats` | Yes | X |  |  |

## Examples

### List Repos

#### Use Case

> *Discover [repositories](https://www.kitploit.com/search/label/Repositories "repositories") being used in a particular SCM system*

#### Syntax

Provide the `listrepo` module, along with any relevant authentication information and URL. This will output the repository name and URL.

##### GitHub Enterprise

This will list all repositories that a user can see.

`SCMKit.exe -s github -m listrepo -c userName:password -u https://github.something.local`

`SCMKit.exe -s github -m listrepo -c apiKey -u https://github.something.local`

##### GitLab Enterprise

This will list all repositories that a user can see.

`SCMKit.exe -s gitlab -m listrepo -c userName:password -u https://gitlab.something.local`

`SCMKit.exe -s gitlab -m listrepo -c apiKey -u https://gitlab.something.local`

##### Bitbucket Server

This will list all repositories that a user can see.

`SCMKit.exe -s bitbucket -m listrepo -c userName:password -u https://bitbucket.something.local`

`SCMKit.exe -s bitbucket -m listrepo -c apiKey -u https://bitbucket.something.local`

#### Example Output

```

```

### Search Repos

#### Use Case

> *Search for repositories by repository name in a particular SCM system*

#### Syntax

Provide the `searchrepo` module and your search criteria in the `-o` command-line switch, along with any relevant authentication information and URL. This will output the matching repository name and URL.

##### GitHub Enterprise

The GitHub repo search is a "contains" search where the string you enter it will search for repos with names that contain your search term.

`SCMKit.exe -s github -m...