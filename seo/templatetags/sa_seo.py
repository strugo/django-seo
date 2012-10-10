# -*- coding: utf-8 -*-
import random
from apps.blog.models import Post
from apps.news.models import NewsPiece
from apps.school.models import SchoolLesson
from apps.trends.models import Digest

from django import template
from django.conf import settings
from django.template.loader import render_to_string
from tagging.models import TaggedItem

register = template.Library()

@register.simple_tag
def sa_wiki_info(obj):
    return render_to_string('templatetags/wiki_info.html', {'obj': obj, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_invested(obj, title=None):
    data = {
        'obj': obj,
        'STATIC_URL': settings.STATIC_URL,
        'title': title,
    }
    return render_to_string('templatetags/wiki_invested.html', data)

@register.simple_tag
def sa_wiki_received(obj):
    return render_to_string('templatetags/wiki_received.html', {'obj': obj, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_offices(obj, qs):
    return render_to_string('templatetags/wiki_offices.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_main(obj):
    return render_to_string('templatetags/wiki_main.html', {'obj': obj, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_team(obj, qs):
    return render_to_string('templatetags/wiki_team.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_vacancies(obj, qs):
    return render_to_string('templatetags/wiki_vacancies.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_videos(obj, qs):
    return render_to_string('templatetags/wiki_videos.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_screenshots(obj, qs):
    return render_to_string('templatetags/wiki_screenshots.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_articles(obj, qs):
    return render_to_string('templatetags/wiki_articles.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_likes(obj=None):
    return render_to_string('templatetags/wiki_likes.html', {'obj': obj, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_banners(obj=None):
    return render_to_string('templatetags/wiki_banners.html', {'obj': obj, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_competitors(obj, qs):
    return render_to_string('templatetags/wiki_competitors.html', {'obj': obj, 'qs': qs, 'STATIC_URL': settings.STATIC_URL})

@register.simple_tag
def sa_wiki_deals(deals_count, deals_sum, deals_types):
    data = {
        'deals_count': deals_count,
        'deals_sum': deals_sum,
        'deals_types':deals_types,
    }
    return render_to_string('templatetags/wiki_deals.html', data)

@register.simple_tag
def sa_wiki_similar(obj):
    tags = obj.tags

    ITEMS_NUM = 3

    posts = list(TaggedItem.objects.get_union_by_model(Post, tags)[:ITEMS_NUM])
    news = list(TaggedItem.objects.get_union_by_model(NewsPiece, tags)[:ITEMS_NUM])
    lessons = list(TaggedItem.objects.get_union_by_model(SchoolLesson, tags)[:ITEMS_NUM])
    digests = list(TaggedItem.objects.get_union_by_model(Digest, tags)[:ITEMS_NUM])
    similar_items = posts + news + lessons + digests
    similar_items = filter(lambda si: si != obj, similar_items)
    similar_items = random.sample(similar_items, min(len(similar_items), ITEMS_NUM))
    return render_to_string('templatetags/wiki_similar.html', {'obj': obj, 'similar_items': similar_items, 'STATIC_URL': settings.STATIC_URL})

