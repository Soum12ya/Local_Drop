const products = [
  {emoji:"🏺",title:"Bankura Terracotta Horse",price:"₹299",distance:"42 km",time:"45–60 min",tag:"Made near you"},
  {emoji:"🍯",title:"Forest Honey",price:"₹349",distance:"31 km",time:"35–50 min",tag:"Local favorite"},
  {emoji:"🧵",title:"Handwoven Stole",price:"₹799",distance:"27 km",time:"40–55 min",tag:"New today"},
];

export default function Home(){
  return (
    <main className="min-h-screen px-5 py-7 md:px-14">
      <header className="mx-auto flex max-w-6xl items-center justify-between">
        <div className="text-xl font-black tracking-tight">LOCALDROP</div>
        <div className="rounded-full bg-[#efe7d8] px-4 py-2 text-sm text-[#1b7759]">📍 Durgapur</div>
      </header>

      <section className="mx-auto max-w-6xl pt-14">
        <p className="text-sm font-bold uppercase tracking-widest text-[#1b7759]">Discover what your city has been hiding.</p>
        <h1 className="mt-3 max-w-3xl text-5xl font-black leading-tight md:text-7xl">What’s interesting today?</h1>
        <p className="mt-5 max-w-2xl text-lg text-gray-500">Unique products from local makers, discovered near you and delivered locally.</p>

        <div className="mt-8 flex flex-wrap gap-3">
          <button className="rounded-full bg-[#1b7759] px-5 py-3 font-bold text-white">🎲 Surprise Me</button>
          <button className="rounded-full bg-white px-5 py-3 font-semibold shadow-sm">🔥 Trending nearby</button>
          <button className="rounded-full bg-white px-5 py-3 font-semibold shadow-sm">🎁 Gifts under ₹500</button>
          <button className="rounded-full bg-white px-5 py-3 font-semibold shadow-sm">🆕 New today</button>
        </div>
      </section>

      <section className="mx-auto max-w-6xl py-12">
        <div className="grid gap-5 md:grid-cols-3">
          {products.map(p=>(
            <article key={p.title} className="overflow-hidden rounded-3xl bg-white shadow-sm ring-1 ring-black/5">
              <div className="flex h-64 items-center justify-center bg-[#efe7d8] text-8xl">{p.emoji}</div>
              <div className="p-6">
                <span className="rounded-full bg-[#efe7d8] px-3 py-1 text-xs font-bold text-[#1b7759]">{p.tag}</span>
                <h2 className="mt-4 text-xl font-black">{p.title}</h2>
                <p className="mt-2 text-sm text-gray-500">{p.distance} away • {p.time}</p>
                <div className="mt-5 flex items-center justify-between">
                  <span className="text-xl font-black">{p.price}</span>
                  <button className="rounded-full bg-[#1b7759] px-4 py-2 text-sm font-bold text-white">View</button>
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="mx-auto max-w-6xl rounded-3xl bg-[#1f2325] p-8 text-white md:p-12">
        <p className="text-sm font-bold uppercase tracking-widest text-[#69c7a4]">The LocalDrop loop</p>
        <h2 className="mt-3 text-3xl font-black">Discover → Get curious → Buy → Receive → Share</h2>
        <p className="mt-4 max-w-2xl text-gray-300">The more you discover, save, buy and share, the better the next local feed becomes.</p>
      </section>
    </main>
  );
}
