import { useEffect, useState } from "react";
import api from "../api/axios";

const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [userId, setUserId] = useState(1); // default user ID
  const [loading, setLoading] = useState(true);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const res = await api.get(`/tasks/user/${userId}`);
      setTasks(res.data);
    } catch (err) {
      console.error("Failed to load tasks:", err.response?.data || err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, [userId]);

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Tasks for User {userId}</h2>

      <input
        type="number"
        value={userId}
        onChange={(e) => setUserId(Number(e.target.value))}
        className="border p-2 mb-4 w-full"
        placeholder="User ID"
      />

      {loading ? (
        <p>Loading...</p>
      ) : tasks.length === 0 ? (
        <p>No tasks found.</p>
      ) : (
        <ul className="space-y-2">
          {tasks.map((task) => (
            <li key={task.id} className="border p-3 rounded">
              <div className="font-semibold">{task.title}</div>
              <div className="text-sm text-gray-700">{task.description}</div>
              <div className="text-xs text-gray-500 mt-1">Status: {task.status}</div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TaskList;
