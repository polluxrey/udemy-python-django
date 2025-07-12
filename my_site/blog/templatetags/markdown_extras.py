from django import template
from django.template.defaultfilters import stringfilter

import re
import markdown as md
from martor.templatetags.martortags import safe_markdown

register = template.Library()

# Matches: Markdown image + optional space + newline + ###### caption
IMAGE_WITH_HEADING_CAPTION = r'!\[.*?\]\(.*?\)\s*\n\s*#{6}\s.*\n?'


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])


@register.filter
def markdown_without_images_and_heading_captions(text):
    cleaned = re.sub(IMAGE_WITH_HEADING_CAPTION, '', text, flags=re.MULTILINE)
    return safe_markdown(cleaned)
