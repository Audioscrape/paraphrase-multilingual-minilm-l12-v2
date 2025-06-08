# paraphrase-multilingual-minilm-l12-v2

This is a [Cog](https://replicate.com/docs/guides/push-a-model) wrapper for the [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) model, published by [AudioScrape](https://audioscrape.com).

It generates 384-dimensional multilingual sentence embeddings optimized for semantic search across more than 50 languages.

This model is used by [audioscrape.com](https://audioscrape.com) to power fast and accurate audio transcription search in multiple languages.

## ✨ Example

```bash
cog predict -i inputs='["hello world", "hola mundo", "bonjour le monde"]'
```

## 📘 Model Details

Name: paraphrase-multilingual-MiniLM-L12-v2

Source: Hugging Face

Embedding size: 384 dimensions

Supported languages: 50+

Use case: Multilingual sentence embeddings for semantic search

## 🔗 Attribution & License

Original model by SBERT.net

Licensed under Apache 2.0

This wrapper is maintained by AudioScrape

