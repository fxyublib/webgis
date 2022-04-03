// var fs = require('fs');
// var archiver = require('archiver');

// var output = fs.createWriteStream('archiver-unzip.zip');
// var archive = archiver('zip');

// output.on('close', function () {
//     console.log(`总共 ${archive.pointer()} 字节`)
//     console.log('fs close.')
// });
// output.on('end', function () {
//     console.log('fs end.')
// });

// archive.on('error', function (err) {
//     throw err;
// });

// archive.on('warning', function (err) {
//     if (err.code === 'ENOENT') {
//         console.warn('archive warning.')
//     } else {
//         throw err
//     }
// })

// archive.pipe(output);

// // archive.bulk([{
// //     src: ['a/**']
// // }]);

// // 从子目录追加文件并将其命名为“新子dir”在存档中
// archive.directory('node_modules/', 'node_modules')

// // 从流中追加文件
// let file1 = __dirname + '/eula.1031.txt'
// archive.append(fs.createReadStream(file1), {
//     name: 'eula.1031.txt'
// })

// // 从字符串追加文件
// archive.append('To see a world in a grain of sand.', {
//     name: 'file2.txt'
// })

// // 从缓冲区追加文件
// let buffer3 = Buffer.from('And a heaven in a wild flower!')
// archive.append(buffer3, {
//     name: 'file3.txt'
// })

// // 追加一个文件
// archive.file('test.pdf', {
//     name: 'test2.pdf'
// })

// archive.finalize();

// var fs = require("fs");
// var unzip = require("unzip");

// fs.createReadStream('archiver-unzip.zip').pipe(unzip.Extract({
//     path: 'unarchive'
// }));

// var fs = require("fs");
// var exec = require('child_process').exec;

// exports.unrar = function(param,next){
//     console.log("param:",param);
//     var cmdStr = "rar x -P"+param.password+" "+param.zipFilePath+" "+param.tgtFilePath+" -y";
//     console.log("cmd:",cmdStr);
//     fs.exists(param.tgtFilePath, function(exists) {  //判断路径是否存在
//         //console.log(">> exists:",exists);
//         if(exists) {
//             exec(cmdStr,function(err,stdout,stderr){  //执行命令行
//                 fs.readdir(param.filesPathInPro,next);
//             });
//         } else {
//             fs.mkdir(param.tgtFilePath,function(){  //创建目录
//                 exec(cmdStr,function(err,stdout,stderr){  //执行命令行
//                     fs.readdir(param.filesPathInPro,next);
//                 });
//             });
//         }
//     });
// }

var fs = require('fs');
var unzipper = require('unzipper');

fs.createReadStream('../assets/test.zip')
    .pipe(unzipper.Parse())
    .on('entry', function (entry) {
        const fileName = entry.path;
        const type = entry.type; // 'Directory' or 'File'
        const size = entry.vars.uncompressedSize; // There is also compressedSize;

        console.log(type);
        if (type == 'Directory') {
            console.log('[DIR]', fileName, type);
            fs.mkdir(fileName, {
                recursive: true
            }, (err) => {
                if (err) throw err;
            });
            return;
        }

        console.log('[FILE]', fileName, type);
        entry.pipe(fs.createWriteStream(fileName));
        // NOTE: To ignore use entry.autodrain() instead of entry.pipe()
    });