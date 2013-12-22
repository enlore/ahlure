
/*
 * GET home page.
 */

var mailgun = require('mailgun')

var mg = new mailgun.Mailgun('key-1le00ub2z3uc8onmlmnk2sdph6-484v5')

var mail_opts = {}
mail_opts.sender = 'CONTACT@ahlure.net'
mail_opts.subj = 'AHLURE LEAD'
mail_opts.body = ''
//mail_opts.recp = ['aelliott2120@gmail.com', 'oneofy@gmail.com']
mail_opts.recp = ['oneofy@gmail.com']

exports.index = function(req, res){
  res.render('index', { flashes: req.flash('success') });
};

exports.submit = function (req, res) {
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

    res.redirect('/#contact-me')
}
