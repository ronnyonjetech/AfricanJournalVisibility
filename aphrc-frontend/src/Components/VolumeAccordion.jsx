import React, { useState } from 'react';
import { Link } from 'react-router-dom'
import './styles/VolumeAccordion.css'
import { CgMoreVertical } from "react-icons/cg";
import { VscCollapseAll } from "react-icons/vsc";
import { VscExpandAll } from "react-icons/vsc";
import { IoIosMore } from "react-icons/io";
import { CgMoreVerticalO } from "react-icons/cg";
const VolumeAccordion = ({ volume }) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleAccordion = () => setIsOpen(!isOpen);

  return (
    <div style={{ marginBottom: '20px' }}>
      
      <button onClick={toggleAccordion} style={{ 
          width: '100%', 
          padding: '10px', 
          cursor: 'pointer', 
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'space-between' 
        }}>
        Volume {volume.volume_number} {isOpen ? <VscCollapseAll /> : <VscExpandAll />} 
        <Link to={`/volumes/${volume.volume_number}`} style={{marginLeft: 'auto'}}><CgMoreVerticalO size={24}/></Link>
      </button>
      {isOpen && (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {volume.articles.map(article => (
            <li key={article.id} style={{ padding: '10px', borderBottom: '1px solid #ccc' }}>
              {/* <h4 className="articleTitle"><Link  to={`/journal/${article.id}`} 
              style={{ textDecoration: 'none' }}>{article.title}</Link></h4> */}
              <Link to={`/journal/${article.id}`} style={{ textDecoration: 'none' }} >
              <h4 className="articleTitle" >{article.title}</h4>
              </Link>
              <p className="articleType">{article.article_type.article_type}</p>
              <p className="articleAuthors">{article.authors}</p>
              <p className="articleDate">Published on: {article.publication_date}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default VolumeAccordion;
