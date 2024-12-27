# Vibely

Vibely is a context-aware music retrieval model that recommends songs based on descriptive "vibes" instead of traditional genre or artist tags. This repository includes the implementation, data files, and supporting materials for training and deploying the model.

---

## Features
- **Context-Aware Retrieval**:
  - Trained on user-generated comments scraped from YouTube, allowing recommendations based on mood, emotions, or specific contextual keywords.

- **Integration with FAISS**:
  - Uses FAISS (Facebook AI Similarity Search) for efficient filtering and indexing of relevant comments, ensuring a high-quality training dataset.

- **Rich Metadata**:
  - Leverages song metadata and listener feedback to improve the precision and context of recommendations.

---

## Files

### 1. `songs_metadata.json`
- **Description**: Contains metadata for each song, including:
  - **Title**: The name of the song.
  - **Artist**: The performer(s) of the song.
  - **Album Name**: The album or collection the song is part of.
  - **View Count**: Number of times the song has been played.
  - **Duration**: The length of the song.
  - **URL**: Link to access the song (e.g., YouTube link).

### 2. `comments_dict.json`
- **Description**: Contains user-generated comments for each song. Each entry corresponds to a particular song and includes YouTube comments, providing:
  - Listener reactions, thoughts, and emotional responses.
  - Context for training the model to identify song "vibes."

---

## Usage

1. **Preprocessing the Data**:
   - Process and clean the metadata and comments to prepare the training dataset:
     ```bash
     python src/preprocess.py --metadata_file data/songs_metadata.json --comments_file data/comments_dict.json
     ```

2. **Training the Model**:
   - Train the music retrieval model using the cleaned dataset:
     ```bash
     python src/train.py
     ```

3. **Using the Retrieval System**:
   - Query the system for recommendations based on descriptive keywords:
     ```bash
     python src/search.py --query "uplifting summer vibes"
     ```

---

## Future Work
- **Enhanced Data Sources**: Include user comments from other platforms to diversify the dataset.
- **Advanced Embeddings**: Experiment with more sophisticated embedding models to capture nuanced song descriptions.
- **Web Deployment**: Deploy the system as an interactive web application for real-world usage.

---

## Contact
For questions, contributions, or collaborations, feel free to open an issue in the repository or reach out directly.
