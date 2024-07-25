import { createContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  let [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
      ? JSON.parse(localStorage.getItem("authTokens"))
      : null
  );
  let [user, setUser] = useState(() =>
    localStorage.getItem("authTokens")
      ? jwtDecode(localStorage.getItem("authTokens"))
      : null
  );
  const navigate = useNavigate();
  let [loading, setLoading] = useState(true);
  let loginUser = async (e) => {
    e.preventDefault();

    let response = await fetch("http://127.0.0.1:8000/api/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: e.target.email.value,
        password: e.target.password.value,
      }),
    });
    let data = await response.json();
    // console.log("data:", data);
    // console.log("response:", response);
    if (response.status === 200) {
      setAuthTokens(data);
      setUser(jwtDecode(data.access));
      console.log(user);
      localStorage.setItem("authTokens", JSON.stringify(data));
      navigate("dashboard-main/");
    } else {
      alert("Something went wrong!");
    }
  };
  let registerUser = async (e) => {
    e.preventDefault();

    let response = await fetch("http://127.0.0.1:8000/api/register/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: e.target.email.value,
        user_name: e.target.user_name.value,
        location: e.target.location.value,
        phone_number: e.target.phone_number.value,
        password: e.target.password.value,
      }),
    });
    let data = await response.json();
    console.log("data:", data);
    console.log("response:", response);
    if (response.status === 200 || response.status === 201) {
      //  navigate("dashboard-main/");
      alert("Successfully registered");
      navigate("login");
    } else {
      alert("Something went wrong!");
    }
  };
  let logoutUser = () => {
    setAuthTokens(null);
    setUser(null);
    localStorage.removeItem("authTokens");
    navigate("login");
  };

  //   let updateToken = async () => {
  //     console.log("Update Token");
  //     let response = await fetch("http://127.0.0.1:8000/api/token/refresh", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //       },
  //       body: JSON.stringify({
  //         refresh: authTokens.refresh,
  //       }),
  //     });
  //     let data = await response.json();
  //     if (response.status === 200) {
  //       setAuthTokens(data);
  //       setUser(jwtDecode(data.access));
  //       console.log(user);
  //       localStorage.setItem("authTokens", JSON.stringify(data));
  //     } else {
  //       logoutUser();
  //     }
  //   };
  //   useEffect(() => {
  //     let interval = setInterval(() => {
  //       if (authTokens) {
  //         updateToken();
  //       }
  //     }, 2000);
  //     return () => clearInterval(interval);
  //   }, [authTokens, loading]);

  let contextData = {
    user: user,
    loginUser: loginUser,
    logoutUser: logoutUser,
    registerUser: registerUser,
  };
  return (
    <AuthContext.Provider value={contextData}>{children}</AuthContext.Provider>
  );
};
