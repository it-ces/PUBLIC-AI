## Preprocessing NLP module
# Iván Andrés Trujillo Abella

import re 
import unicodedata



def clean_space_document(document):
    new_doc = []
    for row in  document:
        if (len(row)==0 or len(row)==1) and (row==" " or row==''):
            pass
        else:
            new_doc.append(row)
    return new_doc

def lower_document(document):
    new_doc = []
    for row in  document:
        new_doc.append(row.lower())
    return new_doc

def doc_strip(document):
    new_doc = []
    for row in document:
        new_doc.append(row.strip())
    return new_doc

def remove_accents(document):
    # Define a dictionary mapping accented characters to their unaccented equivalents
    accents_mapping = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'ñ': 'ñ', 'Ñ': 'Ñ'
    }
    new = []
    for row in document:
        # Replace accented characters with their unaccented equivalents
        new_row = ''.join(accents_mapping.get(char, char) for char in row)
        new.append(new_row)
    return new


patterns = {
    'emails':r'\b\S+@\w+\.\w*.(co|es)?\b', # to drop emails...
    'web':r'(https|www)[.|:](\/\/)?.+', # to drop web pages..
    'digits':r'[0-9]*\.?[0-9]*(%)?', # To drop digits as 1.03, 124
    'Return':r'\n',  # To drop new line
    'symbols':r'[^a-zA-Z\sñáéíóú]'} # drop symbols no alphabetical... 

def apply_row_patterns(row, patterns):
    for pattern in patterns:
       if pattern =='Return' or pattern=='symbols':
           row = re.sub(patterns[pattern], ' ',  row, flags=re.IGNORECASE)
       else:
           row = re.sub(patterns[pattern], '',  row, flags=re.IGNORECASE)
    return row

def apply_document_patterns(document, patterns):
    new = []
    for row in document:
        new.append(apply_row_patterns(row, patterns))
    return new


def process_texts(documents, patterns=patterns):
    new_documents = []
    for document in documents:
        document = lower_document(document)
        document   = clean_space_document(document)
        document = doc_strip(document)
        document = apply_document_patterns(document, patterns)
        document = remove_accents(document)
        new_documents.append(document)
    return new_documents



def flat_DOCS(DOCS):
    new = []
    for doc in DOCS:
        new.append("".join(doc))
    return new


