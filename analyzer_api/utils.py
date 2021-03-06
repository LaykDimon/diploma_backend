import math
import spacy
import re
from collections import Counter

#rus
nlp = spacy.load("ru_core_news_sm")
#eng
# nlp = spacy.load("en_core_web_sm")

lemmatizer = nlp.get_pipe("lemmatizer")

def get_analyze_results(text):
    
    nlp_doc = nlp(text)
    # print(Counter(nlp_doc).most_common(50))
    # lemmatizer = nlp.get_pipe("lemmatizer")
    
    # cleaned_nlp_doc = [token.text for token in nlp_doc if not token.is_stop and not token.is_punct]
    # print(Counter(cleaned_nlp_doc).most_common(50))
    # print(cleaned_nlp_doc)

    lemmatized_nlp_doc = [token.lemma_ for token in nlp_doc if not token.is_stop and not token.is_punct]
    
    NUMBERS_PATTERN = '[0-9]'
    EMOJI_PATTERN = re.compile(
        "(["
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "])"
    )

    lemmatized_nlp_doc = [re.sub(EMOJI_PATTERN, '', i) for i in lemmatized_nlp_doc]
    lemmatized_nlp_doc = [re.sub(NUMBERS_PATTERN, '', i) for i in lemmatized_nlp_doc]
    lemmatized_nlp_doc = [element for element in lemmatized_nlp_doc if element.strip()]
    # print(Counter(lemmatized_nlp_doc).most_common(50))

    analyze_results = {}

    analyze_results["symbol_count"] = get_symbol_count(text)

    analyze_results["symbol_count_without_punct"] = get_symbol_count_without_punct(nlp_doc)

    analyze_results["word_count"] = get_word_count(nlp_doc)

    analyze_results["lemmatized_word_count"] = get_lemmatized_word_count(lemmatized_nlp_doc)

    analyze_results["sentence_count"] = get_sentence_count(nlp_doc)

    analyze_results["water_content"] = get_water_content(nlp_doc)

    analyze_results["classic_nausea"] = get_classic_nausea(lemmatized_nlp_doc)

    analyze_results["academic_nausea"] = get_academic_nausea(nlp_doc)

    analyze_results["words"] = get_text_words(lemmatized_nlp_doc)

    return analyze_results
    

def get_symbol_count (text):
    symbol_count = len(text)
    return symbol_count

def get_symbol_count_without_punct(nlp_document):
    symbol_count_without_punct = len(''.join(token.text for token in nlp_document if token.is_punct != True))
    return symbol_count_without_punct

def get_word_count(nlp_document):
    word_count = len([token.text for token in nlp_document if token.is_punct != True])
    return word_count

def get_lemmatized_word_count(nlp_document):
    lemmatized_word_count = len(nlp_document)
    return lemmatized_word_count

def get_sentence_count(nlp_document):
    sentence_count = len([sent.text for sent in nlp_document.sents])
    return sentence_count

def get_water_content(nlp_document):
    water_word_amount = len([token for token in nlp_document if token.is_stop])
    water_content = round(water_word_amount / get_word_count(nlp_document) * 100, 2)
    #print(water_word_amount)
    return water_content

def get_classic_nausea(nlp_document):
    word_frequency = Counter(nlp_document)
    most_common_word = word_frequency.most_common(1)
    classic_nausea = round(math.sqrt(most_common_word[0][1]), 2)
    #print(most_common_word)
    return classic_nausea

def get_academic_nausea(nlp_document):
    lemmatized_nlp_doc = [token.lemma_ for token in nlp_document if not token.is_stop and not token.is_punct]
    lemmatized_nlp_doc = [element for element in lemmatized_nlp_doc if element.strip()]
    word_frequency = Counter(lemmatized_nlp_doc)
    most_common_word = word_frequency.most_common(1)
    #print(word_frequency.most_common(50 ))
    academic_nausea = round(most_common_word[0][1] / get_word_count(nlp_document) * 100, 2)
    return academic_nausea

def get_text_words(nlp_document):
    word_frequency = Counter(nlp_document)
    most_common_words = word_frequency.most_common()
    print(most_common_words)
    return most_common_words


# def show_recommendations(analyze_results):
#     if()