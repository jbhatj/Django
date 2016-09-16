
function validateForm() {
    var aid = document.getElementById["aid"].value;
    var ftime = document.getElementById["f_time"].value;
    var ttime = document.getElementById["t_time"].value;

    prompt("this is emergency");
    
    if (aid == null || aid == "") {
        alert("analyzerid must not be empty");
        return false;
    }
    if(ftime == null || ftime== "" ) {
        alert("Fill in the from time")
        return false;
    }
    if(ttime == null || ttime== "" ) {
        alert("Fill in the to time")
        return false;
    }

}
