---
title: Wifi_Db - Script To Parse Aircrack-ng Captures To A SQLite Database
url: https://buaq.net/go-153954.html
source: unSafe.sh - 不安全
date: 2023-03-18
fetch_date: 2025-10-04T09:56:34.567113
---

# Wifi_Db - Script To Parse Aircrack-ng Captures To A SQLite Database

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

![](https://8aqnet.cdn.bcebos.com/a2c0f81b4a1a917e49a85201f3c6ae9d.jpg)

Wifi\_Db - Script To Parse Aircrack-ng Captures To A SQLite Database

Script to parse Aircrack-ng captures into a SQLite database and extract useful information l
*2023-3-17 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-153954.htm)
阅读量:24
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhO52gZbQmL_OEzbU412aIPg_SeOmZWvXlqsbl-pDKOLdVB84rwbBJ4eh-P2m_hQBg0a_o8vk4Upb-hMQ_N06B4E3eA_c3uG1BdNCzWIVO3u8zvSBdoKFf7IaK5_6n4s-2EQ_7sfLQa3bBtuHoE8e_QNAYW9CosUxgbqtqAukbgqa3vbW-i_SwmvXOlmw=w640-h594)](https://blogger.googleusercontent.com/img/a/AVvXsEhO52gZbQmL_OEzbU412aIPg_SeOmZWvXlqsbl-pDKOLdVB84rwbBJ4eh-P2m_hQBg0a_o8vk4Upb-hMQ_N06B4E3eA_c3uG1BdNCzWIVO3u8zvSBdoKFf7IaK5_6n4s-2EQ_7sfLQa3bBtuHoE8e_QNAYW9CosUxgbqtqAukbgqa3vbW-i_SwmvXOlmw)

Script to parse [Aircrack-ng](https://www.kitploit.com/search/label/Aircrack-ng "Aircrack-ng") captures into a SQLite database and extract useful information like handshakes (in 22000 hashcat format), MGT identities, interesting relations between APs, clients and it's Probes, WPS information and a global view of all the APs seen.

```
           _   __  _             _  _
```

## Features

* Displays if a network is cloaked (hidden) even if you have the ESSID.
* Shows a detailed table of connected clients and their respective APs.
* Identifies client probes connected to APs, providing insight into potential security risks usin Rogue APs.
* Extracts handshakes for use with hashcat, facilitating password cracking.
* Displays identity information from enterprise networks, including the EAP method used for authentication.
* Generates a summary of each AP group by ESSID and encryption, giving an overview of the security status of nearby networks.
* Provides a WPS info table for each AP, detailing information about the Wi-Fi Protected Setup configuration of the network.
* Logs all instances when a client or AP has been seen with the GPS data and timestamp, enabling location-based analysis.
* Upload files with capture folder or file. This option supports the use of wildcards (\*) to select multiple files or folders.
* Docker version in Docker Hub to avoid dependencies.
* Obfuscated mode for demonstrations and conferences.
* Possibility to add static GPS data.

## Install

### From [DockerHub](https://hub.docker.com/r/r4ulcl/wifi_db "DockerHub") (RECOMMENDED)

```
docker pull r4ulcl/wifi_db
```

### Manual installation

#### Debian based systems (Ubuntu, Kali, Parrot, etc.)

Dependencies:

* python3
* python3-pip
* tshark
* hcxtools

```
sudo apt install tshark
sudo apt install python3 python3-pip

git clone https://github.com/ZerBea/hcxtools.git
cd hcxtools
make
sudo make install
cd ..
```

Installation

```
git clone https://github.com/r4ulcl/wifi_db
cd wifi_db
pip3 install -r requirements.txt
```

#### Arch

Dependencies:

* python3
* python3-pip
* tshark
* hcxtools

```
sudo pacman -S wireshark-qt
sudo pacman -S python-pip python

git clone https://github.com/ZerBea/hcxtools.git
cd hcxtools
make
sudo make install
cd ..
```

Installation

```
git clone https://github.com/r4ulcl/wifi_db
cd wifi_db
pip3 install -r requirements.txt
```

## Usage

### Scan with airodump-ng

Run [airodump-ng](https://www.kitploit.com/search/label/Airodump-ng "airodump-ng") saving the output with -w:

```
sudo airodump-ng wlan0mon -w scan --manufacturer --wps --gpsd
```

### Create the SQLite database using Docker

```
#Folder with captures
CAPTURESFOLDER=/home/user/wifi

# Output database
touch db.SQLITE

docker run -t -v $PWD/db.SQLITE:/db.SQLITE -v $CAPTURESFOLDER:/captures/ r4ulcl/wifi_db
```

* `-v $PWD/db.SQLITE:/db.SQLITE`: To save de output in current folder db.SQLITE file
* `-v $CAPTURESFOLDER:/captures/`: To share the folder with the captures with the docker

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhO52gZbQmL_OEzbU412aIPg_SeOmZWvXlqsbl-pDKOLdVB84rwbBJ4eh-P2m_hQBg0a_o8vk4Upb-hMQ_N06B4E3eA_c3uG1BdNCzWIVO3u8zvSBdoKFf7IaK5_6n4s-2EQ_7sfLQa3bBtuHoE8e_QNAYW9CosUxgbqtqAukbgqa3vbW-i_SwmvXOlmw=w640-h594)](https://blogger.googleusercontent.com/img/a/AVvXsEhO52gZbQmL_OEzbU412aIPg_SeOmZWvXlqsbl-pDKOLdVB84rwbBJ4eh-P2m_hQBg0a_o8vk4Upb-hMQ_N06B4E3eA_c3uG1BdNCzWIVO3u8zvSBdoKFf7IaK5_6n4s-2EQ_7sfLQa3bBtuHoE8e_QNAYW9CosUxgbqtqAukbgqa3vbW-i_SwmvXOlmw)

### Create the SQLite database using manual installation

Once the capture is created, we can create the database by importing the capture. To do this, put the name of the capture without format.

```
python3 wifi_db.py scan-01
```

In the event that we have multiple captures we can load the folder in which they are directly. And with -d we can rename the output database.

```
python3 wifi_db.py -d database.sqlite scan-folder
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhL-Vaq3y0psRaN7c_eyMvqHukYkNPKRfZPPWwljNybjzlT0zsbeKvXP2lM0fVTZ0dVQIukcYs-57pqIjat843tbV0yWdO1nAwO43J-hnbzsqcqKvo-JQQAPhqvSujFSrzB_BZc14hCY7nZ7QFF31Bo95pbRYY400wDbO1Oi_AgNXHI_D9U0g9aRqSODQ=w640-h478)](https://blogger.googleusercontent.com/img/a/AVvXsEhL-Vaq3y0psRaN7c_eyMvqHukYkNPKRfZPPWwljNybjzlT0zsbeKvXP2lM0fVTZ0dVQIukcYs-57pqIjat843tbV0yWdO1nAwO43J-hnbzsqcqKvo-JQQAPhqvSujFSrzB_BZc14hCY7nZ7QFF31Bo95pbRYY400wDbO1Oi_AgNXHI_D9U0g9aRqSODQ)

### Open database

The database can be open with:

* [sqlitebrowser](https://sqlitebrowser.org/ "sqlitebrowser")

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjPwrhKSOK5BnQ2JmXfkWW4dyotmo1eWC7XUhozQSJgl_j-1xQ6TiH2PSYyY4dFArbcEvS3Sy1otlzgxvh0ZLGSTaE69kf0bH_eihHko90e0D8PSxuiHNZyN7wreG_zOzu4lbduORFc0zrq2uh3qYPpzPVHM2keY-2wS_IeH0pDh_rjF-FbBwlsZ4-K_A=w640-h420)](https://blogger.googleusercontent.com/img/a/AVvXsEjPwrhKSOK5BnQ2JmXfkWW4dyotmo1eWC7XUhozQSJgl_j-1xQ6TiH2PSYyY4dFArbcEvS3Sy1otlzgxvh0ZLGSTaE69kf0bH_eihHko90e0D8PSxuiHNZyN7wreG_zOzu4lbduORFc0zrq2uh3qYPpzPVHM2keY-2wS_IeH0pDh_rjF-FbBwlsZ4-K_A)

Below is an example of a ProbeClientsConnected table.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgqPKxTR_l4MiEOdb6KlLy7AKeBmK5cYc3qPiLzGp3QsoShCax5pETY8-ESnCH2saQsmfsnJ4DY5dIyGTFvKHZPHY0W36xxYgpQVs6m1KSJ6wXRHc2x-P3IM1HnU2bKL_WCnhyb5N4008yQL9skZhaRGeVDb6uZRnfvPW_bxQbwsCN6n89uEJ9rSxBOOA=w640-h190)](https://blogger.googleusercontent.com/img/a/AVvXsEgqPKxTR_l4MiEOdb6KlLy7AKeBmK5cYc3qPiLzGp3QsoShCax5pETY8-ESnCH2saQsmfsnJ4DY5dIyGTFvKHZPHY0W36xxYgpQVs6m1KSJ6wXRHc2x-P3IM1HnU2bKL_WCnhyb5N4008yQL9skZhaRGeVDb6uZRnfvPW_bxQbwsCN6n89uEJ9rSxBOOA)

### Arguments

```
usage: wifi_db.py [-h] [-v] [--debug] [-o] [-t LAT] [-n LON] [--source [{aircrack-ng,kismet,wigle}]] [-d DATABASE] capture [capture ...]

positional arguments:
  capture               capture folder or file with extensions .csv, .kismet.csv, .kismet.netxml, or .log.csv. If no extension is provided, all types will
                        be added. This option supports the use of wildcards (*) to select multiple files or folders.

options:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  --debug               increase output verbosity to debug
  -o, --obfuscated      Obfuscate MAC and BSSID with AA:BB:CC:XX:XX:XX-defghi (WARNING: replace all database)
  -t LAT, --lat LAT     insert a fake lat in the new elements
  -n LON, --lon LON     insert a fake lon i   n the new elements
  --source [{aircrack-ng,kismet,wigle}]
                        source from capture data (default: aircrack-ng)
  -d DATABASE, --database DATABASE
                        output database, if exist append to the given database (default name: db.SQLITE)
```

### Kismet

TODO

### Wigle

TODO

## Database

wifi\_db contains several tables to store information related to wireles...