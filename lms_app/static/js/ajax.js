
   // var session_data = document.getElementById('questions').value;
   //  console.log(session_data)

    $('input[type=radio]').click(function (){

        $("input[type=radio]").removeClass('btn-light');
        $("input[type=radio]").addClass('btn-success');

        var checked_value = $("input[type=radio]:checked").val();
        var question_id = $("input[type=radio]:checked").attr('name');

        console.log(checked_value)
        console.log(question_id)

        $("#next_qns").click(
            function store_values(question_id){
                set_cookies(question_id, checked_value);
            }

        //     function () {
        //     sessionStorage.setItem(question_id, checked_value);
        // }


        )

        $("#prev_qns").click(
            function store_values(question_id){
                set_cookies(question_id, checked_value);
            }

        //     function () {
        //     sessionStorage.setItem(`${question_id}`, checked_value);
        // }

        )



        function set_cookies(name, value) {
            document.cookie = name + "=" + value ;
        }


        if ("choice1" == get_cookies(question_id)){
            document.getElementById("choice1").checked = true
            console.log(get_cookies(question_id))
        }
        else if ("choice2" == get_cookies(question_id)){
            document.getElementById("choice2").checked = true
            console.log(get_cookies(question_id))
        }
        else if ("choice3" == get_cookies(question_id)){
            document.getElementById("choice3").checked = true
            console.log(get_cookies(question_id))
        }
        else if ("choice4" == get_cookies(question_id)){
            document.getElementById("choice4").checked = true
            console.log(get_cookies(question_id))
        }
        else{
            //Do nothing
        }

        function get_cookies(name){
            var re = new RegExp(name + "=([^;]+)");
            var value = re.exec(document.cookie);
            return (value != null) ? unescape(value[1]) : null;
        }



    });

//     function get_cookies(name){
//         for (var i=0; i<session_data.length; i++){
//             var key = session_data[i]
//             document.cookie
//         }
//     }
//
//
//