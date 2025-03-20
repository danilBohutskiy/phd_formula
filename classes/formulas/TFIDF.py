import math
from collections import defaultdict
from classes.formulas.Formula import Formula
from classes.handlers.StopWordsHandler import StopWordsHandler

class TFIDF(Formula):
    def __init__(self, corpus_text, text, relevant_terms=None):
        super().__init__(text)

        # Инициализируем обработчик стоп-слов
        self.stop_words_handler = StopWordsHandler()

        self.corpus = corpus_text.strip().split('\n')
        self.documents = [self._tokenize(doc) for doc in self.corpus]
        self.document_count = len(self.corpus)
        self.term_document_occurrences = self._calculate_term_document_occurrences()
        self.relevant_terms = relevant_terms.split() if relevant_terms is not None else []

    def _calculate_term_document_occurrences(self):
        occurrences = defaultdict(int)
        for doc in self.documents:
            unique_terms = set(doc)
            for term in unique_terms:
                occurrences[term] += 1
        return occurrences
    
    def _term_frequency(self, term):
        words = self._tokenize(self.text)
        return words.count(term) / len(words) if words else 0
    
    def _inverse_document_frequency(self, term):
        if term not in self.term_document_occurrences:
            return 0
        return math.log(self.document_count / (1 + self.term_document_occurrences[term]))

    def calculate(self):
        tfidf_scores = {}
        for term in self.relevant_terms:
            tf = self._term_frequency(term)
            idf = self._inverse_document_frequency(term)
            tfidf_scores[term] = round(tf * idf, 5)
            #print(f"Term: {term}, TF: {tf}, IDF: {idf}, TF-IDF: {tfidf_scores[term]}")  # Отладочный вывод
        return tfidf_scores

    def _tokenize(self, text):
            """Разбивает текст на слова и очищает от стоп-слов"""
            words = text.lower().split()
            cleaned_words = [
                word.strip('.,!?;()[]')
                for word in words
                if (
                    not self.stop_words_handler.is_stop_word(word.strip('.,!?;()[]'))
                    and len(word.strip('.,!?;()[]')) > 1
                    and not word.isdigit()
                )
            ]
            return cleaned_words
