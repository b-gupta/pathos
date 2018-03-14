var express = require('express');
var bodyParser = require('body-parser');
var sha256 = require('sha256');

var app = express();
app.use( bodyParser.json() );
app.use(bodyParser.urlencoded({ extended: true }))
var map = {};

app.post('/messages', function(req, res) {
    console.log(req.body.message);
    var hash = sha256(req.body.message);
    map[hash] = req.body.message;
    res.send([{
        "digest": hash
    }]);
});

app.get('/messages/:hash', function(req, res) {
    console.log(req.params.hash);
    if (!map.hasOwnProperty(req.params.hash)) {
        res.status(404).send([{ "err_msg" : "Not found!"}]);
    }
    else {
        res.send([{
            "message": map[req.params.hash]
        }]);
    }
});

app.listen(3001);
console.log('Listening on port 3001...');

