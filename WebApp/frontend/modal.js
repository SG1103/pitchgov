document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('question-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(form);

        fetch('/submit-answer', {
            method: 'POST',
            body: formData
        }).then(response => response.json())
        .then(data => {
            if (data.end) {
                window.location.href = data.redirect;  // Redirect if the quiz is finished
            } else {
                document.querySelector('#question-form [name="question_id"]').value = data.new_question_id;
                document.querySelector('.modal-title').textContent = "Question Number: " + data.question_number;
                document.querySelector('#question-form label').textContent = "The question is: " + data.new_question;
                document.querySelector('#question-form textarea').value = '';  // Clear the textarea after submission
                if (data.image_path) {
                    document.querySelector('#image-container').innerHTML = '<img src="' + data.image_path + '" alt="Question Image" class="img-fluid">';
                } else {
                    document.querySelector('#image-container').innerHTML = '';
                }
            }
        }).catch(error => console.error('Error:', error));
    });
});
