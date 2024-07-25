import { ScrollToTop } from "@/components/scroll-to-top";
import AboutPage from "@/routes/about";
import ContactPage from "@/routes/contact";
import FaqsPage from "@/routes/resources";
import HomePage from "@/routes/home";
import SupportPage from "@/routes/support";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import DashboardMain from "./components/dashboard/dashboard-main";
import Analytics from "./components/dashboard/dashboard-pages/analytics";
import Reports from "./components/dashboard/dashboard-pages/reports";
import Reviewers from "./components/dashboard/dashboard-pages/reviewers";
import Indexers from "./components/dashboard/dashboard-pages/indexers";
import Journals from "./components/dashboard/dashboard-pages/journals";
import Repositories from "./components/dashboard/dashboard-pages/repositories";
import NewsUpdates from "./components/dashboard/dashboard-pages/news-updates";
import Journal from "./components/dashboard/dashboard-pages/journal";
import ResourcesPage from "@/routes/resources";
//import Login from "@/routes/Login";
import Login from "./routes/Login";
import Register from "./routes/Register";
import PasswordResetRequest from "./routes/PasswordResetRequest";
import PasswordResetConfirm from "./routes/PasswordResetConfirm";
import PasswordResetComplete from "./routes/PasswordResetComplete";
import PrivateRoute from "./utils/PrivateRoute";
import { AuthProvider } from "./context/AuthContext";
export default function App() {
  /**
   * Vite exposes env variables on the special import.meta.env object.
   * Basename needs to be set for GitHub Pages to function properly.
   *
   * @link https://vitejs.dev/guide/env-and-mode.html
   */
  const basename = "/";
  // import.meta.env.BASE_URL

  return (
    <BrowserRouter basename={basename}>
      <AuthProvider>
        <ScrollToTop>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="about" element={<AboutPage />} />
            <Route path="contact" element={<ContactPage />} />
            <Route path="faqs" element={<FaqsPage />} />
            <Route path="resources" element={<ResourcesPage />} />
            <Route path="support" element={<SupportPage />} />
            <Route
              path="dashboard-main"
              element={<PrivateRoute Component={DashboardMain} />}
            />
            <Route
              path="analytics"
              element={<PrivateRoute Component={Analytics} />}
            />
            <Route
              path="reports"
              element={<PrivateRoute Component={Reports} />}
            />
            <Route
              path="reviewers"
              element={<PrivateRoute Component={Reviewers} />}
            />
            <Route
              path="indexers"
              element={<PrivateRoute Component={Indexers} />}
            />
            <Route
              path="journals"
              element={<PrivateRoute Component={Journals} />}
            />
            <Route
              path="journal"
              element={<PrivateRoute Component={Journal} />}
            />
            {/* <Route path='/catalog/product/:productId' element={<ImageProduct />} />      */}
            {/* <Route path='journal-details?id=${}" element={<Journal />} />   */}
            {/* /journal-details?id=${journal.id} */}
            <Route path="journal-details/:journalId" element={<Journal />} />
            <Route
              path="repositories"
              element={<PrivateRoute Component={Repositories} />}
            />
            <Route
              path="news"
              element={<PrivateRoute Component={NewsUpdates} />}
            />
            <Route path="login" element={<Login />} />
            <Route path="register" element={<Register />} />

            <Route path="reset_password" element={<PasswordResetRequest />} />
            <Route
              path="reset/:uid/:token"
              element={<PasswordResetConfirm />}
            />
            <Route
              path="reset_password_complete"
              element={<PasswordResetComplete />}
            />
          </Routes>
        </ScrollToTop>
      </AuthProvider>
    </BrowserRouter>
  );
}
