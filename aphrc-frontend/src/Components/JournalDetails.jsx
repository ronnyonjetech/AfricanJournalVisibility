import React,{useState,useEffect} from 'react'
import { useParams } from 'react-router-dom';
const JournalDetails = () => {
  const { id } = useParams();
  const [article, setArticle] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(`https://africanjournalvisibility.onrender.com/journal_api/api/articles/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setArticle(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, [id]);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  if (!article) return <p>No article found.</p>;
  return (
    <div>
      <h1>{article.title}</h1>
      <p><strong>Volume Number:</strong> {article.volume_number}</p>
      <p><strong>Article Type:</strong> {article.article_type.article_type}</p>
      <p><strong>Authors:</strong> {article.authors}</p>
      <p><strong>Keywords:</strong> {article.keywords}</p>
      <p><strong>Publication Date:</strong> {new Date(article.publication_date).toDateString()}</p>
      <button onClick={() => window.history.back()}>Back to List</button>
    </div>
  )
}

export default JournalDetails