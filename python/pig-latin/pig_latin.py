import re

VOWELS = "aeiou"

def parse_to_pig_latin(word):
    # Check if the word starts with a vowel or "xr" or "yt"
    if re.match(rf"^[{VOWELS}]|^(xr|yt)", word):
        return word + "ay"
    
    # Check if the word contains "qu"
    if re.search(r"qu", word):
        first, last = re.split(r"qu", word, maxsplit=1)
        if not re.search(rf"[{VOWELS}]", first):
            return last + first + "qu" + "ay"
    
    # Check if the word contains "y" not at the start
    if "y" in word[1:]:
        first, last = re.split(r"y", word, maxsplit=1)
        if not re.search(rf"[{VOWELS}]", first):
            return "y" + last + first + "ay"
    
    # Move the first consonant cluster to the end and add "ay"
    match = re.search(rf"[{VOWELS}]", word)
    if match:
        i = match.start()
        return word[i:] + word[:i] + "ay"
    
    return word
        
def translate(text):
    return " ".join([parse_to_pig_latin(word) for word in text.split(" ")])
    
    
                