export default function UploadResume({ onUpload }) {
  return (
    <div className="mb-6">
      <label className="block text-sm font-medium text-gray-700 mb-2">
        Upload Resume (PDF / DOCX)
      </label>

      <input
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => onUpload(e.target.files[0])}
        className="block w-full text-sm text-gray-600
          file:mr-4 file:py-2 file:px-4
          file:rounded-lg file:border-0
          file:text-sm file:font-semibold
          file:bg-blue-50 file:text-blue-700
          hover:file:bg-blue-100"
      />
    </div>
  );
}
