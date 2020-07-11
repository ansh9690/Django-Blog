<script
    type="text/javascript"
    src="https://cdn.tiny.cloud/1/rfacfoihsy0aaj593rp0zxulvsz8abg3358f48w77zqyswtk/tinymce/5/tinymce.min.js"
    referrerpolicy="origin">
  </script>
  <script type="text/javascript">
  tinymce.init({
    selector: '#id_content',
    width: 600,
    height: 300,
    plugins: [
      'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
      'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
      'table emoticons template paste help'
    ],
    toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
      'bullist numlist outdent indent | link image | print preview media fullpage | ' +
      'forecolor backcolor emoticons | help',
    menu: {
      favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | spellchecker | emoticons'}
    },
    menubar: 'favs file edit view insert format tools table help',
    content_css: 'css/content.css'
  });
</script>