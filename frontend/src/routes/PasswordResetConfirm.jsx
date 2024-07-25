// import React, { useState } from "react";
// import { useParams } from "react-router-dom";
// import axios from "axios";

// const PasswordResetConfirm = () => {
//   const { uid, token } = useParams();
//   const [password, setPassword] = useState("");
//   const [passwordConfirm, setPasswordConfirm] = useState("");
//   const [message, setMessage] = useState("");

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post(
//         `http://localhost:8000/api/reset/${uid}/${token}/`,
//         {
//           password,
//           password_confirm: passwordConfirm,
//         }
//       );
//       setMessage(response.data.message);
//     } catch (error) {
//       setMessage("Error resetting password.");
//     }
//   };

//   return (
//     <div>
//       <h1>Reset Password</h1>
//       <form onSubmit={handleSubmit}>
//         <label>
//           New Password:
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </label>
//         <br></br>
//         <label>
//           Confirm Password:
//           <input
//             type="password"
//             value={passwordConfirm}
//             onChange={(e) => setPasswordConfirm(e.target.value)}
//             required
//           />
//         </label>
//         <br></br>
//         <button type="submit">Reset Password</button>
//       </form>
//       {message && <p>{message}</p>}
//     </div>
//   );
// };

// export default PasswordResetConfirm;

import React, { useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const PasswordResetConfirm = () => {
  const { uid, token } = useParams();
  const [password, setPassword] = useState("");
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `http://localhost:8000/api/reset/${uid}/${token}/`,
        {
          password,
          password_confirm: passwordConfirm,
        }
      );
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error resetting password.");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-200">
      <div className="w-full max-w-sm p-6 bg-white rounded-lg shadow-lg">
        <h1 className="text-2xl font-bold text-center mb-6 text-gray-800">
          Reset Your Password
        </h1>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="password"
            >
              New Password
            </label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Enter your new password"
            />
          </div>
          <div className="mb-4">
            <label
              className="block mb-2 text-sm font-medium text-gray-700"
              htmlFor="passwordConfirm"
            >
              Confirm Password
            </label>
            <input
              type="password"
              id="passwordConfirm"
              value={passwordConfirm}
              onChange={(e) => setPasswordConfirm(e.target.value)}
              required
              className="w-full px-4 py-2 text-sm border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Confirm your new password"
            />
          </div>
          <div className="mb-4">
            <button
              type="submit"
              className="w-full px-4 py-2 font-semibold text-white bg-blue-600 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Reset Password
            </button>
          </div>
        </form>
        {message && <p className="mt-4 text-center text-gray-600">{message}</p>}
      </div>
    </div>
  );
};

export default PasswordResetConfirm;
