// Validate Assessment Title
$(document).ready(function (){
    $("#assessment_title_validate").hide();
    let assessmentTitle=true
    $("#assessment_title").keyup( function () {
        validateAssessmentTitle();
    });

    function validateAssessmentTitle(){
        let assessment_title = $('#assessment_title').val()
        if (assessment_title == " "){
            $("#assessment_title_validate").show()
            assessmentTitle=false;
            return false;
        }
        else{
            $("#assessment_title_validate").hide();
        }
    }


    $("#assessment_content_validate").hide();
    let assessmentContentError=true;
    $("#assessment_content").keyup(function () {
        validateAssessmentContent();
    })

    function validateAssessmentContent(){
        let assessmentContent=$("#assessment_content").val();
        if (assessmentContent == " "){
            $("#assessment_content_validate").show();
            assessmentContentError=false
            return false
        }
        else{
            $("#assessment_title_validate").hide();
        }

    }


    $("#course_id_validate").hide();
    let courseId=true
    $("#course_id").keyup( function () {
        validateCourseId();
    });

    function validateCourseId(){
        let course_id = $('#course_id').val()
        if (course_id == " "){
            $("#course_id_validate").show()
            courseId=false;
            return false;
        }
        else{
            $("#course_id_validate").hide();
        }
    }



    $("#pass_mark_validate").hide();
    let passMarkError=true
    $("#pass_mark").keyup( function () {
        passMarkFunc();
    });

    function passMarkFunc(){
        let pass_mark = $('#pass_mark').val()
        if (pass_mark == " "){
            $("#pass_mark_validate").show()
            passMarkError=false;
            return false;
        }
        else{
            $("#pass_mark_validate").hide();
        }
    }


    $("#assessment_due_date_validate").hide();
    let assessmentDateError=true
    $("#assessment_due_date").keyup( function () {
        validateAssessmentDate();
    });

    function validateAssessmentDate(){
        let value = $('#assessment_due_date').val();
        if (value == " "){
            $("#assessment_due_date_validate").show();
            assessmentDateError=false;
            return false;
        }
        else{
            $("#assessment_due_date_validate").hide();
        }
    }

    $("#assessment_due_time_validate").hide();
    let assessmentTimeError=true
    $("#assessment_due_time").keyup( function () {
        validateAssessmentTime();
    });

    function validateAssessmentTime(){
        let value = $('#assessment_due_time').val()
        if (value == " "){
            $("#assessment_due_time_validate").show()
            assessmentTimeError=false;
            return false;
        }
        else{
            $("#assessment_due_date_validate").hide();
        }
    }


    $("#course_title_validate").hide();
    let courseTitleError=true
    $("#course_title").keyup( function () {
        validateCourseTitle();
    });

    function validateCourseTitle(){
        let value = $('#course_title').val()
        if (value == " "){
            $("#course_title_validate").show()
            courseTitleError=false;
            return false;
        }
        else{
            $("#course_title_validate").hide();
        }
    }


    $("#course_description_validate").hide();
    let courseDescriptionError=true
    $("#course_description").keyup( function () {
        validateCourseDescription();
    });

    function validateCourseDescription(){
        let value = $('#course_description').val()
        if (value == " "){
            $("#course_description_validate").show()
            courseDescriptionError=false;
            return false;
        }
        else{
            $("#course_description_validate").hide();
        }
    }


});

