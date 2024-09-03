# Ordstatistik
# Din uppgift är att läsa in text från filen som är angiven.
# Därefter ska ditt program räkna ut följande:
# - Antal ord
# - Mest frekventa ord
# - Genomsnittlig ordlängd
# Gör en funktion för varje.

# Bonus, gör en i taget, skapa en funktion för varje: 
# - Längsta och kortaste ordet - om det finns flera, bestäm själv om du skriver ut ett eller flera
# - Räkna antalet unika ord (alltså ord som bara förekommer en gång)


import re
from collections import Counter
import os

def read_from_file(filename: str) -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    print(f"Försöker öppna fil: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Filen '{filename}' kunde inte hittas. Kontrollera att filen finns i samma katalog som skriptet.")
        return ""

def count_words(text: str) -> int:
    return len(re.findall(r'\w+', text))

def most_frequent_word(text: str) -> str:
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(1)[0][0]

def average_word_length(text: str) -> float:
    words = re.findall(r'\w+', text)
    return sum(len(word) for word in words) / len(words)

def longest_and_shortest_words(text: str) -> tuple:
    words = re.findall(r'\w+', text)
    longest = max(words, key=len)
    shortest = min(words, key=len)
    return longest, shortest

def count_unique_words(text: str) -> int:
    words = re.findall(r'\w+', text.lower())
    return sum(1 for word, count in Counter(words).items() if count == 1)

def main():
    filename = "en_resa_genom_svenska_skogen.txt"
    text = read_from_file(filename)
    
    if not text:
        return 
    
    word_count = count_words(text)
    print(f"Antal ord: {word_count}")
    
    frequent_word = most_frequent_word(text)
    print(f"Mest frekventa ord: {frequent_word}")
    
    avg_length = average_word_length(text)
    print(f"Genomsnittlig ordlängd: {avg_length:.2f}")
    
    longest, shortest = longest_and_shortest_words(text)
    print(f"Längsta ordet: {longest}")
    print(f"Kortaste ordet: {shortest}")
    
    unique_count = count_unique_words(text)
    print(f"Antal unika ord: {unique_count}")

if __name__ == "__main__":
    main()