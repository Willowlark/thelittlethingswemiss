---
title: The Little Things We Miss
---

# The Little Things We Miss

The series which is also my namesake. There are five galleries, each covering a different aspect of the world. In a less poetic sense than "The Little Things", these are the photos that exist in every day life, things that look wonderful but we often walk past. The photos capture moments you just might have missed. 

You can also view them directly on [Flickr](https://www.flickr.com/photos/thelittlethingswemiss/collections/72157682809997653/).

{% for post in site.categories.tlt %}
* [{{ post.title }}]({{site.baseurl}}{{ post.url }}) *{{ post.date | date_to_string }}*
{% assign images = post.content | split:"<img " %}
{% for image in images %}
  {% if image contains 'src=' %}
    {% assign imageMarkup = image | split:">" | first %}
    <img style="max-height: 480px;" {{ imageMarkup }}>
    {% break %}
  {% endif %}
{% endfor %}
{% endfor %}