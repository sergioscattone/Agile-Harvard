        function goBack() {
            window.history.back();
        }

        function register(exercise_id, workout_index, user_id) {
            console.log("Register function called");
            console.log("Exercise ID:", exercise_id);
            console.log("Workout Index:", workout_index);
            console.log("User ID:", user_id);

            $.ajax({
                url: '/register_exercise',
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    exercise_id: exercise_id,
                    workout_index: workout_index,
                    user_id: user_id
                }),
                success: function(response) {
                    console.log("Response:", response);
                    alert(response.message);
                },
                error: function(error) {
                    console.log("Error:", error);
                    alert('Error: ' + error.responseJSON.message);
                }
            });
        }

        $(document).ready(function() {
            $('.toggleButton').click(function() {
                $(this).next('.dropdown-content').toggle();
            });
        });