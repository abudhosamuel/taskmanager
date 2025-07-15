import { useState } from "react";
import api from "../api/axios";

const TaskForm = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [userId, setUserId] = useState(1); // default test user
  const [status, setStatus] = useState("pending");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("/tasks", {
        title,
        description,
        user_id: userId,
        status,
      });
      console.log("Task created:", response.data);
      // Clear form
      setTitle("");
      setDescription("");
    } catch (err) {
      console.error("Error creating task", err.response?.data || err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-6 bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Add New Task</h2>

      <input
        type="text"
        placeholder="Title"
        className="border p-2 w-full mb-2"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />

      <textarea
        placeholder="Description"
        className="border p-2 w-full mb-2"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <select
        className="border p-2 w-full mb-2"
        value={status}
        onChange={(e) => setStatus(e.target.value)}
      >
        <option value="pending">Pending</option>
        <option value="in_progress">In Progress</option>
        <option value="done">Done</option>
      </select>

      <input
        type="number"
        placeholder="User ID"
        className="border p-2 w-full mb-2"
        value={userId}
        onChange={(e) => setUserId(Number(e.target.value))}
      />

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Create Task
      </button>
    </form>
  );
};

export default TaskForm;
