import math
import re
from classes.formulas.Formula import Formula

class SMOG(Formula):
    def _count_polysyllabic_words(self):
        # Считаем слова с тремя и более слогами
        polysyllabic_words = 0
        for word in re.findall(r'\b\w+\b', self.text.lower()):
            syllables = 0
            if word[0] in 'aeiouy':
                syllables += 1
            for i in range(1, len(word)):
                if word[i] in 'aeiouy' and word[i-1] not in 'aeiouy':
                    syllables += 1
            if word.endswith('e'):
                syllables = max(1, syllables - 1)
            if syllables >= 3:
                polysyllabic_words += 1
        return polysyllabic_words
    
    def calculate(self):
        if self.sentences == 0:
            return None  # Исключение деления на ноль
        polysyllabic_words = self._count_polysyllabic_words()
        smog_grade = 1.0430 * math.sqrt(polysyllabic_words * (30 / self.sentences)) + 3.1291
        return round(smog_grade, 2)