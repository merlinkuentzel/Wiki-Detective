import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="WikiDetective/1.0 (educational project)",
    language="de"
)

def wiki_article(theme):
    themen_quiz = wiki.page(theme)
    clean_sentences = []

    sentences = themen_quiz.text.split(".")
    for sentence in sentences:
        if theme not in sentence:
            if sentence.strip():
                sentence = sentence.strip()
                clean_sentences.append(sentence)
    return clean_sentences


