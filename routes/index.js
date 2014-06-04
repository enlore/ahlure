
/*
 * GET home page.
 */

var mailgun = require('mailgun')

var mg = new mailgun.Mailgun('key-1le00ub2z3uc8onmlmnk2sdph6-484v5')

var mail_opts = {}
mail_opts.sender = 'ahlure.app@ahlure.net'
mail_opts.subj = 'AHLURE LEAD'
mail_opts.body = ''
//mail_opts.recp = ['aelliott2120@gmail.com', 'oneofy@gmail.com']
mail_opts.recp = ['oneofy@gmail.com']

// index
exports.index = function(req, res){
  res.render('index', { flashes: req.flash('success') });
};

// form submission
exports.submit = function (req, res) {
    // if the secret field is filled out, just redirect like nothin happened
    if (req.body.hush) {
        console.log('hush!')
        return res.redirect('/#contact-me')
    }

    var body = [
            req.body.name,
            req.body.email,
            req.body.phone,
            req.body.about
    ].join('\n')

    console.log('------\n %s \n------', body)

    mg.sendText(mail_opts.sender,
                mail_opts.recp,
                mail_opts.subj,
                body,
                function (err) {
        if (err)
            console.log(err)
    })

    req.flash('success', 'Thanks! I\'ll get back to you promptly!')

    return res.redirect('/#contact-me')
}
