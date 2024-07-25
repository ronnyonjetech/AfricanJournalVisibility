// import React, { useContext } from "react";
// import AuthContext from "../context/AuthContext";
// import afrijour_logo from "../assets/trace.svg";
// import { useNavigate } from "react-router-dom";
// const Register = () => {
//   let { registerUser } = useContext(AuthContext);
//   const navigate = useNavigate();
//   return (
//     <div>
//       Register
//       <form onSubmit={registerUser}>
//         <input type="email" name="email" placeholder="Enter email" />
//         <br></br>
//         <input type="text" name="user_name" placeholder="Enter Username" />
//         <br></br>
//         <input type="text" name="location" placeholder="Enter Location" />
//         <br></br>
//         <input
//           type="text"
//           name="phone_number"
//           placeholder="Enter PhoneNumber"
//         />
//         <br></br>
//         <input type="password" name="password" placeholder="Enter Password" />
//         <br></br>
//         <button type="submit">Register</button>
//       </form>
//     </div>
//   );
// };

// export default Register;
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const Register = () => {
  let { registerUser } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleRegister = (e) => {
    registerUser(e, navigate);
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-200">
      <div className="w-full max-w-sm p-6 bg-white rounded-lg shadow-lg">
        <div className="flex justify-center mb-6">
          <h1 className="text-2xl font-bold">Register</h1>
        </div>
        <form onSubmit={handleRegister}>
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="email"
            >
              Email
            </label>
            <input
              type="email"
              name="email"
              id="email"
              placeholder="Enter email"
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="user_name"
            >
              Username
            </label>
            <input
              type="text"
              name="user_name"
              id="user_name"
              placeholder="Enter Username"
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="location"
            >
              Location
            </label>
            <input
              type="text"
              name="location"
              id="location"
              placeholder="Enter Location"
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="phone_number"
            >
              Phone Number
            </label>
            <input
              type="text"
              name="phone_number"
              id="phone_number"
              placeholder="Enter Phone Number"
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="password"
            >
              Password
            </label>
            <input
              type="password"
              name="password"
              id="password"
              placeholder="Enter Password"
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div className="flex items-center justify-between mb-4">
            <button
              type="submit"
              className="w-full px-4 py-2 font-semibold text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Register
            </button>
          </div>

          <div className="flex justify-between text-sm">
            <a href="/" className="text-blue-500 hover:underline">
              Home
            </a>
            {/* <a href="/reset_password" className="text-blue-500 hover:underline">
              Forgot Password?
            </a> */}
            <a href="/login" className="text-blue-500 hover:underline">
              Log In
            </a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Register;
