import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function Header() {
  const book_img = "src/assets/library-icon.jpg"
  return (
    <header className="heading">
      <img id="book-icon" src={book_img} width="60px" alt="Book Icon" />
      <h1> Book Search Aggregator</h1>
    </header>
  );
}

function SubHeading() {
  return (
    <div className="sub-header">
      <h2>Welcome to the Book Search Aggregator!</h2>
      <p><i>Discover your next great read with our powerful book search aggregator. We bring together results from multiple sources, including Google Books and Open Library, to provide you with a comprehensive selection of books. Whether you're looking for the latest bestsellers, classic literature, or hidden gems, our aggregator makes it easy to find the perfect book for you. Explore a world of books at your fingertips!</i></p>
    </div>
  )
}

function SearchForm() {
  const [title, setTitle] = useState("")
  const [author, setAuthor] = useState("")
  const [results, setResults] = useState([])
  const API_URL =  import.meta.env.VITE_API_URL || "http://127.0.0.1:5000"

  async function handleSubmit(e) {
    e.preventDefault()
    try{
      const response = await fetch(
        `${API_URL}/api/search?title=${encodeURIComponent(title)}&author=${encodeURIComponent(author)}`
      )
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      console.log(data);
      setResults(data)

    } catch (error) {
      console.error("Error fetching book data:", error)
    }
  }

  return (
    <>
    <form className="search-form" onSubmit={handleSubmit}>
        <input type="text" placeholder="enter book title"
               value={title} onChange={(e) => setTitle(e.target.value)} />

        <input type="text" placeholder="enter author name (optional)"
               value={author} onChange={(e) => setAuthor(e.target.value)} />
        <button type="submit">Search</button>
    </form>

    <section className="results">
      {results.map((book, index) => (
        <div className="book-card" key={index}>
          {book.image && <img src={book.image} alt={`${book.title} cover`} />}
          <h3>{book.title}</h3>
          <p>{book.authors}</p>
          <p>{book.source}</p>
          <a href={book.link} target="_blank" rel="noreferrer">View Book</a>
        </div>
      ))}
    </section>
    </>
  )
}

function App() {
  return (
    <div className="App">
      <Header />
      <SubHeading />
      <SearchForm />
    </div>
  )
}

export default App
