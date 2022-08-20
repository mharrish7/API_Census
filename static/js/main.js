

var keyp = 1;
var keye = 1;

$(document).ready(function(){
    

    let u = this;
    $.ajax({
        url: '/loads',
            data: {
                st: 's'
            },
            type: 'POST'
        }).done(function (data) {
            if (data['data'] == 1) {
                console.log('ssd');
                u.style.display = 'none';
                document.querySelector('.popimg').src = "static/images/population" + keyp + ".jpg";
                document.querySelector('.eleimg').src = "static/images/elevation" + keye + ".jpg";
                setTimeout(help,100);
            }
    
        });
    
    
})

function help(){
    document.querySelector('.popimg').src = "static/images/population" + keyp + ".jpg";
    document.querySelector('.eleimg').src = "static/images/elevation" + keye + ".jpg";
}


$('.pchange').on('click',function(ev){
    keyp +=1 ;
    if(keyp>3){
        keyp = 1;
    }
    document.querySelector('.popimg').src = "static/images/population" + keyp + ".jpg";
})

$('.echange').on('click',function(ev){
    keye +=1 ;
    if(keye>3){
        keye = 1;
    }
    document.querySelector('.eleimg').src = "static/images/elevation" + keye + ".jpg";
})