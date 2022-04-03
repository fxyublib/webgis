
const logToFile = function (fs, content) {
    fs.writeFile(__dirname + '/log.txt', content, err => {
      if (err) {
        console.error(err)
        return
      }
    })
}

const readFileByExt = function (pathname, fs, request, response) {
    var ext = pathname.match(/(\.[^.]+|)$/)[0];
    console.log("ext: " + ext);

    switch (ext) {
        case ".css":
        case ".txt":
        case ".js":
        case ".json":
        case ".xml":
        case ".pdf":
        case ".docx":
            fs.readFile("." + request.url, 'utf-8', function (err, data) {
                if (err) throw err;
                response.writeHead(200, {
                    "Content-Type": {
                        ".css": "text/css",
                        ".txt": "text/plain",
                        ".js": "application/javascript",
                        ".json": "application/json",
                        ".xml": "application/xml",
                        ".pdf": "application/pdf",
                        ".docx": "application/msword",
                    } [ext]
                });
                response.write(data);
                response.end();
            });
            break;
            case ".bmp":
        case ".jpg":
        case ".gif":
        case ".png":
            fs.readFile("." + decodeURI(request.url), 'binary', function (err, data) {
                if (err) throw err;
                response.writeHead(200, {
                    "Content-Type": {
                        ".bmp": "image/bmp",
                        ".jpg": "image/jpeg",
                        ".gif": "image/gif",
                        ".png": "image/png",
                    } [ext]
                });
                response.write(data, 'binary');
                response.end();
            });
            break;
        case ".rar":
        case ".zip":
        case ".7z":
            var stats = fs.statSync("." + decodeURI(request.url));
            response.writeHead(200, {
                "Content-Type": "application/octet-stream", //相应该文件应该下载
                "Content-Disposition": `attachment; filename = ${pathname.replace("/","")}`,
                "Content-Length": stats.size
            });
            fs.createReadStream("." + decodeURI(request.url)).pipe(response);
            break;
        case ".mp4":
            fs.stat('.' + decodeURI(request.url), function (err, stats) {
                if (err) {
                    if (err.code === 'ENOENT') {
                        return 404;//return response.sendStatus(404);
                    }
                    response.end(err);
                }
                
                var range = request.headers.range;
                console.log(request.headers);
                console.log(range);
                if (!range) {
                    return 416;//return response.sendStatus(416);
                }
                //替换、切分，请求范围格式为：Content-Range: bytes 0-2000/4932
                var positions = range.replace(/bytes=/, "").split("-");
                var start = parseInt(positions[0]);
                var total = stats.size;
                var end = positions[1] ? parseInt(positions[1], 10) : total - 1;
                var chunksize = (end - start) + 1;

                response.writeHead(206, {
                    "Content-Range": "bytes " + start + "-" + end + "/" + total,
                    "Accept-Ranges": "bytes",
                    "Content-Length": chunksize,
                    "Content-Type": "video/mp4"
                });
                
                var stream = fs.createReadStream('.' + decodeURI(request.url), {
                        start: start,
                        end: end
                    })
                    .on("open", function () {
                        stream.pipe(response); 
                    }).on("error", function (err) {
                        response.end(err);
                    });
            });
            break;
        default:
            fs.readFile('.' + pathname, 'utf-8', function (err, data) {
                response.writeHead(200, {
                    "Content-Type": "text/html"
                });
                response.write(data);
                response.end();
            });
    }
}

exports.readFileByExt = readFileByExt