def words_length(*words: str) -> None:
    for word in words:
        print(len(word))


if __name__ == '__main__':
    words_length("David", "John", "Morgan", "Jeff", "Tim Cook", "Let Tim Cook")
