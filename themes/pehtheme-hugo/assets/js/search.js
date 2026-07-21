(function () {
    const form = document.getElementById("search");
    if (!form) return;

    const input = document.getElementById("search-query");
    const feedback = document.getElementById("search-feedback");
    const resultsList = document.getElementById("search-results");
    const indexUrl = form.dataset.indexUrl;
    const maximumResults = 8;
    let postsPromise;
    let debounceTimer;

    function normalise(value) {
        return String(value || "")
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .toLocaleLowerCase()
            .replace(/[^\p{L}\p{N}]+/gu, " ")
            .trim();
    }

    function loadPosts() {
        if (!postsPromise) {
            postsPromise = fetch(indexUrl, { credentials: "same-origin" })
                .then((response) => {
                    if (!response.ok) throw new Error(`Search index returned ${response.status}`);
                    return response.json();
                });
        }
        return postsPromise;
    }

    function occurrences(text, term) {
        let count = 0;
        let position = 0;
        while ((position = text.indexOf(term, position)) !== -1) {
            count += 1;
            position += term.length;
        }
        return count;
    }

    function rank(post, query, terms) {
        const title = normalise(post.title);
        const description = normalise(post.description);
        const taxonomy = normalise([...(post.tags || []), ...(post.categories || [])].join(" "));
        const content = normalise(post.content);
        const allText = `${title} ${taxonomy} ${description} ${content}`;

        if (!terms.every((term) => allText.includes(term))) return 0;

        let score = 0;
        if (title === query) score += 200;
        else if (title.includes(query)) score += 90;
        if (taxonomy.includes(query)) score += 50;
        if (description.includes(query)) score += 35;
        if (content.includes(query)) score += 10;

        terms.forEach((term) => {
            const titleWord = new RegExp(`(^| )${term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}`);
            if (titleWord.test(title)) score += 35;
            else if (title.includes(term)) score += 20;
            if (taxonomy.includes(term)) score += 15;
            if (description.includes(term)) score += 7;
            score += Math.min(occurrences(content, term), 5);
        });

        return score;
    }

    function excerpt(post, terms) {
        const description = String(post.description || "").replace(/\s+/g, " ").trim();
        const body = String(post.content || "").replace(/\s+/g, " ").trim();
        const source = terms.some((term) => normalise(description).includes(term)) ? description : body;
        if (!source) return "";

        const sourceNormalised = normalise(source);
        const firstMatch = Math.min(...terms
            .map((term) => sourceNormalised.indexOf(term))
            .filter((position) => position >= 0));
        const start = Number.isFinite(firstMatch) ? Math.max(0, firstMatch - 70) : 0;
        const end = Math.min(source.length, start + 180);
        return `${start > 0 ? "…" : ""}${source.slice(start, end).trim()}${end < source.length ? "…" : ""}`;
    }

    function createResult(post, terms) {
        const item = document.createElement("li");
        item.className = "relative rounded-lg border border-zinc-200 bg-white p-4 hover:bg-zinc-100";

        const link = document.createElement("a");
        link.className = "block font-bold hover:underline";
        link.href = post.url;
        link.textContent = post.title;

        const meta = document.createElement("p");
        meta.className = "mt-2 text-xs text-zinc-500";
        const labels = [...(post.categories || []), ...(post.tags || [])].slice(0, 3);
        meta.textContent = [post.date, labels.join(" · ")].filter(Boolean).join(" · ");

        const summary = document.createElement("p");
        summary.className = "mt-2 text-sm text-zinc-500";
        summary.textContent = excerpt(post, terms);

        item.append(link, meta);
        if (summary.textContent) item.append(summary);
        return item;
    }

    function clearResults() {
        resultsList.replaceChildren();
        feedback.textContent = "";
    }

    async function search() {
        const query = normalise(input.value);
        const terms = [...new Set(query.split(" ").filter(Boolean))];
        if (!query) {
            clearResults();
            return;
        }
        if (query.length < 2) {
            resultsList.replaceChildren();
            feedback.textContent = "Enter at least two characters to search.";
            return;
        }

        feedback.textContent = "Searching…";
        try {
            const posts = await loadPosts();
            if (query !== normalise(input.value)) return;

            const ranked = posts
                .map((post) => ({ post, score: rank(post, query, terms) }))
                .filter((result) => result.score > 0)
                .sort((a, b) => b.score - a.score || b.post.dateISO.localeCompare(a.post.dateISO));

            resultsList.replaceChildren(...ranked.slice(0, maximumResults).map(({ post }) => createResult(post, terms)));
            if (!ranked.length) {
                feedback.textContent = `No posts found for “${input.value.trim()}”.`;
            } else if (ranked.length > maximumResults) {
                feedback.textContent = `Showing the best ${maximumResults} of ${ranked.length} posts for “${input.value.trim()}”.`;
            } else {
                feedback.textContent = `${ranked.length} ${ranked.length === 1 ? "post" : "posts"} found for “${input.value.trim()}”.`;
            }
        } catch (error) {
            console.error(error);
            resultsList.replaceChildren();
            feedback.textContent = "Search is temporarily unavailable. Please try again.";
            postsPromise = undefined;
        }
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        window.clearTimeout(debounceTimer);
        search();
    });

    input.addEventListener("input", () => {
        window.clearTimeout(debounceTimer);
        debounceTimer = window.setTimeout(search, 180);
    });

    input.addEventListener("keydown", (event) => {
        if (event.key === "ArrowDown") {
            const firstResult = resultsList.querySelector("a");
            if (firstResult) {
                event.preventDefault();
                firstResult.focus();
            }
        } else if (event.key === "Escape") {
            if (input.value) {
                input.value = "";
                clearResults();
            }
        }
    });

    resultsList.addEventListener("keydown", (event) => {
        if (!event.target.matches("a")) return;
        const links = [...resultsList.querySelectorAll("a")];
        const current = links.indexOf(event.target);
        if (event.key === "ArrowDown" && current < links.length - 1) {
            event.preventDefault();
            links[current + 1].focus();
        } else if (event.key === "ArrowUp") {
            event.preventDefault();
            (links[current - 1] || input).focus();
        } else if (event.key === "Escape") {
            input.focus();
        }
    });
})();
