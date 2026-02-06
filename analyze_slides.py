
import re
import sys

def analyze_presentation(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Split by slide div to be approximate but robust enough
    # Assuming <div class="slide ..."> or <div class="slide">
    
    # Find all slide blocks
    # We can use regex to find start indices of slides
    slide_starts = [m.start() for m in re.finditer(r'<div class="slide', content)]
    
    slides = []
    for i in range(len(slide_starts)):
        start = slide_starts[i]
        end = slide_starts[i+1] if i + 1 < len(slide_starts) else len(content)
        slides.append(content[start:end])

    print(f"# Presentation Analysis Report")
    print(f"**File:** `{file_path}`")
    print(f"**Total Slides:** {len(slides)}")
    print("\n## Slide Overview")
    print("| Index | Slide Number | Title |")
    print("| :--- | :--- | :--- |")

    for i, slide_content in enumerate(slides):
        title = "No Title"
        slide_num = "-"

        # Extract Header H1
        # Look for <header>...<h1>Title</h1>...</header> or just <h1> inside the slide
        
        # Simple regex for h1
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', slide_content, re.DOTALL | re.IGNORECASE)
        if h1_match:
            raw_title = h1_match.group(1)
            # Remove tags from title if any
            clean_title = re.sub(r'<[^>]+>', '', raw_title)
            title = clean_title.strip()
            
            # extract number
            num_match = re.match(r'(\d+)\.', title)
            if num_match:
                slide_num = num_match.group(1)

        # Check footer for page number
        # <div class="footer">...<span>Page 01</span></div>
        footer_match = re.search(r'class="footer"[^>]*>.*?<span>(.*?)</span>\s*</div>', slide_content, re.DOTALL | re.IGNORECASE)
        if footer_match:
             # The footer usually has two spans, we want the last one possibly?
             # My regex above grabs the content of the *last* span if it's greedy? No, non-greedy.
             # Let's simple check spans inside footer
             
             footer_content = footer_match.group(0)
             spans = re.findall(r'<span>(.*?)</span>', footer_content, re.DOTALL)
             if spans:
                 last_span = spans[-1]
                 if 'Page' in last_span:
                     slide_num = last_span.replace('Page', '').strip()
                 elif last_span.strip().isdigit():
                     slide_num = last_span.strip()

        # Clean title
        title = title.replace('\n', ' ').replace('\r', '')
        # Remove extra spaces
        title = re.sub(r'\s+', ' ', title).strip()
        
        if len(title) > 60:
            title = title[:57] + "..."
            
        print(f"| {i} | {slide_num} | {title} |")

if __name__ == "__main__":
    analyze_presentation(r"c:\Users\ODN\.gemini\antigravity\scratch\isedss-presentation-new\presentation.html")
