import React from "react";
import "./../dashboard-layout.css";
import LeftPanel from "../components/left-panel";
import TopPanel from "../components/top-panel";
import FooterPanel from "../components/footer-panel";

const NewsUpdates = () => {
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
        <h1>NewsUpdates Content</h1>
        <p>This is where your NewsUpdates content goes.</p>
        <FooterPanel />
      </div>
    </div>
  );
};

export default NewsUpdates;
