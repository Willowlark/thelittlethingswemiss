---
title: Journal of Elfriede Faun
excerpt: The Journal of Elfriede Faun
---

---

{% for post in site.tags.elfriede %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}