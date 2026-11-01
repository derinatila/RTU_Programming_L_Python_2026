"""
Task 4 – Text-based Arithmetic Analyzer
---------------------------------------
Create a text-based analyzer made of small helper functions.

Rules used by all functions:
- Words are pieces of text separated by whitespace (use .split()).
- A NUMBER is a word that is a whole integer, optionally with a leading
  minus sign, e.g. "7", "42", "-3".
  Punctuation at the end of a word is ignored, so "5," "10." "8!" count
  as 5, 10 and 8. Use word.rstrip(".,!?;:") to remove it.
  Decimals ("3.5") and mixed words ("abc123") are NOT numbers.
- You do not need the `re` module; .split(), .rstrip() and .isdigit()
  are enough.
"""


def count_characters(text: str) -> int:
    """Count characters that are not whitespace."""
    # Boşluk olmayan karakterleri say (boşlukları filtrele)
    return len("".join(text.split()))


def count_words(text: str) -> int:
    """Count number of whitespace-separated words."""
    return len(text.split())


def extract_numbers(text: str) -> list[int]:
    """Return a list of the integers found in text, in order."""
    numbers = []
    # Kelimelere ayır
    words = text.split()
    for word in words:
        # Kelimenin sonundaki noktalama işaretlerini temizle
        clean_word = word.rstrip(".,!?;:")

        # Sayı olup olmadığını kontrol et (eksi işareti de geçerli)
        # clean_word.lstrip('-') ile baştaki eksiği atıp kalanın rakam olup olmadığına bakıyoruz
        if clean_word.lstrip("-").isdigit():
            numbers.append(int(clean_word))

    return numbers


def analyze_text(text: str) -> dict:
    """Return a dict with characters, words, numbers, sum and average."""
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)

    # Eğer sayı yoksa toplam 0, ortalama 0.0 olmalı
    total_sum = sum(nums)
    if len(nums) > 0:
        average = total_sum / len(nums)
    else:
        average = 0.0

    return {
        "characters": chars,
        "words": words,
        "numbers": nums,
        "sum": total_sum,
        "average": average,
    }


if __name__ == "__main__":
    # Kullanıcıdan metin al
    text_input = input("Enter text: ")

    # Analizi yap
    result = analyze_text(text_input)

    # Sonuçları istenen formatta yazdır
    print(f"Characters (no spaces): {result['characters']}")
    print(f"Words: {result['words']}")
    print(f"Numbers: {result['numbers']}")
    print(f"Sum: {result['sum']}")
    # Ortalamayı 2 ondalık basamakla yazdır
    print(f"Average: {result['average']:.2f}")
