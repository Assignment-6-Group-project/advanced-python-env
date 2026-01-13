import string

def analyze_text(input_file="text.txt", output_file="analysis.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)

    text = " ".join(lines).lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    total_words = len(words)
   
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Total lines: {total_lines}\n")
        f.write(f"Total words: {total_words}\n")
        f.write("Word frequency:\n")
        for word, count in freq.items():
            f.write(f"{word}: {count}\n")

if __name__ == "__main__":
    analyze_text(r"C:\VISUAL STUDIO\ITP\advanced-python-env\week-5\text.txt")