import Analyze from "./pages/Analyze";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow">
        <div className="max-w-5xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-blue-600">
            HireLens AI
          </h1>
          <p className="text-sm text-gray-500">
            AI-powered ATS Resume Analyzer
          </p>
        </div>
      </header>

      <main className="py-10">
        <Analyze />
      </main>
    </div>
  );
}
