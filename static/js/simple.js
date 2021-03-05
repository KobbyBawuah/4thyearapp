
var loadingTask = pdfjsLib.getDocument('http://127.0.0.1:5000/send-pdf');
loadingTask.promise.then(function (pdf) {
    console.log(pdf);
    pdf.getPage(1).then(function (page) {
        // you can now use *page* here
        console.log(page);

        var scale = 3;
        var viewport = page.getViewport({ scale: scale, });

        var canvas = document.getElementById('the-canvas');
        var context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        var renderContext = {
            canvasContext: context,
            viewport: viewport
        };
        page.render(renderContext);
    });
});