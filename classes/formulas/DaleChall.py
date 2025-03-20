from classes.formulas.Formula import Formula
import re

class DaleChall(Formula):
    # Заранее определённый список простых слов на английском
    simple_words_list = set([
        # Пример базовых слов. Полный список нужно подгружать из файла или базы.
        "a", "about", "after", "again", "all", "almost", "also", "always", "am", "an", "and", "any",
        "are", "as", "at", "be", "been", "but", "by", "can", "did", "do", "does", "down", "even", "for",
        "from", "get", "go", "had", "has", "have", "he", "her", "him", "his", "how", "if", "in", "into", 
        "is", "it", "just", "like", "look", "make", "many", "me", "my", "new", "no", "not", "now", "of", 
        "on", "one", "only", "or", "other", "our", "out", "over", "said", "see", "she", "so", "some", 
        "than", "that", "the", "their", "them", "then", "there", "these", "they", "this", "to", "up", 
        "use", "was", "we", "what", "when", "which", "who", "will", "with", "would", "you", "your"
    ])
    
    def _count_difficult_words(self):
        # Считаем сложные слова, которые не входят в список простых слов
        difficult_words = 0
        for word in re.findall(r'\b\w+\b', self.text.lower()):
            if word not in self.simple_words_list:
                difficult_words += 1
        return difficult_words

    def calculate(self):
        if self.sentences == 0 or self.words == 0:
            return None  # Исключение деления на ноль
        difficult_words = self._count_difficult_words()
        difficult_word_percentage = (difficult_words / self.words) * 100
        score = 0.1579 * difficult_word_percentage + 0.0496 * (self.words / self.sentences)
        if difficult_word_percentage > 5:
            score += 3.6365
        return round(score, 2)

# Пример использования

