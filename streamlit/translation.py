import googletrans

def translate(text, src = 'en', tgt = 'ta'):
    
    translator = googletrans.Translator()
    translated = translator.translate(text, src = src, dest = tgt)
    return translated.text
