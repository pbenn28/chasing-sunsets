document.addEventListener('keydown', function(event) {
    // Check if user is not typing in an input field
    if (event.target.tagName.toLowerCase() === 'input' || 
        event.target.tagName.toLowerCase() === 'textarea' || 
        event.target.isContentEditable) {
        return; // Don't trigger navigation if user is typing
    }

    switch(event.key) {
        case 'ArrowLeft':
            event.preventDefault(); // Prevent default browser behavior
            triggerSidebar('left');
            break;
        case 'ArrowRight':
            event.preventDefault(); // Prevent default browser behavior
            triggerSidebar('right');
            break;
    }
});

function triggerSidebar(side) {
    const sidebarId = side === 'left' ? '#sidebar1' : '#sidebar2';
    const sidebar = document.querySelector(sidebarId);
    
    if (sidebar) {
        // Find the link inside the sidebar
        const link = sidebar.querySelector('a');
        
        if (link && link.href) {
            // Add visual feedback
            sidebar.style.backgroundColor = '#ddd';
            setTimeout(() => {
                sidebar.style.backgroundColor = ''; // Reset after brief highlight
            }, 150);
            
            // Navigate to the link
            window.location.href = link.href;
        }
    }
};