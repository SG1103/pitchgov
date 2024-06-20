$(document).ready(function(){
    $('#question-form').on('submit', function(e){
        e.preventDefault(); // Stop the form from submitting normally
        $.ajax({
            url: '/submit-answer', // The endpoint on your Flask app
            type: 'POST',
            data: $(this).serialize(), // Serialize the form data
            success: function(response) {
                // Update your page based on the response
                // Assuming response contains the new question, question ID, and question number
                $('#question-form [name="question_id"]').val(response.new_question_id);
                $('.question-number').text("Question Number: " + response.question_number); // Update the question number
                $('label[for="answer"]').text("The question is: " + response.new_question);
                $('#answer').val(''); // Clear the text area
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });
});
