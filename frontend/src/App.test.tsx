import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import App from "./App";
test("renders the F.R.I.E.N.D. landing page", () => { render(<MemoryRouter><App /></MemoryRouter>); expect(screen.getByText("Make space for")).toBeInTheDocument(); });
