---
title: introducing curl command line variables
url: https://daniel.haxx.se/blog/2023/07/31/introducing-curl-command-line-variables/
source: daniel.haxx.se
date: 2023-08-01
fetch_date: 2025-10-06T17:00:43.455041
---

# introducing curl command line variables

[Skip to content](#content)

[![daniel.haxx.se](https://daniel.haxx.se/blog/wp-content/uploads/2024/11/Daniel-blog-header-colonslash-thin.jpg)](https://daniel.haxx.se/blog/)

# [daniel.haxx.se](https://daniel.haxx.se/blog/)

[Search](#search-container)

Primary Menu

* [About](https://daniel.haxx.se/blog/about/)
* [Privacy](https://daniel.haxx.se/blog/privacy-policy/)

Search for:

![](https://daniel.haxx.se/blog/wp-content/uploads/2019/04/tools-1209764_1280-672x372.jpg)

[cURL and libcurl](https://daniel.haxx.se/blog/category/floss/curl/)

# introducing curl command line variables

[July 31, 2023](https://daniel.haxx.se/blog/2023/07/31/introducing-curl-command-line-variables/) [Daniel Stenberg](https://daniel.haxx.se/blog/author/daniel/) [1 Comment](https://daniel.haxx.se/blog/2023/07/31/introducing-curl-command-line-variables/#comments)

If you are anything like me, you appreciate solving your every day simple tasks directly from the command line. Creating crafty single shot command lines or a small shell script to solve that special task you figured out you needed and makes your day go a little smoother. A fellow *command line cowboy*.

## Video presentation

## Background

To make life easier for curl users, the tool supports “[config files](https://everything.curl.dev/cmdline/configfile)“. They are a set of command line options written in a text file that you can point the curl tool to use. By default curl will check for and use such a config file named `.curlrc` if placed in your home directory.

One day not too long ago, a user over in [the curl IRC channel](https://curl.se/docs/irc.html) asked me if it was possible to use environment variables in such config files to avoid having to actually store secrets directly in the file.

## Variables

This new variable system that we introduce in **curl 8.3.0** (commit [2e160c9c65](https://github.com/curl/curl/commit/2e160c9c652504e147f474ed920ae891481e299c)) makes it possible to use environment variable in config files. But it does not stop there. It allows lots of other fun things.

First off, you can *set* named variables on the command line. Like :

```
curl --variable name=content
```

or in the config file:

```
variable=name=content
```

A variable name must only consist of a-z, A-Z, 0-9 or underscore (up to 128 characters). If you set the same name twice, the second set will overwrite the first.

There can be an unlimited amount of variables. A variable can hold up to 10M of content. Variables are set in a left to right order as curl parses the command line or config file.

## Assign

You can assign a variable a plain fixed string as shown above. Optionally, you can tell curl to populate it with the contents of a file:

```
curl --variable name@filename
```

or straight from stdin:

```
curl --variable name@-
```

## Environment variables

The variables mentioned above are only present in the curl command line. You can also opt to “import” an environment variable into this context. To import $HOME:

```
curl --variable %HOME
```

In this case above, curl will exit if there is no environment variable by that name. Optionally, you can set a default value for the case where the variable does not exist:

```
curl --variable %HOME=/home/nouser
```

## Expand variables

All variables that are set or “imported” as described above can be used in subsequent command line option arguments – or in config files.

Variables must be explicitly asked for, to make sure they do not cause problems for older command lines or for users when they are not desired. To accomplish this, we introduce the `--expand-` option prefix.

Only when you use the `--expand-` prefix in front of an option will the argument get variables expanded.

You reference (expand) a variable like `{{name}}`. That means two open braces, the variable name and then two closing braces. This sequence will then be replaced by the contents of the variable and a non-existing variable will expand as blank/nothing.

**Trying to show a variable with a null byte causes error**

## Examples

Use the variable named ‘content’ in the argument to `--data`, telling curl what to send in a HTTP POST:

```
--expand-data “{{content}}”
```

Create the URL to operate on by inserting the variables ‘host’ and ‘user’.

```
--expand-url “https://{{host}}/user/{{user}}”
```

## Expand variables

`--variable` itself can be expanded when you want to create a new variable that uses content from one or more other variables. Like:

```
--expand-variable var1={{var2}}
--expand-variable fullname=’Mrs {{first}} {{last}}’
--expand-variable source@{{filename}}
```

## Expansion functions

When expanding a variable, functions can be applied. Like this: `{{name:function}}`

Such variable functions alter how the variable is expanded. How it gets output.

Multiple functions can be applied in a left-to-right order:
`{{name:func1:func2:func3}}`.

curl offers four different *functions* to help you expand variables in the most productive way: trim, json, url and b64:

* **trim** – removes leading and trailing whitespace
* **json** – outputs the variable JSON quoted (but without surrounding quotes)
* **url** – shows the string URL encoded, also sometimes called percent encoding
* **b64** – shows the variable base64 encoded

## Function examples

Expands the variable URL encoded. Also known as “percent encoded”.

```
--expand-data “name={{name:url}}”
```

To trim the variable first, apply both functions (in the right order):

```
--expand-data “name={{name:trim:url}}”
```

Send the HOME environment variable as part of a JSON object in a HTTP POST:

```
--variable %HOME
--expand-data “{ \"homedir\": \"{{HOME:json}}\” "
```

## Discuss

On [hacker news](https://news.ycombinator.com/item?id=36940525).

[command-line](https://daniel.haxx.se/blog/tag/command-line/)[cURL and libcurl](https://daniel.haxx.se/blog/tag/curl-and-libcurl/)

# Post navigation

[Previous Postcurl 8.2.1](https://daniel.haxx.se/blog/2023/07/26/curl-8-2-1/)[Next Postcurl write-out to files](https://daniel.haxx.se/blog/2023/08/01/curl-write-out-to-files/)

## One thought on “introducing curl command line variables”

1. ![](https://secure.gravatar.com/avatar/9e92907dad427f103165d71e628010f3617a2d26eb0cb91e3c0b82312102c1e2?s=34&d=monsterid&r=g) **[Amin](http://okta.com)** says:

   [August 7, 2023 at 01:51](https://daniel.haxx.se/blog/2023/07/31/introducing-curl-command-line-variables/#comment-26730)

   Nice feature. thanks for sharing.

Comments are closed.

# Recent Posts

* [How I maintain release notes for curl](https://daniel.haxx.se/blog/2025/10/01/how-i-maintain-release-notes-for-curl/)
  October 1, 2025
* [CRA compliant curl](https://daniel.haxx.se/blog/2025/09/22/cra-compliant-curl/)
  September 22, 2025
* [Bye bye Kerberos FTP](https://daniel.haxx.se/blog/2025/09/19/bye-bye-kerberos-ftp/)
  September 19, 2025
* [From suspicion to published curl CVE](https://daniel.haxx.se/blog/2025/09/18/from-suspicion-to-published-curl-cve/)
  September 18, 2025
* [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/)
  September 13, 2025
* [curl 8.16.0](https://daniel.haxx.se/blog/2025/09/10/curl-8-16-0/)
  September 10, 2025

# Recent Comments

* F.Nagy on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27323)
* Fredrik on [Developer of the year](https://daniel.haxx.se/blog/2025/09/13/developer-of-the-year/comment-page-1/#comment-27322)
* [Fazal Majid](https://majid.info/) on [preparing for the worst](https://daniel.haxx.se/blog/2025/09/09/preparing-for-the-worst/comment-page-1/#comment-27321)
* Nikhil on [About](https://daniel.haxx.se/blog/about/comment-page-1/#comment-27320)
* A. Ros on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-curl/comment-page-1/#comment-27318)
* [Daniel Stenberg](https://daniel.haxx.se/) on [car brands running curl](https://daniel.haxx.se/blog/2025/08/15/car-brands-running-c...