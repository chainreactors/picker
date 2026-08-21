---
title: strelka v1.0.2
url: https://kitploit.com/en/posts/github-target-strelka-v102
source: Kitploit
date: 2026-08-20
fetch_date: 2026-08-21T03:02:45.837726
---

# strelka v1.0.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2436/2065ad071dd20cf7e35ddddfba0598d78452e4670e89342eed6f7a190a0a1fcb.png)

New releaseAug 20, 2026

# strelka v1.0.2

Real-time, container-based file scanning at enterprise scale

Share

# ![Strelka Banner](https://assets.kitploit.com/production/public/readmes/2436/2065ad071dd20cf7e35ddddfba0598d78452e4670e89342eed6f7a190a0a1fcb.png)

[Releases](https://github.com/target/strelka/releases/latest "Strelka Latest Release ➶")   |   [Documentation](https://target.github.io/strelka/#/ "Strelka Documentation ➶")   |   [Pull Requests](https://github.com/target/strelka/pulls "Strelka Pull Requests ➶")   |   [Issues](https://github.com/target/strelka/issues "Strelka Issues ➶")

[![GitHub release](https://img.shields.io/github/release/target/strelka.svg?style=for-the-badge)](https://github.com/target/strelka "Strelka Repository ➶") [![Build Status](https://img.shields.io/github/actions/workflow/status/target/strelka/build_strelka_nightly.yml?branch=master&style=for-the-badge)](https://github.com/target/strelka/actions/workflows/build_strelka_nightly.yml "Github Actions ➶") [![Pull Requests](https://img.shields.io/badge/PRs-welcome-orange.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz48c3ZnIGlkPSJzdmcyIiB3aWR0aD0iNjQ1IiBoZWlnaHQ9IjU4NSIgdmVyc2lvbj0iMS4wIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPiA8ZyBpZD0ibGF5ZXIxIj4gIDxwYXRoIGlkPSJwYXRoMjQxNyIgZD0ibTI5Ny4zIDU1MC44N2MtMTMuNzc1LTE1LjQzNi00OC4xNzEtNDUuNTMtNzYuNDM1LTY2Ljg3NC04My43NDQtNjMuMjQyLTk1LjE0Mi03Mi4zOTQtMTI5LjE0LTEwMy43LTYyLjY4NS01Ny43Mi04OS4zMDYtMTE1LjcxLTg5LjIxNC0xOTQuMzQgMC4wNDQ1MTItMzguMzg0IDIuNjYwOC01My4xNzIgMTMuNDEtNzUuNzk3IDE4LjIzNy0zOC4zODYgNDUuMS02Ni45MDkgNzkuNDQ1LTg0LjM1NSAyNC4zMjUtMTIuMzU2IDM2LjMyMy0xNy44NDUgNzYuOTQ0LTE4LjA3IDQyLjQ5My0wLjIzNDgzIDUxLjQzOSA0LjcxOTcgNzYuNDM1IDE4LjQ1MiAzMC40MjUgMTYuNzE0IDYxLjc0IDUyLjQzNiA2OC4yMTMgNzcuODExbDMuOTk4MSAxNS42NzIgOS44NTk2LTIxLjU4NWM1NS43MTYtMTIxLjk3IDIzMy42LTEyMC4xNSAyOTUuNSAzLjAzMTYgMTkuNjM4IDM5LjA3NiAyMS43OTQgMTIyLjUxIDQuMzgwMSAxNjkuNTEtMjIuNzE1IDYxLjMwOS02NS4zOCAxMDguMDUtMTY0LjAxIDE3OS42OC02NC42ODEgNDYuOTc0LTEzNy44OCAxMTguMDUtMTQyLjk4IDEyOC4wMy01LjkxNTUgMTEuNTg4LTAuMjgyMTYgMS44MTU5LTI2LjQwOC0yNy40NjF6IiBmaWxsPSIjZGQ1MDRmIi8+IDwvZz48L3N2Zz4=)](https://github.com/target/strelka/pulls "Strelka Pull Requests ➶") [![Slack](https://img.shields.io/badge/slack-join-red.svg?style=for-the-badge&logo=slack)](https://join.slack.com/t/cfc-open-source/shared_invite/zt-e54crchh-a6x4iDy18D5lVwFKQoEeEQ "Slack (external link) ➶") [![License](https://img.shields.io/badge/license-apache-ff69b4.svg?style=for-the-badge&logo=apache)](https://raw.githubusercontent.com/target/strelka/master/LICENSE "Strelka License File ➶")

Strelka is a real-time, container-based file scanning system used for threat hunting, threat detection, and incident response. Originally based on the design established by Lockheed Martin's [Laika BOSS](https://github.com/lmco/laikaboss) and similar projects (see: [related projects](#related-projects)), Strelka's purpose is to perform file extraction and metadata collection at enterprise scale.

Strelka differs from its sibling projects in a few significant ways:

* Core codebase is Go and Python3.10+
* Server components run in containers for ease and flexibility of deployment
* OS-native client applications for Windows, Mac, and Linux
* Built using [libraries and formats](#architecture) that allow cross-platform, cross-language support

## Features

Strelka is a modular data scanning platform, allowing users or systems to submit files for the purpose of analyzing, extracting, and reporting file content and metadata. Coupled with a [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management), Strelka is able to aggregate, alert, and provide analysts with the capability to better understand their environment without having to perform direct data gathering or time-consuming file analysis.

![Strelka Features](https://assets.kitploit.com/production/public/readmes/2436/041d9351ce69c679db300b6ebd21a9c215a57a95736c7a5eb73935910e603f9c.png)

## Quickstart

Running a file through Strelka is simple. In this section, Strelka capabilities of extraction and analysis are demonstrated for a one-off analysis.

*Please review the [documentation](https://target.github.io/strelka/) for details on how to properly build and deploy Strelka in an enterprise environment.*

#### Step 1: Install prerequisites

root@kitploit:~

```
# Ubuntu 23.04
sudo apt install -y wget git docker docker-compose golang jq && \
sudo usermod -aG docker $USER && \
newgrp docker
```

#### Step 2: Download Strelka

root@kitploit:~

```
git clone https://github.com/target/strelka.git && \
cd strelka
```

#### Step 3: Download and install preferred yara rules (optional)

root@kitploit:~

```
rm configs/python/backend/yara/rules.yara && \
git clone https://github.com/Yara-Rules/rules.git configs/python/backend/yara/rules/ && \
echo 'include "./rules/index.yar"' > configs/python/backend/yara/rules.yara
```

#### Step 4a: Pull precompiled images and start Strelka

**Note**: You can skip the `go build` process and use the `Strelka UI` at `http://0.0.0.0:9980` to analyze files.

root@kitploit:~

```
docker compose -f build/docker-compose-no-build.yaml up -d && \
go build github.com/target/strelka/src/go/cmd/strelka-oneshot
```

#### Step 4b: Build and start Strelka

**Note**: You can skip the `go build` process and use the `Strelka UI` at `http://0.0.0.0:9980` to analyze files.

root@kitploit:~

```
docker compose -f build/docker-compose.yaml build && \
docker compose -f build/docker-compose.yaml up -d && \
go build github.com/target/strelka/src/go/cmd/strelka-oneshot
```

#### Step 5: Prepare a file to analyze

Use any malware sample, or other file you'd like Strelka to analyze.

root@kitploit:~

```
wget https://github.com/ytisf/theZoo/raw/master/malware/Binaries/Win32.Emotet/Win32.Emotet.zip -P samples/
```

#### Step 6: Analyze the file with Strelka using the dockerized oneshot

root@kitploit:~

```
./strelka-oneshot -f samples/Win32.Emotet.zip -l - | jq
```

#### What's happening here?

1. Strelka determined that the submitted file was an encrypted ZIP (See: [taste.yara](https://github.com/target/strelka/blob/HEAD/configs/python/backend/taste/taste.yara) [backend.yaml](https://github.com/target/strelka/blob/HEAD/configs/python/backend/backend.yaml))
2. [ScanEncryptedZip](https://github.com/target/strelka/blob/HEAD/src/python/strelka/scanners/scan_encrypted_zip.py) used a dictionary to crack the ZIP file password, and extract the compressed file
3. The extracted file was sent back into the Strelka pipeline by the scanner, and Strelka determined that the extracted file was an EXE
4. [ScanPe](https://github.com/target/strelka/blob/HEAD/src/python/strelka/scanners/scan_pe.py) dissected the EXE file and added useful metadata to the output
5. [ScanYara](https://github.com/target/strelka/blob/HEAD/src/python/strelka/scanners/scan_yara.py) analyzed the EXE file, using the provided rules, and added numerous matches to the output, some indicating the file might be malicious

*The following output has been edited for brevity.*

root@kitploit:~

```
{
  "file": {
    "depth": 0,
    "flavors": {
      "mime": ["application/zip"],
      "yara": ["encrypted_zip", "zip_file"]
    },
    "scanners": [
      "ScanEncryptedZip",
      "ScanEntropy",
      "ScanFooter",
      "ScanHash",
      "ScanHeader",
      "ScanYara",
      "ScanZip"
    ]
  },
  "scan": {
    "encrypted_zip": {
      "cracked_password": "infected",
      "elapsed": 0.1...