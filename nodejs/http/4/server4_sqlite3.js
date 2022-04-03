// var sqlite3 = require('sqlite3').verbose();
// var db = new sqlite3.Database(':memory:');

// db.serialize(function() {
//   db.run("CREATE TABLE lorem (info TEXT)");

//   var stmt = db.prepare("INSERT INTO lorem VALUES (?)");
//   for (var i = 0; i < 10; i++) {
//       stmt.run("Ipsum " + i);
//   }
//   stmt.finalize();

//   db.each("SELECT rowid AS id, info FROM lorem", function(err, row) {
//       console.log(row.id + ": " + row.info);
//   });
// });

// db.close();

// var fs = require('fs');
// var sqlite3 = require('sqlite3');
// var database_file = __dirname + '/test.db';

// fs.unlink(database_file, function (err) { 
//     //if (err) throw err; 
//     console.log('File deleted!'); 
//  });

// var db = new sqlite3.Database(database_file,function() {
//   db.run("create table t_user(name varchar(15), age int)",function(){
//     db.run("insert into t_user values('爱看书的小沐', 16)",function(){
//       db.all("select * from t_user",function(err,res){
//         if(!err)
//           console.log(JSON.stringify(res));
//         else
//           console.log(err);
//       });
//     })
//   });
// });
// db.close();

var fs = require('fs');
var sqlite3 = require('sqlite3');
var db_file = __dirname + '/test.db';

fs.unlink(db_file, function (err) {
    //if (err) throw err; 
    console.log('File deleted!');
});
var db = new sqlite3.Database(db_file, function (err) {
    // if (err) throw err;
});
//也可以使用内存型，数据不会永久保存
// db = new sqlite3.Database(":memory:", function (err) {
//     if (err) throw err;
// });

db.run(`create table t_user(id INT,name VARCHAR,age INT)`, function (err) {
    // if (err) throw err;
    console.log("Create Table Success!");
});

//增
db.run("INSERT INTO t_user VALUES(1, '爱看书的小沐', 16);", function (err) {
    if (err) throw err;
    console.log("Insert Data Success!");
});

// var sql = "";
// for (var i = 0; i < 10; i++) {
//     sql += "INSERT INTO t_user VALUES(" + i + ", 'hello', 16);";
// }
// db.exec(sql, function (err) {
//     if (err) throw err;
//     console.log("Insert Data Success!");
// });

// //删
// var sql2 = db.prepare("delete from t_user where id = 1");
// sql2.run();

// //改
// var sql3 = db.prepare("update t_user set name = winston where id = 1");
// sql3.run();

// //查
// db.all("select * from t_user", function (err, row) {
//     console.log(JSON.stringify(row));
// })

// //查一条数据
// db.each("select * from t_user", function (err, row) {
//     console.log(row);
// })

// db.close();

// Run Create Table
db.run(`create table t_user (id INT,name VARCHAR,password VARCHAR)`, function (
    err
) {
    if (err) throw err;
    console.log("Create Table Success!");
});

// Run Insert Data
db.run(`insert into t_user values (1,"admin","admin")`, function (err) {
    if (err) throw err;
    console.log("Insert Data Success!");
});

// Run Update Data
db.run(`update t_user set name = "admin123" WHERE id = 1`, function (err) {
    if (err) throw err;
    console.log("Update Data Success!");
});

// Run Delete Data
db.run(`delete from t_user WHERE id = 1`, function (err) {
    if (err) throw err;
    console.log("Delete Data Success!");
});

// Run Drop Table
db.run(`drop table t_user`, function (err) {
    if (err) throw err;
    console.log("Drop Table Success!");
});