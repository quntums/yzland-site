import json
import itertools
import re

durations = ["2 day", "3 day", "4 day"]
routes = ["marrakech to merzouga", "fes to sahara", "casablanca desert"]
styles = ["luxury", "private", "budget"]

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

files = []

for d, r, s in itertools.product(durations, routes, styles):
    keyword = f"{d} {r} {s} tour morocco"
    slug = slugify(keyword)

    title = keyword.title()
    description = f"Book a {keyword} with camel trekking and desert camp experience."

    content = f"""export const metadata = {{
  title: "{title}",
  description: "{description}",
}};

export default function Page() {{
  return (
    <main className="px-6 py-12 max-w-5xl mx-auto space-y-6">
      <h1 className="text-4xl font-bold">{title}</h1>
      <p className="text-gray-600">{description}</p>

      <h2 className="text-2xl font-semibold">Highlights</h2>
      <ul className="text-gray-600">
        <li>Camel trekking</li>
        <li>Luxury desert camp</li>
        <li>Atlas Mountains journey</li>
      </ul>

      <p className="text-xl font-bold">From €450 / person</p>

      <a href="/contact" className="inline-block mt-6 px-6 py-3 bg-black text-white rounded-xl">
        Check Availability
      </a>

      <div className="text-sm mt-6">
        <a href="/tours/sahara-3-days">View Full Tour Details</a>
      </div>
    </main>
  );
}}
"""

    files.append({
        "path": f"app/{slug}/page.tsx",
        "content": content
    })

output = {
    "project_name": "yzland-site",
    "files": files
}

with open("architect_output.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Generated {len(files)} pages.")
