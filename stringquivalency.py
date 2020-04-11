# given two strings, return if they are equivalent when typed into input field
# the hash represents a backspace
# S and T contain only lowercase letters and hash characters
# length of S and T are between 1-200 (inclusive)

def string_compare(s, t):
    """returns true or false depending on equivalency of strings"""

    s_clean = string_cleaning(s)
    t_clean = string_cleaning(t)

    if s_clean == t_clean:
        return True
    else:
        return False


def string_cleaning(to_clean):
    """parses the string and removes backspaces and backspaced chars"""

    cleaned = []
    for char in to_clean:
        if char == '#':
            if len(cleaned) == 0:
                continue
            else:
                cleaned.pop()
        else:
            cleaned.append(char)
    final_str = ''

    return (final_str.join(cleaned))
