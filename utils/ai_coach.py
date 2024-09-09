from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Dummy data for demonstration
tips = [
    "Take short breaks between classes to recharge.",
    "Use positive reinforcement to motivate students.",
    "Implement a mindfulness practice in your daily routine.",
    "Collaborate with colleagues to share teaching strategies.",
    "Set realistic goals for yourself and your students.",
]

vectorizer = TfidfVectorizer()
tip_vectors = vectorizer.fit_transform(tips)

def get_daily_tips(user):
    # In a real-world scenario, we would use more sophisticated ML models
    # and consider user preferences, behavior, and historical data
    user_profile = f"{user.username} {' '.join(user.badges)}"
    user_vector = vectorizer.transform([user_profile])
    
    similarities = cosine_similarity(user_vector, tip_vectors)
    top_tip_idx = np.argmax(similarities)
    
    return tips[top_tip_idx]
