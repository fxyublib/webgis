var http = require('http');
var fs = require('fs');
var url = require('url'); 
var router = require('./router.js');

http.createServer(function (request, response) {
    var pathname = url.parse(request.url).pathname;
    console.log("url: " + request.url);
    if (pathname == "/") {
        pathname = "/index.html";
    }
    
    var ipv4 = get_client_ipv4(request);
    showLog(ipv4, ("请求: " + decodeURI(pathname)));
    fs.exists(__dirname + decodeURI(pathname), function (exists) {
        if (exists) {
            router.readFileByExt(pathname, fs, request, response);
        } else {
            console.log(decodeURI(pathname) + " 文件不存在!");
            response.writeHead(404, {
                "Content-Type": "text/plain"
            });
            response.end(pathname + " 文件不存在!");
        }
    });

}).listen(3000);

console.log('Server running at http://127.0.0.1:3000/');

/**
 * @desc 获取IPV4地址
 * @param req htttp.request
 * @return string 32位IP地址
 */
function get_client_ipv4(req) {
    var ip = req.headers['x-forwarded-for'] ||
        req.ip ||
        req.connection.remoteAddress ||
        req.socket.remoteAddress ||
        req.connection.socket.remoteAddress || '';
    if (ip.split(',').length > 0) {
        ip = (ip.split(',')[0]).match(/(\d+\.\d+\.\d+\.\d+)/)[0];
    }
    return ip;
};

/**
 * @desc 向控制台输出日志，自动在头部添加时间、地址
 * @param ipv4 string
 * @param message string
 */
function showLog(ipv4, message) {
    var date = new Date();
    console.log(date.toLocaleDateString() + " " + date.toLocaleTimeString() +
        " " + ipv4 + " " + message);
}