// File: src/components/Navbar.jsx
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="p-4 bg-gray-800 text-white flex justify-between">
      <div className="font-bold">Task Manager</div>
      <div>
        <Link to="/dashboard" className="mr-4">Dashboard</Link>
        <button onClick={() => { localStorage.removeItem('token'); window.location.href = '/' }}>Logout</button>
      </div>
    </nav>
  );
}