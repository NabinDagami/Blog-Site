document.addEventListener('DOMContentLoaded', function() {
    var messages = document.querySelectorAll('.message');
    messages.forEach(function(message) {
        // Show the message
        message.style.opacity = 1;

        // Hide the message after 5 seconds (adjust the delay if needed)
        setTimeout(function() {
            message.style.opacity = 0;

            // Optionally, remove the message from the DOM after hiding
            setTimeout(function() {
                message.remove();
            }, 500);  // Adjust the delay for removing if needed
        }, 5000);
    });
});