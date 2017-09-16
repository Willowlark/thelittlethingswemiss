---
title: Animu Blog
---

# Blogging about animu. (More than likely to be rants)

{% for post in site.categories.animu %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}