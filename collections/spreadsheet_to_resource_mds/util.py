#! /usr/bin/python3
from goose3 import Goose

import re

GRAB_FIRST_TWO_SENTENCES_RE = '[.!?][\s]{1,2}(?=[A-Z])'
REMOVE_SPECIAL_CHARACTERS_RE = '[^a-zA-Z0-9-_*.]'

CLOSE_PAREN = ")"
COLON = "&#58"
COMMA = ","
DASH = "-"
EMPTY = ""
MARKDOWN_SUFFIX = ".md"
OPEN_PAREN = "("
PERIOD = "."
QUOTE = "\""
SPACE = " "

def get_first_two_sentences_from_page(url):
    """ Rudimentary excerpt creator."""
    regex_object = re.compile(GRAB_FIRST_TWO_SENTENCES_RE)
    all_text_on_page = Goose().extract(url=url).cleaned_text if url != "" else ""
    sentences = regex_object.split(all_text_on_page, re.UNICODE)

    if len(sentences) == 0:
        return EMPTY
    elif "JavaScript isn't enabled in your browser" in sentences[0]:
        return EMPTY
    elif "Get YouTube without the ads" in sentences[0]:
        return EMPTY
    elif len(sentences) > 1:
        return sentences[0] + PERIOD + sentences[1] + PERIOD
    else:
        return sentences[0] + PERIOD

def title_to_file_path(title, resource_type):
    resources_folder_path = "../_"
    if (resource_type == 'writing'):
        resources_folder_path = resources_folder_path + "writings/"
    elif (resource_type == 'multimedia' or resource_type == "media"):
        resources_folder_path = resources_folder_path + "multimedia/"

    return "{}{}{}".format(
            resources_folder_path,
            _camel_case_to_dashed(title),
            MARKDOWN_SUFFIX)

def _camel_case_to_dashed(title):
    return re.sub(
                REMOVE_SPECIAL_CHARACTERS_RE,
                EMPTY,
                re.sub('([a-z0-9])([A-Z])', r'\1-\2',
                re.sub('(.)([A-Z][a-z]+)',r'\1-\2', title))).lower()
