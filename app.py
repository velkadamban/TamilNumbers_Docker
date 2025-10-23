from Tamilnumbers import tamilnum, tamilnum_traditional

def main():
    print("தமிழ் எண் மாற்றி (Tamil Number Converter)")

    # சரியான எண் உள்ளிடும் வரை முறை தொடர்தல்
    while True:
        number = input("எண்ணை உள்ளிடுக (Enter a number): ").strip()
        if number.lstrip('-').isdigit():
            break
        print("தவறான உள்ளீடு. தொகுவெண்ணை மட்டுமே உள்ளிடுக (Enter only Integer)")  # Invalid input message

    # சரியான தேர்வு செய்யும் வரை முறை தொடர்தல்
    while True:
        print("தேர்வு செய்க (Choose conversion type):")
        print("1. நவீன தமிழ் எண் (Modern Tamil numeral)")
        print("2. மரபுத் தமிழ் எண் (Traditional Tamil numeral)")
        choice = input("உங்கள் தேர்வு (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("தவறான தேர்வு! 1 அல்லது 2 ஐத் தேர்வு செய்க (Invalid! Select either 1 or 2)")  # Invalid choice message

    # மாற்றத்தைச் செயல்படுத்துதல்
    if choice == '1':
        result = tamilnum(number)
    else:
        result = tamilnum_traditional(number)

    # முடிவுகளை காட்சி செய்தல்
    print(f"உங்கள் உள்ளீடு: {number}")
    print(f"தமிழ் எண்: {result}")


if __name__ == "__main__":
    main()
