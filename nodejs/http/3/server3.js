var http = require('http');
var fs = require('fs'); 

var documentRoot = __dirname;
console.log("Workdir: " + __dirname);

var server = http.createServer(function (req, res) {
    var file = documentRoot + req.url;
    console.log("Request: " + file);
    
    fs.readFile(file, function (err, data) {
        if (err) {
            res.writeHeader(404, {
                'content-type': 'text/html;charset="utf-8"'
            });
            res.write('<h1>404错误</h1><p>你要找的页面不存在</p>');
            res.end();
        } else {
            res.writeHeader(200, {
                'content-type': 'text/html;charset="utf-8"'
            });
            res.write(data); 
            res.end();
        }

    });
}).listen(3000);

console.log('Server running at http://127.0.0.1:3000/');