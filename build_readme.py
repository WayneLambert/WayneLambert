from __future__ import absolute_import

from pathlib import Path
from typing import List

import feedparser


def get_opening_text() -> str:
    return Path('intro.html').read_text()


def get_latest_blog_posts() -> List:
    xml_feed_location = "https://waynelambert.dev/blog/sitenews/atom/"
    return feedparser.parse(xml_feed_location)["entries"][:5]


def replace_post_metadata(intro_html: str, posts: List) -> str:
    for idx, post in enumerate(posts):
        intro_html = intro_html.replace(f'[link_{idx + 1}]', post.links[0]['href'])
        intro_html = intro_html.replace(f'[title_{idx + 1}]', post.title)
    return intro_html


def main():
    intro_html = get_opening_text()
    posts = get_latest_blog_posts()
    final_html = replace_post_metadata(intro_html, posts)
    readme = Path(__file__).parent / "README.md"
    readme.write_text(final_html)


if __name__ == "__main__":
    main()
