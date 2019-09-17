import re
import requests


def get_response(url):  # returns request object
    #need to handle dodgy links.
    return requests.get(url)


def extract_instagram_alt_text(document):  # returns list
    # finding all "Image may contain: {some bits}" in the web page.
    # useful if URL is a gallery and contains several images.
    captions = re.findall('"Image may contain:.*?"', document.text)  # creates a list
    clean_captions = []
    return [remove_punctuation(caption) for caption in captions]


def remove_punctuation(text):
    return text.replace('\"', "")


def alt_text_from_url(url):  # returns a tuple.
    return extract_instagram_alt_text(get_response(url))


# links to parse here:
links = []

for link in links:
    print(link, extract_instagram_alt_text(link))
