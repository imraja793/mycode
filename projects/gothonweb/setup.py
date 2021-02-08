try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    "name": "coding_challenge",
    "author": "raja",
    "description": "This is to gain knowledge from lpthw",
    "url": "URL to get",
    "download_url": "url to download_url",
    "author_email": "imraja793@gmail.com",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ['NAME'],
    "scripts": [],
}
setup(**config)
