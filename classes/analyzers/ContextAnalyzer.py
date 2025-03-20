# context_analysis.py
from classes.formulas.contextual.ContextualAnalysis import ContextualAnalysis

class ContextAnalyzer:
    def __init__(self, text, term='Laravel', topn=5):
        self.text = text
        self.term = term
        self.topn = topn

    def analyze(self):
        """Выполняет контекстный анализ и возвращает релевантные термины."""
        context_analysis = ContextualAnalysis(self.text)
        relevant_terms = context_analysis.get_relevant_terms(self.term, self.topn)
        
        # Проверка на None перед обработкой
        if relevant_terms is None:
            return f"Термин '{self.term}' не найден в тексте"
    
        return " ".join([term[0] for term in relevant_terms])

    def calculate_tfidf(self):
        """Вычисляет TF-IDF для заданных релевантных терминов."""
        relevant_terms = self.analyze()
        from classes.formulas.TFIDF import TFIDF
        tfidf = TFIDF(self.text, self.text, relevant_terms)
        return tfidf.calculate()

    def save_tfidf_to_csv(self, filename='tfidf_scores.csv'):
        """Сохраняет TF-IDF данные в CSV."""
        tfidf_scores = self.calculate_tfidf()
        tfidf_data = [["Term", "TF-IDF Score"]]
        for term, score in tfidf_scores.items():
            tfidf_data.append([term, score])
        self._save_to_csv(tfidf_data, filename)

    @staticmethod
    def _save_to_csv(data, filename):
        """Сохраняет данные в CSV-файл."""
        import csv
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)