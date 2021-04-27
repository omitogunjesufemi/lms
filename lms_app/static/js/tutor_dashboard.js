let submission = document.getElementById('submission_length');
let assessment = document.getElementById('assessment_count');
let courses = document.getElementById('courses_count');
let students = document.getElementById('student_count');

function submission_length(){
    fetch(`http://${host}/sitting/submitted_to_tutor`,{
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then (response =>response.json())
        .then (function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )
            submission.innerHTML = html_output.join('');
        })
        .catch(err => console.log('Request Failed', err));
}

function assessment_count(){
    fetch(`http://${host}/assessment/api/tutor`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )
            assessment.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function courses_count(){
    fetch(`http://${host}/appointment/api/tutor`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )
            courses.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function enrollments(course_id){
    fetch(`http://${host}/enrollment/api/students/${course_id}`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(
            function (json){
            console.log(course_id)
            console.log(json.length)
            return json.length
        })
        .catch(err => console.log('Request Failed', err))
}

function student_count(){
    fetch(`http://${host}/appointment/api/tutor`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            var output = []

            json.forEach(
                function (current_appointment){
                    console.log(current_appointment.course_id)
                    let a = current_appointment.course_id
                    let int_a = parseInt(a)
                    output.push(enrollments(int_a))
                }
            )

            console.log(output)

            students.innerHTML = output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

submission_length();
assessment_count();
courses_count();
student_count();