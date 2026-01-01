export default function ScoreCard({ score, label }) {
  return (
    <div className="bg-blue-50 border border-blue-200 rounded-xl p-6 text-center mb-6">
      <p className="text-sm text-gray-600 mb-1">ATS Match Score</p>
      <p className="text-5xl font-bold text-blue-600">{score}%</p>
      <p className="mt-2 text-sm font-medium text-gray-700">
        {label}
      </p>
    </div>
  );
}
