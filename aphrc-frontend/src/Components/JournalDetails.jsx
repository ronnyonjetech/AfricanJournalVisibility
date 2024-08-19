import React,{useState,useEffect} from 'react'
import { useParams } from 'react-router-dom';
import "./styles/VolumeAccordion.css"

const JournalDetails = () => {
  const { id } = useParams();
  const [journal, setJournal] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/journal_api/api/journals/${id}`)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        console.log(data)
        setJournal(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, [id]);
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;
  if (!journal) return <p>No journal found.</p>;
  return (
    <div style={{ width: '80%', margin: '0 auto' }}>
      <h1 className="articleTitle">{journal.journal_title}</h1>
      <p className="articleAuthors"> {journal.publishers_name}</p>
      {/* <p><strong>Authors:</strong> {journal.authors}</p> */}
      <p className="articleKeywords"> {journal.thematic_area?journal.thematic_area.thematic_area:"thematic area not specified"}</p>
      <p className="articleDate">Platform-{journal.platform?journal.platform.platform:"platform not specified"}</p>
      <p className="articleDate">ISSN-{journal.issn_number?journal.issn_number:"issn not specified"}</p>
      <p className="articleDate">URL-{journal.link==="nan"?"link not specified": journal.link}</p>
      <p className="articleDate">AIM-{journal.aim_identifier?journal.aim_identifier:"African Index Medicus not specified"}</p>
      {/* <p><strong>Publication Date:</strong> {new Date(journal.publication_date).toDateString()}</p> */}
      {/* <button onClick={() => window.history.back()}>Back to List</button> */}
      
        <button
          onClick={() => window.history.back()}
          style={{
            marginRight: '10px',
            padding: '10px 20px',
            backgroundColor: '#3e6187',
            cursor:  'pointer',
            color: '#fff',
            border: 'none',
            borderRadius: '5px',
            transition: 'background-color 0.3s, opacity 0.3s',
          }}
          onMouseOver={(e) => (e.target.style.backgroundColor = '#3e6187')}
          onMouseOut={(e) => (e.target.style.backgroundColor = '#3e6187')}
        >
          back to list
        </button>  
      </div>
    
  )
}

export default JournalDetails