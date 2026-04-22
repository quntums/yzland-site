import json
import itertools
import re
import random

# Variation pools
intro_variants = [
    "Experience the Sahara with a carefully designed journey across Morocco.",
    "Discover Morocco's desert landscapes with a premium guided tour.",
    "Travel through the Atlas Mountains into the Sahara desert.",
    "Embark on an unforgettable Moroccan desert adventure.",
    "Explore the golden dunes of the Sahara with expert local guides.",
    "Journey from the city to the serenity of the Sahara desert."
]

cta_variants = [
    "Check Availability",
    "Plan Your Trip",
    "Request Your Custom Tour",
    "Book Your Sahara Experience",
    "Reserve Your Spot"
]

highlight_variants = [
    ["Camel trekking", "Desert camp stay", "Atlas Mountains crossing"],
    ["Sunset camel ride", "Luxury camp", "Scenic mountain routes"],
    ["Guided desert journey", "Traditional camp", "Panoramic landscapes"],
    ["Camel caravan at dusk", "Private desert tent", "Atlas Mountain pass"],
    ["Sahara dune exploration", "Overnight campfire", "Cultural stops en route"]
]

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
    
    intro = random.choice(intro_variants)
    cta = random.choice(cta_variants)
    highlights = random.choice(highlight_variants)
    highlights_html = "\n        ".join([f"<li>{h}</li>" for h in highlights])

    content = f"""export const metadata = {{
  title: "{title}",
  description: "{description}",
}};

export default function Page() {{
  return (
    <main className="px-6 py-12 max-w-5xl mx-auto space-y-6">
      <h1 className="text-4xl font-bold">{title}</h1>
      <p className="text-gray-600">{intro}</p>

      <h2 className="text-2xl font-semibold">Highlights</h2>
      <ul className="text-gray-600">
        {highlights_html}
      </ul>

      <p className="text-xl font-bold">From €450 / person</p>

      <a href="/contact" className="inline-block mt-6 px-6 py-3 bg-black text-white rounded-xl">
        {cta}
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

print(f"Generated {len(files)} pages with content variation.")
