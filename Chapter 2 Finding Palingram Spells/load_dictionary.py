"""Load a text as a list."""

import sys


def load(file: str) -> list:
    """
    Load a text file and return a list of all words in lowercase.

    :param file: (str): The name of the text file (including directory path if needed).

    Exceptions:
        IOError: If the file cannot be opened.

    :return: list: A list of all words in the text file in lowercase.

    Requires:
        import sys
    """
    try:
        with open(file, encoding='utf-8') as f:
            text = f.read().split()
            txt = [x.lower() for x in text]
            return txt
    except OSError as e:
        print(f'{e}\nError opening {file}. Terminating program.',
              file=sys.stderr)
        sys.exit(1)
