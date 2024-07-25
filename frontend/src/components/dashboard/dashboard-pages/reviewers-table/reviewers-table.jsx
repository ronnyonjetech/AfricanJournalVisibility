import React, { useState } from "react";
// import "./journals-table.css";
import { MdFirstPage } from "react-icons/md";
import { MdLastPage } from "react-icons/md";
import { GrPrevious } from "react-icons/gr";
import { GrNext } from "react-icons/gr";
import { Link } from "react-router-dom";

const ReviewersTable = ({ data }) => {
  const [currentPage, setCurrentPage] = useState(1);
  const [recordsPerPage, setRecordsPerPage] = useState(15);
  const [sortConfig, setSortConfig] = useState({ key: null, direction: "asc" });
  const [searchQuery, setSearchQuery] = useState("");

  // Function to handle sorting
  const handleSort = (key) => {
    let direction = "asc";
    if (sortConfig.key === key && sortConfig.direction === "asc") {
      direction = "desc";
    }
    setSortConfig({ key, direction });
  };

  // Function to paginate data
  const paginate = (items, currentPage, recordsPerPage) => {
    const startIndex = (currentPage - 1) * recordsPerPage;
    return items.slice(startIndex, startIndex + recordsPerPage);
  };

  // Function to sort data
  const sortData = (items) => {
    if (sortConfig.key !== null) {
      return items.sort((a, b) => {
        if (a[sortConfig.key] < b[sortConfig.key]) {
          return sortConfig.direction === "asc" ? -1 : 1;
        }
        if (a[sortConfig.key] > b[sortConfig.key]) {
          return sortConfig.direction === "asc" ? 1 : -1;
        }
        return 0;
      });
    }
    return items;
  };

  // Dummy data (replace with actual data)
  const journals = [
    {
      id: 1,
      name: "Ron Nyonje",
      reviews: "10",
      date: "2024-02-18",
    },
    {
      id: 2,
      name: "Paul Joseph",
      reviews: "30",
      date: "2024-02-18",
    },
    {
      id: 3,
      name: "Isaac Mchawi",
      reviews: "31",
      date: "2024-02-18",
    },
    {
      id: 3,
      name: "William Mwizi",
      reviews: "31",
      date: "2024-02-18",
    },
  ];

  // Filter data based on search query
  const filteredJournals = journals.filter((journal) =>
    journal.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Sorting and paginating data
  const sortedData = sortData(filteredJournals);

  const paginatedData = paginate(sortedData, currentPage, recordsPerPage);

  return (
    <div>
      <div className="w-f" style={{ display: "grid", justifyContent: "end" }}>
        <form class="mx-auto  " style={{ width: "20rem", margin: "1rem" }}>
          <label
            for="default-search"
            class="sr-only mb-2 text-sm font-medium text-gray-900 dark:text-white"
          >
            Search
          </label>
          <div class="relative">
            <div class="pointer-events-none absolute inset-y-0 start-0 flex items-center ps-3">
              <svg
                class="h-4 w-4 text-gray-500 dark:text-gray-400"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 20"
              >
                <path
                  stroke="currentColor"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                />
              </svg>
            </div>
            <input
              type="search"
              id="default-search"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              class="block h-10 w-full rounded-lg border border-gray-300 bg-gray-50 p-4 ps-10 text-sm text-gray-900 focus:border-gray-500 focus:ring-gray-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-black-500 dark:focus:ring-black-500"
              placeholder="Search Reviewers by name..."
              required
              style={{ borderRadius: "1rem" }}
            />
            {/* <button
              type="submit"
              class="absolute bottom-2.5 end-2.5 rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
            >
              Search
            </button> */}
          </div>
        </form>
      </div>
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        {/* <input
          type="text"
          placeholder="Search by title..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="block w-full border border-gray-300 bg-gray-50 p-2.5 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
        /> */}

        <table class="w-full text-left text-sm text-gray-500 dark:text-gray-400 rtl:text-right">
          <thead class="bg-gray-50 text-xs uppercase text-gray-700 dark:bg-gray-700 dark:text-gray-400">
            <tr style={{ textAlign: "center" }}>
              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("name")}
              >
                Name Of Reviewer
              </th>
              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("reviews")}
              >
                Number Of Reviews
              </th>

              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("date")}
              >
                Date
              </th>
            </tr>
          </thead>
          <tbody>
            {paginatedData.map((journal) => (
              <tr
                key={journal.id}
                class="border-b bg-white hover:bg-gray-50 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-600"
                style={{ textAlign: "center" }}
              >
                <th
                  scope="row"
                  class="whitespace-nowrap px-6 py-4 font-medium text-gray-900 dark:text-white"
                >
                  {/* {journal.title} */}
                  {/* <a href={`journal-details?id=${journal.id}`}>{journal.title}</a> */}
                  {/* <Link to={`/catalog/product/${row?.original?.id}`}>{row.original.name}</Link> */}
                  <Link to={`/journal-details/${journal?.id}`}>
                    {journal.name}
                  </Link>
                </th>

                <td>{journal.reviews}</td>
                <td>{journal.date}</td>
                {/* <td>{journal.category}</td>
                <td>{journal.citation_count}</td>
                <td>{journal.keywords.join(", ")}</td>
                <td>{journal.published ? "Yes" : "No"}</td>
                <td>{journal.DOI}</td> */}
              </tr>
            ))}
          </tbody>
        </table>
        <div
          style={{
            marginBottom: "rem",
            display: "inline-flex",
            width: "100%",
            justifyContent: "center",
          }}
        >
          <div>
            <table class="mt-2 w-full text-left text-sm text-gray-500 dark:text-gray-400 rtl:text-right">
              <tr>
                <td style={{ verticalAlign: "bottom" }}>
                  <button
                    onClick={() => setCurrentPage(1)}
                    disabled={currentPage === 1}
                    style={{ marginTop: "0.8rem" }}
                  >
                    <MdFirstPage size={25} />
                  </button>
                </td>
                <td>
                  <button
                    onClick={() => setCurrentPage((prevPage) => prevPage - 1)}
                    disabled={currentPage === 1}
                    style={{ marginTop: "0.8rem" }}
                  >
                    <GrPrevious />
                  </button>
                </td>
                <td style={{ verticalAlign: "top" }}>
                  <div style={{ textAlign: "center", marginTop: "1rem" }}>
                    Page: {currentPage} of{" "}
                    {Math.ceil(filteredJournals.length / recordsPerPage)}
                  </div>
                </td>
                <td>
                  <button
                    onClick={() => setCurrentPage((prevPage) => prevPage + 1)}
                    disabled={
                      currentPage ===
                      Math.ceil(journals.length / recordsPerPage)
                    }
                    style={{ marginTop: "0.8rem" }}
                  >
                    <GrNext />
                  </button>
                </td>
                <td style={{ verticalAlign: "bottom" }}>
                  <button
                    onClick={() =>
                      setCurrentPage(
                        Math.ceil(journals.length / recordsPerPage)
                      )
                    }
                    disabled={
                      currentPage ===
                      Math.ceil(journals.length / recordsPerPage)
                    }
                    style={{ marginTop: "0.8rem" }}
                  >
                    <MdLastPage size={25} />
                  </button>
                </td>
                <td>
                  <select
                    style={{
                      borderRadius: "15px",
                      borderColor: "#d2d6dc",

                      width: "auto",
                    }}
                    value={recordsPerPage}
                    onChange={(e) =>
                      setRecordsPerPage(parseInt(e.target.value))
                    }
                    class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500"
                  >
                    <option value={5}>5 Records Per Page</option>
                    <option value={10}>10 Records Per Page</option>
                    <option value={15}>15 Records Per Page</option>
                    <option value={30}>30 Records Per Page</option>
                    <option value={50}>50 Records Per Page</option>
                  </select>
                </td>
              </tr>
            </table>
          </div>
          <hr />
        </div>
      </div>
    </div>
  );
};

export default ReviewersTable;
