export const metadata = {
  title: "2 Day Casablanca Desert Budget Tour Morocco",
  description: "Book a 2 day casablanca desert budget tour morocco with camel trekking and desert camp experience.",
};

export default function Page() {
  return (
    <main className="px-6 py-12 max-w-5xl mx-auto space-y-6">
      <h1 className="text-4xl font-bold">2 Day Casablanca Desert Budget Tour Morocco</h1>
      <p className="text-gray-600">Book a 2 day casablanca desert budget tour morocco with camel trekking and desert camp experience.</p>

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
}
