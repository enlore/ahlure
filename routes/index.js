
/*
 * GET home page.
 */

var mailgun = require('mailgun')

var mg = new mailgun.Mailgun('key-1le00ub2z3uc8onmlmnk2sdph6-484v5')
var sender = 'CONTACT@ahlure.net'
    , recp = ['aelliott2120@gmail.com', 'oneofy@gmail.com']
    , subj = 'AHLURE LEAD'
    , body = ''


exports.index = function(req, res){
  res.render('index', { title: 'Express' });
};

exports.submit = function (req, res) {
    var body = [req.body.name, req.body.email, req.body.phone, req.body.about]
    console.log(body)
    mg.sendText(sender, recp, subj, body, function (err) {
        if (err)
            console.log(err)
    })
    res.redirect('/')
}
