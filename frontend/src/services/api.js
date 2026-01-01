const API_BASE = import.meta.env.VITE_API_BASE_URL;

export const uploadResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/resume/upload`, {
    method: "POST",
    body: formData,
  });

  return res.json();
};

export async function fullAnalysis(resumeSkills, jobSkills) {
  const res = await fetch(`${API_BASE}/analysis/full-analysis`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      resume_skills: resumeSkills,
      job_skills: jobSkills,
    }),
  });

  return res.json();
}
