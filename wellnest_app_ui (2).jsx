// firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_AUTH_DOMAIN",
  projectId: "YOUR_PROJECT_ID",
  appId: "YOUR_APP_ID",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

export { auth, db };

// AuthContext.js
import React, { createContext, useContext, useEffect, useState } from "react";
import { onAuthStateChanged } from "firebase/auth";
import { auth } from "./firebase";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (currentUser) => {
      setUser(currentUser);
      setLoading(false);
    });
    return () => unsubscribe();
  }, []);

  return (
    <AuthContext.Provider value={{ user }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

// ProtectedRoute.js
import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

const ProtectedRoute = ({ children }) => {
  const { user } = useAuth();
  return user ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;

// App.js
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes, Link, useNavigate } from "react-router-dom";
import { AuthProvider, useAuth } from "./AuthContext";
import ProtectedRoute from "./ProtectedRoute";
import { signInWithEmailAndPassword, createUserWithEmailAndPassword } from "firebase/auth";
import { auth, db } from "./firebase";
import { addDoc, collection, onSnapshot, query, where, serverTimestamp } from "firebase/firestore";

const App = () => (
  <AuthProvider>
    <Router>
      <Routes>
        <Route path="/" element={<Splash />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/home" element={<ProtectedRoute><Home /></ProtectedRoute>} />
        <Route path="/appointments" element={<ProtectedRoute><Appointments /></ProtectedRoute>} />
        <Route path="/chatbot" element={<ProtectedRoute><ChatBot /></ProtectedRoute>} />
        <Route path="/symptoms" element={<ProtectedRoute><Symptoms /></ProtectedRoute>} />
      </Routes>
    </Router>
  </AuthProvider>
);

const Splash = () => {
  const navigate = useNavigate();
  useEffect(() => {
    const timer = setTimeout(() => navigate("/login"), 1500);
    return () => clearTimeout(timer);
  }, [navigate]);

  return <div className="flex items-center justify-center h-screen text-4xl font-bold">wellnest</div>;
};

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      navigate("/home");
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="flex flex-col items-center p-8">
      <h2 className="text-xl font-bold mb-4">Login to your Account</h2>
      <input className="border p-2 w-full mb-2" type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      <input className="border p-2 w-full mb-4" type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={handleLogin}>Sign In</button>
      <p className="mt-4">Don't have an account? <Link to="/signup" className="text-blue-600">Sign up</Link></p>
    </div>
  );
};

const Signup = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSignup = async () => {
    try {
      await createUserWithEmailAndPassword(auth, email, password);
      navigate("/home");
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="flex flex-col items-center p-8">
      <h2 className="text-xl font-bold mb-4">Create your Account</h2>
      <input className="border p-2 w-full mb-2" type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      <input className="border p-2 w-full mb-4" type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button className="bg-blue-600 text-white px-4 py-2 rounded" onClick={handleSignup}>Sign Up</button>
    </div>
  );
};

const Home = () => {
  const { user } = useAuth();
  const [entry, setEntry] = useState("");
  const [entries, setEntries] = useState([]);

  const handleAddEntry = async () => {
    if (!entry.trim()) return;
    await addDoc(collection(db, "journals"), {
      text: entry,
      timestamp: serverTimestamp(),
      uid: user.uid,
    });
    setEntry("");
  };

  useEffect(() => {
    if (!user) return;
    const q = query(collection(db, "journals"), where("uid", "==", user.uid));
    const unsubscribe = onSnapshot(q, (snapshot) => {
      const data = snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }));
      setEntries(data);
    });
    return () => unsubscribe();
  }, [user]);

  return (
    <div className="p-6">
      <h2 className="text-lg font-semibold mb-2">Hello! {user?.email}</h2>
      <textarea
        className="border p-2 w-full mb-2"
        value={entry}
        onChange={(e) => setEntry(e.target.value)}
        placeholder="Write your journal entry..."
      ></textarea>
      <button className="bg-green-500 text-white px-4 py-2 mb-4" onClick={handleAddEntry}>Add Entry</button>
      <h3 className="font-bold mb-2">Your Journal Entries</h3>
      <ul>
        {entries.map((item) => (
          <li key={item.id} className="mb-2 p-2 bg-gray-200 rounded">
            {item.text} <br /><small>{item.timestamp?.toDate().toLocaleString()}</small>
          </li>
        ))}
      </ul>
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
      <div className="mb-4 font-bold">Buddy - Chat Bot</div>
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
      <div className="mb-4 font-bold">Buddy - Symptom Checker</div>
      <div className="grid grid-cols-3 gap-4">
        {symptoms.map((symptom, idx) => (
          <div key={idx} className="bg-gray-200 p-2 rounded text-center">{symptom}</div>
        ))}
      </div>
    </div>
  );
};

export default App;
