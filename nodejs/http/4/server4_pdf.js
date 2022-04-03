const { PDFDocument, StandardFonts, rgb } = require('pdf-lib');
const fs = require('fs');

run().catch(err => console.log(err));

async function run() {
    // Create a new document and add a new page
    const doc = await PDFDocument.create();
    const page = doc.addPage();

    // Load the image and store it as a Node.js buffer in memory
    let img = fs.readFileSync('./contributors_1.png');
    img = await doc.embedPng(img);

    // Draw the image on the center of the page
    const {
        width,
        height
    } = img.scale(0.1);
    page.drawImage(img, {
        x: 10,
        y: page.getHeight() - height - 10,
        width,
        height
    });

    // Draw the text on the top of the page
    const helveticaFont = await doc.embedFont(StandardFonts.Helvetica);
    page.setFont(helveticaFont)

    page.moveTo(5, 200)
    page.drawText('The Life of an Egg', {
        size: 36
    })

    page.moveDown(36)
    page.drawText('An Epic Tale of Woe', {
        size: 30
    })

    page.drawText(
        `Humpty Dumpty sat on a wall \n` +
        `Humpty Dumpty had a great fall; \n` +
        `All the king's horses and all the king's men \n` +
        `Couldn't put Humpty together again. \n`, {
            x: 25,
            y: 100,
            font: helveticaFont,
            size: 24,
            color: rgb(1, 0, 0),
            lineHeight: 24,
            opacity: 0.75,
        },
    );

    // Write the PDF to a file
    fs.writeFileSync('./test.pdf', await doc.save());
}