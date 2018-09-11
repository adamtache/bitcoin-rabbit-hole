#! /usr/bin/python3
from goose3 import Goose

import re

GRAB_FIRST_TWO_SENTENCES_RE = '[.!?][\s]{1,2}(?=[A-Z])'

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
    regex_object = re.compile(GRAB_FIRST_TWO_SENTENCES_RE)
    all_text_on_page = Goose().extract(url=url).cleaned_text if url != "" else ""
    sentences = regex_object.split(all_text_on_page, re.UNICODE)

    if len(sentences) == 0:
        return EMPTY
    elif "JavaScript isn't enabled in your browser" in sentences[0]:
        return EMPTY
    elif len(sentences) > 1:
        return sentences[0] + PERIOD + sentences[1] + PERIOD
    else:
        return sentences[0] + PERIOD

def title_to_file_path(title, resource_type):
    """
    Converts camelCase to camel-case.
    Cleans up extraneous characters.
    """
    resources_folder_path = "../_"
    if (resource_type == 'Writing'):
        resources_folder_path = resources_folder_path + "writings"
    elif (resource_type == 'Multimedia'):
        resources_folder_path = resources_folder_path + "multimedia"

    return resources_folder_path + "/" \
            + re.sub('([a-z0-9])([A-Z])', r'\1-\2', \
            re.sub('(.)([A-Z][a-z]+)',r'\1-\2', title)) \
            .lower() \
            .replace(SPACE, EMPTY) \
            .replace(COMMA, DASH) \
            .replace(COLON, DASH) \
            .replace(OPEN_PAREN, EMPTY) \
            .replace(CLOSE_PAREN, EMPTY) \
            .replace(DASH + DASH, DASH) \
            .replace(QUOTE, EMPTY) \
            + MARKDOWN_SUFFIX
