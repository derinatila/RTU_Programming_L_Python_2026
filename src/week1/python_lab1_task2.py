"""
Task 2 – Greeting Function with String Manipulation
---------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces at the start and end with .strip()
- capitalizes the first letter with .capitalize()
  (note: .capitalize() also makes the REST of the string lowercase)
- returns exactly: "Hello, <Name>! Welcome to Python!"
- if the name is empty (or only spaces), uses "Stranger" as the name

In the main block: ask the user for their name and print the greeting.
"""


def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    # 1. Baş ve sondaki boşlukları temizle
    clean_name = name.strip()

    # 2. Eğer isim boş kaldıysa "Stranger" ata
    if not clean_name:
        clean_name = "Stranger"
    else:
        # 3. İlk harfi büyüt, geri kalanını küçült
        clean_name = clean_name.capitalize()

    # 4. İstenen formatta geri döndür
    return f"Hello, {clean_name}! Welcome to Python!"


if __name__ == "__main__":
    # Kullanıcıdan girdi al
    user_name = input("Enter your name: ")

    # Fonksiyonu çağır ve sonucu yazdır
    greeting = greet_user(user_name)
    print(greeting)
