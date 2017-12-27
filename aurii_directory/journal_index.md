---
title: Journal Index
permalink: /aurii_journals/index.html
---

Index of the Journals for the players in Aurii

---


{% for item in site.aurii_journals %}
* [{{ item.title }}]({{site.baseurl}}{{item.url}}) *{{ item.date | date_to_string }}*
> {{ item.excerpt }}
{% endfor %}