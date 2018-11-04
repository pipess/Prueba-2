function Registro(){
            var nombre=document.getElementById("id_nombre").value;
	 		var telefono=document.getElementById("id_telefono").value;
            var correo=document.getElementById("id_correo").value;
            var run=document.getElementById("id_run").value;
			
            
            var patron = /^[a-zA-Z]*$/;
            var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
            
            if (/^([0-9]{8})$/i.test(telefono)  )
                {
               
 document.getElementById("id_telefono").style.color = "green";
                
                     
                }
            else{
                document.getElementById("id_telefono").focus();
                document.getElementById("id_telefono").style.color = "red";
                alert("telefono fuera de rango");
                
            }
    
           
            
            if (/^([0-9]{8})$/i.test(run)  )
                {
               
 document.getElementById("id_run").style.color = "green";
                
                     
                }
            else{
                document.getElementById("id_run").focus();
                document.getElementById("id_run").style.color = "red";
                alert("run fuera de rango");
                
            }
            
            if (!nombre.search(patron) && nombre.length>=3 && nombre.length<=40)
            {
                document.getElementById("id_nombre").style.color = "green";
               
            }
            else{
                document.getElementById("id_nombre").focus();
                document.getElementById("id_nombre").style.color = "red";
                alert("nombre fuera de rango");
            }
    
    
            if (regex.test(correo)) {
                document.getElementById("id_correo").style.color = "green";

            } else {
                     document.getElementById("id_correo").focus();
                document.getElementById("id_correo").style.color = "red";
                alert("id_correo fuera de rango");

        
    }
    
            
    
               
     
            
}