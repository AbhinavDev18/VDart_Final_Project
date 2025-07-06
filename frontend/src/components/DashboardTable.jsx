import React, { useEffect, useState } from "react";
import API from "../api";

export default function DashboardTable() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    API.getEmails()
      .then((res) => setEmails(res.data))
      .catch((err) => console.error(err));
  }, []);

  const sendMail = (email) => {
    API.sendMail(email)
      .then(() => alert(`Mail sent to ${email}`))
      .catch((err) => console.error(err));
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-10">
      <h1 className="text-3xl font-bold text-blue-600 mb-8">
        VDart Email Dashboard
      </h1>
      <div className="w-full max-w-4xl bg-white shadow rounded-lg p-6">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Email
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Status
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Send
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {emails.map((row, index) => (
              <tr key={index}>
                <td className="px-6 py-4 whitespace-nowrap">{row.email}</td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span
                    className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                      row.status === "Submitted"
                        ? "bg-green-100 text-green-800"
                        : "bg-red-100 text-red-800"
                    }`}
                  >
                    {row.status}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <button
                    className="inline-flex items-center px-3 py-1 bg-blue-600 text-white text-sm font-medium rounded hover:bg-blue-700"
                    onClick={() => sendMail(row.email)}
                  >
                    Send Mail
                  </button>
                </td>
              </tr>
            ))}
            {emails.length === 0 && (
              <tr>
                <td
                  colSpan="3"
                  className="text-center text-gray-500 py-4"
                >
                  No emails found in Google Sheet
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
