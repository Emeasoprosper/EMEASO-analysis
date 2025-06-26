// Initialize AOS
AOS.init({
    duration: 800,
    easing: 'ease-in-out',
    once: true
});

// Card interactions
const cards = document.querySelectorAll('.right-section [class^="child"]');
cards.forEach((card, index) => {
    // Click effect
    card.addEventListener('click', () => {
        // Add clicked class
        card.classList.add('clicked');
        
        // Create ripple effect
        const ripple = document.createElement('div');
        ripple.style.position = 'absolute';
        ripple.style.borderRadius = '50%';
        ripple.style.background = 'rgba(255, 255, 255, 0.3)';
        ripple.style.transform = 'scale(0)';
        ripple.style.animation = 'ripple 0.6s linear';
        ripple.style.left = '50%';
        ripple.style.top = '50%';
        ripple.style.width = '20px';
        ripple.style.height = '20px';
        ripple.style.marginLeft = '-10px';
        ripple.style.marginTop = '-10px';
        
        card.appendChild(ripple);
        
        // Remove effects after animation
        setTimeout(() => {
            card.classList.remove('clicked');
            ripple.remove();
        }, 600);
        
        // Add subtle shake to other cards
        cards.forEach((otherCard, otherIndex) => {
            if (otherIndex !== index) {
                otherCard.style.transform = 'translateX(2px)';
                setTimeout(() => {
                    otherCard.style.transform = '';
                }, 150);
            }
        });
    });
    
    // Hover effects
    card.addEventListener('mouseenter', () => {
        card.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
    });
    
    card.addEventListener('mouseleave', () => {
        card.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
    });
});

// Add ripple animation style
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Create floating particles effect
function createFloatingParticles() {
    for (let i = 0; i < 15; i++) {
        const particle = document.createElement('div');
        particle.style.position = 'fixed';
        particle.style.width = '4px';
        particle.style.height = '4px';
        particle.style.background = `rgba(${Math.random() * 255}, ${Math.random() * 255}, 255, 0.3)`;
        particle.style.borderRadius = '50%';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.pointerEvents = 'none';
        particle.style.animation = `float ${3 + Math.random() * 4}s ease-in-out infinite`;
        particle.style.animationDelay = Math.random() * 2 + 's';
        document.body.appendChild(particle);
    }
}

// Add float animation
const floatStyle = document.createElement('style');
floatStyle.textContent = `
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.3; }
        50% { transform: translateY(-20px) rotate(180deg); opacity: 0.8; }
    }
`;
document.head.appendChild(floatStyle);

// Initialize particles
createFloatingParticles();

// Navigation hover effects
const navItems = document.querySelectorAll('.nav li');
navItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
        item.style.transform = 'translateY(-3px) scale(1.05)';
    });
    
    item.addEventListener('mouseleave', () => {
        item.style.transform = 'translateY(0) scale(1)';
    });
});