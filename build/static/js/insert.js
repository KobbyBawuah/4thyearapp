var x = 0;
var netlistArray = Array();

function add_element_to_array()
{
 netlistArray[x] = document.getElementById("text1").value;
 x++;
 document.getElementById("text1").value = "";
}

function display_array()
{
   var e = "<hr/>";   
    
   for (var y=0; y<netlistArray.length; y++)
   {
     e += "Line " + y + " = " + netlistArray[y] + "<br/>";
   }
   document.getElementById("Result").innerHTML = e;
}

function clear_array()
{
 netlistArray = [];
}