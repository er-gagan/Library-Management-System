function fun1()
{
    var b = document.getElementById("CurrentAddress").value
    $("#gridCheck").change(function(){
        var st = this.checked;
        if(st){
            $("#PermanentAddress").prop("disabled",true);
            $("#CurrentAddress").prop("disabled",true);
            document.getElementById("PermanentAddress").value=b
        }
        else{
            $("#PermanentAddress").prop("disabled",false);
            $("#CurrentAddress").prop("disabled",false);
            document.getElementById("PermanentAddress").value=""
        }
    });
}