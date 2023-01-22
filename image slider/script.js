// add extra images names to this array with web/ and index
const images = ['web/img1.jpg', 'web/img2.jpg', 'web/img3.jpg', 'web/img4.jpg']
const photo = document.querySelector('.photo')
var num = 0;
function nextImage() {
    num++;
    if (num <= 3) {
        photo.setAttribute('src', images[num])
    }
    else {
        num = 0;
        photo.setAttribute('src', images[num])
    }
}
function prvImage() {
    num--;
    if (num == -1) {
        num = 3;

        photo.setAttribute('src', images[num])
    }
    photo.setAttribute('src', images[num])
}
var str=`hello my dear programmer${num}`
