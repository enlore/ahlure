$(document).ready(function () {
    var $form = $('#contact-form')

    function validateRequiredField(fieldName) {
        var messages = {
            name: "Please tell me who you are.",
            phone: "Please give me your number and area code.",
            email: "Please include your email",
            about: "Can you tell me a little about your event?" 
        }

        var $email = $form.find('[name="' + fieldName + '"]')

        if ($email.val() === '') {
            console.log(messages[fieldName])

            $form.find('label[for="' + fieldName + '"]')
                .text(messages[fieldName])
                .parent().addClass('has-error') 
        }
    }

    $form.on('submit', function (e) {
        console.log('form hit')
        e.preventDefault() 

        var fields = ['about', 'name', 'phone', 'email']

        for (var i = 0; i <  fields.length; i++) {
            console.log('validating field: ', fields[i])
            validateRequiredField(fields[i]) 
        }

    })
})
