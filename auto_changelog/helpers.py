def is_part_in_list(commit_msg, ignore):
    """
    Функция проверяет, есть ли в сообщении коммита слова которые надо игнорировать
    commit_msg: сообщение коммита
    ignore: str аргументы параметра --ignore
    return bool
    """
    ignore = ignore.split()
    for word in ignore:
        if word.lower() in commit_msg.lower():
            return True
    return False

