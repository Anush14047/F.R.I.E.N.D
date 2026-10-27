import { Link } from "react-router-dom";
export function Landing() {
  return <section className="page landing"><div className="hero"><div><p className="eyebrow">A softer place to land</p><h1>Make space for<br /><em>what you feel.</em></h1><p className="lede">F.R.I.E.N.D. helps you pause, name the moment, and find one kind next step — privately and at your own pace.</p><div className="actions"><Link className="button primary" to="/chat">Start a conversation <span>→</span></Link><Link className="button quiet" to="/check-in">Log your mood</Link></div></div><div className="orb"><div className="orb-inner"><span>how are<br />you, really?</span></div></div></div>
    <div className="feature-grid"><article><span className="feature-icon">◌</span><h3>Talk it through</h3><p>Warm, thoughtful prompts that help you put feelings into words.</p></article><article><span className="feature-icon">↗</span><h3>Notice patterns</h3><p>See your mood history as a gentle reflection, never a diagnosis.</p></article><article><span className="feature-icon">◒</span><h3>Find your reset</h3><p>Breathing, grounding, and small practices for the next few minutes.</p></article></div>
    <div className="privacy-strip"><strong>Private by default.</strong><span>Local demo mode needs no account or paid AI key.</span><Link to="/safety">Read our boundaries →</Link></div>
  </section>;
}
