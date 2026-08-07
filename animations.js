document.addEventListener("DOMContentLoaded", (event) => {
    gsap.registerPlugin(ScrollTrigger);

    // Fade Up Animation
    const fadeUps = document.querySelectorAll('.gsap-fade-up');
    fadeUps.forEach((elem) => {
        gsap.from(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
                toggleActions: "play none none none"
            },
            y: 50,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out"
        });
    });

    // Fade Right Animation (comes from left)
    const fadeRights = document.querySelectorAll('.gsap-fade-right');
    fadeRights.forEach((elem) => {
        gsap.from(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
                toggleActions: "play none none none"
            },
            x: -50,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out"
        });
    });

    // Fade Left Animation (comes from right)
    const fadeLefts = document.querySelectorAll('.gsap-fade-left');
    fadeLefts.forEach((elem) => {
        gsap.from(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
                toggleActions: "play none none none"
            },
            x: 50,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out"
        });
    });

    // Zoom In Animation
    const zoomIns = document.querySelectorAll('.gsap-zoom-in');
    zoomIns.forEach((elem) => {
        gsap.from(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
                toggleActions: "play none none none"
            },
            scale: 0.8,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out"
        });
    });

    // GSAP Number Counter
    const counters = document.querySelectorAll('.counter');
    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        
        ScrollTrigger.create({
            trigger: counter,
            start: "top 90%",
            once: true,
            onEnter: () => {
                gsap.to(counter, {
                    innerHTML: target,
                    duration: 2,
                    snap: { innerHTML: 1 },
                    ease: "power2.out"
                });
            }
        });
    });
});
