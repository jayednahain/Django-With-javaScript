console.log('helllow world')


//creating variable ! connect varible with html ids!

const spinnerBox = document.getElementById("spinner-box");
const dataBox = document.getElementById('data-box');

// see they are working or not !
console.log(spinnerBox)
console.log(dataBox.classList)



//using ajex
$.ajax({
    type:'GET',
    url:'/json_response/',
    success:function (response) {
        setTimeout(()=>{
            spinnerBox.classList.add('not-visible')
            console.log(response)

            for (const item of response)
            {
                dataBox.innerHTML += `<h1>${item.title}</h1><br><p>${item.body}</p><hr>`
            }

        },1000)

    },
    error: function (error) {
        setTimeout(()=>{


            spinnerBox.classList.add('not-visible')
            dataBox.innerHTML += `<h3>failed to load the data</h3>`
            console.log(error)


        })

    }

})