import React, { useState } from "react";
import './styles/style.css'; 

const Home = () => {
  const [formType, setFormType] = useState("login");

  const switchForm = (type) => {
    setFormType(type);
  };

  const handleRegister = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
      username: formData.get('username'),
      email: formData.get('email'),
      password: formData.get('password'),
      confirmpassword: formData.get('confirmpassword')
    };

    const response = await fetch('http://localhost:5000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    alert(result.message);

    if (response.ok) {
      window.location.reload();
    }
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = {
      email: formData.get('email'),
      password: formData.get('password')
    };

    const response = await fetch('http://localhost:5000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    alert(result.message);

    if (response.ok) {
      window.location.href = 'http://localhost:5000/welcome';
    }
  };

  return (
    <div className="container">
      <div className="content-wrapper neumorphic">
        <div className="hero-section">
          <div className="logo-container">
            <svg className="logo" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
              <defs>
                <linearGradient id="leafGradient" x1="0%" y1="0%" x2="100%">
                  <stop offset="0%" style={{ stopColor: "#10B981", stopOpacity: 1 }} />
                  <stop offset="100%" style={{ stopColor: "#34D399", stopOpacity: 1 }} />
                </linearGradient>
                <linearGradient id="folderGradient" x1="0%" y1="0%" x2="100%">
                  <stop offset="0%" style={{ stopColor: "#3B82F6", stopOpacity: 1 }} />
                  <stop offset="100%" style={{ stopColor: "#60A5FA", stopOpacity: 1 }} />
                </linearGradient>
              </defs>
              <path d="M50,80 L250,80 L250,250 L50,250 Z" fill="url(#folderGradient)" />
              <path d="M50,80 L130,80 L150,50 L250,50 L250,80" fill="url(#folderGradient)" />
              <path d="M150,100 Q200,150 150,200 Q100,150 150,100" fill="url(#leafGradient)" />
              <path d="M140,170 A30,30 0 1,1 170,140" fill="none" stroke="#F59E0B" strokeWidth="10" strokeLinecap="round" />
              <path d="M170,200 A30,30 0 1,1 140,170" fill="none" stroke="#F59E0B" strokeWidth="10" strokeLinecap="round" />
              <path d="M200,170 A30,30 0 1,1 170,200" fill="none" stroke="#F59E0B" strokeWidth="10" strokeLinecap="round" />
              <polygon points="137,168 143,162 149,174" fill="#F59E0B" />
              <polygon points="172,203 166,197 178,191" fill="#F59E0B" />
              <polygon points="203,168 197,174 191,162" fill="#F59E0B" />
            </svg>
          </div>
          <h1>File Manager</h1>
          <p className="hero-text">
            Experience the future of cloud storage. Seamlessly manage your files with our eco-friendly, AI-powered platform designed for the modern digital age.
          </p>
          <div className="eco-badge glass">
            🌿 Zero Carbon • Smart Storage • Secure
          </div>
        </div>
        <div className="form-section">
          {formType === "login" ? (
            <div id="loginForm">
              <h2>Welcome Back</h2>
              <form onSubmit={handleLogin}>
                <div className="input-group">
                  <input type="email" name="email" id="email" placeholder="Email" required/>
                </div>
                <div className="input-group">
                  <input type="password" name="password" id="password" placeholder="Password" required />
                </div>
                <button type="submit" className="btn" name="signIn">Login</button>
              </form>
              <p className="switch-form" onClick={() => switchForm("register")}>New to File Manager? Join us!</p>
            </div>
          ) : (
            <div id="registerForm">
              <h2>Join File Manager</h2>
              <form onSubmit={handleRegister}>
                <div className="input-group">
                  <input type="text" name="username" id="username" placeholder="User name" required />
                </div>
                <div className="input-group">
                  <input type="email" name="email" id="email" placeholder="Email" required />
                </div>
                <div className="input-group">
                  <input type="password" name="password" id="password" placeholder="Password" required />
                </div>
                <div className="input-group">
                  <input type="password" name="confirmpassword" id="confirmpassword" placeholder="Confirm password" required />
                </div>
                <button type="submit" className="btn" value="Register" name="signUp">Create an Account</button>
              </form>
              <p className="switch-form" onClick={() => switchForm("login")}>Already a member? Log in</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Home;
