from gensim.models import Word2Vec
from classes.handlers.StopWordsHandler import StopWordsHandler

class ContextualAnalysis:
    def __init__(self, text):
        self.text = text
        self.stop_words_handler = StopWordsHandler()
        self.model = self._train_model()  # Инициализация модели

    def _train_model(self):
        sentences = []
        for sentence in self.text.split('\n'):
            words = [
                word.lower().strip('.,!?;()[]')
                for word in sentence.split()
                if (
                    not self.stop_words_handler.is_stop_word(word.strip('.,!?;()[]'))
                    and len(word.strip('.,!?;()[]')) > 1
                    and not word.isdigit()
                )
            ]
            if words:
                sentences.append(words)
        
        model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
        return model

    def get_relevant_terms(self, term, topn=5):
        """Возвращает список наиболее значимых терминов для указанного термина."""
        if term in self.model.wv.key_to_index:
            return self.model.wv.most_similar(term, topn=topn)
        else:
            return None