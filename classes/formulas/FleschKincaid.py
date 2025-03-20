from classes.formulas.Formula import Formula

class FleschKincaid(Formula):
    def calculate(self):
        if self.sentences == 0 or self.words == 0:
            return None  # Исключение деления на ноль
        fk_grade_level = (0.39 * (self.words / self.sentences)) + (11.8 * (self.syllables / self.words)) - 15.59
        return round(fk_grade_level, 2)