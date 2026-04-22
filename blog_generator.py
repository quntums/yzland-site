import json
import re
import random

# Variation pools
intro_variants = [
    "is a key consideration when planning a trip to Morocco. Understanding this will help you make better travel decisions.",
    "is one of the most common questions travelers ask before visiting the Sahara. Getting it right makes all the difference.",
    "can significantly impact your comfort and overall experience in the Moroccan desert. Here's what you need to know.",
    "is often overlooked by first‑time visitors, but it's essential for a smooth and memorable journey.",
    "deserves careful thought before you embark on a Moroccan adventure. Our guide breaks it down."
]

tips_variants = [
    ["Plan ahead during peak seasons", "Choose a trusted local operator", "Prepare for temperature variations"],
    ["Book accommodations early", "Pack light but smart", "Stay hydrated throughout the day"],
    ["Confirm your itinerary in advance", "Bring a power bank for your devices", "Learn a few basic Arabic phrases"],
    ["Check weather forecasts regularly", "Inform your bank about travel plans", "Carry cash for small purchases"],
    ["Respect local customs and dress codes", "Always have travel insurance", "Keep digital copies of important documents"]
]

faq_variants = [
    {"question": "Is this important for first‑time visitors?", "answer": "Yes, understanding this topic helps you avoid common mistakes and enjoy a stress‑free trip."},
    {"question": "Can I figure this out on arrival?", "answer": "It's possible, but planning ahead saves time and often money."},
    {"question": "What's the biggest mistake travelers make?", "answer": "Underestimating the importance of preparation in the desert environment."}
]

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

    intro = random.choice(intro_variants)
    tips = random.choice(tips_variants)
    faq = random.choice(faq_variants)

    content = f"""export const metadata = {{
  title: "{title}",
  description: "{description}",
}};

export default function Page() {{
  return (
    <main className="px-6 py-12 max-w-3xl mx-auto space-y-8">
      <h1 className="text-4xl font-bold">{title}</h1>

      <p className="text-gray-600">
        {kw.capitalize()} {intro}
      </p>

      <h2 className="text-2xl font-semibold">Why It Matters</h2>
      <p className="text-gray-600">
        Many travelers overlook this aspect, but it directly impacts comfort, safety, and overall experience. Taking time to understand {kw} ensures you're well prepared.
      </p>

      <h2 className="text-2xl font-semibold">Detailed Guide</h2>
      <p className="text-gray-600">
        When planning a Sahara desert trip, consider weather conditions, logistics, and travel duration. Choosing the right itinerary based on {kw} leads to a smoother and more enjoyable adventure.
      </p>

      <h2 className="text-2xl font-semibold">Expert Tips</h2>
      <ul className="list-disc pl-6 text-gray-600 space-y-1">
        <li>{tips[0]}</li>
        <li>{tips[1]}</li>
        <li>{tips[2]}</li>
      </ul>

      <h2 className="text-2xl font-semibold">Frequently Asked Questions</h2>
      <p className="text-gray-600"><strong>{faq['question']}</strong> {faq['answer']}</p>

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

print(f"Generated {len(files)-1} long‑form blog posts + updated index.")
