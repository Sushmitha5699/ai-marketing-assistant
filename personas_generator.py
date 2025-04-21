import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def generate_personas(dataframe, k):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(dataframe['review'])

    kmeans = KMeans(n_clusters=k, random_state=42)
    dataframe['cluster'] = kmeans.fit_predict(X)

    terms = vectorizer.get_feature_names_out()
    personas = []

    for cluster_num in range(k):
        cluster_reviews = dataframe[dataframe['cluster'] == cluster_num]['review']
        center = kmeans.cluster_centers_[cluster_num]
        top_indices = center.argsort()[::-1][:5]
        top_words = [terms[i] for i in top_indices]

        body_text = " ".join(cluster_reviews.sample(min(2, len(cluster_reviews)), random_state=1).values)

        personas.append({
            "persona": f"Persona {cluster_num+1}",
            "keywords": top_words,
            "hook": f"Unlock beauty with {top_words[0].capitalize()} ✨",
            "body": body_text,
            "cta": "Try GlowGen now!"
        })

    return personas
