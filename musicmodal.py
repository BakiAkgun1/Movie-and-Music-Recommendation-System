import streamlit as st  # type: ignore
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score

def musicmodal1():
    df = pd.read_csv('spotify.csv')
    df = df.dropna()

    # Özellikler
    features = ['danceability', 'liveness', 'acousticness', 'speechiness', 'valence', 'tempo']
    X = df[features]

    # KNN modelini tanımla
    knn = NearestNeighbors(n_neighbors=10)

    # Başlık
    st.title("Müzik Öneri Sistemi")

    # Şarkı seçimi
    track_options = df['track_name'].tolist()  # Şarkı isimlerini listele
    selected_track = st.selectbox("Bir şarkı seçin:", track_options)

    # Seçilen şarkının özelliklerini al
    selected_track_df = df[df['track_name'] == selected_track]

    if not selected_track_df.empty:
        # Seçilen şarkının türü
        selected_genre = selected_track_df['track_genre'].values[0]

        # Aynı türe sahip şarkıları filtrele
        df_same_genre = df[df['track_genre'] == selected_genre]

        if len(df_same_genre) < 10:
            st.write(f"Bu türde yeterli şarkı bulunamadı. Sadece {len(df_same_genre)} şarkı mevcut.")
            return

        X_same_genre = df_same_genre[features]

        # Seçilen şarkının özellikleri
        user_input = selected_track_df[features].values

        # KNN modelini aynı türe sahip şarkılar üzerinde eğit
        knn.fit(X_same_genre)

        # Önerileri al
        distances, indices = knn.kneighbors(user_input)

        # Önerilen şarkıları al
        recommendations = df_same_genre.iloc[indices[0]]

        # Mesafeleri göster
        distance_df = pd.DataFrame(distances.flatten(), columns=['Distance'])
        recommendations = pd.concat([recommendations.reset_index(drop=True), distance_df], axis=1)

        # Önerilen şarkıları göster (10 öneri)
        st.write(f"Önerilen Şarkılar ({selected_genre}):")
        st.dataframe(recommendations[['track_name', 'album_name', 'artists', 'Distance', 'track_genre']])


        silhouette_avg = silhouette_score(X_same_genre, knn.kneighbors(user_input)[1])
        st.write(f"Silhouette Skoru: {silhouette_avg:.2f}")