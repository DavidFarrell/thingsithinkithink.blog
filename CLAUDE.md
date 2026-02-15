# Blog - thingsithinkithink.blog

## Build and Deploy

Use `./build.sh "commit message"` to build and deploy. The script:
1. Runs `npm run build` (Tailwind CSS)
2. Runs `hugo --gc --minify` (production build)
3. Commits everything
4. Pushes to GitHub

The GitHub Action uploads `./public` directly - it does NOT run Hugo, so the local build must happen first.

**Do NOT commit after running `hugo server`** - it writes localhost:1313 URLs into `public/`. Always use `./build.sh` or `hugo --gc --minify` for production builds.

**Build script location:** `./build.sh` in the blog root.

## Images

- Blog post images go in `assets/images/` (not `static/images/`) so Hugo can process them and generate `_hu_` variants
- Use Hugo figure shortcodes: `{{< figure src="/images/..." caption="..." >}}`

## Style

- No em dashes. Use ` - ` (space-hyphen-space) instead of `—` or `–`
- British English spelling

## Writing Style & Tone

*This section captures patterns from David's editing feedback to help get drafts closer to right first time.*

### Voice
- First person, conversational but thoughtful
- Not authoritative or lecturing - uses "I think", "my gut tells me", "I feel like"
- Draws on personal experience alongside industry observations
- Links to specific sources (podcasts with timestamps, articles, studies)
- **Understated, not grandiose.** Never use words like "eerily", "striking", "remarkable". David's style is to state observations plainly and let the reader draw conclusions
- **Don't narrate the discovery process.** Don't say "Altar noticed that..." or "What surprised me is..." - just state the fact directly. "For example, the phrase X appears repeatedly across Y" not "Altar noticed that X kept appearing"
- **Don't invent pithy summary lines.** No "Writer to director. Coder to reviewer." taglines. David doesn't do punchy parallel constructions that announce the insight. Show the parallel by describing what's happening, don't announce that a parallel exists

### Structure
- Hugo frontmatter with title, date, slug, description, categories, tags, image, draft
- Slug format: `/MM-DD-slug-words/`
- Posts end with a `## thingsithinkithink` section - bullet-pointed personal takes/opinions
- Cross-references previous blog posts where relevant
- **Descriptions/loglines are invitations, not summaries.** Casual and understated ("some interesting stuff from X on Y"). Don't give away the thesis. Credit the source. Don't oversell
- **Section headings should sound natural**, like something you'd say in conversation ("We still haven't figured out how to handle copyright") not like newspaper headlines ("Copyright and the question that won't go away")

### Content Patterns
- References specific sources with hyperlinks
- Builds arguments through personal anecdote + industry evidence
- Doesn't overstate claims - hedges appropriately
- **Use David's actual words and analogies.** When David dictates an outline, his phrasing, analogies (e.g. balloon animals), and sentence constructions are the content. Don't paraphrase them into more "writerly" language - his voice IS the style. Claude's job is to organise and lightly polish, not rewrite
- **Prefer present tense over past.** "Prolific writers publish multiple books a year" not "Prolific writers have historically published multiple books a year"
- **Tighten aggressively.** Two short sentences can often be one. Prefer ` - ` joins over full stops when the second thought is a continuation. Cut throat-clearing phrases ("It turns out", "What's interesting is", "The thing is")
- **When attributing observations to the wider community**, use "as many have commented" or "a view you see online" rather than centring David as the one who noticed it
- **Bridging paragraphs between sections** should set up the reader's expectations before the next section subverts or develops them (e.g. "I was expecting only negative perspectives. But there was more nuance than anticipated")

## Editing Feedback Log

*Record David's editing feedback here so future sessions can learn from it.*

### 2026-02-15 - Like a Ragged Prayer
- **Feedback:** Description/logline was too grandiose and thesis-driven. David replaced "AI is reshaping the romance novel industry, and the patterns are eerily familiar to anyone watching what's happening in software engineering, games, and other creative fields" with "Some interesting stuff from Alexandra Alter on how AI is disrupting the romance novel industry."
- **Pattern:** Post descriptions should be **invitations, not summaries**. Keep them casual and understated ("some interesting stuff") rather than trying to sell the reader on a Big Insight. Don't give away the thesis. Don't oversell. Credit the source rather than centring your own analysis. Words like "eerily" are too presumptuous.
