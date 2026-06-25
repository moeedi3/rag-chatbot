import re


def clean_text(text):

    # remove extra newlines
    text = text.replace("\n", " ")

    # remove repeated spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()