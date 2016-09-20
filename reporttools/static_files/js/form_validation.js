function populate(product) {
    alert(product)





}
function validateForm() {
    var aid = document.getElementById('aid').value;
    var ftime = document.getElementById('f_time').value;
    var ttime = document.getElementById('t_time').value;

    
    if ( aid == null || aid == "") {
        alert("analyzerid must not be empty");
        return false;
    }
    if( ftime == null || ftime== "" ) {
        alert("Fill in the from time")
        return false;
    }
    if(ttime== null || ttime== "" ) {
        alert("Fill in the to time")
        return false;
    }
    
    var f = new Date(ftime).getTime()/1000;
    var t = new Date(ttime).getTime()/1000;

    if( ((t-f) > 7200) ||  ((t-f) < 0 )) {
        alert("time provides is either out of range(2 Hrs Max Limit) or to time is less than from time")
        return false;
    }

}



