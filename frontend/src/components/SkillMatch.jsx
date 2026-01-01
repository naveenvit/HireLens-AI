export default function SkillMatch({ matched, missing }) {
  return (
    <div className="grid grid-cols-2 gap-6 mb-6">
      <div>
        <h3 className="font-semibold text-green-700 mb-2">
          Matched Skills
        </h3>
        <ul className="space-y-1 text-sm">
          {matched.map((s) => (
            <li key={s} className="bg-green-50 px-3 py-1 rounded">
              {s}
            </li>
          ))}
        </ul>
      </div>

      <div>
        <h3 className="font-semibold text-red-700 mb-2">
          Missing Skills
        </h3>
        <ul className="space-y-1 text-sm">
          {missing.map((s) => (
            <li key={s} className="bg-red-50 px-3 py-1 rounded">
              {s}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
