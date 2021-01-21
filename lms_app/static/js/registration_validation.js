$(document).ready(function () {

    $('#first_name_check').hide();
    let firstnameError = true;
    $('#first_name').keyup(function () {
        validateFirstName();
    });

    function validateFirstName() {
        let first_nameValue = $('#first_name').val();
        if (first_nameValue.length == '') {
            $('#first_name_check').show();
            firstnameError = false;
            return false;
        }
        else {
            $('#first_name_check').hide();
        }
    }

    $('#last_name_check').hide();
    let lastnameError = true;
    $('#last_name').keyup(function () {
        validateLastName();
    });

    function validateLastName() {
        let lastnameValue = $('#last_name').val();
        if (lastnameValue.length == '') {
            $('#last_name_check').show();
            lastnameError = false;
            return false;
        }
        else {
            $('#last_name_check').hide();
        }
    }


    $('#phone_check').hide();
    let telephoneError = true;
    let hasElevenDigits = true;
    $('#phone').keyup(function () {
        validatePhone();
    });

    function validatePhone() {
        let phoneValue = $('#phone').val();

        if((phoneValue[0] == 0)) {
            let parsedNumber = parseInt(phoneValue, 10);
            $('#phone').val(parsedNumber)
        }

        if (phoneValue.length == '') {
            $('#phone_check').show();
            telephoneError = false;
            return false;
        }
        else if((phoneValue.length < 10) || (phoneValue.length > 10)) {
            $('#phone_check').show();
            $('#phone_check').html
            ("**length of phone number must be 10");
            hasElevenDigits = false;
            return false;
        }

        else {
            $('#phone_check').hide();
        }
    }


// Validate Username 
    $('#user_check').hide();
    let usernameError = true;
    $('#username').keyup(function () {
        validateUsername();
    });

    function validateUsername() {
        let usernameValue = $('#username').val();
        let user_list_value = $('#user_list').text();
        console.log(user_list_value)
        console.log(usernameValue)

        if (usernameValue.length == '') {
            $('#user_check').show();
            usernameError = false;
            return false;
        }
        else if((usernameValue.length <= 3)) {
            $('#user_check').show();
            $('#user_check').html
            ("**length of username must be greater than 3");
            usernameError = false;
            return false;
        }
        else if((user_list_value.includes(usernameValue))) {
            $('#user_check').show();
            $('#user_check').html
            ("**Username already taken");
            usernameError = false;
            return false;
        }

        else {
            $('#user_check').hide();
        }
    }

// Validate Email 
    const email =
        document.getElementById('email');
    email.addEventListener('blur', ()=>{
        let regex =
            /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
        let s = email.value;
        if(regex.test(s)){
            email.classList.remove(
                'is-invalid');
            emailError = true;
        }
        else{
            email.classList.add(
                'is-invalid');
            emailError = false;
        }
    })

// Validate Password 
    $('#pass_check').hide();
    let passwordError = true;
    $('#password').keyup(function () {
        validatePassword();
    });
    function validatePassword() {
        let passwordValue =
            $('#password').val();
        if (passwordValue.length == '') {
            $('#passcheck').show();
            passwordError = false;
            return false;
        }
        if ((passwordValue.length < 3)) {
            $('#pass_check').show();
            $('#pass_check').html
            ("**length of your password must be greater than 3");
            $('#pass_check').css("color", "red");
            passwordError = false;
            return false;
        } else {
            $('#pass_check').hide();
        }
    }

// Validate Confirm Password 
    $('#confirm_pass_check').hide();
    let confirmPasswordError = true;
    $('#confirm_password').keyup(function () {
        validateConfirmPassword();
    });
    function validateConfirmPassword() {
        let confirmPasswordValue =
            $('#confirm_password').val();
        let passwordValue =
            $('#password').val();
        if (passwordValue !== confirmPasswordValue) {
            $('#confirm_pass_check').show();
            $('#confirm_pass_check').html(
                "**Password didn't Match");
            $('#confirm_pass_check').css(
                "color", "red");
            confirmPasswordError = false;
            return false;
        } else {
            $('#confirm_pass_check').hide();
        }
    }

// Submitt button
//     $('#submitbtn').click(function () {
//         let allow;
//         validateFirstName();
//         validateLastName();
//         validateUsername();
//         validatePassword();
//         validateConfirmPassword();
//
//         if ((usernameError === true) && (passwordError === true) && (confirmPasswordError === true) && (emailError === true)){
//             allow = 1;
//         }
//         else {
//              allow = 0;
//         }
//     });
});
