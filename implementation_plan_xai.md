# Enhancement Plan: XAI Visuals & Future Scope

## Goal
Replace the generic Mermaid diagram in "Slide 03-3: Explainable AI (XAI)" with a high-quality CSS/HTML visualization that demonstrates the "Black Box to Glass Box" concept. Additionally, propose further improvements for the presentation.

## User Review Required
- [ ] Approval of the new XAI visual design (implicit in request).
- [ ] Feedback on brainstormed ideas for future slides.

## Proposed Changes

### Slide 03-3: Explainable AI (XAI)
- **Current**: Mermaid graph (Input -> Model -> Decision -> Reason).
- **New Design**: 
    - **Concept**: "Opening the Black Box".
    - **Visual**: 
        - Left: "Raw Data" (Icons for Fire, Heat, Smoke).
        - Center: "AI Engine" (Gradient Box) -> splitting into "Feature Contribution" bars (CSS animated-style bars showing 'Temperature: 80%', 'CO2: 15%').
        - Right: "Trusted Decision" (Card with 'Evacuate Path A' and a checkmark).
    - **Style**: Use `flex-row`, `progress-bar` styles, and card layouts consistent with the "Ultra-Dense" theme.

### Brainstorming Additional Improvements
1.  **Safety Dashboard Mockup (CSS)**: A static HTML/CSS representation of the actual Crew Tablet UI to make it feel tangible.
2.  **Emergency Response Timeline**: A horizontal timeline showing the *speed* comparison between Human (5 min) vs AI (3 sec).
3.  **Global Standard Roadmap**: Visualizing the path from "Local Certification" to "IMO Standard" as a stairway or mountain climb.

## Verification
- **Visual Check**: Use `browser_subagent` to verify Slide 03-3 looks professional and aligns with the slide dimensions.
