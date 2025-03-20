class StopWordsHandler:
    def __init__(self, base_path='data/stopwords'):
        self.base_path = base_path
        self.stop_words = set()
        self._load_stop_words()

    def _load_stop_words(self):
        """Загружает стоп-слова из всех файлов в директории"""
        files = ['english.txt']
        
        for filename in files:
            file_path = f"{self.base_path}/{filename}"
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Читаем слова, пропуская пустые строки и комментарии
                    words = {
                        word.strip().lower() 
                        for word in file.readlines() 
                        if word.strip() and not word.startswith('#')
                    }
                    self.stop_words.update(words)
            except FileNotFoundError:
                print(f"Warning: Stop words file not found: {file_path}")

    def is_stop_word(self, word):
        """Проверяет, является ли слово стоп-словом"""
        return word.lower() in self.stop_words

    def get_stop_words(self):
        """Возвращает множество всех стоп-слов"""
        return self.stop_words