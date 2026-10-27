import { NavLink, Route, Routes, Link } from "react-router-dom";
import { Landing } from "./pages/Landing";
import { Chat } from "./pages/Chat";
import { CheckIn } from "./pages/CheckIn";
import { Insights } from "./pages/Insights";
import { Toolkit } from "./pages/Toolkit";
import "./styles.css";

const links = [["/chat", "Talk it out"], ["/check-in", "Check-in"], ["/insights", "Insights"], ["/toolkit", "Toolkit"]];

export default function App() {
  return <div className="app-shell">
    <header className="topbar"><Link to="/" className="brand"><span className="brand-mark">✦</span><span>F.R.I.E.N.D.<small>emotional navigation</small></span></Link>
      <nav>{links.map(([to, label]) => <NavLink key={to} to={to} className={({ isActive }) => isActive ? "active" : ""}>{label}</NavLink>)}</nav>
      <Link to="/safety" className="safety-link">Safety & privacy</Link>
    </header>
    <main><Routes><Route path="/" element={<Landing />} /><Route path="/chat" element={<Chat />} /><Route path="/check-in" element={<CheckIn />} /><Route path="/insights" element={<Insights />} /><Route path="/toolkit" element={<Toolkit />} /><Route path="/safety" element={<Safety />} /></Routes></main>
    <footer><span>F.R.I.E.N.D. is a first-layer support tool, not a medical service.</span><span>Built for privacy-conscious reflection · SDG 3</span></footer>
  </div>;
}

function Safety() {
  return <section className="page narrow"><p className="eyebrow">A clear boundary</p><h1>Your wellbeing comes first.</h1><div className="info-card"><h2>Not an emergency service</h2><p>F.R.I.E.N.D. cannot diagnose, treat, or reliably assess risk. AI responses can be mistaken. If you are in immediate danger, contact local emergency services or a trusted person.</p><p><strong>In India:</strong> Tele-MANAS: <strong>14416</strong> · Emergency services: <strong>112</strong>. Verify availability for your location.</p></div><div className="info-card"><h2>Privacy by design</h2><p>This local demonstration stores mood entries in a local SQLite database. No account is required, and chat messages are not saved by the backend. Do not enter identifying or highly sensitive information. Delete mood entries whenever you wish.</p></div></section>;
}
