import React from "react";
import { useState, useEffect } from "react";
import "./../dashboard-layout.css";
import LeftPanel from "../components/left-panel";
import TopPanel from "../components/top-panel";
import FooterPanel from "../components/footer-panel";
import scopus from "../../../assets/indexers/scopus.png";
import google_scholar from "../../../assets/indexers/g_scholar.png";
import { Link } from "react-router-dom";

// const [indexerData, setIndexerData] = useState([])

// useEffect(() => {
//   // Fetch data from the backend endpoint (replace with actual fetch call)
//   const dummyData = [
//     {
//       name: 'Scopus',
//       image: 'https://via.placeholder.com/150',
//       description: 'Scopus offers free features to non-subscribed users as Scopus Preview...',
//       link: 'https://www.scopus.com/home.uri?zone=header&origin=sbrowse',
//     },
//     {
//       name: 'Google Scholar',
//       image: 'https://via.placeholder.com/150',
//       description: 'Google Scholar is a freely accessible web search engine that indexes...',
//       link: 'https://scholar.google.com/',
//     },
//     // Add more dummy data as needed
//   ]

//   // Set dummy data to state
//   setIndexerData(dummyData)
// }, [])

const dummyData = [
  {
    name: "Scopus",
    image: scopus,
    description:
      "  Scopus offers free features to non-subscribed users as Scopus Preview. Researchers use Scopus Preview to assist with research, such as searching for authors and source metrics.",
    link: "https://www.scopus.com/home.uri?zone=header&origin=sbrowse",
  },
  {
    name: "Google Scholar",
    image: google_scholar,
    description:
      "  Google Scholar is a freely accessible web search engine that indexes the full text or metadata of scholarly literature across an array of publishing formats and disciplines.",
    link: "https://scholar.google.com/",
  },
  // Add more dummy data as needed
];

const Indexers = () => {
  return (
    <div
      className="container"
      style={{ overflow: "auto", maxWidth: "-webkit-fill-available" }}
    >
      <div className="left-panel">
        <LeftPanel />
      </div>
      <div className="top-panel">
        <TopPanel />
      </div>

      <div className="main-content">
        {/* Main Content */}
        {/* Breadcrumb navigation */}
        <nav class="flex" aria-label="Breadcrumb">
          <ol class="inline-flex items-center space-x-1 md:space-x-2 rtl:space-x-reverse">
            <li class="inline-flex items-center">
              <a
                href="#"
                class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white"
              >
                <svg
                  class="me-2.5 h-3 w-3"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="m19.707 9.293-2-2-7-7a1 1 0 0 0-1.414 0l-7 7-2 2a1 1 0 0 0 1.414 1.414L2 10.414V18a2 2 0 0 0 2 2h3a1 1 0 0 0 1-1v-4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v4a1 1 0 0 0 1 1h3a2 2 0 0 0 2-2v-7.586l.293.293a1 1 0 0 0 1.414-1.414Z" />
                </svg>
                <Link
                  to="/dashboard-main"
                  className="ms-1 text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white md:ms-2"
                >
                  Home
                </Link>
              </a>
            </li>
            <li>
              <div class="flex items-center">
                <svg
                  class="mx-1 h-3 w-3 text-gray-400 rtl:rotate-180"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 6 10"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="m1 9 4-4-4-4"
                  />
                </svg>

                <Link
                  to="/indexers"
                  className="ms-1 text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white md:ms-2"
                >
                  Indexers
                </Link>
              </div>
            </li>
          </ol>
        </nav>
        <hr className="mt-2" />
        <p className="mb-1 mt-4 text-gray-500 dark:text-gray-400">
          Journals in this platform are index in one or more indexers
          highlighted below
        </p>
        <div className="grid grid-cols-2 gap-1 md:grid-cols-4">
          {dummyData.map((indexer, index) => (
            <div
              key={index}
              className="mt-4 max-w-sm rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800"
            >
              <a href={indexer.link} target="_blank" rel="noopener noreferrer">
                <div
                  style={{
                    maxHeight: "12rem",
                    minHeight: "12rem",
                    textAlign: "-webkit-center",
                    padding: "1rem",
                    alignContent: "space-around",
                    justifyContent: "center",
                  }}
                >
                  <img
                    src={indexer.image}
                    alt={indexer.name}
                    style={{ maxHeight: "inherit" }}
                  />
                </div>
              </a>
              <div className="p-5">
                <a
                  href={indexer.link}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <h5 className="mb-2 text-l font-bold tracking-tight text-gray-900 dark:text-white">
                    {indexer.name}
                  </h5>
                </a>
                <p className="mb-3  font-normal text-gray-700 dark:text-gray-400">
                  {indexer.description}
                </p>
                <a
                  href={indexer.link}
                  className="inline-flex items-center rounded-lg bg-blue-700 px-3 py-2 text-center text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Read more
                  <svg
                    className="ms-2 h-3.5 w-3.5 rtl:rotate-180"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 14 10"
                  >
                    <path
                      stroke="currentColor"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M1 5h12m0 0L9 1m4 4L9 9"
                    />
                  </svg>
                </a>
              </div>
            </div>
          ))}
        </div>
        <FooterPanel />
      </div>
    </div>
  );
};

export default Indexers;
