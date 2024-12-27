# Vibely: Context-Aware Music Retrieval

Vibely is a context-aware music retrieval project that uses user-generated comments and song metadata to recommend tracks based on descriptive "vibes" rather than traditional genre or artist tags. This repository includes the core implementation, data files, and supporting materials.

---

## Features
- **Context-Aware Retrieval**:
  Uses YouTube comments and metadata to capture emotional and contextual descriptions of songs.
- **Efficient Filtering**:
  Integrates FAISS (Facebook AI Similarity Search) to filter irrelevant data and improve search efficiency.
- **Rich Metadata**:
  Provides detailed song information including title, artist, album, duration, and view count.

---

## Files

### 1. `ArtistList.txt`
- **Description**: Contains a list of artists featured in the music database.
- **Purpose**: Provides a reference for artist-based filtering and querying.

### 2. `ArtistStatus.json`
- **Description**: Tracks the active/inactive status of the listed artists.
- **Purpose**: Helps determine the availability of songs by specific artists.

### 3. `comments.json`
- **Description**: Includes user-generated comments for various songs, capturing listener reactions and emotional responses.
- **Purpose**: Used as training data for understanding song "vibes."

### 4. `SongCollection.json`
- **Description**: Stores user feedback on songs, including individual comment threads.
- **Purpose**: Provides additional insights for analyzing audience engagement.

### 5. `SongInfo.json`
- **Description**: Contains detailed metadata for each song, including:
  - **Title**
  - **Artist**
  - **Album Name**
  - **View Count**
  - **Duration**
  - **YouTube URL**
- **Purpose**: Serves as the primary dataset for song metadata.

---

## Code Files

### 1. `Collector.py`
- **Description**: Handles data collection, including scraping and processing YouTube comments and metadata.
- **Purpose**: Automates the data acquisition process.

### 2. `Comment.py`
- **Description**: Processes and structures comments for training and analysis.
- **Purpose**: Ensures the comments are cleaned and ready for integration into the model.

### 3. `Scraper.py`
- **Description**: Custom scraper for retrieving YouTube metadata and comments.
- **Purpose**: Fetches additional details not included in the original dataset.

---

## Usage

1. **Data Preparation**:
   - Use `Collector.py` and `Scraper.py` to fetch and preprocess data.

2. **Analysis**:
   - Analyze user comments and song metadata using `Comment.py`.

3. **Integration**:
   - Use the processed data for model training and retrieval system development.

---

## Contact
For questions or collaboration, please open an issue in the repository or reach out directly.

