# Case Study 35 : Text Compression Using Character Runs
# Name    : AKKALA LAKSHMI VENKATA SAI
# Roll No : 26000414
#
# Run length encoding: consecutive repeated characters are replaced by the
# character followed by the count.  "AAABB" -> "A3B2"
# The encoded length is compared with the original length to see if the
# compression actually helped.

SAMPLES = [
    "AAAABBBCCDAA",
    "WWWWWWWWWWWWBWWWWWWWWWWWWBBB",
    "ABCDEF",
    "aaAA",
    "zzzzzzzzzzzzzzz",
    "",
    "room 101",
]


def is_valid(text):
    # digits are not allowed because the counts are also digits
    for ch in text:
        if ch.isdigit():
            return False
    return True


def encode(text):
    if text == "":
        return ""
    result = ""
    current = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current:
            count = count + 1
        else:
            result = result + current + str(count)
            current = text[i]
            count = 1
    result = result + current + str(count)   # last run
    return result


def decode(code):
    result = ""
    i = 0
    while i < len(code):
        ch = code[i]
        i = i + 1
        number = ""
        while i < len(code) and code[i].isdigit():
            number = number + code[i]
            i = i + 1
        result = result + ch * int(number)
    return result


def compare(text, code):
    # returns (saving percent, remark)
    if len(text) == 0:
        return 0.0, "empty string - nothing to compress"
    saving = (len(text) - len(code)) * 100 / len(text)
    if len(code) < len(text):
        remark = "beneficial"
    elif len(code) == len(text):
        remark = "no gain"
    else:
        remark = "NOT beneficial (encoded is longer)"
    return saving, remark


def main():
    print("=" * 70)
    print("            TEXT COMPRESSION USING CHARACTER RUNS")
    print("=" * 70)
    beneficial = 0
    not_beneficial = 0
    for text in SAMPLES:
        print(f"Original : '{text}'")
        if not is_valid(text):
            print("  REJECTED: input contains digits, cannot be encoded")
            print("-" * 70)
            continue
        code = encode(text)
        saving, remark = compare(text, code)
        back = decode(code)
        print(f"Encoded  : '{code}'")
        print(f"Length   : {len(text)} -> {len(code)}   saving = {saving:.1f}%   ({remark})")
        if back == text:
            print("Decoded  : matches original")
        else:
            print("Decoded  : MISMATCH")
        if len(text) > 0:
            if len(code) < len(text):
                beneficial = beneficial + 1
            else:
                not_beneficial = not_beneficial + 1
        print("-" * 70)
    print(f"Strings where encoding helped     : {beneficial}")
    print(f"Strings where encoding did not    : {not_beneficial}")


if __name__ == "__main__":
    main()
