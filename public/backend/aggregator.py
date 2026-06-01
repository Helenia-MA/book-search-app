import requests
from functools import lru_cache


# GOOGLE BOOKS API
@lru_cache(maxsize=128)
def cached_google_books_search(title, author=""):
    query = f"{title}"
    if author:
        query += f"+inauthor:{author}"

    response = requests.get(
        "https://www.googleapis.com/books/v1/volumes",
        params={"q": query}
    )
    response.raise_for_status()

    return response.json()

def search_google_books(title, author=""):
    try:
        return cached_google_books_search(title, author)
    except requests.RequestException as e:
        if e.response.status_code == 429:
            print("Google Books API rate limit exceeded.")
            return {"items": []}
        raise

# OPEN LIBRARY API
@lru_cache(maxsize=128)
def cached_open_library_search(title, author=""):
    params = {"title": title}

    if author:
        params["author"] = author

    response = requests.get(
        "https://openlibrary.org/search.json",
        params= params
    )
    response.raise_for_status()

    return response.json()


def search_open_library(title, author=""):
    try:
        return cached_open_library_search(title, author)
    except requests.RequestException as e:
        if e.response.status_code == 429:
            print("Open Library API rate limit exceeded.")
            return {"docs": []}
        raise

def combine_data(g_results, o_results):
    combined = []
    if g_results:
        for item in g_results.get("items", []):
            volume_info = item.get("volumeInfo", {})
            authors = volume_info.get("authors") or ["N/A"]
            combined.append({
                "source": "Google Books",
                "title": volume_info.get("title", "N/A"),
                "authors": authors[0],
                "link": volume_info.get("infoLink", "N/A"),
                "image": volume_info.get("imageLinks", {}).get("thumbnail", ""),
            })

    if o_results:
        for doc in o_results.get("docs", []):
            image = None
            if "cover_i" in doc:
                image = (f"http://covers.openlibrary.org/b/id/"
                         f"{doc['cover_i']}-M.jpg")
            authors = doc.get("author_name") or ["N/A"]
            combined.append({
                "source": "Open Library",
                "title": doc.get("title", "N/A"),
                "authors": authors[0],
                "link": f"https://openlibrary.org{doc.get('key', '')}",
                "image": image,
            })

    return combined