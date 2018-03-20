---
title: Gathering Shoots
---

Photoshoots, usually at cons, that are a bunch of like minded individuals all together. 

You can also view them directly on [Flickr](https://www.flickr.com/photos/thelittlethingswemiss/collections/72157683243269453/).

{% for post in site.categories.group %}
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