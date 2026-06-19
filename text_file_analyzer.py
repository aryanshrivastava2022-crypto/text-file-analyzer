from collections import Counter

file_name = input("Enter text file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    words = content.split()

    print("\n📊 Text File Analysis")
    print(f"Characters: {len(content)}")
    print(f"Words: {len(words)}")
    print(f"Lines: {content.count(chr(10)) + 1}")

    word_count = Counter(words)

    print("\n🔝 Top 5 Most Frequent Words:")
    for word, count in word_count.most_common(5):
        print(f"{word}: {count}")

except FileNotFoundError:
    print("❌ File not found.")
