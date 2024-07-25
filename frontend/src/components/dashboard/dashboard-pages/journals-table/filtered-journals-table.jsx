import React, { useState } from "react";
import "./journals-table.css";
import { MdFirstPage } from "react-icons/md";
import { MdLastPage } from "react-icons/md";
import { GrPrevious } from "react-icons/gr";
import { GrNext } from "react-icons/gr";
import { Link } from "react-router-dom";

const JournalsTable = ({ data }) => {
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
      title: "Journal 1",
      author: "Author 1",
      date: "2024-02-18",
      category: "Science",
      keywords: ["experiment", "research", "analysis"],
      citation_count: 25,
      published: true,
      DOI: "doi:10.1234/abcd.5678",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 2,
      title: "Journal 2",
      author: "Author 2",
      date: "2024-02-17",
      category: "Medicine",
      keywords: ["clinical trial", "treatment", "patients"],
      citation_count: 42,
      published: true,
      DOI: "doi:10.5678/efgh.9012",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 3,
      title: "Journal 3",
      author: "Author 3",
      date: "2024-02-16",
      category: "Psychology",
      keywords: ["behavior", "mind", "therapy"],
      citation_count: 18,
      published: true,
      DOI: "doi:10.9012/ijkl.3456",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 4,
      title: "Journal 4",
      author: "Author 4",
      date: "2024-02-15",
      category: "Engineering",
      keywords: ["design", "innovation", "technology"],
      citation_count: 36,
      published: true,
      DOI: "doi:10.3456/mnop.7890",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 5,
      title: "Journal 5",
      author: "Author 5",
      date: "2024-02-14",
      category: "Economics",
      keywords: ["market", "finance", "trade"],
      citation_count: 30,
      published: true,
      DOI: "doi:10.6789/qrst.1234",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 6,
      title: "Journal 6",
      author: "Author 6",
      date: "2024-02-13",
      category: "Education",
      keywords: ["learning", "teaching", "curriculum"],
      citation_count: 22,
      published: true,
      DOI: "doi:10.2345/uvwx.5678",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 7,
      title: "Journal 7",
      author: "Author 7",
      date: "2024-02-12",
      category: "History",
      keywords: ["events", "culture", "society"],
      citation_count: 14,
      published: true,
      DOI: "doi:10.5678/yzab.9012",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 8,
      title: "Journal 8",
      author: "Author 8",
      date: "2024-02-11",
      category: "Environmental Science",
      keywords: ["climate", "ecosystem", "pollution"],
      citation_count: 28,
      published: true,
      DOI: "doi:10.9012/cdef.3456",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 9,
      title: "Journal 9",
      author: "Author 9",
      date: "2024-02-10",
      category: "Sociology",
      keywords: ["community", "identity", "inequality"],
      citation_count: 20,
      published: true,
      DOI: "doi:10.3456/ghij.7890",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 10,
      title: "Journal 10",
      author: "Author 10",
      date: "2024-02-09",
      category: "Political Science",
      keywords: ["government", "policy", "democracy"],
      citation_count: 35,
      published: true,
      DOI: "doi:10.6789/klmn.1234",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 11,
      title: "Journal 11",
      author: "Author 11",
      date: "2024-02-08",
      category: "Art",
      keywords: ["creativity", "expression", "aesthetics"],
      citation_count: 19,
      published: true,
      DOI: "doi:10.2345/opqr.5678",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 12,
      title: "Journal 12",
      author: "Author 12",
      date: "2024-02-07",
      category: "Communication",
      keywords: ["media", "message", "audience"],
      citation_count: 26,
      published: true,
      DOI: "doi:10.5678/stuv.9012",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 13,
      title: "Journal 13",
      author: "Author 13",
      date: "2024-02-06",
      category: "Linguistics",
      keywords: ["language", "grammar", "communication"],
      citation_count: 21,
      published: true,
      DOI: "doi:10.9012/wxyz.3456",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 14,
      title: "Journal 14",
      author: "Author 14",
      date: "2024-02-05",
      category: "Anthropology",
      keywords: ["culture", "evolution", "society"],
      citation_count: 17,
      published: true,
      DOI: "doi:10.3456/abcd.7890",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
      id: 15,
      title: "Journal 15",
      author: "Author 15",
      date: "2024-02-04",
      category: "Philosophy",
      keywords: ["ethics", "reasoning", "metaphysics"],
      citation_count: 33,
      published: true,
      DOI: "doi:10.6789/efgh.1234",
      eISSN: 2773 - 3807,
      print_ISSN: 2716 - 9421,
      desc: "Advanced Research in Economics and Business Strategy is a peer reviewed scientific biannual international and free of charge, open-access journal, issued regularly by Faculty of Economics, Business and Management Sciences - University of Oran 2, in two issues (June and December) from each year. The Journal is interested in the following fields of research: Business, Management and Accounting; Economics, Econometrics and Finance.",
      current_issue:
        "Vol 4 No 2 (2023): Advanced Research in Economics and Business Strategy Journal-December 2023",
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
    {
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
      image:
        "https://www.ajol.info/public/journals/775/homepageImage_en_US.jpg",
    },
  ];

  // Filter data based on search query
  const filteredJournals = journals.filter((journal) =>
    journal.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  // Sorting and paginating data
  const sortedData = sortData(filteredJournals);

  const paginatedData = paginate(sortedData, currentPage, recordsPerPage);

  return (
    <div>
      <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <table
          class="w-full text-left text-sm text-gray-500 dark:text-gray-400 rtl:text-right"
          style={{ lineHeight: "1" }}
        >
          <thead class="bg-gray-50 text-xs uppercase text-gray-700 dark:bg-gray-700 dark:text-gray-400">
            <tr style={{ textAlign: "center" }}>
              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("title")}
              >
                Title
              </th>
              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("author")}
              >
                Author
              </th>

              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("category")}
              >
                Category
              </th>

              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("citation_count")}
              >
                Citation Count
              </th>

              <th
                scope="col"
                class="px-6 py-3"
                onClick={() => handleSort("published")}
              >
                Published
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
                    {journal.title}
                  </Link>
                </th>
                <td>{journal.author}</td>
                <td>{journal.category}</td>
                <td>{journal.citation_count}</td>

                <td>{journal.published ? "Yes" : "No"}</td>
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

export default JournalsTable;
