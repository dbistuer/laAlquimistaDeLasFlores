
function setProgressBar(progressbar, value,class_name){
    progressbar.style["width"] = value + "%";
    progressbar.setAttribute("aria-valuenow",value);
    progressbar.innerHTML = value + "%";
    progressbar.classList.remove("bg-danger","bg-warning","bg-info","bg-success");
    progressbar.classList.add(class_name);
}

function setProgressBarPercents(maxPercent, value, progressbar){
    percent = 100/maxPercent;
    percent = percent * value;
    if(percent >= 0 && percent <= 40)
        setProgressBar(progressbar,percent,"bg-danger");
    else if(percent > 40 && percent <= 80)
        setProgressBar(progressbar,percent,"bg-warning");
    else if(percent > 80 && percent <= 100)
        setProgressBar(progressbar,percent,"bg-success");
}

