---
title: When AI Makes 0-Days Feel Like N-Days
url: https://starlabs.sg/blog/2026/07-when-ai-makes-0-days-feel-like-n-days/
source: Blog on STAR Labs
date: 2026-07-27
fetch_date: 2026-07-28T04:58:40.723530
---

# When AI Makes 0-Days Feel Like N-Days

[![STAR Labs](/images/logo.png)](/)

[About](/about/)
[Services](/services/)
[Advisories](/advisories/)
[Blog](/blog/)
[Achievements](/achievements/)
[Publications](/publications/)
[Team](/team/)
[RSS](/index.xml)

MENU

Research
July 27, 2026
By Lee Jia Jie (@mkofdwu)
17 min read

# When AI Makes 0-Days Feel Like N-Days

Table of Contents

* [Introduction](#introduction)
  + [AI usage](#ai-usage)
* [Brief conceptual overview of net/sched](#brief-conceptual-overview-of-netsched)
* [The bug](#the-bug)
  + [How are these functions reached?](#how-are-these-functions-reached)
  + [Extra requirements](#extra-requirements)
* [Race optimization](#race-optimization)
  + [1. Binder threads](#1-binder-threads)
  + [2. Deleter threads](#2-deleter-threads)
  + [Final race setup](#final-race-setup)
* [kASLR leak](#kaslr-leak)
* [Exploit - primitives](#exploit---primitives)
  + [Reclaim object](#reclaim-object)
  + [RCU](#rcu)
  + [KEYCTL\_UPDATE spray](#keyctl_update-spray)
* [RIP control to arbitrary write](#rip-control-to-arbitrary-write)
  + [One final, minor bug](#one-final-minor-bug)
* [Final exploit](#final-exploit)
  + [Demo video](#demo-video)
* [TyphoonPwn 2026 results](#typhoonpwn-2026-results)
* [Other bugs found](#other-bugs-found)
* [Closing thoughts](#closing-thoughts)

## Introduction

After my n-day analysis on net/tls bugs and exploit writing for a patched net/rxrpc bug, I moved on to 0-day bug hunting. With the help of AI, I found a UAF bug in net/sched, and went about creating an LPE exploit based on it. This blog goes into the technical details of that exploit, and how I optimized it to target CentOS 9 desktop in TyphoonPwn 2026.

Additionally, I will show a glimpse of two other exploitable bugs I found in kernel/events/core.c (with an LPE exploit for one).

### AI usage

Compared to my previous exploit for an n-day in net/rxrpc, I had a greater focus on completing and improving this exploit quickly rather than fully understanding every aspect from the ground up. As such, I used AI to speed up various aspects of the process - discovery of the bug, KASAN poc, and improving the race condition. It was certainly helpful for iterating quickly, but still lacking in reasoning ability and having clear blind spots. It was still crucial to exercise my own judgement especially when fine-tuning.

## Brief conceptual overview of net/sched

net/sched is the packet scheduling subsystem in linux. It sits in a layer above the device drivers, and decides when, in what order, and whether packets are transmitted. It also provides an API through netlink to configure packet handling rules. Each network device is attached to a Qdisc (queueing discipline) that holds all this configuration data.

To decide what to do with a given packet, net/sched introduces chains, filters and actions. Chains are an ordered list of filters, filters check for certain attributes in the packet, and based on that, decide what *action* to perform on it.

net/sched is designed in a way to maximally allow reuse of components - multiple network devices can share the same Qdisc. Importantly for this bug, actions can be shared within the same net namespace, and are uniquely identified by an “index”. A per-net radix tree `action_idr` records all action objects and enables lookup by their indexes. This is done by the `tcf_idr_check_alloc` function:

```
int tcf_idr_check_alloc(struct tc_action_net *tn, u32 *index,
			struct tc_action **a, int bind)
{
	struct tcf_idrinfo *idrinfo = tn->idrinfo;
	struct tc_action *p;
	int ret;
	u32 max;

	if (*index) {
		rcu_read_lock();
		p = idr_find(&idrinfo->action_idr, *index); // [0]: ACTION LOOKUP

		// [1]: WINDOW OPENS

		if (IS_ERR(p)) {
			/* This means that another process allocated
			 * index but did not assign the pointer yet.
			 */
			rcu_read_unlock();
			return -EAGAIN;
		}

		if (!p) {
			/* Empty slot, try to allocate it */
			max = *index;
			rcu_read_unlock();
			goto new;
		}

		// [2]: WINDOW CLOSES

		if (!refcount_inc_not_zero(&p->tcfa_refcnt)) {
			/* Action was deleted in parallel */
			rcu_read_unlock();
			return -EAGAIN;
		}

		if (bind)
			atomic_inc(&p->tcfa_bindcnt);
		*a = p;

		rcu_read_unlock();

		return 1;
	} else {
		/* Find a slot */
		*index = 1;
		max = UINT_MAX;
	}

new:
	*a = NULL;

	mutex_lock(&idrinfo->lock);
	ret = idr_alloc_u32(&idrinfo->action_idr, ERR_PTR(-EBUSY), index, max,
			    GFP_KERNEL);
	mutex_unlock(&idrinfo->lock);

	/* N binds raced for action allocation,
	 * retry for all the ones that failed.
	 */
	if (ret == -ENOSPC && *index == max)
		ret = -EAGAIN;

	return ret;
}
```

When creating a filter with a list of actions, we can simply specify the action index and it will be fetched from the idr without having to create a new object.

For this exploit, we need only focus on the netlink operations used to configure packet-handling rules, specifically those for creating and deleting filters.

## The bug

The vulnerability is a lock-mismatch: `tcf_idr_check_alloc()` accesses the action idr with only `rcu_read_lock()`, while actions are freed with `idrinfo->lock` and `rtnl_lock()` held, but without waiting for the RCU grace period (i.e. raw kfree).

Thus, this leads to a race condition where the action can be freed during lookup leading to a UAF scenario.

Take another look at the `tcf_idr_check_alloc` function above. If the retrieved `tc_action` has a `tcfa_refcnt` of 0, it gets dropped harmlessly. Thus, for a successful UAF we have to both free and reclaim the action (to overwrite `tcfa_refcnt`) within the same window [1] to [2].

The basic structure of the race looks like this:

```
CPU 0: lookup action  CPU 1: delete action  CPU 2: reclaim
====================  ====================  ==============
p = idr_find(
  &idrinfo->action_idr,
  *index
);
                      kfree(p);
                                            // reclaim
                                            // set p->tcfa_refcnt != 0
refcount_inc_not_zero(
  &p->tcfa_refcnt
)
```

### How are these functions reached?

I initially proved the bug using RTM\_NEWACTION and RTM\_DELACTION. However, these operations require CAP\_NET\_ADMIN in the *init* namespace, making this path infeasible:

```
static int tc_ctl_action(struct sk_buff *skb, struct nlmsghdr *n,
			 struct netlink_ext_ack *extack)
{
	struct net *net = sock_net(skb->sk);
	struct nlattr *tca[TCA_ROOT_MAX + 1];
	u32 portid = NETLINK_CB(skb).portid;
	u32 flags = 0;
	int ret = 0;

	if ((n->nlmsg_type != RTM_GETACTION) &&
	    !netlink_capable(skb, CAP_NET_ADMIN))
		return -EPERM;
```

Instead, we have to use RTM\_NEWTFILTER and RTM\_DELTFILTER. When creating a filter, we also specify a list of actions to create along with it. Likewise, deleting a filter allows us to free its actions once all other refs have been dropped.

By itself, this race is pretty challenging to hit. In the next section I’ll describe the techniques I used to ensure the race gets hit quickly, but first, some requirements for this exploit:

### Extra requirements

Note that in most cases, `rtnl_lock()` is taken in this path:

```
static int tc_new_tfilter(struct sk_buff *skb, struct nlmsghdr *n,
			  struct netlink_ext_ack *extack)
{
	...

	/* Take rtnl mutex if rtnl_held was set to true on previous iteration,
	 * block is shared (no qdisc found), qdisc is not unlocked, classifier
	 * type is not specified, classifier is not unlocked.
	 */
	if (rtnl_held ||
	    (q && !(q->ops->cl_ops->flags & QDISC_CLASS_OPS_DOIT_UNLOCKED)) ||
	    !tcf_proto_is_unlocked(name)) {
		rtnl_held = true;
		rtnl_lock();
	}
```

By using a clsact qdisc and flower filter (which have the necessary DOIT\_UNLOCKED flags set), we can avoid taking the lock. This requires CONFIG\_NET\_ACT\_GACT=y or m and CONFIG\_NET\_CLS\_FLOWER=y or m.

Since the bug can only be reached through netlink operations, we need to create a separate user namespace to have CAP\_NET\_ADMIN and pass the check:

```
static int rtnetlink_rcv_msg(struct sk_buff *sk...