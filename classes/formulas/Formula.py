import re

# Родительский класс Formula
class Formula:
    def __init__(self, text):
        self.text = text
        self.sentences = self._count_sentences()
        self.words = self._count_words()
        self.syllables = self._count_syllables()

    def _tokenize(self, text):
        return re.findall(r'\b\w+\b', text.lower())

    def _count_sentences(self):
        # Считаем предложения по наличию точек, восклицательных и вопросительных знаков
        sentence_endings = re.compile(r'[.!?]')
        sentences = sentence_endings.split(self.text)
        return len([s for s in sentences if len(s.strip()) > 0])
    
    def _count_words(self):
        # Считаем слова
        words = re.findall(r'\b\w+\b', self.text)
        return len(words)
    
    def _count_syllables(self):
        # Примерное вычисление слогов на основе простых правил
        vowels = 'aeiouy'
        syllable_count = 0
        for word in re.findall(r'\b\w+\b', self.text.lower()):
            word_syllables = 0
            if word[0] in vowels:
                word_syllables += 1
            for i in range(1, len(word)):
                if word[i] in vowels and word[i-1] not in vowels:
                    word_syllables += 1
            if word.endswith('e'):
                word_syllables = max(1, word_syllables - 1)
            syllable_count += max(1, word_syllables)
        return syllable_count

    def _count_syllables(self):
        # Примерное вычисление слогов на основе простых правил
        vowels = 'aeiouy'
        syllable_count = 0
        for word in re.findall(r'\b\w+\b', self.text.lower()):
            word_syllables = 0
            if word[0] in vowels:
                word_syllables += 1
            for i in range(1, len(word)):
                if word[i] in vowels and word[i-1] not in vowels:
                    word_syllables += 1
            if word.endswith('e'):
                word_syllables = max(1, word_syllables - 1)
            syllable_count += max(1, word_syllables)
        return syllable_count

    def calculate(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе.")