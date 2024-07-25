import { useContext } from "react";
import { Navigate } from "react-router-dom";
import AuthContext from "../context/AuthContext";
const PrivateRoute = ({ Component }) => {
  let { user } = useContext(AuthContext);
  //const[isAuthenticated,setIsAuthenticated]=useState(true)
  console.log("private route works");
  //return user ? <Component /> : <Navigate to="/login" />;
  //const authenticated = true;
  return user ? <Component /> : <Navigate to="/login" />;
};

export default PrivateRoute;
