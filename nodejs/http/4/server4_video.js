var http = require('http');
var fs = require('fs');
var url = require('url');

http.createServer(function (request, response) {
    //获取当前访问网址
    var pathname = url.parse(request.url).pathname;
    console.log("url: " + pathname);
    if (pathname == "/") {
        pathname = "/index.html";
    }
    
    //构建完整本地路径
    var pathname_full = __dirname + decodeURI(pathname);
    console.log("request: " + pathname_full);

    //获取文件的扩展名
    var ext = pathname.match(/(\.[^.]+|)$/)[0];
    console.log("ext: " + ext);

    //根据不同的文件扩展名做出不同的处理
    if(ext == ".mp4" || ext == ".webm") {
        fs.exists(pathname_full, function (exists) {
            if (exists) {
                response.writeHead(200, {
                    'Content-Type': 'video/mp4'
                });
                var stream = fs.createReadStream(pathname_full).on("open", function () {
                    stream.pipe(response); 
                }).on("error", function (err) {
                    response.end(err);
                }); 
    
            } else {
                console.log(pathname_full + " 文件不存在!");
                response.writeHead(404, {
                    "Content-Type": "text/plain"
                });
                response.end(pathname + " 文件不存在!");
            }
        });
    }
    else {
        fs.readFile('.' + pathname, 'utf-8', function (err, data) {
            response.writeHead(200, {
                "Content-Type": "text/html"
            });
            response.write(data);
            response.end();
        });
    }
    
}).listen(3000);

console.log('Server running at http://127.0.0.1:3000/');