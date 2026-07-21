// TOGGLE BUTTON
(function () {
	// Get all elements with the "toggle-button" class
    const toggleButtons = document.querySelectorAll(".toggle-button");

    function setExpanded(targetElement, expanded) {
        toggleButtons.forEach((button) => {
            const targetIds = button.getAttribute("data-target").split(" ");
            if (targetIds.includes(targetElement.id)) {
                button.setAttribute("aria-expanded", String(expanded));
            }
        });
    }

    function closeElement(element) {
        element.classList.remove("open");
        element.classList.add("close");
        setExpanded(element, false);
    }

    function hideAllExcept(targetElement) {
        document.querySelectorAll(".open").forEach((element) => {
            if (element !== targetElement) {
                closeElement(element);
            }
        });
    }

    // Function to toggle the state of an element (open/close)
    function toggleElement(targetElement) {
        const isHidden = targetElement.classList.contains("close");
        hideAllExcept(targetElement);
        targetElement.classList.toggle("close", !isHidden);
        targetElement.classList.toggle("open", isHidden);
        setExpanded(targetElement, isHidden);
    }

    toggleButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const targetIds = this.getAttribute("data-target").split(" ");
            targetIds.forEach((targetId) => {
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    toggleElement(targetElement);
                    if (targetElement.classList.contains("open")) {
                        const input = targetElement.querySelector("input");
                        if (input) window.requestAnimationFrame(() => input.focus());
                    }
                }
            });
        });
    });

    // Add event listener to the document to close elements when a click occurs outside of open elements
    document.addEventListener("click", function (event) {
        const targetElements = Array.from(document.querySelectorAll(".open"));
        const clickedOutsideAllTargets = targetElements.every((element) => {
            return !element.contains(event.target) && !event.target.closest(".toggle-button");
        });

        if (clickedOutsideAllTargets) {
            targetElements.forEach(closeElement);
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            document.querySelectorAll(".open").forEach(closeElement);
        }
    });

})();
