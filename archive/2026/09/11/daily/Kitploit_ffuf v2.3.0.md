---
title: ffuf v2.3.0
url: https://kitploit.com/en/posts/github-ffuf-ffuf-v230
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:19.350602
---

# ffuf v2.3.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/365/fcab41490fbb82d9b84cbd4e2acf93da6aec22710001d8dc7b0c46cf7d5de5c2.png)

New releaseSep 11, 2026

# ffuf v2.3.0

Fast web fuzzer written in Go

Share

![ffuf mascot](https://assets.kitploit.com/production/public/readmes/365/fcab41490fbb82d9b84cbd4e2acf93da6aec22710001d8dc7b0c46cf7d5de5c2.png)

# ffuf - Fuzz Faster U Fool

A fast web fuzzer written in Go.

* [Installation](https://github.com/ffuf/ffuf#installation)
* [Example usage](https://github.com/ffuf/ffuf#example-usage)
  + [Content discovery](https://github.com/ffuf/ffuf#typical-directory-discovery)
  + [Vhost discovery](https://github.com/ffuf/ffuf#virtual-host-discovery-without-dns-records)
  + [Parameter fuzzing](https://github.com/ffuf/ffuf#get-parameter-fuzzing)
  + [POST data fuzzing](https://github.com/ffuf/ffuf#post-data-fuzzing)
  + [Using external mutator](https://github.com/ffuf/ffuf#using-external-mutator-to-produce-test-cases)
  + [Configuration files](https://github.com/ffuf/ffuf#configuration-files)
* [Help](https://github.com/ffuf/ffuf#usage)
  + [Interactive mode](https://github.com/ffuf/ffuf#interactive-mode)

## Installation

* [Download](https://github.com/ffuf/ffuf/releases/latest) a prebuilt binary from [releases page](https://github.com/ffuf/ffuf/releases/latest), unpack and run!

  *or*
* If you are on Windows with [Scoop](https://scoop.sh/), ffuf can be installed with: `scoop install ffuf`

  *or*
* If you are on Windows with [Winget](https://learn.microsoft.com/en-us/windows/package-manager/), ffuf can be installed with: `winget install ffuf.ffuf`

  *or*
* If you are on macOS with [homebrew](https://brew.sh), ffuf can be installed with: `brew install ffuf`

  *or*
* If you have recent go compiler installed: `go install github.com/ffuf/ffuf/v2@latest` (the same command works for updating)

  *or*
* `git clone https://github.com/ffuf/ffuf ; cd ffuf ; go get ; go build`

1. Ffuf depends on Go 1.20 or greater.
2. A go build from a checkout shows `git-<date>-<commit>` rather than the tag. A local build isn't an official release even when you're sitting on a tag, and Go's embedded build info gives us the commit but not the tag name — so we surface the exact commit it was built from. The authoritative versioned binaries are the ones on the releases page.

## Example usage

The usage examples below show just the simplest tasks you can accomplish using `ffuf`.

More elaborate documentation that goes through many features with a lot of examples is
available in the ffuf wiki at <https://github.com/ffuf/ffuf/wiki>

For more extensive documentation, with real life usage examples and tips, be sure to check out the awesome guide:
"[Everything you need to know about FFUF](https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html)" by
Michael Skelton ([@codingo](https://github.com/codingo)).

You can also practise your ffuf scans against a live host with different lessons and use cases either locally by using the docker container <https://github.com/adamtlangley/ffufme> or against the live hosted version at <http://ffuf.me> created by Adam Langley [@adamtlangley](https://twitter.com/adamtlangley).

### Typical directory discovery

[![asciicast](https://assets.kitploit.com/production/public/readmes/365/1c862d1e97978c8b504da2cab34e5b812cb81c981ce3e65ffe31da1ae7212bef.png)](https://asciinema.org/a/211350)

By using the FUZZ keyword at the end of URL (`-u`):

root@kitploit:~

```
ffuf -w /path/to/wordlist -u https://target/FUZZ
```

### Virtual host discovery (without DNS records)

[![asciicast](https://assets.kitploit.com/production/public/readmes/365/7159f08726e2144eedf1a4cfb5fc950064008842011b64fd7a949b91aba561f8.png)](https://asciinema.org/a/211360)

Assuming that the default virtualhost response size is 4242 bytes, we can filter out all the responses of that size (`-fs 4242`)while fuzzing the Host - header:

root@kitploit:~

```
ffuf -w /path/to/vhost/wordlist -u https://target -H "Host: FUZZ" -fs 4242
```

### GET parameter fuzzing

GET parameter name fuzzing is very similar to directory discovery, and works by defining the `FUZZ` keyword as a part of the URL. This also assumes a response size of 4242 bytes for invalid GET parameter name.

root@kitploit:~

```
ffuf -w /path/to/paramnames.txt -u https://target/script.php?FUZZ=test_value -fs 4242
```

If the parameter name is known, the values can be fuzzed the same way. This example assumes a wrong parameter value returning HTTP response code 401.

root@kitploit:~

```
ffuf -w /path/to/values.txt -u https://target/script.php?valid_name=FUZZ -fc 401
```

### POST data fuzzing

This is a very straightforward operation, again by using the `FUZZ` keyword. This example is fuzzing only part of the POST request. We're again filtering out the 401 responses.

root@kitploit:~

```
ffuf -w /path/to/postdata.txt -X POST -d "username=admin\&password=FUZZ" -u https://target/login.php -fc 401
```

### Maximum execution time

If you don't want ffuf to run indefinitely, you can use the `-maxtime`. This stops **the entire** process after a given time (in seconds).

root@kitploit:~

```
ffuf -w /path/to/wordlist -u https://target/FUZZ -maxtime 60
```

When working with recursion, you can control the maxtime **per job** using `-maxtime-job`. This will stop the current job after a given time (in seconds) and continue with the next one. New jobs are created when the recursion functionality detects a subdirectory.

root@kitploit:~

```
ffuf -w /path/to/wordlist -u https://target/FUZZ -maxtime-job 60 -recursion -recursion-depth 2
```

It is also possible to combine both flags limiting the per job maximum execution time as well as the overall execution time. If you do not use recursion then both flags behave equally.

### Using external mutator to produce test cases

For this example, we'll fuzz JSON data that's sent over POST. [Radamsa](https://gitlab.com/akihe/radamsa) is used as the mutator.

When `--input-cmd` is used, ffuf will display matches as their position. This same position value will be available for the callee as an environment variable `$FFUF_NUM`. We'll use this position value as the seed for the mutator. Files example1.txt and example2.txt contain valid JSON payloads. We are matching all the responses, but filtering out response code `400 - Bad request`:

root@kitploit:~

```
ffuf --input-cmd 'radamsa --seed $FFUF_NUM example1.txt example2.txt' -H "Content-Type: application/json" -X POST -u https://ffuf.io.fi/FUZZ -mc all -fc 400
```

It of course isn't very efficient to call the mutator for each payload, so we can also pre-generate the payloads, still using [Radamsa](https://gitlab.com/akihe/radamsa) as an example:

root@kitploit:~

```
# Generate 1000 example payloads
radamsa -n 1000 -o %n.txt example1.txt example2.txt

# This results into files 1.txt ... 1000.txt
# Now we can just read the payload data in a loop from file for ffuf

ffuf --input-cmd 'cat $FFUF_NUM.txt' -H "Content-Type: application/json" -X POST -u https://ffuf.io.fi/ -mc all -fc 400
```

### Configuration files

When running ffuf, it first checks if a default configuration file exists. Default path for a `ffufrc` file is
`$XDG_CONFIG_HOME/ffuf/ffufrc`. You can configure one or multiple options in this file, and they will be applied on
every subsequent ffuf job. An example of ffufrc file can be found
[here](https://github.com/ffuf/ffuf/blob/master/ffufrc.example).

A more detailed description about configuration file locations can be found in the wiki:
<https://github.com/ffuf/ffuf/wiki/Configuration>

The configuration options provided on t...