from constants import WORD_IGNORE


def is_part_in_list(commit_msg):
    """
    Функция проверяет, есть ли в сообщении коммита слова которые надо игнорировать
    return bool
    """
    for word in WORD_IGNORE:
        if word.lower() in commit_msg.lower():
            return True
    return False
