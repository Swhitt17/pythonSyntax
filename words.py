words = ["rain", "lane","install","bee","kitchen"]

def print_upper_words(words):
    """ print each word seperated and uppercased

    >>> print_upper_words(["rain", "lane","install","bee","kitchen"])
    RAIN
    LANE
    INSTALL
    BEE
    KITCHEN
    """
    for word in words:
        print(word.upper())

words2 =["entry","Equip","red","Era", "reputation"]

def print_upper_words2(words2):
     """ print each word seperated and uppercased that starts with e or E

     >>>print_upper_words2(["entry","Equip","red","Era", "reputation"])
     ENTRY
     EQUIP
     ERA 
     """
     for word in words2:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

words3 = ["ivory", "fearless","layer", "jungle", "banquet"]

def print_upper_words3(words3, must_start_with):
     """print each word seperated and uppercased if it starts with selected letters

     >>> print_upper_words3(["ivory", "fearless","layer", "jungle", "banquet"]),
                            must_start_with=["I","J"]

     IVORY
     JUNGLE                       
     """

     for word in words3:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
         