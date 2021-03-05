var netlistArray = Array();
var valueArray = Array();

function add_element_to_array()
{
    var text = document.getElementById("text1").value.trim();
    document.getElementById("text1").value = "";
    if (text.length == 0)
    {
        return;
    }
    netlistArray.push(text);
    display_array();
}

function add_element_to_array2() {
    var text = document.getElementById("text2").value.trim();
    document.getElementById("text2").value = "";
    if (text.length == 0) {
        return;
    }
    valueArray.push(text);
    display_array2();
}

function display_array()
{
    var e = "<hr/>";
   for (var y=0; y<netlistArray.length; y++)
   {
     e += netlistArray[y] + "<br/>";
   }
   document.getElementById("Result").innerHTML = e;
}

function display_array2() {
    var e = "<hr/>";
    for (var y = 0; y < valueArray.length; y++) {
        e += valueArray[y] + "<br/>";
    }
    document.getElementById("Result2").innerHTML = e;
}

function clear_array()
{
    netlistArray = [];
    display_array();
}

function clear_array2() {
    valueArray = [];
    display_array2();
}

function remove_array() {
    netlistArray.pop();
    display_array();
}

function remove_array2() {
    valueArray.pop();
    display_array2();
}

function solve() {
    var dataObj = {
        netlistArray: netlistArray,
        valueArray: valueArray
    };

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // Typical action to be performed when the document is ready:
            // document.getElementById("demo").innerHTML = xhttp.responseText;
            window.location.href = "/run";
        }
    };
    xhttp.open("POST", "/simulate", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(dataObj));
}

function getPdf() {
    console.log('In get pdf function');

    var loadingTask = pdfjsLib.getDocument('http://127.0.0.1:5000/send-pdf');
    loadingTask.promise.then(function (pdf) {
        console.log(pdf);
        pdf.getPage(1).then(function (page) {
            // you can now use *page* here
            console.log(page);
           
            var scale = 1.5;
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
}