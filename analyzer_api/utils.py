from lib2to3.pgen2 import token
import math
import re
import cmath
from this import s
import pymorphy2 as pym
import spacy
from collections import Counter
#rus
nlp = spacy.load("ru_core_news_sm")
#eng
nlp2 = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")

def get_analyze_results(text):
    
    nlp_doc = nlp(text)
    # lemmatizer = nlp.get_pipe("lemmatizer")
    
    cleaned_nlp_doc = [token.text for token in nlp_doc if not token.is_stop and not token.is_punct and token.pos_ is 'NOUN']
    # lemmatized_nlp_doc = [token.lemma_ for token in cleaned_nlp_doc]
    # print(lemmatized_nlp_doc)

    analyze_results = {}

    analyze_results["symbol_count"] = get_symbol_count(text)

    analyze_results["symbol_count_without_punct"] = get_symbol_count_without_punct(nlp_doc)

    analyze_results["word_count"] = get_word_count(nlp_doc)

    analyze_results["sentence_count"] = get_sentence_count(nlp_doc)

    analyze_results["water_content"] = get_water_content(nlp_doc)

    analyze_results["classic_nausea"] = get_classic_nausea(cleaned_nlp_doc)

    analyze_results["academic_nausea"] = get_academic_nausea(nlp_doc)

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

def get_sentence_count(nlp_document):
    sentence_count = len([sent.text for sent in nlp_document.sents])
    return sentence_count

def get_water_content(nlp_document):
    water_word_amount = len([token for token in nlp_document if token.is_stop])
    water_content = round(water_word_amount / get_word_count(nlp_document) * 100, 2)
    return water_content

def get_classic_nausea(nlp_document):
    word_frequency = Counter(nlp_document)
    most_common_word = word_frequency.most_common(1)
    classic_nausea = round(math.sqrt(most_common_word[0][1]), 2)
    return classic_nausea

def get_academic_nausea(nlp_document):
    cleaned_nlp_doc = [token.text for token in nlp_document if not token.is_stop and not token.is_punct and token.pos_ is 'NOUN']
    word_frequency = Counter(cleaned_nlp_doc)
    most_common_word = word_frequency.most_common(1)
    academic_nausea = round(most_common_word[0][1] / get_word_count(nlp_document) * 100, 2)
    return academic_nausea





# Метод разбивает строку на слова и возвращает словарь найденых слов с их индексами в строке
# {'Слова':[(начальный индекс вхождения 1, конечный индекс вхождения 1),(начальный индекс вхождения 2, конечный индекс вхождения 2),...]}
# def get_word_positions(text):
#     # Убирает лишние символы и сдвигает индексы соответственно
#     def temp(tp):
#         r = re.finditer('\w+', tp[2])
#         s = next(r)
#         return tp[0] + s.start(0), tp[0] + s.start(0) + (s.end(0) - s.start(0)), s.group(0)

#     tmp = {}
#     for m in re.finditer('[\W|\s]?(\w+)[\W|\s]?', text):
#         w = temp((m.start(0), m.end(0), m.group(0)))
#         if w[2] in tmp.keys():
#             tmp[w[2]].append((w[0], w[1]))
#         else:
#             tmp[w[2]] = [(w[0], w[1])]

#     return tmp


# Метод выделяет из списка слов значемые (существительные)
# и стоп слова (Союзы, Местоимения, Предлоги, Частицы, Междометия, Цифры)
# и иностранные слова
# def get_morph_words(words):
#     significant_words = []
#     insignificant_words = []
#     latin_words = []
#     morph_analyzer = pym.MorphAnalyzer()
#     for word in words:
#         if 'NOUN' in morph_analyzer.parse(word)[0].tag:
#             significant_words.append(word)
#         elif ('CONJ' or 'NPRO' or 'PREP' or 'PRCL' or 'INTJ' or 'NUMR') in morph_analyzer.parse(word)[0].tag:
#             insignificant_words.append(word)
#         elif morph_analyzer.parse(word)[0].tag.POS is None:
#             latin_words.append(word)
#     return significant_words, insignificant_words, latin_words


# Метод возвращает все аналитические параметры текста
# def get_text_stats(text):
#     words = get_word_positions(text)

#     # Количество символов
#     symbol_count = len(text)

#     # Количество символов без пробелов
#     symbol_count_no_wp = len(re.sub('\s+', '', text))

#     # Количество слов
#     word_count = sum([len(x) for x in words.values()])

#     # Количество букв
#     letter_count = sum([len(w) for w in words.keys()])

#     morph_words = get_morph_words(words)

#     # Количество иностранных слов
#     word_latin_count = len(morph_words[2])

#     try:
#         # Процент воды
#         text_water_perc = sum([len(words[mw]) for mw in morph_words[1]]) / sum(
#             [len(words[mw]) for mw in morph_words[0]]) * 100
#     except ZeroDivisionError:
#         text_water_perc = 100

#     # Количество знаков пунктуации
#     punctuation_count = len([x for x in text if re.match('[^\w\s\d]', x)])

#     # Значимые слова отсортированные по количеству
#     significant_words_sorted = sorted([(x, len(words[x])) for x in morph_words[0]], key=lambda item: item[1],
#                                       reverse=True)

#     try:
#         if len(significant_words_sorted) > 0:
#             # Классическая тошнота текста
#             classic_text_nausea = round(cmath.sqrt(significant_words_sorted[0][1]).real, 2)
#             # Академическая тошнота текста
#             academician_text_nausea = round(significant_words_sorted[0][1] / word_count * 100, 2)
#         else:
#             classic_text_nausea = 0
#             academician_text_nausea = 0
#     except Exception as ex:
#         print(ex)
#     return (('Общее количество слов: ', word_count),
#             ('  Общее количество символов (с пробелами): ', symbol_count),
#             ('  Общее количество символов (без пробелов): ', symbol_count_no_wp),
#             ('  Общее количество букв: ', letter_count),
#             ('  Количество иностранных слов: ', word_latin_count),
#             ('  Общее количество знаков пунктуации: ', punctuation_count),
#             ('  Классическая тошнота документа: ', classic_text_nausea),
#             ('  Аккадемическая тошнота документа: ', academician_text_nausea),
#             ('  Процент воды: ', text_water_perc))



#parsers
 