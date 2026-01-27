const phrases = ["Future of Business", "Next Digital Era", "Modern Experience"];
let phraseIndex = 0;
const textElement = document.getElementById('text-cycler');

// Initialize styles
textElement.style.transition = 'all 0.5s ease-in-out';
textElement.style.opacity = '1';
textElement.style.transform = 'translateX(-50%)'; // Centered state

setInterval(() => {
    // 1. Exit to Left
    textElement.style.opacity = '0';
    textElement.style.filter = 'blur(10px)';
    // Move left from center (-50% - 50px)
    textElement.style.transform = 'translateX(calc(-50% - 50px))';

    setTimeout(() => {
        // 2. Reset to Right (No Animation)
        textElement.style.transition = 'none'; // Disable transition
        phraseIndex = (phraseIndex + 1) % phrases.length;
        textElement.textContent = phrases[phraseIndex];
        // Move to right side of center (-50% + 50px)
        textElement.style.transform = 'translateX(calc(-50% + 50px))';
        
        // Force reflow to apply the instant jump
        void textElement.offsetWidth;

        // 3. Enter to Center
        setTimeout(() => {
            textElement.style.transition = 'all 0.5s ease-in-out'; // Re-enable transition
            textElement.style.opacity = '1';
            textElement.style.filter = 'blur(0)';
            // Return to absolute center
            textElement.style.transform = 'translateX(-50%)'; 
        }, 50);
        
    }, 500);
}, 3000);