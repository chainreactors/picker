---
title: Creating a FujiWinFE external drive
url: https://malwaremaloney.blogspot.com/2026/04/last-child-margin-bottom-15px-table-tr.html
source: Instapaper: Unread
date: 2026-04-29
fetch_date: 2026-04-30T05:30:48.754205
---

# Creating a FujiWinFE external drive

[![MALoney (It's in the name)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFONMYzjaTaf0PMebgsLM2EgUZ1tLRqAAASIGtbHMoC0Lg8n676906qdGcFww5mXGQRtu3Cg4j3a8uB5oYQMljPSjjopnUdxLDQFxeSdleqk_TvvwAk1rBaBd-UfxK-W5caERP14HExgw/s1600/9-30-2016+6-41-54+AM.png)](https://malwaremaloney.blogspot.com/)

## Pages

* [Home](https://malwaremaloney.blogspot.com/)
* [All Things Symantec](https://malwaremaloney.blogspot.com/p/all-things-symantec.html)
* [All Things OneDrive](https://malwaremaloney.blogspot.com/p/all-things-onedrive.html)
* [Tools](https://malwaremaloney.blogspot.com/p/tools.html)

## Wednesday, April 8, 2026

### Creating a Fuji/WinFE external drive

# Creating a Fuji/WinFE external drive

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXdN7xBmAh5RuBpo2ENJMUqfouaQVPVdJMpOkDbcBjC6CO77bIjQHlhyphenhyphenI5qZpQ_NE270IzYuRDNjJQ6wu8m9c1iOFfBP6F1lfcx28eb80zQWK9Ct1g5nmM-fm74tHEk1nTlp8IEoCyh9JiqSzd9X43clq-ZHq2zNZv_4f4Xby9sd3djC9Utv3m3n2MEEk/s400/fujiwinfe.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXdN7xBmAh5RuBpo2ENJMUqfouaQVPVdJMpOkDbcBjC6CO77bIjQHlhyphenhyphenI5qZpQ_NE270IzYuRDNjJQ6wu8m9c1iOFfBP6F1lfcx28eb80zQWK9Ct1g5nmM-fm74tHEk1nTlp8IEoCyh9JiqSzd9X43clq-ZHq2zNZv_4f4Xby9sd3djC9Utv3m3n2MEEk/s575/fujiwinfe.png)

This post walks through how to build a combined Fuji Cartridge and WinFE drive, giving you a single setup that can handle forensic imaging for both macOS and Windows systems. Having everything on one device makes it easier to switch between platforms without needing multiple drives or tools.

The focus here is on preparing the external drive, setting up the partitions, and getting the Fuji Cartridge and WinFE in place. By the end, you’ll have a flexible, portable solution that can be used across a variety of imaging scenarios.

Building the WinFE (Windows Forensic Environment) itself isn’t covered in this post. If you need help with that piece, you can follow the instructions available at <https://www.winfe.net/build>
.

## Bill of Materials (BOM)

[Fuji: Forensic Unattended Juicy Imaging](https://fujiapp.top/)
[WinFE: Windows Forensic Environment](https://www.winfe.net/download)
[balenaEtcher](https://etcher.balena.io/)

## Preparing a Fuji Cartridge drive

Begin with an empty external drive; in this example, a 2 TB device is used.

An elevated Command Line Interface (CLI) session should be opened. From the prompt, run `diskpart` and press **Enter**.

Once the DiskPart utility launches, the prompt will appear as follows:

```
DISKPART>
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFuVt4GGxvNEGjGlp7eAx4ZnR-SXwxyQvccBu5xxVnSDh4vlEE3yfchES7KzjQtrkFabio7J7DwV9vlYJWhbJVBITpwMS6ylBr1jvnr-gLpdXqbYcfKhIOmVsViRSxAnsR4ovVsTil4o-s-XefvF07NYdaDbVqnPrNqHEkycA8Q8VAbGG-lY_5x0kS7LI/s1600/Screenshot_2026-04-08_094800.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhFuVt4GGxvNEGjGlp7eAx4ZnR-SXwxyQvccBu5xxVnSDh4vlEE3yfchES7KzjQtrkFabio7J7DwV9vlYJWhbJVBITpwMS6ylBr1jvnr-gLpdXqbYcfKhIOmVsViRSxAnsR4ovVsTil4o-s-XefvF07NYdaDbVqnPrNqHEkycA8Q8VAbGG-lY_5x0kS7LI/s1600/Screenshot_2026-04-08_094800.png)

Execute the following commands in sequence:

```
Type: List Disk <enter>
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1v6YOPHrxozWSskxMkkFicl-nD3SGm2VjhGk0zc5XcmTKheu-vEpxZSUGFy9p7XqL9DdQ9iUscIrhdjSNnx_C0Qyn567hMl5hgHr4h-fj3d6gQJaaWW7n9eSX2Kn9TJRqRwL7vHL5V2eLloC2jLhvyju-2NlQwnA1emYKJ_x4Qz6m8L9iDoMgIPC5L5k/s1600/Screenshot_2026-04-08_095027.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1v6YOPHrxozWSskxMkkFicl-nD3SGm2VjhGk0zc5XcmTKheu-vEpxZSUGFy9p7XqL9DdQ9iUscIrhdjSNnx_C0Qyn567hMl5hgHr4h-fj3d6gQJaaWW7n9eSX2Kn9TJRqRwL7vHL5V2eLloC2jLhvyju-2NlQwnA1emYKJ_x4Qz6m8L9iDoMgIPC5L5k/s1600/Screenshot_2026-04-08_095027.png)

```
Type: Select Disk X (X being your USB Hard Disk Drive) <Enter>
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ibTqqB5o3SggwFfDMD8zf05wopJhKi7JYa7KQ8GvzSdhMwhSbIgStL9ZsY61VukRAz-RCZFobviPXir5M3qReOfGJShIIGnaKA86qLSWIeV9CawCU7Ug1ebI3Ppt6tSiBXNjJjjgtPl-q8A4D0svjmHCyD3-UbRFV4MnUeOK3J1U1npPNtPnfMHxQ2k/s1600/Screenshot_2026-04-08_095204.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ibTqqB5o3SggwFfDMD8zf05wopJhKi7JYa7KQ8GvzSdhMwhSbIgStL9ZsY61VukRAz-RCZFobviPXir5M3qReOfGJShIIGnaKA86qLSWIeV9CawCU7Ug1ebI3Ppt6tSiBXNjJjjgtPl-q8A4D0svjmHCyD3-UbRFV4MnUeOK3J1U1npPNtPnfMHxQ2k/s1600/Screenshot_2026-04-08_095204.png)

```
Type: Clean <Enter>
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKpNp7USXwf3a7CA5GrGrhOwE0_cfzFmxADwkeNOiM6KdmKZDk7t0oUx-3cf9BDrPMl6KsxKZqfjzl5jSHVhLSsqgXHj08L4yO-64hXS5bbW0gabu2v3a_EDldxYwZnatx6UMBitqo2mjAiCbo21JAewAKYyER1DDJ7AnKbYNaN5QYPKc2jRpxg8Ejrhc/s1600/Screenshot_2026-04-08_095328.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKpNp7USXwf3a7CA5GrGrhOwE0_cfzFmxADwkeNOiM6KdmKZDk7t0oUx-3cf9BDrPMl6KsxKZqfjzl5jSHVhLSsqgXHj08L4yO-64hXS5bbW0gabu2v3a_EDldxYwZnatx6UMBitqo2mjAiCbo21JAewAKYyER1DDJ7AnKbYNaN5QYPKc2jRpxg8Ejrhc/s1600/Screenshot_2026-04-08_095328.png)

```
Type: Create Partition Primary Size = 256 <Enter>
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwPQSRlqVjnvXndZU9LvV_3SVlZ6EZi_Qb7CkKDnJ93eJn2knHCykqKKyt-2h-Hsp39COlOIoM1dq3bOc3iqiYRiboDPrFCCDm_uBC0_aSYFyLgg5gjktXlhwh7AJQIZ65573H5O4WDTFC1aG_aoFmAeWMSiPWqBAFxUC2oguuJrYNoLzpWJt4f5a7z1Y/s1600/Screenshot_2026-04-08_095604.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwPQSRlqVjnvXndZU9LvV_3SVlZ6EZi_Qb7CkKDnJ93eJn2knHCykqKKyt-2h-Hsp39COlOIoM1dq3bOc3iqiYRiboDPrFCCDm_uBC0_aSYFyLgg5gjktXlhwh7AJQIZ65573H5O4WDTFC1aG_aoFmAeWMSiPWqBAFxUC2oguuJrYNoLzpWJt4f5a7z1Y/s1600/Screenshot_2026-04-08_095604.png)

```
Type: Exit <Enter>
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXRge9plcYX6Fy1xnSNfINnerIKxY4nS9V-bapPSuWPIs5CWmYsVl6PK4DNWmJhOPZR8GmV36-kzEXVVXm2v-pq1F6QUkwG8-HMG8aQYsmSp2p-3AzkkDbgv8EKdvT9-9mRVKaNZWKL_coQx45OcOvZK01KLXTgXAEoETIQrGEyizLEl6IlDQOE_94LGc/s1600/Screenshot_2026-04-08_103112.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhXRge9plcYX6Fy1xnSNfINnerIKxY4nS9V-bapPSuWPIs5CWmYsVl6PK4DNWmJhOPZR8GmV36-kzEXVVXm2v-pq1F6QUkwG8-HMG8aQYsmSp2p-3AzkkDbgv8EKdvT9-9mRVKaNZWKL_coQx45OcOvZK01KLXTgXAEoETIQrGEyizLEl6IlDQOE_94LGc/s1600/Screenshot_2026-04-08_103112.png)

At this stage, the disk layout should appear as follows:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPW3hvRA81guv2hJHY3xJSsFf_zXYaVBaXsXtHC4skq5beih01kIEX6rGsOCpjctEEhjjKppvDAox6vIrVoYgo58dzZYh9txvwG_0O6VaUonCigeiZTeK4a784FDwY3igMcYCT5akxQNWPwoVPvJwem7w9A-nwivdwqgTA2tcbSlBA8LTxf3UuEaQsoco/s1600/Screenshot_2026-04-08_102921.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPW3hvRA81guv2hJHY3xJSsFf_zXYaVBaXsXtHC4skq5beih01kIEX6rGsOCpjctEEhjjKppvDAox6vIrVoYgo58dzZYh9txvwG_0O6VaUonCigeiZTeK4a784FDwY3igMcYCT5akxQNWPwoVPvJwem7w9A-nwivdwqgTA2tcbSlBA8LTxf3UuEaQsoco/s1600/Screenshot_2026-04-08_102921.png)

Next, launch **balenaEtcher** and select **Flash from file**.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhvgi2uzF0lKzY6V3FeRaFDlbKyN1uDu5Dj0wHkr81Nt5BmhvN1-_8ktJ_VfiGhayOy8T4_xJPUUVub9R_8y3AzW17lmzO3qX_a4r861TP-1p09ZBONxVHv2w4Is7wRvpo0i96hgAAVxTOz6wMl8iO08LY0OZs7JAwa00ettiTrRTBcZ8xgHYY1AabZms/s1600/Screenshot_2026-04-08_103327.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjhvgi2uzF0lKzY6V3FeRaFDlbKyN1uDu5Dj0wHkr81Nt5BmhvN1-_8ktJ_VfiGhayOy8T4_xJPUUVub9R_8y3AzW17lmzO3qX_a4r861TP-1p09ZBONxVHv2w4Is7wRvpo0i96hgAAVxTOz6wMl8iO08LY0OZs7JAwa00ettiTrRTBcZ8xgHYY1AabZms/s1600/Screenshot_2026-04-08_103327.png)

Browse to and select the `FujiApp-1.2.0.dmg` image file.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-65uOO9fSX1yAJMdyjazCOkqw9NGozW6WfghUdt2WYxOjLeq65KE9T2Ii8JiocDW_Hpnqzlv_SwCms1AEHAbxkzBt9SS627t1DH-qPpBu-ptIyqKDhfU1z4rMjurfK5wR1t_XWE4sX4Nw_YM7jUZGPvK0fVO_bOHtyBxSs3Yzopa-cHqDG8Jj8TTFtT8/s1600/Screenshot_2026-04-08_103625.png)](https://blogger.googleusercontent.com/img/b/...