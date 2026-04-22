import json
import re

# Starter keyword bank (20 topics)
keywords = [
    "best time to visit morocco desert",
    "how many days for sahara tour",
    "is 3 day desert tour enough",
    "what to pack for sahara desert",
    "what to wear in morocco desert",
    "do you need a guide in morocco",
    "is morocco safe for tourists",
    "is sahara desert tour safe",
    "morocco travel tips for foreigners",
    "what is a desert camp like",
    "camel trekking experience morocco",
    "merzouga vs zagora desert",
    "sahara desert weather by month",
    "how to book a sahara tour",
    "morocco desert tour cost",
    "luxury vs budget sahara tour",
    "family sahara desert tour morocco",
    "solo travel morocco desert",
    "photography tips sahara desert",
    "traditional food in sahara tour"
]

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

files = []

for kw in keywords:
    slug = slugify(kw)
    title = kw.title()
    description = f"Guide: {kw} with expert travel tips for Morocco."

    content = f"""export const metadata = {{
  title: "{title}",
  description: "{description}",
}};

export default function Page() {{
  return (
    <main className="px-6 py-12 max-w-3xl mx-auto space-y-6">
      <h1 className="text-4xl font-bold">{title}</h1>

      <p className="text-gray-600">
        {kw.capitalize()} is one of the most common questions travelers ask when planning a Morocco trip.
      </p>

      <h2 className="text-2xl font-semibold">Key Insights</h2>
      <p className="text-gray-600">
        Understanding this topic helps you plan a better Sahara desert experience.
      </p>

      <h2 className="text-2xl font-semibold">Expert Advice</h2>
      <p className="text-gray-600">
        Choosing the right tour and preparation ensures a smooth and memorable journey.
      </p>

      <a href="/tours/sahara-3-days" className="inline-block mt-6 px-6 py-3 bg-black text-white rounded-xl">
        Explore Sahara Tours
      </a>
    </main>
  );
}}
"""

    files.append({
        "path": f"app/blog/{slug}/page.tsx",
        "content": content
    })

# Also update the blog index to list all generated posts
index_content = """export default function Page() {
  return (
    <main className='px-6 py-12 max-w-5xl mx-auto'>
      <h1 className='text-4xl font-bold'>Morocco Travel Guides</h1>
      <p className='text-gray-600 mt-4'>
        Expert tips and insights for planning your Morocco journey.
      </p>
      <ul className='mt-8 space-y-4'>
"""

for kw in keywords:
    slug = slugify(kw)
    title = kw.title()
    index_content += f"        <li><a href='/blog/{slug}' className='text-blue-600 hover:underline'>{title}</a></li>\n"

index_content += """      </ul>
    </main>
  );
}"""

files.append({
    "path": "app/blog/page.tsx",
    "content": index_content
})

output = {
    "project_name": "yzland-site",
    "files": files
}

with open("architect_output.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Generated {len(files)-1} blog posts + updated index.")
