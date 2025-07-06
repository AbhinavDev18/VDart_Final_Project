import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import DashboardTable from "./components/DashboardTable";
import FormPage from "./components/FormPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<DashboardTable />} />
        <Route path="/form" element={<FormPage />} />
      </Routes>
    </Router>
  );
}

export default App;
