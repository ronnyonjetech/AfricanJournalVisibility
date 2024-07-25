import { Article } from "@/components/article";
import { Layout } from "@/components/layout";
import resorces from "../assets/resources.jpeg";
import { Link } from "react-router-dom";

export default function ResourcesPage() {
  return (
    <Layout>
      <Article
        title="Resources"
        imageAlt="Lorem Picsum"
        imageSrc="https://picsum.photos/420/640?grayscale"
      >
        <img src={resorces} className="w-full h-96 object-cover rounded-lg" />
        <p className="mb-1 mt-6 text-gray-800 dark:text-gray-400">
          The following are resources that can be accessed on our platform
        </p>
        <details
          className="mt-4 block rounded-sm border px-4 open:border-primary-400 hover:border-primary-300"
          open
        >
          <summary className="-mx-4 cursor-pointer border-primary-200 px-4 py-3">
            African Journals Directory
          </summary>
          <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">
            With our African Journals Directory you can access a wide range of
            journals from different disciplines. We have journals from the
            fields of Medicine, Engineering, Agriculture, Law, and many more.
            The Journals are from accross the African continent.
            <br />
            Access them by clicking on the link below.
            <br />
            <Link to="/journals" style={{ color: "red" }}>
              <button className="text-white mt-3 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Journals Directory
              </button>
            </Link>
          </p>
        </details>

        <details className="mt-4 block rounded-sm border border-gray-200 px-4 hover:border-primary-300">
          <summary className="-mx-4 cursor-pointer px-4 py-3">
            African Journals Indexers
          </summary>
          <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">
            You can find the list of African Journals Indexers on our platform
            here:
            <br />
            <Link to="/indexers" style={{ color: "red" }}>
              <button className="text-white mt-3 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Indexers Directory
              </button>
            </Link>
          </p>
        </details>

        <details className="mt-4 block rounded-sm border border-gray-200 px-4 hover:border-primary-300">
          <summary className="-mx-4 cursor-pointer px-4 py-3">
            African Journals Repositories
          </summary>
          <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">
           Our platform has journals that are being hosted on the repositories. You can find them here:
            <br />
            <Link to="/repositories" style={{ color: "red" }}>
              <button className="text-white mt-3 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Reviwers Directory
              </button>
            </Link>
          </p>
        </details>

        <details className="mt-4 block rounded-sm border border-gray-200 px-4 hover:border-primary-300">
          <summary className="-mx-4 cursor-pointer px-4 py-3">
            African Journals Reviewers
          </summary>
          <p className="mb-1 mt-1 text-gray-500 dark:text-gray-400">
            Our platform also provides a list of African Journals Reviewers.
            They help in the peer review process of the journals. You can find
            them here:
            <br />
            <Link to="/reviewers" style={{ color: "red" }}>
              <button className="text-white mt-3 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Reviwers Directory
              </button>
            </Link>
          </p>
        </details>
      </Article>
    </Layout>
  );
}
