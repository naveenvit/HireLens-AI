export default function JobDescription({ value, onChange }) {
  return (
    <div className="mb-6">
      <label className="block text-sm font-medium text-gray-700 mb-2">
        Job Description
      </label>

      <textarea
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Paste the job description here..."
        className="w-full h-40 p-4 border border-gray-300 rounded-lg
          focus:outline-none focus:ring-2 focus:ring-blue-500
          resize-none text-sm"
      />
    </div>
  );
}
