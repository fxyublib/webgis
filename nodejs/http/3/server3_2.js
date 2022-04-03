var http = require('http');
var fs = require('fs');
var url = require('url');
const path = require('path');

// 创建服务器
http.createServer(function (req, res) {
    // 解析请求，包括文件名
    var pathname = url.parse(req.url).pathname;
   //获取node.exe的绝对路径
   console.log(process.execPath);//D:\nodejs\node.exe

    //当前文件（即server.js）的绝对路径
    console.log(__filename);//D:\nodeTest\node_path\lib\server.js

   //存放当前文件（即server.js）文件夹的绝对路径
   console.log(__dirname);//D:\nodeTest\node_path\lib

   //从所传入的文件路径（相对或绝对）中获取存放传入文件的文件夹的相对或绝对路径 
   //（例如 传入 public/home.html 则返回的是public）
   console.log(path.dirname(__filename));//D:\nodeTest\node_path\lib

   //执行当前脚本（即server.js）的位置 （例如 在根目录下执行 node ./xxx/xxx/a.js 则返回的是根目录地址 ）
   console.log(process.cwd());//D:\nodeTest\node_path\lib

   //'a/b/c'和'../src' 组合而成的绝对路径 文件或文件夹都行
    //例如 console.log(path.resolve('a/b/c', '../src'));//D:\nodeTest\node_path\lib\a\b\src
    console.log(path.resolve(__dirname, '../public'));//D:\nodeTest\node_path\public

    //'a/b/c'和'../src'组成的相对路径
    //console.log(path.join('a/b/c', '../src'));//a\b\src
    console.log(path.join(__dirname, '../public'));//D:\nodeTest\node_path\public

    // 输出请求的文件名
    console.log("Request for " + pathname + " received.");
    if (pathname == "/") {
        fs.stat('/index.html', function (err, stat) {
            if (stat && stat.isFile()) {
                console.log('index.html existed.');
            } else {
                console.log('index.html not existed.');
            }
        });

        fs.readFile("index.html", function (err, data) {
            if (err) {
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/plain');
                res.end('Hello World');
            } else {
                res.writeHead(200, {
                    "Content-Type": "text/html;charset=UTF-8"
                });
                res.end(data);
            }
        });
    } else if (pathname.indexOf(".jpg") != -1 || pathname.indexOf(".png") != -1) {
        
        fs.readFile(__dirname + pathname, 'binary', function (err, data) {
            if (err) {
                console.log(err);
            } else {
                res.writeHead(200, {'Content-type':'image/jpeg'});
                res.write(data, 'binary');
                res.end();
            }
        });
    } else {
        // 从文件系统中读取请求的文件内容
        fs.readFile(__dirname + pathname, function (err, data) {
            if (err) {
                console.log(err);
                // HTTP 状态码: 404 : NOT FOUND
                // Content Type: text/html
                res.writeHead(404, {
                    'Content-Type': 'text/html'
                });
            } else {
                // HTTP 状态码: 200 : OK
                // Content Type: text/html
                res.writeHead(200, {
                    'Content-Type': 'text/html;charset=utf-8'
                });

                // 响应文件内容
                res.write(data.toString());
            }
            //  发送响应数据
            res.end();
        });
    }

}).listen(3000);

// 控制台会输出以下信息
console.log('Server running at http://127.0.0.1:3000/');