---
title: Table-2

---

{% for post in site.tags.rss %}
{% if post.tags contains "table-2" %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
{% endif %}
{% endfor %}