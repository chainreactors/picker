---
title: Hacking at Scale: Crush Massive Target Scopes & Supercharge Your Bug Bounty
url: https://infosecwriteups.com/hacking-at-scale-crush-massive-target-scopes-supercharge-your-bug-bounty-dcd856d01601?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-14
fetch_date: 2025-10-06T23:21:41.862616
---

# Hacking at Scale: Crush Massive Target Scopes & Supercharge Your Bug Bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdcd856d01601&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-at-scale-crush-massive-target-scopes-supercharge-your-bug-bounty-dcd856d01601&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-at-scale-crush-massive-target-scopes-supercharge-your-bug-bounty-dcd856d01601&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dcd856d01601---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dcd856d01601---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hacking at Scale: Crush Massive Target Scopes & Supercharge Your Bug Bounty

[![Dheeraj Madhukar](https://miro.medium.com/v2/resize:fill:64:64/1*sh8iY28NfTWWQA5E3UklEQ.jpeg)](https://medium.com/%40dheerajkmadhukar?source=post_page---byline--dcd856d01601---------------------------------------)

[Dheeraj Madhukar](https://medium.com/%40dheerajkmadhukar?source=post_page---byline--dcd856d01601---------------------------------------)

6 min read

·

Jul 12, 2025

--

Listen

Share

## Build your own Distributed Commands Execution System

## **Why Distributed Command Execution?**

> Picture this: You’re hunting on a bug bounty program with a scope like **\*.bigcorp.com**. Your trusty **amass, subfinder, etc** run just dumped a list of **2 million subdomains** . Running **httpx** to check for live hosts on each one using a single machine?
> 😓 Now, imagine splitting those **2 million subdomains** across 10 **cloud VMs**, each running **httpx** in **parallel**, finishing the scan in hours instead of days. That’s the power of distributed command execution! Here’s why this setup is a game-changer for bug hunters:
> **Tackle Massive Scopes**: Distribute tasks across multiple servers to scan millions of subdomains lightning-fast.

* **Tackle Massive Scopes**: Distribute tasks across multiple servers to scan millions of subdomains lightning-fast.
* **Save Time**: Parallel execution means you’re finding live hosts (and potential vulns) while others are still waiting.
* **Run Any Tool**: From httpx to nmap to custom scripts, this system handles it all.
* **Find Bugs Faster**: Speed up recon to focus on chaining vulns for that critical bounty payout.

## Automating workflows

A big part of my workflow relies on automation. In fact, 60% of my tasks are automated with custom scripts that constantly look for bugs🐞 in public projects. However, automation isn’t just about executing scripts, it’s about doing it intelligently.

Press enter or click to view image in full size

![]()

Automating workflows

* **Master Node**: Your main machine queues commands (e.g., `subfinder, amass, nuclei`).
* **Worker Nodes**: Other machines (VMs, cloud instances) execute those commands in parallel.
* **Redis**: A fast message broker that coordinates tasks between the master and workers.
* **Round-Robin Algo**: Tasks are evenly distributed across workers, so no single machine gets overwhelmed.

## Setting Up Your Distributed Bug Bounty

Let’s get to the fun part — setting up your own distributed system. You’ll need a Linux machine (e.g., Kali) for the master and a few VMs or cloud instances for workers. I’ll walk you through the setup

## Step 1: Install Dependencies & Configure

> On **all nodes** (master and workers):

```
sudo apt update
sudo apt install python3 python3-pip python3-venv redis-server
mkdir -p /root/distshell
cd /root/distshell
python3 -m venv venv
source venv/bin/activate
pip install celery redis
```

Set the Redis password in `/etc/redis/redis.conf`

```
requirepass supersecret
bind 0.0.0.0
```

On the **master node** (or a dedicated Redis server), enable and start Redis:

```
sudo systemctl enable redis
sudo systemctl start redis
```

Test Redis (use your Redis server IP, e.g., `192.168.206.130`):

```
redis-cli --config ~/.rediscli -h 192.168.206.130 -p 6379 PING
```

Should return `PONG`. If it fails, check your firewall (`sudo ufw allow 6379`) or Redis config.

## Step 2: Create the Task Module

> Save this as `/root/distshell/tasks.py` on all nodes (master and workers):
>
> This is the heart of the system, defining how commands are executed and sent back to the master.
> *NOTE: Must verify* ***REDIS PASSWORD*** *&* **REDIS SERVER IP.**

```
import os
import logging
from celery import Celery

# Set up logging
logging.basicConfig(level=logging.INFO, filename='/tmp/celery_tasks.log')
logger = logging.getLogger(__name__)

# Celery configuration
app = Celery('distshell',
             broker='redis://default:supersecret@192.168.206.130:6379/0',
             backend='redis://default:supersecret@192.168.206.130:6379/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=300,
    broker_connection_retry_on_startup=True,
)

@app.task(name='distshell.execute_command')
def execute_command(command, run_id):
    import subprocess
    logger.info(f"Executing command: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=300)
        output = result.stdout + result.stderr
        status = 'success' if result.returncode == 0 else 'error'
    except subprocess.TimeoutExpired:
        output = "Command timed out"
        status = 'error'
        logger.error(f"Command timed out: {command}")
    except Exception as e:
        output = f"Command failed: {str(e)}"
        status = 'error'
        logger.error(f"Command failed: {command}, error: {str(e)}")
    return {'worker': os.uname().nodename, 'command': command, 'output': output.strip(), 'result': status, 'run_id': run_id}
```

## Step 3: Set Up the Scheduler

Save this as `/root/distshell/scheduler.py` on the master node:

```
import sys
import uuid
import logging
from celery.result import AsyncResult
from tasks import app, execute_command

# Set up logging
logging.basicConfig(level=logging.INFO, filename='/tmp/scheduler.log')
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting scheduler")
    run_id = str(uuid.uuid4())
    print(f"Started DistShell run {run_id}. Waiting for results...")

    # Read commands
    if len(sys.argv) > 1:
        commands = [' '.join(sys.argv[1:])]
    else:
        commands = []
        current_command = []
        for line in sys.stdin:
            line = line.strip()
            if line:
                current_command.append(line...