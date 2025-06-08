from cog import BasePredictor, Input
from typing import List
from sentence_transformers import SentenceTransformer


class Predictor(BasePredictor):
    def setup(self):
        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

    def predict(
        self,
        inputs: List[str] = Input(
            description="List of sentences or text segments to embed for semantic search."
        ),
    ) -> List[List[float]]:
        return self.model.encode(inputs, convert_to_numpy=True).tolist()
