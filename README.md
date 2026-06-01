# 📚 Book Search Aggregator
I've developed a web app that searches multiple book databases at once, bringing together results from **Google Books** and **Open Library** in one place in order to increase efficiency when looking up books without having to manually sift through multiple sites.

## Live Demo
https://book-search-app-static.onrender.com

## Tech Stack
- **Frontend:** React, Vite
- **Backend:** Flask, Python
- **APIs:** Google Books API, Open Library API

## Running it locally

**Backend**
```bash
cd public/backend
pip install flask flask-cors requests gunicorn
python app.py
```

**Frontend**
```bash
npm install
npm run dev
```

Then open http://localhost:5174/ 

## Features
- Search by title or title + author
- Results from multiple sources in one view
- Caches repeated searches to avoid API rate limits
- Links to full book info for each result

<img width="1470" height="956" alt="Screenshot 2026-05-31 at 10 39 00 PM" src="https://github.com/user-attachments/assets/1fe6d762-17d3-4b23-a903-8986d46483e9" />
