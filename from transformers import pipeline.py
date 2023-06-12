from transformers import pipeline
pipe = pipeline('translation',model='helsinki-nlp/opus-mt-tc-big-en-ko')
print(pipe(text))