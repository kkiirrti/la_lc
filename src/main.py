# coding=utf-8
import re


def create_corpora_simple_sentences():
    with open('resources/Hindi Parallel Corpus.txt') as f:
        for sentence in f:
            if is_simple_sentence(sentence):
                print(sentence.strip())


def is_word_present(word, sentence):
    """
    >>> is_word_present("कि", "जोमा अन्य से अलग है।")
    False
    >>> is_word_present("कि", "लेकिन अगर आप")
    False
    >>> is_word_present("कि", "ध्यान से देखेंगे,कि अगर आप")
    False
    >>> is_word_present("कि", "लेकिन अगर आप उनको ध्यान से देखेंगे तो आप पाएँगे कि इनमें से कुछ की टिमटिमाहट अन्य से अलग है।")
    True
    """
    match = re.match(r'\b({0})\b'.format(word), sentence)
    return True if match else False


def is_simple_sentence(sentence):
    """
    # >>> is_simple_sentence("लेकिन अगर आप उनको ध्यान से देखेंगे तो आप पाएँगे कि इनमें से कुछ की टिमटिमाहट अन्य से अलग है।")
    # False 
    # >>> is_simple_sentence("जोमा अन्य से अलग है।")
    # True

    >>> is_simple_sentence("सूर्यास्त  के बाद आकाश को देखना कितना अच्छा लगता है।")
    True
    >>> is_simple_sentence("लेकिन अगर आप उनको ध्यान से देखेंगे तो आप पाएँगे कि इनमें से कुछ की टिमटिमाहट अन्य से अलग है।")
    False
    """
    connective = "कि"
    return not is_word_present(connective, sentence)

    # connectives = ['कि', 'तथा', 'यद्यपि', 'और', 'मानो', 'परन्तु', 'जो', 'जिसे', 'जिसने ', 'जिसको', 'जिसका', 'जिसके', 'जिससे', 'जिसमें', 'जिनको', 'जिनके', 'जिनसे', 'जिनमें', 'जिन्हें', 'जिन्होंने', 'इसलिए', 'इसलिये', 'इसीलिये', 'क्योंकि', 'जैसे', 'किन्तु', 'एवं', 'यद्यपि', 'तथापि', 'भले ही', 'तो', 'अगर', 'मगर', 'अतः', 'चूंकि', 'चूँकि', 'जिस तरह', 'जिस प्रकार', 'लेकिन', 'जब', 'तब', 'तभी', 'या','जहाँ','वरना','अन्यथा','ताकि', 'बशर्तें' ,'जैसे', 'जबकि', 'यदि', 'मानो', 'वरन' , 'परंतु' , 'किंतु' , 'हालाँकि' , 'हालांकि', 'जिस', 'जिन']
    
    # complex_sentence =  ( ' तथा ' in sentence )

    # for x in connectives:
    #     complex_sentence =  x in sentence
    #     if complex_sentence: break
    # return not complex_sentence
    

if __name__ == "__main__":
    create_corpora_simple_sentences()
