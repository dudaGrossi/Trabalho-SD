from setuptools import setup, find_packages

setup(
    name='YoutubeComments',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'google-auth-oauthlib',
        'google-auth',
        'google-api-python-client',
        'matplotlib',
        'wordcloud',
        'nltk'
    ],
)
