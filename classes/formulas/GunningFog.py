import re
from classes.formulas.Formula import Formula

class GunningFog(Formula):
    def _count_complex_words(self):
        # Считаем слова с тремя и более слогами
        complex_words = 0
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
                complex_words += 1
        return complex_words

    def calculate(self):
        if self.sentences == 0 or self.words == 0:
            return None  # Исключение деления на ноль
        complex_words = self._count_complex_words()
        fog_index = 0.4 * ((self.words / self.sentences) + (complex_words / self.words) * 100)
        return round(fog_index, 2)