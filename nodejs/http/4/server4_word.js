const fs = require('fs')
const officegen = require('officegen')

module.exports = {
    create_word: async () => {

        //创建word对象
        let docx = officegen('docx');

        docx.on('finalize', function (written) {
            console.log('这里成功创建了一个word文件.')
        })

        docx.on('error', function (err) {
            console.log(err)
        })

        // 创建第一段文字
        let pObj = docx.createP();
        pObj.addText('This is a first text.');
        pObj.addLineBreak();
        pObj.addText('长安一片月，万户捣衣声。');
        pObj.addLineBreak();
        pObj.addText('秋风吹不尽，总是玉关情。');
        pObj.addLineBreak();
        pObj.addText('何日平胡虏，良人罢远征。');
        pObj.addLineBreak();

        // 创建第二段文字，设置颜色
        pObj = docx.createP();
        pObj.addText('This is a two text with color', {
            color: '00FF00'
        })
        pObj.addText(' and back color.', {
            color: '00ffff',
            back: '000088'
        })
        pObj.addText(' and highlight color', {
            highlight: true
        })
        pObj.addText(' and highlight color2', {
            highlight: 'darkGreen'
        })
        pObj.addLineBreak();

        pObj.addText('主人有酒欢今夕，请奏鸣琴广陵客。', {
            color: '00FF00'
        });
        pObj.addLineBreak();
        pObj.addText('月照城头乌半飞，霜凄万木风入衣。', {
            color: '00FFFF'
        });
        pObj.addLineBreak();
        pObj.addText('铜炉华烛烛增辉，初弹渌水后楚妃。', {
            color: '0000FF'
        });
        pObj.addLineBreak();
        pObj.addText('一声已动物皆静，四座无言星欲稀。', {
            color: 'FFFF00'
        });
        pObj.addLineBreak();
        pObj.addText('清淮奉使千余里，敢告云山从此始。', {
            color: 'FF00FF'
        });
        pObj.addLineBreak();

        // 创建第三段文字，设置网络链接
        pObj = docx.createP()
        pObj.addText('This is a three text with ')
        pObj.addText('external link', {
            link: 'https://www.csdn.net'
        })

        // 创建第四段文字，加粗
        pObj = docx.createP()
        pObj.addText('This is a four text with Bold + underline', {
            bold: true,
            underline: true
        })

        // 创建第五段文字，居中
        pObj = docx.createP({
            align: 'center'
        })
        pObj.addText('This is a five text with center this text', {
            border: 'dotted',
            borderSize: 12,
            borderColor: '88CCFF'
        })

        // 创建第六段文字，右对齐
        pObj = docx.createP()
        pObj.options.align = 'right'
        pObj.addText('This is a six text with align this text to the right.')

        // 执行分页操作
        docx.putPageBreak()

        // 创建第七 段文字，
        pObj = docx.createP()
        pObj.addText('言入黄花川，每逐青溪水。', {
            font_face: 'Arial'
        })
        pObj.addText('随山将万转，趣途无百里。', {
            font_face: 'Arial',
            font_size: 40
        })

        // 执行分页操作
        docx.putPageBreak()

        // 创建图片对象，
        pObj = docx.createP()
        pObj.addImage('../assets/test.jpg')
        pObj.addImage('../assets/contributors_1.png')

        // 执行分页操作
        docx.putPageBreak()

        // 添加表格
        let tableStyle = {
            tableColWidth: 2500,
            tableSize: 60,
            tableColor: "blue",
            tableAlign: "center",
            tableVAlign: "center",
            tableFontFamily: "Arial",
            borders: true
        }
        let table = [
            [{
                val: '姓名',
                opts: {
                    align: "center",
                    vAlign: "center",
                    sz: '40',
                }
            }, {
                val: '学校',
                opts: {
                    align: "center",
                    vAlign: "center",
                    sz: '35',
                }
            }, {
                val: '年龄',
                opts: {
                    align: "center",
                    vAlign: "center",
                    sz: '35',
                }
            }]
        ]

        let student1 = ['戈戈', '北京大学', 12]
        let student2 = ['狄狄', '清华大学', 25]
        let student3 = ['可乐', '社会大学', 32]
        table.push(student1, student2)
        docx.createTable(table, tableStyle)

        // 保存docx文件
        let out = fs.createWriteStream('test.docx')

        out.on('error', function (err) {
            console.log(err)
        })

        docx.generate(out)
    }
}