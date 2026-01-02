const API_BASE = import.meta.env.VITE_API_BASE_URL;

import ScoreCard from "../components/ScoreCard";
import SkillMatch from "../components/SkillMatch";

export default function Result({ data, resumeSkills, jobSkills }) {
  return (
  <div className="mt-8 border-t pt-8">
    <ScoreCard score={data.ats_score} label={data.label} />

    <SkillMatch
      matched={data.matched_skills}
      missing={data.missing_skills}
    />

    <div className="bg-gray-50 border rounded-lg p-4 mb-6">
      <h3 className="font-semibold text-gray-800 mb-2">
        Suggestions
      </h3>
      <p className="text-sm text-gray-700 whitespace-pre-line">
        {data.ai_suggestions}
      </p>
    </div>
<button
  onClick={async () => {
    const res = await fetch(
      `${API_BASE}/analysis/download-report`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          resume_skills: resumeSkills,
          job_skills: jobSkills,
        }),
      }
    );

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "ATS_Report.pdf";
    a.click();
  }}
  className="w-full bg-green-600 hover:bg-green-700 text-white py-3 rounded-lg font-semibold transition"
    >
      Download PDF Report
    </button>
  </div>
);
}
