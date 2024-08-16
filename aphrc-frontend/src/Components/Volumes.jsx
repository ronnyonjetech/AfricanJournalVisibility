import React, { useEffect, useState } from 'react'
import VolumeAccordion from './VolumeAccordion';
const Volumes = () => {
  const [volumes, setVolumes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  //https://africanjournalvisibility.onrender.com/journal_api/api/volumes/
  useEffect(() => {
    fetch('http://127.0.0.1:8000/journal_api/api/volumes/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // console.log(data)
        // console.log(data.volumes)
        setVolumes(data.volumes);
        setLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setLoading(false);
      });
  }, []);
  console.log(volumes)
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return (
  <div style={{ width: '80%', margin: '0 auto' }}>
     <h1 style={{ textAlign: 'center' }}>Volumes</h1>
    {volumes.map(volume => (
      <VolumeAccordion key={volume.volume_number} volume={volume} />
    ))}
  </div>
  )
}

export default Volumes