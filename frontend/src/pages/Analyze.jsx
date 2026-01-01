import { useState } from "react";
import UploadResume from "../components/UploadResume";
import JobDescription from "../components/JobDescription";
import { uploadResume, fullAnalysis } from "../services/api";
import Result from "./Result";

export default function Analyze() {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
const [resumeSkills, setResumeSkills] = useState([]);
const [jobSkills, setJobSkills] = useState([]);

  const handleAnalyze = async () => {
    if (!file || !jobDesc) {
      alert("Please upload resume and add job description");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      // 1️⃣ Upload resume
      const resumeRes = await uploadResume(file);
setResumeSkills(resumeRes.skills);


      // 2️⃣ Extract job skills
      const jobSkillsRes = await fetch(
        `http://127.0.0.1:8000/analysis/job-skills?job_description=${encodeURIComponent(jobDesc)}`,
        { method: "POST" }
      );

      if (!jobSkillsRes.ok) {
        throw new Error("Job skill extraction failed");
      }

      const jobSkillsData = await jobSkillsRes.json();
setJobSkills(jobSkillsData.job_skills);

      // 3️⃣ Full analysis
      const analysis = await fullAnalysis(
        resumeRes.skills,
        jobSkillsData.job_skills
      );

      setResult(analysis);
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Check console.");
    } finally {
      setLoading(false);
    }
  };
return (
  <div className="max-w-3xl mx-auto px-4">
    <div className="bg-white rounded-xl shadow-lg p-8">
      <h2 className="text-xl font-semibold text-gray-800 mb-6">
        Analyze Your Resume
      </h2>

      <UploadResume onUpload={setFile} />
      <JobDescription value={jobDesc} onChange={setJobDesc} />

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="w-full mt-4 bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-semibold transition disabled:opacity-50"
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {error && (
        <p className="text-red-600 text-sm mt-4">{error}</p>
      )}

      {result && (
        <Result
          data={result}
          resumeSkills={resumeSkills}
          jobSkills={jobSkills}
        />
      )}
    </div>
  </div>
);

}
