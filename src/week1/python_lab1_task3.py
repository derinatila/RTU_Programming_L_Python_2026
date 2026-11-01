"""
Task 3 – Function with Combined Logic
-------------------------------------
Write a function `analyze_sentence(text)` that returns a tuple of three values,
in this order:
1. total character count of the text exactly as given, spaces included (len)
2. word count, where words are separated by whitespace (.split())
3. True if "python" appears anywhere in the text, ignoring case, else False
   (a simple substring check: "Pythonic" and "PYTHON!" both count)

Return type: (int, int, bool)

In the main block: read a sentence, call the function, and print a summary.
"""


def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""
    # 1. Toplam karakter sayısı (boşluklar dahil)
    char_count = len(text)

    # 2. Kelime sayısı (varsayılan olarak boşluklardan böler)
    word_count = len(text.split())

    # 3. "python" kelimesi geçiyor mu? (Büyük/küçük harf duyarsız)
    # Metni tamamen küçük harfe çevirip içinde "python" arıyoruz
    contains_python = "python" in text.lower()

    # İstenen sırayla tuple (demet) olarak geri döndür
    return (char_count, word_count, contains_python)


if __name__ == "__main__":
    # Kullanıcıdan cümle al
    sentence = input("Enter a sentence: ")

    # Fonksiyonu çağır ve dönen tuple'ı parçala (unpack)
    chars, words, has_python = analyze_sentence(sentence)

    # Sonuçları yazdır
    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {has_python}")
