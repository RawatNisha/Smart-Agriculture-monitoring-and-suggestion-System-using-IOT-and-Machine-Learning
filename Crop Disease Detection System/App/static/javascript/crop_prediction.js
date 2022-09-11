function updateFileName(event) {
    console.log("file changed");
    let file=document.getElementById('file').files[0];
    let file_name=document.getElementById("file_name")
    if (!!file) {
        file_name.innerHTML=file.name;
    }else{
        file_name.innerHTML="Select Crop Image";
    }
    console.log(file);
}




async function SubmitFile(event) {
    let file=document.getElementById('file').files[0];
    let file_name=document.getElementById("file_name")



    document,getElementById('output_container').style.display='flex'
}