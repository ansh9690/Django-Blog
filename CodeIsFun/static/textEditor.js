var script = document.createElement('script');
script.type = "text/javascript";
script.src = "https://cdn.tiny.cloud/1/rfacfoihsy0aaj593rp0zxulvsz8abg3358f48w77zqyswtk/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

script.onload = function(){
    tinymce.init({
        selector: '#id_content',
    });
}