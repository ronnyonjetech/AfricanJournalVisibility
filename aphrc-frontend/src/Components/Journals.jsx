import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { FaSearch } from 'react-icons/fa';
import { useNavigate } from 'react-router-dom';

const Journals = () => {
  const [journals, setJournals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const pageSize = 10; 
  const navigate = useNavigate();

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const url = searchQuery
          ? `http://127.0.0.1:8000/journal_api/journals/search/?page=${currentPage}&query=${encodeURIComponent(searchQuery)}`
          : `http://127.0.0.1:8000/journal_api/journals/?page=${currentPage}`;

        const response = await fetch(url, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setJournals(data.results);
        setTotalPages(Math.ceil(data.count / pageSize)); // Calculate total pages
      } catch (error) {
        //navigate('/journals');
        window.location.reload();
        //setError(`Failed to fetch Journals: ${error.message}`);
        //fetchArticles()
      } finally {
        setLoading(false);
      }
    };

    fetchArticles();
  }, [currentPage, searchQuery]);

  const handleSearch = () => {
    setCurrentPage(1); // Reset to first page when performing a new search
  };

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage(currentPage + 1);
    }
    console.log(currentPage)
    console.log( totalPages)
  };

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div style={{ width: '80%', margin: '0 auto' }}>
      <div style={{ textAlign: 'center', marginBottom: '20px' }}>
        <div style={{ position: 'relative', maxWidth: '400px', width: '100%', margin: '0 auto' }}>
          <input
            type="text"
            placeholder="Search for journals..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              padding: '10px',
              paddingRight: '0px',
              width: '100%',
              border: '1px solid #ddd',
              borderRadius: '20px',
              boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
              outline: 'none',
              transition: 'border-color 0.3s',
              fontSize: '16px',
            }}
            onFocus={(e) => (e.target.style.borderColor = '#007BFF')}
            onBlur={(e) => (e.target.style.borderColor = '#ddd')}
          />
          <FaSearch
            onClick={handleSearch}
            style={{
              position: 'absolute',
              right: '15px',
              top: '50%',
              transform: 'translateY(-50%)',
              cursor: 'pointer',
              color: '#888',
              transition: 'color 0.3s',
            }}
            onMouseOver={(e) => (e.target.style.color = '#007BFF')}
            onMouseOut={(e) => (e.target.style.color = '#888')}
          />
        </div>
      </div>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {journals.map((journal) => (
          <li key={journal.id} style={{ padding: '10px', borderBottom: '1px solid #ccc' }}>
            <Link to={`/journal/${journal.id}`} style={{ textDecoration: 'none' }}>
              <h4 className="articleTitle">{journal.journal_title}</h4>
            </Link>
            <p className="articleType">{journal.country ? journal.country.country : "Country not specified"}</p>
            <p className="articleAuthors">{journal.publishers_name ? journal.publishers_name : "Publisher not specified"}</p>
            <p className="articleKeywords">{journal.thematic_area ?journal.thematic_area.thematic_area:"thematic area not specified"}</p>
            {/* <p className="articleVolume">VOL({article.volume_number}) ARTICLE {article.id}</p>
            <p className="articleDate">Publication Date: {new Date(article.publication_date).toDateString()}</p> */}
          </li>
        ))}
      </ul>
      <div style={{ textAlign: 'center', margin: '20px 0' }}>
        <button
          onClick={handlePreviousPage}
          disabled={currentPage === 1}
          style={{
            marginRight: '10px',
            padding: '10px 20px',
            backgroundColor: '#3e6187',
            color: '#fff',
            border: 'none',
            borderRadius: '5px',
            cursor: currentPage === 1 ? 'not-allowed' : 'pointer',
            opacity: currentPage === 1 ? 0.5 : 1,
            transition: 'background-color 0.3s, opacity 0.3s',
          }}
          onMouseOver={(e) => (e.target.style.backgroundColor = '#3e6187')}
          onMouseOut={(e) => (e.target.style.backgroundColor = '#3e6187')}
        >
          Previous
        </button>
        <button
          onClick={handleNextPage}
          disabled={currentPage === totalPages}
          style={{
            padding: '10px 20px',
            backgroundColor: '#3e6187',
            color: '#fff',
            border: 'none',
            borderRadius: '5px',
            cursor: currentPage === totalPages ? 'not-allowed' : 'pointer',
            opacity: currentPage === totalPages ? 0.5 : 1,
            transition: 'background-color 0.3s, opacity 0.3s',
          }}
          onMouseOver={(e) => (e.target.style.backgroundColor = '#3e6187')}
          onMouseOut={(e) => (e.target.style.backgroundColor = '#3e6187')}
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default Journals;
