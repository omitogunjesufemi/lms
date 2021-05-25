    var submit = document.getElementById('submit_quiz')
    var session_data = document.getElementById('qns').value;
    var session_datas = document.getElementById('questions').value;
    var time_line = document.querySelector('.time_line')
    var timeText = document.querySelector(".timer .time_left")
    var timeCount = document.getElementById('timer_min')

    function startTimer(time){
        var counter = setInterval(timer, 1000);
        function timer(){
            timeCount.innerHTML = time;
            time--;
            if (time < 10){
                let addZero = timeCount.innerHTML;
                timeCount.textContent = "0" + addZero;
            }

            if (time === 0){
                clearInterval(counter);
                timeText.innerHTML = 'Time Off'
            }
        }
    }

    function startTimerLine(time){
        var counterLine = setInterval(timer, 300)
    }

    function setCookie(c_name, c_value){
        document.cookie = `${c_name}=${c_value}`;
    }

    function getCookies(c_name){
        let name = `${c_name}=`;
        let decoded_cookie = decodeURIComponent(document.cookie);
        let de_cookie = decoded_cookie.split(';');
        for (let i = 0; i < de_cookie.length; i++){
            let d_cookie = de_cookie[i];
            while (d_cookie.charAt(0) == ' '){
                d_cookie = d_cookie.substring(1)
            }

            if (d_cookie.indexOf(name) == 0){
                return d_cookie.substring(name.length, d_cookie.length)
            }
        }
        return "";

    }

    function checkCookies(name){
        let search_name = getCookies(name);
        if (search_name != ""){
            var radiobtn = document.getElementById(search_name);
            radiobtn.checked = true;
        }
    }

    checkCookies(session_data);

    function submit_quiz(){
        let user_pick_list = []
        let i;
        for (i=0; i<session_datas.length-1; i++){
            let cookie_key = session_datas[i];
            let user_pick = getCookies(cookie_key);
            if (user_pick !== ""){
                let string = user_pick.toString()
                user_pick_list.push(string);
            }

        }
        console.log(user_pick_list);
        let answer = document.getElementById('answer').value = user_pick_list;

    }


    submit_quiz();
    startTimer(300);
    startTimerLine(300);
    submit.addEventListener('click', submit_quiz)



