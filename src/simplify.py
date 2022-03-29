# coding=utf-8
import re


def create_corpora_simple_sentences():
    input_file = 'resources/Hindi Parallel Corpus.txt'
    with open(input_file) as f:
        for sentence in f:
            if is_simple_sentence(sentence):
                print(sentence.strip())

def is_simple_sentence(sentence):
    """
    # testcases
    # >>> is_simple_sentence("लेकिन अगर आप उनको ध्यान से देखेंगे तो आप पाएँगे कि इनमें से कुछ की टिमटिमाहट अन्य से अलग है।")
    # False
    # >>> is_simple_sentence("सूर्यास्त  के बाद आकाश को देखना कितना अच्छा लगता है।")
    # True
    # >>> is_simple_sentence("ऐसा प्रतीत होता है, मानो आकाश में हीरे जड़े हों।")
    # False
    # >>> is_simple_sentence(" पृथ्वी का आकार गोले के समान है,इसलिए एक समय में सिर्फ इसके आधे भाग पर ही सूर्य की रोशनी प्राप्त होती है ;चित्र(3.2)|")
    # False
    # >>> is_simple_sentence("इकबाल ने पूछा, हमारा पर्यावरण क्यों बदल रहा है?")
    True
    #>>> is_simple_sentence("सूर्यास्त  के बाद आकाश को देखना कितना अच्छा लगता है।")
    True
    #>>> is_simple_sentence("लेकिन अगर आप उनको ध्यान से देखेंगे तो आप पाएँगे कि इनमें से कुछ की टिमटिमाहट अन्य से अलग है।")
    False


    """
    # connective = "कि"
    # return not is_word_present(connective, sentence)

    connectives = ['कि', 'तथा', 'यद्यपि', 'और', 'मानो', 'परन्तु', 'जो', 'जिसे', 'जिसने ', 'जिसको', 'जिसका', 'जिसके', 'जिससे', 'जिसमें', 'जिनको', 'जिनके', 'जिनसे', 'जिनमें', 'जिन्हें', 'जिन्होंने', 'इसलिए', 'इसलिये', 'इसीलिये', 'क्योंकि', 'जैसे', 'किन्तु', 'एवं', 'यद्यपि', 'तथापि', 'भले ही', 'तो', 'अगर', 'मगर', 'अतः', 'चूंकि', 'चूँकि', 'जिस तरह', 'जिस प्रकार', 'लेकिन', 'जब', 'तब', 'तभी', 'या','जहाँ','वरना','अन्यथा','ताकि', 'बशर्तें' ,'जैसे', 'जबकि', 'यदि', 'मानो', 'वरन' , 'परंतु' , 'किंतु' , 'हालाँकि' , 'हालांकि', 'जिस', 'जिन']
    for x in connectives:
        complex_sentence = x in [ws.strip(',.?!') for ws in sentence.split()]
        if complex_sentence: break
    return not complex_sentence


if __name__ == "__main__":
    create_corpora_simple_sentences()
