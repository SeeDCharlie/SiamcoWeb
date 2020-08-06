function captureDoc() {

    const $objetivo = document.querySelector("#cotDoc"), // A qué le tomamos la foto
        $contenedorCanvas = document.querySelector("#tocanvas");

    var w = document.getElementById("cotDoc").offsetWidth;
    var h = document.getElementById("cotDoc").offsetHeight;
    //alert("cap alv 2");

    html2canvas($objetivo) // Llamar a html2canvas y pasarle el elemento
        .then(canvas => {
            var img = canvas.toDataURL("image/jpeg", 1);
            $contenedorCanvas.appendChild(img);
            /*var doc = new jsPDF('L', 'px', [w, h]);
            doc.addImage(img, 'JPEG', 0, 0, w, h);
            doc.save('sample-file.pdf');*/
        });
}


function generateCot() {

    var doc = new jsPDF('p', 'mm', 'a4');
    doc.text(20, 20, 'Hello world!');
    //doc.addImage(getPage('#pageOne'), 'PNG', 0, 0, 500, 600);
    doc.text(20, 30, 'This is client-side Javascript, pumping out a PDF.');
    doc.addPage();
    doc.text(20, 20, 'Do you like that?');

    doc.save('Test.pdf');

}

function getPage(namePage) {

    html2canvas(document.getElementById('#pageOne'), {

        onrendered: function (canvas) {
            var img = canvas.toDataURL("image/png", 1);
            return img;
        }
    });
}


$("button").click(function (e) {


    //alert("seoprimio el botongenerar!!");

    captureDoc();


});