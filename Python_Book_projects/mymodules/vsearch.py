# anotation isn't necessary, and don't affect program behavior


def search4vowels(phrase: str) -> set:
    """Display any vowels, found in a supplied phrase """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns set of letters from 'letters' found in a supplied phrase.
        By default searching for vowels(if second param is not provided)"""
    return set(letters).intersection(set(phrase))
