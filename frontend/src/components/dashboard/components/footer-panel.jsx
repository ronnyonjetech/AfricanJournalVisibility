import React from "react";
import aphrc_logo from "../../../assets/aphrc.png";

const FooterPanel = () => {
  return (
    <div
      style={{ display: "flex", alignItems: "end", justifyContent: "flex-end", background: '#e8e8e8', borderRadius: '10px' , marginTop:'1rem'}}
    >
      <div>
        <span
          style={{
            display: "inline-flex",
            alignItems: "center",
            marginBlock: "0.5rem",
          }}
        >
          <p
            class="text-gray-500 dark:text-gray-400"
            style={{ fontSize: "12px" }}
          >
            © 2021 African Population and Health Research Center
          </p>

          <img
            src={aphrc_logo}
            alt="Logo"
            style={{ height: "2.5rem", marginLeft: "1rem" }}
          />
        </span>
      </div>
    </div>
  );
};

export default FooterPanel;
