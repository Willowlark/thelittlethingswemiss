---
title: Aurii Library
permalink: /aurii_library/index.html
---

The Aurii Library (Located in Theanovene, for anyone curious) is a collection of documents that chronicle the world as a whole, it's people, the events, and stories that take place with in it. Find below Aurii's history, people, and current events. 

---


{% for item in site.aurii_library %}
# [{{ item.title }}]({{site.baseurl}}{{item.url}})
> {{ item.excerpt }}
{% endfor %}