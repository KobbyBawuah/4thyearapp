var array = Array();

function add_element_to_array()
{
    var text = document.getElementById("text1").value.trim();
    document.getElementById("text1").value = "";
    if (text.length == 0)
    {
        return;
    }
    array.push(text);
    display_array();
}

function display_array()
{
    var e = "<hr/>";
   for (var y=0; y<array.length; y++)
   {
     e += array[y] + "<br/>";
   }
   document.getElementById("Result").innerHTML = e;
}

function clear_array()
{
    array = [];
    display_array();
}

function solve() {
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
    xhttp.send(JSON.stringify(array));
}