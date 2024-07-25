import React, { useContext } from "react";
import { NavLink } from "react-router-dom";
import { Sidebar, Menu, MenuItem, useProSidebar } from "react-pro-sidebar";
import {
  MdOutlineInventory,
  MdSpaceDashboard,
  MdContactSupport,
  MdStore,
  MdOutlineAddLink,
} from "react-icons/md";
import { RiMoneyDollarCircleFill, RiLogoutBoxFill } from "react-icons/ri";
import { GoPackage } from "react-icons/go";
import {
  FaBoxArchive,
  FaChartSimple,
  FaHandshakeAngle,
  FaRegCreditCard,
} from "react-icons/fa6";
import { BsFillPersonFill } from "react-icons/bs";
import { AiTwotoneSetting } from "react-icons/ai";
import { LuNewspaper } from "react-icons/lu";
import { GrAnalytics } from "react-icons/gr";
import afrijour_logo from "../../../assets/trace.svg";
import AuthContext from "../../../context/AuthContext";

// Main navigation links
const mainNavLinks = [
  { to: "/dashboard-main", label: "Dashboard", icon: "MdSpaceDashboard" },
  { to: "/analytics", label: "Analytics", icon: "GrAnalytics" },
  { to: "/journals", label: "Journals", icon: "GoPackage" },
  { to: "/indexers", label: "Indexers", icon: "MdOutlineInventory" },
  { to: "/repositories", label: "Repositories", icon: "FaBoxArchive" },
  { to: "/reviewers", label: "Reviewers", icon: "BsFillPersonFill" },
  { to: "/reports", label: "Reports", icon: "FaChartSimple" },
  { to: "/news", label: "News & Updates", icon: "LuNewspaper" },
];

const iconMapping = {
  MdSpaceDashboard: MdSpaceDashboard,
  GrAnalytics: GrAnalytics,
  RiMoneyDollarCircleFill: RiMoneyDollarCircleFill,
  GoPackage: GoPackage,
  FaHandshakeAngle: FaHandshakeAngle,
  MdOutlineInventory: MdOutlineInventory,
  FaRegCreditCard: FaRegCreditCard,
  BsFillPersonFill: BsFillPersonFill,
  MdOutlineAddLink: MdOutlineAddLink,
  FaChartSimple: FaChartSimple,
  FaBoxArchive: FaBoxArchive,
  MdStore: MdStore,
  MdContactSupport: MdContactSupport,
  AiTwotoneSetting: AiTwotoneSetting,
  LuNewspaper: LuNewspaper,
  RiLogoutBoxFill: RiLogoutBoxFill,
};

const LeftPanel = () => {
  const isActiveLink = (path) => {
    return location.pathname === path;
  };

  // Function to go to home
  const goHome = () => {
    console.log("hhdh");
    window.location.href = "/";
  };
  let { logoutUser } = useContext(AuthContext);

  return (
    <div
      style={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}
    >
      <div style={{ width: "100%" }}>
        <img
          src={afrijour_logo}
          className={"h-20 w-20 object-contain"}
          alt="Logo"
          onClick={goHome}
          style={{ cursor: "pointer", width: "auto" }}
        />
      </div>
      <div style={{ marginTop: "4rem", width: "min-content" }}>
        <Menu
          menuItemStyles={{
            button: ({ level, active, disabled }) => ({
              color: disabled ? "#fff" : "#000",
              backgroundColor: active ? "#000" : "transparent",
              "&:hover": {
                color: "black",
                borderRadius: "25px 0 0 25px",
                fontWeight: "bold",
              },
            }),
            label: () => ({
              color: "rgb(var(--accessible-color))",
            }),
          }}
        >
          {mainNavLinks.map(({ to, label, icon }) => (
            <NavLink
              key={to}
              to={to}
              active="active"
              style={{ fontWeight: "500" }}
            >
              <MenuItem
                className={`menu-item ${isActiveLink(to) ? "menu-item-active" : ""}`}
                icon={React.createElement(iconMapping[icon], {
                  className: `icon text2xl ${isActiveLink(to) ? "active-link" : ""}`,
                })}
              >
                <span className="text">{label}</span>
              </MenuItem>
            </NavLink>
          ))}
          <MenuItem
            className="menu-item menu-item-active"
            //className={`menu-item ${isActiveLink(to) ? "menu-item-active" : ""}`}
            icon={<RiLogoutBoxFill className="icon text2xl" />}
            onClick={logoutUser}
          >
            <span className="text">Log Out</span>
          </MenuItem>
        </Menu>
      </div>
    </div>
  );
};

export default LeftPanel;
