
def count_valid_words(phrases):
    return sum(1 for p in phrases if is_valid_passphrase(p))

def is_valid_passphrase(passphrase):
    words = set()
    for word in passphrase.split():
        word = word.strip()
        if word in words:
            return False
        words.add(word)
    return True



if __name__ == '__main__':
    with open('input.txt') as f:
        print(count_valid_words(f))