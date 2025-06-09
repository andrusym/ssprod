
import joblib
import numpy as np

model = joblib.load('bots/models/strategy_model.pkl')

def score_strategy(features):
    try:
        X = np.array([features[key] for key in sorted(features.keys())]).reshape(1, -1)
        score = model.predict(X)[0]
        return {"score": float(score)}
    except Exception as e:
        return {"error": str(e)}
