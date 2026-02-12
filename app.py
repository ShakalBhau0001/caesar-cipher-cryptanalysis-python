def caesar_shift(text, shift, direction):
    result = ""
    # Direction Shifting
    if direction == "L":
        shift = -shift
    elif direction == "R":
        pass
    else:
        return ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def english_score(text):
    freq_bonus = "ETAOIN SHRDLU"
    score = 0

    for ch in text.upper():
        if ch in freq_bonus:
            score += 2
        elif ch.isalpha():
            score += 1
        elif ch == " ":
            score += 3
        else:
            score -= 1

    return score


def brute_force_caesar(cipher_text):
    results = []
    seen_texts = set()  # preventing from mirror duplication

    for shift in range(1, 26):
        for direction in ["L", "R"]:

            plaintext = caesar_shift(cipher_text, shift, direction)

            # Avoiding duplicate mirror results
            if plaintext in seen_texts:
                continue

            seen_texts.add(plaintext)

            score = english_score(plaintext)
            results.append((score, shift, direction, plaintext))

    # Ranking by score
    results.sort(reverse=True)
    return results


print("\n--- Caesar Cipher Brute Force ---\n")
cipher = input("Enter Caesar cipher text: ")
ranked_results = brute_force_caesar(cipher)
print("\nTop Possible Plaintexts:\n")
for score, shift, direction, text in ranked_results[:5]:
    print(f"Shift {shift:2d} | Dir {direction} | Score {score:3d} | {text}")
