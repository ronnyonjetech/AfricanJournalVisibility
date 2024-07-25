import React from "react";
import "./../dashboard-layout.css";
import LeftPanel from "../components/left-panel";
import TopPanel from "../components/top-panel";
import FooterPanel from "../components/footer-panel";
import JournalsTable from "./journals-table/journals-table";
import { Link } from "react-router-dom";
/* styles.css */

const journal_data = {
  id: 16,
  title: "Journal 16",
  author: "Author 16",
  date: "2024-02-03",
  category: "Literature",
  keywords: ["fiction", "poetry", "narrative"],
  citation_count: 24,
  published: true,
  DOI: "doi:10.2345/ijkl.5678",
  eISSN: 2773 - 3807,
  print_ISSN: 2716 - 9421,
  desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
  current_issue:
    "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
  image: "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
};

const Journal = () => {
  return (
    <div
      className="container"
      style={{ overflow: "hidden", maxWidth: "-webkit-fill-available" }}
    >
      <div className="left-panel">
        <LeftPanel />
      </div>
      <div className="top-panel">
        <TopPanel />
      </div>
      <div className="main-content">
        {/* Main Content */}
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
            <li class="inline-flex items-center">
              <a
                href="#"
                class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white"
              >
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
                  to="/journals"
                  className="ms-1 text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white md:ms-2"
                >
                  Journals
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
                  to="/journal"
                  className="ms-1 text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white md:ms-2"
                >
                  Journal
                </Link>
              </div>
            </li>
          </ol>
        </nav>
        <hr className="mt-2" />
        <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
          About {journal_data.title}
        </p>

        <div
          class="relative overflow-x-auto shadow-md sm:rounded-lg"
          style={{
            display: "inline-flex",
            justifyContent: "center",
            background: "white",
            width: "100%",
            maxHeight: "100vh",
            minHeight: "70vh",
          }}
        >
          <div style={{ width: "100%" }}>
            <p className="mb-4 ml-8 mt-10 size-8 w-full text-gray-500 dark:text-gray-400">
              Title: {journal_data.title}
            </p>
            <div className="grid grid-cols-2   gap-0.5 md:grid-cols-3">
              <div className="mb-8 ml-8 mt-4 max-w-sm bg-white ">
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> eISSN</b>: {journal_data.eISSN}
                </p>
                <hr />
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> DOI: </b>
                  {journal_data.DOI}
                </p>
                <hr />

                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Date:</b> {journal_data.date}
                </p>
              </div>
              <div className="ml-2 mt-4 max-w-sm bg-white ">
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Author: </b> {journal_data.author}
                </p>
                <hr />
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Category: </b> {journal_data.category}
                </p>
                <hr />
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Citations Count: </b> {journal_data.citation_count}
                </p>
              </div>

              <div className="ml-2 mt-4 max-w-sm bg-white ">
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Keywords: </b>
                  {journal_data.keywords}
                </p>
                <hr />
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Published: </b> {journal_data.published ? "YES" : "NO"}
                </p>
                <hr />
                <p className="mb-4 mt-4 size-8 w-full text-gray-500 dark:text-gray-400">
                  <b> Print ISSN: </b>
                  {journal_data.print_ISSN}
                </p>
              </div>
            </div>
            <hr />
            <div className="grid grid-cols-2   gap-5 md:grid-cols-2">
              <div className="max-w-fukk mb-8 ml-8 mt-4 bg-white ">
                <div>
                  <p className="text-justify text-gray-500 dark:text-gray-400">
                    <b> Journal Description: </b>
                    <br />
                    {journal_data.desc}
                  </p>
                </div>

                <div className="mt-4">
                  <p className=" text-gray-500 dark:text-gray-400">
                    <b>Current Issue:</b> <br /> {journal_data.current_issue}
                  </p>
                </div>
              </div>
              <div className="ml-2 mt-4 max-w-full bg-white ">
                <p className=" text-gray-500 dark:text-gray-400">
                  {/* <b>Current Issue:</b> <br /> */}
                  <img
                    src={journal_data.image}
                    alt={journal_data.title}
                    style={{ maxHeight: "20rem" }}
                  />
                </p>
              </div>
            </div>
          </div>
        </div>
        <FooterPanel />
      </div>
    </div>
  );
};

export default Journal;
