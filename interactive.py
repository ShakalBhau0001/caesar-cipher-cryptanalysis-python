from rich.console import Console
from rich.panel import Panel

console = Console()


def caesar_shift(text, shift, direction):
    result = ""
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
    seen_texts = set()

    for shift in range(1, 26):
        for direction in ["L", "R"]:
            plaintext = caesar_shift(cipher_text, shift, direction)

            if plaintext in seen_texts:
                continue

            seen_texts.add(plaintext)
            score = english_score(plaintext)
            results.append((score, shift, direction, plaintext))

    results.sort(reverse=True)
    return results


console.print(
    Panel.fit(
        "[bold cyan]🔓 Caesar Cipher Brute Force[/bold cyan]", border_style="cyan"
    )
)

cipher = console.input("\n[bold yellow]Enter Caesar cipher text:[/bold yellow] ")
ranked_results = brute_force_caesar(cipher)
console.print("\n[bold green]Top Possible Plaintexts:[/bold green]\n")
for score, shift, direction, text in ranked_results[:5]:
    console.print(f"Shift {shift:2d} | Dir {direction} | Score {score:3d} | {text}")
