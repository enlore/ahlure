
/**
 * Module dependencies.
 */

var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');
var flash = require('connect-flash')

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(express.compress())
app.use(express.favicon(path.join(__dirname, '/static/favicon.ico')));
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(express.bodyParser())
app.use(express.cookieParser('a;sldkfja;oiwefj;a'));
app.use(express.session({ cookie: { maxAge: 60000 }}));
app.use(flash())
app.use(app.router);
app.use(require('less-middleware')({ src: path.join(__dirname, 'static') }));
app.use(express.static(path.join(__dirname, 'static')));

var mail_opts = {}
mail_opts.sender = 'CONTACT@ahlure.net'
mail_opts.subj = 'AHLURE LEAD'
mail_opts.body = ''

if ('production' == app.get('env')) {
    mail_opts.recp = ['aelliott2120@gmail.com', 'oneofy@gmail.com']
}

// development only
if ('development' == app.get('env')) {
    app.use(express.errorHandler());
    mail_opts.recp = ['oneofy@gmail.com']
}

app.get('/', routes.index);
app.post('/', routes.submit)

exports.start = function () {
    app.listen(app.get('port'), function(){
        console.log('Express server listening on port ' + app.get('port'));
    });
}
