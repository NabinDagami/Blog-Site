document.addEventListener('DOMContentLoaded', function () {
  var contactForm = document.getElementById('contactForm');

  contactForm.addEventListener('submit', function (event) {
      if (!validateForm()) {
          event.preventDefault();
      }
  });

  // Add input event listeners for real-time validation
  var titleInput = document.getElementById('name');
  var authorSelect = document.getElementById('author');
  var contentInput = document.getElementById('content');

  titleInput.addEventListener('input', validateTitle);
  authorSelect.addEventListener('input', validateAuthor);
  contentInput.addEventListener('input', validateContent);

  function validateForm() {
      var isValid = true;

      // Run individual validation functions
      isValid = isValid && validateTitle();
      isValid = isValid && validateAuthor();
      isValid = isValid && validateContent();

      return isValid;
  }

  function validateTitle() {
      var title = titleInput.value;
      var titleError = document.querySelector('#name + p');
      titleError.textContent = '';

      if (title.trim() === '') {
          titleError.textContent = 'Please enter a title.';
          return false;
      }

      return true;
  }

  function validateAuthor() {
      var author = authorSelect.value;
      var authorError = document.querySelector('#author + p');
      authorError.textContent = '';

      if (author === 'Select Author') {
          authorError.textContent = 'Please select an author.';
          return false;
      }

      return true;
  }

  function validateContent() {
      var content = contentInput.value;
      var contentError = document.querySelector('#content + p');
      contentError.textContent = '';

      if (content.trim() === '') {
          contentError.textContent = 'Please enter content.';
          return false;
      }

      return true;
  }
});