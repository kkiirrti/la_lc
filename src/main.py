# coding=utf-8
import re


def create_corpora_simple_sentences():
    input file = "resources/simple_corpora_hindi.txt"
    english_file = "resources/English Parallel Corpus.txt"
    out_file = "resources/simple_corpora_English.txt"
    with open(input_file) as hindi_file:
        for sentence in hindi_file:
            num = get_line_no(sentence)
            if output_sentence.split('.')[0] == line_num
                print(output_sentence)


def get_line_no(sentence):
    line_num = sentence.split('.')[0]
    return line_num



def find_line(line_num, english_file):
    """
    >>> find_line(0, english_file)
    False
    >>> find_line(3, english_file)
   True
    """



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
