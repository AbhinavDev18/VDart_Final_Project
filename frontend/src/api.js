import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api"; // Backend URL

const API = {
  // Get emails
  getEmails: () => axios.get(`${API_BASE_URL}/emails/`),

  // Send mail to a specific user
  sendMail: (email) => axios.post(`${API_BASE_URL}/send-mail/${email}/`),

  // Submit form data with email and token
  submitForm: (email, token, formData) =>
    axios.post(`${API_BASE_URL}/submit-form/${email}/${token}/`, formData),
};

export default API; // ✅ FIXED default export
