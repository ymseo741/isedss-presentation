
const fs = require('fs');

try {
    const content = fs.readFileSync('presentation.html', 'utf8');

    // Find all slide divs
    // We'll use a regex to split or find matches. 
    // Since we need to process them, let's find indices of <div class="slide

    // Regex for finding slide start
    const slideRegex = /<div class="slide/g;
    let match;
    const slideStarts = [];

    while ((match = slideRegex.exec(content)) !== null) {
        slideStarts.push(match.index);
    }

    const slides = [];
    for (let i = 0; i < slideStarts.length; i++) {
        const start = slideStarts[i];
        const end = (i + 1 < slideStarts.length) ? slideStarts[i + 1] : content.length;
        slides.push(content.substring(start, end));
    }

    console.log("# Presentation Analysis Report");
    console.log(`**File:** \`presentation.html\``);
    console.log(`**Total Slides:** ${slides.length}`);
    console.log("\n## Slide Overview");
    console.log("| Index | Slide Number | Title |");
    console.log("| :--- | :--- | :--- |");

    slides.forEach((slideContent, i) => {
        let title = "No Title";
        let slideNum = "-";

        // Extract H1
        const h1Match = slideContent.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
        if (h1Match) {
            let rawTitle = h1Match[1];
            // Remove tags
            title = rawTitle.replace(/<[^>]+>/g, '').trim();

            // Extract number from title
            const numMatch = title.match(/^(\d+)\./);
            if (numMatch) {
                slideNum = numMatch[1];
            }
        }

        // Fallback title check (if h1 didn't work or for title slide)
        if (title === "No Title") {
            // Maybe it's the title slide
            if (slideContent.includes('title-slide')) {
                const heroH1 = slideContent.match(/<h1>([\s\S]*?)<br>/i); // specialized for title slide
                if (heroH1) {
                    title = heroH1[1].replace(/<[^>]+>/g, '').trim();
                }
            }
        }

        // Extract Page Number from footer
        // <div class="footer">...<span>Page 01</span></div>
        const footerMatch = slideContent.match(/class="footer"[^>]*>([\s\S]*?)<\/div>/i);
        if (footerMatch) {
            const footerContent = footerMatch[1];
            const spanMatches = [...footerContent.matchAll(/<span>([\s\S]*?)<\/span>/g)];
            if (spanMatches.length > 0) {
                const lastSpan = spanMatches[spanMatches.length - 1][1];
                if (lastSpan.includes('Page')) {
                    slideNum = lastSpan.replace('Page', '').trim();
                } else if (!isNaN(parseInt(lastSpan.trim()))) {
                    slideNum = lastSpan.trim();
                }
            }
        }

        // Clean title
        title = title.replace(/\n/g, ' ').replace(/\s+/g, ' ');
        if (title.length > 60) {
            title = title.substring(0, 57) + "...";
        }

        console.log(`| ${i} | ${slideNum} | ${title} |`);
    });

} catch (e) {
    console.error("Error:", e.message);
}
