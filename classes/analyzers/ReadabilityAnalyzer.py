# readability.py
from classes.formulas.FleschKincaid import FleschKincaid
from classes.formulas.SMOG import SMOG
from classes.formulas.GunningFog import GunningFog
from classes.formulas.DaleChall import DaleChall

class ReadabilityAnalyzer:
    def __init__(self, text):
        self.text = text

    def analyze(self):
        """Выполняет анализ читаемости текста и возвращает результаты."""
        fk = FleschKincaid(self.text)
        grade_level = fk.calculate()

        smog = SMOG(self.text)
        smog_grade = smog.calculate()

        gf = GunningFog(self.text)
        fog_index = gf.calculate()

        dc = DaleChall(self.text)
        dale_chall_score = dc.calculate()

        return grade_level, smog_grade, fog_index, dale_chall_score

    def save_results_to_csv(self, filename='readability_scores.csv'):
        """Сохраняет результаты читаемости в CSV."""
        results = self.analyze()
        readability_data = [
            ["Metric", "Value"],
            ["Flesch-Kincaid Grade Level", results[0]],
            ["SMOG Grade", results[1]],
            ["Gunning Fog Index", results[2]],
            ["Dale-Chall Score", results[3]]
        ]
        self._save_to_csv(readability_data, filename)

    @staticmethod
    def _save_to_csv(data, filename):
        """Сохраняет данные в CSV-файл."""
        import csv
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
