# Movie and Music Recommendation System 🎬🎵  

This project is a **Streamlit-based web application** designed to provide movie and music recommendations. The app features personalized suggestions, an IMDb TOP 250 list, data visualizations, and analyses based on movie and music datasets.

---

## 📋 Features  

### **1. Movie Recommendation System**  
- **Functionality**: Recommends 10 movies similar to the selected one based on genre, content, and storyline.  
- **Algorithm Used**: FP-Growth.  
- **Dataset**: Cleaned movie dataset (`clean_data.csv`).  

---

### **2. IMDb TOP 250 List**  
- **Functionality**: Displays a curated IMDb TOP 250 list based on IMDb ratings and a minimum of 1000 votes.  
- **Dataset**: `clean_data.csv`.  

---

### **3. Analysis**  
- **Functionality**: Provides visualizations and analyses based on the movie dataset.  
- **Highlights**:  
  - Distribution of ratings by genre.  
  - Number of movies directed by different directors.  
  - Analysis of genres with the highest average ratings.  
- **Code File**: `visual.py`.  

---

### **4. Music Recommendation System**  
- **Functionality**: Provides music recommendations based on genre and the following parameters:  
  - `danceability`  
  - `liveness`  
  - `acousticness`  
  - `speechiness`  
  - `valence`  
  - `tempo`  
- **Algorithm Used**: K-Nearest Neighbors (KNN).  
- **Challenges**: Repeated records in the dataset result in duplicate recommendations.  

---

## 📁 Project Structure  

| **File/Folder**        | **Description**                                                          |
|-------------------------|--------------------------------------------------------------------------|
| `main.py`              | Main script to run the Streamlit app.                                    |
| `clean.ipynb`          | Jupyter notebook for cleaning the movie dataset.                         |
| `clean_data.csv`       | Cleaned movie dataset.                                                   |
| `modal.py`             | Code file for the movie recommendation model.                            |
| `movie_dataset.csv`    | Raw movie dataset.                                                       |
| `musicmodal.py`        | Code file for the music recommendation model.                            |
| `spotify.csv`          | Dataset for the music recommendation system.                             |
| `requirements.txt`     | Python libraries and versions required to run the project.               |
| `visual.py`            | Code for visualizing data from the movie dataset.                        |
| `modal.ipynb`          | Notebook for testing clustering and model algorithms (e.g., KMeans, Agglomerative Clustering). |
| `images/`              | Folder containing screenshots and app-related visualizations.            |

---

## 🔬 Some Model Performances  

### **Movie Recommendation System**  
- **Algorithm**: FP-Growth  

### **Music Recommendation System (Clustering Results)**  
- **Agglomerative Clustering Silhouette Score**: `0.1608`  
- **KMeans Clustering Silhouette Score**: `0.1844`  
- **MiniBatchKMeans Silhouette Score**: `0.3632`  

---

## 💻 Installation Steps  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/project-name.git
   cd project-name
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # For Windows
   ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

4. Install Streamlit (if not already installed):  
   ```bash
   pip install streamlit
   ```

5. Run the application:  
   ```bash
   streamlit run main.py
   ```

---

## 🖼️ Screenshots  

### **1. Movie Recommendation System**  
![Movie Recommendation System](images/movie_recommendation.png)  

### **2. IMDb TOP 250 List**  
![IMDb TOP 250](images/imdb_top_250.png)  

### **3. Data Analysis Visualizations**  
![Data Analysis](images/analysis.png)  

### **4. Music Recommendation System**  
![Music Recommendation System](images/music_recommendation.png)  

---

## 📊 Datasets  

1. **Movie Dataset**: `clean_data.csv`  
2. **Raw Movie Dataset**: `movie_dataset.csv`  
3. **Music Dataset**: `spotify.csv`  

---
