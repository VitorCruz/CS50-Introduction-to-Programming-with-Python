
import emoji as em

def main():
    emoji_str = input("Your emoji in a string: ")
    print(em.emojize(f"Converting that string to emoji: {emoji_str}"))

if __name__ == "__main__":
    main()