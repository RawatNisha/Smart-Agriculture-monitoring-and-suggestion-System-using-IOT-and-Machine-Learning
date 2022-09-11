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
    event.preventDefault();
    let loader = document.getElementById("loader");
    loader.style.display = "flex";
    console.log("submitted");
    let file = document.getElementById("file").files[0];
    let filename = document.getElementById("file_Name");
    let inputContainer = document.getElementById("input_container");
    let outputContainer = document.getElementById("output_container");
    let image = document.getElementById("image");
    let detectionresult=document.getElementById('detectionresult')
    if (!!file) {
        console.log(file);
        let filename = file.name;
        console.log(filename);
        let extention = file.name.split(".")[file.name.split(".").length - 1];
        console.log(extention);
        if (
            extention.toLowerCase() == "jpg" ||
            extention.toLowerCase() == "png"
        ) {
            console.log("extension accepted");
            if (file.size < 10000000) {
                try {
                    let formData = new FormData();
                    formData.append("file", file ? file : "");
                    let response = await fetch("/upload", {
                        method: "POST",
                        body: formData,
                    });
                    console.log(response);
                    let data = await response.json();
                    // console.log(data);
                    if (!!data.image_path) {
                        loader.style.display = "none";
                        inputContainer.style.display = "none";
                        outputContainer.style.display = "flex";
                        // console.log(data.image_path);
                        image.src = data.image_path;
                        // console.log(image);
                        try {
                            let outputResponse= await fetch('/getresult',{
                                method:"POST"
                            });
                            console.log(outputResponse);
                            let result=await outputResponse.json();
                            console.log(result);
                            console.log(result.data);
                            if (!!result.data) {
                                detectionresult.innerHTML=result.data
                            }
                            else{
                                window.alert("Some Error Occured")
                            }
                        } catch (error) {
                            console.log(error);
                        }
                    } else {
                        window.alert("some error occured")
                    }
                } catch (error) {
                    console.log(error);
                }
            } else {
                window.alert("more than 10 mb is mot allowed");
            }
        } else {
            window.alert("extension not allowed");
        }
    } else {
        window.alert("Please Select File Frst");
    }
    // setTimeout(() => {
        loader.style.display = "none";
    // }, 1000);
}