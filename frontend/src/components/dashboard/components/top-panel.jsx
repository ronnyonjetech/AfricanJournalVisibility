import React, { useContext } from "react";
import { AiOutlineSearch } from "react-icons/ai";
import { RiHomeOfficeLine } from "react-icons/ri";
import AuthContext from "../../../context/AuthContext";
import { Link } from "react-router-dom";
const TopPanel = () => {
  let { user } = useContext(AuthContext);
  console.log(user);
  return (
    <div style={{ width: "-webkit-fill-available" }}>
      <table>
        <tr>
          <td>
            {" "}
            <RiHomeOfficeLine size={30} />
          </td>

          <td>
            <p style={{ fontSize: "22px", color: "grey", marginLeft: "1rem" }}>
              Welcome to African Journals Dashboard
              {/* <p>Hello {user.name}</p> */}
              {/* {user && <p>Hello {user.email}</p>}
              {user ? <p>Logout</p> : <Link to="/login">Login</Link>} */}
            </p>
          </td>
        </tr>
      </table>
    </div>
  );
};

export default TopPanel;
