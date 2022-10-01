
from twttr2 import shorten

def main():
    test_phrase_lowercase()
    test_phrase_uppercase()
    test_phrase_acentos()

def test_phrase_acentos():
    text = 'onde fui parar NÉ MEU AMIGO ATÉ À VISTA'
    correct = 'nd f prr N M MG T VST'

    try:
        assert shorten(text) == correct
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct}'")


def test_phrase_lowercase():
    text = 'onde fui parar'
    correct = 'nd f prr'

    try:
        assert shorten(text) == correct
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct}'")

def test_phrase_uppercase():
    text = 'oNde fui parar NUNCA FOI MESMO'
    correct = 'Nd f prr NNC F MSM'

    try:
        assert shorten(text) == correct
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct}'")

if __name__ == "__main__":
    main()