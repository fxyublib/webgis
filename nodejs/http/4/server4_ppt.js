const officegen = require('officegen')
const http = require('http')

/**
 * This is a simple web server that response with a PowerPoint document.
 */
http.createServer(function(req, res) {
  // We'll send a generated on the fly PowerPoint document without using files:
  if (req.url == '/') {
    // Create an empty PowerPoint object:
    let pptx = officegen('pptx')

    // Let's create a new slide:
    var slide = pptx.makeNewSlide()

    slide.name = 'Hello World'

    // Change the background color:
    slide.back = '000000'

    // Declare the default color to use on this slide:
    slide.color = 'ffffff'

    // Basic way to add text string:
    slide.addText('Created on the fly using a http server!')

    //
    // Let's generate the PowerPoint document directly into the response stream:
    //

    res.writeHead(200, {
      'Content-Type':
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
      'Content-disposition': 'attachment filename=out-' + new Date().getTime() + '.pptx'
    })

	// Content types related to Office documents:
    // .xlsx   application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
    // .xltx   application/vnd.openxmlformats-officedocument.spreadsheetml.template
    // .potx   application/vnd.openxmlformats-officedocument.presentationml.template
    // .ppsx   application/vnd.openxmlformats-officedocument.presentationml.slideshow
    // .pptx   application/vnd.openxmlformats-officedocument.presentationml.presentation
    // .sldx   application/vnd.openxmlformats-officedocument.presentationml.slide
    // .docx   application/vnd.openxmlformats-officedocument.wordprocessingml.document
    // .dotx   application/vnd.openxmlformats-officedocument.wordprocessingml.template
    // .xlam   application/vnd.ms-excel.addin.macroEnabled.12
    // .xlsb   application/vnd.ms-excel.sheet.binary.macroEnabled.12

    // This one catch only the officegen errors:
    pptx.on('error', function(err) {
      res.end(err)
    })

    // Catch response errors:
    res.on('error', function(err) {
      res.end(err)
    })

    // End event after sending the PowerPoint data:
    res.on('finish', function() {
      res.end()
    })

    // This async method is working like a pipe - it'll generate the pptx data and pass it directly into the output stream:
    pptx.generate(res)
  } else {
    res.end('Invalid Request!')
  } // Endif.
}).listen(3000)