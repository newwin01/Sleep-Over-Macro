```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
</head>
<body>
    <h2>Get Classes of HTML Element as String using JavaScript</h2>
    <div id="myElement" class="abc xyz pqr">Hello World</div>
    <br>
    <button type="button" onclick="execute()">Click Me</button>
    <script>
    function execute(){
        var element = document.getElementById('myElement');
        var classes = element.className;
        console.log(classes);
    }
    </script>
</body>
</html>
```