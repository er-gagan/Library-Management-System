function fun1()
{
    var b = document.getElementById("CurrentAddress").value
    $("#gridCheck").change(function(){
        var st = this.checked;
        if(st){    
            $("#PermanentAddress").prop("readonly",true);
            $("#CurrentAddress").prop("readonly",true);
            document.getElementById("PermanentAddress").value=b
        }
        else{
            $("#PermanentAddress").prop("readonly",false);
            $("#CurrentAddress").prop("readonly",false);
            document.getElementById("PermanentAddress").value=""
        }
    });
}