# Implementation Plan: Refinement of Slides 01-4 and 11-1

This plan addresses layout overflow issues and technical depth/readability improvements as requested by the user.

## Proposed Changes

### 1. Slide 01-4 (Decision Intelligence Framework)
- **Goal**: Fix diagram overflow.
- **Changes**:
  - Add `max-height: 380px;` and `display: flex; flex-direction: column; justify-content: center;` to the diagram container.
  - Apply `transform: scale(0.9); transform-origin: top center;` to the `.mermaid` div if necessary, or simply ensure the container constrains it.
  - Adjust margins to prevent the diagram from hitting the footer.

### 2. Slide 11-1 (Global Standard & Regulation Compliance)
- **Goal**: Increase readability (font size) and technical sophistication.
- **Changes**:
  - Increase `h3` font-size from `14px` to `16px`.
  - Increase `p` font-size from `11px` to `13px`.
  - Increase `table` font-size from `10px` to `11.5px`.
  - **Content Enhancement**:
    - Elaborate on **MSC.1/Circ.1238** to include "Validation via Advanced Evacuation Analysis (AEA) and fire/smoke interaction modeling".
    - Elaborate on **NMEA 2000** to include "Seamless PGN (Parameter Group Number) mapping for engine/AIS/GPS data harvesting".
    - Elaborate on **ISO 23611** to include "Hardware hardening for VDR (Voyage Data Recorder) level reliability in extreme maritime conditions".

### 3. [MODIFY] [presentation.html](file:///Users/seo/.gemini/antigravity/brain/5fa3caba-c837-49e5-8344-a4fa3ac58405/presentation.html)
- Apply the CSS and content changes mentioned above.

## Verification Plan

### Automated Tests
- None.

### Manual Verification
1. **Browser Review**:
   - Navigate to Slide 01-4 (Page 05). Confirm the Mermaid diagram is fully visible and doesn't overlap the footer.
   - Navigate to Slide 11-1 (Page 25). Confirm the text is larger and more readable.
   - Verify that the layout remains balanced (16:9) after font size increases.
