import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes, Link, useNavigate } from "react-router-dom";

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Splash />} />
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/home" element={<Home />} />
      <Route path="/appointments" element={<Appointments />} />
      <Route path="/chatbot" element={<ChatBot />} />
      <Route path="/symptoms" element={<Symptoms />} />
    </Routes>
  </Router>
);

const Splash = () => {
  const navigate = useNavigate();
  setTimeout(() => navigate("/login"), 1500);
  return <div className="flex items-center justify-center h-screen text-4xl font-bold">wellnest</div>;
};

const Login = () => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col items-center p-8">
      <h2 className="text-xl font-bold mb-4">Login to your Account</h2>
      <input className="border p-2 w-full mb-2" type="email" placeholder="Email" />
      <input className="border p-2 w-full mb-4" type="password" placeholder="Password" />
      <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={() => navigate("/home")}>Sign In</button>
      <p className="mt-4">Don't have an account? <Link to="/signup" className="text-blue-600">Sign up</Link></p>
    </div>
  );
};

const Signup = () => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col items-center p-8">
      <h2 className="text-xl font-bold mb-4">Create your Account</h2>
      <input className="border p-2 w-full mb-2" type="email" placeholder="Email" />
      <input className="border p-2 w-full mb-2" type="password" placeholder="Password" />
      <input className="border p-2 w-full mb-4" type="password" placeholder="Confirm Password" />
      <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={() => navigate("/home")}>Sign Up</button>
    </div>
  );
};

const Home = () => {
  return (
    <div className="p-6">
      <h2 className="text-lg font-semibold mb-2">Hello! Riya Shah</h2>
      <div className="mb-4">Heart Rate: <span className="font-bold">97 bpm</span></div>
      <h3 className="font-bold mb-2">Services</h3>
      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="p-4 bg-blue-100">Medical</div>
        <div className="p-4 bg-pink-100">Therapy</div>
        <div className="p-4 bg-yellow-100">Counseling</div>
        <div className="p-4 bg-purple-100">AI Chat Bot</div>
      </div>
      <Link to="/appointments" className="block text-center bg-gray-300 p-2 rounded">View Appointments</Link>
    </div>
  );
};

const Appointments = () => {
  return (
    <div className="p-6">
      <h2 className="text-lg font-semibold mb-2">Upcoming Appointments</h2>
      <div className="bg-blue-200 p-2 mb-2">Wed 13 - 10:45 AM - Dr. Mini Akther (Depression)</div>
      <div className="bg-orange-200 p-2 mb-4">Tue 20 - 09:25 AM - Dr. Akshaya Kumar (Gynaecologist)</div>
      <h2 className="text-lg font-semibold mb-2">Latest Appointments</h2>
      <div className="bg-pink-200 p-2 mb-2">Mon 7 - 11:45 AM - Dr. Mini Akther</div>
      <div className="bg-purple-200 p-2">Fri 15 - 07:20 PM - Dr. Daman Aggarwal</div>
    </div>
  );
};

const ChatBot = () => {
  const [message, setMessage] = useState("");
  return (
    <div className="p-6">
      <div className="mb-4">Buddy - Chat Bot</div>
      <div className="bg-gray-100 p-4 rounded mb-2">Hi! how are you feeling today?</div>
      <input
        className="border p-2 w-full"
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type here..."
      />
    </div>
  );
};

const Symptoms = () => {
  const symptoms = ["Anxiety", "Fatigue", "Headache", "Stomachache", "Fever", "Cough", "Joint Pain", "Itchy Eyes", "Others"];
  return (
    <div className="p-6">
      <div className="mb-4">Hi! how are you feeling today?</div>
      <div className="grid grid-cols-3 gap-4">
        {symptoms.map((symptom, idx) => (
          <div key={idx} className="bg-gray-200 p-2 rounded text-center">{symptom}</div>
        ))}
      </div>
    </div>
  );
};

export default App;
