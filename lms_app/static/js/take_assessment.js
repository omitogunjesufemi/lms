// $(document).ready( function(){
//
//     let j=1
//
//
//     $("a[id='prv']").on('click', function (){
//         j--
//         console.log(j)
//     })
//
//     $("a[id='nxt']").on('click', function (){
//         j++
//         console.log(j)
//     })
//
//     console.log(j)
//
//     let str = j.toString();
//
//     let radios = document.getElementsByName(j);
//     let val = sessionStorage.getItem(str);
//     console.log(val);
//     for (let i=0; i<radios.length; i++) {
//         if (radios[i].value == val){
//             console.log(radios.length)
//             console.log(radios[i].value);
//             radios[i].checked = true;
//         }
//     }
//
//
//    $("input[type=radio]").on('change', function (){
//         sessionStorage.setItem(str, $(this).val());
//    });
// });