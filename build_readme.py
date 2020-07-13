from pathlib import Path

import feedparser


def main():
    chunks = list(get_opening_text())
    chunks.append('')
    chunks.extend(get_latest_blog_posts())
    readme = Path(__file__).parent / "README.md"
    readme.write_text("\n".join(chunks))


def get_opening_text():
    s = []
    with open('intro.txt', 'r') as file:
        [s.append(line.strip()) for line in file.readlines()]
    return s


def build_latest_blog_posts_str(posts: list) -> str:
    s = []
    for post in posts:
        s.append(f"{chr(10132)} [{post['title']}]({post['link']})")
        s.append(f"(Last updated by {post['author']} on {post['updated'].split('T')[0]})")
        s.append('\n')
    return s


def get_latest_blog_posts():
    XML_FEED_LOCATION = "http://localhost:8001/blog/sitenews/atom/"
    chunks = ["#### Latest Blog Posts\n"]
    posts = feedparser.parse(XML_FEED_LOCATION)["entries"][:10]
    chunks.extend(build_latest_blog_posts_str(posts))
    return chunks


if __name__ == "__main__":
    main()
