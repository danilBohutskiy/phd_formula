import argparse
from classes.analyzers.ReadabilityAnalyzer import ReadabilityAnalyzer
from classes.analyzers.ContextAnalyzer import ContextAnalyzer

def read_text_from_file(filename='text.txt'):
    """Читает текст из указанного файла."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main(term='', topn=50):
    text = read_text_from_file()

    # Анализ читаемости
    readability_analyzer = ReadabilityAnalyzer(text)
    readability_analyzer.save_results_to_csv()

    # Анализ контекста, Вычисление TF-IDF
    context_analyzer = ContextAnalyzer(text, term, topn)
    context_analyzer.save_tfidf_to_csv()

    print("CSV saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Analyze text and calculate readability and TF-IDF scores.')
    parser.add_argument('--term', type=str, default='request', help='The term for context analysis')
    parser.add_argument('--topn', type=int, default=5, help='The number of relevant terms to retrieve')

    args = parser.parse_args()
    print(args.term)
    print(args.topn)

    main(args.term, args.topn)