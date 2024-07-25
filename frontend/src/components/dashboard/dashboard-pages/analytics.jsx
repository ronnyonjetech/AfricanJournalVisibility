import React from "react";
import "./../dashboard-layout.css";
import LeftPanel from "../components/left-panel";
import TopPanel from "../components/top-panel";
import FooterPanel from "../components/footer-panel";
import { Link } from "react-router-dom";
import { LuLanguages } from "react-icons/lu";
import { SiWolframmathematica } from "react-icons/si";
import { FaPenToSquare } from "react-icons/fa6";
import { FaGlobeAfrica } from "react-icons/fa";
import { MdOutlineFeaturedPlayList } from "react-icons/md";
import JournalsTable from "./journals-table/filtered-journals-table";
import FilteredJournals from "./dashboard-graph-components/filteredJournalsChart";

const Analytics = () => {
  return (
    <div className="wrapper">
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
                    to="/analytics"
                    className="ms-1 text-sm font-medium text-gray-700 hover:text-blue-600 dark:text-gray-400 dark:hover:text-white md:ms-2"
                  >
                    Analytics
                  </Link>
                </div>
              </li>
            </ol>
          </nav>
          <hr className="mt-2" />
          <p className="mb-1 mt-4 text-gray-500 dark:text-gray-400">
            Explore our Journals
          </p>
          <div className="grid grid-cols-2 gap-1 ">
            <div className="mt-4 max-w-xsm align-middle text-center rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
              <form class=" mx-auto" style={{ margin: "1rem" }}>
                <div className="grid grid-cols-2 gap-4 ">
                  <div>
                    <label
                      for="default"
                      class="block mb-2  text-left text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      Country <FaGlobeAfrica color="#6762B4" />
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>All Countries</option>
                      <option value="US">United States</option>
                      <option value="CA">Canada</option>
                      <option value="FR">France</option>
                      <option value="DE">Germany</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      Discipline <SiWolframmathematica color="#6762B4" />
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>All Disciplines</option>
                      <option value="US">Medicine</option>
                      <option value="CA">Agriculture</option>
                      <option value="FR">Social Science</option>
                      <option value="DE">Anthropology</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      Langauge <LuLanguages color="#6762B4" />
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>All Langauges</option>
                      <option value="US">English</option>
                      <option value="CA">Swahili</option>
                      <option value="FR">German</option>
                      <option value="DE">French</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      Indexed on <FaPenToSquare color="#6762B4" />
                    </label>
                    <ul
                      class="items-center w-full text-sm font-medium text-gray-600 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white"
                      style={{ height: "42px" }}
                    >
                      <li class="w-full  border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                        <div class="flex items-center ps-3">
                          <input
                            id="vue-checkbox-list"
                            type="checkbox"
                            value=""
                            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                          />
                          <label
                            for="vue-checkbox-list"
                            class="w-full py-3 ms-2 text-sm font-medium text-gray-600 dark:text-gray-300"
                          >
                            Google Scholar
                          </label>
                        </div>
                      </li>
                      <li class="w-full  border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                        <div class="flex items-center ps-3">
                          <input
                            id="react-checkbox-list"
                            type="checkbox"
                            value=""
                            class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                          />
                          <label
                            for="react-checkbox-list"
                            class="w-full py-3 ms-2 text-sm font-medium text-gray-600 dark:text-gray-300"
                          >
                            Scopus
                          </label>
                        </div>
                      </li>
                    </ul>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      <MdOutlineFeaturedPlayList color="#6762B4" />
                      Listed on Directory of Open Access Journal (DOAJ)
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>Any</option>
                      <option value="US">Yes</option>
                      <option value="CA">No</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      <MdOutlineFeaturedPlayList color="#6762B4" />
                      Listed on Open Access Journal (OAJ)
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>Any</option>
                      <option value="US">Yes</option>
                      <option value="CA">No</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      <MdOutlineFeaturedPlayList color="#6762B4" />
                      Online Publisher Based in Africa
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>Any</option>
                      <option value="US">Yes</option>
                      <option value="CA">No</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      <MdOutlineFeaturedPlayList color="#6762B4" />
                      Hosted on INASP's Journals Online
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>Any</option>
                      <option value="US">Yes</option>
                      <option value="CA">No</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      <MdOutlineFeaturedPlayList color="#6762B4" />
                      Publisher is a member of Commitee on Publication Ethics
                      (COPE)
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>Any</option>
                      <option value="US">Yes</option>
                      <option value="CA">No</option>
                    </select>
                  </div>
                  <div>
                    <label
                      for="default"
                      class="block  text-left mb-2 text-sm font-medium text-gray-600 dark:text-white"
                      style={{
                        display: "flex",
                        gap: "5px",
                        alignItems: "center",
                      }}
                    >
                      <MdOutlineFeaturedPlayList color="#6762B4" />
                      Listed on Iternational Standard Serial Number (ISSN)
                      Portal
                    </label>
                    <select
                      id="default"
                      class="bg-gray-50 border border-gray-300 text-gray-600 mb-6 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    >
                      <option selected>Any</option>
                      <option value="US">Yes</option>
                      <option value="CA">No</option>
                    </select>
                  </div>
                </div>
                <hr
                  style={{ border: "1px solid #E5E7EB", marginTop: "1rem" }}
                />
                <p className="mb-1 mt-4 text-gray-500 dark:text-gray-400">
                  Selected Criteria
                </p>
                <div class="flex justify-center">
                  Listed on Iternational Standard Serial Number (ISSN) Portal
                  Listed on Iternational Standard Serial Number (ISSN) Portal
                  Listed on Iternational Standard Serial Number (ISSN) Portal
                  Listed on Iternational Standard Serial Number (ISSN) Portal
                  Listed on Iternational Standard Serial Number (ISSN) Portal
                </div>
              </form>
            </div>
            <div className="mt-4 max-w-xsm align-middle text-center rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
              <div className="grid grid-cols-2 gap-1 ">
                <div className="mt-0 max-w-xsm align-middle text-center rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
                  <div className="p-5">
                    <h5
                      className="mb-2 text-xs tracking-tight text-gray-600 dark:text-white"
                      style={{ color: "#585859" }}
                    >
                      Journals Distribution per Country
                    </h5>
                  </div>
                </div>

                <div className="mt-0 max-w-xsm align-middle text-center rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
                  <FilteredJournals value={87} journals= {300} color="#252973" />
                </div>
              </div>
              <div className="mt-4 max-w-xsm align-middle text-center rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
                <h5
                  className="mb-0  ml-4  mt-4 text-left text-xs tracking-tight text-gray-600 dark:text-white"
                  style={{ color: "#585859", marginLeft: "1rem" }}
                >
                  Journals that met your criteria
                </h5>
                <div
                  class="relative overflow-x-auto overflow-y-auto shadow-md sm:rounded-lg"
                  style={{
                    display: "inline-flex",
                    justifyContent: "center",
                    background: "white",
                    width: "100%",
                    height: "100%", // occupy the available space
                    overflowY: "auto", // scroll if necessary
                  }}
                >
                  <div
                    style={{
                      width: "100%",
                      height: "27rem", // occupy the available space
                      overflowY: "auto",
                    }}
                  >
                    <JournalsTable />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <FooterPanel />
        </div>
      </div>
    </div>
  );
};

export default Analytics;
