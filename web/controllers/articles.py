from web.models.articles import *
import datetime


# Returns (category, name) from a full name
def get_name(full_name):
    split = full_name.split(':', 1)
    if len(split) == 2:
        return split[0], split[1]
    else:
        return '_default', split[0]


def get_article(full_name_or_article):
    if type(full_name_or_article) == str:
        category, name = get_name(full_name_or_article)
        objects = Article.objects.filter(category=category, name=name)
        if objects:
            return objects[0]
        else:
            return None
    else:
        return full_name_or_article


# Creates article with specified id. Does not add versions
def create_article(full_name):
    category, name = get_name(full_name)
    article = Article(
        category=category,
        name=name,
        created_at=datetime.datetime.now(),
        title=name
    )
    article.save()
    return article


# Creates new article version for specified article
def create_article_version(full_name_or_article, source):
    article = get_article(full_name_or_article)
    version = ArticleVersion(
        article=article,
        created_at=datetime.datetime.now(),
        source=source,
        rendered=None
    )
    version.save()
    return version


# Get latest source of article
def get_latest_source(full_name_or_article):
    article = get_article(full_name_or_article)
    if article is None:
        return None
    latest_version = ArticleVersion.objects.filter(article=article).order_by('-created_at')[:1]
    if latest_version:
        return latest_version[0].source
    else:
        return None
