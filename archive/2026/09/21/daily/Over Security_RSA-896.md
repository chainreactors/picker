---
title: RSA-896
url: https://saweis.net/posts/rsa-896.html
source: Over Security
date: 2026-09-21
fetch_date: 2026-09-22T07:04:55.617710
---

# RSA-896

[Stephen A. Weis](../index.html)

# RSA-896

September 2026

[RSA-896](https://en.wikipedia.org/wiki/RSA_numbers#RSA-896) is a RSA challenge number I factored with Claude on September 19, 2026. More details will follow. Briefly,
Claude was used to port [CADO-NFS](https://cado-nfs.gitlabpages.inria.fr/) to run on GPUs. It orchestrated running on a fleet of up to 2048 GPUs as a low-priority job
during unused idle time between regular jobs. The computation ran over a 10-day period and performed about 30 GPU-years of compute time at Anthropic.

This work did not meaninfgully improve the runtime of the General Number Field Sieve (GNFS) algorithm. It does not impact the security of deployed RSA-2048 keys. However, it does
demonstrates that RSA-1024 keys are vulnerable to many actors with data center-level fleets of GPUs.

```
RSA-896 =
4120234369866595438555313653325759481798116998443279828454556264
3387644556524842619809887042316184187926142024718886949256093177
6375033421130982397485150944909106910269861031862704114880866970
5649029036536588674337317208131041051908642547932826013912576240
33946373269391
```

```
p =
636606729769440499166579950236036751749912014371509557713570027
508971809534551913252252094954941974952859310861988904737359709
200557919
q =
647218161102195448058768698177623951380616936266986989243011933
572862870905830904361851542450154852431416136790787107595965374
752513489
```