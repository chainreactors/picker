---
title: DShield Sensor JSON Log to Elasticsearch, (Sat, Jan 21st)
url: https://isc.sans.edu/diary/rss/29458
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-22
fetch_date: 2025-10-04T04:34:25.158063
---

# DShield Sensor JSON Log to Elasticsearch, (Sat, Jan 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29456)
* [next](/diary/29460)

# [DShield Sensor JSON Log to Elasticsearch](/forums/diary/DShield%2BSensor%2BJSON%2BLog%2Bto%2BElasticsearch/29458/)

**Published**: 2023-01-21. **Last Updated**: 2023-01-21 17:35:47 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/DShield%2BSensor%2BJSON%2BLog%2Bto%2BElasticsearch/29458/#comments)

My current project has been to rebuild my home DShield sensor from a Rasberry Pi to a Ubuntu 20.04.5 LTS server to be able to process my sensor logs into Elasticsearh. I use as a guide the example listed [here](https://cowrie.readthedocs.io/en/latest/elk/README.html) (my ELK is version 8.x) sending the cowrie.json logs to a remote ELK server (version 8.4.1) using Filebeat and Logstash. However, my steps were a little different than the reference:

1 - Install the OS (basic server version)
2 - Add the following packages

$ sudo apt-get install net-tools open-vm-tools htop ntp bind9-utils vim network-manager
$ sudo systemctl start NetworkManager
$ sudo systemctl enable NetworkManager
$ sudo nmcli device show

Configure sensor static IP [[2](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-configure-networking-in-ubuntu-20-04-with-netplan/)]
$ sudo vi /etc/netplan/00-installer-config.yaml

3 - Install DShield sensor using the steps and script shared in [Github](https://github.com/DShield-ISC/dshield)
4 - Install and configure filebeat

$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-8.x.list
$ sudo apt-get update && sudo apt-get install filebeat

→ Edit and configure the filebeat.yml with the following setting to send the logs to Elasticsearch

$ sudo vi or nano /etc/filebeat/filebeat.yml

filebeat.inputs:

- type: log
  json.keys\_under\_root: true
  json.add\_error\_key: true
  json.message\_key: log

  # Unique ID among all inputs, an ID is required.
  id: cowrie

  # Change to true to enable this input configuration.
  enabled: true

  # Paths that should be crawled and fetched. Glob based paths.
  paths:
    - /srv/cowrie/var/log/cowrie/cowrie.json\*

output.logstash:
  hosts: ["192.168.xx.xx:5044"]

$ sudo systemctl start filebeat
$ sudo systemctl status filebeat
$ sudo systemctl enable filebeat

5 - Import the Cowrie mapping template into Elasticsearch via Dev Tools.
6 - Copy and configure Logstash parser (i.e. ELK destination, certificates, etc)

I have shared the Kibana Cowrie mapping template [here](https://handlers.sans.edu/gbruneau/elk/cowrie-mapping-template.txt) and logstash parser [here](https://handlers.sans.edu/gbruneau/elk/logstash-filter-cowrie.conf).
$ sudo systemctl restart logstash

After a logstash service restart, monitor the service to ensure there are no errors and a file like this, *cowrie-2023.01.21-000001* should be visible in the Index Management in Kibana. The shared dashboard available [here](https://handlers.sans.edu/gbruneau/elk/cowrie_8.4.1.ndjson) to be imported in Kibana in the shared object (version => 8.4.1).

**Kibana Cowrie logs**

![](https://isc.sans.edu/diaryimages/images/kibana_cowrie.PNG)

**Kibana Dashboard**

The activity shown in this dashboard should be the same as the logs the sensor is reporting to [DShield](https://isc.sans.edu/mysshreports/). Now this information is available to compare against threatintel.

![](https://isc.sans.edu/diaryimages/images/kibana_dashboard.PNG)

**DShield Sensor Log Location**

Log files: /srv/cowrie/var/log/cowrie/
Uploaded files: /srv/cowrie/var/lib/cowrie/downloads
Firewall logs: /var/log/dshield.log
Weblogs: /srv/www/DB/swebserver.sqlite

[1] https://cowrie.readthedocs.io/en/latest/elk/README.html
[2] https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-configure-networking-in-ubuntu-20-04-with-netplan/
[3] https://isc.sans.edu/tools/honeypot/
[4] https://isc.sans.edu/diary/29412
[5] https://isc.sans.edu/diary/29370
[6] https://isc.sans.edu/diary/28872
[7] https://handlers.sans.edu/gbruneau/elk/logstash-filter-cowrie.conf
[8] https://handlers.sans.edu/gbruneau/elk/cowrie\_8.4.1.ndjson
[9] https://handlers.sans.edu/gbruneau/elk/cowrie-mapping-template.txt

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [detection](/tag.html?tag=detection) [dshield](/tag.html?tag=dshield) [elasticsearch](/tag.html?tag=elasticsearch) [filebeat](/tag.html?tag=filebeat) [infosec](/tag.html?tag=infosec) [json](/tag.html?tag=json) [log analysis](/tag.html?tag=log analysis) [logs analysis](/tag.html?tag=logs analysis) [logstash](/tag.html?tag=logstash) [sensor](/tag.html?tag=sensor)

[0 comment(s)](/diary/DShield%2BSensor%2BJSON%2BLog%2Bto%2BElasticsearch/29458/#comments)

* [previous](/diary/29456)
* [next](/diary/29460)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)