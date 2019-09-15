import requests
import re

def sort_response(url):  # returns request object
    return requests.get(url)

def extract_alt_text(document):  # returns list
    # finding all "Image may contain: {some bits}" in the web page.
    # useful if URL is a gallery and contains several images.
    captions = re.findall("\"Image may contain:.*?\"", document.text)  # creates a list
    clean_captions = []
    for caption in captions:
        clean_captions.append(remove_punctuation(caption))
    return clean_captions

def remove_punctuation(text):
    return text.replace('\"', "")

def instagram_alt_text_from_url(url):  # returns a tuple.
    response = sort_response(url)
    return url, extract_alt_text(response)

#links to parse here:
links = []

for link in links:
    print(instagram_alt_text_from_url(link))
