// File: src/pages/Register.jsx
import { useState } from 'react';
import axios from 'axios';

export default function Register() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/auth/register', {
        name,
        email,
        password,
      });
      alert('User registered. Please login.');
      window.location.href = '/';
    } catch (err) {
      alert('Registration failed');
    }
  };

  return (
    <div className="p-10 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-6">Register</h2>
      <input type="text" placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} className="block w-full mb-4 p-2 border" />
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="block w-full mb-4 p-2 border" />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="block w-full mb-4 p-2 border" />
      <button onClick={handleRegister} className="bg-green-600 text-white px-4 py-2">Register</button>
    </div>
  );
}
