---
title: Play by Post GM Blog
permalink: /aurii/
---

{% for post in site.categories.aurii %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}