---
title: Theanovene Almanac Collection
excerpt: The library's collection of Theanovene almanacs, published by the Newscrafting guild her in Thenovene. It's recent collection unfortunately; our old collection was lost in some... strange circumstances.
---

---

{% for post in site.tags.theanovene-almanac %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
> {{ post.excerpt }}
{% endfor %}