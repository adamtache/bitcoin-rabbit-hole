#! /usr/bin/python3
#-*- coding: UTF-8 -*-
import re
import unidecode

from goose3 import Goose

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

def get_excerpt_from_page(url):
    """ Rudimentary excerpt creator."""
    regex_object = re.compile(GRAB_FIRST_TWO_SENTENCES_RE)
    all_text_on_page = Goose().extract(url=url).cleaned_text if url != "" else ""
    sentences = regex_object.split(all_text_on_page, re.UNICODE)

    if len(sentences) == 0 or _is_common_bad_excerpt(sentences[0]):
        return EMPTY
    if len(sentences) == 1:
        return _remove_duplicate_spaces_and_colons(sentences[0] + PERIOD.replace(COLON, EMPTY))
    else:
        return _remove_duplicate_spaces_and_colons((sentences[0] + PERIOD + SPACE + sentences[1] + PERIOD).replace(COLON, EMPTY))

def _remove_duplicate_spaces_and_colons(str):
    return " ".join(str.split()).replaceAll(COLON, EMPTY)

def _is_common_bad_excerpt(sentence):
    common_bad_excerpts = [
        "JavaScript isn't enabled in your browser",
        "Get YouTube without the ads",
    ]
    for excerpt in common_bad_excerpts:
        if excerpt in sentence:
            return True
    return False

def title_to_file_path(title, resource_type):
    resources_folder_path = "../../collections/_"
    if (resource_type == 'writing'):
        resources_folder_path = resources_folder_path + "writings/"
    elif (resource_type == 'multimedia' or resource_type == "media"):
        resources_folder_path = resources_folder_path + "multimedia/"

    return "{}{}{}".format(
            resources_folder_path,
            _camel_case_to_dashed(title),
            MARKDOWN_SUFFIX)

def author_to_file_path(valid_author_slug):
    """ Replaces extraneous symbols and cleans up accents and umlauts
        in author names. """
    return "{}{}{}".format(
        "../../collections/_authors/",
        valid_author_slug,
        MARKDOWN_SUFFIX)

def get_valid_author_slug(author):
    return unidecode.unidecode(_remove_extraneous_symbols(
            re.sub(' ', '-', author.strip()).lower()))

def _camel_case_to_dashed(title):
    return _remove_extraneous_symbols(
                re.sub('([a-z0-9])([A-Z])', r'\1-\2',
                re.sub('(.)([A-Z][a-z]+)',r'\1-\2', title))).lower()

def _remove_extraneous_symbols(str):
    return re.sub(
        '-+',
        '-',
        re.sub(REMOVE_SPECIAL_CHARACTERS_RE, "", str))
