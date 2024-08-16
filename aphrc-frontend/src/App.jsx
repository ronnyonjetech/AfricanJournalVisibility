import { useState } from 'react'

import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Components/Home'
import Details from './Components/JournalDetails'
import JournalDetails from './Components/JournalDetails';
import Volumes from './Components/Volumes';
import VolumeDetail from './Components/VolumeDetail'
import Journals from './Components/Journals';
function App() {
  

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/journals" element={<Journals />} />
        <Route path="/journal/:id" element={<JournalDetails/>} />
        <Route path="/volumes" element={<Volumes/>} />
        <Route path="/volumes/:id" element={<VolumeDetail/>} />
        {/* <Route path="/resources" element={<Details/>} />
        <Route path="/coolstats" element={<Details />} /> */}
      </Routes>
    </Router>
  )
}

export default App
