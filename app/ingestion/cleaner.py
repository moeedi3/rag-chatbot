import re


def clean_text(text):

    # Remove line breaks
    text = text.replace("\n", " ")

    # Remove strange bullet characters
    text = text.replace("\uf0b7", " ")

    # Remove tabs
    text = text.replace("\t", " ")

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()