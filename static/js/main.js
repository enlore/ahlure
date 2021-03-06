$(document).ready(function () {
    var $form = $('#contact-form')

    function bumpFirsty(str) {
        return str.charAt(0).toUpperCase() + str.slice(1)
    }

    function validateRequiredField(fieldName) {
        var messages = {
            name: "A name is required for submission.",
            phone: "A 10-digit phone number is required for submission.",
            email: "An email address is required for submission.",
            about: "Please give a brief description about the event you need service for!"
        }

        var $field = $form.find('[name="' + fieldName + '"]')

        if ($field.val() === '') {
            console.log(Date.now() + ' ' + messages[fieldName])

            $form.find('label[for="' + fieldName + '"]')
                .text(messages[fieldName])
                .parent().addClass('has-error')

            return true

        } else {
            $form.find('label[for="' + fieldName + '"]')
                .text(bumpFirsty(fieldName))
                .parent().removeClass('has-error')

            return false
        }
    }

    $form.on('submit', function (e) {
        console.log('\n---------------')
        e.preventDefault()

        var fields = ['about', 'name', 'phone', 'email']
          , errors = {name: false, phone: false, about: false, email: false}

        for (var i = 0; i <  fields.length; i++) {
            errors[fields[i]] = validateRequiredField(fields[i])
        }


        // form submission should happen if all errors are false
        var hasError = false

        for (var j = 0; j < fields.length; j++) {
            // if we find a true, set errors to true
            if (errors[fields[j]]) {
                hasError = true
            }
        }

        if (!hasError) {
            e.target.submit()
        }
    })
})
